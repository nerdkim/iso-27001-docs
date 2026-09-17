# A.8.7 Protection against malware

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.7 Protection against malware |
| Control type (ref.) | Preventive / Detective / Corrective |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.10.9 Malware control |
| 2013 mapping | A.12.2.1 |

## Control objective

This control protects information and information processing facilities against malware (viruses, worms, ransomware, trojans, and so on). It requires combining technical defenses (anti-malware/EDR, filtering, and so on) with user awareness so that malware is prevented from entering, infections are detected, and recovery is fast when infection occurs.

## Key checkpoints

1. Are anti-malware solutions installed and operated on in-scope assets (servers, endpoints, mobile devices, and so on), with engines/signatures kept up to date?
2. Are detection/response measures such as real-time monitoring, suitable scanning, and isolation operated according to asset type and supported capabilities, with validated alternatives where unavailable?
3. Is execution of unauthorized software/scripts controlled (for example, allow-listing, attachment/web filtering), and are external media and download paths scanned?
4. Is user awareness training on malware prevention conducted, and are reporting/response procedures in place when infection is found?
5. Are malware detection/blocking events logged and reviewed periodically, with significant infections escalated to incident response procedures?

## Implementation guidance

- Select suitable defenses per asset type (servers/PCs/mobile/virtualization/containers, and so on) and manage policy and update status centrally.
- Combine signature/behavior detection, allow-listing, and isolation according to asset needs. Schedule full scans after evaluating support and performance/safety impact; use validated alternatives for mobile, container, OT, or other environments that cannot support agents or scanning.
- Apply scanning and filtering to the main entry paths, including email attachments/URLs, web downloads, and removable media.
- Control privileges so end users cannot disable the defense solution or set exceptions on their own.
- Link with threat intelligence (A.5.7) and technical vulnerability management (A.8.8) to handle new/variant threats, and secure ransomware recovery capability through backups (A.8.13).
- Define and rehearse response procedures for containment, blocking, evidence preservation, and recovery before an infection occurs.

## Related controls and attributes

- ISO 27001 clauses: 8.1 (Operational planning and control), 6.1 (Actions to address risks and opportunities)
- Adjacent Annex A: A.5.7 (Threat intelligence), A.8.8 (Management of technical vulnerabilities), A.8.13 (Information backup), A.8.19 (Installation of software on operational systems), A.8.23 (Web filtering), A.6.3 (Information security awareness, education and training)
- ISMS-P mapping: 2.10.9 Malware control
- 2013 mapping: A.12.2.1 (Controls against malware)

## Evidence

- Deployment status of defense solutions (anti-malware/EDR) and policy configuration screens
- Engine/signature update history and full-scan execution records
- Malware detection/remediation/quarantine logs and review records
- Malware prevention training/notice materials for users
- Infection incident response procedure and response records

## Nonconformity examples

- Malware protection is missing or excepted for assets without risk assessment or alternative safeguards.
- A defense solution is installed but its engine/signatures have not been updated for a long time, so new malware is not detected.
- Real-time monitoring or scanning required by the approved protection plan is disabled or omitted without compensating controls.
- Malware detection logs are only collected but not reviewed, so repeated infection/spread goes unnoticed.
- Privileges are left unmanaged so users can stop the defense solution at will.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
