# A.8.14 Redundancy of information processing facilities

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.14 Redundancy of information processing facilities |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Availability |
| ISMS-P mapping | 2.9.2 Performance and failure management |
| 2013 mapping | 17.2.1 Availability of information processing facilities |

## Control objective

This control requires that information processing facilities (servers, storage, network equipment, power, communication links, data centers) be implemented with redundancy sufficient to meet the availability requirements of the services they support, so the failure of a single component does not cause a service outage. It calls for defining the availability target of each critical business service, duplicating components accordingly, and regularly verifying that automatic/manual failover actually works. Redundancy is not merely adding hardware: it must remove single points of failure (SPOF) and be designed and tested so that switchover procedures and spare capacity can carry the real load.

## Key checkpoints

1. Are availability requirements (target availability, RTO) defined per critical service, and is the redundancy scope based on them?
2. Have single points of failure across servers, storage, network, power, and links been identified and removed/mitigated?
3. Are the redundancy scheme (active/active, active/standby, clustering, load balancing) and the failover procedure documented?
4. Is failover/failback tested regularly to confirm it actually works, and are the results fed back into improvement?
5. Has capacity been sized and verified so the redundant configuration can carry both normal and failure-time load?
6. Are the status, synchronization, and switchover events of redundant components monitored, with alerts on anomalies?

## Implementation guidance

- Assign an availability tier to each service based on business impact analysis, and design the redundancy level (component, site, data center) to match the tier.
- Remove SPOFs layer by layer: servers (cluster/HA), storage (RAID/replication), network (redundant paths and devices), power (UPS/generator/dual feed), and links (diverse carriers/redundant routes).
- Choose synchronous or asynchronous data replication to meet the RPO requirement, and design so data consistency is preserved after switchover.
- Document automatic failover triggers/thresholds, the manual switchover procedure, and the failback procedure, and clarify responsible roles.
- Run periodic failure-injection/switchover tests, measuring switchover time, data loss, and performance degradation, and improve based on the results.
- Combine geographically distributed redundancy (for wide-area disasters) with local redundancy according to risk and cost, and include physical infrastructure (power/cooling/links) in the review.
- Monitor health checks, replication lag, and switchover events of redundant components, and periodically check configuration/firmware version consistency.

## Related controls and attributes

- ISO 27001 clauses: 6.1 (Actions to address risks and opportunities), 8.1 (Operational planning and control), 9.1 (Monitoring, measurement, analysis and evaluation)
- Adjacent Annex A: A.5.29 (Information security during disruption), A.5.30 (ICT readiness for business continuity), A.8.6 (Capacity management), A.8.13 (Information backup), A.7.11 (Supporting utilities), A.7.12 (Cabling security)
- ISMS-P mapping: 2.9.2 Performance and failure management (linked: 2.12.1 Safety measures for disaster/emergency preparedness, 2.9.3 Backup and recovery management)
- 2013 mapping: 17.2.1 Availability of information processing facilities

## Evidence

- Per-service availability requirements and redundancy design (including architecture diagrams)
- SPOF analysis/removal records and infrastructure diagrams (server/storage/network/power/link)
- Failover/failback procedures and role definitions
- Redundancy switchover test plans/result reports (including switchover time and data-loss measurement)
- Data replication settings and replication-lag/consistency check records
- Redundancy status monitoring dashboards/alert settings and event logs
- Capacity sizing basis and load-test results

## Nonconformity examples

- Only some equipment is made redundant without defined availability requirements, while other layers such as power/links remain single, leaving SPOFs.
- Redundancy is configured but failover has never been tested, so switchover fails during a real incident.
- The standby node lacks capacity/performance, so the service cannot be processed normally after switchover.
- Replication lag is not managed, causing data loss/inconsistency after switchover.
- Redundant components run different configuration/firmware versions, causing malfunction at switchover.
- There is no monitoring/alerting on redundancy status, so a degraded state (one side already failed) goes unnoticed.
- Redundancy exists only within the same data center/same power feed, so a wide-area disaster brings everything down at once.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
