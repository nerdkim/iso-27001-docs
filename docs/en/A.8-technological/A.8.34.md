# A.8.34 Protection of information systems during audit testing

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.34 Protection of information systems during audit testing |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 1.4.2 Management system review |
| 2013 mapping | A.12.7.1 |

## Control objective

This control ensures that assessment activities on operational information systems, such as audits, vulnerability assessments, penetration tests, and technical compliance reviews, are planned in advance and carried out within an agreed scope so they do not cause service disruption, data corruption, or exposure of sensitive information. It requires agreeing the target, timing, method, and access rights with the owner of the system under test, limiting access to read-only where possible, and recording and managing audit accounts/tools and access activity during the test. The aim is to minimize the risk that the assessment activity itself undermines operational stability and information protection.

## Key checkpoints

1. Are audit/vulnerability assessment/penetration test activities on operational systems planned in advance, with scope/timing/method/access rights agreed with the system owner?
2. During testing, is access to operational systems and data limited to the minimum needed for the purpose, and are read-only access or isolated copies used where possible?
3. Are the privileges granted to temporary test accounts and testing tools limited to the purpose, and are accounts/temporary access rights/tools revoked and removed after the test?
4. Is access and activity during testing logged and monitored so it can be verified afterward?
5. Are tests that may affect performance/availability/integrity (load generation, scanning, change-inducing actions) performed under controlled conditions (such as off-peak windows) after impact assessment and approval?
6. Are data/results/evidence obtained from testing stored securely under access control and disposed of once the retention period has passed?

## Implementation guidance

- Agree and document in advance the request, scope, schedule, access rights, responsible parties, and emergency contact arrangements for assessment activities on operational systems (internal/external audits, vulnerability assessments, penetration tests, compliance checks).
- Make least privilege and read-only access the default for testing, and require tests needing write/change access to run on isolated copies or a test environment (A.8.31) separated from production.
- Assign a validity period and usage scope to temporary test accounts and tools, and revoke/delete them immediately after the test so no account or tool remains on operational systems.
- Log and monitor access and executed commands during testing (A.8.15, A.8.16), and establish a procedure to immediately halt/roll back on anomalies or incidents.
- Perform tests that may affect performance/availability (load tests, large-scale scans, vulnerability exploitation) after impact assessment and approval, during off-peak hours or an agreed testing window.
- Store operational data, test results, and evidence obtained from testing in an access-controlled repository, and dispose of them securely once the retention period has passed.

## Related controls and attributes

- ISO 27001 clauses: 9.2 (Internal audit), 9.1 (Monitoring, measurement, analysis and evaluation), 8.1 (Operational planning and control)
- Adjacent Annex A: A.8.8 (Management of technical vulnerabilities), A.5.35 (Independent review of information security), A.8.15 (Logging), A.8.16 (Monitoring activities), A.8.31 (Separation of development, test and production environments), A.8.9 (Configuration management), A.5.18 (Access rights)
- ISMS-P mapping: 1.4.2 Management system review (related: 2.11.2 Vulnerability assessment and remediation, 2.9.4 Log and access record management, 2.5.5 Special account and privilege management, 2.8.3 Separation of test and production environments)
- 2013 mapping: A.12.7.1 (Information systems audit controls)

## Evidence

- Audit/test plans and records of scope/schedule/access-rights agreement with the system owner
- Temporary test account issuance/privilege grant and post-test revocation/deletion records
- Access/activity logs and monitoring records during testing
- Impact assessment and approval records for load-inducing/change-inducing tests
- List of testing tools and confirmation of tool removal after testing
- Test result reports and records of obtained-data storage/disposal

## Nonconformity examples

- Vulnerability assessment or penetration testing on operational systems is carried out without prior agreement/approval, causing a service outage.
- Temporary accounts issued or testing tools installed for a test remain on operational systems because they were not revoked/removed after the test.
- Excessive write/change privileges on operational data are granted during testing, resulting in data corruption.
- Access and activity during testing are not logged, so what was tested cannot be verified afterward.
- A load-inducing test is run during business hours without impact assessment, causing performance degradation or a service outage.
- Operational data/results obtained from testing are stored without access control or not disposed of, leaving a risk of leakage.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
