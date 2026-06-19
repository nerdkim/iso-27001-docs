# A.5.15 Access control

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.15 Access control |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.5.1 User account management (related: 2.5.5 Privileged account and rights management, 2.5.6 Access rights review, 2.6.1 Network access, 2.6.2 Information system access) |
| 2013 mapping | 9.1.1, 9.1.2 |

## Control objective

This control requires the organization to establish and implement rules that grant or restrict physical and logical access to information and associated assets on the basis of business needs and information security requirements. The intent is to grant only the minimum rights required according to need-to-know and need-to-use, and to block unauthorized access, thereby reducing the risk of exposure, alteration, or damage of information and of service misuse. The organization should document an access control policy and apply access rules consistently in line with asset classification and risk level, managing access across users, systems, and network services.

## Key checkpoints

1. Is an access control policy (rules) documented on the basis of business and information security requirements, reflecting least privilege and segregation of duties?
2. Are access rules defined according to asset classification/criticality and user roles, covering both physical and logical access?
3. Is access to networks and network services restricted to the scope explicitly authorized for business needs?
4. Are the granting, modification, and revocation of access rights performed through an approval procedure and recorded?
5. Is the adequacy of access rules reviewed periodically and updated to reflect organizational and risk changes?
6. Is the access control policy communicated to relevant employees and external parties and applied consistently?

## Implementation guidance

- Document the access control policy and state its core principles, including need-to-know/need-to-use, least privilege, and consideration of segregation of duties.
- Define access rules according to asset classification level and risk assessment results, and choose an authorization model suited to the organization, such as role-based (RBAC) or attribute-based (ABAC).
- Manage physical access (protected areas/facilities) and logical access (systems/applications/databases/networks) consistently under one policy framework.
- Limit access to networks and network services to explicitly authorized scope, and set the baseline policy to deny by default.
- Define procedures for requesting, approving, granting, modifying, and revoking access rights, and designate the owner and required records for each step.
- Review access rights periodically to prevent excessive accumulation, and promptly adjust or revoke rights upon role change, resignation, or contract termination.
- Check the consistency between access rules and actual granted results (whether policy matches real configuration) and retain the history.

## Related controls and attributes

- ISO 27001 clauses: 5.3 (Roles, responsibilities and authorities), 6.1 (Actions to address risks and opportunities), 8.1 (Operational planning and control), 9.1 (Monitoring, measurement, analysis and evaluation)
- Adjacent Annex A: A.5.16 (Identity management), A.5.17 (Authentication information), A.5.18 (Access rights), A.8.2 (Privileged access rights), A.8.3 (Information access restriction), A.8.4 (Access to source code), A.8.5 (Secure authentication), A.7.1 (Physical security perimeters)
- ISMS-P mapping: 2.5.1 User account management (related: 2.5.5 Privileged account and rights management, 2.5.6 Access rights review, 2.6.1 Network access, 2.6.2 Information system access)
- 2013 mapping: 9.1.1 (Access control policy), 9.1.2 (Access to networks and network services)

## Evidence

- Access control policy/guideline documents (including principles, scope, and authorization model)
- Access rule definitions linked to asset classification/criticality (such as a role-based permission matrix)
- Records of requesting/approving/granting/modifying/revoking access rights
- Network and network service access approvals and configurations (firewall/access control lists, etc.)
- Results of periodic access rights reviews and records of resulting actions
- Records of access control policy communication/training

## Nonconformity examples

- No documented access control policy exists, or one exists but does not reflect core principles such as least privilege and segregation of duties.
- The same access rights are granted uniformly regardless of asset classification or risk level, leaving access uncontrolled.
- Network service access is open by default, allowing access beyond the scope authorized for business needs.
- Rights are granted, modified, or revoked arbitrarily without an approval procedure or records.
- Existing access rights are not revoked after a role change or resignation, so unnecessary rights remain.
- Access rights reviews are not performed, so the policy and the actual system configuration are inconsistent.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
