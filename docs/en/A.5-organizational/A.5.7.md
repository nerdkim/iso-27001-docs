# A.5.7 Threat intelligence

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.7 Threat intelligence |
| Control type (ref.) | Preventive / Detective / Corrective |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.11.1 Establishment of incident prevention and response system (related: 2.11.3 Anomaly analysis and monitoring, 2.11.2 Vulnerability assessment and remediation) |
| 2013 mapping | New in 2022 |

## Control objective

This control requires the organization to collect, analyze, and use information about information security threats that may target it, so that the threat landscape is understood and addressed proactively. It calls for keeping current on attacker tactics/techniques/procedures (TTPs), targets, motivations, exploited vulnerabilities, and indicators of compromise (IOCs), and feeding that knowledge into risk assessment, detection/blocking rules, and the prioritization of safeguards. The aim is to shorten the time to recognize and respond to emerging threats and to keep defenses continuously aligned with the actual threat situation.

## Key checkpoints

1. Are internal and external sources and a collection procedure defined for threat information relevant to the organization?
2. Is collected threat information analyzed at strategic, tactical, and operational levels, with source reliability and organizational relevance evaluated?
3. Are analysis results reflected in real safeguards, such as risk assessment, detection rules, blocking policies, and vulnerability remediation priorities?
4. Is threat information shared in a timely manner with relevant functions and stakeholders, such as incident response and monitoring teams?
5. Are roles and responsibilities for threat intelligence assigned, and is the effectiveness of the activity reviewed and improved periodically?

## Implementation guidance

- Identify internal sources (logs, incident history, vulnerability assessment results) and external sources (CERTs/response bodies, industry information sharing communities, security vendors, open-source feeds) and select them according to purpose.
- Analyze threat information by level: strategic (long-term threat trends), tactical (attacker TTPs), and operational (immediately usable indicators such as IOCs).
- Evaluate source reliability, timeliness, and organizational relevance to filter out false positives and noise, and assign priorities.
- Turn analysis into defense by feeding it into detection/blocking rules in SIEM/IPS/firewalls, risk assessment updates, and vulnerability remediation priorities.
- Structure threat information in standard formats (for example, STIX/TAXII) and participate in trust-based sharing communities to enable two-way use of information.
- Assign roles and responsibilities for the threat intelligence process and document how outputs are used and fed back, so that the activity does not rely on the capability of a single individual.

## Related controls and attributes

- ISO 27001 clauses: 6.1 (Actions to address risks), 9.1 (Monitoring, measurement, analysis and evaluation), 10.2 (Nonconformity and continual improvement)
- Adjacent Annex A: A.5.5 (Contact with authorities), A.5.6 (Contact with special interest groups), A.8.8 (Management of technical vulnerabilities), A.8.16 (Monitoring activities), A.5.24 to A.5.27 (Information security incident management)
- ISMS-P mapping: 2.11.1 Establishment of incident prevention and response system (related: 2.11.3 Anomaly analysis and monitoring, 2.11.2 Vulnerability assessment and remediation)
- 2013 mapping: New in 2022

## Evidence

- Threat intelligence collection/analysis procedure and role/responsibility definition document
- List of threat information sources and status of subscriptions/contracts/community participation
- Periodic threat intelligence reports (strategic/tactical/operational levels)
- Records of threat information applied (detection rule change history, blocked IOC lists, risk assessment update records)
- Records of threat information sharing (internal distribution history, sends/receives with external sharing communities)

## Nonconformity examples

- Threat information is only collected, with no analysis or use procedure, so it is never reflected in safeguards or detection rules.
- Threat information collection and analysis rely solely on one individual's capability, with no documented sources or procedures, so the work is not reproducible.
- External threat feeds are subscribed to but applied as-is without evaluating organizational relevance or reliability, causing a large volume of false positives.
- Information about an actively exploited new vulnerability is obtained but is not reflected in vulnerability remediation priorities.
- Threat intelligence results are not shared with the incident response/monitoring teams, so they cannot be used for actual detection and response.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
