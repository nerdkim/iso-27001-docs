# A.5.29 Information security during disruption

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.29 Information security during disruption |
| Control type (ref.) | Preventive/Corrective |
| Security properties (ref.) | Confidentiality/Integrity/Availability |
| ISMS-P mapping | 2.12.1 Safety measures for disaster/emergency preparedness |
| 2013 mapping | 17.1.1, 17.1.2, 17.1.3 |

## Control objective
This control requires the organization to plan in advance so that its information security level is not inappropriately degraded while normal operations are disrupted or switched to alternative arrangements due to a disaster, crisis, or major incident. During a crisis, the pressure to recover quickly often weakens security controls through relaxed access controls, temporary workarounds, or use of less-hardened alternative environments. The aim is to keep confidentiality, integrity, and availability at an appropriate level throughout the disruption and to restore controls to their normal state once operations return to normal. Unlike A.5.30 (ICT readiness for business continuity), which addresses technical recovery capability, this control focuses on sustaining and restoring security controls across the whole disruption period.

## Key checkpoints
1. Are information security requirements embedded in the business continuity/disaster recovery framework, defining the security level to be maintained during disruption?
2. Are core security controls (access control, encryption, backup, logging) applied at the alternative site/emergency operating environment to the same standard as the normal environment?
3. Are approval, usage recording, and revocation procedures in place for emergency/temporary privileges granted during a crisis?
4. Are security roles, responsibilities, and decision authority assigned for disruption, and is an emergency contact scheme maintained?
5. Is there a procedure to reverse temporary measures/workarounds introduced during disruption and re-establish security controls upon return to normal?
6. Are the related plans validated through testing/exercises, with results fed back into improvement?

## Implementation guidance
- Integrate information security requirements into the business continuity plan (BCP)/disaster recovery plan (DRP) and define the minimum security control baseline to maintain for each type of disruption.
- Design each alternative processing mode (alternative site, cloud failover, manual operation) so that access control, encryption, backup, and logging/monitoring are maintained at normal levels.
- Define a break-glass emergency access procedure that specifies the approval path, usage logging, post-event review, and automatic/manual revocation.
- Document the security owner and roles (RACI), escalation paths, and internal/external communication criteria for disruption, and keep the emergency contact list current.
- Reflect obligations to maintain security and notification requirements during disruption in contracts with alternative-environment and service providers (A.5.19-A.5.22) and cloud services (A.5.23).
- Establish a return-to-normal procedure covering removal of temporary controls, data integrity verification, and access rights reset, and improve the plan periodically using exercise and real-incident results.

## Related controls and attributes
- ISO 27001 clauses: 6.1 Actions to address risks and opportunities, 8.1 Operational planning and control, 10.1/10.2 Continual improvement and corrective action
- Adjacent Annex A: A.5.30 ICT readiness for business continuity, A.5.24 Information security incident management planning and preparation, A.5.26 Response to information security incidents, A.8.13 Information backup, A.8.14 Redundancy of information processing facilities
- ISMS-P mapping: 2.12.1 Safety measures for disaster/emergency preparedness (related: 2.12.2 Disaster recovery testing and improvement, 2.9.3 Backup and recovery management)
- 2013 mapping: 17.1.1 Planning information security continuity, 17.1.2 Implementing information security continuity, 17.1.3 Verify, review and evaluate information security continuity

## Evidence
- BCP/DRP with embedded information security requirements, and the minimum security control baseline per disruption type
- Security configuration records for the alternative site/emergency operating environment (access control, encryption, backup, logging settings)
- Break-glass emergency access procedure and approval/usage/revocation records
- Security roles and responsibilities (RACI), emergency contact list, and escalation scheme for disruption
- Return-to-normal procedure and records of temporary-control removal/restoration
- Exercise/test plans and result reports, and plan revision history

## Nonconformity examples
- A BCP/DRP exists but does not embed information security requirements, so the security level to maintain during alternative operation is undefined.
- The alternative site is configured with weaker access control/encryption/logging than the primary site, degrading the security level during disruption.
- Emergency privileges granted during a crisis are neither logged nor revoked, so excessive privileges persist after return to normal.
- Temporary workarounds introduced during disruption are not reversed on return to normal and remain as vulnerabilities.
- The related plans are never validated through exercises, so whether security controls hold during an actual disruption cannot be confirmed.
- Contracts with alternative service/cloud providers omit obligations to maintain security and notification requirements during disruption, leaving responsibility unclear.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
