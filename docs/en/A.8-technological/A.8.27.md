# A.8.27 Secure system architecture and engineering principles

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.27 Secure system architecture and engineering principles |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality/Integrity/Availability |
| ISMS-P mapping | 2.8.1 Security requirements definition |
| 2013 mapping | 14.2.5 (Secure system engineering principles) |

## Control objective

This control requires the organization to define secure engineering principles and to apply them consistently throughout the design and construction of information systems. Rather than bolting on security ad hoc in each project, it calls for standardizing and reusing principles at the architecture level, such as security by design, defense in depth, least privilege, secure by default, fail-secure, and minimizing the attack surface. By designing trust boundaries and controls consistently across layers, the organization prevents vulnerabilities from being introduced structurally and keeps the security level stable even when new technologies are adopted.

## Key checkpoints

1. Are secure system architecture and engineering principles (security by design, defense in depth, least privilege, secure defaults, and so on) documented, approved, and shared with relevant staff?
2. Are the defined principles actually applied to new system designs and to significant changes/re-builds of existing systems, and is compliance checked during design review?
3. Is there a security architecture (reference architecture/design patterns) that specifies trust boundaries, data flows, authentication/authorization points, and control layers?
4. Are the principles made concrete for the technology stack the organization uses, such as cloud, containers, APIs, microservices, and zero trust?
5. When exceptions to the principles arise, are they risk-assessed, approved, documented, and managed with compensating controls?
6. Are the architecture principles reviewed/updated periodically in line with the threat landscape and technology changes?

## Implementation guidance

- Define and approve the organization's secure engineering principles, such as security by design, defense in depth (multiple defensive layers), least privilege and segregation of duties, secure defaults, fail-secure, minimizing the attack surface, and never trust (zero trust), then share them.
- Make the principles concrete as reusable reference architectures, secure design patterns, and standard components (authentication/authorization modules, cryptographic libraries, logging components) so projects can adopt them easily.
- When designing a system, diagram trust boundaries and data flows, and place authentication/authorization/input validation/encryption/logging controls at each boundary to design layered defense.
- Design accounts and privileges around least privilege and segregation of duties by default, and apply least privilege to administrative/service accounts and system-to-system integrations as well.
- Establish security baselines that make the principles concrete per adopted technology (hardening standards, network segregation, secrets management for cloud/containers/APIs/microservices) and reflect them in designs.
- Check compliance with the principles at design review (and threat modeling), and manage exceptions with documented risk assessment/approval/compensating controls/expiry.
- Review and update the principles and reference architectures periodically based on threat intelligence, lessons from incidents, and the adoption of new technologies, and keep a change history.

## Related controls and attributes

- ISO 27001 clauses: 6.1 (Actions to address risks and opportunities), 8.1 (Operational planning and control), 6.2 (Information security objectives), 7.2 (Competence)
- Adjacent Annex A: A.8.25 (Secure development life cycle), A.8.26 (Application security requirements), A.8.28 (Secure coding), A.8.29 (Security testing in development and acceptance), A.8.9 (Configuration management), A.8.22 (Segregation of networks), A.8.4 (Access to source code), A.5.8 (Information security in project management)
- ISMS-P mapping: 2.8.1 Security requirements definition (related: 2.6.1 Network access, 2.6.2 Information system access, 2.5.5 Privileged account and rights management, 2.10.2 Cloud security)
- 2013 mapping: 14.2.5 (Secure system engineering principles)

## Evidence

- Secure system architecture and engineering principles document (policy/standard) with approval/sharing records
- Reference architectures, secure design patterns, and a list of standard security components
- Security architecture design documents for new/changed systems (trust boundaries, data flows, control placement)
- Design review/threat modeling results and records of principle-compliance checks
- Technology-specific security baselines (hardening/cloud/container/API) documents
- Risk assessment/approval/compensating-control records for exceptions to the principles
- Change history of periodic reviews/updates of the architecture principles

## Nonconformity examples

- Security architecture/engineering principles are not documented, so the security level varies from project to project at the designer's discretion.
- Principles exist, but there is no procedure to verify their application to new designs and significant changes, so they are not actually reflected.
- Systems are designed to rely on a single control (for example, a perimeter firewall) without defense in depth, so a single breach fully exposes the interior.
- Least privilege/segregation of duties is not reflected in the design, so service accounts/administrative rights are granted excessively.
- When adopting new technologies such as cloud/containers, the existing principles are not made concrete, so systems are deployed with insecure default settings.
- Exceptions to the principles are allowed arbitrarily without risk assessment/approval, and compensating controls are not managed.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
