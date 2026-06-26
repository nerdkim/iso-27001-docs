#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deterministic builder: parse docs/ and regenerate every derived index in this repository.

docs/ is the authoritative corpus and is read-only here; this script never writes into it
except for the generated per-language INDEX.md navigation files.

Inputs
  extended/catalog/controls.json            control numbers/titles/themes (the public Annex A list)
  docs/{ko,en}/<theme-dir>/<no>.md          the explanatory documents (original material)

Outputs
  extended/manifest.json                    corpus manifest (schema corpus-manifest/v3).
                                            This file is the published contract that downstream
                                            consumers (the web viewer, AI agents) read.
  extended/index/control-index.csv          flat index for spreadsheet/human review
  extended/index/nonconformity-rulebook.json  Korean nonconformity-case rulebook (93 controls)
  extended/index/evidence-dictionary.json   Korean evidence-example dictionary (93 controls)
  docs/{ko,en}/INDEX.md                     human-facing table of contents

Copyright boundary: control numbers, titles, and the four-theme classification come from the
public list of ISO/IEC 27001:2022 Annex A. The explanatory bodies parsed here are this
repository's own original material, not the normative text of the standard.

Usage: python3 tools/build_index.py
"""
import csv
import glob
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
EXT = os.path.join(ROOT, "extended")
IDX = os.path.join(EXT, "index")
CATALOG = os.path.join(EXT, "catalog", "controls.json")

LANGS = ("ko", "en")
THEME_ORDER = ["organizational", "people", "physical", "technological"]

# Section headings counted per item, by language. ISO controls carry no "related laws"
# section (that is an ISMS-P concept), so the laws bucket stays empty here.
SECTIONS = {
    "ko": {"checkpoints": ["주요 확인사항"], "evidence": ["증적자료"], "defects": ["부적합 사례"]},
    "en": {
        "checkpoints": ["Key checkpoints"],
        "evidence": ["Evidence"],
        "defects": ["Nonconformity examples"],
    },
}

# The six-section document structure, published so consumers can validate a document.
ITEM_SECTIONS = {
    "ko": ["통제 목적", "주요 확인사항", "이행 지침", "관련 통제 및 속성", "증적자료", "부적합 사례"],
    "en": [
        "Control objective",
        "Key checkpoints",
        "Implementation guidance",
        "Related controls and attributes",
        "Evidence",
        "Nonconformity examples",
    ],
}

STANDARD_LABEL = {"ko": "ISO/IEC 27001:2022 Annex A", "en": "ISO/IEC 27001:2022 Annex A"}
STANDARD_BLURB = {
    "ko": "ISO/IEC 27001:2022 Annex A는 4개 테마(조직적/인적/물리적/기술적) 93개 정보보안 통제 목록입니다.",
    "en": (
        "ISO/IEC 27001:2022 Annex A is a list of 93 information security controls across four "
        "themes (Organizational, People, Physical, Technological)."
    ),
}
PROVENANCE = {
    "ko": (
        "통제 번호/명칭/테마 분류는 ISO/IEC 27001:2022 Annex A의 공개 목록에 근거합니다. 설명 본문은 "
        "본 자료집이 새로 작성한 원저작이며 ISO 표준 원문의 규범 텍스트가 아닙니다. 정본 대조는 "
        "라이선스된 표준 원문으로 하십시오."
    ),
    "en": (
        "Control numbers, titles, and theme classification are based on the public list of "
        "ISO/IEC 27001:2022 Annex A. The explanatory text is original material and is not the "
        "normative text of the ISO standard. For an authoritative check, use a licensed copy of "
        "the standard."
    ),
}


# ---------------------------------------------------------------------------
# Markdown parsing helpers
# ---------------------------------------------------------------------------
def section_body(text, title):
    """Return the body of the '## <title>' section, up to the next '## ' or '---'."""
    m = re.search(
        r"(?m)^##\s+" + re.escape(title) + r"\b[^\n]*\n(.*?)(?=\n##\s|\n---|\Z)", text, re.S
    )
    return m.group(1).strip() if m else ""


def first_section_body(text, titles):
    for t in titles:
        body = section_body(text, t)
        if body:
            return body
    return ""


def bullets(text):
    """Top-level '- ' bullets, skipping italic placeholder lines such as _(none)_."""
    out = []
    for line in text.split("\n"):
        s = line.strip()
        if s.startswith("- "):
            v = s[2:].strip()
            if v and not (v.startswith("_") and v.endswith("_")):
                out.append(v)
    return out


def numbered(text):
    return [
        re.sub(r"^\d+\.\s*", "", line.strip())
        for line in text.split("\n")
        if re.match(r"^\d+\.\s", line.strip())
    ]


def control_sort_key(no):
    return [int(n) for n in no.replace("A.", "").split(".")]


# ---------------------------------------------------------------------------
def parse_item(path, lang, themes, by_no, dir_theme):
    rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
    theme_dir = rel.split("/")[2]  # docs / <lang> / <theme-dir> / <no>.md
    theme_key = dir_theme.get(theme_dir, "")
    theme = themes.get(theme_key, {})
    no = os.path.splitext(os.path.basename(path))[0]
    catalog_entry = by_no.get(no, {})
    name = catalog_entry.get("title_ko" if lang == "ko" else "title_en", no)

    text = open(path, encoding="utf-8").read()
    sec = SECTIONS[lang]
    checks = numbered(first_section_body(text, sec["checkpoints"]))
    evidence = bullets(first_section_body(text, sec["evidence"]))
    defects = bullets(first_section_body(text, sec["defects"]))
    theme_label = theme.get("label_ko" if lang == "ko" else "label_en", theme_key)

    return {
        "lang": lang,
        "section": theme_key,
        "no": no,
        "name": name,
        # ISO navigates by theme, so the theme is both the group and the section.
        "groupNo": theme.get("no", ""),
        "group": theme_label,
        "subgroupNo": "",
        "subgroup": "",
        "appliesTo": [],
        "path": rel,
        "counts": {
            "checkpoints": len(checks),
            "evidence": len(evidence),
            "defects": len(defects),
            "hasLaws": False,
        },
        "_evidence": evidence,
        "_defects": defects,
    }


def collect(lang, themes, by_no, dir_theme):
    files = [
        f
        for f in glob.glob(os.path.join(DOCS, lang, "**", "*.md"), recursive=True)
        if os.path.basename(f) != "INDEX.md"
    ]
    items = [parse_item(f, lang, themes, by_no, dir_theme) for f in files]
    items.sort(
        key=lambda x: (
            THEME_ORDER.index(x["section"]) if x["section"] in THEME_ORDER else len(THEME_ORDER),
            control_sort_key(x["no"]),
        )
    )
    return items


# ---------------------------------------------------------------------------
def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def build_docs_index(items, lang, themes):
    base = f"docs/{lang}"
    heading = "ISO/IEC 27001:2022 Annex A" + (" (한국어)" if lang == "ko" else " (English)")
    if lang == "ko":
        total_line = f"총 {len(items)}개 통제 (조직 37 / 인적 8 / 물리 14 / 기술 34)."
        note = "> 통제 번호/명칭/테마는 공개 목록 근거. 설명 본문은 원저작이며 표준 원문이 아닙니다."
    else:
        total_line = (
            f"{len(items)} controls in total (Organizational 37 / People 8 / Physical 14 / "
            "Technological 34)."
        )
        note = (
            "> Numbers/titles/themes are from the public list. Explanatory text is original "
            "material, not the standard."
        )
    lines = [f"# {heading}", "", total_line, "", note, ""]
    for key in THEME_ORDER:
        lst = [it for it in items if it["section"] == key]
        if not lst:
            continue
        theme = themes[key]
        label = theme["label_ko" if lang == "ko" else "label_en"]
        lines += [f"## {theme['no']} {label} ({len(lst)})", ""]
        for it in lst:
            href = os.path.relpath(os.path.join(ROOT, it["path"]), os.path.join(ROOT, base))
            lines.append(f"- [{it['no']} {it['name']}]({href})")
        lines.append("")
    return write(f"{base}/INDEX.md", "\n".join(lines).rstrip() + "\n")


# ---------------------------------------------------------------------------
def main():
    catalog = json.load(open(CATALOG, encoding="utf-8"))
    themes = catalog["themes"]
    by_no = {c["no"]: c for c in catalog["controls"]}
    dir_theme = {v["dir"]: k for k, v in themes.items()}

    per_lang = {lang: collect(lang, themes, by_no, dir_theme) for lang in LANGS}

    def public(it):
        return {k: v for k, v in it.items() if not k.startswith("_")}

    all_items = [public(it) for lang in LANGS for it in per_lang[lang]]

    def theme_count(key, lang):
        return sum(1 for it in per_lang[lang] if it["section"] == key)

    sections = [
        {
            "id": key,
            "slug": themes[key]["dir"],
            "no": themes[key]["no"],
            "label": {"ko": themes[key]["label_ko"], "en": themes[key]["label_en"]},
            "count": {lang: theme_count(key, lang) for lang in LANGS},
        }
        for key in THEME_ORDER
    ]

    counts = {lang: len(per_lang[lang]) for lang in LANGS}
    counts["total"] = len(all_items)
    manifest = {
        "schema": "corpus-manifest/v3",
        "description": (
            "Machine-readable index of the ISO/IEC 27001:2022 Annex A reference corpus in this "
            "repository. Consumers locate, cite, and render items from this file."
        ),
        "standard": {
            "id": "iso-27001",
            "label": STANDARD_LABEL,
            "blurb": STANDARD_BLURB,
            "nav": "themes",
            "langs": list(LANGS),
            "sections": sections,
            "source": {lang: catalog.get("source_note", "") for lang in LANGS},
            "provenance": PROVENANCE,
            "itemSections": ITEM_SECTIONS,
        },
        "counts": counts,
        "items": all_items,
    }
    os.makedirs(IDX, exist_ok=True)
    with open(os.path.join(EXT, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
        f.write("\n")

    with open(os.path.join(IDX, "control-index.csv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "lang", "theme", "theme_no", "no", "name",
                "n_checkpoints", "n_evidence", "n_nonconformity_cases", "path",
            ]
        )
        for lang in LANGS:
            for it in per_lang[lang]:
                c = it["counts"]
                w.writerow(
                    [
                        it["lang"], it["section"], it["groupNo"], it["no"], it["name"],
                        c["checkpoints"], c["evidence"], c["defects"], it["path"],
                    ]
                )

    ko = per_lang["ko"]
    rulebook = {
        "schema": "iso-27001-nonconformity-rulebook/v1",
        "description": (
            "Nonconformity-case rulebook for the 93 Annex A controls. Source of check rules for "
            "self-assessment and internal audit preparation. Original material, not the standard."
        ),
        "total_nonconformity_cases": sum(len(it["_defects"]) for it in ko),
        "items": {
            it["no"]: {
                "name": it["name"],
                "theme": f"{it['groupNo']} {it['group']}",
                "path": it["path"],
                "cases": it["_defects"],
            }
            for it in ko
        },
    }
    evidence = {
        "schema": "iso-27001-evidence-dictionary/v1",
        "description": (
            "Evidence-example dictionary for the 93 Annex A controls. Reference dictionary for "
            "evidence-to-control mapping. Original material, not the standard."
        ),
        "total_evidence_examples": sum(len(it["_evidence"]) for it in ko),
        "items": {
            it["no"]: {
                "name": it["name"],
                "theme": f"{it['groupNo']} {it['group']}",
                "path": it["path"],
                "evidence": it["_evidence"],
            }
            for it in ko
        },
    }
    for name, payload in (
        ("nonconformity-rulebook.json", rulebook),
        ("evidence-dictionary.json", evidence),
    ):
        with open(os.path.join(IDX, name), "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=1)
            f.write("\n")

    written = [build_docs_index(per_lang[lang], lang, themes) for lang in LANGS]

    print(f"manifest v3: {counts['total']} items  {json.dumps(counts, ensure_ascii=False)}")
    print(
        f"nonconformity-rulebook: {rulebook['total_nonconformity_cases']} cases / {len(ko)} "
        "controls (ko)"
    )
    print(
        f"evidence-dictionary: {evidence['total_evidence_examples']} examples / {len(ko)} "
        "controls (ko)"
    )
    for w in written:
        print("wrote", w)


if __name__ == "__main__":
    main()
