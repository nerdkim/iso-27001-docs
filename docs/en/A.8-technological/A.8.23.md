# A.8.23 Web filtering

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.23 Web filtering |
| Control type (ref.) | Preventive/Detective |
| Security properties (ref.) | Confidentiality/Integrity/Availability |
| ISMS-P mapping | 2.6.7 Internet access control |
| 2013 mapping | New in 2022 |

## Control objective

This control requires that access to external websites be managed/controlled so that members of the organization are less exposed to malicious content and risky sites. When users reach compromised sites, phishing sites, command-and-control (C2) servers, or sites that are unrelated to work or legally problematic, the result can be malware infection, information leakage, and reputational/legal risk. The objective is to protect confidentiality, integrity, and availability together by allowing or blocking target URLs/domains/categories according to policy and by recording and reviewing the outcome.

## Key checkpoints

1. Is an allow/block policy for access to external websites (category, URL, domain, reputation based) defined and formally approved?
2. Is a web filtering capability (proxy, secure web gateway, DNS filtering, firewall URL filter, and so on) in place that blocks known malicious/phishing/C2 sites and risky categories?
3. Are threat intelligence, reputation lists, and category databases kept up to date so that newly identified risky sites are reflected promptly?
4. Is the same filtering policy applied when users connect from outside the corporate network, such as remote workers and mobile devices?
5. Is there an inspection policy for encrypted traffic such as HTTPS, along with criteria for exceptions that consider personal data/privacy?
6. Are block/bypass-attempt logs collected and reviewed, and is there a procedure to request and review exceptions for false positives/negatives?

## Implementation guidance

- Establish allow/block policies per web category based on business need and risk level, and block by default the sites known to distribute malware, host phishing/C2, or provide anonymizing proxies.
- Deploy technical means such as a secure web gateway, proxy, or DNS filtering to control access by URL/domain/reputation/category, and direct policy violations to a block notice page.
- Automatically update threat intelligence, reputation feeds, and category databases so that the latest risky sites are reflected promptly.
- Apply the same policy in remote/mobile environments through an endpoint agent or cloud-based filtering to remove blind spots.
- Apply HTTPS traffic inspection (SSL inspection) while managing sensitive sites such as finance/healthcare on an exception list, and document the inspection scope and exceptions to meet privacy/legal requirements.
- Collect and periodically review block events, bypass attempts, and policy-exception requests, and operate an exception-approval procedure and user guidance (acceptable use policy) for false positives/negatives.
- Combine with download-file scanning and malware controls to defend against web-borne threats in multiple layers.

## Related controls and attributes

- ISO 27001 clauses: 6.1 (Actions to address risks and opportunities), 8.1 (Operational planning and control)
- Adjacent Annex A: A.8.22 (Segregation of networks), A.8.20 (Networks security), A.8.21 (Security of network services), A.8.7 (Protection against malware), A.5.10 (Acceptable use of information and other associated assets)
- ISMS-P mapping: 2.6.7 Internet access control (for the malware aspect, also 2.10.9 Malware control)
- 2013 mapping: New in 2022 (no corresponding control in the 2013 edition)

## Evidence

- Web filtering/internet access control policy and allow/block category criteria
- Secure web gateway/proxy/DNS filter configuration screens and block-policy settings
- Update history of threat intelligence/reputation/category databases
- Block-event logs, bypass-attempt logs, and periodic review/inspection records
- Policy-exception (allow) request/approval records and the exception list
- Filtering coverage status for remote/mobile devices and SSL-inspection exception documentation

## Nonconformity examples

- There is no allow/block policy for internet access, or it is undocumented, so unrestricted access to any site is possible.
- A web filtering capability is deployed, but the category/reputation database is not updated for a long time, so newly emerging malicious/phishing sites are not blocked.
- Filtering is applied on the corporate network but not on remote-work/mobile devices, allowing access to be bypassed.
- Block/bypass-attempt logs are only collected and never reviewed, so attempts to reach malicious sites go unnoticed.
- Blocks are lifted arbitrarily without an exception-approval procedure, or the exception list is not maintained.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
