# A.7.14 Secure disposal or re-use of equipment

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.7 Physical controls |
| Control | A.7.14 Secure disposal or re-use of equipment |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality |
| ISMS-P mapping | 2.9.7 Reuse and disposal of information assets (related: 2.10.7 Management of removable storage media, 2.4.6 Control of devices brought in and out) |
| 2013 mapping | A.11.2.7 |

## Control objective

The purpose is to deal with the fact that a machine stops being in use long before the data written to it stops existing. Equipment flagged for disposal or reassignment drops out of day-to-day oversight first, and from that point it passes through hands the organization no longer controls. The organization should decide deletion and destruction methods according to information sensitivity for every asset that can hold data (servers, PCs, laptops, portable storage, multifunction devices, network equipment), and verify and record the outcome. This prevents leakage of residual data during resale, lease return, repair outsourcing, or disposal, and at the same time avoids software licensing violations and gaps in asset management.

## Key checkpoints

1. Is a disposal and re-use procedure for equipment with storage media documented, with deletion and destruction methods differentiated by information sensitivity and media type (HDD/SSD/flash)?
2. After required retention checks, is data on equipment for reuse/disposal appropriately sanitized, software removed or transferred according to entitlements, and the outcome validated and recorded?
3. For media where simple deletion or partial overwriting does not fully erase data, such as SSD and flash, is a separate secure method applied (cryptographic erase, physical destruction)?
4. When disposal or destruction is outsourced, does the contract include security requirements and is proof of completion (a destruction certificate) obtained?
5. Is built-in storage in devices where storage is not obvious, such as multifunction devices, printers, network equipment, and IoT/OT devices, included in the scope of disposal and re-use?
6. After disposal or re-use processing, is the asset inventory updated so that asset status and disposal history stay current?

## Implementation guidance

- Select sanitization for sensitivity, media behavior, reuse/disposal plans, and anticipated recovery threats. Validate supported purge commands, cryptographic erase where prerequisites are met, or suitable physical destruction; overwrite pass count alone does not determine effectiveness.
- Ordinary deletion or overwriting may miss residual areas on SSD/eMMC/flash. Verify the coverage and success of device sanitization functions; if unsupported or unverifiable, choose another method or physical destruction appropriate to risk.
- For cryptographic erase, verify that target data was appropriately encrypted from the outset and that all relevant keys and recovery/escrow/backup copies can be removed. Treat plaintext copies on other media and copies encrypted under separate keys independently.
- After sanitization, assess execution and suitability using command results, media condition, and available verification. Record asset/media identifiers, method, operator, time, outcome, and verification limits; a certificate alone does not prove elimination of every recovery possibility.
- When disposal or destruction is outsourced, reflect security requirements in the contract and require control during transport and storage plus receipt of a destruction certificate (quantity, method, date).
- Include easily overlooked storage points such as the internal hard disk of multifunction devices and printers, configuration and credentials on network equipment, and returned leased devices in the disposal and re-use checklist.
- Reset equipment to a standard baseline before re-use (default settings, credentials removed, software cleaned up) and confirm transfer or removal of licensed software.
- After disposal is complete, reflect the status change (re-use or disposal) and supporting record in the asset inventory or management system so that asset records match reality.

## Related controls and attributes

- ISO 27001 clauses: 6.1 (Actions to address risks and opportunities), 8.1 (Operational planning and control), 7.5 (Documented information)
- Adjacent Annex A: A.7.10 (Storage media), A.7.9 (Security of assets off-premises), A.7.13 (Equipment maintenance), A.8.10 (Information deletion), A.5.9 (Inventory of information and other associated assets), A.5.11 (Return of assets)
- ISMS-P mapping: 2.9.7 Reuse and disposal of information assets (related: 2.10.7 Management of removable storage media, 2.4.6 Control of devices brought in and out)
- 2013 mapping: A.11.2.7 (Secure disposal or re-use of equipment)

## Evidence

- Equipment disposal and re-use procedure (deletion and destruction methods per media type, verification and recording criteria)
- Data deletion and destruction records (target asset, media serial number, method, operator, date and time, verification result)
- Records of secure erase, cryptographic erase, or physical destruction, with supporting evidence such as destruction photos or video
- Contract with security requirements and destruction certificates for outsourced work
- Checklist for handling built-in storage in multifunction devices, network equipment, and similar
- Asset inventory change history before and after disposal (status, disposal reason, date)

## Nonconformity examples

- Storage devices in PCs or servers due for disposal are only file-deleted or quick-formatted before the equipment is taken off site or sold, so data can be recovered.
- Only HDD-style overwriting is applied to SSD or flash media, so residual data is not actually erased.
- The internal hard disk of multifunction devices or printers is omitted from scope when the units are returned from lease or disposed of.
- Disposal is outsourced without obtaining a destruction certificate or processing evidence, so destruction cannot be proven.
- Reassigned equipment retains the previous user's accounts/credentials or software without a continuing right of use.
- There is no verification step after deletion or destruction and disposal history is not reflected in the asset inventory, so records do not match reality.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
