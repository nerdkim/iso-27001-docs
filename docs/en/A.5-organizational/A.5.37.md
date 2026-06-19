# A.5.37 Documented operating procedures

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.37 Documented operating procedures |
| Control type (ref.) | Preventive, Corrective |
| Security properties (ref.) | Confidentiality, Integrity, Availability |
| ISMS-P mapping | 1.1.5 Establishment of policies |
| 2013 mapping | 12.1.1 Documented operating procedures |

## Control objective
This control requires that the activities used to operate information processing facilities and information systems be captured as standardized, documented procedures, so that personnel perform tasks consistently and correctly rather than relying on personal memory or experience. Well maintained operating procedures prevent human error, missed steps, and the service outages or security incidents that follow, and they preserve operational continuity across staff handovers, absences, and emergencies. Documented procedures also serve as the training baseline for new personnel and as evidence, during audits or reviews, that actual operations conform to control requirements.

## Key checkpoints
1. Are the main operational activities of information processing facilities and systems (startup/shutdown, backup/recovery, batch jobs, media handling, incident response, etc.) documented as operating procedures?
2. Do the procedures contain the information needed to execute them: scope, method and sequence of steps, responsible party and required privileges, normal/abnormal completion criteria, error/exception handling, and contact/escalation paths?
3. Are the operating procedures made available in an accessible form to the personnel who actually need to perform them, and kept current?
4. When system, configuration, or environment changes occur, are the related operating procedures updated, reviewed, and approved in conjunction with the change management process?
5. Is the validity of operating procedures reviewed periodically so that gaps between documented procedures and actual operations are identified and corrected?
6. Are the procedures reflected in training and handover so that new or rotating staff can understand and use them?

## Implementation guidance
- Identify the operational activities of information processing facilities and systems, and prioritize procedures for tasks that are repetitive/routine or high impact on error (backup, batch, startup/shutdown, incident handling, media management).
- In each procedure, state the target system/task, prerequisites and preconditions, step by step method, responsible party and required privileges, normal completion criteria, and handling of abnormal/error conditions with escalation contacts.
- Bring operating procedures into the organization's document management scheme (version, author/reviewer/approver, revision history, distribution scope) so the current version is clearly identifiable.
- Define access paths and permissions so personnel can consult procedures immediately when needed, balancing access control with availability (for example, offline copies and an emergency access method).
- On system, configuration, or environment changes, update the related procedures in conjunction with change management, and route the updates through review and approval.
- Review the validity of procedures periodically to detect divergence from actual operations, retire procedures for tasks no longer performed, and promptly reflect new or changed tasks.
- Use procedures as the baseline for onboarding and shift handover so that operational knowledge is not concentrated in a single individual.

## Related controls and attributes
- ISO 27001 clauses: 7.5 (Documented information), 8.1 (Operational planning and control), 7.2 (Competence)
- Adjacent Annex A: A.5.1 (Policies for information security), A.8.32 (Change management), A.8.9 (Configuration management), A.8.13 (Information backup)
- ISMS-P mapping: 1.1.5 Establishment of policies (adjacent: 1.3.3 Management of operational status, 2.1.1 Maintenance of policies, 2.9.1 Change management)
- 2013 mapping: 12.1.1 Documented operating procedures

## Evidence
- Operating procedures/operations manuals (backup/recovery, batch, startup/shutdown, incident handling, media handling, etc.)
- Version/revision history and author/reviewer/approver records for the procedures
- Distribution and access status of operating procedures (access permission lists, publication locations)
- Records of procedure updates linked to change management records
- Results of periodic procedure reviews and related improvement/correction records
- Records of procedures used in onboarding training and shift handover

## Nonconformity examples
- Key operational tasks such as backup or incident response depend solely on an individual's knowledge, with no documented procedure.
- Operating procedures exist but are left out of date, diverging from how operations are actually performed.
- After a system or configuration change, related operating procedures are not updated, so documentation and operations are inconsistent.
- Procedures are accessible only to a specific individual, so they cannot be used during shift work or when the person is absent or in an emergency.
- Procedures lack version/approval management, so the current version cannot be identified.
- Procedures omit error/exception handling or escalation contacts, delaying response during an incident.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
