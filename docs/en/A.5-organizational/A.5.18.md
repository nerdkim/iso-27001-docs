# A.5.18 Access rights

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.18 Access rights |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.5.6 Review of access rights (related: 2.5.1 User account management, 2.5.5 Special account and privilege management) |
| 2013 mapping | 9.2.2 User access provisioning, 9.2.5 Review of user access rights, 9.2.6 Removal or adjustment of access rights |

## Control objective
This control requires that access rights to information and other associated assets be provisioned, modified, and revoked based on business need and authorization, and that already-granted rights be reviewed periodically to confirm they remain valid over time. Where the access control policy (A.5.15) sets the rules, this control focuses on the operational activity of assigning actual rights to individual subjects and keeping them current across the whole lifecycle. When provisioning happens without approval, or when rights are not revoked and instead accumulate after a job change or departure, the least-privilege principle breaks down and the risk of privilege misuse and insider threat rises; preventing that is the objective.

## Key checkpoints
1. Are access rights provisioned/modified/revoked based on business need and the approval of the asset owner (or responsible party), and are these actions recorded?
2. Are rights granted only to the minimum scope matching the role/job, in line with the least-privilege and need-to-know principles?
3. Are privileged (administrator) rights and rights over sensitive assets treated separately from ordinary rights, with stricter approval, recording, and restriction applied?
4. When a subject's status changes (job change/transfer/retirement/contract termination), are the associated access rights adjusted or revoked without delay?
5. Does the asset owner periodically review the validity of granted access rights, and are unnecessary or excessive rights actually acted upon as a result?
6. Is the consistency between the rights recorded in policy and the rights actually configured in systems reconciled, and are discrepancies handled?

## Implementation guidance
- Standardize the request/approval/execution/recording procedure for access rights, and clearly designate the approver (asset owner/department head) and the recorded fields at each step.
- Define role-based access profiles (RBAC) in line with least-privilege and need-to-know principles, and assign rights only to the minimum scope needed to perform the job.
- Apply a separate, stronger approval process, use-justification records, and time limits (automatic expiry for temporary grants) to privileged accounts and access to sensitive assets.
- Build a workflow linked to HR/contract management so that onboarding/job-change/retirement/contract-termination events automatically drive the adjustment or revocation of access rights.
- Define the cycle/scope/reviewer (asset owner) for periodic access-right review (recertification), and keep records of review outcomes and actions taken (revoke/reduce/retain with justification).
- Periodically reconcile the rights recorded in policy against actual system configuration to detect and clean up unauthorized and residual rights.
- Log the key events for provisioning/modification/revocation of rights so that accountability and after-the-fact verification are possible.

## Related controls and attributes
- ISO 27001 clauses: 5.3 (Organizational roles, responsibilities and authorities), 6.1 (Actions to address risks and opportunities), 8.1 (Operational planning and control), 9.1 (Monitoring, measurement, analysis and evaluation)
- Adjacent Annex A: A.5.15 (Access control), A.5.16 (Identity management), A.5.17 (Authentication information), A.8.2 (Privileged access rights), A.8.3 (Information access restriction), A.8.4 (Access to source code), A.8.18 (Use of privileged utility programs), A.6.5 (Responsibilities after termination or change of employment)
- ISMS-P mapping: 2.5.6 Review of access rights (related: 2.5.1 User account management, 2.5.5 Special account and privilege management)
- 2013 mapping: 9.2.2 (User access provisioning), 9.2.5 (Review of user access rights), 9.2.6 (Removal or adjustment of access rights)

## Evidence
- Access-right management procedure (including provisioning/modification/revocation/review steps and approver definitions)
- Per-role access profiles and privilege matrix (RBAC definition document)
- Records of access-right provisioning/modification/revocation requests and approvals
- Approval forms for privileged-account/sensitive-asset rights, with use-justification and grant-period records
- Results of periodic access-right review (recertification) and records of actions taken (revoke/reduce)
- Reconciliation results between policy rights and actual system configuration, with discrepancy-handling records
- HR-linked processing records (rights adjustment and revocation on job change/retirement)

## Nonconformity examples
- Access rights are provisioned/modified at the operator's discretion without the asset owner's approval.
- On a job change, the rights of the previous role are not revoked and accumulate alongside the new rights, leaving excessive rights in place.
- The access rights of a leaver/contract-terminated party are not revoked, so access remains possible after the status change.
- Periodic access-right review is not performed, or the review is a formality (signature only) that leaves unnecessary rights untouched.
- Privileged (administrator) rights are over-granted to many users and managed without separate approval or records.
- Policy rights and actual system configuration are not reconciled, so unauthorized rights exist.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
