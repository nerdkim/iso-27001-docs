# A.8.2 Privileged access rights

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.2 Privileged access rights |
| Control type (ref.) | Preventive / Detective |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.5.5 Special accounts and privilege management |
| 2013 mapping | A.9.2.3 |

## Control objective

Privileged access rights (administrator, root, system/DB administrator privileges, and so on) can cause organization-wide damage if misused or stolen, so this control requires granting them to as few people as necessary and controlling their use strictly. It aims to manage the full lifecycle of privileged accounts (grant, use, review, revocation), keep them separate from ordinary work accounts, and thereby reduce the risk of misuse and compromise while preserving accountability for privileged activity.

## Key checkpoints

1. Are criteria and an approval process for granting privileged access rights defined, with grants based on least privilege and need-to-use?
2. Are privileged accounts separated from ordinary user accounts and individually identifiable, and is the use of shared/default administrator accounts controlled?
3. Is stronger authentication (such as multi-factor authentication) applied to privileged access, and are session/time limits or just-in-time grants considered?
4. Is privileged account activity logged/retained and reviewed periodically, and are holdings reviewed on a regular cycle so unnecessary rights are revoked?
5. Are privileged credentials (administrator passwords, SSH keys, and so on) stored/rotated securely, and are privileged rights granted to external/outsourced personnel managed separately?

## Implementation guidance

- Define a list of privileged right types/roles, process grants only with documented approval and an expiry (time limit), and minimize standing privileges.
- Use individually identifiable privileged accounts, minimize shared administrator account use, and where unavoidable ensure use is logged and attributable to a responsible person.
- Apply hardening measures to privileged access, such as multi-factor authentication, access via bastion/jump hosts, session recording, and privileged access management (PAM) solutions.
- Grant privileges only when needed through just-in-time elevation, and revoke them automatically once the task is complete.
- Store privileged credentials securely (for example in a vault) and rotate them periodically, and disable or rename/repassword default system administrator accounts.
- Adjust privileged rights immediately on transfer/termination/role change, and link with periodic access reviews (A.5.18) to check for excessive grants.
- Retain privileged activity logs separately and link them with logging/monitoring (A.8.15, A.8.16) to detect anomalous behavior.

## Related controls and attributes

- ISO 27001 clauses: 5.3 (Organizational roles, responsibilities and authorities), 6.1 (Actions to address risks), 8.1 (Operational planning and control)
- Adjacent Annex A: A.5.15 (Access control), A.5.16 (Identity management), A.5.17 (Authentication information), A.5.18 (Access rights), A.8.3 (Information access restriction), A.8.5 (Secure authentication), A.8.15 (Logging), A.8.16 (Monitoring activities), A.8.18 (Use of privileged utility programs)
- ISMS-P mapping: 2.5.5 Special accounts and privilege management
- 2013 mapping: A.9.2.3 (Management of privileged access rights)

## Evidence

- Privileged access request forms and approval/change history
- Privileged account inventory and holdings (account, scope of rights, reason for grant, expiry date)
- Authentication configuration for privileged access (multi-factor authentication) and PAM/bastion policy screens
- Privileged account activity logs and periodic review records
- Privileged credential storage/rotation history and evidence of default-account disablement
- Periodic access review results and records of revoking unnecessary rights

## Nonconformity examples

- Privileged rights are used without approval or a documented basis, or no expiry/revocation procedure exists.
- Multiple administrators share a common root/administrator account, so individual actions cannot be traced.
- Multi-factor authentication is not applied to privileged access, so a simple password alone grants access.
- Privileged account activity is not logged, or logs are collected but never reviewed.
- Privileged rights of leavers/role-changers are not revoked and remain active.
- Default system administrator accounts/passwords are left at their initial values and still in use.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
