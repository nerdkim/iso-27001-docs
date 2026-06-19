# A.8.25 Secure development life cycle

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.25 Secure development life cycle |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality, Integrity, Availability |
| ISMS-P mapping | 2.8.1 Security requirements definition |
| 2013 mapping | 14.2.1 (Secure development policy) |

## Control objective

This control requires the organization to build security activities into every stage of planning, designing, implementing, testing, deploying, and maintaining software and systems, so that vulnerabilities are prevented from entering deliverables and the cost of remediating them after the fact is reduced. By defining security requirements from the earliest stage and applying consistent rules and verification steps at each phase, the organization achieves security by design and security by default. The approach should apply consistently across the whole organization regardless of the development methodology (waterfall/agile/DevOps) and whether development is in-house or outsourced.

## Key checkpoints

1. Is a secure development life cycle (SDLC) policy/standard documented and applied consistently to both in-house and outsourced development?
2. Are the security activities and pass criteria (security gates) to be performed at each stage (requirements/design/implementation/test/deployment/transition to production) defined?
3. Are secure coding standards and training provided to developers, and is compliance checked?
4. Is a secure development/configuration management environment (version control, access control, build/deployment pipeline) established and controlled?
5. Are security requirements and verification (license, vulnerabilities, SBOM, and so on) defined for open source/third-party/outsourced components?
6. Are the results of pre-deployment security review/testing (threat modeling, secure code review, vulnerability assessment) reflected in deployment approval?

## Implementation guidance

- Define the security activities, roles and responsibilities, deliverables, and pass criteria across all SDLC stages as a standard, and align them with the development methodology the organization uses (including agile/DevOps).
- Derive security and privacy requirements during the planning/requirements stage, and perform threat modeling and security architecture review during the design stage.
- Establish secure coding standards (input validation, authentication/authorization, session/encryption, error handling, safe logging, and so on) and run developer training and compliance checks in parallel.
- Automate static analysis (SAST), dynamic analysis (DAST), software composition analysis (SCA/open source vulnerabilities), and secret scanning by integrating them into the CI/CD pipeline.
- Separate development/test/production environments, and secure configuration/version control, source code access control, and the integrity of build/deployment artifacts (signing, artifact verification).
- Treat pre-deployment security testing (secure code review, vulnerability assessment, penetration testing) as a pass criterion, and manage completion of remediation for identified defects as a condition of deployment approval.
- For outsourced development, include security requirements and acceptance criteria in the contract, and verify the security of deliverables at the point of acceptance.

## Related controls and attributes

- ISO 27001 clauses: 6.1 (Actions to address risks and opportunities), 8.1 (Operational planning and control), 7.2 (Competence)
- Adjacent Annex A: A.8.26 (Application security requirements), A.8.27 (Secure system architecture and engineering principles), A.8.28 (Secure coding), A.8.29 (Security testing in development and acceptance), A.8.30 (Outsourced development), A.8.31 (Separation of development, test and production environments), A.8.4 (Access to source code), A.8.32 (Change management), A.8.33 (Test information)
- ISMS-P mapping: 2.8.1 Security requirements definition (related: 2.8.2 Security requirements review and testing, 2.8.3 Separation of test and production environments, 2.8.5 Source program management, 2.9.1 Change management)
- 2013 mapping: 14.2.1 (Secure development policy)

## Evidence

- Secure development life cycle (SDLC) policy/standard and procedures
- Per-stage security activity checklists and security gate pass records
- Secure coding standard documents and developer security training records
- Threat modeling/security architecture review deliverables
- SAST/DAST/SCA scan results and remediation records
- Pre-deployment security testing (code review, vulnerability assessment, penetration testing) reports and deployment approval records
- Outsourced development contracts (including security requirements) and acceptance verification results

## Nonconformity examples

- An SDLC policy exists, but in actual projects security checks are performed only just before deployment after development is complete.
- Secure coding standards do not exist, or exist but are not shared/taught to developers and so are not actually followed.
- Security testing is not integrated into the CI/CD pipeline, so vulnerable code is deployed automatically without verification.
- Open source/third-party components are adopted without verifying their known vulnerabilities and licenses.
- Deployment is approved even though defects found in vulnerability assessment have not been remediated.
- The outsourced development contract has no security requirements, and no security verification is performed at acceptance.
- Development/test/production environments and source code access privileges are not separated/controlled.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
