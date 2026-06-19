# A.8.15 Logging

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.15 Logging |
| Control type (ref.) | Detective |
| Security properties (ref.) | Confidentiality, Integrity, Availability |
| ISMS-P mapping | 2.9.4 Log and access record management |
| 2013 mapping | A.12.4.1 / A.12.4.2 / A.12.4.3 (Event logging / Protection of log information / Administrator and operator logs) |

## Control objective

Logging requires that events arising from information systems, applications, network/security devices, and user activity be recorded so that the evidence and accountability needed to detect, investigate, and respond to security incidents are available. Because logs underpin the identification of anomalous behavior, root-cause analysis of incidents, and compliance with legal/regulatory requirements, the organization must define clearly what is recorded, at what level of detail, and for how long it is kept. Logs themselves can be a target for tampering, deletion, or unauthorized viewing, so the objective extends beyond producing records to protecting the integrity and confidentiality of the logs.

## Key checkpoints

1. Are the systems in scope for logging and the event types to record (login, privilege change, data access, configuration change, error, and so on), together with the level of detail, defined in a logging policy/procedure?
2. Is each log configured to include the mandatory fields (event timestamp, subject identifier, target, action, success/failure result, source, and so on)?
3. Are protective measures such as access control, tamper prevention, encryption, and central collection applied to preserve the integrity and confidentiality of logs?
4. Is the log retention period defined in line with legal/regulatory/internal requirements, and are logs stored without loss for that period?
5. Are the activities of privileged/administrator accounts logged separately, with separation of duties/controls so that a log administrator cannot conceal their own actions?
6. Is there a procedure to detect and respond to conditions that undermine logging reliability, such as collection failures, storage exhaustion, and unsynchronized time?

## Implementation guidance

- Select the systems, event types, and level of detail in scope for logging based on asset criticality and risk assessment results, and document them in a logging policy/standard.
- Include in each log at least the event timestamp (based on a synchronized time source), the user/process identifier, the event type, the target of access, the success/failure result, and the source address.
- Forward logs to a remote central store (log server/SIEM) so that original records survive even if an individual system is compromised, and encrypt the transmission path.
- Minimize read/write permissions on logs and either block deletion/modification or make integrity verifiable through append-only storage, hashing, or digital signatures.
- Apply masking/filtering so that personal data or authentication data (passwords, tokens, resident registration numbers, and so on) are not left in logs in plaintext.
- Define log rotation, retention, archiving, and disposal rules, and continuously monitor storage capacity and collection status.
- Keep privileged/administrator activity logs separate from ordinary user logs, and separate the log-management role from the system-operations role so that mutual oversight is possible.

## Related controls and attributes

- ISO 27001 clauses: 8.1 (Operational planning and control), 9.1 (Monitoring, measurement, analysis and evaluation)
- Adjacent Annex A: A.8.16 (Monitoring activities), A.8.17 (Clock synchronization), A.5.28 (Collection of evidence), A.8.6 (Capacity management), A.5.33 (Protection of records)
- ISMS-P mapping: 2.9.4 Log and access record management (review under 2.9.5, time synchronization under 2.9.6)
- 2013 mapping: A.12.4.1 / A.12.4.2 / A.12.4.3

## Evidence

- Logging policy/standard (systems in scope, events recorded, mandatory fields, retention periods defined)
- Log configuration screens or configuration files for key systems/security devices, plus samples of actually collected logs
- Central log store (SIEM/log server) architecture diagram and log forwarding/collection status
- Log access-permission list and evidence of integrity protection (hashing/signatures/append-only)
- Log retention and disposal history, and monitoring records for storage capacity/collection status
- Privileged/administrator activity logs and evidence of separation of duties for log management

## Nonconformity examples

- Logging is disabled on key servers/security devices, or critical events (privilege changes, access failures, and so on) are not recorded.
- Clocks are not synchronized across systems, making log correlation and time-based tracing impossible during an incident.
- Administrators can arbitrarily delete/modify logs on individual servers, so log integrity is not assured.
- The log retention period falls short of a legal requirement (for example, a mandatory access-record retention period) or logs are deleted prematurely.
- Sensitive information such as passwords or resident registration numbers is recorded in logs in plaintext.
- A collection failure or storage exhaustion goes undetected, leaving logs missing for a considerable period without anyone noticing.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
