# A.8.24 Use of cryptography

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.24 Use of cryptography |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.7.1 Application of cryptographic policy |
| 2013 mapping | A.10.1.1, A.10.1.2 |

## Control objective

This control requires the organization to define through policy, and operate consistently, when, where, and at what strength cryptography is applied in order to protect the confidentiality, integrity, and authenticity of information. Cryptography is not completed by algorithm selection alone: the full key lifecycle from generation to destruction, together with legal/regulatory constraints (nationally approved algorithms, import/export rules, contractual requirements), must be considered for the protection to be effective in practice. The objective is to exclude unvalidated in-house algorithms and weak configurations, maintain cryptographic strength proportionate to the level of risk, and be prepared to replace algorithms as they age over time.

## Key checkpoints

1. Is an organization-wide policy on the use of cryptography established, specifying the scope of application (data at rest, data in transit, authentication data, etc.) and the approved algorithms/minimum key lengths?
2. Do the algorithms and key lengths in use meet current recommended levels, and are weak or to-be-retired algorithms (legacy hashes/block ciphers) identified with a replacement plan in place?
3. Are management procedures and responsibilities defined for the entire key lifecycle: generation/distribution/storage/use/rotation/destruction/recovery?
4. Is important information such as personal data and authentication data encrypted at rest and in transit, and are approvals and justifications recorded when exceptions apply?
5. Are legal/regulatory cryptography requirements (nationally approved algorithms, import/export rules, contractual requirements) identified and complied with?
6. Is access to cryptographic modules/key stores (HSM, KMS, etc.) controlled, and are related activities logged and reviewed?

## Implementation guidance

- Document the scope, list of approved algorithms, minimum key lengths, operating modes, and exception approval procedure in the cryptography policy, and prioritize the targets of application by linking to risk assessment results.
- Apply encryption at rest (disk/database/file) and encryption in transit (secure protocols/versions such as TLS) distinctly, and disable weak protocols (legacy TLS) and weak cipher suites.
- Generate keys from a secure random source and store them in an HSM or a dedicated key management system (KMS); never store plaintext keys in source code, configuration files, or logs.
- Define key rotation periods, immediate destruction/re-issuance on suspected compromise, and backup/escrow procedures against loss, and apply dual control and separation of duties to key handling.
- Use only validated standard algorithms and trustworthy libraries, prohibit in-house cryptographic development, and continuously manage the versions of libraries in use and their known vulnerabilities.
- Build crypto-agility into the design to prepare for the aging of algorithms/key strength, and periodically re-review and update the policy and its state of implementation.

## Related controls and attributes

- ISO 27001 clauses: 6.1.3 (Information security risk treatment), 8.1 (Operational planning and control), 7.5 (Documented information)
- Adjacent Annex A: A.5.31 (Legal, statutory, regulatory and contractual requirements), A.8.5 (Secure authentication), A.5.14 (Information transfer), A.8.20 (Networks security), A.8.26 (Application security requirements)
- ISMS-P mapping: 2.7.1 Application of cryptographic policy (related: 2.7.2 Cryptographic key management, 2.10.5 Information transfer security, 2.5.4 Password management)
- 2013 mapping: A.10.1.1 (Policy on the use of cryptographic controls), A.10.1.2 (Key management)

## Evidence

- Cryptography policy/guideline documents and the approved algorithm/minimum key length reference table
- A status table of encryption at rest/in transit (algorithm/key length/protocol version per target system)
- Key management procedures and the key lifecycle register (generation/rotation/destruction history)
- HSM/KMS access privilege lists and access/operation logs
- TLS configuration review results (evidence of disabling weak versions/cipher suites) and vulnerability assessment reports
- Records of the review of compliance with cryptography-related laws/regulations

## Nonconformity examples

- A cryptography policy exists but lacks the scope of application and minimum key length criteria, so cryptography is applied inconsistently across systems.
- Personal data is stored in plaintext in the database or stored using weak hashes (plain MD5/SHA-1).
- Legacy TLS (1.0/1.1) and weak cipher suites remain enabled on production servers.
- Cryptographic keys are hardcoded in plaintext within application source code, configuration files, or repositories.
- No key rotation period is defined, so the same key has been used for years, and there is no destruction/re-issuance procedure on compromise.
- An unvalidated in-house cryptographic algorithm is used, or the requirement for nationally approved algorithms is not met.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
