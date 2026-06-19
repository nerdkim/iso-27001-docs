# A.8.12 Data leakage prevention

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.12 Data leakage prevention |
| Control type (ref.) | Preventive/Detective |
| Security properties (ref.) | Confidentiality |
| ISMS-P mapping | 2.10.5 Information transmission security |
| 2013 mapping | New in 2022 |

## Control objective

This control requires that the movement of sensitive/critical information beyond the organization's control boundary to unauthorized recipients or locations be detected and blocked. By monitoring and governing data movement across leakage channels such as email, web/cloud uploads, removable media, printouts, remote access, and screen capture, the objective is to prevent both deliberate exfiltration and accidental exposure, thereby protecting the confidentiality of personal data, trade secrets, and intellectual property.

## Key checkpoints

1. Are the types and classification criteria of sensitive/critical information subject to leakage prevention defined, and is the control scope (systems/networks/endpoints/storage media) identified?
2. Are detection/blocking policies established and applied for each major leakage channel (email, web/cloud upload, removable media, printouts, remote access, and so on)?
3. Are policy violation events logged, with response levels (alert/approval/block) distinguished according to severity?
4. Are procedures and assigned responsibilities defined for reviewing, responding to, and handling exceptions for detected violation events?
5. Is control effectiveness (false positives/negatives, bypass potential) reviewed periodically, and are detection rules and policies updated?
6. Is the monitoring scope and handling of logs reviewed from the perspective of worker privacy/personal-data protection, with a basis such as notice/consent in place?

## Implementation guidance

- Working from the information classification scheme, identify the data to protect (personal data, trade secrets, authentication data, intellectual property) and define detection rules (regular expressions, fingerprinting, keywords, classification labels).
- Place control points by data state: in transit (network gateways, email/web proxies), in use (endpoint agents), and at rest (cloud access security broker (CASB), repository scanning).
- Distinguish response levels in policy: log only, warn the user, allow after approval, block, or enforce encryption.
- Manage tasks that require exceptions/bypass (bulk transfers, export of development/test data) on the basis of prior approval and a validity period, and keep audit logs.
- To reduce false positives, operate initially in monitoring (detection) mode, then strengthen blocking policies in stages after validation.
- Store events/logs in an access-controlled repository, and finalize the monitoring scope and notices after legal/HR review to manage the risk of privacy intrusion.

## Related controls and attributes

- ISO 27001 clauses: 6.1 (Actions to address risks and opportunities), 8.1 (Operational planning and control), 9.1 (Monitoring, measurement, analysis and evaluation)
- Adjacent Annex A: A.5.12 (Classification of information), A.5.13 (Labelling of information), A.5.14 (Information transfer), A.8.10 (Information deletion), A.8.11 (Data masking), A.8.16 (Monitoring activities), A.8.24 (Use of cryptography)
- ISMS-P mapping: 2.10.5 Information transmission security (related: 2.10.1 Operation of security systems, 2.10.6 Security of work devices, 2.10.7 Management of removable storage media, 2.6.7 Internet access control)
- 2013 mapping: New in 2022 (no corresponding control in the 2013 edition)

## Evidence

- DLP policy/operating procedure and the classification criteria for data to be protected
- Detection/blocking rule configuration screens and policy lists by channel
- DLP violation event logs and alert/response handling history
- Exception approval requests/records and a validity-period management register
- Policy-effectiveness review (false positive/negative analysis) results and detection-rule improvement history
- Employee notice/consent and legal/HR review materials related to monitoring

## Nonconformity examples

- Types of data to be protected are not defined, so DLP rules are set only nominally and fail to detect actual sensitive information.
- DLP is applied only to the email channel, while major leakage paths such as web upload, cloud, and removable media are not controlled.
- Violation events occur in large volumes, but no reviewer/responder is assigned and they are left unattended.
- Exceptions are granted indefinitely without an approval process, effectively nullifying the control.
- The system runs only in detection (monitoring) mode, failing to block actual leakage attempts, with no plan to transition to blocking policies.
- Retention period/access control for DLP event logs is inadequate, so they cannot be used for later investigation and root-cause analysis.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
