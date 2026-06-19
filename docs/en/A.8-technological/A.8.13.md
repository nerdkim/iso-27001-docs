# A.8.13 Information backup

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.8 Technological controls |
| Control | A.8.13 Information backup |
| Control type (ref.) | Corrective |
| Security properties (ref.) | Integrity, Availability |
| ISMS-P mapping | 2.9.3 Backup and recovery management |
| 2013 mapping | A.12.3.1 Information backup |

## Control objective

This control requires that copies of information, software, and system images be created and retained on a regular basis so that, when the original is lost through failure, deletion, corruption, or ransomware, it can be restored within the agreed recovery point objective (RPO) and recovery time objective (RTO). Taking backups alone is not sufficient: the objective is to protect the integrity and availability of information by proving recoverability through periodic testing and by protecting the backup copies themselves from unauthorized access, alteration, and destruction.

## Key checkpoints

1. Are the backup scope (business data, configuration information, system images, cryptographic keys, and so on), backup frequency, retention period, and storage location defined in the backup policy/procedure?
2. Do the backup scope and frequency align with recovery targets such as the RPO/RTO derived from business criticality?
3. Is the recoverability of backup data tested periodically, with actual recovery time/consistency results recorded and acted upon?
4. Are access control, encryption, and storage separated from the source (off-site/isolated, and so on) applied to backup repositories/media?
5. Are resilience measures such as immutable/offline/isolated backups in place to guard against simultaneous corruption, for example by ransomware?
6. Is the success/failure of backup jobs monitored, with re-run and escalation procedures operated when a job fails or is missed?

## Implementation guidance

- Define and document the backup scope, frequency, and retention period (including generation management) based on asset criticality and legal/contractual retention requirements.
- Design the backup method (full/incremental/differential) and frequency to meet the RPO/RTO derived from business continuity needs, applying shorter cycles to more critical systems.
- Keep backup copies in a location physically/network-separated from the source, and hold at least one copy in offline/off-site or immutable storage to guard against ransomware spread and single points of failure.
- Encrypt backup data and removable media, and control access to backup repositories and recovery consoles under the least-privilege principle.
- Plan periodic recovery tests (partial/full) to verify actual restore time and data consistency, and record the test results and improvement actions.
- Monitor backup job results with automated alerting, and operate retry and escalation procedures for failures or omissions.
- Manage change history for backup policy/configuration, and apply secure erasure/destruction of residual data when backup media are disposed of.

## Related controls and attributes

- ISO 27001 clauses: 8.1 (Operational planning and control), 6.1 (Actions to address risks and opportunities)
- Adjacent Annex A: A.5.29 (Information security during disruption), A.5.30 (ICT readiness for business continuity), A.8.14 (Redundancy of information processing facilities), A.8.16 (Monitoring activities), A.8.24 (Use of cryptography), A.8.10 (Information deletion)
- ISMS-P mapping: 2.9.3 Backup and recovery management
- 2013 mapping: A.12.3.1 Information backup

## Evidence

- Backup policy/procedure (defining backup scope, frequency, retention period, and owner)
- Backup schedule and backup job logs/success-failure reports
- Recovery test plan and test result reports (including restore time and data consistency)
- Access-rights list and access logs for backup repositories/media
- Evidence of backup encryption settings and of off-site/immutable/offline storage configuration
- Backup media register and disposal records

## Nonconformity examples

- Backups are performed but recovery has never been tested, so actual restorability cannot be demonstrated.
- Backup copies are stored on the same network/storage as the source, so a ransomware infection encrypts the backups as well.
- The backup cycle for a critical system exceeds the defined RPO, so more data is lost during an incident than the tolerated amount.
- Backup media are stored without encryption or access control, exposing them to unauthorized removal/leakage.
- There is no monitoring/alerting for backup failures, so missed backups go unnoticed for several days.
- Retention period/generation management is not defined, so data from a required point in time cannot be restored.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
