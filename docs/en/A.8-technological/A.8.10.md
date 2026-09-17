# A.8.10 Information deletion

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.10 Information deletion |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality |
| ISMS-P mapping | 2.9.7 Reuse and disposal of information assets |
| 2013 mapping | New in 2022 |

## Control objective

This control requires that information no longer needed be reliably erased from information systems, devices, and storage media to prevent unnecessary exposure. Retaining data beyond its required period widens the impact of any breach and can violate legal/contractual retention limits, so the objective is to protect confidentiality by defining what to delete and how, and by verifying that deletion has actually taken place.

## Key checkpoints

1. Are retention/deletion timing and legal preservation exceptions defined by information type, with a procedure to identify and delete information once its retention basis ends?
2. Are individual-record deletion and whole-media sanitization distinguished, with methods appropriate to system/media/cloud capabilities and responsibilities?
3. Are deletion execution and method suitability verified, with verifiable scope, residual copies, and validation limits recorded?
4. In outsourced/cloud environments, is deletion of the data held or processed by the processor upon contract termination or purpose fulfillment reflected in contracts/procedures, and is fulfillment of that obligation verified?
5. Does the deletion scope cover all copies of the same information, including backups, snapshots, archives, and derived copies?

## Implementation guidance

- Define retention bases and deletion triggers by information type and process expired information periodically. For exceptions such as legal holds, record scope, basis, owner, and review timing, and restrict unrelated use.
- Delete individual data through application/service functions and copy-management procedures; sanitize whole media for reuse/disposal under A.7.14. Do not universally apply ordinary overwrites to SSDs or assume customers can overwrite shared cloud hardware. Verify provider capabilities and contractual responsibilities.
- Use cryptographic erase after verifying encryption coverage throughout the target data's history and removal of relevant key copies. Identify recovery/escrow/backup keys and separate plaintext or differently encrypted copies; deleting one key does not establish erasure of every copy.
- Verify execution through deletion logs, service state, provider evidence, and feasible sample checks. Verifiability differs across media and services; record and track limitations and outstanding items instead of treating a log or certificate as proof of absolute irrecoverability.
- State in cloud/outsourcing contracts the obligation to return or delete data upon termination and to submit proof of deletion, and check that it is met.
- Map backups, snapshots, replicas, logs, and temporary files. Where immediate selective deletion is impractical, set retention/expiry deadlines and use restrictions consistent with applicable obligations, with an assigned owner. Reapply deletions during recovery to prevent reintroduction into use, and verify expiry processing.

## Related controls and attributes

- ISO 27001 clauses: 7.5 (Documented information), 8.1 (Operational planning and control)
- Adjacent Annex A: A.8.11 (Data masking), A.8.12 (Data leakage prevention), A.7.10 (Storage media), A.7.14 (Secure disposal or re-use of equipment), A.5.34 (Privacy and protection of PII)
- ISMS-P mapping: 2.9.7 Reuse and disposal of information assets (for personal data, also 3.4.1 Destruction of personal data)
- 2013 mapping: New in 2022 (no corresponding control in the 2013 edition)

## Evidence

- Information retention/deletion policy and procedure, and a retention-period table by information type
- Records of identifying and deleting data past its retention period (deletion logs, deletion register)
- Secure-deletion/destruction confirmation or destruction certificates for storage media
- Key-destruction records and key management register where cryptographic erasure is used
- Deletion clauses in cloud/outsourcing contracts and proof of deletion upon contract termination
- Deletion-completeness verification results (recovery-attempt outcomes, sample check records)

## Nonconformity examples

- Data past its retention period is left in operational systems for a long time with no deletion criteria in place.
- Deletion is marked complete after a simple file delete without checking SSD/cloud deletion capabilities or residual copies against the required outcome.
- Backups/snapshots/logs remaining after active-data deletion lack a retention basis, use restrictions, expiry, or re-deletion controls during recovery.
- After a cloud/outsourcing contract ends, deletion of the data held by the processor is neither confirmed nor supported by any proof.
- Deletion is reported complete without evidence sufficient to verify the processing outcome, scope, and limitations.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
