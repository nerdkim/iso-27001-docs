# A.8.26 Application security requirements

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.26 Application security requirements |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.8.1 Definition of security requirements |
| 2013 mapping | A.14.1.2, A.14.1.3 |

## Control objective

This control ensures that, when applications are developed or acquired/purchased, information security requirements are identified, specified, and approved by taking into account the sensitivity of the information processed, the exposure environment, the access/authentication characteristics, and the nature of transactions, and that these requirements are reflected throughout development and acquisition. Defining security requirements early in planning/design rather than after the fact prevents vulnerabilities from being built into the design and implementation stages and reduces rework cost. Applications exposed over public networks (the internet) and electronic transactions in particular need additional requirements such as transaction integrity, non-repudiation, and prevention of incomplete/erroneous/replayed transmissions.

## Key checkpoints

1. Is there a procedure to identify, document, and approve security requirements for application development/acquisition according to the sensitivity of the information processed and the exposure environment (internal/public network)?
2. Are requirements for authentication/authorization/session management/access control specifically reflected in the requirements specification?
3. Are requirements for addressing application vulnerabilities (input validation, output encoding, safe error handling, protection against injection/tampering) defined?
4. For transactions/transmissions over public networks, are requirements defined for transport encryption, transaction integrity, non-repudiation, and prevention of incomplete/duplicated/replayed/misrouted messages?
5. Are legal/contractual requirements (for personal data, payment data, etc.) and logging/audit-trail requirements reflected?
6. Are the defined security requirements verified/tested during the design/implementation/testing stages and approved before release?

## Implementation guidance

- Establish a security requirements catalog/checklist keyed to application type (web/mobile/API/electronic transaction, etc.), data classification, and exposure environment, and select requirements based on the risk assessment at project initiation.
- Specify requirements for authentication (including multi-factor), authorization and least privilege, session management, and access control, and define control requirements for interactions between users/systems of differing trust levels.
- Define defenses against known vulnerabilities such as input validation, output encoding/escaping, safe error handling, injection/XSS/CSRF/insecure deserialization, linked to the secure coding standard (A.8.28).
- For public-network/electronic-transaction applications, define requirements for transport encryption (TLS), transaction integrity and non-repudiation (digital signatures/timestamps), prevention of incomplete/duplicated/replayed/misrouted messages, and payment/settlement validation.
- Where personal data and payment data are processed, reflect applicable laws/standards (data protection law, PCI DSS, etc.) together with data retention/disposal and logging/audit-trail requirements.
- Maintain traceability (requirement IDs) for the defined security requirements so they can be verified in design/implementation/testing (A.8.29), and for acquired (purchased/SaaS) products, assess and approve whether the supplier's security features meet the requirements.

## Related controls and attributes

- ISO 27001 clauses: 6.1 (Actions to address risks and opportunities), 8.1 (Operational planning and control)
- Adjacent Annex A: A.8.25 (Secure development life cycle), A.8.27 (Secure system architecture and engineering principles), A.8.28 (Secure coding), A.8.29 (Security testing in development and acceptance), A.8.30 (Outsourced development), A.5.8 (Information security in project management), A.8.24 (Use of cryptography)
- ISMS-P mapping: 2.8.1 Definition of security requirements (related: 2.8.2 Review and testing of security requirements, 2.6.3 Application access, 2.10.4 Electronic transaction and fintech security)
- 2013 mapping: A.14.1.2 (Securing application services on public networks), A.14.1.3 (Protecting application services transactions)

## Evidence

- Application security requirements specification/checklist and approval records
- Risk assessment and data classification results underpinning the requirements
- Authentication/authorization/access control/session management design documents
- Specification and applied records for public-network/electronic-transaction requirements (transport encryption, transaction integrity, non-repudiation, etc.)
- Test/verification results for security requirements (design reviews, security test reports)
- Supplier security requirement conformance assessment and approval documents for acquired applications

## Nonconformity examples

- Applications are developed/acquired using only functional requirements, without separately defining security requirements.
- Transactions over public networks have no defined requirements for transport encryption/transaction integrity/non-repudiation.
- Vulnerability-handling requirements such as input validation/injection prevention are absent, so the same class of vulnerability recurs.
- Legal requirements for processing personal data/payment data are not reflected in the security requirements.
- Defined security requirements are released without being confirmed during the testing/verification stage.
- The security features of an acquired (purchased/SaaS) application are adopted without being assessed for conformance to requirements.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
