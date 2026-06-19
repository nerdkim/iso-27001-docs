# A.8.20 Networks security

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.20 Networks security |
| Control type (ref.) | Preventive / Detective |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.6.1 Network access |
| 2013 mapping | A.13.1.1, A.13.1.2 |

## Control objective

This control ensures that networks and network devices are securely managed and controlled so that information passing over the network and the systems/services it supports are protected from threats such as unauthorized access, eavesdropping, tampering, and denial of service. Because networks include both connections between internal systems and paths to external parties, areas of differing trust levels must be separated, traffic across perimeters and segments must be controlled, and the confidentiality/integrity of data in transit must be assured. Network activity must also be continuously logged and monitored so that anomalies can be detected and responded to.

## Key checkpoints

1. Are network diagrams/asset inventories kept current, and are areas (DMZ, internal network, management network, etc.) separated according to trust level?
2. Are access control policies across perimeters and segments defined on a least-privilege basis and reflected in firewalls/ACLs?
3. Are security configuration baselines for network devices (changing default passwords, disabling unnecessary services/ports, restricting management access) established and applied?
4. Are encryption and authentication applied to remote access, wireless, and external connection segments?
5. Is network traffic logged/monitored, and is there an operating capability to detect and alert on anomalies?
6. Are security requirements/service levels (SLAs) for network services (internally operated or from external providers) identified, agreed, and fulfilled?

## Implementation guidance

- Separate the network into zones by trust level (public/DMZ, internal business network, management network, development network, etc.) and configure inter-zone traffic to block by default and permit only required flows (default deny) via firewalls/ACLs.
- Establish security configuration standards for network devices (routers, switches, firewalls, wireless APs, etc.) covering default account/password changes, disabling unnecessary services/ports, restricting management-interface access, and keeping firmware up to date.
- To protect confidentiality/integrity in transit, use encrypted protocols such as SSH/HTTPS for remote management, and apply VPN and strengthened authentication (multi-factor) to external/wireless/remote access segments.
- Collect logs from network devices and security systems centrally (log server/SIEM), and continuously monitor for signs of intrusion/misuse using threshold-based alerting and anomalous-traffic detection (IDS/IPS, NDR, etc.).
- With external network service providers, specify the security features, service levels, and management requirements of the provided services in contracts/agreements, and periodically review whether they are fulfilled.
- Apply the change management (A.8.32) procedure to network configuration changes, periodically review firewall policies/ACLs to remove unused or overly permissive rules, and keep network diagrams current.

## Related controls and attributes

- ISO 27001 clauses: 8.1 (Operational planning and control), 6.1 (Actions to address risks), 9.1 (Monitoring and measurement)
- Adjacent Annex A: A.8.21 (Security of network services), A.8.22 (Segregation of networks), A.8.23 (Web filtering), A.8.24 (Use of cryptography), A.8.16 (Monitoring activities), A.8.15 (Logging)
- ISMS-P mapping: 2.6.1 Network access (related: 2.10.1 Operation of security systems, 2.10.5 Information transfer security, 2.6.7 Internet access control, 2.6.5 Wireless network access)
- 2013 mapping: A.13.1.1 (Network controls), A.13.1.2 (Security of network services)

## Evidence

- Network diagrams and network asset/zone inventories
- Firewall/ACL policies and policy review (periodic re-review) records
- Network device security configuration standards and applied configuration records (snapshots/inspection results)
- Encryption and authentication configuration for remote/wireless/external access (VPN, multi-factor authentication, etc.)
- Log collection and monitoring/alerting configuration for network/security devices, and anomaly detection/response records
- External network service contracts/SLAs and fulfillment review results

## Nonconformity examples

- Areas of differing trust level are not separated, so externally reachable systems and internal core systems coexist on the same network.
- The firewall policy contains overly permissive (any-any) rules with unclear purpose/justification and is not periodically reviewed.
- Default accounts/passwords on network devices are unchanged, or unnecessary management services are exposed externally.
- Remote/wireless access segments lack encryption or strengthened authentication, creating a risk of eavesdropping/unauthorized access.
- Network device logs are not collected/monitored, so intrusion attempts or anomalous traffic cannot be detected.
- Security requirements/service levels for external network services are not defined in the contract, so fulfillment cannot be verified.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
