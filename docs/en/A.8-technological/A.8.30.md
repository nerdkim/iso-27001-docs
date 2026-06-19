# A.8.30 Outsourced development

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.30 Outsourced development |
| Control type (ref.) | Preventive, Detective |
| Security properties (ref.) | Confidentiality, Integrity, Availability |
| ISMS-P mapping | 2.8.1 Security requirements definition |
| 2013 mapping | 14.2.7 (Outsourced development) |

## Control objective

This control ensures that when all or part of system development is outsourced to external personnel or suppliers, the organization's security requirements are applied throughout the development process and their fulfillment is continuously directed, monitored, and verified. Because outsourcing shifts control over source code, data, and infrastructure to an external party and moves security activities outside the organization's direct oversight, the control requires clear requirements from the contract stage and verification steps up to acceptance, in order to reduce the risk of vulnerabilities being introduced, malicious functionality being inserted, and intellectual property or data being leaked. The goal is to achieve the same level of security in outsourced deliverables as in in-house development.

## Key checkpoints

1. Do outsourced development contracts/requests for proposal (RFP) specify security requirements (secure coding, testing, deliverables, intellectual property, data handling, right to audit, and so on)?
2. Is the supplier's secure development capability and security management maturity assessed before contracting and reflected in the selection criteria?
3. Are there procedures and deliverable submission requirements that let the organization check/oversee fulfillment of its security requirements during development?
4. Is security verification (security testing, vulnerability assessment, source code review, malware/backdoor checks) performed before accepting deliverables, and are the results reflected in acceptance approval?
5. Are controls defined for the source code, data, access privileges, and development environment provided or created for the project, along with return/destruction procedures at contract termination?
6. Are source code ownership/escrow, licensing, restrictions on sub-contracting (secondary outsourcing), and maintenance/warranty responsibility stipulated in the contract?

## Implementation guidance

- Include in the outsourced development contract and RFP the security requirements, the secure development standards/secure coding rules to comply with, the deliverable list, acceptance criteria, right to audit, and sanctions for violations in specific terms.
- Assess secure development capability, personnel security, past track record, and sub-contract management ability when selecting a supplier, and stipulate that sub-contracting requires prior approval and inherits equivalent security obligations.
- Minimize production data provided for development, replacing it with pseudonymized/anonymized or test data, and grant least-privilege access to source code/development environment/documentation with access logging.
- Direct and oversee requirement fulfillment through phase-based security checks (design review, interim deliverable review, sharing of security test results) and regular reporting.
- At acceptance, perform source code review, static/dynamic analysis (SAST/DAST), software composition analysis (SCA/open source vulnerabilities), and checks for malware/backdoors/hardcoded credentials, and manage completion of defect remediation as a condition of acceptance approval.
- Stipulate intellectual property ownership, source code escrow, license compliance, maintenance and warranty responsibility, and notification/joint-response duties in the event of a security incident in the contract.
- At contract termination/expiry, confirm the return or destruction of provided assets, source code, access privileges, and development/test data, and retain evidence.

## Related controls and attributes

- ISO 27001 clauses: 8.1 (Operational planning and control), 6.1 (Actions to address risks and opportunities), 7.4 (Communication), 9.1 (Monitoring, measurement, analysis and evaluation)
- Adjacent Annex A: A.8.25 (Secure development life cycle), A.8.26 (Application security requirements), A.8.28 (Secure coding), A.8.29 (Security testing in development and acceptance), A.8.31 (Separation of development, test and production environments), A.8.4 (Access to source code), A.5.19 (Information security in supplier relationships), A.5.20 (Addressing information security within supplier agreements), A.5.21 (Managing information security in the ICT supply chain)
- ISMS-P mapping: 2.8.1 Security requirements definition (related: 2.3.2 Security in external party contracts, 2.3.3 Management of external party security compliance, 2.3.4 Security on external party contract change and expiry, 2.8.2 Security requirements review and testing, 2.8.5 Source program management)
- 2013 mapping: 14.2.7 (Outsourced development)

## Evidence

- Outsourced development contracts/RFP and security requirement specifications (including secure coding, acceptance criteria, right to audit, sub-contracting clauses)
- Supplier security capability assessment and selection review records
- Phase-based security check/oversight records and progress reports
- Acceptance-stage security testing/vulnerability assessment/source code review/malware check reports and defect remediation records
- Acceptance approval records and deliverable lists
- Source code escrow agreements and license/intellectual property documents
- Confirmation of return or destruction of assets/data/access privileges at contract termination

## Nonconformity examples

- The outsourced development contract lacks security requirements and acceptance criteria, so deliverables are accepted with a lower level of security than in-house development.
- No security testing/vulnerability assessment is performed before acceptance, so vulnerabilities or hardcoded credentials are carried into production.
- Production data is provided to the supplier for development without pseudonymization/anonymization, exposing personal and confidential information.
- The contract has no restriction on sub-contracting, so a secondary supplier the organization was unaware of processes the source code.
- Source code/development environment access privileges granted to the supplier are not revoked and remain after the contract ends.
- Source code ownership/escrow and maintenance responsibility are not stipulated in the contract, making maintenance impossible when the supplier withdraws.
- There is no right to audit/inspection over the development process, so requirement fulfillment cannot be verified.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
