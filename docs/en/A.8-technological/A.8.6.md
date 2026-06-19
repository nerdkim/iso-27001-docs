# A.8.6 Capacity management

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.6 Capacity management |
| Control type (ref.) | Preventive / Detective |
| Security properties (ref.) | Availability |
| ISMS-P mapping | 2.9.2 Performance and fault management |
| 2013 mapping | A.12.1.3 |

## Control objective

This control requires the organization to monitor and tune the use of information processing resources (compute, memory, storage, network bandwidth, human resources, and so on) and to forecast future demand so that needed capacity is secured in time. The objective is to prevent performance degradation and service outages caused by resource exhaustion while avoiding wasteful over-provisioning, thereby sustaining service availability and continuity.

## Key checkpoints

1. Are the resources subject to capacity management (CPU, memory, storage, network bandwidth, and so on) and their performance metrics identified per key system/service, with baselines defined?
2. Is resource utilization monitored continuously, with warning/critical thresholds set so that alerts and responses occur when they are exceeded?
3. Is demand forecasting performed based on historical trends and business plans (new services, user growth, and so on), and is it linked to budget/procurement planning?
4. Are response options for capacity shortfalls (resource expansion, reclamation/optimization, load balancing, data cleanup, and so on) defined in advance?
5. In cloud/outsourced environments, are auto-scaling policies and cost controls (such as budget alerts) configured and operated together?

## Implementation guidance

- Define the resources and performance metrics (response time, throughput, utilization, and so on) to be managed per key service, and establish baselines for the normal state.
- Collect resource utilization in real time with monitoring tools, and operate an early-warning scheme using at least two threshold levels (warning/critical).
- Perform demand forecasting based on historical usage trends and business plans, and compare/adjust forecast against actuals on a regular cycle (for example, quarterly).
- Prepare response options for shortfalls in advance, including resource expansion, reclamation/optimization of unused resources, load balancing, and archiving/data cleanup.
- In cloud environments, set auto-scaling upper/lower bounds, a mix of reserved/on-demand resources, and budget alerts to manage availability and cost together.
- Link capacity planning with procurement lead times so that budget and orders are completed before the point at which expansion is needed.

## Related controls and attributes

- ISO 27001 clauses: 7.1 (Resources), 8.1 (Operational planning and control), 9.1 (Monitoring, measurement, analysis and evaluation)
- Adjacent Annex A: A.8.16 (Monitoring activities), A.8.14 (Redundancy of information processing facilities), A.5.30 (ICT readiness for business continuity), A.8.9 (Configuration management)
- ISMS-P mapping: 2.9.2 Performance and fault management
- 2013 mapping: A.12.1.3 (Capacity management)

## Evidence

- Capacity management policy/procedure and the list of managed resources/performance metrics
- Resource utilization monitoring dashboards/reports and threshold configuration records
- Capacity/demand forecast reports and periodic capacity review meeting minutes
- Resource expansion/adjustment history (change management records, order/procurement documents)
- Cloud auto-scaling and budget alert configuration screens
- Threshold-exceeded alerts and response action records

## Nonconformity examples

- Managed resources and thresholds are not defined, so utilization is not noticed until it reaches saturation.
- Log collection/backup halts due to insufficient storage, but with no early-warning scheme it is discovered only after the fact.
- No capacity sizing is performed when introducing a new service, causing performance degradation/outage right after launch.
- Cloud auto-scaling has no upper bound, so a traffic surge causes an outage, or conversely leads to excessive cost.
- Demand forecasting is performed but procurement lead time is not considered, so the timing of expansion does not match actual demand.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
