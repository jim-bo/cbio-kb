---
name: MSKCC NSCLC Pembrolizumab Cohort (Rizvi 2015)
studyId: nsclc_mskcc_2015
institution: Memorial Sloan Kettering Cancer Center
size: 34 advanced NSCLC patients (discovery n=16, validation n=18) treated with pembrolizumab
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - pd-l1-ihc-22c3
panels: []
tags:
  - nsclc
  - immunotherapy
  - tumor-mutation-burden
  - neoantigens
  - pd-1-blockade
  - pembrolizumab
  - dna-repair
  - smoking-signature
processed_by: crosslinker
processed_at: 2026-05-14
---

# MSKCC NSCLC Pembrolizumab Cohort (Rizvi 2015)

## Overview

Two independent cohorts of advanced non-small cell lung cancer ([NSCLC](../cancer_types/NSCLC.md)) patients treated with the anti-PD-1 antibody [pembrolizumab](../drugs/pembrolizumab.md) at Memorial Sloan Kettering Cancer Center; paired tumor/normal whole-exome sequencing used to characterize somatic mutation burden and its relationship to anti-PD-1 response. The study was published in *Science* in 2015 by Rizvi et al. (DOI: 10.1126/science.aaa1348). Data are deposited at cBioPortal (study "Rizvi lung cancer") and dbGaP (phs000980.v1.p1).

## Composition

- **Discovery cohort:** n=16 advanced [NSCLC](../cancer_types/NSCLC.md) patients treated with [pembrolizumab](../drugs/pembrolizumab.md).
- **Validation cohort:** n=18 advanced [NSCLC](../cancer_types/NSCLC.md) patients treated with [pembrolizumab](../drugs/pembrolizumab.md).
- 34 paired tumor/normal exomes total.
- PD-L1 expression measured on 30/34 patients; cohort was enriched for PD-L1 expression (24/30 with detectable expression).
- Cancer type: [NSCLC](../cancer_types/NSCLC.md).

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — mean target coverage 164×; 94.5% of target covered ≥10×. Orthogonal Ampliseq resequencing of 376 variants confirmed 357 (95%).
- [pd-l1-ihc-22c3](../methods/pd-l1-ihc-22c3.md) — PD-L1 expression by clone 22C3 (Merck) on 30/34 patients.
- HLA class I-restricted neoantigen prediction (mutant nonamers ≤500 nM binding) and MHC multimer screening on serially collected peripheral blood lymphocytes.

## Papers using this cohort

- [PMID:25765070](../papers/25765070.md) — Rizvi et al. (2015). Whole-exome sequencing of 34 pembrolizumab-treated [NSCLC](../cancer_types/NSCLC.md) tumors; established nonsynonymous mutation burden as a predictive biomarker for durable clinical benefit and demonstrated neoantigen-specific T cell expansion paralleling tumor regression.

## Notable findings derived from this cohort

- Higher nonsynonymous somatic mutation burden significantly associated with durable clinical benefit (DCB), objective response rate, and progression-free survival in both discovery and validation cohorts; pooled analysis (n=34) Mann-Whitney P=0.0008, PFS HR 0.19 (95% CI 0.08–0.47, P=0.0004). [PMID:25765070](../papers/25765070.md)
- A cutoff of ≥178 nonsynonymous mutations showed discovery sensitivity 100%/specificity 67% and validation sensitivity 86%/specificity 75% for predicting DCB. [PMID:25765070](../papers/25765070.md)
- A molecular smoking signature (transversion-high classifier) stratified outcomes more powerfully than self-reported smoking history (PFS HR 0.15, P=0.0001 vs P=0.29 for self-reported). [PMID:25765070](../papers/25765070.md)
- Neoantigen burden (median 112/tumor, range 8–610) strongly correlated with mutation burden (Spearman ρ=0.91) and DCB (median 203 vs 83 neoantigens, P=0.001). [PMID:25765070](../papers/25765070.md)
- Deleterious mutations in [POLD1](../genes/POLD1.md), [POLE](../genes/POLE.md), and [MSH2](../genes/MSH2.md) identified a never-smoker subset reaching the high-burden state via DNA repair/replication defects. [PMID:25765070](../papers/25765070.md)
- In one exceptional responder, anti-PD-1 induced a CD8+ T cell response specific for a [HERC1](../genes/HERC1.md) P3278S neoantigen (HLA-A-restricted; ASNASSAAK) that paralleled radiographic tumor regression, directly linking mutation-derived neoantigen recognition to clinical efficacy. [PMID:25765070](../papers/25765070.md)
- Mutation burden stratified outcomes within PD-L1-positive tumors, suggesting mutation burden and PD-L1 IHC capture complementary information. [PMID:25765070](../papers/25765070.md)

## Sources

- [PMID:25765070](../papers/25765070.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
