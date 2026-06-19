# A.5.20 Addressing information security within supplier agreements

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.20 Addressing information security within supplier agreements |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality, Integrity, Availability |
| ISMS-P mapping | 2.3.2 Security in external party contracts (related: 2.3.3 Managing external party security performance, 2.3.4 Security on external party contract change and termination) |
| 2013 mapping | A.15.1.2 |

## Control objective
When a supplier accesses, processes, stores, or transmits the organization's information or assets, or provides elements of the IT infrastructure, the corresponding information security requirements must be explicitly reflected in the contract or agreement and agreed with the supplier. This control aims to control supply chain risk in advance and to clarify each party's obligations and accountability by documenting security responsibilities, control levels, incident notification, audit rights, and termination actions from the contracting stage. The essence is to enforce, as contractual terms, requirements proportionate to the access scope and the sensitivity of the information, rather than relying on verbal agreements or informal practice.

## Key checkpoints
1. Are the information security requirements to be included in agreements defined according to supplier type, access level, and the sensitivity of the information handled?
2. Do the contract or the supplementary security agreement specify, in concrete terms, confidentiality, the scope of access rights, incident notification, audit/inspection rights, and control of subcontracting (further outsourcing)?
3. Are the security control levels and performance criteria the supplier must meet (policy/standard/SLA) linked to the contract and defined in a measurable way?
4. Are procedures for return/disposal of information, revocation of access rights, and return of assets on contract termination or cancellation stipulated in the agreement?
5. Are there clauses for action, remediation, and sanctions in case of a requirement change or a breach during contract performance?
6. For suppliers that process personal data or regulated information, are legal/regulatory requirements (outsourcing clauses, cross-border transfer, and similar) reflected in the contract?

## Implementation guidance
- Perform a per-supplier risk assessment before contracting, derive a list of security requirements proportionate to the access scope and information sensitivity, and reflect it in the contract terms.
- Prepare a standard contract template and a security schedule so that confidentiality, data handling, access control, encryption, log/monitoring, and vulnerability and patch management are stipulated consistently.
- Include a prior-approval procedure for subcontracting (further outsourcing) and a clause that flows down equivalent security obligations to sub-suppliers.
- Clearly define the incident notification deadline (for example, within 24 hours or 72 hours of becoming aware), the notification recipients/channels, and the obligation to cooperate in investigations.
- Specify audit/inspection rights, the obligation to submit evidence, the scope of accepted third-party certifications (for example, ISO 27001, SOC 2), and the conditions for re-audit.
- Include clauses for return/disposal evidence of data, revocation of accounts/access rights, return of assets, and surviving obligations (such as residual confidentiality) on contract termination or cancellation.
- When outsourcing the processing of personal data, reflect the processing purpose/scope, restrictions on further outsourcing, safeguards, and cross-border transfer conditions required by applicable law in the contract.

## Related controls and attributes
- ISO 27001 clauses: 4.2 (Needs and expectations of interested parties), 6.1 (Actions to address risks), 8.1 (Operational planning and control)
- Adjacent Annex A: A.5.19 Information security in supplier relationships, A.5.21 Managing information security in the ICT supply chain, A.5.22 Monitoring, review and change management of supplier services, A.5.23 Information security for use of cloud services
- ISMS-P mapping: 2.3.2 Security in external party contracts (related: 2.3.3 Managing external party security performance, 2.3.4 Security on external party contract change and termination)
- 2013 mapping: A.15.1.2

## Evidence
- Supplier contracts and supplementary security agreements (NDA, personal data processing outsourcing agreement, security schedule, and similar)
- Supplier security requirements definition/checklist
- Records of pre-contract risk assessment and supplier due diligence results
- SLA and security control level agreement documents
- Records of prior approval for subcontracting and notification history
- Data disposal/return confirmation and access rights revocation records at contract termination

## Nonconformity examples
- A contract with a supplier that processes sensitive information omits confidentiality and security requirement clauses.
- The contract has no incident notification deadline or procedure, delaying awareness and response to incidents on the supplier side.
- The supplier's subcontracting is done without prior approval, and security obligations are not flowed down to the sub-supplier.
- Supplier accounts and access rights are retained rather than revoked after contract termination.
- There is no audit/inspection right clause, so there is no way to confirm whether the supplier meets its security obligations.
- A personal data processing outsourcing agreement does not reflect the safeguards or restrictions on further outsourcing required by law.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
