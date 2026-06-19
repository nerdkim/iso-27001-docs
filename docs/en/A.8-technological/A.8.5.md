# A.8.5 Secure authentication

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.5 Secure authentication |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity |
| ISMS-P mapping | 2.5.3 User authentication |
| 2013 mapping | A.9.4.2 |

## Control objective

This control requires authentication technologies and procedures to be applied in proportion to the sensitivity and risk of the information and systems being accessed, so that the claimed identity of a user/entity is verified before access is granted. By setting authentication strength to match asset classification and risk, it reduces the risk of unauthorized access through credential theft, guessing, or reuse.

## Key checkpoints

1. Are authentication methods (knowledge/possession/biometric based) applied differentially according to the sensitivity and risk of the information/system being accessed?
2. Is multi-factor authentication (MFA) applied to high-risk access such as privileged accounts, remote access, and access to critical systems?
3. Are login attempts limited (account lockout/delay/CAPTCHA), and are failure messages designed not to reveal which credential was wrong?
4. Are credentials such as passwords/tokens protected during transmission and storage (encryption in transit, hashing/salting at rest)?
5. Are secure log-on procedures (input masking, session timeout, access warning banner) configured, and are authentication events logged and monitored?

## Implementation guidance

- Select authentication factors based on asset classification and risk assessment results, applying multi-factor authentication for high-risk access.
- Do not display passwords on screen during entry; encrypt the transmission path with TLS and prohibit cleartext transmission.
- Store credentials using strong salted hashing; prohibit storage in cleartext or with weak algorithms (such as MD5/SHA-1).
- Apply lockout/delay/alerts for repeated login failures, and do not indicate in error messages whether the ID or the password was wrong.
- Terminate idle sessions automatically, require re-authentication for sensitive operations, and consider adaptive authentication based on context such as location, device, and behavior.
- Adopt authentication methods resistant to phishing/replay attacks (such as FIDO2, certificate-based), and link with authentication information management (A.5.17).

## Related controls and attributes

- ISO 27001 clauses: 6.1 (Actions to address risks), 8.1 (Operational planning and control)
- Adjacent Annex A: A.5.15 (Access control), A.5.16 (Identity management), A.5.17 (Authentication information), A.5.18 (Access rights), A.8.2 (Privileged access rights), A.8.3 (Information access restriction)
- ISMS-P mapping: 2.5.3 User authentication
- 2013 mapping: A.9.4.2 (Secure log-on procedures)

## Evidence

- Authentication policy/standard defining authentication methods per classification/risk
- MFA configuration screens for privileged/remote/critical access
- Account lockout/login attempt limit configuration screens
- Evidence of credential storage method (hash/salt) and transmission encryption settings
- Access warning banner and session timeout configuration screens
- Authentication success/failure logs and abnormal authentication monitoring/alert records

## Nonconformity examples

- The administrator console/privileged accounts are accessible with a single password and no multi-factor authentication is applied.
- Login error messages specifically reveal whether the ID or the password was wrong.
- There is no account lockout/attempt limit, so unlimited login attempts (brute force) are possible.
- Credentials are transmitted in cleartext (HTTP) or stored in cleartext or with weak hashes.
- Multiple users share a single privileged account, so individual authentication is not performed.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
