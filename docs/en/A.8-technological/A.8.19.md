# A.8.19 Installation of software on operational systems

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.19 Installation of software on operational systems |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.8.6 Transfer to operational environment |
| 2013 mapping | A.12.5.1, A.12.6.2 |

## Control objective

This control ensures that software installed on operational (production) systems is managed through a controlled procedure, so that unauthorized or unverified software cannot enter the operational environment and compromise system integrity and availability. It requires restricting installation/update privileges, transferring only software that has passed testing and approval, and retaining installation history and previous versions so that a fast recovery is possible if a problem occurs. It also covers keeping supplier software at a supported version and controlling arbitrary installation by users.

## Key checkpoints

1. Is the privilege to install/update software on operational systems restricted to designated personnel?
2. Does software transferred to the operational environment pass prior testing/verification and an approval procedure?
3. Are software installation/change records (version, date/time, performer, approver) logged and retained?
4. Are previous versions (executable code/configuration) retained and rollback procedures prepared so recovery is possible if a problem occurs?
5. Is supplier-provided software kept at a supported (patchable) version?
6. Is arbitrary software installation on general users' endpoints technically controlled?

## Implementation guidance

- Restrict install/update privileges on operational systems to the minimum number of people, avoid granting administrator rights permanently, and elevate them only when needed under approval.
- Validate software in a test environment, and once acceptance criteria are met, deploy it through change management (A.8.32) and the transfer-to-operational-environment procedure.
- Record and retain installation/update history (package name, version, deployment date/time, performer, basis of approval) in an auditable form.
- Back up the current version (executable code, libraries, configuration) before deployment, and prepare in advance a rollback plan that can restore the previous state if a fault or side effect occurs.
- Manage end-of-life (EOL) status of supplier software so it stays on a supported version, and remove unnecessary elements such as development code, debug tools, and compilers from the operational environment.
- Use application allowlisting, software deployment tooling, and endpoint controls to block unapproved software installation by users, and verify the integrity (signature/hash) of deployment packages.

## Related controls and attributes

- ISO 27001 clauses: 8.1 (Operational planning and control), 6.1 (Actions to address risks), 9.1 (Monitoring and measurement)
- Adjacent Annex A: A.8.32 (Change management), A.8.9 (Configuration management), A.8.8 (Management of technical vulnerabilities), A.8.31 (Separation of development, test and production environments), A.8.29 (Security testing in development and acceptance), A.8.4 (Access to source code)
- ISMS-P mapping: 2.8.6 Transfer to operational environment (related: 2.10.8 Patch management, 2.9.1 Change management)
- 2013 mapping: A.12.5.1 (Installation of software on operational systems), A.12.6.2 (Restrictions on software installation)

## Evidence

- Operational software installation/transfer procedures and assignment of installation privileges
- Software testing/acceptance and deployment approval records
- Software installation/update history (version/date/time/performer/approver)
- Previous-version backups and rollback procedures/execution records
- Supplier software supported-version register (including EOL status)
- Configuration records of software installation restrictions (allowlist/deployment tools) on endpoints/servers

## Nonconformity examples

- Installation privileges on operational systems are permanently granted to many people and are not controlled.
- Software is installed directly into the operational environment without testing/approval, causing an outage.
- Installation/change history is not recorded, so it is impossible to tell when, by whom, and what was deployed.
- There is no previous-version backup or rollback plan, so service recovery is delayed when a deployment fails.
- End-of-life supplier software continues to run in the operational environment without replacement or mitigation.
- Unapproved software installation on user endpoints is not controlled, allowing risky software to enter.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
