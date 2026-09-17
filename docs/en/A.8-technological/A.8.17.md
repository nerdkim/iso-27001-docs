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

This control manages in-scope systems and network devices against a trustworthy common time basis. Multiple approved sources may be used, with accuracy, availability, and consistency considered together. Distinguishing timestamp time zones from clock error supports reliable event ordering and correlation. Monitor synchronization and preserve relevant offset information to support incident investigation and evidence interpretation.

## Key checkpoints

1. Is a trustworthy reference time source designated (for example, an internal NTP server synchronized to a reliable external reference such as national standard time) and is a synchronization policy established?
2. Do servers, devices, endpoints, applications, and cloud resources use an approved common time basis, with UTC or explicit time-zone offsets in logs?
3. Is synchronization status monitored, and are clock drift, synchronization failures, and anomalies detected and remediated?
4. Is the time source protected against tampering/spoofing (for example, restricting which sources may be queried, and NTP authentication)?
5. Do logs record consistent and accurate time that can be used for cross-system correlation?

## Implementation guidance

- Approve internal time servers, trusted external references, or provider time services appropriate to the environment and define distribution arrangements. Verify consistent baselines and tolerances across sources and assess dependence on a single server.
- Make records comparable through UTC or explicit time-zone offsets, and define clock-error tolerances and synchronization policy. Different time-zone representations do not necessarily mean different clock times; distinguish format conversion from clock-error correction during analysis.
- Configure servers, network/security devices, endpoints, and virtual machines for suitable time services. For containers sharing the host clock, verify host synchronization and application time representation instead of requiring NTP in each container. Verify provider capabilities for managed cloud services.
- Protect the time source: restrict which sources devices may query, use authenticated NTP where supported, place time servers in protected segments, and monitor for spoofing.
- Continuously monitor synchronization health (offset/drift alerts), remediate devices that fall out of sync, and provide time source redundancy for availability.
- Verify that logging layers record system time correctly and handle time zones and known clock offsets in the SIEM. Retain original timestamps and conversion/correction records so analysis remains traceable.

## Related controls and attributes

- ISO 27001 clauses: 8.1 (Operational planning and control), 9.1 (Monitoring, measurement, analysis and evaluation)
- Adjacent Annex A: A.8.15 (Logging), A.8.16 (Monitoring activities), A.5.28 (Collection of evidence), A.8.20 (Networks security), A.8.21 (Security of network services)
- ISMS-P mapping: 2.9.6 Time synchronization (related: 2.9.4 Log and access record management, 2.9.5 Review of logs and access records, 2.11.3 Anomaly analysis and monitoring)
- 2013 mapping: A.12.4.4 (Clock synchronization)

## Evidence

- Clock synchronization policy/standard (reference source, time baseline, synchronization interval, allowed drift)
- NTP architecture diagram and time server configuration values
- Synchronization configuration captures on servers/network/security devices/endpoints
- Synchronization status monitoring/alert records and drift remediation history
- Log samples showing consistent time across systems
- Access control/authentication settings for the time source

## Nonconformity examples

- Missing time-zone/offset information or an unclear time basis prevents reliable comparison of log timestamps.
- Some devices (network/security appliances, legacy servers) are not synchronized and are left with significant clock drift.
- The internal time server itself is not synchronized to a reliable external reference, or it is a single point with no redundancy.
- Synchronization status is not monitored, so drift/failures go unnoticed for extended periods.
- Devices or internal time servers are configured to reference arbitrary external NTP with no restriction or authentication, exposing them to time source spoofing.
- Log timestamps are inaccurate, weakening incident investigation and the admissibility of evidence.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
