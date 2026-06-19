# A.8.9 Configuration management

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.9 Configuration management |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.9.1 Change management |
| 2013 mapping | New in 2022 |

## Control objective

This control requires the organization to define and document the configurations (including security configurations) of hardware, software, services, and networks as standardized baselines, and to apply, monitor, and review them consistently. The objective is to detect and correct unauthorized configuration changes and the configuration drift that accumulates over time, so that systems continuously maintain their intended security posture. It helps reduce the attack surface created by insecure defaults, unnecessary functions, and inconsistent settings.

## Key checkpoints

1. Are secure configuration baselines/templates defined and documented per asset type (server OS, network devices, DBMS, middleware, cloud services, endpoints, and so on)?
2. Are the defined baselines built into deployment procedures so they are actually applied during new provisioning/reinstallation/provisioning?
3. Is the live configuration of running systems periodically checked against the baseline to detect drift and unauthorized changes?
4. Is configuration information (settings, versions, interdependencies, owners, and so on) kept current and linked to the change management process?
5. Is access to sensitive configuration information (credentials, keys, detailed settings) controlled, and is it stored/transmitted securely?
6. Are configuration baselines reviewed and updated periodically in line with changes in threats/vulnerabilities?

## Implementation guidance

- Establish configuration baselines/templates per asset type that reflect hardening requirements, and document the rationale (vendor guidance, industry benchmarks, internal policy).
- Standardize common hardening items such as changing default accounts/passwords, disabling unnecessary services/ports/functions, and enabling logging and time synchronization.
- Use golden images, infrastructure as code (IaC), and configuration management tools to apply baselines automatically, reducing manual errors and drift.
- Compare live configurations against baselines on a regular/continuous basis to detect drift, and either roll back unauthorized changes or formalize them through change management.
- Keep configuration items (CIs), versions, dependencies, and owners current in a CMDB/configuration repository, integrated with change and asset management.
- Avoid hardcoding credentials/keys in configuration files; protect them with secret management (vault), access control, and encryption.
- Periodically re-review and revise baselines to reflect the evolving threat landscape and new vulnerability information, and keep a revision history.

## Related controls and attributes

- ISO 27001 clauses: 7.5 (Documented information), 8.1 (Operational planning and control), 9.1 (Monitoring, measurement, analysis and evaluation)
- Adjacent Annex A: A.8.32 (Change management), A.8.19 (Installation of software on operational systems), A.8.8 (Management of technical vulnerabilities), A.5.9 (Inventory of information and other associated assets), A.8.16 (Monitoring activities)
- ISMS-P mapping: 2.9.1 Change management (from the secure-configuration/hardening angle, it also relates to 2.6.2 Information system access and 2.10.1 Security system operation)
- 2013 mapping: New in 2022 (a control newly introduced in ISO/IEC 27002:2022)

## Evidence

- Secure configuration baseline/hardening standard documents per asset type
- Configuration management tool/IaC code, golden images/templates, and deployment records
- Configuration drift check results and corrective action records
- CMDB/configuration repository records of configuration items/versions/dependencies
- Configuration change approvals and change-management linkage records
- Periodic review/revision history of configuration baselines

## Nonconformity examples

- No secure configuration baseline is defined, so settings differ from server to server and whether hardening was applied cannot be confirmed.
- Systems are found running with default administrator accounts/passwords still unchanged.
- With no procedure to check for configuration drift, unauthorized setting changes go unaddressed for a long time.
- The CMDB is not kept current, so the actual configuration does not match the documented configuration.
- Database passwords/API keys are hardcoded in plaintext in configuration files and exposed in the repository.
- A baseline is established only once at the start and is never updated to reflect changes in threats/vulnerabilities.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
