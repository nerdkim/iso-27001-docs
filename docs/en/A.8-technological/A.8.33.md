# A.8.33 Test information

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.33 Test information |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality, Integrity |
| ISMS-P mapping | 2.8.4 Test data security |
| 2013 mapping | 14.3.1 (Protection of test data) |

## Control objective

This control requires the organization to carefully select, protect, and manage the information used for testing and development, so that operational data (especially personal or sensitive data) is not copied indiscriminately into lower-assurance test environments where it could be exposed, and so that its integrity is not damaged during testing. Test information should be used only to the extent needed for the test purpose, and where operational data must be used, its identifiability should be removed through masking/pseudonymization before applying access controls equivalent to those in production. This minimizes the leakage and misuse risk that arises from using real data for the sake of testing convenience, while also preserving the reliability of test results.

## Key checkpoints

1. Is there a policy/procedure for selecting, using, protecting, and disposing of test data, and is it shared with development/test teams?
2. Is the use of operational data for testing restricted in principle, with approval by the responsible owner obtained where it is unavoidable?
3. When operational data is used for testing, is the identifiability of personal and sensitive data removed through masking/pseudonymization/transformation?
4. Are access controls and storage/transmission protection equivalent to the production environment applied to test data?
5. Is the copying/transfer of operational data into test environments logged and traceable?
6. After testing completes, is test data (especially copies of operational data) promptly and securely deleted/disposed of according to the defined procedure?

## Implementation guidance

- Document the criteria and responsibilities for selecting, generating, using, protecting, and disposing of test data as a policy/procedure, and train/share it with development and test staff.
- Prioritize the use of synthetic or fabricated test data over real operational data, so that personal/sensitive data is fundamentally prevented from entering test environments.
- Where operational data must be used, obtain prior approval from the responsible owner (and the data protection officer where relevant), and clearly limit the scope and duration of use.
- Before using operational data for testing, remove the identifiability of personal and unique identifying information through masking/pseudonymization/tokenization/partial deletion.
- Apply access controls, account management, encryption (at rest and in transit), and logging to test data at a level equivalent to production, and raise the overall security level of the test environment accordingly.
- Manage the copying/transfer of operational data into test environments so that the approval, timing, target, handler, and method are recorded and traceable.
- When testing ends, promptly remove copies of operational data and residual test data in a secure manner (unrecoverable deletion/disposal) and record the result.

## Related controls and attributes

- ISO 27001 clauses: 8.1 (Operational planning and control), 6.1 (Actions to address risks and opportunities)
- Adjacent Annex A: A.8.31 (Separation of development, test and production environments), A.8.29 (Security testing in development and acceptance), A.8.3 (Information access restriction), A.8.4 (Access to source code), A.8.10 (Information deletion), A.8.11 (Data masking), A.8.12 (Data leakage prevention), A.8.24 (Use of cryptography)
- ISMS-P mapping: 2.8.4 Test data security (related: 2.8.3 Separation of test and production environments, 3.2.5 Pseudonymized data processing, 2.9.7 Reuse and disposal of information assets, 3.4.1 Destruction of personal data)
- 2013 mapping: 14.3.1 (Protection of test data)

## Evidence

- Test data management policy/procedure and test data selection/use criteria
- Approval requests/records for the use of operational data in testing (owner/data protection officer approval)
- Masking/pseudonymization/transformation processing records and before/after samples or verification records
- Test environment access privilege lists and access/usage logs
- Records of copying/transferring operational data into test environments (timing/target/handler)
- Confirmation of deletion/disposal of test data after testing and disposal history

## Nonconformity examples

- An operational database is copied into the test environment without masking/pseudonymization and used for development/testing.
- Staff take out and use operational data at their own discretion without any approval process for test data use.
- The access control/encryption level of the test environment is markedly lower than production, leaving personal data exposed to risk.
- Masking is applied but is insufficient (only some fields processed, reversible), so individuals can still be identified.
- After testing ends, copies of operational data remain on test servers, developer PCs, or shared storage.
- The use/copying of operational data for testing is not logged, so it cannot be traced which data was used where.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
