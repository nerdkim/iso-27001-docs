#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Corpus integrity checks for this repository. Read-only: nothing is written.

Checks
  [1] manifest present and self-consistent (counts match the item list)
  [2] Korean and English mirror each other exactly, keyed by (theme, control number)
  [3] every control document carries the six required sections, in order
  [4] the H1 names the control: the number matches the file name, and the title is the catalog's
  [5] every control document ENDS with the source/limitation footer, a '---' rule followed by
      the '>' block, so the copyright boundary is the last thing in the file
  [6] every path recorded in the manifest exists on disk, no document on disk is missing from the
      manifest, every control in the catalog has a document in both languages, and every document
      sits at its canonical docs/<lang>/<theme-dir>/<no>.md path
  [7] each counted section is counted exactly as tools/build_index.py counts it (numbered items
      in the checkpoints section, '- ' bullets elsewhere), holds at least one item, and holds the
      same number of items in both languages. A section that cannot be located is a failure, never
      a silent skip
  [8] every 'A.x.y (title)' cross-reference anywhere in a document reproduces that control's title
      from the catalog, and on the adjacency line the parenthesised title form is mandatory so
      that a reference cannot escape that comparison
  [9] the metadata table carries the expected rows; the control title, the control-type and
      security-property values, and the numbers in the two factual mapping rows ('2013' and
      'ISMS-P') agree with the catalog, between the two languages, and with the matching line in
      the related-controls section
 [10] every ISO main-body clause citation carries a parenthesised clause title, one clause number
      is cited under one title across the whole corpus per language, and an Annex A number never
      stands on the clause line
 [11] the skill routing table (skill/iso-27001-review/topic-index.json) names only controls that
      exist in the catalog, and every catalog control is reachable from at least one topic

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
TOPIC_INDEX = os.path.join(ROOT, "skill", "iso-27001-review", "topic-index.json")

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


def h1_form(no, lang, entry):
    """The H1 the catalog dictates for this control, in this language.

    Read from the catalog at run time, never hardcoded, so a catalog retitle is picked up here
    without touching this check.
    """
    if lang == "ko":
        return f"# {no} {entry['title_ko']}({entry['title_en']})"
    return f"# {no} {entry['title_en']}"


def check_document(path, lang, catalog_by_no):
    rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
    text = open(path, encoding="utf-8").read()

    # [4] H1 names the control: the number matches the file name, and the title is the catalog's.
    # Checking only the number let a title typo ship while INDEX.md and extended/manifest.json,
    # both generated from the catalog, carried the correct title.
    expected_no = os.path.splitext(os.path.basename(path))[0]
    first = text.split("\n", 1)[0].rstrip()
    m = re.match(r"^#\s+(A\.\d+\.\d+)\s+\S", first)
    if not m:
        fail(f"{rel}: first line is not a '# <no> <title>' heading")
    elif m.group(1) != expected_no:
        fail(f"{rel}: H1 control number {m.group(1)} does not match the file name {expected_no}")
    elif expected_no in catalog_by_no:
        want = h1_form(expected_no, lang, catalog_by_no[expected_no])
        if first != want:
            fail(f"{rel}: H1 is '{first}' but the catalog says '{want}'")

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

    # [5] source/limitation footer, at the END of the document. An unanchored search passed on any
    # document holding a '---' line followed by a '>' line ANYWHERE, so a footer left stranded in
    # the middle of a document satisfied the check that carries this repository's copyright
    # boundary. The last non-empty lines must be the rule and the '>' block, nothing after them.
    if not re.search(r"(?m)^---[ \t]*\n(?:>[ \t]*\S[^\n]*\n?)+[ \t\n]*\Z", text):
        fail(f"{rel}: the document does not END with the source/limitation footer. The last lines "
             "must be a '---' rule followed by the '> ' footer block.")

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
# The left-boundary guard is the same one CLAUSE_NO_RE carries below, and for the same reason:
# without it the '7.10' inside an Annex A number such as 'A.7.10(...)' was parsed as main-body
# clause 7.10, which both masked the misplaced reference and could raise a title-conflict failure
# naming an innocent document.
CLAUSE_CITE_RE = re.compile(r"(?<![\w.])\d+(?:\.\d+){0,2}(?:\s*/\s*\d+(?:\.\d+){0,2})*\s*[(（]")
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
# 2013-edition control numbers carry four segments (A.8.1.3). Their three-segment prefix would
# otherwise be read as a 2022 control number, so they are removed before check [8] looks.
LEGACY_NO_RE = re.compile(r"A\.\d+\.\d+\.\d+")
# The two factual metadata rows, as (label, number pattern, (ko row, en row), (ko marker, en
# marker)). The markers name the matching line in the related-controls section.
MAPPING_ROWS = (
    ("2013 mapping", re.compile(r"A\.\d+\.\d+\.\d+(?![\w.])"),
     ("2013 대응", "2013 mapping"), ("2013 대응:", "2013 mapping:")),
    ("ISMS-P mapping", re.compile(r"(?<![\w.])\d+\.\d+\.\d+(?![\w.])"),
     ("ISMS-P 대응", "ISMS-P mapping"), ("ISMS-P 대응:", "ISMS-P mapping:")),
)


def read(path):
    return open(path, encoding="utf-8").read()


# tools/build_index.py counts numbered items in the checkpoints section and '- ' bullets in every
# other counted section. Counting both markers alike here meant a swapped list marker zeroed the
# published index while this check still reported the two languages in agreement.
NUMBERED_SECTIONS = {"주요 확인사항", "Key checkpoints"}


def section_body(text, title):
    """The body of the '## <title>' section, or None when the heading is not there.

    Anchored exactly as build_index.section_body() is: the heading may carry trailing text after
    the section name, and the section ends at the next '## ' or at a BARE '---' rule line. The two
    boundaries must stay identical, or the checker counts a section the builder has truncated.
    """
    m = re.search(r"(?m)^##\s+" + re.escape(title) + r"\b[^\n]*$(.*?)(?=^##\s|\n---\n|\Z)",
                  text, re.S)
    return None if m is None else m.group(1)


def count_bullets(body):
    """Mirrors build_index.bullets(): '- ' items, italic placeholders such as _(none)_ dropped."""
    n = 0
    for line in body.split("\n"):
        stripped = line.strip()
        if not stripped.startswith("- "):
            continue
        value = stripped[2:].strip()
        if value and not (value.startswith("_") and value.endswith("_")):
            n += 1
    return n


def count_numbered(body):
    """Mirrors build_index.numbered(): 'N.' items."""
    return len([l for l in body.split("\n") if re.match(r"^\d+\.\s", l.strip())])


def section_items(text, title):
    """(items under the expected list marker, items under the other one), or None.

    None means the section could not be located at all, and the caller must report that rather
    than skip the comparison. The second count turns a swapped marker into a specific message
    instead of a bare 'this section is empty'.
    """
    body = section_body(text, title)
    if body is None:
        return None
    if title in NUMBERED_SECTIONS:
        return (count_numbered(body), count_bullets(body))
    return (count_bullets(body), count_numbered(body))


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
        # An Annex A control belongs on the adjacency line, never here. The guard in CLAUSE_CITE_RE
        # stops it being misread as a main-body clause, which would leave it entirely unreported.
        for m in re.finditer(r"A\.\d+\.\d+", body):
            fail(f"{rel}: Annex A control {m.group(0)} is written on the ISO clause line. "
                 f"'{CLAUSE_MARKER[lang]}' carries main-body clauses only; move the control to "
                 f"the '{XREF_MARKER[lang]}' line.")
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


def check_counted_sections(no, text, rel):
    """[7] every counted section is present, non-empty, correctly marked, and equal across langs.

    Each of the three guarantees closes a way a real defect used to reach a green run: a section
    the parser could not locate was skipped in silence, a section emptied in both languages passed
    the parity comparison as 0 == 0 and published an empty list into extended/index/, and a section
    whose list marker was swapped was counted here but zeroed by the builder.
    """
    for ko_sec, en_sec in zip(COUNTED_SECTIONS["ko"], COUNTED_SECTIONS["en"]):
        name = {"ko": ko_sec, "en": en_sec}
        counts = {lang: section_items(text[lang], name[lang]) for lang in LANGS}
        unparsed = [lang for lang in LANGS if counts[lang] is None]
        if unparsed:
            for lang in unparsed:
                fail(f"{rel[lang]}: section '{name[lang]}' could not be located, so the two "
                     "languages were never compared for it. The heading must be "
                     f"'## {name[lang]}' on its own line.")
            continue
        for lang in LANGS:
            expected, other = counts[lang]
            marker = ("numbered 'N.' items" if name[lang] in NUMBERED_SECTIONS else "'- ' bullets")
            if expected == 0 and other > 0:
                fail(f"{rel[lang]}: section '{name[lang]}' holds {other} items under the wrong "
                     f"list marker. tools/build_index.py counts {marker} here, so the published "
                     "index would carry an empty list for it.")
            elif expected == 0:
                fail(f"{rel[lang]}: section '{name[lang]}' has no items. A counted section is "
                     "published into extended/index/, where an empty list is indistinguishable "
                     "from a control that was never written.")
        if counts["ko"][0] != counts["en"][0]:
            fail(f"{no}: '{ko_sec}' has {counts['ko'][0]} items but '{en_sec}' has "
                 f"{counts['en'][0]}. Edit both languages in the same commit.")


def check_mapping_rows(no, text, rel, meta):
    """[9] the two factual mapping rows agree across languages and with the body line.

    '2013 대응' / '2013 mapping' and 'ISMS-P 대응' / 'ISMS-P mapping' are read as fact by an
    auditor, and a one-language edit to either used to land unnoticed. Only the NUMBERS are
    compared: each language renders the item names its own way. The related-controls line may add
    related items, so the row's numbers must all APPEAR on that line rather than equal it.
    """
    for label, pat, rows, markers in MAPPING_ROWS:
        cell = {}
        for lang, row, marker in zip(LANGS, rows, markers):
            cell[lang] = set(pat.findall(meta[lang].get(row, "")))
            line = next((l for l in text[lang].split("\n")
                         if l.lstrip().startswith("-") and marker in l), None)
            if line is None:
                fail(f"{rel[lang]}: the related-controls section carries no '{marker}' line")
                continue
            absent = cell[lang] - set(pat.findall(line.split(marker, 1)[1]))
            if absent:
                fail(f"{rel[lang]}: the '{row}' metadata row names {sorted(absent)}, which the "
                     f"'{marker}' line does not. Every number in the row must appear on the line.")
        if cell.get("ko") != cell.get("en"):
            fail(f"{no}: {label} is {sorted(cell.get('ko', ()))} in ko but "
                 f"{sorted(cell.get('en', ()))} in en")


def check_pair(no, paths, catalog_by_no):
    """Checks [7], [8] and [9] for one control across both languages."""
    text = {lang: read(paths[lang]) for lang in LANGS}
    rel = {lang: os.path.relpath(paths[lang], ROOT).replace(os.sep, "/") for lang in LANGS}

    # [7] structural parity between the two languages.
    check_counted_sections(no, text, rel)

    meta = {lang: meta_rows(text[lang]) for lang in LANGS}
    for lang in LANGS:
        for row in META_ROWS[lang]:
            if row not in meta[lang]:
                fail(f"{rel[lang]}: metadata table is missing the '{row}' row")

    # [9] the catalog is the source of truth for a control's title, so the document's own title row
    # is compared with it exactly as every cross-reference label already is.
    for lang, row, key in (("ko", "통제", "title_ko"), ("en", "Control", "title_en")):
        want = f"{no} {catalog_by_no[no][key]}"
        got = meta[lang].get(row)
        if got is not None and got != want:
            fail(f"{rel[lang]}: the '{row}' row says '{got}' but the catalog says '{want}'")

    # [9] the two factual mapping rows.
    check_mapping_rows(no, text, rel, meta)

    # [9] the two languages must classify a control the same way.
    kt = [TYPE_KO.get(x, x) for x in attr_tokens(meta["ko"].get("통제 유형(참고)", ""))]
    et = attr_tokens(meta["en"].get("Control type (ref.)", ""))
    if kt != et:
        fail(f"{no}: control type is {kt} in ko but {et} in en")
    kp = [PROP_KO.get(x, x) for x in attr_tokens(meta["ko"].get("보안 속성(참고)", ""))]
    ep = attr_tokens(meta["en"].get("Security properties (ref.)", ""))
    if kp != ep:
        fail(f"{no}: security properties are {kp} in ko but {ep} in en")

    # [8] cross-reference labels must reproduce the catalog title, wherever they are written.
    for lang, key in (("ko", "title_ko"), ("en", "title_en")):
        check_cross_references(rel[lang], lang, key, text[lang], catalog_by_no)


def check_cross_references(rel, lang, key, text, catalog_by_no):
    """[8] every 'A.x.y(<title>)' label in this document reproduces the catalog title.

    The label is judged wherever it is written, not only on the adjacency line: a title invented in
    the body of a document misleads a reader exactly as one invented on the adjacency line does.
    The parenthesised FORM is still required on the adjacency line alone, because elsewhere a bare
    'A.5.24' is an ordinary pointer and carries no label to compare.
    """
    for line in text.split("\n"):
        # The metadata table and the H1 carry this control's own number and title, which check [4]
        # and the title row already compare with the catalog, and the '2013' row would be misread.
        if line.lstrip().startswith("|") or line.startswith("# "):
            continue
        on_marker = XREF_MARKER[lang] in line
        body = line.split(XREF_MARKER[lang], 1)[1] if on_marker else line
        body = LEGACY_NO_RE.sub("", RANGE_RE.sub("", body))
        # On the adjacency line the parenthesised form is mandatory, because the title comparison
        # below only sees a label that is wrapped in parentheses. A reference written as bare
        # 'A.5.24 <title>' slipped past it entirely, and six Korean documents carried abbreviated
        # or invented titles that way while this check still reported PASS.
        if on_marker:
            for m in re.finditer(r"(A\.\d+\.\d+)\s*([(（])?", body):
                if m.group(2) is None:
                    fail(f"{rel}: cross-reference {m.group(1)} carries no parenthesised title, so "
                         "its label is never checked against the catalog. Write "
                         "'A.x.y(<catalog title>)'.")
        for m in re.finditer(r"(A\.\d+\.\d+)\s*[(（]", body):
            ref = m.group(1)
            if ref not in catalog_by_no:
                fail(f"{rel}: cross-reference {ref} is not a control in the catalog")
                continue
            end = close_paren(body, m.end() - 1)
            if end is None:
                continue
            label = body[m.end():end]
            want = catalog_by_no[ref][key]
            if label != want:
                fail(f"{rel}: {ref} is labelled '{label}' but the catalog says '{want}'")


def check_topic_index(catalog_nos):
    """[11] the skill routing table and the catalog agree in both directions.

    The skill routes a user's words to control numbers through this table before it reads any
    document, so a control missing from every topic is unreachable through the skill, and a number
    that is not in the catalog would route to a document that does not exist. Both are defects of the
    same kind as a catalog/document mismatch, and are judged the same way.
    """
    rel = os.path.relpath(TOPIC_INDEX, ROOT).replace(os.sep, "/")
    if not os.path.exists(TOPIC_INDEX):
        fail(f"{rel}: missing. The skill cannot route without its topic index.")
        return
    try:
        index = json.load(open(TOPIC_INDEX, encoding="utf-8"))
    except ValueError as exc:
        fail(f"{rel}: not valid JSON ({exc})")
        return
    topics = index.get("topics")
    if not isinstance(topics, list) or not topics:
        fail(f"{rel}: 'topics' must be a non-empty list")
        return
    reachable = set()
    for i, topic in enumerate(topics):
        label = topic.get("topic_ko") or topic.get("topic_en") or f"#{i}"
        controls = topic.get("controls")
        if not isinstance(controls, list) or not controls:
            fail(f"{rel}: topic '{label}' has no controls")
            continue
        if not topic.get("keywords"):
            fail(f"{rel}: topic '{label}' has no keywords, so nothing can route to it")
        for no in controls:
            if no not in catalog_nos:
                fail(f"{rel}: topic '{label}' routes to {no}, which is not a control in the catalog")
            reachable.add(no)
    for no in sorted(catalog_nos - reachable):
        fail(f"{rel}: {no} is not reachable from any topic, so the skill can never route to it")


def check_manifest(manifest):
    """[1] the manifest agrees with itself, and [2] the two languages mirror each other in it."""
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
    keys = {lang: {(it["section"], it["no"]) for it in items if it["lang"] == lang}
            for lang in LANGS}
    for lang, other in (("ko", "en"), ("en", "ko")):
        for key in sorted(keys[lang] - keys[other]):
            fail(f"{key[0]} {key[1]} exists in {lang} but is missing in {other}")


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

    check_manifest(manifest)
    items = manifest["items"]
    counts = manifest["counts"]

    catalog_nos = {c["no"] for c in catalog["controls"]}
    catalog_by_no = {c["no"]: c for c in catalog["controls"]}
    theme_dir = {tid: t["dir"] for tid, t in catalog["themes"].items()}
    canonical = {
        f"docs/{lang}/{theme_dir[c['theme']]}/{c['no']}.md"
        for lang in LANGS
        for c in catalog["controls"]
    }

    # [6] manifest, catalog, and disk all agree.
    on_disk = set()
    for lang in LANGS:
        for path in glob.glob(os.path.join(DOCS, lang, "**", "*.md"), recursive=True):
            if os.path.basename(path) == "INDEX.md":
                continue
            on_disk.add(os.path.relpath(path, ROOT).replace(os.sep, "/"))
            check_document(path, lang, catalog_by_no)
    in_manifest = {it["path"] for it in items}
    for missing in sorted(in_manifest - on_disk):
        fail(f"{missing}: recorded in the manifest but not present on disk")
    for extra in sorted(on_disk - in_manifest):
        fail(f"{extra}: present on disk but missing from the manifest")

    # [6] a document at a non-canonical path is indexed under the theme its directory names, not
    # the theme the catalog gives it, and the bilingual pair checks below never reach it. A number
    # that is not in the catalog at all is already reported just below, so it is not repeated here.
    for extra in sorted(on_disk - canonical):
        if os.path.splitext(os.path.basename(extra))[0] not in catalog_nos:
            continue
        fail(f"{extra}: not the canonical path for this control. A control document lives at "
             "docs/<lang>/<theme-dir>/<no>.md and nowhere else.")
    for lang in LANGS:
        documented = {it["no"] for it in items if it["lang"] == lang}
        for missing in sorted(catalog_nos - documented):
            fail(f"{missing}: listed in the catalog but has no {lang} document")
        for extra in sorted(documented - catalog_nos):
            fail(f"{extra}: has a {lang} document but is not listed in the catalog")

    for control in catalog["controls"]:
        no = control["no"]
        paths = {lang: os.path.join(DOCS, lang, theme_dir[control["theme"]], no + ".md")
                 for lang in LANGS}
        absent = [lang for lang in LANGS if not os.path.exists(paths[lang])]
        if not absent:
            check_pair(no, paths, catalog_by_no)
            continue
        # Skipping in silence was the fail-open: a document moved anywhere else under the theme
        # tree still satisfied the manifest and catalog checks, because the builder derives the
        # theme from the path segment and the control number from the file name, so every pair
        # check ([7][8][9]) was dropped for that control without a word.
        for lang in absent:
            fail(f"{os.path.relpath(paths[lang], ROOT).replace(os.sep, '/')}: expected at this "
                 f"exact path, so the bilingual pair checks [7][8][9] never ran for {no} in "
                 f"{lang}. A control document lives at docs/<lang>/<theme-dir>/<no>.md and "
                 "nowhere else.")

    # [11] the skill routing table names real controls and reaches every one of them.
    check_topic_index(catalog_nos)

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
