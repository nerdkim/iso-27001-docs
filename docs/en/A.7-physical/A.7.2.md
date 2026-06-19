# A.7.2 Physical entry

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.7 Physical controls |
| Control | A.7.2 Physical entry |
| Control type (ref.) | Preventive / Detective |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.4.2 Access control (related: 2.4.1 Designation of protected areas, 2.4.3 Information system protection, 2.4.6 Control of devices brought in and out) |
| 2013 mapping | 11.1.2, 11.1.6 |

## Control objective

This control requires that entry to protected areas and facilities be restricted through appropriate entry controls so that only authorized personnel can access each area. The intent is to apply entry procedures and control strength commensurate with the sensitivity of each area, such as office space, computer rooms, and delivery/loading areas, and to retain entry records so that access can be traced afterward. This reduces the risk of exposure, theft, damage, or service disruption caused by unauthorized physical access, and removes control blind spots by identifying, escorting, and supervising visitors and external personnel.

## Key checkpoints

1. Are entry control mechanisms (access cards, biometrics, locks, etc.) and authentication strength applied differentially according to the sensitivity of each protected area?
2. Are the granting, modification, and revocation of entry rights performed through an approval procedure, with rights promptly adjusted upon transfer, resignation, or contract termination?
3. Is the entry of visitors and external personnel controlled through identity verification, prior approval, recording of visit purpose, and escort/supervision?
4. Are entry records for each area (entry/exit times, identity, etc.) generated, retained, and reviewed periodically?
5. Are external-facing points such as delivery/loading areas separated from and controlled apart from internal protected areas?
6. Are secondary entry paths (emergency exits, shutters, rear doors) and bypass/unauthorized opening of the entry control system (including tailgating) addressed?

## Implementation guidance

- Define entry control levels according to area sensitivity (general office, computer room, communications room, records storage, etc.) and apply authentication means (single/multi-factor) commensurate with each level.
- Grant entry rights minimally on the basis of business need (need-to-enter), and clearly define the request/approval/granting/revocation procedure, owners, and required records.
- Issue visitor badges after prior approval and identity verification, record the purpose/time/host of each visit, and provide continuous escort/supervision in sensitive areas.
- Integrate the entry control system (card readers, biometrics, electronic locks, etc.) with monitoring means (CCTV, alarms) to detect and respond to unauthorized entry and tailgating.
- Retain entry records securely for a defined period and review them periodically to identify abnormal entries (unauthorized attempts, late-night entry, etc.).
- Separate delivery/loading areas so that outsiders cannot enter internal protected areas, and operate inspection and receipt procedures for incoming goods.
- Establish procedures for lost/damaged/unreturned access cards or keys (immediate deactivation, controlled reissuance) and periodically verify validity so that no residual rights remain.

## Related controls and attributes

- ISO 27001 clauses: 6.1 (Actions to address risks and opportunities), 7.5 (Documented information), 8.1 (Operational planning and control), 9.1 (Monitoring, measurement, analysis and evaluation)
- Adjacent Annex A: A.7.1 (Physical security perimeters), A.7.3 (Securing offices, rooms and facilities), A.7.4 (Physical security monitoring), A.7.6 (Working in secure areas), A.5.15 (Access control), A.5.20 (Addressing information security within supplier agreements), A.6.7 (Remote working)
- ISMS-P mapping: 2.4.2 Access control (related: 2.4.1 Designation of protected areas, 2.4.3 Information system protection, 2.4.6 Control of devices brought in and out)
- 2013 mapping: 11.1.2 (Physical entry controls), 11.1.6 (Delivery and loading areas)

## Evidence

- Definitions of entry control levels and control mechanisms per area
- Records of requesting/approving/granting/modifying/revoking entry rights (rights register)
- Visitor management log (identity verification, visit purpose, badge issuance/return, escort records)
- Entry control system logs (entry/exit records) and results of periodic reviews
- Operation and integration records of monitoring means such as CCTV/alarms
- Inspection/receipt records of incoming goods in delivery/loading areas
- Records of access card/key issuance, return, and loss response

## Nonconformity examples

- The same entry control mechanism is applied to sensitive areas (such as computer rooms) and general offices, so no differential control by level exists.
- Visitors are admitted without identity verification or prior approval, or move unaccompanied in sensitive areas without escort/supervision.
- Entry rights are not revoked after a transfer or resignation, so unnecessary entry rights remain.
- Entry records are not generated, or are not retained/reviewed, making later tracing and identification of abnormal entry impossible.
- No controls exist against tailgating or bypass entry through emergency exits/rear doors.
- Delivery/loading areas are not separated from internal protected areas, allowing outsiders to enter the interior without control.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
