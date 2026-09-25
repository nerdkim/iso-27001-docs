# iso-27001-docs

> 한국어: [README.ko.md](README.ko.md)

A bilingual practical reference for the 93 controls of **ISO/IEC 27001:2022 Annex A**, one Markdown
file per control, in **Korean and English**.

This repository holds documents only. There is no application here, no build output, and no
infrastructure. A consumer reads [`extended/manifest.json`](extended/manifest.json), which is the
published contract for this corpus.

**Scope: Annex A only.** This corpus covers the 93 Annex A controls and nothing else. It does not
document the ISMS requirements of main-body clauses 4 to 10: scope, leadership, risk assessment and
treatment, the Statement of Applicability required by 6.1.3, objectives, competence, documented
information, operation, performance evaluation, internal audit, management review, nonconformity
and corrective action. The `ISO 27001 clauses` lines in the control documents are pointers into the
main body, not summaries of it, so a reader who needs those requirements needs a licensed copy of
the standard. The Statement of Applicability is where an organization records its decision on each
of the 93 controls; this corpus is not one and does not generate one.

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

[REVIEW.md](REVIEW.md) records the 2026-09-17 full body review of all 186 control documents,
including corrections, control-by-control coverage, and verification limits.

## Contents

| Theme | Controls per language |
|---|---|
| A.5 Organizational controls | 37 |
| A.6 People controls | 8 |
| A.7 Physical controls | 14 |
| A.8 Technological controls | 34 |
| **Total** | **93 per language** (186 documents) |

Every control document keeps the same six sections:

`Control objective` → `Key checkpoints` → `Implementation guidance` →
`Related controls and attributes` → `Evidence` → `Nonconformity examples`

## Layout

```
docs/
  README.md / README.ko.md       what these documents are, and the read-only rule
  ko/                            Korean documents
    A.5-organizational/<no>.md   e.g. docs/ko/A.5-organizational/A.5.1.md
    A.6-people/<no>.md
    A.7-physical/<no>.md
    A.8-technological/<no>.md
    INDEX.md                     generated table of contents
  en/                            English documents, same relative paths
extended/
  README.md / README.ko.md       operating rules for AI use of the corpus
  catalog/controls.json          the public Annex A control list (numbers, titles, themes)
  manifest.json                  machine-readable index (the published contract)
  index/                         flat CSV index, nonconformity rulebook, evidence dictionary
tools/
  build_index.py                 regenerate every derived index from docs/
  check_corpus.py                read-only integrity checks
  test_check_corpus.py           regression tests for document boundaries and the AGENTS.md link
harness/
  install-hooks.sh               wire this clone to the git hooks (run once, see Setup)
  check-conventions.sh           documentation conventions checker (playbook docs/16)
  test-check-conventions.sh      self-test for the checker above; CI runs it first
  check-infra-conformance.sh     infra conformance checker (finds nothing here by design)
  githooks/                      pre-commit, commit-msg, pre-push
  gitmessage                     commit message template
skill/
  iso-27001-review/              Claude Code skill: assess content against Annex A using this corpus
    SKILL.md                     the procedure (routing, reading, verdicts, report format)
    topic-index.json             routing table from everyday words to control numbers
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
    "counts": { "checkpoints": 6, "evidence": 6, "defects": 6, "hasLaws": false }
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

It is idempotent and writes nothing outside `.git/config`, apart from setting the executable bit
on the three hook files. It activates `pre-commit` (documentation conventions), `commit-msg`
(message rules), and `pre-push` (blocks a direct push to master). The
hooks are a convenience guardrail and are bypassable; the authoritative gate is CI
(`.github/workflows/docs.yml`), which runs the same checkers.

Everything else needs only Python 3 (standard library only) and bash.

## Working with Claude Code

Open this repository in Claude Code. It reads [CLAUDE.md](CLAUDE.md), the single maintained
instruction file. [AGENTS.md](AGENTS.md) is a symlink to it, so an agent that reads `AGENTS.md`
receives the same rules; `tools/check_corpus.py` fails if it stops being a symlink.

The review skill is installed per user by symlinking its directory into `~/.claude/skills/`. Run
this once from the corpus root. It leaves any existing installation in place:

```bash
mkdir -p "$HOME/.claude/skills"
if [ ! -e "$HOME/.claude/skills/iso-27001-review" ] && [ ! -L "$HOME/.claude/skills/iso-27001-review" ]; then
  ln -s "$PWD/skill/iso-27001-review" "$HOME/.claude/skills/iso-27001-review"
fi
```

For a content review, run `/iso-27001-review` followed by the text or a file path, or with no
argument to assess content pasted earlier in the conversation. Claude Code may also pick the skill
on its own when a request matches its description. The skill resolves the corpus root through the
symlink, so it works from any project. It only reads the corpus; maintaining the corpus is a
separate task governed by `CLAUDE.md`.

## Maintaining

```bash
python3 tools/build_index.py    # regenerate extended/ and the docs/{ko,en}/INDEX.md files
python3 tools/check_corpus.py   # read-only integrity checks
python3 -B -m unittest discover -s tools -p 'test_*.py'
bash harness/test-check-conventions.sh
bash harness/check-conventions.sh
bash harness/check-infra-conformance.sh
git diff --check
```

The builder is deterministic and reproducible: CI regenerates and fails on any diff, so the
committed indexes always match the corpus.

When you add, edit, or delete a control, **update the counterpart document in the other language in
the same commit**. The correspondence is keyed by control number. A Korean-only or English-only edit
is a bug. `tools/check_corpus.py` fails when a control exists in only one language, and when the two
languages carry a different number of items in any counted section; rewording that keeps the counts
equal is caught in review, not by CI.

Adding a control also means adding it to `extended/catalog/controls.json`; `check_corpus.py` fails
when the catalog and the documents disagree in either direction.

The dated verification record and its limits are in [UPDATES.md](UPDATES.md). The installed
playbook guard baseline is v0.1.6; v0.2.0 migration has not been applied. `CLAUDE.md` records
the reference-checkout and upstream revisions checked.

## License

- Code and tooling: MIT. See [LICENSE](LICENSE).
- The corpus (the original explanatory material, the compilation under `docs/`, the generated data
  under `extended/`, and the prose of the meta documents): CC BY 4.0. See
  [LICENSE-CONTENT](LICENSE-CONTENT) and [NOTICE](NOTICE).

These licenses cover this project's own work only. The ISO/IEC 27001 standard text remains the
property of ISO and IEC and is not relicensed, reproduced, or translated here.
