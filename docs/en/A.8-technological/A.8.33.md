# A.8.33 Test information

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.33 Test information |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity |
| ISMS-P mapping | 2.8.4 Test data security |
| 2013 mapping | A.14.3.1 (Protection of test data) |

## Control objective

This control selects and protects development/test information and manages its retention and deletion. Prefer synthetic or appropriately transformed data; where real production information is essential, verify a lawful basis, minimum scope, approval, and adequate safeguards. Masking or pseudonymization does not automatically guarantee anonymity, so assess re-identification and source-data disclosure risks. The aim is to protect information according to sensitivity while preserving reliable test results.

## Key checkpoints

1. Is there a policy/procedure for selecting, using, protecting, and disposing of test data, and is it shared with development/test teams?
2. Is the use of production data for testing restricted in principle, with approval by the responsible owner obtained where it is unavoidable?
3. When production data is used, is identifiability reduced as needed and re-identification risk assessed, with any exception to transformation managed through a lawful basis and separate approval/safeguards?
4. Are access and storage/transport safeguards appropriate to actual test-data sensitivity, with production-equivalent protection for sensitive production copies?
5. Are the copying/transfer of production data into test environments and its use there logged and traceable?
6. Is unneeded data securely deleted after testing, with a defined basis, deadline, and access restrictions for records that must be retained?

## Implementation guidance

- Document the criteria and responsibilities for selecting, generating, using, protecting, and disposing of test data as a policy/procedure, and train/share it with development and test staff.
- Prefer synthetic/fabricated data but check whether generation reproduces source personal information or rare records. The synthetic label alone does not justify public disclosure or unrestricted use.
- Verify the necessity and lawful basis for production data and obtain prior owner approval and privacy-function approval where needed. Where transformation is unsuitable, document a separate exception limiting scope, duration, users, and compensating controls.
- Reduce unnecessary identifiers through masking, pseudonymization, tokenization, or field removal and assess linkage with other data. Pseudonymized data can remain identifiable using additional information, so separate keys/mappings and maintain required privacy safeguards.
- Apply privileges, account management, necessary encryption, and logging according to test-data sensitivity and risk. Give sensitive production copies protection equivalent to production, without lowering safeguards for test convenience.
- Manage the copying/transfer of production data into test environments so that the approval, timing, target, handler, and method are recorded and traceable.
- After testing, delete unneeded production copies and residual data under A.8.10 and record outcomes. Where legal preservation or justified validation records are needed, define minimum scope, retention deadlines, and use restrictions, including backup expiry/recovery procedures.

## Related controls and attributes

- ISO 27001 clauses: 8.1 (Operational planning and control), 6.1 (Actions to address risks and opportunities)
- Adjacent Annex A: A.8.31 (Separation of development, test and production environments), A.8.29 (Security testing in development and acceptance), A.8.3 (Information access restriction), A.8.4 (Access to source code), A.8.10 (Information deletion), A.8.11 (Data masking), A.8.12 (Data leakage prevention), A.8.24 (Use of cryptography)
- ISMS-P mapping: 2.8.4 Test data security (related: 2.8.3 Separation of test and production environments, 3.2.5 Pseudonymized data processing, 2.9.7 Reuse and disposal of information assets, 3.4.1 Destruction of personal data)
- 2013 mapping: A.14.3.1 (Protection of test data)

## Evidence

- Test data management policy/procedure and test data selection/use criteria
- Approval requests/records for the use of production data in testing (owner/data protection officer approval)
- Masking/pseudonymization/transformation and re-identification-risk verification records, with minimized and restricted access to sensitive before/after samples
- Test environment access privilege lists and access/usage logs
- Records of copying/transferring production data into test environments (timing/target/handler)
- Confirmation of deletion/disposal of test data after testing and disposal history

## Nonconformity examples

- A production database is copied unchanged for testing without the required lawful basis, exception approval, and safeguards.
- Staff take out and use production data at their own discretion without any approval process for test data use.
- The access control/encryption level of the test environment is markedly lower than production, leaving personal data exposed to risk.
- Masked/pseudonymized data remains re-identifiable but is treated as anonymous and used without needed access restrictions.
- Unneeded production copies remain on test servers, developer PCs, or shared storage after testing without a valid retention basis or deletion plan.
- The use/copying of production data for testing is not logged, so there is no way to trace which data was used where.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
