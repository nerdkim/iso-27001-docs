# A.5.9 Inventory of information and other associated assets

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.9 Inventory of information and other associated assets |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 1.2.1 Identification of information assets (related: 2.1.3 Information asset management, 1.1.4 Scope definition) |
| 2013 mapping | 8.1.1 Inventory of assets (related: 8.1.2 Ownership of assets) |

## Control objective

This control requires the organization to identify, without omission, the information assets it must protect together with the other assets that process, store, or transmit them, and to keep this inventory accurate and current. If the organization does not know what it holds, where those assets are, and who is accountable for them, there is no basis for any downstream protection activity such as risk assessment, access control, or incident response. The aim is therefore to secure foundational data for the whole information security management system by requiring asset identification, assignment of owners, and maintenance of an accurate inventory.

## Key checkpoints

1. Are criteria and a procedure defined for identifying information assets and other associated assets (hardware, software, services, facilities, people)?
2. Are identified assets managed in an inventory, with each asset recording the necessary attributes such as owner, location, type, and criticality?
3. Is the inventory updated in a timely manner when lifecycle changes occur, such as acquisition, change, or disposal of assets?
4. Does the inventory match the scope of the management system and reflect the actual operating environment without omissions or duplicates?
5. Is the accuracy of the inventory reviewed/reconciled periodically, and are the results linked to risk assessment and safeguards?

## Implementation guidance

- Identify, by type, information assets (documents, databases, files, personal data) and the associated assets that support them (hardware such as servers and endpoints, application/system software, cloud and external services, networks, facilities, people).
- For each asset, define and record the attributes needed for management, such as a unique identifier, name, type, location (physical/logical), owner and custodian, criticality/classification level, and acquisition/disposal dates.
- Assign an owner (accountable party) to every asset to make responsibility clear for asset classification, access approval, and inventory accuracy.
- Link lifecycle events such as acquisition, transfer, change, and disposal to change management/procurement procedures so that the inventory is updated automatically or manually.
- Use tools such as a CMDB, an asset management system, and network asset discovery to improve inventory accuracy and currency and to compensate for omissions from manual handling.
- Use the inventory as the reference data for risk assessment, asset classification (A.5.12), access control, incident response, and disposal, and confirm through periodic reconciliation that it matches the actual environment.

## Related controls and attributes

- ISO 27001 clauses: 4.3 (Determining the scope of the management system), 6.1 (Actions to address risks), 8.1 (Operational planning and control)
- Adjacent Annex A: A.5.10 (Acceptable use of information and other associated assets), A.5.11 (Return of assets), A.5.12 (Classification of information), A.5.13 (Labelling of information), A.7.9 (Security of assets off-premises), A.8.1 (User endpoint devices)
- ISMS-P mapping: 1.2.1 Identification of information assets (related: 2.1.3 Information asset management, 1.1.4 Scope definition)
- 2013 mapping: 8.1.1 Inventory of assets (related: 8.1.2 Ownership of assets)

## Evidence

- Asset identification criteria and asset management procedure (including owner assignment, update cycle, and reconciliation method)
- Inventory of information assets and other associated assets (with attributes such as identifier, type, location, owner, criticality)
- History of asset acquisition/change/disposal and records of linkage with change management
- Results of periodic inventory reconciliation/review and records of actions taken on discrepancies
- Evidence of linkage between the inventory and the results of risk assessment/asset classification

## Nonconformity examples

- An inventory exists, but a recently acquired server or cloud service is missing, so it does not match the actual operating environment.
- No owner or custodian is assigned to assets, so accountability for classification, access approval, and inventory updates is unclear.
- Disposed or returned assets are not cleared from the inventory, so nonexistent assets remain under management.
- The inventory lacks criticality/classification levels, so it cannot serve as the basis for prioritizing risk assessment and safeguards.
- The inventory is not updated after its initial creation and no periodic reconciliation is performed, so currency is not maintained.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
