# A.7.8 Equipment siting and protection

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.7 Physical controls |
| Control | A.7.8 Equipment siting and protection |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality, Integrity, Availability |
| ISMS-P mapping | 2.4.3 Information system protection (related: 2.4.4 Protection facility operation, 2.10.6 Business device security) |
| 2013 mapping | 11.2.1 |

## Control objective
The purpose is to place equipment that stores, processes, or transmits information in locations with low exposure to physical and environmental threats and to unauthorized access or damage, and to apply protection commensurate with each location. The organization should decide siting for servers, network devices, endpoints, and output based on each item's importance and exposure, reducing threats such as water, dust, vibration, temperature and humidity, electromagnetic interference, and line of sight. In doing so it prevents loss of availability from equipment damage or malfunction, information exposure such as shoulder surfing of screens and printouts, and integrity compromise through physical access.

## Key checkpoints
1. Are critical items such as servers and network devices sited where unauthorized access, line-of-sight exposure, and environmental threats are low (dedicated areas, racks, lockable cabinets)?
2. Are criteria defined and applied at siting to reduce environmental threats such as water, dust, vibration, temperature and humidity, power anomalies, and electromagnetic interference?
3. Are screens and printouts that handle or display sensitive information positioned or shielded so they are not visible to unauthorized people?
4. Are physical protection measures in place for endpoints, printers, and network ports located in open offices, common areas, or exposed positions?
5. Is there a rule that restricts actions that could damage equipment or expose information, such as handling food and drink, smoking, or unauthorized photography?
6. Is there a procedure to keep the level of protection intact when equipment is moved, relocated, or disposed of?

## Implementation guidance
- Classify siting tiers by equipment importance and the sensitivity of the information handled, and place critical items in access-controlled dedicated areas or locked racks and cabinets.
- Choose locations that lower environmental threats such as water, dust, vibration, rapid temperature and humidity change, power surge, and electromagnetic interference, and apply shielding, dust and water protection, and threshold monitoring where needed.
- Position screens that display sensitive information away from lines of sight toward doors, windows, and corridors, or block shoulder surfing with privacy filters or partitions.
- Keep printers and multifunction devices in access-controlled areas and apply secure print (release after user authentication) to prevent exposure from unattended output.
- Restrict unauthorized connection or movement of endpoints, unused network ports, and console ports in common or open areas through physical locks, port disabling, and cable fixing.
- Restrict actions that could damage equipment or expose information inside processing areas, such as handling food and drink, smoking, or unauthorized photography, and make users aware of the rules.
- Establish approval and record procedures so the same protection criteria are maintained during movement, relocation, transfer, or disposal, and recheck the protection state after any change of location.

## Related controls and attributes
- ISO 27001 clauses: 6.1 (actions to address risks and opportunities), 8.1 (operational planning and control), 9.1 (monitoring and measurement)
- Adjacent Annex A: A.7.5 (Protecting against physical and environmental threats), A.7.7 (Clear desk and clear screen), A.7.10 (Storage media), A.7.11 (Supporting utilities), A.7.12 (Cabling security), A.7.13 (Equipment maintenance), A.8.1 (User endpoint devices)
- ISMS-P mapping: 2.4.3 Information system protection (related: 2.4.4 Protection facility operation, 2.10.6 Business device security)
- 2013 mapping: 11.2.1 (Equipment siting and protection)

## Evidence
- Equipment siting criteria or policy (importance tiers, environmental threat mitigation criteria, line-of-sight blocking criteria)
- Equipment layout plans for server rooms and offices, and a list of critical equipment
- Status of physical protection measures such as rack and cabinet locking, port disabling, and cable fixing
- Records of exposure-prevention measures such as secure print and screen shielding
- Rules and notices restricting actions inside processing areas (food, photography, and the like)
- Approval records for equipment movement, relocation, transfer, or disposal, and recheck records after location changes

## Nonconformity examples
- Servers or network devices sit in unlocked open spaces or common corridors, so anyone can access them physically.
- Screens displaying sensitive information face doors, windows, or corridors, so unauthorized people can easily shoulder surf.
- Printers and multifunction devices lack secure print, so printouts are left unattended and can be collected by third parties.
- Critical equipment is placed in high-threat spots such as under piping, by windows, or in vibration- and dust-prone locations, with no mitigation applied.
- Unused network or console ports in common areas remain active, allowing unauthorized connection.
- After equipment is moved or relocated, no recheck confirms that protection criteria (locking, line-of-sight blocking) are still in place.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
