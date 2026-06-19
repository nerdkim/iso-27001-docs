# A.8.3 Information access restriction

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.3 Information access restriction |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity |
| ISMS-P mapping | 2.6.3 Application access |
| 2013 mapping | A.9.4.1 |

## Control objective

This control restricts access to information and application system functions in line with the access control policy, so that authorized users/processes reach only the data and functions they need for their work. By implementing least privilege and need-to-know at the system, application, and data layers, it aims to prevent unauthorized viewing, modification, and leakage.

## Key checkpoints

1. Is access to information and application system functions restricted according to the access control policy and per-duty authorization definitions (roles/menus/functions/data scope)?
2. Following least privilege and need-to-know, are the accessible data and functions separated per user/role?
3. Are unauthorized accesses blocked at the screen/menu/function/record/field level, and is the scope of viewing/output/download of results controlled?
4. Are sensitive functions (bulk queries, downloads, administrator menus, and so on) separately restricted/approved and logged?
5. Are applications configured to access back-end resources (databases/files/APIs) using least-privilege accounts?

## Implementation guidance

- Define a role-based (RBAC) or attribute-based (ABAC) authorization model from the access control policy, and document a permission matrix per menu/function/data.
- Verify authorization on the server side for every request, so protection does not rely on hidden/disabled UI elements alone (block bypass via direct URL/API calls).
- Apply limits to bulk output/download/copy of query results (count limits/masking/watermarking/approval).
- Use least-privilege service accounts for application-to-database connections instead of shared administrator accounts, and confine access to the required tables/views/procedures.
- Link grant/change/revoke procedures with periodic access rights review (A.5.18), and prevent risky privilege combinations through segregation of duties (A.5.3).
- Log authorization grant and denial events (A.8.15) and connect them to monitoring.

## Related controls and attributes

- ISO 27001 clauses: 8.1 (Operational planning and control), 6.1 (Actions to address risks), 9.1 (Monitoring, measurement, analysis and evaluation)
- Adjacent Annex A: A.5.15 (Access control), A.5.18 (Access rights), A.5.3 (Segregation of duties), A.8.2 (Privileged access rights), A.8.4 (Access to source code), A.8.5 (Secure authentication), A.8.18 (Use of privileged utility programs)
- ISMS-P mapping: 2.6.3 Application access (related: 2.6.2 Information system access, 2.6.4 Database access)
- 2013 mapping: A.9.4.1 (Information access restriction)

## Evidence

- Access control policy and per-role/per-duty permission matrix
- Application menu/function permission configuration screens and user-to-role mapping status
- Server-side authorization logic/configuration (for example, permission-check code, policy files)
- Bulk-query/download restriction and approval records
- Application-to-database service account grant records and access rights review results

## Nonconformity examples

- Menus are only hidden in the UI while server-side authorization is absent, so unauthorized functions/data can be reached via direct URL/API calls.
- Broad query/download permissions are granted by default regardless of duty, so least privilege is not upheld.
- The application connects with an over-privileged database administrator account and can access all tables.
- There is no restriction, approval, or logging for bulk queries/downloads of personal data.
- The permission matrix is not kept current, so actual granted permissions differ from defined ones.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
