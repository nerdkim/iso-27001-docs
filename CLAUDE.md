# CLAUDE.md

This repository is a **documents-only** reference corpus: a practical reference for the 93 controls
of ISO/IEC 27001:2022 Annex A, one Markdown file per control, bilingual in Korean and English.
There is no application, no build output, and no infrastructure here. This file defines the rules
AI agents (Claude Code, OpenAI Codex, and so forth) follow when **maintaining this repository**.

The common engineering standard (interaction, priority, commit, punctuation, terminology,
security) is **not copied into this file**; the playbook docs are the single source. Before
working, read `playbook/docs/README.md` and follow it. This file keeps only what is specific to
this repository. See the managed block at the bottom.

> Project kind: **document corpus** (no application). Branch model: **develop-master** (2-branch).
>
> `AGENTS.md` is a symbolic link to this `CLAUDE.md` (identical content; per playbook `docs/10` the
> real file is `CLAUDE.md`). Claude Code reads `CLAUDE.md`; other agents such as Codex read
> `AGENTS.md`. Edit only this file and both are updated.

## Copyright boundary (the rule that overrides convenience)

This is the single most important constraint in this repository.

- Control **numbers, titles, and the four-theme classification** are based on the **public list** of
  ISO/IEC 27001:2022 Annex A, held in `extended/catalog/controls.json`. That is factual reference
  data and may be used.
- The **explanatory body of every document is newly written original material** for practical
  reference. **Never** reproduce, paraphrase closely, or translate the standard's normative text,
  its implementation guidance, its attribute tables, or third-party commentary.
- Every document **must** end with the source and limitation footer stating this boundary.
  `tools/check_corpus.py` fails when a document is missing it, and CI runs that check.
- A licensed copy of the standard may be consulted locally for an authoritative comparison, but it
  is never committed: `references/` is git-ignored for exactly this reason.
- When a request would require the standard's text to answer it, say so and stop. Do not fill the
  gap with invented normative language.

## Repository layout

- `docs/` : the per-control documents. `docs/<lang>/<theme-dir>/<no>.md`, where `<lang>` is `ko` or
  `en` and the two languages mirror each other with identical relative paths. Organizational 37 plus
  People 8 plus Physical 14 plus Technological 34 is 93 controls per language, plus one generated
  `INDEX.md` per language.
- `extended/` : `catalog/controls.json` holds the public Annex A list; `manifest.json` is the
  published contract; `index/` holds the generated flat index, nonconformity rulebook, and evidence
  dictionary. `extended/README.md` states the operating rules for AI use of the corpus.
- `tools/` : `build_index.py` regenerates every derived index from `docs/`; `check_corpus.py` runs
  read-only integrity checks. Both are dependency-free (Python standard library only).
- `harness/` : the playbook guard set (documentation conventions checker, git hooks). `core.hooksPath`
  is local `.git/config` state and does not travel with a clone, and this repository has no
  `package.json` to hang a `prepare` script on, so the wiring is `bash harness/install-hooks.sh`,
  run once per clone. It is idempotent and writes nothing outside `.git/config`.
- `README.md` / `README.ko.md` : repository introduction (English default, Korean companion).
- `UPDATES.md` / `UPDATES.ko.md` : the source pin and the update model. It separates the small
  **factual layer** (the public Annex A control list, pinned to the 2022 revision) from the large
  **original layer** (the explanatory bodies, pinned to nothing upstream). Confusing the two is the
  failure mode it exists to prevent: there is no upstream text to re-sync against, so an ISO revision
  changes the control list here, not the wording of the explanations.
- `docs/README.md` / `docs/README.ko.md` : the entry point for someone standing inside `docs/`
  (what these documents are and are not, read-only rule, layout, section structure, manifest-first
  routing). It sits outside the `docs/<lang>/**` glob that both builders use, so it is invisible to
  them.

## Maintenance rules (repository-specific)

Common rules (commit author, branch and GitOps flow, forbidden punctuation, terminology, tests
mandatory) follow the playbook docs. Only repository-specific rules are kept here.

- **English-default meta docs (`X.md` plus `X.ko.md`)**: code, comments, commit messages, and PR
  titles and bodies are written in English. Meta documentation is **bilingual** with the **English
  version as the default `X.md`** and a **Korean companion `X.ko.md`**. Keep the pair in sync: edit
  both language versions in the same commit, and each version links to its counterpart
  (`> 한국어: [X.ko.md]` and `> English: [X.md]`). `CLAUDE.md` and `AGENTS.md` stay **English-only**
  (single spec; `AGENTS.md` is a symlink, per playbook `docs/10`).
- **Keep Korean and English in sync (important)**: when you add, edit, or delete a control's
  content, **update the corresponding document in the other language in the same commit**. The
  correspondence is keyed by control number. `tools/check_corpus.py` and CI enforce this.
- **Control documents** keep the 6-section structure (통제 목적 / 주요 확인사항 / 이행 지침 /
  관련 통제 및 속성 / 증적자료 / 부적합 사례), the metadata table at the top, and the source and
  limitation footer at the bottom. The character rules from playbook `docs/16` apply, except that
  `docs/ko/` and `docs/en/` are a confirmed exception listed in `harness/conventions-exclude`.
- **Regeneration**: `docs/` and `extended/catalog/controls.json` drive everything derived. Run
  `python3 tools/build_index.py` after any change and commit the result in the same commit. CI
  regenerates and fails on any diff, so a stale `extended/manifest.json` blocks the merge.
- **Do not rename these stable keys**: the standard id `"iso-27001"`, the theme ids
  `organizational` / `people` / `physical` / `technological`, and the control numbers. The web
  viewer and the manifest consumers depend on them.
- **The manifest is a published contract.** `extended/manifest.json` is read by consumers outside
  this repository. Renaming a field or changing a shape breaks them, so bump the `schema` string and
  land the consumer change with it.

## nerdkim 공통 엔지니어링 표준(playbook)

이 repository는 nerdkim 공통 엔지니어링 표준을 따른다. 표준 문서 전체는 함께 두는 `./playbook`에
있다(작업용 참조본이며 git에는 포함하지 않는다). 작업을 시작하기 전에 `playbook/docs/README.md`를 읽고,
거기서 안내하는 규칙(응대 방식, commit, 문장 부호, 용어, 보안 등)을 그대로 따른다. 그 규칙들은 이 파일에
옮겨 적지 않는다. 정본은 언제나 playbook 문서다.

`./playbook`이 없으면 먼저 확보한다: `gh repo clone nerdkim/playbook playbook`(private, gh 인증).
표준을 최신으로 맞추려면 `git -C playbook pull` 후 `bash playbook/install-playbook.sh`를 다시 실행한다.

playbook 버전: v0.1.6 (동기화 기준일 2026-07-21)
