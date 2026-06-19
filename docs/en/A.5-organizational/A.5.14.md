# A.5.14 Information transfer

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.14 Information transfer |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.10.5 Information transfer security (related: 2.3.2 Security in external party contracts) |
| 2013 mapping | 13.2.1 Information transfer policies and procedures, 13.2.2 Agreements on information transfer, 13.2.3 Electronic messaging |

## Control objective

This control requires that confidentiality, integrity, and availability be maintained whenever information is exchanged between internal units and with external parties. Its scope covers electronic transfer (email, file transfer, messaging, system interfaces), physical media transfer (movement of documents and storage media), and verbal transfer (in person, by phone, in meetings). The aim is to establish policies and procedures for each transfer method so that information is not intercepted, altered, lost, or misdelivered in transit, and to put agreements in place for transfers with external parties that define the responsibilities and protection levels of each side. The level of protection should be applied in proportion to the classification of the information.

## Key checkpoints

1. Are protection policies and procedures established for each transfer method (electronic/physical/verbal), with protection levels differentiated by information classification?
2. Are transfer agreements (contracts/arrangements) concluded with external parties that define responsibilities, protective measures, incident notification/handling, and return/disposal?
3. Are technical safeguards such as transport encryption, integrity checking, and recipient authentication applied to electronic transfers?
4. When physical media are transported, are controls such as trusted couriers, packaging/sealing, and handover records applied?
5. Are measures in place to prevent misdelivery, wrong attachments, and unauthorized auto-forwarding in email/messaging?
6. Are employees and external parties aware of and compliant with transfer rules and precautions, including preventing verbal disclosure in public places?

## Implementation guidance

- Define, in line with the classification scheme, which channels are permitted and what protection each requires, and document this as policies and procedures covering electronic, physical, and verbal transfer.
- Apply transport encryption (such as TLS) by default to electronic channels (email, large-file transfer, SFTP, API interfaces), and add end-to-end or document-level encryption for sensitive information.
- Where there is regular or bulk transfer with external organizations, include in the data transfer agreement the security requirements, allocation of responsibility, incident notification procedure, data return/disposal conditions, and restrictions on onward transfer.
- Control the movement of physical media (documents, removable storage) through approved transport procedures, locked storage, sealing, and handover logs, and encrypt the information held on the media.
- Operate measures to prevent misdelivery and leakage: recipient address confirmation, external-send warnings, send delay/recall, approval for large or sensitive sends, and DLP rules.
- Include in training the awareness criteria for verbal transfer, such as limiting conversations in public places, guarding against eavesdropping in meeting rooms, and caution with speakerphone/video conferencing.
- Keep transfer records (sender, recipient, time, information transferred) and periodically review for abnormal sending to act on anomalies.

## Related controls and attributes

- ISO 27001 clauses: 6.1 (Actions to address risks), 8.1 (Operational planning and control), 7.5 (Documented information)
- Adjacent Annex A: A.5.10 (Acceptable use of information and other associated assets), A.5.13 (Labelling of information), A.5.33 (Protection of records), A.6.6 (Confidentiality or non-disclosure agreements), A.8.12 (Data leakage prevention), A.8.24 (Use of cryptography)
- ISMS-P mapping: 2.10.5 Information transfer security (related: 2.3.2 Security in external party contracts)
- 2013 mapping: 13.2.1 Information transfer policies and procedures, 13.2.2 Agreements on information transfer, 13.2.3 Electronic messaging

## Evidence

- Information transfer policy/procedure (covering electronic, physical, and verbal transfer) and transfer guidance per classification
- Data transfer agreements/contracts with external parties (including security requirement clauses)
- Encryption configuration records for electronic transfer (TLS, mail encryption, SFTP setup)
- Handover logs for physical media transport, and sealing/packaging and media-encryption records
- Email security settings (external-send warning, DLP rules, auto-forward restriction) and approval history for large/sensitive sends
- Transfer-related training materials and completion records for employees and external parties, plus transfer logs/review results

## Nonconformity examples

- A transfer policy exists but lacks procedures for physical media transport or verbal transfer, being limited to electronic transfer only.
- Sensitive or personal information is sent to external parties by email in plaintext without encryption.
- Information is regularly transferred to external organizations without concluding a transfer agreement that sets out security requirements and responsibilities.
- A large-file transfer service shares links without expiry or access controls, allowing an unspecified number of people to download.
- Email auto-forwarding rules continuously send internal information to personal external accounts without control or monitoring.
- Data is taken out on removable storage media without handover records or media encryption.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
