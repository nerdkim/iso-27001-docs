# A.5.33 Protection of records

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.33 Protection of records |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality/Integrity/Availability |
| ISMS-P mapping | 2.9.4 Log and access record management |
| 2013 mapping | 18.1.3 |

## Control objective
This control requires the organization to protect the records it must retain under legislative, regulatory, contractual, and business requirements (accounting and transaction records, contracts, personnel records, audit logs, personal data processing records, and similar) from loss, destruction, falsification, unauthorized access, and unauthorized release. Because records serve as the basis for legal evidence, accountability, regulatory response, and business continuity, their authenticity, completeness, legibility, and availability must be maintained throughout the retention period. The aim is to define the retention period and protection level for each record type and to preserve the reliability and accessibility of records against media degradation, obsolescence of playback technology, and unauthorized change until retention ends and the records are securely disposed of.

## Key checkpoints
1. Are the types of records to be retained under legislative/regulatory/contractual/business requirements, and each retention period, identified and documented?
2. Are storage, access control, encryption, and integrity-assurance measures in place to protect records from loss/destruction/falsification/unauthorized access/unauthorized release?
3. Are media/format migration and legibility-preservation measures in place for long-term records to counter media degradation and obsolescence of playback technology?
4. Are records whose retention period has expired disposed of securely according to a defined procedure, with the results managed?
5. Are the retention periods and access rights of records containing personal or confidential information managed on a minimization basis?
6. Can the authenticity and reliability of records required for audit and evidentiary purposes be demonstrated after the fact?

## Implementation guidance
- Establish a records retention schedule that defines, for each record type, the legal/regulatory/contractual basis, retention period, storage location, owner, and disposal point.
- Apply access control, encryption, backup, change-history management, and logging to record stores to prevent unauthorized access/change/deletion and ensure integrity (for electronic records, use anti-tampering measures such as hashing, digital signatures, and WORM storage).
- For long-term records, prepare a plan for periodic media migration, format standardization, and legibility checks to counter media degradation and obsolescence of playback software/hardware.
- Apply purpose-based minimum retention periods to records containing personal or sensitive information, and dispose of them in an unrecoverable manner once retention ends, keeping a disposal record.
- Apply the same protection level and retention period to backups and archives as to the originals, and maintain controls across media check-in/out, storage, and destruction (linked to A.7.10, A.8.10).
- Assign management responsibility across the whole record lifecycle (creation/storage/transfer/disposal), and maintain indexing and classification so records can be retrieved/produced promptly on audit and regulatory requests.

## Related controls and attributes
- ISO 27001 clauses: 7.5 (Documented information), 9.2 (Internal audit records), 9.3 (Management review records), 5.3/8.1 (Organizational roles/responsibilities and operational control)
- Adjacent Annex A: A.5.34 (Privacy and protection of PII), A.5.37 (Documented operating procedures), A.7.10 (Storage media), A.8.10 (Information deletion), A.8.13 (Information backup), A.8.15 (Logging)
- ISMS-P mapping: 2.9.4 Log and access record management (related: 1.4.1 Review of compliance with legal requirements, 3.4.2 Measures when retaining after purpose achieved, 2.9.7 Reuse and disposal of information assets)
- 2013 mapping: 18.1.3 Protection of records

## Evidence
- Records retention schedule and records management policy (retention period, legal basis, and disposal point per type)
- Access rights list and access logs for record stores, and encryption/WORM/integrity-verification configuration records
- Media/format migration plan and legibility check records for long-term records
- Disposal plan and disposal confirmations/disposal register for records with expired retention
- Protection settings and retention-period application records for backups and archives
- Record retrieval and production history in response to audit/regulatory requests

## Nonconformity examples
- Retention periods per record type are undefined, so legally required records are deleted at will or kept far longer than necessary.
- Legally retained records such as accounting/transaction records are left in shared folders without access control or integrity assurance, exposing them to tampering.
- No provision is made against media degradation and format obsolescence of long-term records, so records cannot be read within their retention period.
- Records containing personal data whose retention period has expired are not disposed of and remain in storage.
- Audit logs are stored without change-prevention measures, so whether they were tampered with cannot be demonstrated afterward.
- No indexing/retrieval scheme exists to respond to a regulator's request to produce records, so they cannot be produced within the required period.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
