# A.5.23 Information security for use of cloud services

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.23 Information security for use of cloud services |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality/Integrity/Availability |
| ISMS-P mapping | 2.10.2 Cloud security |
| 2013 mapping | New in 2022 |

## Control objective
This control defines and enforces the organization's security requirements across the full lifecycle of cloud services: acquisition, use, migration, and exit. Because cloud operates under a shared responsibility model that splits control points between the provider and the customer, the essential task is to carry out every security responsibility that falls to the customer through contracts, configuration, and monitoring. The aim is to govern unapproved cloud use and to securely recover or destroy data on exit or migration, so that cloud risk stays within the organization's management scope.

## Key checkpoints
1. Are security requirements and usage criteria defined and subject to an approval process before adopting a cloud service?
2. Is the boundary of security responsibility between provider and customer documented per service type (IaaS/PaaS/SaaS) under the shared responsibility model?
3. Are security baselines for cloud accounts and configuration (privileges, network, encryption, logging) established and their compliance reviewed?
4. Is the provider's security level (certifications, SLA, incident notification, data storage location) assessed before contracting and reflected in the agreement?
5. Are procedures for data recovery/destruction and account/privilege revocation in place for service termination or migration?

## Implementation guidance
- Establish a cloud adoption/use policy and operate a process to identify and block unapproved cloud (shadow IT) use.
- Produce a shared responsibility matrix per service type that clarifies customer-owned items such as account management, data encryption, network controls, and log collection.
- Define cloud configuration security baselines and periodically check for risky configurations such as exposed public storage, excessive privileges, and unencrypted data.
- Specify data storage location/cross-border transfer, incident notification deadlines, audit rights, and data return/destruction on termination in the contract and SLA.
- Apply multi-factor authentication and least privilege to cloud administrator accounts, and log and monitor administrative actions.
- Prepare an exit plan in advance to manage data portability and vendor lock-in risk.

## Related controls and attributes
- ISO 27001 clauses: 6.1 Risk assessment and treatment, 8.1 Operational planning and control
- Adjacent Annex A: A.5.19 Information security in supplier relationships, A.5.20 Addressing information security within supplier agreements, A.5.21 Managing information security in the ICT supply chain, A.5.22 Monitoring, review and change management of supplier services
- ISMS-P mapping: 2.10.2 Cloud security
- 2013 mapping: New in 2022

## Evidence
- Cloud adoption/use policy and adoption approval records
- Shared responsibility matrix per service type
- Cloud contract/SLA (including data storage location, incident notification, exit clauses)
- Cloud configuration review reports and remediation records for risky configurations
- Cloud administrator account privilege/MFA settings and access logs
- Data return/destruction confirmation on service termination or migration

## Nonconformity examples
- A team adopts a SaaS to store customer data without approval, and it is omitted from the organization's management scope.
- Misunderstanding the shared responsibility model, the customer assumes the provider performs data encryption/access control that are in fact the customer's responsibility.
- Cloud storage is configured as public and exposed to the internet.
- The contract lacks clauses on data storage location and destruction on termination, leaving no clear basis for transfer or disposal.
- The cloud management console account has no MFA applied and no access logs are collected for administrative actions.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
