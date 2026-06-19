# A.5.32 Intellectual property rights

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.32 Intellectual property rights |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality, Integrity, Availability |
| ISMS-P mapping | 1.4.1 Review of compliance with legal requirements |
| 2013 mapping | 18.1.2 Intellectual property rights |

## Control objective
This control ensures that the organization uses intellectual property (copyright, software licenses, patents, trademarks, trade secrets, source code, design documents, datasets, and similar) lawfully, and that it also protects its own intellectual property. The aim is to prevent legal disputes, damages, fines, and reputational harm arising from unauthorized copying, exceeding or breaching license terms, or installing illegal software. To achieve this, the organization must know the licenses and ownership of the software and materials it uses, and put procedures and controls in place so that contractual terms and applicable laws are met across acquisition, use, distribution, and disposal.

## Key checkpoints
1. Are procedures and responsibilities defined for identifying and managing assets subject to intellectual property rights (software, copyrighted works, data) and their license terms?
2. Is there a periodic check that the number of licensed copies held matches the number of copies actually installed and used for the software in use?
3. Are preventive controls in place (restricting install privileges, awareness) to stop employees and external parties from installing unauthorized/illegal software or copying works without permission?
4. Is proof of license (purchase/contract/certificate) and proof of ownership retained, and are license expiry, renewal, and reclamation managed?
5. Are the usage terms of open source, third-party materials, and materials obtained from public networks reviewed and complied with?
6. Is the ownership and right to use the organization's own intellectual property (source code, design documents, brand) protected through contracts and policy?

## Implementation guidance
- Establish an intellectual property rights management policy that states the scope (commercial software, open source, copyrighted works such as fonts/images/documents, datasets, patents/trademarks, in-house deliverables) and the compliance principles.
- Operate a software asset management (SAM) capability that records licenses held, installation status, and usage in a register, and periodically reconcile (comparing installed counts against licensed counts).
- Control software installation privileges on workstations/servers, and use asset scanning/inventory tools to detect and remove unauthorized or illegal software.
- When using open source, review the license type (GPL, MIT, Apache, etc.) and its obligations (attribution, source disclosure, usage restrictions), and where needed use an SBOM and an open source review process to check for license conflicts in distributed deliverables.
- Securely retain license agreements, purchase records, certificates, and proof of ownership, and track expiry/renewal/reassignment (including reclaiming licenses on termination and role change).
- Communicate the prohibition of unauthorized copying and illegal installation, and the consequences of violation, through awareness training, security undertakings, and contract clauses, and secure ownership of the organization's own intellectual property and confidentiality obligations by contract.

## Related controls and attributes
- ISO 27001 clauses: 4.2 (Understanding the needs and expectations of interested parties), 7.5 (Documented information), 8.1 (Operational planning and control)
- Adjacent Annex A: A.5.31 (Legal, statutory, regulatory and contractual requirements), A.5.33 (Protection of records), A.5.9 (Inventory of information and other associated assets), A.5.10 (Acceptable use of information and other associated assets), A.8.19 (Installation of software on operational systems)
- ISMS-P mapping: 1.4.1 Review of compliance with legal requirements (adjacent: 2.10.6 Security of business-use terminal devices, 2.8.5 Source program management, 2.1.3 Information asset management)
- 2013 mapping: 18.1.2 Intellectual property rights

## Evidence
- Intellectual property rights and software license management policy/procedures
- Software asset register (licenses held, installation status, usage) and periodic reconciliation/audit results
- License agreements, purchase records, certificates, and expiry/renewal management records
- Results of unauthorized/illegal software detection (asset scanning/inventory) and remediation records
- Open source usage review sheets, SBOM, and evidence of meeting license obligations (attribution notices, etc.)
- IPR awareness training materials/undertakings, and intellectual property ownership and confidentiality clauses in contracts

## Nonconformity examples
- There is no software license register, or the number of copies actually installed exceeds the number of licenses held.
- There is no control over install privileges on workstations, so employees can freely install illegal or unauthorized software.
- Software continues to be used after license expiry without renewal, or licenses assigned to leavers are not reclaimed or reassigned.
- Open source is adopted/distributed without reviewing its license terms (attribution, source disclosure, etc.), breaching the obligations.
- Fonts/images/documents obtained from public networks are used commercially without checking the usage terms.
- Ownership of outsourced development deliverables and source code is not stated in the contract, leaving the intellectual property rights unclear.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
