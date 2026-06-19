# A.5.3 Segregation of duties

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.3 Segregation of duties |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.2.2 Segregation of duties |
| 2013 mapping | A.6.1.2 |

## Control objective

This control separates conflicting duties and areas of responsibility so that no single person can carry a sensitive process end to end and then conceal it alone. When activities that should check one another, such as requesting, approving, executing, and reviewing, are concentrated in one individual, there is nothing left to catch fraud, error, or misuse of privileges. The control requires the organization to identify high-risk combinations of duties and separate them, and where the organization is too small for full separation, to put compensating controls in place so the checking function is preserved.

## Key checkpoints

1. Are conflicting duties and responsibilities (request/approve/execute/review, development/operations, asset registration/disposal approval, and so on) identified, with the separation criteria documented?
2. Are the identified conflicts reflected in actual privilege granting and work assignment so that one person cannot run the whole process without a check?
3. Are additional controls applied to high-risk combinations such as privileged account management, security policy configuration, and log management?
4. Where full segregation is impractical because of organization size or staffing limits, are compensating controls (activity monitoring, dual approval, independent log review) defined and operated?
5. Are segregation breaches (conflicting privileges, concentration of authority from combined roles) reviewed periodically and corrected when found?

## Implementation guidance

- Define the activities that should check one another, such as request/approve/execute/review, development/operations, and change request/change approval, in a segregation-of-duties (SoD) matrix, stating which privilege combinations must not be held together.
- Grant only the privileges each duty needs under the least-privilege principle, and add a verification step to the grant/revoke procedure so conflicting privileges do not accumulate in one account or person.
- Separate high-risk areas such as development and operations, or operations and security audit, and control privileged account use by splitting the requester, approver, and executor.
- Where combined roles are unavoidable due to limited staff, design compensating controls (senior approval, dual control, independent review of activity logs) to substitute for the checking function.
- Use IAM/entitlement tools to detect conflicting privilege combinations automatically, and check for SoD breaches as part of periodic access-rights reviews.
- Re-examine the segregation criteria and reallocate privileges on reorganization, personnel movement, and introduction of new systems.

## Related controls and attributes

- ISO 27001 clauses: 5.3 (Organizational roles, responsibilities and authorities), 6.1 (Actions to address risks and opportunities), 8.1 (Operational planning and control)
- Adjacent Annex A: A.5.2 (Information security roles and responsibilities), A.5.15 (Access control), A.5.18 (Access rights), A.8.2 (Privileged access rights), A.8.3 (Information access restriction)
- ISMS-P mapping: 2.2.2 Segregation of duties
- 2013 mapping: A.6.1.2 (Segregation of duties)

## Evidence

- Segregation-of-duties (SoD) matrix or a policy/regulation defining the separation criteria
- Privilege-grant register per duty, with grant/approval records
- Access-rights review results and SoD breach check records
- Records of combined-role operation and compensating controls (dual approval logs, independent log review records)
- Organization chart, job descriptions, and documentation of development/operations separation

## Nonconformity examples

- One person requests, approves, grants, and reviews access rights, so no mutual check operates.
- Developers access and change production systems/databases directly, with no separation between development and operations.
- No matrix or criteria identify conflicting duties, so there is no basis to judge which privilege combinations are risky.
- In a small organization where combined roles are unavoidable, operations run without compensating controls such as dual approval or independent log review.
- Access-rights reviews are performed only as a formality, so conflicting privileges accumulated in one individual are not detected or corrected.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
