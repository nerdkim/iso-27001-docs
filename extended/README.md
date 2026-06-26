# extended

> 한국어: [README.ko.md](README.ko.md)

The layer that lets an AI agent **use** the `docs/` corpus without re-reading all of it, and the
operating rules that keep that use honest. Everything here is generated from `docs/` plus
`catalog/controls.json`, except this readme pair.

## What is in here

```
catalog/controls.json               the public Annex A control list: number, theme, Korean and
                                    English title. Factual reference data, and the source of truth
                                    for which controls must exist.
manifest.json                       machine-readable index of every document (schema
                                    corpus-manifest/v3). The published contract: this is what the
                                    web viewer and any other consumer reads.
index/control-index.csv             flat index for spreadsheet or human review
index/nonconformity-rulebook.json   the Korean 부적합 사례 of all 93 controls, keyed by control
                                    number. Check rules for self-assessment and internal audit prep.
index/evidence-dictionary.json      the Korean 증적자료 of all 93 controls, keyed by control number.
                                    Reference dictionary for evidence-to-control mapping.
```

Regenerate everything with `python3 tools/build_index.py` from the repository root. The build is
deterministic, and CI fails if the committed output drifts from `docs/`.

## Operating rules for AI use

These are the rules a consuming agent must follow. Reflect them into the consuming environment's
`CLAUDE.md` or `AGENTS.md`.

1. **`docs/` is read-only.** Never create, modify, or delete anything under `docs/` while using the
   corpus. Write derived output somewhere in the consuming workspace, never back into this
   repository.
2. **Manifest-first routing.** Read `manifest.json` first and narrow to the relevant control
   numbers and `path` values. Then read only those documents. Do not grep across all of `docs/`.
3. **Cite every claim.** Attach the `docs/` path and the section name to each statement, in the
   form `[Source: docs/ko/A.5-organizational/A.5.1.md > 주요 확인사항]`. If you cannot produce a
   citation, do not assert; say that the corpus does not cover it.
4. **Stay inside the corpus.** The authoritative sources for this repository are the 186 `.md`
   documents, `manifest.json`, `index/*`, and `catalog/controls.json`. Do not assert control
   requirements, figures, or thresholds from general model knowledge.
5. **Respect the copyright boundary.** The explanatory bodies here are original material, not the
   standard. Never present them as the normative text of ISO/IEC 27001:2022, and never fill a gap by
   reconstructing the standard's wording. For an authoritative answer, direct the reader to a
   licensed copy of the standard.
6. **Human gate.** Certification-readiness judgments, final conformity determinations, and
   remediation-completion determinations are decided by a person, not by the agent. Present findings
   as candidates for review.

## Example routing

A question such as "what evidence proves access control is operating?" resolves as:

1. In `manifest.json`, find controls whose `name` relates to access control (the A.8.2 to A.8.5
   range and A.5.15).
2. Read only those documents and pull their `증적자료` and `부적합 사례` sections, or read the same
   content directly out of `index/evidence-dictionary.json` and `index/nonconformity-rulebook.json`
   when only the lists are needed.
3. Answer with a citation per item, and mark anything the corpus does not cover as unverified.
