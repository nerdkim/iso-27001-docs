# A.8.11 Data masking

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.11 Data masking |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality |
| ISMS-P mapping | 3.2.5 Pseudonymized data processing |
| 2013 mapping | New in 2022 |

## Control objective

This control requires the organization to limit unnecessary exposure of sensitive data, especially personal data, by applying techniques such as masking, pseudonymization, and anonymization in line with access rights, business need, and legal requirements. When data is shown on screen, used in development/test environments, or shared/analyzed externally, the original values should not be revealed in full, reducing the risk of unauthorized viewing and disclosure. The key is to strike a balance that preserves data usefulness while lowering re-identification potential to a controllable level.

## Key checkpoints

1. Are the target data (resident registration numbers, card numbers, contact details, account numbers, and so on) and the criteria for applying masking/pseudonymization/anonymization defined?
2. Is the extent of exposure (full/partial disclosure, number of masked digits, and so on) differentiated according to access rights and business need?
3. Are masked/pseudonymized/synthetic data used instead of real data in non-production environments such as development, test, and training?
4. Are the applied techniques designed and validated so that re-identification risk (for example, through combinations of quasi-identifiers) is sufficiently reduced?
5. Is alignment with legal requirements (such as personal data protection law) ensured?
6. Are approval/logging controls in place for unmasking (viewing originals) and for exception handling?

## Implementation guidance

- Identify the fields to be masked based on the data classification results, and document the applicable technique and exposure extent per field as a standard.
- Distinguish and apply static masking (permanent transformation when storing or generating copies) and dynamic masking (real-time transformation at query time) according to the use case.
- Select techniques such as partial masking, substitution, shuffling, tokenization, pseudonymization, anonymization, and synthetic data, balancing risk against data usefulness.
- Integrate with role-based access control (RBAC) to differentiate exposure by role/duty, and apply masking consistently across all output paths, including screens, APIs, downloads, and logs, not just the display.
- Assess re-identification risk (for example, k-anonymity and review of quasi-identifier combinations) and revalidate periodically when data structures or business processes change.
- Store masking rules and the keys/mapping tables (additional information) used for pseudonymization securely and separately, and control access and change history.

## Related controls and attributes

- ISO 27001 clauses: 6.1 (Actions to address risks and opportunities), 8.1 (Operational planning and control)
- Adjacent Annex A: A.5.12 (Classification of information), A.5.34 (Privacy and protection of PII), A.8.10 (Information deletion), A.8.12 (Data leakage prevention), A.8.4 (Access to source code), A.8.33 (Test information)
- ISMS-P mapping: 3.2.5 Pseudonymized data processing (related: 2.8.4 Test data security, 2.6.3 Application access)
- 2013 mapping: New in 2022

## Evidence

- Data masking policy/standard and the list of target fields
- Masking rule definitions and captures of applied screens/query results (including exposure differentiated by privilege)
- Non-production data generation procedures and records of pseudonymized/synthetic data output
- Re-identification risk assessment reports
- Approval and exception-handling logs for unmasking (viewing originals)
- Configuration values such as dynamic masking policies in the DBMS/security solution

## Nonconformity examples

- A production database is copied as-is and real data is used in the development/test environment.
- Masking is applied on screen, but plaintext is still exposed in API responses, downloaded files, and logs.
- With no masking criteria, application varies by field at the discretion of individual staff, resulting in inconsistency.
- Data is treated as fully anonymized even though re-identification is possible through combinations of quasi-identifiers.
- Unmasking (viewing originals) privileges are granted broadly and viewing history is not recorded.
- After pseudonymization, the mapping table (additional information) is stored on the same system as the original without separation.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
