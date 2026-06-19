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

1. Are retention periods and deletion timing defined per information type, with a procedure to identify and delete data that has passed its retention period?
2. Are deletion methods (secure deletion, overwriting, cryptographic erasure, physical destruction) defined to suit the media/system characteristics (magnetic disk, SSD, cloud storage, backups, logs, and so on)?
3. After deletion is requested/executed, is it verified and recorded that the data has actually been rendered unrecoverable?
4. In outsourced/cloud environments, is deletion of the processor's data upon contract termination or purpose fulfillment reflected in contracts/procedures, and is that performance confirmed?
5. Does the deletion scope cover all copies of the same information, including backups, snapshots, archives, and derived copies?

## Implementation guidance

- Define retention periods and deletion criteria per information type in policy, and operate a procedure that periodically identifies and deletes data past its retention period.
- Standardize deletion methods to suit media and system characteristics: overwriting/secure deletion based on a recognized standard for reusable media, cryptographic erasure or vendor secure-erase for SSD/flash, and physical destruction for media being discarded.
- Where cryptographic erasure (crypto-shredding) is used, link it to key management so the target data is stored only in strongly encrypted form and the key is securely destroyed.
- Confirm complete deletion after execution through recovery attempts/sample verification or deletion logs/certificates, and retain the results.
- State in cloud/outsourcing contracts the obligation to return or delete data upon termination and to submit proof of deletion, and check that it is met.
- Map in advance every location where the same information may exist, such as backups, snapshots, replicas, logs, and temporary files, to prevent deletion gaps.

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
- Only a simple file delete is performed on SSD/cloud storage, without making the data unrecoverable (overwriting/cryptographic erasure).
- Operational data is deleted, but the same information remains in backups/snapshots/logs and is omitted from the deletion scope.
- After a cloud/outsourcing contract ends, deletion of the processor's data is neither confirmed nor supported by any proof.
- Deletion is claimed but cannot be confirmed as complete because there is no verifying evidence such as deletion logs or certificates.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
