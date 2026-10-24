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
  ISO/IEC 27001:2022 Annex A (Table A.1). That list is factual reference data. The English titles
  keep the wording of that table; the Korean titles are this collection's own rendering, not an
  official translation.
- The **explanatory body of every document is original material written for this collection**:
  control objective, key checkpoints, implementation guidance, related controls, evidence examples,
  and nonconformity examples. It is **not** the normative text of ISO/IEC 27001:2022 or 27002:2022,
  and it is not a translation of that text.
- The `Control type (ref.)` and `Security properties (ref.)` rows of each metadata table are
  **this collection's own classification**, not the attribute values of ISO/IEC 27002:2022, and
  they may differ from those values. Do not cite them as ISO's attributes.
- The standard's normative text, its implementation guidance, its attribute tables, and third-party
  commentary are **never reproduced verbatim** in this repository.
- For anything authoritative, compare against a **licensed copy of the standard**. Every document
  carries this notice in its footer, and CI fails if a document is missing it.

That boundary also decides how this corpus is updated: there is no upstream text to re-sync against,
so an ISO revision changes the **control list** here, not the wording of the explanations.
[UPDATES.md](UPDATES.md) records the edition each layer is pinned to and how each layer is
maintained.

[REVIEW.md](REVIEW.md) records the 2026-09-17 full body review of all 186 control documents,
including corrections, control-by-control coverage, and verification limits. Changes made after
that review, including the 2026-10-20 fact check, are listed in its section 5 and in
[UPDATES.md](UPDATES.md).

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
  test_check_corpus.py           regression tests for document boundaries, the AGENTS.md link,
                                 and the forbidden characters
harness/                         playbook guard set, refreshed by the playbook installer (not by hand)
  bootstrap-hooks.sh             wire this clone to the git hooks (run once, see Setup)
  verify.sh                      run every guard check (--self-tests adds the checkers' own tests)
  check-conventions.sh           documentation conventions checker (playbook docs/16)
  conventions-exclude            this repository's own file: docs/ko/, which the conventions checker skips
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
bash harness/bootstrap-hooks.sh
```

It is idempotent and writes nothing outside `.git/config`, apart from setting the executable bit
on the hook files. It activates `pre-commit` (guard integrity, documentation conventions, security
checks), `commit-msg` (message rules), and `pre-push` (blocks a direct push to main), and sets the
commit message template. The hooks are a convenience guardrail and are bypassable. The
authoritative gates are the two checks that `main` requires: `docs-conventions`
(`.github/workflows/conventions.yml`, the same guard checkers) and `corpus-integrity`
(`.github/workflows/docs.yml`, the corpus tools below).

Everything else needs only Python 3 (standard library only), bash, and GNU grep with `-P` support
(the guard checkers and the `commit-msg` hook use it).

## Working with Claude Code

Open this repository in Claude Code. It reads [CLAUDE.md](CLAUDE.md), the single maintained
instruction file. [AGENTS.md](AGENTS.md) is a symlink to it, so an agent that reads `AGENTS.md`
receives the same rules; `tools/check_corpus.py` fails if it stops being a symlink. The playbook
installer also writes `.claude/settings.json`: the commit co-author, the Korean writing style hooks,
and a Stop hook that asks for the documents a change needs.

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
bash harness/verify.sh          # every guard check, conventions included
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

The documentation conventions checker skips `docs/ko/` (`harness/conventions-exclude`). The
Korean control documents keep the Korean renderings of IT terms that their readers use, and the
playbook term rule would otherwise report them. `check_corpus.py` still scans every control
document for the forbidden characters, and `docs/en/` stays under every conventions check.
[CLAUDE.md](CLAUDE.md) gives the reasoning.

The dated verification record and its limits are in [UPDATES.md](UPDATES.md). The playbook guard
set is v0.10.11 (`harness/ADOPTED`); section 2.7 of UPDATES.md records the upgrade.

## License

- Code and tooling: PolyForm Noncommercial 1.0.0. See [LICENSE](LICENSE).
- The corpus (the original explanatory material, the compilation under `docs/`, the generated data
  under `extended/`, and the prose of the meta documents): CC BY-NC 4.0. See
  [LICENSE-CONTENT](LICENSE-CONTENT) and [NOTICE](NOTICE).

Both licenses allow noncommercial use only; commercial use needs a separate permission from
NerdKim. They are source-available terms, not open source licenses in the OSI sense. Until
2026-10-24 the project was offered under MIT and CC BY 4.0, and copies obtained under those terms
keep them.

These licenses cover this project's own work only. The ISO/IEC 27001 standard text remains the
property of ISO and IEC and is not relicensed, reproduced, or translated here.
