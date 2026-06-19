# A.7.12 Cabling security

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.7 Physical controls |
| Control | A.7.12 Cabling security |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality, Integrity, Availability |
| ISMS-P mapping | 2.4.3 Information system protection (related: 2.4.4 Protection facility operation, 2.10.5 Information transfer security) |
| 2013 mapping | 11.2.3 |

## Control objective
The purpose is to protect power and telecommunications cabling that carries data or supports information services from interception, interference, and physical damage. The organization should keep power supply and data transmission continuous and reduce the risk of signal interception, electromagnetic interference, and cable cutting or damage along cabling runs. In doing so it prevents service interruption from cable damage (availability), interception of information in transit (confidentiality), and data tampering or unauthorized device connection through manipulation of the cabling (integrity).

## Key checkpoints
1. Are power and telecommunications/data cables routed along paths with low risk of physical damage, interception, and interference (cable ducts, underground conduits, protective trays)?
2. Are power and telecommunications lines routed separately to prevent signal errors or damage from electromagnetic interference (EMI)?
3. Is physical access controlled to wiring rooms (MDF/IDF), frames, patch panels, and cable junction points?
4. Are cables, ports, and patch panels labeled and is the cabling diagram kept current to prevent miswiring and unauthorized connection?
5. Are additional protections such as shielded cable, fiber optics, conduit locking, and electromagnetic shielding applied to segments carrying sensitive information?
6. Are unused cables and ports removed or disabled rather than left in place, and is the attachment of unauthorized tapping devices checked?

## Implementation guidance
- Route power and telecommunications/data cables through underground conduits, inside walls, or in protective trays and ducts wherever possible to reduce physical damage and exposure to unauthorized access.
- Separate power and telecommunications lines by adequate clearance or use metal conduit or shielded cable to prevent electromagnetic interference.
- Apply locks and access control to wiring rooms (MDF/IDF), frames, patch panels, and junction boxes, and keep records of access.
- Label all cables, ports, and patch panels and keep the cabling diagram current to prevent miswiring and unauthorized change, updating the diagram immediately whenever changes occur.
- Apply strengthened protection such as shielded (STP) cable, fiber optics, locked conduit, and electromagnetic shielding to segments requiring high confidentiality, and perform cable scanning or tap detection where needed.
- Remove or physically and logically disable unused cables and network ports, and confirm through periodic inspection that no unauthorized junction points or tapping devices are attached.
- Provide redundancy for critical segments over physically separate alternate cabling routes so a single cable fault does not cause a full service outage.

## Related controls and attributes
- ISO 27001 clauses: 6.1 (actions to address risks and opportunities), 8.1 (operational planning and control), 7.5 (documented information)
- Adjacent Annex A: A.7.8 (Equipment siting and protection), A.7.11 (Supporting utilities), A.7.13 (Equipment maintenance), A.7.5 (Protecting against physical and environmental threats), A.8.20 (Networks security), A.8.21 (Security of network services)
- ISMS-P mapping: 2.4.3 Information system protection (related: 2.4.4 Protection facility operation, 2.10.5 Information transfer security)
- 2013 mapping: 11.2.3 (Cabling security)

## Evidence
- Cabling diagram, and labeling and management register for cables, ports, and patch panels
- Status of access control and locking for wiring rooms (MDF/IDF) and frames, and access records
- Records of power/telecommunications line separation and shielding/conduit application (photos, installation and inspection records)
- Records of removal or disabling of unused cables and ports
- Cable inspection and tap detection records and follow-up actions
- Configuration and test records for cabling redundancy (alternate routes) on critical segments

## Nonconformity examples
- Telecommunications or power cables are exposed on floors, ceilings, or corridors without protection, leaving them vulnerable to physical damage or unauthorized access.
- Power and telecommunications lines run adjacent to each other, causing signal degradation or errors from electromagnetic interference.
- Wiring rooms or frames are left open without locks, so anyone can reach cable junction points.
- Cables and ports are unlabeled and the cabling diagram is outdated and inconsistent with the actual wiring, so miswiring or unauthorized connection cannot be identified.
- Unused network ports or cables remain active, allowing unauthorized device connection or attachment of tapping devices.
- Critical circuits are routed over a single path only, so a cable cut or damage causes a full service outage.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
