# A.7.10 Storage media

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.7 Physical controls |
| Control | A.7.10 Storage media |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.10.7 Management of removable storage media (related: 2.9.7 Reuse and disposal of information assets, 2.4.6 Control of devices brought in and out) |
| 2013 mapping | 8.3.1, 8.3.2, 8.3.3, 11.2.5 |

## Control objective

This control requires that information held on storage media be protected against unauthorized disclosure, alteration, loss, or recovery across the full media life cycle: acquisition, registration, use, storage, transfer, transport, re-use, and disposal. The scope covers removable media such as USB drives, external hard disks, optical discs, and backup tapes, as well as fixed media embedded in servers and endpoints. Because physical transport and disposal easily fall outside routine controls and carry high risk of loss, theft, or recovery of residual data, the organization should define a protection level commensurate with the media type and the sensitivity of the stored information, and keep verifiable records of how media are handled and destroyed.

## Key checkpoints

1. Are procedures and responsibilities defined for the acquisition, registration, use, storage, and disposal of storage media, and are media identified and managed as assets?
2. Is the use of removable media restricted to the minimum necessary, so that only approved and registered media may be used?
3. When media are moved in/out or physically transported off-site, are protections applied such as encryption, tamper-evident sealing/packaging, and handover records?
4. Before re-use or disposal, is an unrecoverable sanitization/destruction method appropriate to the media type applied, and is the result recorded (for example, on a certificate)?
5. Is the storage environment for media holding sensitive information managed (physical access control, temperature/humidity, migration ahead of media ageing)?
6. Is protection at the point of storage, such as encryption, applied to important/personal data on media so that exposure is prevented if the media are lost?

## Implementation guidance

- Define classification criteria and handling rules by media type (removable/fixed/optical/tape/SSD), and apply labelling and asset-register entries so that location and status can be tracked.
- Restrict removable media use by default, issue media only after approval/registration when there is a genuine business need, and encrypt stored information so that loss or theft does not expose data.
- For off-site transport, use trusted carriers, tamper-evident sealing/packaging, handover and receipt-confirmation records, and in-transit encryption, and retain the transport history.
- For re-use, reset previous data so that it cannot be recovered (multi-pass overwriting, cryptographic erase, etc.); for disposal, perform physical destruction/perforation/degaussing/incineration suited to the media type.
- Use verifiable, standard methods for sanitization/destruction and record the date, target media, method, responsible person, and result on a certificate; where outsourced, obtain the processing evidence and the contract.
- For media with unreliable overwrite behaviour such as SSD/flash, encrypt from the point of storage and dispose by key destruction (cryptographic erase) or combine with physical destruction; do not rely on degaussing alone.

## Related controls and attributes

- ISO 27001 clauses: 6.1 (Actions to address risks and opportunities), 7.5 (Documented information), 8.1 (Operational planning and control)
- Adjacent Annex A: A.7.9 (Security of assets off-premises), A.7.14 (Secure disposal or re-use of equipment), A.8.10 (Information deletion), A.8.12 (Data leakage prevention), A.5.9 (Inventory of information and other associated assets), A.5.10 (Acceptable use of information and other associated assets), A.5.14 (Information transfer)
- ISMS-P mapping: 2.10.7 Management of removable storage media (related: 2.9.7 Reuse and disposal of information assets, 2.4.6 Control of devices brought in and out)
- 2013 mapping: 8.3.1 (Management of removable media), 8.3.2 (Disposal of media), 8.3.3 (Physical media transfer), 11.2.5 (Removal of assets)

## Evidence

- Storage media management procedure/guideline (type classification, handling/storage/disposal criteria)
- Removable media asset register/registration log and media in/out log
- Media disposal/sanitization certificates and destruction certificates (with contract and processing-result report where outsourced)
- Handover/receipt-confirmation records and sealing/tracking history for off-site transport
- Media encryption status and policy/solution configuration screens
- Media storage-environment (access control, temperature/humidity) management records

## Nonconformity examples

- No control policy exists for removable media, so staff freely use personal USB drives for work.
- Hard disks scheduled for disposal are handed to a recycling vendor after only a quick format, leaving data in a recoverable state.
- No disposal/sanitization certificate is retained, so whether and how media were destroyed cannot be tracked or verified.
- Media holding sensitive information are shipped off-site by ordinary courier without encryption, leaving exposure risk unaddressed if lost.
- SSDs are processed by degaussing only, so the data is not actually erased before re-use or disposal.
- Removable media are not identified or registered as assets, so their location and holdings cannot be established.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
