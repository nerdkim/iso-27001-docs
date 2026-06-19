# A.8.18 Use of privileged utility programs

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.18 Use of privileged utility programs |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality / Integrity / Availability |
| ISMS-P mapping | 2.5.5 Special account and privilege management |
| 2013 mapping | 9.4.4 Use of privileged utility programs |

## Control objective

Privileged utility programs are tools capable of overriding or bypassing the normal controls of a system or application, such as access control, authorization checks, and logging. This control requires the organization to restrict and tightly govern the possession, installation, and use of such tools, so that unauthorized users cannot exploit them to alter data/systems or evade controls. By ensuring they are used only by the minimum necessary personnel, only when needed, and in a verified/recorded manner, the control protects operational stability and the integrity/confidentiality of information.

## Key checkpoints

1. Are privileged utility programs that can override system/application controls identified, inventoried, and managed?
2. Are there approval procedures for installing/holding/using privileged utility programs and criteria for granting usage rights?
3. Are usage rights limited to the minimum personnel who genuinely need them for their work, and are they reviewed periodically?
4. Are privileged utility usage actions (who/when/what/why) logged and reviewed?
5. Are unnecessary or unused privileged utility programs removed or disabled?
6. In environments where application controls are enforced, is the use of tools that can bypass them technically restricted?

## Implementation guidance

- Identify and maintain an inventory of programs that can bypass controls, such as operating system administration tools, diagnostic/debugging tools, disk/memory editors, password recovery tools, packet analyzers, and database administration utilities.
- Require prior approval for installing/using privileged utilities, and record the approval rationale, purpose, and duration of use.
- Grant rights only to necessary personnel under the least-privilege principle, and tie shared tools to individual accounts/tokens so that individuals remain identifiable.
- Separate ordinary user rights from privileged utility usage rights, and distinguish everyday work accounts from administration-purpose accounts.
- Log and monitor privileged utility usage, and configure alerts to detect unapproved or abnormal use.
- Remove or disable unused/unnecessary utilities from systems, and restrict access to executables using file permissions/allowlisting.
- By default, isolate/block tools that can bypass application controls (authorization checks, integrity checks, and so on) on operational systems, and permit them only temporarily in a controlled environment when required.
- Allow the use of privileged utilities by external/maintenance personnel only within the contracted/approved scope, and record and supervise their sessions.

## Related controls and attributes

- ISO 27001 clauses: 8.1 (Operational planning and control), 9.1 (Monitoring, measurement, analysis and evaluation), 6.1 (Actions to address risks and opportunities)
- Adjacent Annex A: A.8.2 (Privileged access rights), A.8.3 (Information access restriction), A.8.5 (Secure authentication), A.8.19 (Installation of software on operational systems), A.8.15 (Logging), A.8.16 (Monitoring activities)
- ISMS-P mapping: 2.5.5 Special account and privilege management (from the usage-control/recording angle, it also relates to 2.6.2 Information system access and 2.9.4 Log and access record management)
- 2013 mapping: 9.4.4 Use of privileged utility programs

## Evidence

- Inventory identifying and managing privileged utility programs
- Approval requests and records for installing/using privileged utilities
- Records of granting/revoking usage rights and periodic rights reviews
- Privileged utility usage logs and monitoring/alert records
- Records of removing/disabling unused utilities
- Approval/session records for privileged tool use by external maintenance personnel

## Nonconformity examples

- The organization cannot identify or manage which utilities capable of bypassing system controls are installed.
- Personnel install/use privileged utilities at their own discretion with no approval procedure.
- Shared administration tools are used jointly without individual identification, so the acting user cannot be determined.
- No usage logs are kept for privileged utilities, so misuse cannot be verified after the fact.
- Diagnostic/debugging tools are left on operational systems after a project ends and are accessible to anyone.
- Despite application access controls, data is arbitrarily modified by bypassing the controls with a direct database editing tool.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
