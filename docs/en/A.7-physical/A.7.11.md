# A.7.11 Supporting utilities

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.7 Physical controls |
| Control | A.7.11 Supporting utilities |
| Control type (ref.) | Preventive / Detective |
| Security properties (ref.) | Availability |
| ISMS-P mapping | 2.4.4 Protection facility operation (related: 2.4.3 Information system protection, 2.12.1 Safeguards against disaster) |
| 2013 mapping | 11.2.2 |

## Control objective
Supporting utilities are the infrastructure services that information processing facilities depend on for normal operation, such as electricity, telecommunications, heating and cooling, air conditioning, water supply, gas, and drainage. This control requires preventive and detective measures, including adequate capacity, redundancy, continuous monitoring, and periodic inspection, so that degradation, failure, or interruption of these utilities does not compromise the availability of information systems. The purpose is to keep operations continuous by preventing a single utility failure, such as a power outage, cooling failure, or line disruption, from turning into a service interruption or equipment damage.

## Key checkpoints
1. Are the supporting utilities the facility depends on (power, telecommunications, air conditioning, water and drainage) identified, and is each utility's capacity sized to cover current load and future expansion?
2. To guard against power failures such as outages, are UPS, standby generators, and dual feeds provided, and are uninterrupted transfer and battery or fuel runtime verified?
3. Are the states of supporting utilities such as server-room temperature and humidity, power quality, water leakage, and fuel level monitored continuously, with alerts delivered to responsible staff when thresholds are exceeded?
4. Are periodic preventive maintenance and tests for supporting utilities (generator load tests, UPS battery checks) performed as planned and recorded?
5. Are contracts (SLAs) with utility providers, an emergency contact scheme, and alternate supply or recovery procedures in place?
6. Are the locations and accessibility of emergency power cutoff switches and valves ensured, and do relevant staff know the cutoff and recovery procedures?

## Implementation guidance
- Build the power path from dual feeds, a UPS (uninterruptible power supply), and a standby generator, guarantee uninterrupted transfer with an automatic transfer switch (ATS), and verify battery and fuel levels and runtime periodically.
- Define the allowable temperature and humidity range for the server room and make precision cooling units redundant, so that if one fails the standby unit takes over automatically and an alert is raised.
- Monitor power quality, temperature and humidity, water leakage, fuel level, and battery state in real time, and notify responsible staff over multiple channels (SMS, email, operations center) when thresholds are exceeded.
- Perform preventive maintenance such as generator load tests, UPS battery performance checks, and air-conditioning filter replacement on a regular schedule, and record and retain inspection results and actions taken.
- Physically separate and duplicate telecommunications lines and power paths to remove single points of failure (SPOF), using different providers or routes where possible.
- Mark the locations of emergency power cutoff devices and water valves, confirm interlock with fire suppression, and document utility providers' emergency contacts and recovery SLAs, then train relevant staff.

## Related controls and attributes
- ISO 27001 clauses: 6.1 (actions to address risks and opportunities), 7.1 (resources), 8.1 (operational planning and control)
- Adjacent Annex A: A.7.5 (Protecting against physical and environmental threats), A.7.8 (Equipment siting and protection), A.7.12 (Cabling security), A.7.13 (Equipment maintenance), A.5.29 (Information security during disruption), A.5.30 (ICT readiness for business continuity)
- ISMS-P mapping: 2.4.4 Protection facility operation (related: 2.4.3 Information system protection, 2.12.1 Safeguards against disaster)
- 2013 mapping: 11.2.2 (Supporting utilities)

## Evidence
- List of supporting utilities and capacity sizing or load calculation documents
- UPS and standby generator specifications, and automatic transfer and load test records
- Temperature/humidity, power, and leakage monitoring dashboards, and alert and response history
- Periodic preventive maintenance plans, inspection checklists, and result reports
- Utility supply contracts or SLAs, emergency contact lists, and recovery procedures
- Battery and fuel level inspection records and replacement history

## Nonconformity examples
- A UPS is installed, but its battery runtime or transfer operation has never been tested, so uninterrupted transfer fails during an actual outage.
- The server-room precision cooling unit is a single unit with no standby, and its failure alert is not delivered to responsible staff.
- The standby generator's fuel level is not managed, so its runtime is insufficient during a prolonged outage.
- A temperature or humidity threshold alert is raised, but no responsible person or procedure is defined, so it is left unaddressed.
- A preventive maintenance plan for supporting utilities exists, but actual execution and result records are missing.
- Power or telecommunications is provisioned over a single path, leaving a single point of failure, yet no redundancy review has been done.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
