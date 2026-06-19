# A.8.1 User endpoint devices

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.1 User endpoint devices |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.10.6 Business-use device security |
| 2013 mapping | A.6.2.1, A.11.2.8 |

## Control objective

This control protects information that is stored on, processed by, or accessed through user endpoint devices such as laptops, desktops, smartphones, and tablets. Because these devices operate outside the controlled data-center perimeter and are exposed to loss, theft, and untrusted networks, they require both a use policy and technical safeguards. It requires managing device registration, configuration, and user responsibilities so that information is not exposed through the endpoint.

## Key checkpoints

1. Is there a policy defining secure configuration and use of user endpoint devices, and are users made aware of their responsibilities?
2. Are endpoint devices that access organizational information registered/identified, and is ownership (corporate-issued / personally owned (BYOD)) distinguished?
3. Is a technical baseline applied to endpoints: disk encryption, screen lock, malware protection, patching, and restriction of unauthorized software?
4. Is there a remote lock/wipe capability and a reporting procedure for lost/stolen devices, and is it followed?
5. For BYOD, are business and personal data separated, and are intellectual property/licensing/privacy matters handled with user consent?
6. Is access to information and use of endpoints controlled according to network location/trust level, such as public networks or teleworking?

## Implementation guidance

- Establish an endpoint device policy covering registration, permitted use, minimum security configuration, and user obligations, and obtain user acknowledgment/signature.
- Enforce the technical baseline through endpoint management (MDM/UEM): storage encryption, automatic screen lock, strengthened authentication, patching, and malware protection.
- Restrict installation of unauthorized software and control administrator privileges; for BYOD, separate business and personal areas through containerization/profiles.
- Provide remote lock/wipe, mandate prompt reporting of loss/theft, and link this to incident response (A.5.24).
- Apply least privilege, avoid storing sensitive data locally where risk is high (use centralized/virtual access), and control connections from untrusted public networks.
- On end of use, perform secure return/erasure (A.8.10) and access revocation, and ensure physical protection of off-premises devices (A.7.9).

## Related controls and attributes

- ISO 27001 clauses: 8.1 (Operational planning and control), 6.1 (Actions to address risks and opportunities)
- Adjacent Annex A: A.7.9 (Security of assets off-premises), A.6.7 (Remote working), A.5.10 (Acceptable use of information and other associated assets), A.8.24 (Use of cryptography), A.8.7 (Protection against malware), A.8.8 (Management of technical vulnerabilities), A.8.19 (Installation of software on operational systems)
- ISMS-P mapping: 2.10.6 Business-use device security
- 2013 mapping: A.6.2.1 (Mobile device policy), A.11.2.8 (Unattended user equipment)

## Evidence

- Endpoint device security policy / acceptable use policy and user acknowledgment (signature) records
- Endpoint/device inventory (including BYOD) with ownership type and assignment status
- MDM/UEM configuration screens: encryption, screen lock, patch status, application control
- Loss/theft reporting records and remote lock/wipe execution logs
- Records of secure erasure/return and access revocation on end of use/offboarding
- BYOD agreements addressing separation of business/personal areas, privacy, and intellectual property/licensing

## Nonconformity examples

- A laptop holding sensitive data is not encrypted, so information is exposed if it is lost or stolen.
- Endpoint devices are not registered/identified, so unmanaged devices access organizational information.
- There is no remote lock/wipe capability, and the lost-device reporting procedure is undefined or not followed.
- BYOD devices access business data with no separation from personal areas and no user consent procedure.
- Endpoint patching and malware protection are not applied consistently, leaving devices unpatched for a long time.
- Users are granted local administrator rights and install unauthorized software freely, neutralizing the baseline.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
