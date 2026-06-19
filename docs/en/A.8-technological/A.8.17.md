# A.8.17 Clock synchronization

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.17 Clock synchronization |
| Control type (ref.) | Detective |
| Security properties (ref.) | Integrity |
| ISMS-P mapping | 2.9.6 Time synchronization |
| 2013 mapping | A.12.4.4 (Clock synchronization) |

## Control objective

This control requires that the clocks of all in-scope information systems and network devices be synchronized to a single, trustworthy reference time source, so that timestamps in logs across systems are consistent and directly comparable. Accurate and aligned time is essential for cross-system log correlation, incident investigation, forensic reliability, and preserving the integrity of legal evidence. When device clocks drift apart, the sequence of events becomes difficult to reconstruct and collected logs may lose their evidentiary value.

## Key checkpoints

1. Is a trustworthy reference time source designated (for example, an internal NTP server synchronized to a reliable external reference such as national standard time) and is a synchronization policy established?
2. Are all in-scope assets (servers, network/security devices, endpoints, applications, cloud resources) synchronized to the reference source and configured with a consistent time zone/UTC baseline?
3. Is synchronization status monitored, and are clock drift, synchronization failures, and anomalies detected and remediated?
4. Is the time source protected against tampering/spoofing (for example, restricting which sources may be queried, and NTP authentication)?
5. Do logs record consistent and accurate time that can be used for cross-system correlation?

## Implementation guidance

- Design a hierarchical time distribution architecture with internal NTP server(s) synchronized to a reliable external reference (national time authority, GPS, and so on), and have all systems point to the internal servers.
- Standardize on UTC or a single defined time zone as the baseline, and document the policy including the allowed drift tolerance and synchronization interval.
- Configure servers, network devices, security appliances, endpoints, containers, and cloud resources to synchronize automatically, and for cloud make appropriate use of the provider's time service.
- Protect the time source: restrict which sources devices may query, use authenticated NTP where supported, place time servers in protected segments, and monitor for spoofing.
- Continuously monitor synchronization health (offset/drift alerts), remediate devices that fall out of sync, and provide time source redundancy for availability.
- Verify that logging subsystems apply the synchronized time, and reconcile the time baseline in log correlation/SIEM so that event ordering is consistent.

## Related controls and attributes

- ISO 27001 clauses: 8.1 (Operational planning and control), 9.1 (Monitoring, measurement, analysis and evaluation)
- Adjacent Annex A: A.8.15 (Logging), A.8.16 (Monitoring activities), A.5.28 (Collection of evidence), A.8.20 (Networks security), A.8.21 (Security of network services)
- ISMS-P mapping: 2.9.6 Time synchronization (related: 2.9.4 Log and access record management, 2.9.5 Log and access record review, 2.11.3 Anomaly analysis and monitoring)
- 2013 mapping: A.12.4.4 (Clock synchronization)

## Evidence

- Clock synchronization policy/standard (reference source, time baseline, synchronization interval, allowed drift)
- NTP architecture diagram and time server configuration values
- Synchronization configuration captures on servers/network/security devices/endpoints
- Synchronization status monitoring/alert records and drift remediation history
- Log samples showing consistent time across systems
- Access control/authentication settings for the time source

## Nonconformity examples

- Systems are set to inconsistent time zones or local times with no common baseline, making log correlation impossible.
- Some devices (network/security appliances, legacy servers) are not synchronized and are left with significant clock drift.
- The internal time server itself is not synchronized to a reliable external reference, or it is a single point with no redundancy.
- Synchronization status is not monitored, so drift/failures go unnoticed for extended periods.
- The time source is open to arbitrary external NTP with no restriction/authentication, exposing it to spoofing.
- Log timestamps are inaccurate, weakening incident investigation and the admissibility of evidence.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
