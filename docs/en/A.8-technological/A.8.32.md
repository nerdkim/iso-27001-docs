# A.8.32 Change management

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.32 Change management |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.9.1 Change management |
| 2013 mapping | A.12.1.2, A.14.2.2, A.14.2.3, A.14.2.4 |

## Control objective

This control ensures that changes to information processing facilities and information systems (infrastructure, applications, configuration, procedures) are planned, reviewed, approved, tested, and deployed through a controlled procedure, so that unverified changes cannot compromise security or service stability. It requires assessing the impact and risk of a change in advance, obtaining approval from authorized parties, and applying the change in a state where the previous condition can be restored if it fails. The aim is to reduce outages, introduction of vulnerabilities, and unauthorized functional changes caused by change, while keeping change history traceable.

## Key checkpoints

1. Is a change management procedure documented for information system/infrastructure/application changes, with its scope (routine/emergency/standard changes) defined?
2. When a change is requested, are its purpose, scope of impact, security impact, risk, and rollback plan reviewed in advance and approved by an authorized party?
3. Is a change validated in a test environment and confirmed to meet acceptance criteria before it is applied to production?
4. Is there a separate procedure for emergency changes, including post-implementation review/approval and recording, that is actually operated?
5. Is change history (request/approval/test/deployment/result) recorded and retained in a traceable form, and are related documents (configuration/operating procedures) updated together?
6. Is a rollback prepared in advance and confirmed afterward so the previous state can be restored if a change fails or has unexpected effects?

## Implementation guidance

- Establish a change management procedure that defines the stages (request, impact/risk assessment, approval, testing, deployment, closure) and responsible parties for each change type (standard/routine/emergency).
- Standardize the change request so it includes the change purpose, target assets, security/privacy impact, interdependencies, expected downtime, rollback plan, and verification method.
- Have a change advisory body (such as a change advisory board) or an authorized approver review/approve changes commensurate with risk level, and separate the requester from the approver to prevent self-approval.
- Validate changes in a test environment separated from production (A.8.31), and once acceptance criteria are met, apply them through the transfer-to-operational-environment/deployment procedure (A.8.19).
- Back up current configuration/executable code/data before deployment, and prepare and test in advance a rollback procedure that can restore the previous state within a defined time if the change fails.
- Process emergency changes quickly but complete formal review/approval/recording afterward, and update all change history, configuration/operating documents, and security controls (firewall rules, access rights, and so on) in line with the change.

## Related controls and attributes

- ISO 27001 clauses: 8.1 (Operational planning and control), 6.3 (Planning of changes), 10 (Improvement)
- Adjacent Annex A: A.8.31 (Separation of development, test and production environments), A.8.19 (Installation of software on operational systems), A.8.9 (Configuration management), A.8.8 (Management of technical vulnerabilities), A.8.29 (Security testing in development and acceptance), A.8.25 (Secure development life cycle)
- ISMS-P mapping: 2.9.1 Change management (related: 2.8.6 Transfer to operational environment, 2.8.2 Review and testing of security requirements, 2.10.8 Patch management)
- 2013 mapping: A.12.1.2 (Change management), A.14.2.2 (System change control procedures), A.14.2.3 (Technical review of applications after operating platform changes), A.14.2.4 (Restrictions on changes to software packages)

## Evidence

- Change management procedure and documentation defining change types (standard/routine/emergency)
- Change request/approval records (including impact/risk assessment and rollback plan)
- Change test/acceptance results and production deployment records
- Emergency change handling and post-implementation review/approval records
- Pre-change backup and rollback execution/verification records
- Change advisory board minutes or approval history, and records of configuration/operating document updates arising from the change

## Nonconformity examples

- No change management procedure exists, or it does not apply to certain systems (for example network devices or cloud configuration), so changes are applied without control.
- A change is applied directly to production without impact/risk assessment or approval, causing an outage or introducing a vulnerability.
- A change is applied to production without validation in a test environment, or the requester approves their own change.
- After handling an emergency change, no post-implementation review/approval/record is kept, so the change cannot be verified.
- There is no pre-change backup or rollback plan, so service recovery is delayed when a change fails.
- After a change, configuration documents, access rights, or security policies are not updated, so the actual configuration and the documentation are inconsistent.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
