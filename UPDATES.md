# Source basis and update tracking

> 한국어: [UPDATES.ko.md](UPDATES.ko.md)

This corpus has an unusual shape, and this document records it so a later maintainer does not have
to reconstruct it:

- a **small factual layer** taken from the public Annex A control list, which is pinned to a
  standard edition and changes only when ISO revises the standard, and
- a **large original layer** written by this project, which is not pinned to anything upstream and
  is maintained on its own terms.

Confusing the two is the failure mode this document exists to prevent.

Last checked: 2026-07.

## 1. Source versions

| Part of the corpus | Basis | Edition |
|---|---|---|
| Control numbers, titles, and theme classification (`extended/catalog/controls.json`) | the **public** list of ISO/IEC 27001:2022 Annex A | 2022 |
| 통제 목적, 주요 확인사항, 이행 지침, 관련 통제 및 속성, 증적자료, 부적합 사례 | **original material** written by this project for practical reference | not an upstream edition |
| The English documents under `docs/en/` | this project's own English edition | see 2.2 |

The 93 controls across four themes (A.5 organizational 37, A.6 people 8, A.7 physical 14,
A.8 technological 34) follow the 2022 revision, which restructured Annex A from the 114 controls of
the 2013 edition.

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
Korean-only or English-only content edit is a defect, and CI rejects it.

### 2.3 Confirmed as current

| Item | Status |
|---|---|
| ISO/IEC 27001 edition | 2022 is the current revision. No later revision of the standard is reflected here. |
| Control list | All 93 controls are present in both languages, and `tools/check_corpus.py` fails when the catalog and the documents disagree in either direction. |
| ISO/IEC 27002:2022 | Not used as a source. Its guidance text is in scope of the same copyright boundary as the standard. |

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
