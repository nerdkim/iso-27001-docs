# A.7.5 Protecting against physical and environmental threats

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.7 Physical controls |
| Control | A.7.5 Protecting against physical and environmental threats |
| Control type (ref.) | Preventive / Detective |
| Security properties (ref.) | Confidentiality, Integrity, Availability |
| ISMS-P mapping | 2.4.4 Operation of protective facilities (related: 2.12.1 Safety measures for disaster preparedness, 2.4.1 Designation of protected areas) |
| 2013 mapping | 11.1.4 |

## Control objective

This control protects premises and information processing facilities against natural and man-made threats such as fire, flooding, earthquake, lightning, power failure, explosion, and civil unrest. The organization should identify the threats relevant to each site from its geographic location, surroundings, and history of past incidents, and then design and operate preventive and mitigating facilities and procedures proportionate to the assessed threat level. The aim is to reduce the risk of information loss, equipment damage, and service disruption caused by physical or environmental events, and to establish a basis for limiting impact and recovering quickly when an event does occur.

## Key checkpoints

1. Are physical and environmental threats identified for each site with regard to geographic location and surroundings (rivers, adjacent hazardous facilities, traffic, flooding history, etc.)?
2. For each identified threat (fire, flooding, earthquake, power failure, lightning, etc.), are preventive and mitigating facilities in place proportionate to the risk level?
3. Are environmental protection facilities such as fire detection and suppression, water-leak detection, temperature/humidity control, and UPS/emergency power inspected and tested regularly to confirm they operate correctly?
4. Are critical facility areas such as server rooms and data centers sited or reinforced to avoid locations vulnerable to flooding, fire spread, or external impact (lowest basement level, beneath plumbing, adjacent to outer walls, etc.)?
5. Are procedures and responsibilities defined for alerting, initial response, notification of authorities, and escalation to responsible staff when a physical or environmental event occurs?
6. Are threats arising from adjacent premises or external factors (nearby construction, hazardous material storage, leaks from upper floors, etc.) identified and addressed?

## Implementation guidance

- Survey each site for geographic/environmental characteristics and history of past incidents, list the relevant physical and environmental threats, and set treatment priorities based on the risk assessment.
- Against fire, apply detectors, automatic suppression suited to IT equipment (for example gas-based systems), extinguishers, fire compartmentation, and fire-resistant materials, and test their operation periodically.
- Against flooding and leaks, install leak-detection sensors, drainage, and water barriers, and review siting so critical facilities are not placed in the lowest level, beneath plumbing, or against outer walls.
- Against power failure or anomalies, provide UPS and emergency generation, periodically check and test capacity, runtime, and fuel reserves, and apply surge protection and grounding.
- Operate HVAC/precision cooling for temperature and humidity control with alarms on threshold breaches, and in seismic areas apply earthquake reinforcement such as securing racks and equipment.
- Link detection and alarm facilities to continuous monitoring and notification so events are recognized early, and document and rehearse initial-response and authority-notification procedures.
- Periodically reassess threats from external factors such as adjacent premises, nearby construction, and handling of hazardous materials, and update mitigations, drawing on advice from specialists or authorities where needed.

## Related controls and attributes

- ISO 27001 clauses: 6.1 (actions to address risks and opportunities), 8.1 (operational planning and control), 9.1 (monitoring, measurement, analysis and evaluation), 10.1 (continual improvement)
- Adjacent Annex A: A.7.1 (Physical security perimeters), A.7.4 (Physical security monitoring), A.7.8 (Equipment siting and protection), A.7.11 (Supporting utilities), A.7.12 (Cabling security), A.5.29 (Information security during disruption), A.5.30 (ICT readiness for business continuity)
- ISMS-P mapping: 2.4.4 Operation of protective facilities (related: 2.12.1 Safety measures for disaster preparedness, 2.4.1 Designation of protected areas)
- 2013 mapping: 11.1.4 (Protecting against external and environmental threats)

## Evidence

- Physical and environmental threat identification and risk assessment results per site
- Inventory and layout of protection facilities such as fire detection/suppression, leak detection, precision cooling, and UPS/emergency power
- Plans and records of periodic inspection and operational testing of protection facilities
- Environmental monitoring (temperature/humidity, leak, power) records and alarm history
- Physical/environmental event response procedures and documentation of the authority-notification and escalation scheme
- Records of threat reviews for adjacent premises and external factors, and of advice from specialists or authorities

## Nonconformity examples

- The server room sits in the building's lowest level, beneath plumbing, or against an outer wall, exposing it to flooding/leak risk, yet no mitigating measures are in place.
- Fire detection/suppression, leak detection, and precision cooling exist but are not inspected or operationally tested, so it cannot be confirmed they actually work.
- No physical or environmental threat identification has been performed with regard to geographic location or surroundings (flooding history, adjacent hazardous facilities, etc.).
- UPS/emergency generation capacity or runtime does not meet the actual load or recovery objectives, or fuel/battery condition is not checked.
- No alarm or notification scheme exists for temperature/humidity, leak, or power anomalies, so events are not recognized early even when they occur.
- Threats from adjacent premises or external factors such as leaks from upper floors or nearby construction are omitted from identification and treatment.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
