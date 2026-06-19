# A.8.31 Separation of development, test and production environments

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.31 Separation of development, test and production environments |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality, Integrity, Availability |
| ISMS-P mapping | 2.8.3 Separation of test and production environments |
| 2013 mapping | 12.1.4 (Separation of development, testing and operational facilities) |

## Control objective

This control requires the organization to separate development, test, and production environments physically or logically, so that unverified code or configuration changes cannot reach production services outside a controlled process and production data cannot leak into lower environments with weaker protection. By making the boundaries between environments and the promotion procedures explicit, the organization protects the integrity and availability of production systems and minimizes the impact that mistakes or unauthorized changes during development/test can have on production. The same separation principle should be maintained consistently not only on premises but also in cloud/container/CI-CD and other automated deployment environments.

## Key checkpoints

1. Are development/test/production environments separated physically or logically (network/system/account)?
2. Are procedures for promoting software and changes between environments (approval, linkage with change management, integrity verification, rollback) defined and enforced?
3. Is the use of production data in development/test environments controlled, with masking/pseudonymization and separate approval where unavoidable?
4. Are access privileges separated per environment, and is developers' direct access to production minimized/controlled?
5. Are unnecessary development elements (compilers, development tools, source code) removed from production so that it is kept to a minimal configuration?
6. Is environment separation, including separation of accounts and secrets, applied in cloud/container/IaC/CI-CD automated deployment environments as well?

## Implementation guidance

- Separate development/test/production environments physically, or logically through distinct network segments/VPCs/subscriptions/projects/namespaces and accounts.
- Link promotion from lower environments to production with change management for approval and recording, and provide integrity verification of deployment artifacts (signing, artifact verification) and rollback procedures.
- Block developers' direct access to production by default, and where needed grant least-privilege/time-bound access controlled and logged through privileged access management (PAM).
- As a rule do not use production data for testing; where unavoidable, use it in a limited way after masking/pseudonymization and owner approval.
- Apply login banners/screen colors/host naming conventions so that environments are clearly identifiable, preventing mis-operation between production and test.
- Remove unnecessary elements such as compilers, debugging tools, development accounts, and source code from production to minimize the attack surface.
- In cloud/IaC/CI-CD pipelines, separate accounts, networks, secrets/credentials, and pipeline permissions per environment to prevent cross-environment access.

## Related controls and attributes

- ISO 27001 clauses: 8.1 (Operational planning and control), 6.1 (Actions to address risks and opportunities)
- Adjacent Annex A: A.8.32 (Change management), A.8.33 (Test information), A.8.25 (Secure development life cycle), A.8.4 (Access to source code), A.8.9 (Configuration management), A.8.2 (Privileged access rights), A.8.3 (Information access restriction)
- ISMS-P mapping: 2.8.3 Separation of test and production environments (related: 2.8.4 Test data security, 2.8.6 Transition to production, 2.9.1 Change management, 2.5.5 Special account and privilege management)
- 2013 mapping: 12.1.4 (Separation of development, testing and operational facilities)

## Evidence

- Development/test/production environment separation policy/procedures and network diagrams
- Per-environment access privilege lists and access privilege review records
- Cross-environment promotion/deployment approval records (linked to change management) and rollback procedure documents
- Test data masking/pseudonymization records and usage approval records
- Cloud/IaC environment separation configuration evidence (account/VPC/namespace/secret separation)
- Production minimal-configuration review results (confirmation that compilers/development tools/source code are removed)

## Nonconformity examples

- Development/test/production run on the same server or same network segment without separation.
- Developers hold standing access privileges to production databases/servers.
- Production data is copied into test environments and used without masking/pseudonymization.
- Developers apply source code or configuration directly to production (hotfix) without change management approval.
- Compilers/debugging tools/source code remain in production, expanding the attack surface.
- In the cloud, development and production share the same account/VPC or use common secrets/credentials.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
