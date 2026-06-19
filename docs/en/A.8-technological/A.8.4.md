# A.8.4 Access to source code

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.4 Access to source code |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity |
| ISMS-P mapping | 2.8.5 Source program management |
| 2013 mapping | A.9.4.5 |

## Control objective

This control restricts read and write access to source code, development tools, and software libraries according to business need. It aims to prevent insertion of unauthorized functionality, malicious changes, and accidental modification, and to preserve the confidentiality of source code as intellectual property. It requires controlling who can access source code and to what extent across development, build, and deployment, while keeping change history traceable.

## Key checkpoints

1. Is access to the source code repository (configuration/version control system) granted on a least-privilege, business-need basis, with read and write permissions managed separately?
2. Is repository access authenticated with individually identifiable accounts, and are access/commit/merge/permission-change events logged so they can be audited?
3. Is unnecessary source code kept off operational systems, and is access to development tools, libraries, and build pipeline credentials also controlled?
4. Are source code changes applied through a review process (code review, merge approval), with unapproved direct changes blocked?
5. When external developers or suppliers access source code, is the scope and duration limited and governed by contract/confidentiality undertakings?
6. Are access rights reviewed periodically and revoked immediately on termination or role change?

## Implementation guidance

- Manage source code centrally in an authorized configuration/version control system, and separate read/write permissions by role at the repository/branch level.
- Apply individually identifiable accounts and strong authentication (for example, SSO/multi-factor) to repository access, and log all access/commit/merge/permission-change events to ensure traceability.
- Deploy only the artifacts needed to run in operational/deployment environments and do not leave original source code there; minimize access to build tools, libraries, and pipeline credentials such as tokens/keys.
- Control changes with code review and merge approval and with protected-branch policies (such as no force-push), blocking unapproved direct changes.
- Apply secret scanning and pre-commit checks to prevent hardcoded credentials/keys from entering the source code.
- Limit external personnel to only the repositories they need, revoke access immediately when the access period ends or the contract expires, and review the permission list periodically.

## Related controls and attributes

- ISO 27001 clauses: 8.1 (Operational planning and control), 6.1 (Actions to address risks)
- Adjacent Annex A: A.8.3 (Information access restriction), A.8.2 (Privileged access rights), A.8.31 (Separation of development, test and production environments), A.8.32 (Change management), A.8.25 (Secure development life cycle), A.8.28 (Secure coding), A.5.18 (Access rights)
- ISMS-P mapping: 2.8.5 Source program management
- 2013 mapping: A.9.4.5 (Access control to program source code)

## Evidence

- Access permission list and role/permission configuration screens of the configuration management system
- Repository access/commit/merge/permission-change logs
- Code review and merge approval records, protected-branch policy settings
- Periodic review records and revocation history of source code access rights
- Access-control contracts/confidentiality undertakings for external developers and evidence of scoped access assignment
- Results of secret scanning / pre-commit checks

## Nonconformity examples

- Least privilege is not applied, for example all developers hold admin/write access to the source code repository.
- A shared account is used to access the repository, so the author of a change cannot be traced.
- Original source code is left on operational servers, creating a risk of unauthorized viewing/modification.
- Direct changes to a protected branch (such as force-push) are possible without code review/merge approval.
- Repository access rights of leavers or role-changed staff are not revoked and remain active.
- Credentials/keys are committed hardcoded in the source code but are not checked for.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
