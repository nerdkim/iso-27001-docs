# A.5.17 Authentication information

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.17 Authentication information |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity |
| ISMS-P mapping | 2.5.4 Password management (related: 2.5.3 User authentication) |
| 2013 mapping | A.9.2.4, A.9.3.1, A.9.4.3 |

## Control objective

Authentication information (passwords, PINs, token secrets, certificate private keys, API keys, and similar) is the core secret that proves the identity of a user or system, so it must be distributed, stored, and managed securely across its full lifecycle from issuance through use, renewal, and disposal. This control requires the organization to establish responsibilities and procedures for both the organization and the user so that authentication information cannot be leaked, guessed, or reused to enable unauthorized access. The essence is to assure both the quality of the authentication information (complexity/length/reuse limits) and its secure storage and transmission.

## Key checkpoints

1. Are there defined procedures for verifying identity and securely delivering authentication information when it is first issued to a new user or system?
2. Are initial/temporary passwords given a short validity period and set to be changed on first login?
3. Are quality rules appropriate to each credential type, such as password length, breached-password blocking, and reuse restrictions, plus replacement on compromise, defined and enforced?
4. Are verifier-held user passwords stored using a salted password hashing scheme with an appropriate work factor, recoverable service secrets protected separately with encryption and access control, and transmission paths protected?
5. Are users informed of restrictions on credential sharing and reuse across work/personal accounts, given safe storage options such as approved password managers, and asked to acknowledge these responsibilities?
6. Are there procedures to reset authentication information immediately when leakage/exposure is suspected, and to change default authentication information?

## Implementation guidance

- Document issuance/delivery/storage/disposal procedures by type of authentication information (user passwords, service account secrets, cryptographic keys, certificates) and assign owners.
- Give initial/temporary passwords a short validity, deliver them securely, and require replacement on first use. Apply activation, expiry, and revocation procedures suited to keys, certificates, and one-time codes.
- Protect password transmission and store verifier-held passwords with a purpose-built password hashing scheme, unique salts, and an appropriate work factor. A general-purpose hash alone or reversible encryption is unsuitable for password verification storage.
- Apply adequate length, blocking of breached/common passwords, attempt throttling, MFA, and password manager support. Do not treat arbitrary composition rules or periodic password changes as universal requirements; require changes on suspected compromise or under a separately applicable obligation.
- Remove hardcoded credentials from system/service accounts, manage them centrally in a secrets vault, and rotate them periodically.
- Train users on their responsibilities (no sharing of authentication information, phishing resistance, no reuse across personal/work accounts) and obtain acknowledgements.

## Related controls and attributes

- ISO 27001 clauses: 7.2 (Competence), 7.3 (Awareness), 8.1 (Operational planning and control)
- Adjacent Annex A: A.5.15 (Access control), A.5.16 (Identity management), A.5.18 (Access rights), A.8.2 (Privileged access rights), A.8.5 (Secure authentication)
- ISMS-P mapping: 2.5.4 Password management (related: 2.5.3 User authentication)
- 2013 mapping: A.9.2.4, A.9.3.1, A.9.4.3

## Evidence

- Authentication information management policy/procedure (covering issuance, delivery, storage, disposal)
- Password policy settings (length, breached-password blocking, attempt limits, MFA, and replacement triggers)
- Evidence of first-login replacement and expiry settings for initial/temporary passwords
- Records verifying the password hashing scheme, salts, work factor, and transport protection settings
- Operation records of the secrets vault and the secret rotation history
- User security acknowledgements and training records on handling authentication information

## Nonconformity examples

- New accounts are issued the same initial password for all users and a first-login change is not forced.
- User passwords are stored in the database in plaintext or simple encoding (base64).
- A database access password is hardcoded in application source/configuration files and committed to version control.
- User passwords can be viewed in plaintext from the administrator screen.
- Defined password length, breached-password blocking, or authentication attempt limits are not enforced in the systems.
- Authentication information is not reset even after an incident where its leakage was suspected.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
