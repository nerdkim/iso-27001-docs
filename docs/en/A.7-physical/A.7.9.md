# A.7.9 Security of assets off-premises

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.7 Physical controls |
| Control | A.7.9 Security of assets off-premises |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality, Integrity, Availability |
| ISMS-P mapping | 2.10.6 Business device security (related: 2.4.6 Control of equipment carried in and out, 2.10.7 Removable media management) |
| 2013 mapping | 11.2.6, 6.2.1 |

## Control objective
The purpose is to protect assets that are used or stored outside the organization's controlled facilities (offices, server rooms, and the like) against theft, loss, damage, and unauthorized access or disclosure. It covers assets taken off-site such as laptops, mobile devices, and portable storage, as well as equipment located externally for telework, remote or field work, travel, repair, outsourcing, or lease. The objective is to preserve the confidentiality, integrity, and availability of information even where the organization cannot fully exercise control over the physical environment off-premises.

## Key checkpoints
1. Is there a procedure to pre-authorize and register the removal of assets off-site, recording the holder, asset, removal period, and purpose?
2. Are protective measures such as disk encryption, strong authentication, automatic screen lock, and remote lock/wipe applied to laptops and mobile devices used off-premises?
3. Are physical protection guidelines in place so that assets are not left unattended in transit, public places, public transport, vehicles, or accommodation?
4. Are asset-handling responsibilities and security obligations defined and communicated to teleworkers and remote or field staff?
5. For equipment sent off-site for repair, outsourcing, lease, or disposal, are data-handling (prior deletion/encryption) and return procedures defined?
6. Is there a reporting and response procedure (remote lock/wipe, credential revocation, and the like) for loss or theft of off-premises assets?

## Implementation guidance
- Define in policy which assets may be taken off-site and under what conditions (approver, permitted period, scope of use), and manage removal and return history in a register or log.
- Apply disk/file encryption, strong authentication, automatic screen lock, and remote location/lock/wipe (MDM/EMM) to devices and media used off-premises.
- Prohibit leaving assets unattended in public places, public transport, vehicles, or accommodation, and recommend privacy filters against shoulder surfing and physical locking devices.
- Handle and transport equipment in line with manufacturer guidance (temperature, humidity, shock, electromagnetic exposure) and protect it against damage in transit.
- Train teleworkers and remote or field staff on precautions (avoiding untrusted networks, secure storage, blocking access by family or third parties) and assign clear handling responsibility.
- Before sending equipment off-site for repair, outsourcing, or disposal, delete or encrypt sensitive data in advance, and include security requirements and return/destruction confirmation in the contract.
- Where appropriate, set insurance or liability limits and predefine reporting channels and remote response procedures for loss or theft.

## Related controls and attributes
- ISO 27001 clauses: 6.1 (actions to address risks and opportunities), 7.5 (documented information), 8.1 (operational planning and control), 9.1 (monitoring and measurement)
- Adjacent Annex A: A.8.1 (User endpoint devices), A.6.7 (Remote working), A.7.10 (Storage media), A.5.11 (Return of assets), A.7.8 (Equipment siting and protection), A.7.14 (Secure disposal or re-use of equipment)
- ISMS-P mapping: 2.10.6 Business device security (related: 2.4.6 Control of equipment carried in and out, 2.10.7 Removable media management)
- 2013 mapping: 11.2.6 (Security of equipment and assets off-premises), 6.2.1 (Mobile device policy)

## Evidence
- Approval records and register for off-premises removal of assets
- Device encryption/MDM/EMM policy and deployment status (configuration screens, enrolled device list)
- Remote and telework security guidelines and training/acknowledgement records
- Data deletion/encryption confirmation and outsourcing contracts for equipment sent off-site for repair
- Records of loss/theft reporting and response (remote lock/wipe, credential revocation)
- Return confirmation records for assets removed off-site

## Nonconformity examples
- Laptops or mobile devices are taken off-site without authorization or registration, so no removal history can be confirmed.
- Devices used off-premises lack disk encryption or remote lock/wipe, leaving information exposed if lost or stolen.
- No asset-handling guidance or accountability exists for teleworkers, so the level of protection relies on individual judgment.
- Storage media in equipment sent off-site for repair is removed without prior deletion or encryption.
- No reporting or response procedure exists for loss or theft of off-premises assets, so remediation is delayed.
- Return of removed assets is not tracked, so unreturned assets are left unaccounted for.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
