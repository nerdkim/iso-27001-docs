# A.5.24 Information security incident management planning and preparation

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.24 Information security incident management planning and preparation |
| Control type (ref.) | Preventive/Corrective |
| Security properties (ref.) | Confidentiality, Integrity, Availability |
| ISMS-P mapping | 2.11.1 Establishing incident prevention and response system |
| 2013 mapping | 16.1.1 |

## Control objective
This control requires the organization to define, before any incident actually occurs, the roles, responsibilities, processes, and resources needed to detect, report, assess, respond to, recover from, and follow up on information security incidents. Its purpose is to enable a fast and consistent response that minimizes damage and spread, and to systematically feed lessons learned back into the process to prevent recurrence. Without advance preparation, decision-making stalls during an incident, evidence is easily compromised, and legal or regulatory notification duties are missed.

## Key checkpoints
1. Are the definition, types, and severity classification criteria for information security incidents documented and shared across the organization?
2. Are the response organization (owner, response team, role holders), a standing emergency contact chain, and an escalation path designated?
3. Is the handling process defined step by step, from detection through reporting, assessment, response, recovery, closure, and post-incident review?
4. Are channels and methods for personnel and external parties to promptly report incident indicators established and communicated?
5. Do the procedures cover legal or regulatory notification duties (supervisory authorities, data subjects, etc.), notification deadlines, and external communication criteria?
6. Are the resources needed for response (tools, logs, budget, contracts with external specialists) secured in advance?

## Implementation guidance
- Establish an incident response policy and procedure, and define criteria for distinguishing an event from an incident together with a severity rating table.
- Designate an incident response owner and a response team (e.g., CSIRT), and document roles and responsibilities (RACI), authority, escalation paths, and the emergency contact list, keeping them current.
- Prepare response playbooks and first-action checklists by incident type (malware infection, data breach, denial of service, account compromise, personal data breach, etc.).
- Define in advance the notification requirements and deadlines for authorities, law enforcement, and data subjects, along with the spokesperson, external communication channel, and internal reporting criteria.
- Ensure integration with log collection and monitoring (A.8.15, A.8.16), evidence collection (A.5.28), and contact with external bodies (A.5.5, A.5.6), and provision the tools and resources needed for response.
- Validate the plan's effectiveness through exercises, and revise the procedures periodically to reflect exercise and real incident results.

## Related controls and attributes
- ISO 27001 clauses: 5.3 (roles, responsibilities, and authorities), 7.5 (documented information), 9.1 (monitoring and measurement), 10.1/10.2 (nonconformity and corrective action, continual improvement)
- Adjacent Annex A: A.5.25 (Assessment and decision on information security events), A.5.26 (Response to information security incidents), A.5.27 (Learning from information security incidents), A.5.28 (Collection of evidence), A.5.5 (Contact with authorities), A.5.6 (Contact with special interest groups), A.6.8 (Information security event reporting), A.8.15 (Logging), A.8.16 (Monitoring activities)
- ISMS-P mapping: 2.11.1 (Establishing incident prevention and response system), related 2.11.4 (Incident response drills and improvement), 2.11.5 (Incident response and recovery)
- 2013 mapping: 16.1.1 (Responsibilities and procedures for information security incident management)

## Evidence
- Information security incident response policy/procedure, incident type and severity classification criteria
- Incident response organization chart, roles and responsibilities (RACI), emergency contact list, escalation scheme
- Response playbooks by incident type, first-action checklists, reporting channel guidance
- Summary table of legal or regulatory notification requirements and deadlines, external communication guidelines
- Exercise plans and result reports, procedure revision history
- Contracts or cooperation arrangements with external specialists (forensics, legal, etc.)

## Nonconformity examples
- An incident response procedure document exists, but roles/responsibilities and the emergency contact list are not kept current, so the actual responsible person cannot be identified.
- No criteria distinguish events from incidents and no severity ratings exist, so the timing of reporting and escalation depends on the individual handler's discretion.
- No reporting channel is provided, so personnel who notice incident indicators do not know where or how to report them.
- Legal notification duties and deadlines (e.g., for personal data breaches) are not reflected in the procedure, creating a risk of delayed notification.
- No exercise has ever been conducted after the plan was established, so the effectiveness of the procedures has not been validated.
- The logs, tools, and external-body contact arrangements needed for response were not secured in advance, delaying first response during an incident.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
