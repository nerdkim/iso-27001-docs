# A.5.28 Collection of evidence

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.28 Collection of evidence |
| Control type (ref.) | Corrective |
| Security properties (ref.) | Confidentiality, Integrity, Availability |
| ISMS-P mapping | 2.11.5 Incident response and recovery |
| 2013 mapping | 16.1.7 Collection of evidence |

## Control objective
This control establishes and consistently applies, in advance, procedures for the identification, collection, acquisition, and preservation of evidence related to information security incidents so that the evidence can be used for disciplinary action, litigation, regulatory reporting, and cause analysis. If the integrity and chain of custody of evidence are not maintained, then no matter how much material is gathered after an incident, it may lose its value as evidence in legal or disciplinary proceedings. The aim is therefore to prepare procedures, roles, tools, and external cooperation arrangements before an incident occurs, so that evidence can be secured promptly and in a defensible manner when one happens.

## Key checkpoints
1. Are procedures for the identification/collection/acquisition/preservation of incident-related evidence documented, and do they reflect applicable laws and the evidence-admissibility criteria of the relevant jurisdiction?
2. Are a standard form and procedure in place to record and maintain the chain of custody, tracking acquisition time, handlers, and the movement/handover path?
3. For digital evidence, are methods defined to preserve the integrity of the original (forensic imaging, hash generation and verification, write-blocking, and similar)?
4. Are qualified internal staff or external specialists (forensic firms, law enforcement) designated in advance for collecting and handling evidence?
5. Are storage, sealing, access control, and retention periods defined for evidence, preventing unauthorized alteration and damage?

## Implementation guidance
- Define collection procedures and priorities for each evidence type (logs, disk images, memory dumps, network packets, documents, physical media), and specify an order that secures the most volatile evidence first (memory, sessions, temporary data).
- Standardize a chain-of-custody record that captures the acquisition date/time, location, handler, handover details, and storage location without gaps, and update it at every movement or examination.
- Work on verified copies (bit-level images) rather than analyzing the original directly, and generate a hash immediately after collection so that the copy can be proven identical to the original.
- Use write-blocking devices, verified forensic tools, and time-synchronized (NTP) system clocks to ensure collection integrity and a reliable timeline.
- Restrict evidence-handling privileges to a minimal set of qualified personnel, protect evidence with sealed and locked storage and access logs, and define retention periods and disposal procedures.
- When handling evidence that contains personal or confidential information, comply with applicable laws and privacy requirements, and collect or examine only the minimum needed for the purpose of the investigation.
- Identify in advance situations that require cooperation with external forensic specialists or law enforcement, prepare contracts/agreements and contact arrangements, and define procedures so the chain of custody is not broken at handover.

## Related controls and attributes
- ISO 27001 clauses: 8 (Operation), 9.1 (Monitoring, measurement, analysis and evaluation), 10.2 (Nonconformity and corrective action), 7.5 (Documented information)
- Adjacent Annex A: A.5.24 (Information security incident management planning and preparation), A.5.25 (Assessment and decision on information security events), A.5.26 (Response to information security incidents), A.5.27 (Learning from information security incidents), A.8.15 (Logging), A.8.16 (Monitoring activities)
- ISMS-P mapping: 2.11.5 Incident response and recovery (adjacent: 2.11.1 Establishing incident prevention and response system, 2.9.4 Log and access record management)
- 2013 mapping: 16.1.7 Collection of evidence

## Evidence
- Evidence collection/preservation procedures and the standard chain-of-custody record form
- Chain-of-custody records completed during actual incidents, evidence item lists, and sealing/unsealing records
- Forensic imaging logs and hash generation/verification records
- Evidence store access logs, retention management registers, and disposal records
- Cooperation contracts or agreements with forensic specialists/law enforcement and emergency contact arrangements
- Designation documents for evidence-handling personnel and related training records

## Nonconformity examples
- Evidence collection procedures are not documented, so during an incident staff collect evidence at their own discretion.
- The original disk is opened/analyzed directly, changing timestamps and compromising evidence integrity.
- No chain-of-custody record exists, so the handling history of the evidence cannot be traced and its validity cannot be demonstrated in legal or disciplinary proceedings.
- Hashes are not generated/verified, so the collected copy cannot be proven identical to the original.
- The evidence store has no access control, allowing many people to access the evidence without authorization.
- Evidence containing personal data is collected excessively without limits on purpose/scope, breaching privacy requirements.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
