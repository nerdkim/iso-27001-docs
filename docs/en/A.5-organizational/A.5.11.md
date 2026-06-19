# A.5.11 Return of assets

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.11 Return of assets |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.2.5 Management of retirement and job change (related: 2.3.4 Security on change and termination of external party contracts, 2.1.3 Information asset management) |
| 2013 mapping | 8.1.4 Return of assets |

## Control objective

This control requires that personnel and external parties return all organizational assets they received or accessed for their work when their employment/contract/agreement changes or ends. When return is missed, information can be taken out without authorization, residual access can persist after departure or transfer, and assets can be lost, undermining the accuracy of the asset inventory. The scope of return covers not only physical devices such as laptops and mobile phones but also documents, removable media, authentication tokens, intellectual property, and the accounts/privileges controlled by the organization; where an asset cannot be physically returned, the associated information must be transferred, deleted, or its access blocked.

## Key checkpoints

1. Is the scope and list of assets to be returned defined in advance for retirement/job change/contract termination, so it can be reconciled one-to-one against the assets issued to each individual?
2. Is the asset return procedure linked to the HR/contract-termination process so it runs without omission, and are return confirmation records (signatures/confirmation forms) kept?
3. Are physical and logical access rights (access cards, accounts, VPN, remote access) revoked/disabled at the same time as return?
4. For assets that are hard to return (work information stored on personally owned devices, cloud accounts), are measures for information transfer/deletion/access blocking in place, and are the results verified?
5. Is intangible knowledge such as work know-how handed over and documented?
6. Is the risk of delayed or non-returnable assets assessed, and are compensating controls applied?

## Implementation guidance

- Register assets in the inventory at issuance and assign a custodian, so that at return the issued items can be reconciled to verify recovery.
- Include asset return items in the retirement/job-change/contract-expiry checklist, and clearly define the roles and processing order across HR, general affairs, security, and IT functions.
- Define, by asset type (laptops/mobiles/removable media/smart cards/tokens/keys/access cards/security documents), the return method and verification steps (wiping, confirmation of data deletion, inspection before reissue).
- For work information and personal data stored on personally owned devices (BYOD), recover it by remote wipe or selective wipe, then verify and record the result.
- On completion of return, immediately revoke/disable accounts, privileges, and access rights; for assets whose return is delayed or impossible, assess the risk and apply compensating controls such as access blocking and monitoring.
- Keep evidence such as return confirmation forms/signatures, and update the asset status (returned/disposed/reissued) in the inventory to keep it consistent with the actual holdings.

## Related controls and attributes

- ISO 27001 clauses: 7.5 (Documented information), 8.1 (Operational planning and control), 9.1 (Monitoring, measurement, analysis and evaluation)
- Adjacent Annex A: A.5.9 (Inventory of information and other associated assets), A.5.10 (Acceptable use of information and other associated assets), A.5.18 (Access rights), A.6.5 (Responsibilities after termination or change of employment), A.7.9 (Security of assets off-premises), A.8.1 (User endpoint devices)
- ISMS-P mapping: 2.2.5 Management of retirement and job change (related: 2.3.4 Security on change and termination of external party contracts, 2.1.3 Information asset management)
- 2013 mapping: 8.1.4 Return of assets

## Evidence

- Asset return procedure/guideline and retirement/job-change/contract-termination checklist
- Per-individual asset issuance/return ledger and return confirmation forms (signed)
- Records of account/privilege revocation (disable logs, access-right deletion records)
- Records of BYOD/mobile device remote wipe/selective wipe results
- Risk assessment and compensating control records for delayed/non-returnable assets
- Records of wiping/data deletion inspection performed on returned assets before reissue

## Nonconformity examples

- A laptop/storage media returned by a leaver is reissued or left unattended without wiping, so the previous user's information remains.
- A return procedure is documented, but no actual return confirmation records exist, so recovery of issued assets cannot be evidenced.
- The access card/account of an external party whose contract has ended is not revoked, so physical/logical access remains possible after termination.
- No deletion procedure exists for customer information/business materials stored on BYOD devices, so work information remains on personal devices after departure.
- On a job change, the privileges/tokens used for the previous role are not revoked, so unnecessary privileges accumulate.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
