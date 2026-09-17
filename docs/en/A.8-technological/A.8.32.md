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

This document covers planning, review, authorization, validation, and deployment of changes to systems, infrastructure, applications, and procedures. Assess security and service impact, implement under authorized approval, and prepare validated rollback or alternative recovery if a change fails. Procedures suited to change type and risk, with traceable records, reduce unauthorized changes, outages, and introduced vulnerabilities.

## Key checkpoints

1. Is a change management procedure documented for information system/infrastructure/application changes, with the systems it covers and the change types (standard/routine/emergency) defined?
2. Are purpose, impact scope, security impact, risk, and rollback/alternative recovery reviewed in advance with authorized approval?
3. Is validation appropriate to risk and change type performed before production deployment, with limited testing for emergency changes managed through authorized procedures and retrospective review?
4. Is there a separate procedure for emergency changes, including post-implementation review/approval and recording, that is actually operated?
5. Is change history (request/approval/test/deployment/result) recorded and retained in a traceable form, and are related documents (configuration/operating procedures) updated together?
6. Is rollback or alternative recovery prepared with data/schema compatibility in view, and are service and data state verified after a failure?

## Implementation guidance

- Establish a change management procedure that defines the stages (request, impact/risk assessment, approval, testing, deployment, closure) and responsible parties for each change type (standard/routine/emergency).
- Record purpose, assets, security/privacy impact, dependencies, expected downtime, validation, and rollback or alternative recovery in change requests. For irreversible changes, state limitations and potential data loss during recovery.
- Have a change review body such as a change advisory board (CAB) or an authorized approver review/approve changes commensurate with risk level, and separate the requester from the approver to prevent self-approval.
- Validate changes in a test environment separated from production (A.8.31), and once acceptance criteria are met, apply them through the production promotion/deployment procedure (A.8.19).
- Preserve necessary code/configuration/data and validate recovery procedures. Check whether reverting remains safe after data/schema changes; where it does not, prepare compatible transitions, restoration, or forward fixes, with criteria for stopping deployment.
- Process emergency changes through predefined authority and contacts, obtaining expedited authorization where feasible and recording the basis and minimum validation. Complete formal retrospective review and required approvals afterward, and update configuration/operating documents and security controls.

## Related controls and attributes

- ISO 27001 clauses: 8.1 (Operational planning and control), 6.3 (Planning of changes), 10 (Improvement)
- Adjacent Annex A: A.8.31 (Separation of development, test and production environments), A.8.19 (Installation of software on operational systems), A.8.9 (Configuration management), A.8.8 (Management of technical vulnerabilities), A.8.29 (Security testing in development and acceptance), A.8.25 (Secure development life cycle)
- ISMS-P mapping: 2.9.1 Change management (related: 2.8.6 Transfer to operational environment, 2.8.2 Review and testing of security requirements, 2.10.8 Patch management)
- 2013 mapping: A.12.1.2 (Change management), A.14.2.2 (System change control procedures), A.14.2.3 (Technical review of applications after operating platform changes), A.14.2.4 (Restrictions on changes to software packages)

## Evidence

- Change management procedure and documentation defining change types (standard/routine/emergency)
- Change request/approval records including impact/risk assessment and rollback or alternative recovery plans
- Change test/acceptance results and production deployment records
- Emergency change handling and post-implementation review/approval records
- Necessary pre-change backups and rollback/alternative recovery validation records
- Change advisory board minutes or approval history, and records of configuration/operating document updates arising from the change

## Nonconformity examples

- No change management procedure exists, or it does not apply to certain systems (for example network devices or cloud configuration), so changes are applied without control.
- A change is applied directly to production without impact/risk assessment or approval, causing an outage or introducing a vulnerability.
- Validation/authorization required for the change type is omitted, or a requester approves their own change without independent oversight or approved compensating controls.
- After handling an emergency change, no post-implementation review/approval/record is kept, so the change cannot be verified.
- Backups and validated rollback/alternative recovery needed for a failed change are absent, delaying service restoration.
- After a change, configuration documents, access rights, or security policies are not updated, so the actual configuration and the documentation are inconsistent.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
