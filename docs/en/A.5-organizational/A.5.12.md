# A.5.12 Classification of information

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.12 Classification of information |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 1.2.1 Identification of information assets (establishing classification criteria and rating importance) (related: 2.1.3 Information asset management) |
| 2013 mapping | 8.2.1 |

## Control objective

This control requires information to be classified according to its confidentiality/integrity/availability requirements and its legal/business importance, using consistent criteria, so that a level of protection proportionate to each class can be applied. A clear classification result lets the organization decide follow-on safeguards such as access control, encryption, storage/transmission, and retention/disposal in proportion to risk. The aim is to prevent both wasted resources from over-protection and exposure from under-protection, while ensuring the whole organization handles information against the same baseline.

## Key checkpoints

1. Is the classification scheme (class definitions, classification criteria, reclassification procedure) documented and approved/published at the organizational level?
2. Do the criteria reflect not only confidentiality but also integrity/availability and legal/regulatory requirements (such as personal data)?
3. Is each asset in the information asset inventory assigned an owner and a classification level, and kept up to date?
4. Are handling rules per classification level (access/storage/transmission/printing/disposal) defined and applied in actual operations?
5. Are reclassification and declassification procedures operated as information ages or its context changes?
6. When information is exchanged with external parties, is a basis for interpreting and mapping classification levels agreed upon?

## Implementation guidance

- Design the class scheme to be simple and fit the organization's size and business (for example, 3 to 4 levels such as public/internal/restricted/confidential). Too many levels reduce practical compliance.
- Describe in each class definition the impact from a confidentiality/integrity/availability perspective (expected damage from disclosure/alteration/disruption), so staff have a basis for deciding the level.
- Link classification to the information asset inventory (A.5.9) so that asset owners assign/approve the class and specify a procedure for periodic re-review.
- Identify legally protected data (personal data, unique identifiers, trade secrets) with separate tags or labels so they connect automatically to the handling rules.
- Define how to mark (label) classification per medium (documents/files/email/databases), and where possible turn the class into metadata using DLP and document security tools for enforcement.
- Assign responsibility for the initial classification of newly created and collected information, and set a default (how to treat unclassified items) to prevent gaps.
- Define the approval authority and recording method for reclassification/declassification/disposal, so aged information is neither over-protected nor left unreviewed.

## Related controls and attributes

- ISO 27001 clauses: 6.1.2/6.1.3 (Information security risk assessment and treatment), 7.5 (Documented information), 8.1 (Operational planning and control)
- Adjacent Annex A: A.5.9 (Inventory of information and other associated assets), A.5.13 (Labelling of information), A.5.10 (Acceptable use of information and other associated assets), A.8.10 (Information deletion), A.8.12 (Data leakage prevention)
- ISMS-P mapping: 1.2.1 Identification of information assets (establishing classification criteria and rating importance) (related: 2.1.3 Information asset management)
- 2013 mapping: 8.2.1 (Classification of information)

## Evidence

- Classification criteria and class definition document, and handling rules per class (policy/guideline)
- Information asset inventory (including owner, classification level, and last review date per asset)
- Labelling examples (document header/footer, file properties, email classification tags)
- Reclassification and declassification approval records
- Training material and completion records related to information classification
- DLP/document security policy configuration screens (basis for mapping controls to each class)

## Nonconformity examples

- Classification levels are defined, but actual assets carry no level, so most information is left unclassified.
- The class definitions cover only confidentiality and do not reflect integrity/availability or legal requirements (such as personal data).
- The asset inventory and the classification scheme are not linked, so owners and levels are not kept current.
- Restricted documents carry no label, so no level-based control is applied when they are taken outside or sent by email.
- No reclassification/declassification procedure exists, so aged confidential information stays over-protected or, conversely, is left unreviewed.
- No classification-mapping basis is agreed with external partners, so a counterpart handles the information at a lower level of protection than intended.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
