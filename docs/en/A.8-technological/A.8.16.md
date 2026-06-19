# A.8.16 Monitoring activities

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.16 Monitoring activities |
| Control type (ref.) | Detective, Corrective |
| Security properties (ref.) | Confidentiality, Integrity, Availability |
| ISMS-P mapping | 2.11.3 Anomaly analysis and monitoring |
| 2013 mapping | New in 2022 |

## Control objective

This control requires networks, systems, and applications to be observed on an ongoing basis so that anomalous behavior, abnormal traffic, and unauthorized access attempts that deviate from a normal baseline are detected early, evaluated as potential information security incidents, and responded to promptly. The essence is not merely to keep logs but to analyze and correlate the collected data in real time or near real time to identify signs of compromise. The objective is to continuously tune detection rules and baselines so that both missed detections and excessive false positives are reduced, and to ensure the monitoring feeds into the incident response process.

## Key checkpoints

1. Are the monitoring targets (network, servers/OS, applications, security appliances, cloud, accounts/privileges, and so on) and the collected items defined on a risk basis?
2. Are a normal-state baseline and anomaly detection rules/thresholds defined, and are they updated periodically to reflect threat intelligence and incident history?
3. When an anomaly occurs, are alert generation, severity classification, and linkage (escalation) to the incident response process defined and operated?
4. Are people, tools (such as a SIEM), and responsibilities assigned to perform monitoring continuously (including whether 24x7 is required)?
5. Are the integrity and access control of the logs/alerts produced by monitoring themselves assured, and do they meet legal retention periods?
6. Are detection performance (false positives/false negatives) and alert handling times reviewed periodically to improve rules and baselines?

## Implementation guidance

- Define the monitoring targets and collected indicators (login failures, privilege escalation, abnormal traffic, bulk data exfiltration, configuration changes, and so on) based on asset criticality and threat scenarios.
- Establish a normal-behavior baseline, and design anomaly detection rules/thresholds and correlation rules, reflecting them in a SIEM or other security monitoring tools.
- Classify alerts by severity, and document the triage and escalation flow that leads to owner assignment, investigation, and the incident response process.
- Tune detection rules and baselines periodically using external threat intelligence and past incident/false-positive results to reduce both false negatives and false positives.
- Apply access control, time synchronization, and retention periods so that monitoring logs and alert data cannot be altered or deleted without authorization.
- For high-criticality environments, consider a 24x7 monitoring capability or linkage with an external managed monitoring service, and establish means to gain visibility over blind spots (encrypted traffic, cloud/SaaS, and so on).

## Related controls and attributes

- ISO 27001 clauses: 9.1 (Monitoring, measurement, analysis and evaluation), 8.1 (Operational planning and control), 6.1 (Actions to address risks and opportunities)
- Adjacent Annex A: A.8.15 (Logging), A.8.17 (Clock synchronization), A.5.7 (Threat intelligence), A.5.25 (Assessment and decision on information security events), A.8.20 (Networks security), A.8.6 (Capacity management)
- ISMS-P mapping: 2.11.3 Anomaly analysis and monitoring (related: 2.9.5 Review of logs and access records, 2.10.1 Operation of security systems)
- 2013 mapping: New in 2022

## Evidence

- Monitoring policy/procedure (defining targets, collected items, baseline, alert criteria, and responsibilities)
- SIEM/monitoring tool configuration and the list of detection rules/correlation rules
- Alert generation and handling history (triage results, escalation records)
- Monitoring dashboards/operations reports (daily/weekly reports, and so on)
- History of detection-rule tuning and baseline updates, and false-positive/false-negative review records
- Access-rights list for monitoring logs and evidence of retention/integrity settings

## Nonconformity examples

- Logs are collected but left unattended without real-time/periodic analysis, so signs of compromise are not detected.
- Anomaly detection rules/baselines are never updated after initial setup, so they fail to reflect new attacks or environmental changes.
- A high volume of alerts is generated but, with no severity classification/handling procedure, genuine threat alerts are buried among false positives.
- New environments such as cloud/SaaS and remote work are omitted from the monitoring scope, creating visibility blind spots.
- Escalation from an alert into the incident response process is not defined, so the response is delayed.
- Monitoring logs/alert data have no access control, so an administrator or an attacker can delete traces at will.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
