# A.8.22 Segregation of networks

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.22 Segregation of networks |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality/Integrity/Availability |
| ISMS-P mapping | 2.6.1 Network access |
| 2013 mapping | 13.1.3 (Segregation in networks) |

## Control objective
Segregation of networks partitions a single network into zones with different trust levels, business functions, and data sensitivity, using logical and/or physical separation so that a compromise or fault in one zone does not spread to others. By separating service networks, management networks, development/test networks, the DMZ, and internal user networks, and by limiting inter-zone traffic to the minimum necessary, the control reduces the attack surface and hinders lateral movement. This protects the confidentiality, integrity, and availability of critical information assets and, when an incident occurs, contains its impact within a specific zone.

## Key checkpoints
1. Is the network divided into zones/segments by trust level, business purpose, and data sensitivity, with the criteria documented?
2. Is inter-zone communication configured to block by default and permit only required traffic (default deny)?
3. Are public-facing services (DMZ) separated from the internal network, the production network from the management network, and the development/test network from production?
4. Are wireless, guest, and business networks separated from one another with controlled access paths?
5. In cloud/virtualized environments, is logical separation applied via VPCs/subnets/security groups and reviewed periodically?
6. Are the segmentation policy and firewall rules reviewed regularly to remove unnecessary or overly permissive allow rules?

## Implementation guidance
- Define trust boundaries and design zones based on asset identification and risk assessment results.
- Place firewalls/router ACLs/next-generation firewalls at zone boundaries and manage allow rules on a whitelist basis after applying default deny.
- Route management traffic through a dedicated management network (OOB) or a bastion/jump host, keeping it separate from the general business network.
- In the cloud, build zones with VPCs/subnets/security groups/network ACLs/service endpoints and manage configuration as code (IaC).
- Consider workload-level micro-segmentation and East-West traffic control from a zero-trust perspective.
- Set a regular review cycle for inter-zone allow rules and tie changes to the change management process with approvals and records.

## Related controls and attributes
- ISO 27001 clauses: 6.1 (risk assessment and treatment), 8.1 (operational planning and control)
- Adjacent Annex A: A.8.20 Networks security, A.8.21 Security of network services, A.8.23 Web filtering, A.5.14 Information transfer
- ISMS-P mapping: 2.6.1 Network access
- 2013 mapping: 13.1.3 (Segregation in networks)

## Evidence
- Network diagrams and zone design documents (trust zones, IP ranges, VLAN configuration)
- Firewall/ACL rule lists and default deny configuration screens
- Results of periodic firewall policy reviews and records of unused/excessive rule cleanup
- Management network/bastion configuration and access control settings
- Cloud VPC/subnet/security group/network ACL configuration details
- Change management records (approvals for zone/rule changes)

## Nonconformity examples
- Public-facing servers reside in the same segment as the internal business network with no DMZ zone.
- Firewall policy contains any-any allow rules, effectively nullifying segmentation.
- The development/test network is not separated from production, so test traffic reaches production systems.
- Management traffic is carried over the general business network with no dedicated management network/bastion.
- A cloud security group exposes management ports (22/3389) to 0.0.0.0/0.
- Inter-zone firewall rules are not reviewed periodically, leaving rules for departed staff or decommissioned systems in place.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
