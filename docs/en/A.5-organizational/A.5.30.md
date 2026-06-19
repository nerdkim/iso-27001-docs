# A.5.30 ICT readiness for business continuity

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.30 ICT readiness for business continuity |
| Control type (ref.) | Preventive, Corrective |
| Security properties (ref.) | Integrity, Availability |
| ISMS-P mapping | 2.12.1 Safeguards against disasters and disruptions |
| 2013 mapping | New in 2022 |

## Control objective
ICT readiness for business continuity is the control for planning, implementing, maintaining, and testing the continuity and recovery capability of ICT services so that the organization can meet its predefined business continuity objectives. Based on business impact analysis (BIA) and risk assessment, it requires the organization to derive the recovery requirements (recovery time objective, recovery point objective, minimum service level) for the ICT services that support critical activities, and to put in place recovery strategies, configurations, and procedures that satisfy them. The aim is to keep ICT in a constant state of readiness and to verify it regularly, so that ICT can be restored quickly to the agreed level even during a disaster or disruption.

## Key checkpoints
1. Does the business impact analysis (BIA) identify critical activities and the ICT services that support them, with a recovery time objective (RTO) and recovery point objective (RPO) defined for each service?
2. Are ICT continuity/recovery strategies (redundancy, backup, alternate processing facilities, cloud-based recovery, etc.) established to meet the defined RTO/RPO, with the necessary resources secured?
3. Are ICT recovery procedures (fault detection, invocation criteria, recovery stages and priorities, roles/responsibilities, emergency contacts) documented and kept up to date?
4. Are the ICT continuity/recovery plans tested regularly and after significant changes, with results evaluated against RTO/RPO achievement and fed into improvement?
5. Are the backups, configuration information, documents, licenses, and access means needed for recovery protected and stored so that they remain usable during a disaster?
6. Is ICT readiness aligned and integrated with the organization's business continuity management (BCM) and its incident/crisis management arrangements?

## Implementation guidance
- Based on the BIA and risk assessment results, quantitatively define RTO/RPO/minimum service level for each critical ICT service, and confirm them as recovery targets with management approval.
- Select recovery strategies that meet the targets (system redundancy/clustering, geographically separated alternate processing facilities, data backup and offsite storage, cloud-based recovery, manual workarounds, etc.), and apply them differentially by service criticality with cost and risk in mind.
- Document the ICT continuity/recovery plan to include fault/disaster detection and invocation criteria, recovery priorities and stage-by-stage procedures, roles and responsibilities, emergency contact lists, coordination with external suppliers/telecom/cloud providers, and the procedure for returning to normal operation after recovery.
- Store the backups, system configuration/images, network diagrams, operational documents, software licenses, and credentials/access means essential to recovery in a separate secure location, and periodically verify their integrity and recoverability.
- Test the continuity/recovery plan regularly (and after significant infrastructure/configuration changes) using varied methods (checklist review, walk-through, simulation, live failover), and record RTO/RPO achievement and gaps as improvement items.
- Secure the availability of recovery resources such as people, skills, facilities, and external contracts, and ensure recovery is possible even when specific individuals are absent by training staff and designating backup personnel.
- Integrate the ICT readiness plan with the organization's business continuity management system and incident/crisis management procedures, and update them together whenever changes occur to keep them consistent.

## Related controls and attributes
- ISO 27001 clauses: 6.1 (Actions to address risks and opportunities), 8.1 (Operational planning and control), 8.2/8.3 (Information security risk assessment/treatment), 9.1 (Monitoring, measurement, analysis and evaluation)
- Adjacent Annex A: A.5.29 (Information security during disruption), A.5.24 (Information security incident management planning and preparation), A.8.13 (Information backup), A.8.14 (Redundancy of information processing facilities), A.8.6 (Capacity management), A.7.5 (Protecting against physical and environmental threats), A.7.11 (Supporting utilities)
- ISMS-P mapping: 2.12.1 Safeguards against disasters and disruptions (adjacent: 2.12.2 Disaster recovery testing and improvement, 2.9.3 Backup and recovery management, 2.11.5 Incident response and recovery, 2.9.2 Performance and fault management)
- 2013 mapping: New in 2022

## Evidence
- Business impact analysis (BIA) results and the RTO/RPO definition for each critical ICT service
- ICT continuity/recovery strategy document and architecture diagrams (redundancy, alternate processing facilities, backup architecture, etc.)
- ICT disaster recovery plan (DRP)/recovery procedures (including invocation criteria, recovery stages, roles/responsibilities, emergency contact lists)
- Recovery test plan and test result reports (RTO/RPO achievement, identified gaps, and improvement follow-up)
- Records of offsite storage of backups and configuration/documents, and recoverability verification (restore testing)
- Recovery-related training/exercise history and the designation of primary/backup personnel
- Recovery-related contracts/SLAs with external suppliers/telecom/cloud providers

## Nonconformity examples
- ICT recovery targets (RTO/RPO) are not defined because no BIA was performed, so there is no basis for recovery priorities or resource allocation.
- A disaster recovery strategy/plan exists but is outdated and inconsistent with the current infrastructure/configuration, with no update history.
- Backups are performed but restore testing has never been done, so recoverability in an actual disaster is unverified.
- After the recovery plan was established, no periodic test or post-significant-change test is performed at all.
- Configuration information, documents, licenses, and access means needed for recovery exist only at the primary site, so they are inaccessible during a disaster.
- Recovery procedures depend on specific individuals, with no backup personnel or training, so recovery is impossible when the owner is absent.
- RTO/RPO shortfalls were identified in testing but were left unaddressed rather than managed as improvement items.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
