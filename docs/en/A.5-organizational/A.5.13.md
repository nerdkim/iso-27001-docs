# A.5.13 Labelling of information

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.13 Labelling of information |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.1.3 Information asset management (related: 1.2.1 Information asset identification) |
| 2013 mapping | 8.2.2 Labelling of information |

## Control objective

This control requires the organization to attach labels that indicate classification levels to information and other associated assets, in line with the classification scheme it has adopted, and to apply and maintain those labels consistently. If information is classified but the result is not shown on the asset itself, people handling the asset cannot recognize its sensitivity, which can lead to improper handling, disclosure, or misdelivery. The aim is therefore to establish a labelling procedure, define how and to what labels are applied, and ensure consistent marking across physical and electronic forms so that classification decisions translate into actual handling controls.

## Key checkpoints

1. Is a labelling procedure linked to the information classification scheme established, with label notation and the asset types to be labelled defined?
2. Are the method and location for applying labels defined per form, such as documents, electronic files, email, storage media, and system screens/printouts?
3. Are labels applied to assets consistently according to their classification level, and is there a rule for handling unclassified or unlabelled assets?
4. Are employees and external parties educated so they understand the meaning of labels and the handling rules for each level?
5. Is the adequacy of labelling reviewed periodically, and are labels updated together when a classification changes?

## Implementation guidance

- Define label notation rules that map one-to-one to the organization's classification scheme (for example, Public/Internal/Restricted/Confidential), and standardize the name and marking format of each level (color, header/footer, watermark, metadata tag, and so on).
- Make the labelling targets explicit by form: paper documents (cover/header/footer), electronic documents and files (file naming rules, document properties, watermarks), email (subject/body marking, classification tags), storage media (external labels), system screens and printouts, and databases/datasets (classification metadata).
- Reflect in the procedure that classification and labelling are performed at the point information is created or acquired, and embed default labelling features into document templates and the mail system to reduce manual omissions.
- Use automated labelling/classification tools (DLP, document security, mail classification solutions) to achieve consistency and accuracy across large volumes of assets, and validate the results of automatic labelling.
- Link handling rules per level (viewing/copying/transmission/storage/disposal) to the labels and communicate them, and raise awareness of what labels mean and what must be complied with through training for employees and external parties.
- Update labels together whenever a classification level changes or the sensitivity of information changes, and periodically review the status and accuracy of labelling to remediate omissions and mislabelling.

## Related controls and attributes

- ISO 27001 clauses: 7.5 (Documented information), 8.1 (Operational planning and control), 6.1 (Actions to address risks)
- Adjacent Annex A: A.5.12 (Classification of information), A.5.9 (Inventory of information and other associated assets), A.5.10 (Acceptable use of information and other associated assets), A.5.14 (Information transfer), A.7.10 (Storage media), A.8.12 (Data leakage prevention)
- ISMS-P mapping: 2.1.3 Information asset management (related: 1.2.1 Information asset identification)
- 2013 mapping: 8.2.2 Labelling of information

## Evidence

- Labelling procedure linked to the classification scheme (notation, labelling targets, methods per form)
- Label standards per level (color/header/watermark/metadata tag, and so on) and document/mail templates
- Examples of labels applied to actual assets (documents, email, storage media, screen/printout captures)
- Configuration and applied-result records of automated labelling/classification tools
- Labelling-related training materials and completion records for employees and external parties
- Results of labelling status reviews/inspections and records of remediation for mislabelling/omissions

## Nonconformity examples

- A classification scheme exists, but there is no labelling procedure or criteria, so classification levels are not marked on assets.
- Restricted/confidential documents carry no classification marking, so handlers do not recognize their sensitivity and treat them like ordinary documents.
- Labels are applied to paper documents, but there are no marking rules for other forms such as electronic files, email, and storage media, resulting in inconsistency.
- A classification level is raised, but the existing label is not updated, so the marking no longer matches the actual sensitivity.
- There is no training on the meaning of labels and the handling rules per level, so employees neither recognize nor comply with the labels.
- The labelling status is not reviewed, leaving many assets unlabelled or mislabelled.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
