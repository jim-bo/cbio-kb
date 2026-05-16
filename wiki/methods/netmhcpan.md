---
name: NetMHCpan
slug: netmhcpan
kind: method
canonical_source: corpus
unverified: true
tags: [neoantigen-prediction, mhc-binding, immunogenicity]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# NetMHCpan

## Overview

NetMHCpan is a pan-allele MHC class I binding affinity prediction algorithm that estimates the probability of a peptide being presented by a given HLA allele. It accepts as input a set of peptide sequences and a patient's personal HLA alleles (typically typed by tools such as POLYSOLVER or ATHLATES), and returns predicted IC50 affinity values. Peptides below a defined affinity threshold (commonly 500 nM, with stricter cutoffs of 150 nM or 50 nM also used) are classified as predicted neoepitopes.

## Used by

- [Hugo et al. 2016 — anti-PD-1 melanoma study](../papers/26997480.md): NetMHCpan v2.8 (MHC class I) and NetMHCIIpan v3.0 (MHC class II) used to predict neoepitope loads in 38 anti-PD-1-treated metastatic melanoma WES samples; HLA typing performed by ATHLATES; neoepitope load (class I 231 vs 156, p=0.41; class II 130 vs 95, p=0.36) trended higher in responders but did not reach significance [PMID:26997480](../papers/26997480.md).
- [Giannakis et al. 2016 — CRC neoantigen-survival study](../papers/27149842.md): NetMHCpan v2.4 applied to 9-mer and 10-mer mutant peptides with personal HLA alleles (typed by POLYSOLVER) at <500 nM affinity cutoff (alternates: 150 nM and 50 nM also tested); neoantigen load correlated with lymphocytic infiltration (Spearman rho=0.29, p=2.6e-11) and independently predicted improved CRC-specific survival (multivariate HR=0.57, 95% CI 0.35–0.93) in 619 CRC cases [PMID:27149842](../papers/27149842.md).
- NetMHC v4.0 used for neoantigen prediction from 9-mer sliding windows of 17-mer mutated peptides (rank<2%) in 68 melanoma WES samples; identified neoantigens selectively depleted on nivolumab in responders [PMID:29033130](../papers/29033130.md)
- Used to predict HLA-restricted neoantigen binding affinity from somatic mutations in the MSK IMPACT neoantigen cohort [PMID:29657128](../papers/29657128.md)

## Notes

- The standard 500 nM affinity cutoff is considered permissive; stricter cutoffs (150 nM, 50 nM) yield stronger but fewer predicted neoantigens.
- NetMHCpan does not assess peptide processing efficiency (proteasomal cleavage, TAP transport) or actual T-cell recognition — these are known limitations.
- The tool accepts patient-specific HLA allele inputs, enabling personalized neoantigen prediction.
- Pan-allele coverage allows use even for rare HLA alleles not covered by allele-specific models.

## Sources

- Nielsen M, Andreatta M (2016) NetMHCpan-3.0; improved induction of MHC binding motifs. *Nucleic Acids Research* 44:W551–W556.
- [PMID:26997480](../papers/26997480.md)
- [PMID:27149842](../papers/27149842.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29033130](../papers/29033130.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29657128](../papers/29657128.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
