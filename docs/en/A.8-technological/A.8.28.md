# A.8.28 Secure coding

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.28 Secure coding |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality, Integrity, Availability |
| ISMS-P mapping | 2.8.1 Definition of security requirements |
| 2013 mapping | New in 2022 |

## Control objective

The organization is required to define secure coding principles and standards suited to the languages and frameworks it uses, and to apply them in day-to-day development so that code-level vulnerabilities are not introduced into software that is built or acquired. Coding-stage defects such as insufficient input validation, flawed authentication/authorization handling, use of unsafe libraries, and hardcoded credentials become an attack surface once deployed. Controlling code quality from a security perspective across design through maintenance reduces the likelihood of incidents, lowers the cost of remediation, and increases the trustworthiness of development deliverables.

## Key checkpoints

1. Are secure coding standards or guidelines established per programming language/framework in use, and shared with developers?
2. Is there a procedure to detect and remediate vulnerabilities during coding and build using automated tools such as static analysis (SAST)?
3. Are vulnerabilities, licenses, and currency of external libraries/open source components identified and managed?
4. Is secure coding training delivered to developers on a regular basis, with completion status tracked?
5. Do code review and merge/release approval procedures include security check items?
6. Are severity classification, remediation deadlines, and recurrence prevention for identified vulnerabilities tracked and managed?

## Implementation guidance

- Document secure coding standards reflecting language/framework characteristics, covering input validation, output encoding, authentication/session management, error handling, and safe logging principles.
- Integrate SAST/SCA/secret scanning into the development pipeline (CI/CD) to check automatically at commit/build time, and apply build-blocking or exception-approval policies based on severity.
- Maintain a software bill of materials (SBOM), and remediate components with known vulnerabilities (CVEs) by version upgrade or replacement.
- Prohibit hardcoding credentials/cryptographic keys in source code, and keep secrets separated in a dedicated secrets management solution.
- Operate a security-focused code review checklist, and ensure high-risk changes cannot be merged without peer review and approval.
- Deliver secure coding training and hands-on practice to developers regularly, continuously reflecting new threat and vulnerability types in the material.

## Related controls and attributes

- ISO 27001 clauses: Clause 8 (Operation), 7.2 (Competence)/7.3 (Awareness), 6.1 (Actions to address risks and opportunities)
- Adjacent Annex A: A.8.25 (Secure development life cycle), A.8.26 (Application security requirements), A.8.27 (Secure system architecture and engineering principles), A.8.29 (Security testing in development and acceptance), A.8.8 (Management of technical vulnerabilities)
- ISMS-P mapping: 2.8.1 Definition of security requirements (related: 2.8.2 Review and testing of security requirements, 2.8.5 Source program management)
- 2013 mapping: New in 2022

## Evidence

- Secure coding standard/guideline documents and their revision history
- SAST/SCA tool scan results and vulnerability remediation records
- Code review records and merge/release approval logs (PR approval history)
- Developer secure coding training plans and completion status
- SBOM and open source vulnerability management register
- Vulnerability remediation tracking tickets/issue records and exception approval justifications

## Nonconformity examples

- Secure coding standards exist but are not applied to actual development or the pipeline, remaining as formal documents only.
- High/medium severity vulnerabilities from SAST results are left unremediated for a long period with no exception approval justification.
- An outdated version of an open source library with known vulnerabilities (CVEs) is deployed to production as is.
- API keys and database passwords are hardcoded in source code and committed to the version control repository.
- A code review procedure is defined, but reviews are performed with a focus on functionality only, without security check items.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
