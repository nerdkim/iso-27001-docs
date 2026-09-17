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
3. Are repeated failures controlled through delays, attempt limits, or suitable lockout, with limited information in error messages? Is CAPTCHA used only as a supplement to these controls?
4. Are storage protection and secure transport appropriate to credential type, including password-verification hashing and encryption/access control for recoverable secrets?
5. Are secure log-on procedures (input masking, session timeout, access warning banner) configured, and are authentication events logged and monitored?

## Implementation guidance

- Select authentication factors based on asset classification and risk assessment results, applying multi-factor authentication for high-risk access.
- Mask password entry by default; a user-controlled temporary reveal option may be offered with shoulder-surfing risk in view. Protect transport with TLS or an equivalent secure channel and prohibit plaintext transmission.
- Store verifier-held passwords using a purpose-built password hashing scheme with unique salts and an appropriate work factor. A general-purpose hash alone is insufficient; apply separate encryption/access controls to recoverable service secrets and private keys.
- Apply lockout/delay/alerts for repeated login failures, and do not indicate in error messages whether the ID or the password was wrong.
- Terminate idle sessions automatically, require re-authentication for sensitive operations, and consider adaptive authentication based on context such as location, device, and behavior.
- Consider phishing- and replay-resistant authentication for high-risk access. For FIDO2 or certificate-based methods, verify binding to the verifier/service identity in the actual configuration; the presence of a certificate alone does not establish phishing resistance (linked to A.5.17).

## Related controls and attributes

- ISO 27001 clauses: 6.1 (Actions to address risks and opportunities), 8.1 (Operational planning and control)
- Adjacent Annex A: A.5.15 (Access control), A.5.16 (Identity management), A.5.17 (Authentication information), A.5.18 (Access rights), A.8.2 (Privileged access rights), A.8.3 (Information access restriction)
- ISMS-P mapping: 2.5.3 User authentication
- 2013 mapping: A.9.4.2 (Secure log-on procedures)

## Evidence

- Authentication policy/standard defining authentication methods per classification/risk
- MFA configuration screens for privileged/remote/critical access
- Account lockout/login attempt limit configuration screens
- Evidence of password hashing scheme/salts/work factor, recoverable-secret protection, and transport encryption settings
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
