# A.8.29 Security testing in development and acceptance

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.29 Security testing in development and acceptance |
| Control type (ref.) | Preventive / Detective |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.8.2 Review and testing of security requirements |
| 2013 mapping | A.14.2.8, A.14.2.9 |

## Control objective

This control ensures that systems/applications being developed or acquired are tested to confirm they actually meet the defined security requirements before they are moved into the operational environment. Security testing should be planned and performed throughout the development life cycle, and at the acceptance stage (transfer to operations/purchased-product adoption) results should be verified and approved against pre-established acceptance criteria. This ensures vulnerabilities are found and removed before they reach production and that test results serve as the basis for release approval.

## Key checkpoints

1. Are the scope, methods, timing, and responsible parties for security testing planned and documented in advance for the target of development/acquisition?
2. Is testing designed against the security requirements defined in A.8.26, with traceability maintained between requirements and test cases?
3. Are security testing techniques appropriate to the system's risk level applied, such as static/dynamic analysis, vulnerability assessment, and penetration testing?
4. At the acceptance stage (transfer to operations/adoption of purchased products), are acceptance criteria defined in advance and are test results verified and approved against those criteria?
5. Are discovered vulnerabilities/defects remediated and re-tested according to severity, and is residual risk reflected in release approval?
6. Are the test environment and data controlled so that live production data is not used as-is, and are test records retained?

## Implementation guidance

- Establish a security testing plan aligned with the development life cycle (A.8.25), and vary the test scope and depth (code review, vulnerability assessment, penetration testing, etc.) according to the system's risk rating and exposure environment.
- Translate the security requirements from A.8.26 and the architecture/engineering principles from A.8.27 into concrete test cases, and maintain traceability by linking requirement IDs to test cases so nothing goes unverified.
- During development, integrate static analysis (SAST), software composition analysis (SCA/dependency vulnerability scanning), and secret scanning into the CI pipeline for early defect detection, and complement these with dynamic analysis (DAST)/fuzzing against the running environment.
- At the acceptance stage, define pass/fail criteria (acceptable residual risk, severity-based remediation thresholds) in advance, and approve transfer to operations only when the acceptance testing (secure configuration review, penetration test result review) is passed.
- For purchased/externally sourced products (including SaaS), review the security test/certification results provided by the supplier and, where necessary, perform independent vulnerability assessment to confirm the product meets adoption requirements (linked to A.8.30).
- Use pseudonymized/synthetic data rather than live production/personal data for testing (linked to A.8.31/A.8.33), and retain documentation of remediation of discovered vulnerabilities, re-test results, and approvals.

## Related controls and attributes

- ISO 27001 clauses: 8.1 (Operational planning and control), 9.1 (Monitoring, measurement, analysis and evaluation), 6.1 (Actions to address risks and opportunities)
- Adjacent Annex A: A.8.25 (Secure development life cycle), A.8.26 (Application security requirements), A.8.27 (Secure system architecture and engineering principles), A.8.28 (Secure coding), A.8.30 (Outsourced development), A.8.31 (Separation of development, test and production environments), A.8.33 (Test information), A.8.8 (Management of technical vulnerabilities)
- ISMS-P mapping: 2.8.2 Review and testing of security requirements (related: 2.8.1 Definition of security requirements, 2.8.3 Separation of test and production environments, 2.8.4 Test data security, 2.8.6 Migration to production, 2.11.2 Vulnerability assessment and remediation)
- 2013 mapping: A.14.2.8 (System security testing), A.14.2.9 (System acceptance testing)

## Evidence

- Security testing plan (scope/methods/timing/responsible parties) and a traceability matrix between requirements and test cases
- Static/dynamic analysis, vulnerability assessment, and penetration test reports, plus CI pipeline security scan logs
- Acceptance test pass criteria and acceptance/transfer-to-operations approval records
- Records of vulnerability remediation, re-test results, and residual-risk acceptance approvals
- Review of supplier security test/certification results and adoption approval documents for purchased/acquired products
- Test data controls (use of pseudonymized/synthetic data) and evidence of test record retention

## Nonconformity examples

- Only functional testing is performed without a security testing plan, and the system is transferred to operations.
- There are no test cases linked to security requirements, so requirements are released without being verified.
- High-risk defects found in vulnerability assessment/penetration testing are moved to production without remediation/re-testing.
- Acceptance (transfer-to-operations) pass criteria are not defined in advance, so approval decisions are made arbitrarily.
- Purchased/externally sourced products are adopted without reviewing their security test results.
- Live production/personal data is used for security testing without controls.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
