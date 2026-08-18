# iso-27001-docs

> 한국어: [README.ko.md](README.ko.md)

A bilingual practical reference for the 93 controls of **ISO/IEC 27001:2022 Annex A**, one Markdown
file per control, in **Korean and English**.

This repository holds documents only. There is no application here, no build output, and no
infrastructure. A consumer reads [`extended/manifest.json`](extended/manifest.json), which is the
published contract for this corpus.

## Copyright boundary, read this first

- Control **numbers, titles, and the four-theme classification** come from the **public list** of
  ISO/IEC 27001:2022 Annex A. That list is factual reference data.
- The **explanatory body of every document is original material written for this collection**:
  control objective, key checkpoints, implementation guidance, related controls, evidence examples,
  and nonconformity examples. It is **not** the normative text of ISO/IEC 27001:2022 or 27002:2022,
  and it is not a translation of that text.
- The standard's normative text, its implementation guidance, its attribute tables, and third-party
  commentary are **never reproduced verbatim** in this repository.
- For anything authoritative, compare against a **licensed copy of the standard**. Every document
  carries this notice in its footer, and CI fails if a document is missing it.

That boundary also decides how this corpus is updated: there is no upstream text to re-sync against,
so an ISO revision changes the **control list** here, not the wording of the explanations.
[UPDATES.md](UPDATES.md) records the edition each layer is pinned to and how each layer is
maintained.

## Contents

| Theme | Controls per language |
|---|---|
| A.5 조직적 통제(Organizational) | 37 |
| A.6 인적 통제(People) | 8 |
| A.7 물리적 통제(Physical) | 14 |
| A.8 기술적 통제(Technological) | 34 |
| **Total** | **93 per language** (186 documents) |

Every control document keeps the same six sections:

`통제 목적` → `주요 확인사항` → `이행 지침` → `관련 통제 및 속성` → `증적자료` → `부적합 사례`

## Layout

```
docs/
  ko/                            Korean documents
    A.5-organizational/<no>.md   e.g. docs/ko/A.5-organizational/A.5.1.md
    A.6-people/<no>.md
    A.7-physical/<no>.md
    A.8-technological/<no>.md
    INDEX.md                     generated table of contents
  en/                            English documents, same relative paths
extended/
  catalog/controls.json          the public Annex A control list (numbers, titles, themes)
  manifest.json                  machine-readable index (the published contract)
  index/                         flat CSV index, nonconformity rulebook, evidence dictionary
tools/
  build_index.py                 regenerate every derived index from docs/
  check_corpus.py                read-only integrity checks
harness/
  install-hooks.sh               wire this clone to the git hooks (run once, see Setup)
  check-conventions.sh           documentation conventions checker (playbook docs/16)
```

All paths are ASCII, so there are no URL-encoding surprises for consumers.

## The manifest contract

`extended/manifest.json` (schema `corpus-manifest/v3`) is what downstream consumers read. `nav` is
set to `themes`, so a consumer renders the four themes as its top-level navigation:

```json
{
  "schema": "corpus-manifest/v3",
  "standard": {
    "id": "iso-27001",
    "nav": "themes",
    "langs": ["ko", "en"],
    "sections": [{ "id": "organizational", "slug": "A.5-organizational", "no": "A.5",
                   "label": { "ko": "조직적 통제", "en": "Organizational controls" },
                   "count": { "ko": 37, "en": 37 } }],
    "provenance": { "ko": "...", "en": "..." },
    "itemSections": { "ko": ["통제 목적", "..."], "en": ["Control objective", "..."] }
  },
  "counts": { "ko": 93, "en": 93, "total": 186 },
  "items": [{
    "lang": "ko", "section": "organizational", "no": "A.5.1", "name": "정보보안 정책",
    "groupNo": "A.5", "group": "조직적 통제", "subgroupNo": "", "subgroup": "",
    "appliesTo": [], "path": "docs/ko/A.5-organizational/A.5.1.md",
    "counts": { "checkpoints": 4, "evidence": 4, "defects": 4, "hasLaws": false }
  }]
}
```

**Stable keys, never renamed**: the standard id `iso-27001`, the theme ids `organizational` /
`people` / `physical` / `technological`, and the control numbers. Consumers key on them.

## Setup

This repository holds documents only, so there is no package manager and no install step to hang
the git-hook wiring on. `core.hooksPath` lives in `.git/config`, which is local state that does not
travel with a clone, so run this **once per clone**:

```bash
bash harness/install-hooks.sh
```

It is idempotent, writes nothing outside `.git/config`, and activates `pre-commit` (documentation
conventions), `commit-msg` (message rules), and `pre-push` (blocks a direct push to master). The
hooks are a convenience guardrail and are bypassable; the authoritative gate is CI
(`.github/workflows/docs.yml`), which runs the same checkers.

Everything else needs only Python 3 (standard library only) and bash.

## Maintaining

```bash
python3 tools/build_index.py    # regenerate extended/ and the docs/{ko,en}/INDEX.md files
python3 tools/check_corpus.py   # read-only integrity checks
bash harness/check-conventions.sh
```

Both builders are deterministic and reproducible: CI regenerates and fails on any diff, so the
committed indexes always match the corpus.

When you add, edit, or delete a control, **update the counterpart document in the other language in
the same commit**. The correspondence is keyed by control number. A Korean-only or English-only edit
is a bug, and CI rejects it.

Adding a control also means adding it to `extended/catalog/controls.json`; `check_corpus.py` fails
when the catalog and the documents disagree in either direction.

## License

- Code and tooling: MIT. See [LICENSE](LICENSE).
- The corpus (the original explanatory material and the compilation under `docs/`): CC BY 4.0. See
  [LICENSE-CONTENT](LICENSE-CONTENT) and [NOTICE](NOTICE).

These licenses cover this project's own work only. The ISO/IEC 27001 standard text remains the
property of ISO and IEC and is not relicensed, reproduced, or translated here.
