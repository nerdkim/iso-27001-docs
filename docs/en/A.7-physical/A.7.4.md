# A.7.4 Physical security monitoring

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.7 Physical controls |
| Control | A.7.4 Physical security monitoring |
| Control type (ref.) | Preventive, Detective |
| Security properties (ref.) | Confidentiality, Integrity, Availability |
| ISMS-P mapping | 2.4.2 Physical entry control |
| 2013 mapping | New in 2022 |

## Control objective
The purpose is to keep facilities that hold information and information processing equipment under continuous surveillance so that unauthorized physical access attempts are detected in real time or after the fact and can be acted upon. To recognize early when entry control or a perimeter is bypassed or defeated and to preserve evidence, the organization should deploy and operate monitoring means such as surveillance cameras, intrusion detection, alarms, and staffed guarding in proportion to assessed risk. Monitoring serves as the last line that detects failures of preventive controls and connects them to a fast response, underpinning the overall effectiveness of physical security.

## Key checkpoints
1. Are monitoring means such as surveillance cameras, intrusion sensors, and alarm systems installed and operated in proportion to risk for areas holding information processing facilities and sensitive information?
2. Have the areas to be monitored and their blind spots been identified, with key points such as entry routes, doors, and the outer boundary included in coverage?
3. Are the retention period, storage location, and access rights for monitoring records (video, alarm history) defined, and are the records protected against unauthorized viewing or tampering?
4. Are verification, escalation, and response procedures, responsible personnel, and response-time targets defined for alarms, and do they actually work?
5. Is there a means to detect and respond to failure, power loss, network disconnection, or tampering of the monitoring system itself?
6. Does camera operation comply with legal requirements for protecting personal (image) data, such as signage, capture scope, and viewing controls?

## Implementation guidance
- Define the areas and points that need monitoring from risk assessment, and deploy a layered combination of surveillance cameras, intrusion detection, alarms, and staffed guarding.
- Map key points and blind spots such as doors, entry routes, loading bays, and data center or server room interiors, and minimize blind spots through camera fields of view and sensor placement.
- Set retention periods and storage media for monitoring records, and protect the record store physically and logically so an intruder cannot delete or alter the records.
- Integrate alarms so that a control or security operator is notified immediately, and document the verification, on-site dispatch, and escalation stages along with response-time targets.
- Apply redundancy and uninterruptible power to the power, network, and storage of the monitoring system, and configure it to detect defeat attempts such as camera obstruction, sensor tampering, or signal loss.
- Test and inspect monitoring means and alarms periodically for correct operation, and record responses to false alarms and real incidents to feed improvement.
- Ensure camera installation and operation comply with personal data protection law through signage, defined capture purpose and scope, controls on viewing and disclosure of footage, and access-right management.

## Related controls and attributes
- ISO 27001 clauses: 8.1 (operational planning and control), 9.1 (monitoring and measurement), 10.2 (nonconformity and corrective action)
- Adjacent Annex A: A.7.1 (Physical security perimeters), A.7.2 (Physical entry), A.7.3 (Securing offices, rooms and facilities), A.5.7 (Threat intelligence), A.8.16 (Monitoring activities)
- ISMS-P mapping: 2.4.2 Physical entry control
- 2013 mapping: New in 2022

## Evidence
- Physical monitoring policy or guideline (monitored areas, monitoring means, record retention criteria)
- Camera and sensor placement plans and a list of monitoring points
- Records for retention period and access-right management of monitoring records (video/alarm)
- Alarm response procedure documents and records of actual alarms and responses
- Results of periodic inspection and testing of the monitoring system and fault response records
- Camera installation signage and records of controls on viewing and disclosure of image data

## Nonconformity examples
- No cameras cover the server room interior or its doors, so there is no means to detect or trace unauthorized access when it occurs.
- Cameras are installed but do not record, or the retention period has lapsed, so no footage remains for the time of an incident.
- An intrusion alarm notifies only a single person, but no response procedure or accountable owner is defined, so the alarm is left unattended.
- The monitoring record store is located inside the monitored area itself, so an intruder can easily remove the records.
- Camera fields of view leave many blind spots, omitting key entry routes from coverage.
- Camera operation lacks installation signage and controls on footage viewing, so personal data protection requirements are not met.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
