# A.7.9 Security of assets off-premises

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.7 Physical controls |
| Control | A.7.9 Security of assets off-premises |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.10.6 Business-use device security (related: 2.4.6 Control of devices brought in and out, 2.10.7 Management of removable storage media) |
| 2013 mapping | A.11.2.6 |

## Control objective

The purpose is to protect assets that are used or stored outside the organization's controlled facilities (offices, server rooms, and the like) against theft, loss, damage, and unauthorized access or disclosure. It covers assets taken off-site such as laptops, mobile devices, and portable storage, as well as equipment located externally for telework, remote or field work, travel, repair, outsourcing, or lease. The objective is to preserve the confidentiality, integrity, and availability of information even where the organization cannot fully exercise control over the physical environment off-premises.

## Key checkpoints

1. Is there a procedure to pre-authorize and register the removal of assets off-site, recording the holder, asset, removal period, and purpose?
2. Do off-premises laptops/mobiles have required encryption, strong authentication, and automatic locking, with remote lock/wipe prepared according to support and authorized scope?
3. Are physical protection guidelines in place so that assets are not left unattended in transit, public places, public transport, vehicles, or accommodation?
4. Are asset-handling responsibilities and security obligations defined and communicated to teleworkers and remote or field staff?
5. Are repair/outsourcing/lease distinguished from disposal when defining data protection, media removal or sanitization, and return verification?
6. Is there a reporting and response procedure (remote lock/wipe, credential revocation, and the like) for loss or theft of off-premises assets?

## Implementation guidance

- Define in policy which assets may be taken off-site and under what conditions (approver, permitted period, scope of use), and manage removal and return history in a register or log.
- Apply encryption, strong authentication, and automatic locking to off-premises devices and media. Use remote location/lock/wipe according to legal authority, device support, and connectivity; sending a command does not establish completion.
- Prohibit leaving assets unattended in public places, public transport, vehicles, or accommodation, and recommend privacy filters against shoulder surfing and physical locking devices.
- Handle and transport equipment in line with manufacturer guidance (temperature, humidity, shock, electromagnetic exposure) and protect it against damage in transit.
- Train teleworkers and remote or field staff on precautions (avoiding untrusted networks, secure storage, blocking access by family or third parties) and assign clear handling responsibility.
- Before external repair/outsourcing, make necessary backups and protect information through media removal, deletion, or suitable encryption and access restrictions. For disposal/reuse, follow validated sanitization under A.7.14; enabled encryption alone does not establish deletion. Include protection duties and return/processing evidence in contracts.
- Where appropriate, set insurance or liability limits and predefine reporting channels and remote response procedures for loss or theft.

## Related controls and attributes

- ISO 27001 clauses: 6.1 (Actions to address risks and opportunities), 7.5 (Documented information), 8.1 (Operational planning and control), 9.1 (Monitoring, measurement, analysis and evaluation)
- Adjacent Annex A: A.8.1 (User endpoint devices), A.6.7 (Remote working), A.7.10 (Storage media), A.5.11 (Return of assets), A.7.8 (Equipment siting and protection), A.7.14 (Secure disposal or re-use of equipment)
- ISMS-P mapping: 2.10.6 Business-use device security (related: 2.4.6 Control of devices brought in and out, 2.10.7 Management of removable storage media)
- 2013 mapping: A.11.2.6 (Security of equipment and assets off-premises)

## Evidence

- Approval records and register for off-premises removal of assets
- Device encryption/MDM/EMM policy and deployment status (configuration screens, enrolled device list)
- Remote and telework security guidelines and training/acknowledgement records
- Data deletion/encryption confirmation and outsourcing contracts for equipment sent off-site for repair
- Records of loss/theft reporting and response (remote lock/wipe, credential revocation)
- Return confirmation records for assets removed off-site

## Nonconformity examples

- Laptops or mobile devices are taken off-site without authorization or registration, so no removal history can be confirmed.
- Off-premises devices lack required encryption, authentication, locking, and loss-response arrangements, exposing information on loss.
- No asset-handling guidance or accountability exists for teleworkers, so the level of protection relies on individual judgment.
- Equipment with sensitive data is sent for repair without media removal, deletion, or suitable encryption and access restrictions.
- No reporting or response procedure exists for loss or theft of off-premises assets, so remediation is delayed.
- Return of removed assets is not tracked, so unreturned assets are left unaccounted for.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
