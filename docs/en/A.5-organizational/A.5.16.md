# A.5.16 Identity management

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.16 Identity management |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality, Integrity, Availability |
| ISMS-P mapping | 2.5.2 User identification |
| 2013 mapping | 9.2.1 User registration and de-registration |

## Control objective
This control governs the full life cycle of identities assigned to internal personnel, external parties, and non-human entities such as systems, services, and devices. Each subject must be uniquely identifiable so that actions can be traced back to an accountable owner and so that granted access rights map precisely to the real user of an identity. Weak identity management leads to orphaned accounts, privilege misuse, and an inability to attribute incidents, which this control aims to prevent across creation, change, deactivation, and deletion.

## Key checkpoints
1. Are identities assigned to personnel and non-human entities (service accounts, system accounts, devices) uniquely identifiable and linked to a real subject?
2. Are procedures for creating, granting, changing, deactivating, and deleting identities documented, with approvals and request rationale recorded?
3. Are shared identities limited to unavoidable business cases, subject to explicit approval, an assigned responsible owner, and usage logging?
4. When status changes occur (leavers, transfers, contract termination), are the related identities deactivated or revoked in a timely manner?
5. Are active identities periodically reconciled against actual employment/contract status and the access rights they hold?
6. Are significant identity events (creation, privilege change, deactivation) recorded and traceable?

## Implementation guidance
- Establish a one-identity-per-subject principle, assign a unique identifier per individual, and maintain the mapping to the real user to preserve accountability.
- Define roles, responsibilities, and approvers for each life-cycle stage (request, approval, issuance, change, suspension, removal) and standardize them as a workflow.
- Manage non-human identities (service accounts, system accounts, API keys, device certificates) in the same inventory, each with a designated owner.
- Prohibit shared identities by default; where unavoidable, document the rationale, approval, scope, and owner, and apply compensating controls to attribute individual actions.
- Integrate with the HR or contract-management system so that joiner, leaver, and role-change events are automatically reflected in identity status.
- Set criteria to detect unused or dormant identities (for example, no login within a defined period) and deactivate or delete them on a regular cycle.
- Periodically reconcile the active identity inventory against actual status and record the resolution of any discrepancies.

## Related controls and attributes
- ISO 27001 clauses: 7.2 (Competence), 8.1 (Operational planning and control), 9.1 (Monitoring, measurement, analysis and evaluation)
- Adjacent Annex A: A.5.17 (Authentication information), A.5.18 (Access rights), A.5.15 (Access control), A.8.2 (Privileged access rights), A.8.5 (Secure authentication)
- ISMS-P mapping: 2.5.2 User identification (adjacent: 2.5.1 User account management, 2.5.5 Special account and privilege management)
- 2013 mapping: 9.2.1 User registration and de-registration

## Evidence
- Identity/account management policy and procedures (including life-cycle stages and defined approvers)
- Identity inventory (a consolidated list of personnel accounts and non-human identities such as services, systems, and devices)
- Records of identity creation, change, deactivation, and deletion requests and approvals
- Approval forms and usage history for shared identities, plus owner-designation documents
- HR integration processing records (joiner/leaver/role change) and evidence of leaver account revocation
- Results of periodic reconciliation of active identities and records of cleaned-up unused accounts

## Nonconformity examples
- Identities of leavers or terminated contractors are left active for long periods without deactivation.
- Multiple people share a single common identity without approval or logging, making individual actions untraceable.
- Service accounts and system accounts have no designated owner, creating management blind spots.
- No approval or request rationale is recorded when identities are created or changed.
- No reconciliation is performed between the active identity list and actual employment status, leaving numerous orphaned accounts.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
