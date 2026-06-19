# A.8.8 Management of technical vulnerabilities

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.8 Management of technical vulnerabilities |
| Control type (ref.) | Preventive / Corrective |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.11.2 Vulnerability assessment and remediation |
| 2013 mapping | A.12.6.1, A.18.2.3 |

## Control objective

This control ensures that technical vulnerabilities in the information systems the organization uses are identified in a timely manner, assessed according to risk, and acted upon so that known weaknesses cannot be exploited. It requires a repeatable cycle that runs from maintaining an asset inventory, through collecting vulnerability information and evaluating exposure, to applying patches or mitigations, so that disclosed flaws are not left unaddressed. For vulnerabilities the organization cannot fix directly, interim mitigations and a documented risk acceptance decision should be applied together.

## Key checkpoints

1. Is the inventory of assets subject to vulnerability management (including hardware/software and version information) kept current?
2. Are channels and owners assigned to regularly collect vulnerability information (vendor advisories, security bulletins such as CVEs, threat intelligence)?
3. Are identified vulnerabilities assessed by severity/exposure/asset criticality, with remediation deadlines set per risk level?
4. Are periodic vulnerability assessments (scanning, penetration testing, and so on) performed, and is remediation of findings tracked and verified?
5. For vulnerabilities that cannot be patched immediately, are interim mitigations (access restriction, configuration changes, and so on) applied and residual risk accepted/recorded?
6. Are patches tested and passed through change management before deployment to review impact on operational stability?

## Implementation guidance

- Maintain an inventory of in-scope assets together with configuration details (OS/middleware/application/version/owner), and reflect newly introduced assets in the process so nothing is missed.
- Define vulnerability information sources (vendor notices, CVE/security advisories, CERT/threat intelligence) and make collection frequency and verification responsibility explicit.
- Prioritize by combining vulnerability severity (for example, CVSS), actual exposure, and asset criticality, and set remediation deadlines (SLAs) per risk tier.
- Validate patches in a test environment, deploy them through change management (A.8.32), and prepare a rollback plan alongside.
- When immediate remediation is not possible, apply mitigations such as tightened access control, service deactivation, or virtual patching, and register the residual risk in the risk management framework.
- Link periodic vulnerability assessment (scanning, penetration testing) with patch management (A.8.19), verify remediation through re-testing, and manage metrics such as open findings and deadline compliance rate.

## Related controls and attributes

- ISO 27001 clauses: 8.1 (Operational planning and control), 6.1 (Actions to address risks), 9.1 (Monitoring and measurement)
- Adjacent Annex A: A.8.19 (Installation of software on operational systems), A.8.9 (Configuration management), A.8.32 (Change management), A.5.7 (Threat intelligence), A.8.7 (Protection against malware), A.5.36 (Compliance with policies, rules and standards for information security)
- ISMS-P mapping: 2.11.2 Vulnerability assessment and remediation (related: 2.10.8 Patch management)
- 2013 mapping: A.12.6.1 (Management of technical vulnerabilities), A.18.2.3 (Technical compliance review)

## Evidence

- List of assets subject to vulnerability management and their configuration details
- Vulnerability information sources/frequency and collection records
- Vulnerability assessment (scanning/penetration test) reports and remediation plans
- Records of vulnerability remediation (patch/mitigation) and re-test results
- Mitigation and residual-risk acceptance approval records for vulnerabilities that cannot be fixed immediately

## Nonconformity examples

- The asset inventory is not kept current, so some systems are excluded from vulnerability management.
- No owner or channel collects vulnerability information, so vulnerabilities disclosed long ago go unnoticed.
- Priorities and deadlines are not set because severity is not assessed, leaving high-risk vulnerabilities unaddressed for a long time.
- Remediation of findings from assessments is not tracked or verified, so unremediated conditions recur.
- Vulnerabilities that cannot be patched immediately are left without any mitigation or residual-risk acceptance decision.
- A patch is deployed to production without testing or change management, causing an outage.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
