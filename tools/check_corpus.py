#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Corpus integrity checks for this repository. Read-only: nothing is written.

Checks
  [1] manifest present and self-consistent (counts match the item list)
  [2] Korean and English mirror each other exactly, keyed by (theme, control number)
  [3] every control document carries the six required sections, in order
  [4] the H1 heading carries the control number that matches the file name
  [5] every control document ends with a source/limitation footer
  [6] every path recorded in the manifest exists on disk, no document on disk is missing
      from the manifest, and every control in the catalog has a document in both languages
  [7] the Korean and English documents for a control carry the same number of items in each
      counted section, so a structural one-language edit cannot land on its own
  [8] every 'A.x.y (title)' cross-reference reproduces that control's title from the catalog,
      and carries the parenthesised title form so that it cannot escape that comparison
  [9] the metadata table carries the expected rows, and the control-type and security-property
      values agree between the two languages
 [10] every ISO main-body clause citation carries a parenthesised clause title, and one clause
      number is cited under one title across the whole corpus, per language

Exit code 0 when the corpus is intact, 1 otherwise.

Usage: python3 tools/check_corpus.py
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
MANIFEST = os.path.join(ROOT, "extended", "manifest.json")
CATALOG = os.path.join(ROOT, "extended", "catalog", "controls.json")

LANGS = ("ko", "en")

REQUIRED_SECTIONS = {
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

problems = []


def fail(msg):
    problems.append(msg)


def headings(text):
    return [m.group(1).strip() for m in re.finditer(r"(?m)^##\s+(.+)$", text)]


def check_document(path, lang):
    rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
    text = open(path, encoding="utf-8").read()

    # [4] H1 carries the control number, and it matches the file name.
    expected_no = os.path.splitext(os.path.basename(path))[0]
    first = text.split("\n", 1)[0]
    m = re.match(r"^#\s+(A\.\d+\.\d+)\s+\S", first)
    if not m:
        fail(f"{rel}: first line is not a '# <no> <title>' heading")
    elif m.group(1) != expected_no:
        fail(f"{rel}: H1 control number {m.group(1)} does not match the file name {expected_no}")

    # [3] the six required sections, in order.
    found = headings(text)
    cursor = 0
    for title in REQUIRED_SECTIONS[lang]:
        while cursor < len(found) and not found[cursor].startswith(title):
            cursor += 1
        if cursor == len(found):
            fail(f"{rel}: missing or out-of-order section '{title}'")
            break
        cursor += 1

    # [5] source/limitation footer. It carries the copyright boundary, so it is mandatory.
    if not re.search(r"(?m)^---\s*\n>\s*\S", text):
        fail(f"{rel}: missing the trailing source/limitation footer ('---' followed by a '>' line)")

    # [10] ISO main-body clause citations: uniform form, and one title per clause number.
    check_clause_citations(rel, lang, text)


COUNTED_SECTIONS = {
    "ko": ["주요 확인사항", "이행 지침", "증적자료", "부적합 사례"],
    "en": ["Key checkpoints", "Implementation guidance", "Evidence", "Nonconformity examples"],
}
META_ROWS = {
    "ko": ["표준", "테마", "통제", "통제 유형(참고)", "보안 속성(참고)", "ISMS-P 대응", "2013 대응"],
    "en": ["Standard", "Theme", "Control", "Control type (ref.)",
           "Security properties (ref.)", "ISMS-P mapping", "2013 mapping"],
}
XREF_MARKER = {"ko": "인접 Annex A:", "en": "Adjacent Annex A:"}
CLAUSE_MARKER = {"ko": "ISO 27001 본문 연계:", "en": "ISO 27001 clauses:"}
# One clause number, or a slash-joined group of them, followed by a parenthesised clause title.
CLAUSE_CITE_RE = re.compile(r"\d+(?:\.\d+){0,2}(?:\s*/\s*\d+(?:\.\d+){0,2})*\s*[(（]")
# A clause number not preceded or followed by a word char or dot, so the 'A.7.10' of an Annex A
# reference in a trailing note is never mistaken for main-body clause 7.10.
CLAUSE_NO_RE = re.compile(r"(?<![\w.])\d+(?:\.\d+){0,2}(?![\w.])")
# lang -> clause number -> title -> the documents citing it that way. Filled per document, judged
# once at the end, because a title can only be inconsistent relative to the rest of the corpus.
clause_titles = {"ko": {}, "en": {}}
TYPE_KO = {"예방적": "Preventive", "탐지적": "Detective", "교정적": "Corrective"}
PROP_KO = {"기밀성": "Confidentiality", "무결성": "Integrity", "가용성": "Availability"}
# A range such as "A.5.24~A.5.28(...)" carries a group label, not one control's title.
RANGE_RE = re.compile(r"A\.\d+\.\d+\s*(?:[~\-]|\s+to\s+)\s*A\.\d+\.\d+\s*[(（]")


def read(path):
    return open(path, encoding="utf-8").read()


def section_items(text, title):
    m = re.search(r"(?m)^##\s+" + re.escape(title) + r"\s*$(.*?)(?=^##\s|\n---\n|\Z)", text, re.S)
    if not m:
        return None
    return len([l for l in m.group(1).split("\n") if re.match(r"^\s*(?:-|\d+\.)\s", l)])


def meta_rows(text):
    return {k.strip(): v.strip()
            for k, v in re.findall(r"(?m)^\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*$", text)}


def attr_tokens(cell):
    return [x.strip() for x in re.split(r"[/,]", re.sub(r"\([^)]*\)", "", cell)) if x.strip()]


def close_paren(s, i):
    opener = s[i]
    closer = ")" if opener == "(" else "）"
    depth = 0
    for j in range(i, len(s)):
        if s[j] == opener:
            depth += 1
        elif s[j] == closer:
            depth -= 1
            if depth == 0:
                return j
    return None


def check_clause_citations(rel, lang, text):
    """[10] every ISO main-body clause citation names the clause, in one uniform form.

    The parenthesis is the clause-title slot and carries the title alone. Without the form rule a
    citation could be written bare ('9.1 Monitoring, measurement, analysis and evaluation'), which
    is ambiguous in a comma-separated list and is how three documents came to cite a clause under
    the wrong title. Glosses go in the body of the document, not in this slot.
    """
    for line in text.split("\n"):
        if CLAUSE_MARKER[lang] not in line:
            continue
        body = line.split(CLAUSE_MARKER[lang], 1)[1]
        chars = list(body)
        pos = 0
        while True:
            m = CLAUSE_CITE_RE.search(body, pos)
            if not m:
                break
            end = close_paren(body, m.end() - 1)
            if end is None:
                fail(f"{rel}: unbalanced parenthesis in an ISO clause citation")
                break
            nos = [x.strip() for x in body[m.start():m.end() - 1].split("/") if x.strip()]
            title = body[m.end():end]
            # A slash-joined group carries one combined label for the pair, so it is not comparable
            # with the title of either clause on its own.
            if len(nos) == 1:
                clause_titles[lang].setdefault(nos[0], {}).setdefault(title, set()).add(rel)
            for i in range(m.start(), end + 1):
                chars[i] = " "
            pos = end + 1
        for leftover in CLAUSE_NO_RE.findall("".join(chars)):
            fail(f"{rel}: ISO clause citation {leftover} carries no parenthesised clause title. "
                 f"Write '{leftover}(<clause title>)' so the citation names the clause it points "
                 "at and the list stays unambiguous.")


def check_pair(no, paths, catalog_by_no):
    """Checks [7], [8] and [9] for one control across both languages."""
    text = {lang: read(paths[lang]) for lang in LANGS}
    rel = {lang: os.path.relpath(paths[lang], ROOT).replace(os.sep, "/") for lang in LANGS}

    # [7] structural parity between the two languages.
    for ko_sec, en_sec in zip(COUNTED_SECTIONS["ko"], COUNTED_SECTIONS["en"]):
        a = section_items(text["ko"], ko_sec)
        b = section_items(text["en"], en_sec)
        if a is not None and b is not None and a != b:
            fail(f"{no}: '{ko_sec}' has {a} items but '{en_sec}' has {b}. "
                 "Edit both languages in the same commit.")

    meta = {lang: meta_rows(text[lang]) for lang in LANGS}
    for lang in LANGS:
        for row in META_ROWS[lang]:
            if row not in meta[lang]:
                fail(f"{rel[lang]}: metadata table is missing the '{row}' row")

    # [9] the two languages must classify a control the same way.
    kt = [TYPE_KO.get(x, x) for x in attr_tokens(meta["ko"].get("통제 유형(참고)", ""))]
    et = attr_tokens(meta["en"].get("Control type (ref.)", ""))
    if kt != et:
        fail(f"{no}: control type is {kt} in ko but {et} in en")
    kp = [PROP_KO.get(x, x) for x in attr_tokens(meta["ko"].get("보안 속성(참고)", ""))]
    ep = attr_tokens(meta["en"].get("Security properties (ref.)", ""))
    if kp != ep:
        fail(f"{no}: security properties are {kp} in ko but {ep} in en")

    # [8] cross-reference labels must reproduce the catalog title.
    for lang, key in (("ko", "title_ko"), ("en", "title_en")):
        for line in text[lang].split("\n"):
            if XREF_MARKER[lang] not in line:
                continue
            body = RANGE_RE.sub("", line.split(XREF_MARKER[lang], 1)[1])
            # The parenthesised form is mandatory, because the title check below only sees a label
            # that is wrapped in parentheses. A reference written as bare 'A.5.24 <title>' slipped
            # past it entirely, and six Korean documents carried abbreviated or invented titles that
            # way while this check still reported PASS. Requiring the form closes that fail-open.
            for m in re.finditer(r"(A\.\d+\.\d+)\s*([(（])?", body):
                if m.group(2) is None:
                    fail(f"{rel[lang]}: cross-reference {m.group(1)} carries no parenthesised "
                         "title, so its label is never checked against the catalog. Write "
                         "'A.x.y(<catalog title>)'.")
            for m in re.finditer(r"(A\.\d+\.\d+)\s*[(（]", body):
                ref = m.group(1)
                if ref not in catalog_by_no:
                    fail(f"{rel[lang]}: cross-reference {ref} is not a control in the catalog")
                    continue
                end = close_paren(body, m.end() - 1)
                if end is None:
                    continue
                label = body[m.end():end]
                want = catalog_by_no[ref][key]
                if label != want:
                    fail(f"{rel[lang]}: {ref} is labelled '{label}' but the catalog says '{want}'")


def main():
    for required in (MANIFEST, CATALOG):
        if not os.path.exists(required):
            print(
                f"{os.path.relpath(required, ROOT)} is missing. Run: python3 tools/build_index.py",
                file=sys.stderr,
            )
            return 1
    manifest = json.load(open(MANIFEST, encoding="utf-8"))
    catalog = json.load(open(CATALOG, encoding="utf-8"))

    # [1] manifest self-consistency.
    items = manifest["items"]
    counts = manifest["counts"]
    for lang in LANGS:
        actual = sum(1 for it in items if it["lang"] == lang)
        if actual != counts.get(lang):
            fail(f"manifest counts.{lang} is {counts.get(lang)} but the item list holds {actual}")
    if counts.get("total") != len(items):
        fail(f"manifest counts.total is {counts.get('total')} but the item list holds {len(items)}")
    for section in manifest["standard"]["sections"]:
        for lang in LANGS:
            actual = sum(1 for it in items if it["lang"] == lang and it["section"] == section["id"])
            if actual != section["count"][lang]:
                fail(
                    f"manifest section {section['id']} count.{lang} is "
                    f"{section['count'][lang]} but the item list holds {actual}"
                )

    # [2] Korean and English mirror each other.
    keys = {lang: {(it["section"], it["no"]) for it in items if it["lang"] == lang} for lang in LANGS}
    for lang, other in (("ko", "en"), ("en", "ko")):
        for key in sorted(keys[lang] - keys[other]):
            fail(f"{key[0]} {key[1]} exists in {lang} but is missing in {other}")

    # [6] manifest, catalog, and disk all agree.
    on_disk = set()
    for lang in LANGS:
        for path in glob.glob(os.path.join(DOCS, lang, "**", "*.md"), recursive=True):
            if os.path.basename(path) == "INDEX.md":
                continue
            on_disk.add(os.path.relpath(path, ROOT).replace(os.sep, "/"))
            check_document(path, lang)
    in_manifest = {it["path"] for it in items}
    for missing in sorted(in_manifest - on_disk):
        fail(f"{missing}: recorded in the manifest but not present on disk")
    for extra in sorted(on_disk - in_manifest):
        fail(f"{extra}: present on disk but missing from the manifest")

    catalog_nos = {c["no"] for c in catalog["controls"]}
    for lang in LANGS:
        documented = {it["no"] for it in items if it["lang"] == lang}
        for missing in sorted(catalog_nos - documented):
            fail(f"{missing}: listed in the catalog but has no {lang} document")
        for extra in sorted(documented - catalog_nos):
            fail(f"{extra}: has a {lang} document but is not listed in the catalog")

    catalog_by_no = {c["no"]: c for c in catalog["controls"]}
    theme_dir = {tid: t["dir"] for tid, t in catalog["themes"].items()}
    for control in catalog["controls"]:
        no = control["no"]
        paths = {lang: os.path.join(DOCS, lang, theme_dir[control["theme"]], no + ".md")
                 for lang in LANGS}
        if all(os.path.exists(paths[lang]) for lang in LANGS):
            check_pair(no, paths, catalog_by_no)

    # [10] one clause number, one title. Judged here rather than per document, because a title is
    # only inconsistent relative to how the rest of the corpus cites the same clause.
    for lang in LANGS:
        for clause, titles in sorted(clause_titles[lang].items()):
            if len(titles) < 2:
                continue
            shown = []
            for title, files in sorted(titles.items()):
                where = sorted(files)[0]
                if len(files) > 1:
                    where += f" and {len(files) - 1} more"
                shown.append(f'"{title}" ({where})')
            fail(f"ISO clause {clause} is cited under {len(titles)} different titles in {lang}: "
                 + "; ".join(shown)
                 + ". One clause number carries one title across the corpus.")

    if problems:
        for p in problems:
            print(f"FAIL {p}")
        print(f"\nRESULT: FAIL ({len(problems)} problems)")
        return 1
    print(
        f"RESULT: PASS ({counts['total']} documents, "
        + ", ".join(f"{lang} {counts[lang]}" for lang in LANGS)
        + f", catalog {len(catalog_nos)} controls)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
