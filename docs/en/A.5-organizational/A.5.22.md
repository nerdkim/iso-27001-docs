# A.5.22 Monitoring, review and change management of supplier services

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.22 Monitoring, review and change management of supplier services |
| Control type (ref.) | Preventive, Detective |
| Security properties (ref.) | Confidentiality, Integrity, Availability |
| ISMS-P mapping | 2.3.3 External party security implementation management |
| 2013 mapping | 15.2.1 Monitoring and review of supplier services, 15.2.2 Managing changes to supplier services |

## Control objective
This control ensures that suppliers deliver services in line with contractual and agreed security requirements throughout the life of the relationship, and that any change to a supplier's services is managed in a controlled way. Even when a security level is agreed at contract signing, the service scope, personnel, sub-suppliers, and technical configuration change over time, and so does the risk, which is why ongoing verification and change handling are needed. The aim is to prevent security degradation and incidents propagating through the supply chain, and to detect and act on problems early when they arise.

## Key checkpoints
1. Is there a defined procedure and cadence for regularly monitoring and reviewing each supplier's compliance with contractual and agreed security requirements?
2. Is actual performance assessed against the SLA and security requirements using evidence such as service reports, audit results, and incident history?
3. When a supplier changes its services or its sub-suppliers (subcontracting), is the organization notified in advance and is the risk re-assessed?
4. Are deficiencies found during review or monitoring managed through improvement requests, corrective actions, and re-verification, all kept as records?
5. Are supplier-related security incidents and vulnerabilities reported to the organization and handled according to contractual response requirements?

## Implementation guidance
- Classify suppliers by service criticality and risk level, and apply differentiated monitoring/review cadence and methods per tier (periodic meetings, performance reporting, on-site inspection, third-party certificate review).
- State security performance indicators, reporting obligations, the right to audit, change-notification duties, and sub-supplier approval conditions in contracts and SLAs, and use them as review criteria.
- Regularly collect and validate supplier-provided service reports, independent audit results, penetration test/vulnerability assessment results, and certificates (for example, ISO 27001, SOC 2).
- Require advance notice of changes to supplier services (scope, personnel, location, network/technical configuration, sub-suppliers), re-assess the impact on the organization's risk, and adjust controls accordingly.
- Manage deficiencies identified in monitoring/review as improvement plans (corrective action, owner, deadline), and close them only after re-verifying that the action was implemented.
- Agree notification and response procedures for supplier-related incidents/vulnerabilities in advance, and handle them in conjunction with the organization's incident response process when they occur.
- Where subcontracting occurs, verify that equivalent security requirements are cascaded to and met by the sub-suppliers.

## Related controls and attributes
- ISO 27001 clauses: 8.1 (Operational planning and control), 9.1 (Monitoring, measurement, analysis and evaluation), 9.3 (Management review), 10.1 (Continual improvement)
- Adjacent Annex A: A.5.19 (Information security in supplier relationships), A.5.20 (Addressing information security within supplier agreements), A.5.21 (Managing information security in the ICT supply chain), A.5.23 (Information security for use of cloud services), A.6.6 (Confidentiality or non-disclosure agreements)
- ISMS-P mapping: 2.3.3 External party security implementation management (adjacent: 2.3.4 Security on external party contract change and termination, 2.3.2 Security in external party contracts, 2.9.1 Change management)
- 2013 mapping: 15.2.1 Monitoring and review of supplier services, 15.2.2 Managing changes to supplier services

## Evidence
- Supplier management (monitoring/review/change) policy and procedures, and supplier tiering criteria
- Per-supplier periodic review/inspection plans and results (minutes, performance reports, checklists)
- Supplier-submitted service reports, independent audit results, vulnerability/penetration test results, and valid certificates
- Assessments of SLA and security-requirement compliance, deficiency improvement plans, and evidence of completed actions
- Supplier service change notifications, and records of the resulting risk re-assessment and control adjustments
- History of supplier-related security incident/vulnerability notifications and handling, and sub-supplier (subcontracting) approval and management records

## Nonconformity examples
- Security requirements are agreed only at contract signing, with no periodic monitoring or review of compliance thereafter.
- A supplier adds sub-suppliers (subcontracting) or changes the service configuration without notifying the organization and without any risk re-assessment.
- SLA/security performance reports are not obtained from the supplier, or are received but merely filed without review or verification.
- Deficiencies are identified during review, but no improvement request, corrective action, or re-verification is recorded, so closure cannot be confirmed.
- Security incidents on the supplier side are not reported to the organization, or contractual response requirements are not defined.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
