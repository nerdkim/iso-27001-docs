# Source basis and update tracking

> 한국어: [UPDATES.ko.md](UPDATES.ko.md)

This corpus has an unusual shape, and this document records it so a later maintainer does not have
to reconstruct it:

- a **small factual layer** taken from the public Annex A control list, which is pinned to a
  standard edition and changes only when ISO revises the standard, and
- a **large original layer** written by this project, which is not pinned to anything upstream and
  is maintained on its own terms.

Confusing the two is the failure mode this document exists to prevent.

Last checked: 2026-09.

## 1. Source versions

| Part of the corpus | Basis | Edition |
|---|---|---|
| Control numbers, titles, and theme classification (`extended/catalog/controls.json`) | the **public** list of ISO/IEC 27001:2022 Annex A | 2022, not touched by Amd 1:2024 |
| Control objective, Key checkpoints, Implementation guidance, Related controls and attributes, Evidence, Nonconformity examples | **original material** written by this project for practical reference | not an upstream edition |
| The English documents under `docs/en/` | this project's own English edition | see 2.2 |

The 93 controls across four themes (A.5 organizational 37, A.6 people 8, A.7 physical 14,
A.8 technological 34) follow the 2022 revision, which restructured Annex A from the 114 controls of
the 2013 edition. That list is still current: as of the check date there is no later revision of
ISO/IEC 27001, and the one amendment published since 2022 does not reach Annex A. Section 2.3
explains why.

## 2. What is and is not tracked upstream

### 2.1 The copyright boundary is also the update boundary

The normative text of ISO/IEC 27001:2022, its implementation guidance, and its attribute tables are
**not reproduced, paraphrased close to the source, or translated here**. Only the control numbers,
titles, and theme classification come from the public list. Everything else is original.

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
| ISO/IEC 27001 edition | 2022 is still the current edition. There is no 2026 revision, and none is in progress. |
| ISO/IEC 27001:2022/Amd 1:2024 | Published February 2024. Amends main-body clauses 4.1 and 4.2 only. Annex A unchanged, so this corpus is unaffected. See 2.3. |
| Annex A control list | 93 controls, four themes, 2022 numbering, unchanged. All 93 are present in both languages, and `tools/check_corpus.py` fails when the catalog and the documents disagree in either direction. |
| ISO/IEC 27002 | Still the 2022 edition, unamended. The climate amendment applied to management system standards; 27002 is guidance, not one. Not used as a source here in any case. |
| ISO/IEC 27000 | Sixth edition published July 2026, retitled from "Overview and vocabulary" to "Overview", and no longer the vocabulary reference for the ISMS family. It does not change Annex A and is not a source for this corpus. |
| 2013 transition | Closed. Certificates issued against the 2013 edition expired on 31 October 2025. |

## 3. Operating principle

- **A new ISO revision** is the only upstream trigger. When one lands: update
  `extended/catalog/controls.json` first (it defines which controls must exist), then add, retire,
  or renumber the documents in both languages **in the same commit**, then regenerate with
  `python3 tools/build_index.py`. Record the plan in this document before touching `docs/`.
- **The original explanatory layer** is improved on its own schedule, without an upstream trigger:
  clearer guidance, better evidence lists, more realistic nonconformity examples. This is ordinary
  content work and does not belong in the register above.
- **Never close a gap by reconstructing the standard's wording.** If the corpus does not cover
  something, the correct move is to say so and point the reader at a licensed copy of the standard,
  not to fill it in from memory of the text.
- Update the "Last checked" date above whenever this register is reviewed, even when nothing changed.
  A stale check date and "nothing has changed upstream" look identical otherwise.

## 4. Sources checked

- ISO/IEC 27001:2022 Annex A control list (numbers, titles, themes): the publicly available control
  listing. Authoritative comparison is done against a **licensed** copy of the standard, which is
  not redistributed with this repository.
- Korean control titles: rendered by this project for consistency across the corpus; they are not an
  official Korean translation of the standard, and the standard's own terminology prevails for any
  formal use.
- Edition and amendment status (section 2.4): confirmed against the ISO catalogue entry for
  ISO/IEC 27001:2022/Amd 1:2024 and against published summaries of the 2026 ISO/IEC 27000 edition.
  This check covers only which documents exist and what they cover, never their text.
