# A.5.26 Response to information security incidents

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.26 Response to information security incidents |
| Control type (ref.) | Corrective |
| Security properties (ref.) | Confidentiality/Integrity/Availability |
| ISMS-P mapping | 2.11.5 Incident response and recovery |
| 2013 mapping | 16.1.5 Response to information security incidents |

## Control objective
This control ensures that matters classified as information security incidents are responded to, contained, and recovered from promptly, following procedures and assigned responsibilities defined in advance. Damage and recurrence are minimized when designated personnel consistently carry out the stages that follow detection: initial assessment, containment, eradication, recovery, closure decision, and external notification. The aim is to preserve evidence during response, communicate with stakeholders in a timely manner, and record the handling results as a basis for later improvement.

## Key checkpoints
1. Are response procedures and a response organization (roles/responsibilities/escalation paths) defined in advance by incident type and severity?
2. After an incident is received, do designated personnel carry out and record staged actions through containment, eradication, recovery, and closure?
3. During response, is evidence needed for later analysis or legal action collected and preserved without corruption?
4. Are notification obligations under law or contract (regulators, data subjects/customers, partners) identified and met within the required deadlines?
5. Are response outcomes (cause, actions, impact, recurrence prevention) recorded and reported to relevant departments and management?

## Implementation guidance
- Define incident severity levels (for example high/medium/low) and document target response times and escalation criteria per level.
- On initial response, determine the scope of impact and prioritize containment actions (account lockout, session termination, network isolation) to stop the spread.
- Eradicate the root cause and remediate the vulnerability, then restore services/systems to a normal state and verify correct operation and absence of reinfection after recovery.
- Collect evidence such as logs, images, and memory dumps in a manner that preserves originality, and record custody/transfer history (chain of custody).
- For reportable incidents such as personal data breaches, confirm statutory deadlines and notification recipients and complete notification/reporting without omission.
- Keep a chronological incident log of the whole response, and on closure produce a handling report that feeds into learning from incidents (A.5.27).

## Related controls and attributes
- ISO 27001 clauses: 10.1 Nonconformity and corrective action, 8.1 Operational planning and control, 7.4 Communication
- Adjacent Annex A: A.5.24 Information security incident management planning and preparation, A.5.25 Assessment and decision on information security events, A.5.27 Learning from information security incidents, A.5.28 Collection of evidence, A.5.29 Information security during disruption, A.6.8 Information security event reporting
- ISMS-P mapping: 2.11.5 Incident response and recovery
- 2013 mapping: 16.1.5 Response to information security incidents

## Evidence
- Incident response procedures and severity level/escalation criteria
- Response organization chart and role/responsibility (RACI) definitions
- Records of individual incidents (incident log, containment/recovery actions, timeline)
- Evidence collection and chain-of-custody records
- External notification/reporting documents to regulators/data subjects and proof of dispatch
- Incident closure reports and records of reporting to management

## Nonconformity examples
- Response procedures exist but lack severity levels/escalation criteria, so the level of response varies from incident to incident.
- Recovery is started without containment, so the incident recurs while the attacker remains present.
- Logs are arbitrarily deleted or overwritten during response, destroying evidence needed for root-cause analysis and legal action.
- A personal data breach is recognized but regulator/data-subject notification is not made within the statutory deadline.
- An incident is handled but the outcome and cause are not recorded, so it does not lead to recurrence prevention or lessons learned.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
