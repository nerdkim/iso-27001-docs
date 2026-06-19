# A.7.13 Equipment maintenance

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.7 Physical controls |
| Control | A.7.13 Equipment maintenance |
| Control type (ref.) | Preventive, Corrective |
| Security properties (ref.) | Confidentiality, Integrity, Availability |
| ISMS-P mapping | 2.9.2 Performance and fault management (related: 2.4.4 Protection facility operation, 2.3.3 External party security compliance management) |
| 2013 mapping | 11.2.4 |

## Control objective
The purpose is to inspect and service equipment that stores, processes, or transmits information in line with the manufacturer's recommended specifications and the organization's operational needs, so as to prevent loss of information availability caused by malfunction, failure, or performance degradation. Maintenance covers both planned preventive servicing and repair or replacement after a fault, and it should be controlled so that only qualified and authorized personnel perform it. In particular, when servicing is carried out by external technicians, remotely, or by taking equipment off site for repair, stored information must be protected from exposure or alteration, so that confidentiality and integrity are assured alongside availability.

## Key checkpoints
1. Are maintenance targets, cycles, and owners defined and followed for each item, based on the asset inventory and the manufacturer's recommended specifications?
2. Is maintenance performed only by qualified and authorized personnel, and for external technicians are supervision, attendance, and limited access scope applied?
3. Are maintenance records (date and time, performer, actions taken, faults found, parts replaced) kept and retained?
4. For external servicing, remote maintenance, and off-site repair, are measures in place to prevent exposure or alteration of stored information (backup, data removal or encryption, confidentiality agreements, session logging)?
5. Are maintenance contract and SLA terms, warranty conditions, and relevant legal requirements (safety inspections for electrical, fire, and the like) defined and verified for compliance?
6. After maintenance, is the equipment rechecked to confirm normal operation and that security settings (permissions, patches, configuration) have not been degraded?

## Implementation guidance
- Define maintenance targets, preventive servicing cycles, and owners based on the asset inventory, and build the maintenance plan reflecting manufacturer specifications and operational criticality.
- Separate preventive servicing (periodic inspection, consumable and part replacement, firmware checks) from corrective servicing (fault response, repair, replacement), and set procedures and approval criteria for each.
- Restrict maintenance to qualified and authorized personnel, and for external technicians apply attendance and supervision, minimized access scope, and before-and-after checks.
- Before external servicing or off-site repair, back up and then remove sensitive information or detach the storage media; where this is unavoidable, protect it with encryption and a nondisclosure agreement (NDA).
- Apply prior approval, least-privilege accounts, encrypted connections, and session logging and monitoring to remote maintenance, and revoke access rights when the work ends.
- Include security requirements in maintenance contracts and SLAs (warranty scope, response time, information protection obligations, subcontracting controls), and review compliance periodically.
- After maintenance completes, verify that the equipment operates normally and that security configuration, patches, and access rights are intact, and record and retain the results and history.

## Related controls and attributes
- ISO 27001 clauses: 7.1 (resources), 8.1 (operational planning and control), 9.1 (monitoring and measurement)
- Adjacent Annex A: A.7.8 (Equipment siting and protection), A.7.10 (Storage media), A.7.11 (Supporting utilities), A.7.14 (Secure disposal or re-use of equipment), A.5.29 (Information security during disruption), A.8.14 (Redundancy of information processing facilities)
- ISMS-P mapping: 2.9.2 Performance and fault management (related: 2.4.4 Protection facility operation, 2.3.3 External party security compliance management)
- 2013 mapping: 11.2.4 (Equipment maintenance)

## Evidence
- Inventory of equipment subject to maintenance and the maintenance plan or schedule (including preventive servicing cycles)
- Maintenance logs, work orders, and inspection checklists (performer, actions taken, parts replaced)
- Maintenance contracts and SLAs, warranty documents, and nondisclosure agreements (NDAs) with external technicians
- Entry and attendance records for external technicians and approval records for access scope
- Approval records and session logs for remote maintenance
- Records confirming data backup and removal before off-site repair, and recheck records of normal operation and security settings after maintenance

## Nonconformity examples
- No maintenance cycle is defined for critical equipment, or preventive servicing is chronically delayed, leaving the risk of failure or performance degradation unmanaged.
- Maintenance history is not recorded, or actions taken and parts replaced are omitted, so servicing cannot be traced.
- External technicians access equipment without attendance or supervision, creating a risk that stored sensitive information is exposed.
- Equipment is taken off site for repair without backing up or removing data on the storage media, creating a risk of information leakage.
- Remote maintenance uses shared accounts or leaves sessions unlogged, so it is impossible to confirm who did what.
- Equipment whose warranty or SLA has expired is left in place without renewal or replacement, making timely recovery difficult when a fault occurs.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
