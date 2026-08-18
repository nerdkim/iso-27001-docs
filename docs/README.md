# docs/ : the Annex A control corpus

> 한국어: [README.ko.md](README.ko.md)
>
> Repository overview: [../README.md](../README.md) and source basis: [../UPDATES.md](../UPDATES.md)

This directory is the corpus itself: the 93 information security controls of ISO/IEC 27001:2022
Annex A, one Markdown file per control, in Korean and English. Everything else in this repository is
generated from these files or exists to guard them.

## What these documents are, and are not

**They are not the standard.** Control numbers, titles, and theme classification come from the
public Annex A control list. The explanatory body of every document is **original material** written
by this project for practical reference.

The normative text of ISO/IEC 27001:2022, its implementation guidance, and its attribute tables are
not reproduced, paraphrased close to the source, or translated here. Each document carries a source
and limitation notice at the bottom saying so. For an authoritative answer, use a licensed copy of
the standard.

This boundary is a hard rule when editing, and it is also the reason the update model here differs
from an ordinary mirror of an upstream document. See [../UPDATES.md](../UPDATES.md).

## Read-only

Treat this directory as **immutable while using the corpus**. `tools/build_index.py` and
`tools/check_corpus.py` only read from here, and an agent answering questions with the corpus must
never create, edit, or delete anything under `docs/`. Derived output belongs in the consuming
workspace.

Maintainers do edit these files. That is a different activity, with its own rules: see
[../CLAUDE.md](../CLAUDE.md) and the parity rule below.

## Layout

`docs/<lang>/<theme-slug>/<no>.md`, where `<lang>` is `ko` or `en`. The two languages mirror each
other with **identical relative paths**. All paths are ASCII.

```
docs/
  ko/
    A.5-organizational/A.5.1.md    37 controls
    A.6-people/*.md                 8 controls
    A.7-physical/*.md              14 controls
    A.8-technological/*.md         34 controls
    INDEX.md                       generated table of contents
  en/                              same relative paths
    ...
    INDEX.md
```

93 controls per language, 186 documents in total.

| Theme (stable id) | Slug | Controls | Range | Index |
|---|---|:--:|:--:|---|
| `organizational` | `A.5-organizational` | 37 | A.5.1 to A.5.37 | [ko](ko/INDEX.md) / [en](en/INDEX.md) |
| `people` | `A.6-people` | 8 | A.6.1 to A.6.8 | same |
| `physical` | `A.7-physical` | 14 | A.7.1 to A.7.14 | same |
| `technological` | `A.8-technological` | 34 | A.8.1 to A.8.34 | same |

Which controls must exist is defined by [`../extended/catalog/controls.json`](../extended/catalog/controls.json).
`check_corpus.py` fails when the catalog and the documents disagree in either direction, so the
catalog and this directory cannot silently drift apart.

## Document structure

Every control document carries a metadata table, then the same six sections in the same order, then
the source and limitation notice:

`통제 목적` → `주요 확인사항` → `이행 지침` → `관련 통제 및 속성` → `증적자료` → `부적합 사례`

`check_corpus.py` fails when a document is missing a section or reorders them, so the structure is
safe to depend on.

## Language parity

Unlike the ISMS-P corpus, neither language here is a translation of the other, and neither is
subordinate: both are this project's own writing. They must still say the same thing, and they must
change **in the same commit**. A Korean-only or English-only content edit is a defect, and CI
rejects it. The correspondence is keyed by control number.

## For AI agents: route through the manifest

Do not grep `docs/` blindly. Start from [`../extended/manifest.json`](../extended/manifest.json),
which indexes every document with its `no`, `path`, theme, and per-section counts. Narrow to the
relevant control numbers first, then read only those files. When only the lists are needed, read
`../extended/index/evidence-dictionary.json` or `../extended/index/nonconformity-rulebook.json`
instead of the documents.

The full operating rules (read-only corpus, manifest-first routing, mandatory citation, the
copyright boundary, human approval gates) are in [../extended/README.md](../extended/README.md).
