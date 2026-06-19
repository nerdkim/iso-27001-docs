# A.5.21 Managing information security in the ICT supply chain

| Field | Value |
|---|---|
| Standard | ISO/IEC 27001:2022 Annex A |
| Theme | A.5 Organizational controls |
| Control | A.5.21 Managing information security in the ICT supply chain |
| Control type (ref.) | Preventive |
| Security properties (ref.) | Confidentiality, Integrity, Availability |
| ISMS-P mapping | 2.3.2 Security in external party contracts |
| 2013 mapping | 15.1.3 Information and communication technology supply chain |

## Control objective
This control identifies and manages the risks that arise across the acquisition and use of ICT products and services. Hardware, software, firmware, cloud, and managed services reach an organization through multiple upstream and downstream suppliers, so a vulnerability or tampering in a single component can propagate across the whole environment. The control requires security requirements to flow down and be verified not only through the directly contracted supplier but along the full chain of sub-suppliers (subcontractors). Its aim is to assure the authenticity and integrity of components, prepare for supply disruption, and prevent risk proactively.

## Key checkpoints
1. Is there a procedure to identify and assess ICT supply chain risks (component provenance, sub-suppliers, tampering/counterfeiting) when acquiring ICT products/services?
2. Do contracts/agreements require security requirements to be propagated down to sub-suppliers (subcontractors)?
3. Are there methods to verify the authenticity and integrity of acquired hardware/software components (genuineness, tamper checks, signature/hash verification)?
4. Are software components (open source, third-party libraries) inventoried (e.g., an SBOM) with tracking of vulnerabilities, licenses, and end-of-life/support (EoL/EoS) status?
5. Have alternatives and continuity measures been considered for supply disruption, discontinuation, or supplier failure of critical ICT products/services?
6. Is security verification and monitoring performed on components delivered through the supply chain, both before adoption and during operation?

## Implementation guidance
- State supply chain security requirements (component provenance disclosure, authenticity evidence, flow-down obligations to sub-suppliers, vulnerability notification duties) in the ICT acquisition policy and embed them in the procurement process.
- Identify ICT products/services critical to the organization and their suppliers, map the supply chain tiers (first, second, and beyond) and subcontracting structure, and apply management effort proportionate to risk.
- Include in contracts/agreements the flow-down of security requirements, provision of component specifications (including an SBOM), notification of security incidents/vulnerabilities, and audit/verification rights.
- Verify authenticity and integrity by checking hardware for genuineness/tampering (seals, serials, chain-of-custody) and software via digital signatures, hashes, or checksums.
- Obtain and maintain a software bill of materials (SBOM) and continuously track known vulnerabilities (CVEs), license risks, and end-of-support dates.
- Reduce single-supplier dependence for critical components by pre-assessing alternative suppliers/products, and keep migration plans ready for discontinuation or end of support (EoS).
- Formalize pre-adoption security verification (acceptance testing, known-vulnerability checks) and in-operation monitoring (reflecting patches, version changes, and vulnerability advisories).

## Related controls and attributes
- ISO 27001 clauses: 6.1 (Actions to address risks and opportunities), 8.1 (Operational planning and control), 9.1 (Monitoring, measurement, analysis and evaluation)
- Adjacent Annex A: A.5.19 (Information security in supplier relationships), A.5.20 (Addressing information security within supplier agreements), A.5.22 (Monitoring, review and change management of supplier services), A.5.23 (Information security for use of cloud services), A.8.30 (Outsourced development)
- ISMS-P mapping: 2.3.2 Security in external party contracts (adjacent: 2.3.1 External party status management, 2.3.3 Management of external party security compliance, 2.8.1 Definition of security requirements)
- 2013 mapping: 15.1.3 Information and communication technology supply chain

## Evidence
- ICT acquisition policy/procedures that include supply chain security requirements
- List of critical ICT products/services and suppliers, plus documentation mapping supply chain tiers/subcontracting
- Contracts/agreements specifying security requirements (flow-down to sub-suppliers, SBOM provision, vulnerability notification)
- Records of component authenticity/integrity verification (signature/hash checks, genuineness confirmation)
- Software bill of materials (SBOM) and a register tracking vulnerabilities/licenses/end-of-support
- Pre-adoption security verification results and in-operation monitoring/action records
- Alternative-supplier assessments for critical components and continuity/migration plans

## Nonconformity examples
- ICT products/services are contracted without identifying supply chain risks or defining security requirements.
- Security requirements are imposed only on the directly contracted supplier, with no flow-down to sub-suppliers (subcontractors).
- No software bill of materials (SBOM) is obtained for adopted software, so the impact scope of open-source vulnerabilities (CVEs) cannot be determined.
- Hardware/software is adopted without authenticity/integrity verification (genuineness, signature, hash), exposing the organization to tampering/counterfeiting risk.
- A critical ICT product remains in operation past its end of support (EoS) with no replacement or migration plan.

---
> Source/limitation: Control numbers, titles, and theme classification are based on the publicly available list of ISO/IEC 27001:2022 Annex A. The explanatory text (control objective, key checkpoints, implementation guidance, evidence, nonconformity examples) and the attribute classification are original material written by this collection for practical reference; they are not the normative text of the ISO/IEC 27001:2022 or 27002:2022 standards. For certification, verify against a licensed copy of the standard.
