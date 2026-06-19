# A.6.8 Information security event reporting

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.6 People controls |
| Control | A.6.8 Information security event reporting |
| Control type (ref.) | Detective / Corrective |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.11.1 Establishing an incident prevention and response system |
| 2013 mapping | A.16.1.2, A.16.1.3 |

## Control objective

This control establishes formal procedures and channels so that employees, external parties, and users can report observed or suspected information security events (anomalies, policy violations, discovered vulnerabilities, malfunctions) without undue delay. Most incidents begin at the point where a person first notices something unusual before it escalates into an actual breach, so early detection and a fast response are only possible when everyone knows what to report, when, and how. A further core purpose is to protect people who report in good faith from adverse consequences, thereby preventing concealment and under-reporting.

## Key checkpoints

1. Are formal reporting channels (hotline, email, ticket, portal) and a reporting procedure defined for information security events, and are employees/external parties aware of them?
2. Is guidance provided on what should be reported as an event, including types, examples, and decision criteria?
3. Are reporting deadlines (e.g. immediately on becoming aware, or within a set time) and the information to include (time of occurrence, affected asset, symptoms, actions taken) specified?
4. Is confidentiality and protection from retaliation for good-faith reporters guaranteed by policy?
5. Are received events routed into the incident assessment/classification/response procedure (A.5.24 onward), and is the outcome fed back to the reporter?
6. Are reporting channels and methods also provided for parties outside the organization, such as external parties, suppliers, and users?

## Implementation guidance

- Define and communicate the event types to be reported (suspected account compromise, malware detection, lost/stolen device, phishing received, access errors, signs of information leakage, discovered vulnerabilities) with concrete examples.
- Provide an easy-to-reach single reporting point (hotline, dedicated mailbox, intranet portal, ticketing system) and maintain a contact route for out-of-hours and emergency situations.
- Supply a minimum set of fields and a standard form so anyone can report simply and quickly.
- Establish a policy that protects good-faith reporters (confidentiality, no retaliation, anonymous reporting where needed) and make it known to all members.
- Route received events into the incident management procedure without delay so they connect to assessment/classification/response (A.5.24, A.5.25, A.5.26), and send an acknowledgement and outcome back to the reporter.
- Include reporting methods and examples in awareness training (A.6.3), and use exercises (such as phishing simulations) to verify that reporting actually works.
- State the reporting obligation and channels in external-party/supplier contracts and user guidance, so reporting is not limited to internal staff.

## Related controls and attributes

- ISO 27001 clauses: 7.3 (Awareness), 7.4 (Communication), 9.1 (Monitoring, measurement, analysis and evaluation), 10.2 (Nonconformity and corrective action)
- Adjacent Annex A: A.5.24 (Information security incident management planning and preparation), A.5.25 (Assessment and decision on information security events), A.5.26 (Response to information security incidents), A.5.27 (Learning from information security incidents), A.6.3 (Information security awareness, education and training), A.5.7 (Threat intelligence)
- ISMS-P mapping: 2.11.1 Establishing an incident prevention and response system (related: 2.2.4 Awareness and training, 2.11.5 Incident response and recovery)
- 2013 mapping: A.16.1.2 (Reporting information security events), A.16.1.3 (Reporting information security weaknesses)

## Evidence

- Information security event reporting procedure/guidance and reporting form
- Configuration of reporting channels (hotline, dedicated mailbox, portal, ticketing system) and the notice announcing them
- Event intake/handling log, ticket history, and records of routing into the incident management procedure
- Reporter-protection policy documents (confidentiality/no retaliation/anonymous reporting)
- Training materials on reporting methods for employees/external parties and completion records
- Results and improvement records of reporting exercises such as phishing simulations
- Acknowledgement and outcome feedback records sent to reporters

## Nonconformity examples

- Reporting channels exist but are not communicated to employees/external parties, so people do not actually know where or how to report.
- There are no event types, criteria, or examples for what should be reported, so the decision to report is left entirely to individual judgment.
- Even when events are reported, they are not routed into the assessment/classification/response procedure and are left unattended after intake.
- No reporter-protection policy exists, so fear of adverse consequences leads to concealment and under-reporting.
- No reporting channel is offered to external parties/suppliers/users, so events noticed outside the organization cannot be received.
- Reporting deadlines and required fields are not defined, so intake time and content are not recorded and the response is delayed.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
