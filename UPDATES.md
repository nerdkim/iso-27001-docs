# Source basis and update tracking

> 한국어: [UPDATES.ko.md](UPDATES.ko.md)

This corpus has an unusual shape, and this document records it so a later maintainer does not have
to reconstruct it:

- a **small factual layer** taken from the public Annex A control list, which is pinned to a
  standard edition and changes only when ISO revises the standard, and
- a **large original layer** written by this project, which is not pinned to anything upstream and
  is maintained on its own terms.

Confusing the two is the failure mode this document exists to prevent.

Last checked: 2026-09-17. This is a dated verification, not a promise of future currency.

## 1. Source versions

| Part of the corpus | Basis | Edition |
|---|---|---|
| Control numbers, titles, and theme classification (`extended/catalog/controls.json`) | the **public** list of ISO/IEC 27001:2022 Annex A | 2022, not touched by Amd 1:2024 |
| Control objective, Key checkpoints, Implementation guidance, Related controls and attributes, Evidence, Nonconformity examples | **original material** written by this project for practical reference | not an upstream edition |
| The English documents under `docs/en/` | this project's own English edition | see 2.2 |
| ISMS-P item numbers and names in the metadata tables and `Related controls and attributes` | the **public** item list of the Korean ISMS-P 인증기준 | the 101-item set of the 2023.11 인증기준 안내서 |

The 93 controls across four themes (A.5 organizational 37, A.6 people 8, A.7 physical 14,
A.8 technological 34) follow the 2022 revision, which restructured Annex A from the 114 controls of
the 2013 edition. That list is still current: as of the check date there is no later revision of
ISO/IEC 27001, and the one amendment published since 2022 does not reach Annex A. Section 2.3
explains why.

## 2. What is and is not tracked upstream

### 2.1 The copyright boundary is also the update boundary

The normative text of ISO/IEC 27001:2022, and the implementation guidance and attribute tables of
ISO/IEC 27002:2022, are **not reproduced, paraphrased close to the source, or translated here**.
Only the control numbers, titles, and theme classification come from the public list. Everything
else is original.

This has a direct consequence for updates: there is no upstream text to re-sync against. A change
in the standard's wording does not mechanically propagate into these documents, because these
documents never carried that wording in the first place. What an ISO revision **does** change is the
control list, and that is what `extended/catalog/controls.json` tracks.

### 2.2 The bilingual pair is peer to peer

The Korean and English documents here are both this project's own writing. Neither is a translation
of an official ISO text, and neither is subordinate to the other in the way `docs/ko/` is
authoritative over `docs/en/` in the ISMS-P corpus. They must still say the same thing: a
Korean-only or English-only content edit is a defect. `tools/check_corpus.py` fails when a control
exists in only one language, and when the two languages carry a different number of items in any
counted section, so CI rejects a structural one-language edit. Rewording that leaves the item counts
equal is caught in review, not by CI.

### 2.3 The 2024 amendment does not reach Annex A

ISO/IEC 27001:2022 was amended in February 2024 by **ISO/IEC 27001:2022/Amd 1:2024, "Climate action
changes"**, one of a coordinated set of amendments ISO issued across roughly 31 management system
standards. It adds a climate-change consideration to main-body clause **4.1** and a related note to
clause **4.2**.

It changes nothing in Annex A. The 93 controls, their numbers, their titles, and the four themes are
exactly as published in 2022, so the factual layer of this corpus is unaffected and no control
document needed a content change for it.

Recording this is the whole point of the register. Someone who reads "2022" here and "amended in
2024" elsewhere should be able to resolve the apparent conflict without opening the standard:
certification is against the 2022 edition **as amended**, but the amendment lives in the main body,
which an Annex A corpus does not cover. Five documents cite clause 4.1 or 4.2 in their
`Related controls and attributes` section (A.5.5, A.5.20, A.5.31, A.5.32, A.5.34). Those lines are
pointers into the main body, not summaries of it, and they remain correct as they stand.

For what the amendment actually requires, use a licensed copy. This corpus does not restate
main-body requirements, and the rule in section 3 against reconstructing the standard's wording
applies to the amendment exactly as it applies to everything else.

### 2.4 Confirmed as current

Every row below was verified on the check date at the top of this document.

| Item | Status |
|---|---|
| ISO/IEC 27001 edition | The [ISO catalogue](https://www.iso.org/standard/27001) lists the 2022 edition as published. Do not infer the absence of future revision work from that status. |
| ISO/IEC 27001:2022/Amd 1:2024 | Published February 2024. Amends main-body clauses 4.1 and 4.2 only. Annex A unchanged, so this corpus is unaffected. See 2.3. |
| Annex A control list | 93 controls, four themes, 2022 numbering, unchanged. All 93 are present in both languages, and `tools/check_corpus.py` fails when the catalog and the documents disagree in either direction. |
| ISO/IEC 27002 | The [ISO catalogue](https://www.iso.org/standard/75652.html) lists edition 3, published February 2022, with an English corrected version dated March 2022. Its guidance is not reproduced here. |
| ISO/IEC 27000 | The [ISO catalogue](https://www.iso.org/standard/27000) records publication of edition 6 on 3 July 2026, titled "Overview". This is a different document, not a replacement edition of ISO/IEC 27001 or Annex A. |
| 2013 transition | The transition deadline was 31 October 2025. [IAF MD 26:2023](https://iaf.nu/iaf_system/uploads/documents/IAF_MD26_Issue_2_15012023.pdf), section 3. |
| ISMS-P mapping basis | The [official resource list](https://isms-p.or.kr/ntcn/rcsrm/selectGnrlRcsrmList.do) still publishes the 2023.11 guide used for this corpus's mappings. The [10 April 2026 reform announcement](https://isms-p.or.kr/ntcn/ntc/selectGnrlNtcList.do?pageIndex=2) is a separate policy development. An announcement is not proof that every planned measure is in force; verify the applicable notice and effective date before changing a mapping or claiming a new obligation. This repository does not track all ISMS-P legal changes. |

### 2.5 Repository verification and limits

- All 186 control documents were checked for catalog coverage, bilingual section counts, metadata
  agreement, references, section order, and the complete source/limitation footer. Derived indexes
  were regenerated and checked for reproducibility.
- `tools/check_corpus.py` checks that `AGENTS.md` is a working symlink to `CLAUDE.md` and that
  the skill source files exist. Regression tests cover missing or replaced notices, extra
  sections, a missing or copied `AGENTS.md`, and a missing skill source. The conventions checker
  tests the Korean path exemption separately from punctuation and spacing checks.
- On 2026-09-23 the agent setup returned to Claude Code. The `.agents/skills` discovery link
  added for Codex on 2026-09-17 was removed. The skill is installed through `~/.claude/skills/`,
  and `AGENTS.md` stays a symlink to `CLAUDE.md` for other agents.
- The full body review read all 93 Korean/English pairs and corrected 73 pairs (146 documents).
  The remaining 20 pairs had no substantive finding in this pass. [REVIEW.md](REVIEW.md) records
  every control's disposition, factual references, and the reviewed file snapshot. The earlier
  unsupported numeric minima in A.6.3 and the review skill were also removed. Automated checks
  cannot establish semantic equivalence or certification sufficiency. No licensed standard text
  was used for an authoritative comparison, and the crosswalks remain reference aids.
- The installed playbook guard baseline remains v0.1.6, with repository-specific fixes. The local
  reference checkout is v0.2.0 at `d8a44e5`; upstream `develop` was checked at `692444c`.
  Full v0.2.0 adoption includes incompatible language defaults and Claude-specific tooling.
  On 2026-09-17 the owner excluded that migration from this repository's current work.
  The installed baseline remains in place; the agent setup is separate from a guard upgrade.

## 3. Operating principle

- **An ISO revision affecting the public control list** triggers a catalog review. When one lands: update
  `extended/catalog/controls.json` first (it defines which controls must exist), then add, retire,
  or renumber the documents in both languages **in the same commit**, then regenerate with
  `python3 tools/build_index.py`. Record the plan in this document before touching `docs/`.
- **ISMS-P item-list changes** trigger a separate review of the cross-reference mappings in both
  languages. They do not change the Annex A catalog. Record the effective source and date first.
- **The original explanatory layer** is improved on its own schedule, without an upstream trigger:
  clearer guidance, better evidence lists, more realistic nonconformity examples. This is ordinary
  content work and does not belong in the register above.
- **Never close a gap by reconstructing the standard's wording.** If the corpus does not cover
  something, the correct move is to say so and point the reader at a licensed copy of the standard,
  not to fill it in from memory of the text.
- Update the "Last checked" date, direct source links, and verification limits whenever this register
  is reviewed, even when nothing changed.
  A stale check date and "nothing has changed upstream" look identical otherwise.

## 4. Sources checked

- ISO/IEC 27001:2022 Annex A control list (numbers, titles, themes): the publicly available control
  listing. Authoritative comparison is done against a **licensed** copy of the standard, which is
  not redistributed with this repository.
- Korean control titles: rendered by this project for consistency across the corpus; they are not an
  official Korean translation of the standard, and the standard's own terminology prevails for any
  formal use.
- Edition and amendment status (section 2.4): the ISO catalogue pages linked above and
  [ISO/IEC 27001:2022/Amd 1:2024](https://www.iso.org/standard/88435.html).
  The [ISO/IAF announcement](https://www.iso.org/files/live/sites/isoorg/files/standards/popular_standards/management_systems/ISO-IAF%20Joint%20Communique%20Feb%202024.pdf)
  identifies the affected main-body clauses. This check uses publication metadata and change scope;
  it does not reproduce the amended requirements.
- 2013 transition (section 2.4): IAF MD 26, the International Accreditation Forum's transition
  requirements for ISO/IEC 27001:2022, which fix the expiry of 2013-edition certificates at
  31 October 2025.
- ISMS-P claims (sections 1 and 2.4): the published item list of the ISMS-P 인증기준 안내서, 2023.11
  revision on the official resource list linked above, and the dated reform announcement. Only
  item numbers, item names, and publication status are used as factual reference data. Crosswalks
  between standards are this project's reference mappings, not official equivalence determinations.
