# A.7.6 Working in secure areas

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.7 Physical controls |
| Control | A.7.6 Working in secure areas |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.4.5 Working in protected areas (related: 2.4.6 Control of devices brought in and out, 2.4.2 Access control) |
| 2013 mapping | 11.1.5 |

## Control objective

This control requires that work performed inside secure areas (computer rooms, communications rooms, records storage, data centres, etc.), such as maintenance, construction, installation, cleaning, visits, and moving items in and out, be governed so that it does not lead to exposure, damage, unauthorized manipulation, or service disruption. Even where physical safeguards such as entry control and perimeters exist, unauthorized actions, photography, media introduction, or arbitrary configuration changes can occur at the moment work actually takes place. The organization should therefore preserve the security level even during work through prior approval, supervision during the work, and retention of work records. By managing the risk of the moment when people and equipment actually intervene in a secure area, this control reinforces the effectiveness of the overall physical security scheme.

## Key checkpoints

1. Is there a work control procedure that defines, per secure area, the permitted types of work, the approving authority, and the allowed working hours?
2. Is work inside secure areas performed only after a prior request/approval process, with the purpose, scope, personnel, and equipment used recorded and managed?
3. For external personnel such as maintenance contractors, are identity verification, temporary badge issuance, and continuous escort/supervision applied?
4. Are risky actions during work, such as photography, bringing in storage media/personal devices, and unauthorized network connection, notified in advance and controlled?
5. Is unattended lone work restricted, and are additional controls applied to work during vulnerable time windows (outside business hours, etc.)?
6. After work is completed, are the removal of introduced equipment/media confirmed, temporary changes reverted, and work records reviewed?

## Implementation guidance

- Document the permitted work types, approving authority, allowed working hours, and mandatory rules for each secure area, and apply control strength differentially to match the sensitivity of each area.
- Require work requests to state the purpose, scope, participating personnel, equipment/media brought in, and expected duration, and allow work to proceed only after prior approval.
- Issue temporary badges to external workers after identity verification, permit work only under the continuous escort/supervision of a responsible person, and recover the badge when work ends.
- Notify in advance the rules to be observed during work, such as restrictions on cameras/personal devices/storage media, prohibition of photography, and prohibition of arbitrary network connection or system manipulation, and set criteria for action upon violation.
- Prohibit unattended lone work, and apply reinforcing controls such as two-person teams or additional approval for work during vulnerable windows such as late night or holidays.
- On completion, confirm the removal of equipment/media brought in, revert any temporarily granted rights or changed configurations, and review work records (request forms, entry logs, CCTV, etc.) to check for anomalies.
- For repetitive work such as periodic maintenance, standardize the work procedure and approval method, and record work results and exceptions to feed into improvement.

## Related controls and attributes

- ISO 27001 clauses: 7.2 (Competence), 7.3 (Awareness), 8.1 (Operational planning and control), 9.1 (Monitoring, measurement, analysis and evaluation)
- Adjacent Annex A: A.7.1 (Physical security perimeters), A.7.2 (Physical entry), A.7.3 (Securing offices, rooms and facilities), A.7.4 (Physical security monitoring), A.7.10 (Storage media), A.6.3 (Information security awareness, education and training)
- ISMS-P mapping: 2.4.5 Working in protected areas (related: 2.4.6 Control of devices brought in and out, 2.4.2 Access control)
- 2013 mapping: 11.1.5 (Working in secure areas)

## Evidence

- Work control procedure/guideline for secure areas (permitted work, approving authority, rules, etc.)
- Work request/approval records (including electronic approval) and work completion confirmations
- Identity verification materials for external workers, temporary badge issuance/return register, escort/supervision records
- Register of equipment and storage media brought in and out during work
- CCTV footage of the work area, entry logs, and approval records for work during vulnerable windows
- Records of temporary rights/configuration grants and confirmation of their reversion

## Nonconformity examples

- A maintenance contractor enters the computer room and performs work without a prior request/approval.
- An external worker enters and works alone in the server room without escort/supervision by a responsible person.
- The work request has no record of the laptop/storage media brought in, so removal cannot be confirmed when work ends.
- A firewall rule opened temporarily or an account right granted during work is not reverted after completion.
- A rule prohibiting photography in secure areas exists, but a worker's mobile phone photography is not actually controlled.
- Lone work is carried out unattended during late-night hours with no control to restrict or supervise it.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
