<!-- playbook standard PR template (docs/12, docs/20). Write PRs in English (docs/16 4.1).
     This is a documents-only repository: there is no build output and no deploy, so the
     surface below is content and tooling, not a deploy surface. -->

## Summary
<!-- What changes and why, in 1-3 lines. -->

## Change surface
<!-- Check what applies. -->
- [ ] corpus content (`docs/ko/` and `docs/en/`, the control documents)
- [ ] control catalog (`extended/catalog/controls.json`, which controls must exist)
- [ ] generated indexes (`extended/manifest.json`, `extended/index/`, `docs/{ko,en}/INDEX.md`)
- [ ] tooling (`tools/build_index.py`, `tools/check_corpus.py`)
- [ ] CI / harness / repository meta docs
- [ ] source pin (`UPDATES.md` and `UPDATES.ko.md`)

## Bilingual parity
<!-- A Korean-only or English-only content edit is a bug, and CI rejects it. -->
- [ ] Korean and English counterparts changed in **this same commit**, keyed by control number
- [ ] N/A (this PR touches no control content)

## Copyright boundary
<!-- The hard rule of this repository. Control numbers, titles, and theme classification come
     from the PUBLIC list of ISO/IEC 27001:2022 Annex A. Everything else here is original
     material written for practical reference. -->
- [ ] no normative text, implementation guidance, or attribute table of ISO/IEC 27001:2022 is reproduced, paraphrased close to the source, or translated in this change
- [ ] each touched document still carries its source and limitation notice at the bottom
- [ ] N/A (this PR touches no control content)

## Verification
<!-- The exact commands you ran and their results; make it reproducible (playbook docs/20 5). -->
- `python3 tools/check_corpus.py` → result:
- `python3 tools/build_index.py` then `git diff --exit-code -- extended docs` → result:
- `bash harness/check-conventions.sh` → result:

## Consumer impact (the manifest contract)
<!-- extended/manifest.json (schema corpus-manifest/v3) is a PUBLISHED CONTRACT read by consumers
     outside this repository. Renaming a field or changing a shape is a breaking change: bump the
     `schema` string and land the consumer change with it. -->
- [ ] no schema change (counts or content only, consumer unaffected)
- [ ] schema changed → `schema` string bumped, and every consumer has a matching change ready
- [ ] stable keys untouched: standard id `iso-27001`, theme ids `organizational` / `people` / `physical` / `technological`, and the control numbers

## Rollback
<!-- Concrete steps: revert commit, then re-run build_index.py if the indexes moved. -->
