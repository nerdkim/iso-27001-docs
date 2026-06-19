# A.5.25 Assessment and decision on information security events

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.25 Assessment and decision on information security events |
| Control type (ref.) | Detective/Corrective |
| Security properties (ref.) | Confidentiality/Integrity/Availability |
| ISMS-P mapping | 2.11.1 Establishing incident prevention and response system |
| 2013 mapping | A.16.1.4 |

## Control objective
This control assesses information security events against predefined categorization and prioritization criteria and consistently decides whether each event should be classified as an information security incident. Not every event is an incident, so the essential task is to filter out false positives, duplicates, and minor events while quickly identifying events that require a real response. By recording the basis for each assessment and decision, the organization allocates response resources by priority and secures a starting point for later analysis and improvement.

## Key checkpoints
1. Are criteria (severity/impact/priority) defined for deciding whether an information security event is classified as an incident?
2. Are received events assessed by a designated person/team (e.g., a response team) against the defined criteria?
3. Are the assessment result, the incident classification decision, and its rationale recorded?
4. For events decided to be incidents, are they connected to a response and escalation procedure matching their grade/priority?
5. Are the assessment/decision criteria reviewed periodically to reduce false positives and missed detections?

## Implementation guidance
- Document a classification scheme (categories, severity grades, priorities) for deciding whether an event is an incident, and share it across the organization.
- Designate an event intake channel (single point of contact) and operate a procedure that assesses received events against consistent criteria.
- During assessment, jointly consider asset criticality, scope of impact, likelihood of spread, and legal/regulatory notification requirements.
- Record the assessment result (incident/non-incident), classification grade, decision rationale, decision-maker, and timestamp in the incident management system.
- Immediately connect events decided as incidents to the grade-based response procedure (A.5.26) and the escalation/notification path.
- Periodically analyze false-positive/miss rates and reclassification cases to improve the classification criteria and thresholds.

## Related controls and attributes
- ISO 27001 clauses: 9.1 Monitoring, measurement, analysis and evaluation; 10.1 Continual improvement; 10.2 Nonconformity and corrective action
- Adjacent Annex A: A.5.24 Information security incident management planning and preparation, A.5.26 Response to information security incidents, A.5.27 Learning from information security incidents, A.6.8 Information security event reporting, A.8.15 Logging, A.8.16 Monitoring activities
- ISMS-P mapping: 2.11.1 Establishing incident prevention and response system (related: 2.11.3 Anomaly analysis and monitoring, 2.11.5 Incident response and recovery)
- 2013 mapping: A.16.1.4

## Evidence
- Event/incident classification criteria and priority definitions
- Event intake/assessment log (including assessment result, incident decision, and rationale)
- Assessment/decision records in the incident management system (tickets)
- Escalation/notification criteria and actual notification history
- Classification criteria review/revision history and false-positive/reclassification analysis reports

## Nonconformity examples
- With no criteria for classifying events as incidents, judgments vary by individual and the response is delayed.
- The basis for assessing/deciding on received events is not recorded, so the reasoning cannot be verified after the fact.
- An event that is in fact an incident is misjudged as minor, and the response and notification deadlines are missed.
- An event is decided to be an incident but is not assigned a grade/priority, so response resources are not allocated.
- False positives recur but the classification criteria/thresholds are not reviewed, so a real incident is buried in noise.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
