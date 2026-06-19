# A.6.7 Remote working

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.6 People controls |
| Control | A.6.7 Remote working |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.6.6 Remote access control |
| 2013 mapping | A.6.2.2 |

## Control objective

This control ensures that information accessed, processed, or stored by personnel working outside the organization's physical boundary (home, in transit, client sites, shared offices) is protected to the same level as on-premises work. Remote environments carry greater exposure than the office because of uncontrolled networks, spaces shared with family or others, and devices prone to loss or theft, so the organization must define in advance the conditions under which remote working is permitted and the technical, physical, and procedural safeguards to be applied. The aim is to preserve the confidentiality, integrity, and availability of information and to keep access controlled regardless of where work is performed.

## Key checkpoints

1. Is there a policy/procedure defining the conditions, scope, and approval process for remote working and the security requirements to be met?
2. When accessing internal systems/data from remote locations, are secure connections (such as VPN) and strengthened authentication (such as multi-factor) enforced?
3. Are security requirements (encryption, anti-malware, screen lock, patching) defined and checked for devices used in remote work, whether company-issued or personally owned (BYOD)?
4. Are physical safeguards in place for the environment (screen exposure in shared spaces, handling of printouts/storage media, response to loss/theft)?
5. Are remote workers' access rights and access logs managed/monitored the same as on-premises, and are rights/assets reclaimed when remote working ends?
6. Are remote workers trained on the relevant policy and incident reporting procedures, and is compliance checked?

## Implementation guidance

- Establish a policy that specifies who/where/under what conditions remote working is permitted, the approval and exception process, and the permitted devices and services, and obtain management approval.
- Enforce encrypted communication channels such as VPN and multi-factor authentication for access to internal resources from remote locations, and restrict target/time/network where needed.
- Apply minimum security baselines to remote devices (disk encryption, anti-malware, automatic screen lock, current patches, remote wipe for loss) and check them periodically.
- Where personally owned devices (BYOD) are allowed, run separate conditions and consent procedures such as work/personal separation, limited access scope, and no local data storage.
- Advise on physical and network practices such as preventing shoulder-surfing in shared/public spaces (privacy filters, seating), controlling printouts/removable media, and limiting use of public Wi-Fi.
- Provide procedures and contact channels so that incidents such as loss/theft or data leakage can be reported immediately and responded to with remote lock/wipe.
- Reclaim access rights and require return/deletion of issued devices and data when remote working ends or a role changes.

## Related controls and attributes

- ISO 27001 clauses: 6.1 (Actions to address risks), 7.2 (Competence), 7.3 (Awareness), 8.1 (Operational planning and control)
- Adjacent Annex A: A.6.2 (Terms and conditions of employment), A.6.3 (Information security awareness, education and training), A.7.9 (Security of assets off-premises), A.8.1 (User endpoint devices), A.8.5 (Secure authentication)
- ISMS-P mapping: 2.6.6 Remote access control (related: 2.4.7 Workspace security, 2.10.6 End-user device security)
- 2013 mapping: A.6.2.2 (Teleworking)

## Evidence

- Remote working policy/procedure and management approval document
- Remote working application/approval records and list of approved personnel
- VPN/multi-factor authentication configuration and remote access logs
- Remote device security baselines and check results (encryption, anti-malware, patch status)
- BYOD conditions, user consent forms, and access-scope configuration
- Security training materials for remote workers and completion records
- Access-rights reclamation and asset-return records at end of remote working

## Nonconformity examples

- Remote working is widely practiced, but there is no governing policy or approval process, so no control basis can be confirmed.
- Internal systems are accessed from remote locations in cleartext or with single-factor authentication, without VPN or multi-factor authentication.
- Remote devices have no disk encryption or screen lock, so information leakage is not controlled if a device is lost or stolen.
- Personally owned devices (BYOD) are used for work without separate conditions or consent, and data is stored/retained on personal devices.
- Access logs of remote workers are not collected or monitored, so anomalous access cannot be detected.
- After remote working ends, access rights are not reclaimed and issued devices/data are left unreturned.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
