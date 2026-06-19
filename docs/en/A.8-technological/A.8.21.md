# A.8.21 Security of network services

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.21 Security of network services |
| Control type (ref.) | Preventive / Detective |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.6.1 Network access |
| 2013 mapping | A.13.1.2 |

## Control objective

This control ensures that the security features, service levels, and service requirements of the network services the organization uses (whether operated internally or provided by external suppliers, such as circuits, connectivity, VPN, DNS, firewall/IPS, load balancing, DDoS protection, and managed security services) are clearly identified, implemented, and continuously monitored. Because network services determine the availability of business systems and the confidentiality/integrity of information in transit, the security characteristics and performance/availability levels required for each service must be defined in advance and reflected in contracts or internal baselines. The security features actually delivered must also be verified periodically to confirm they are implemented and meet the agreed levels, controlling the risks arising from service degradation or non-delivery of security features.

## Key checkpoints

1. Is there a maintained inventory of the network services the organization uses (internally provided and externally outsourced), with the security features/requirements of each service identified?
2. Are the required security characteristics (authentication, encryption, filtering, isolation, etc.) and service levels (availability, bandwidth, recovery time, etc.) defined and agreed for each network service?
3. Are the security features/service levels (SLAs) of externally provided network services stated in contracts/agreements, with subcontracting and responsibility boundaries specified?
4. Are the security features of network services implemented in actual configuration/operation, and is fulfillment of service levels monitored?
5. Is access to network services controlled on a least-privilege basis (which users/systems may use which services)?
6. Are detection/reporting/response procedures in place for abnormal situations such as service degradation, outages, and non-delivery of security features?

## Implementation guidance

- Inventory all network services the organization uses (leased lines/MPLS, internet circuits, VPN, DNS, firewall/IPS, load balancing, DDoS protection, cloud connectivity, managed security services, etc.) and define the required security features and service requirements for each.
- Document the required security characteristics per service (transport encryption, mutual authentication, access filtering, traffic isolation, provision of logs, etc.) and service level targets (availability, bandwidth, latency, recovery time, support hours), set in line with the risk level.
- For network services from external suppliers, specify security features, service levels, responsibility boundaries, subcontracting conditions, breach/outage notification obligations, and audit/reporting rights in contracts/SLAs, and include disconnection and data return procedures at termination.
- Verify that the defined security features are reflected in actual configuration (for example VPN cipher suites, firewall service policies, DNS security settings), and control which users/systems may use each network service on a least-privilege basis.
- Continuously monitor fulfillment of service levels and security features (availability/performance metrics, security events, SLA reports), and operate corrective-request and escalation procedures when agreed levels are not met.
- Apply security requirement review and the change management (A.8.32) procedure when introducing or changing network services, and periodically re-review the service inventory/requirements/contracts to keep them current.

## Related controls and attributes

- ISO 27001 clauses: 8.1 (Operational planning and control), 6.1 (Actions to address risks), 9.1 (Monitoring and measurement)
- Adjacent Annex A: A.8.20 (Networks security), A.8.22 (Segregation of networks), A.8.23 (Web filtering), A.5.21 (Managing information security in the ICT supply chain), A.5.22 (Monitoring, review and change management of supplier services), A.5.23 (Information security for use of cloud services)
- ISMS-P mapping: 2.6.1 Network access (related: 2.3.2 Security in external party contracts, 2.3.3 Management of external party security compliance, 2.10.1 Operation of security systems, 2.10.5 Information transfer security, 2.9.2 Performance and fault management)
- 2013 mapping: A.13.1.2 (Security of network services)

## Evidence

- Network service inventory and per-service security feature/requirement definitions
- Documentation of service levels (availability/bandwidth/recovery time, etc.) and security characteristics
- External network service contracts/SLAs and the security requirements stated therein (including subcontracting/notification/audit clauses)
- Security feature implementation verification records (configuration snapshots for VPN/firewall/DNS, etc., and inspection results)
- Service level/security feature monitoring reports and corrective-request/escalation records for shortfalls
- Security review and change management records for the introduction/change of network services

## Nonconformity examples

- The security features/requirements of the network services the organization uses are not identified, so what security characteristics each service needs is undefined.
- The contract/SLA with an external supplier does not state security features or service levels, so fulfillment cannot be verified.
- Defined security features (for example transport encryption, access filtering) are not reflected in the actual service configuration.
- Availability/performance and security feature fulfillment of network services are not monitored, so degradation or non-delivery goes unnoticed.
- The external supplier's subcontracting, breach/outage notification obligations, and responsibility boundaries are not specified, leaving no basis for response when an incident occurs.
- A new network service is connected without a security requirement review at introduction, creating an uncontrolled path.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
