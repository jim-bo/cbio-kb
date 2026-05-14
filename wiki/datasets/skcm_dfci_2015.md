---
name: Skin Cutaneous Melanoma (DFCI, Science 2015)
studyId: skcm_dfci_2015
institution: Dana-Farber Cancer Institute / Broad Institute; multi-institution European collaboration
size: 110
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - MRNA_EXPRESSION
panels: []
tags:
  - melanoma
  - immunotherapy
  - checkpoint-blockade
  - ipilimumab
  - tumor-mutational-burden
  - neoantigens
  - tumor-microenvironment
processed_by: crosslinker
processed_at: 2026-05-14
---

# Skin Cutaneous Melanoma (DFCI, Science 2015)

## Overview

The skcm_dfci_2015 dataset is from Van Allen et al. (Science, 2015) and comprises pretreatment whole-exome sequencing of 110 metastatic melanoma patients treated with single-agent [ipilimumab](../drugs/ipilimumab.md) (anti-CTLA-4), with matched tumor RNA-seq for 42 (40 with matched WES). This is a landmark study establishing tumor mutational load and predicted neoantigen load as genomic correlates of clinical benefit from CTLA-4 blockade. Patients were stratified by RECIST response and overall survival. All sequencing data are deposited in dbGaP (phs000452.v2.p1).

## Composition

- 110 metastatic melanoma patients treated with ipilimumab monotherapy.
- Histology: 92 cutaneous [SKCM](../cancer_types/SKCM.md), 4 mucosal, 14 occult melanomas.
- Clinical stratification: clinical benefit (CR/PR or SD with [OS](../cancer_types/OS.md) >1 yr, n=27); no clinical benefit (PD or SD with OS <1 yr, n=73); long-term-survival/early-progression (PFS <6 mo but OS >2 yr, n=10).
- Average exome coverage: 183.7× (tumor), 157.2× (germline).
- RNA-seq for 42 patients (40 with matched WES).
- Reference genome: hg19.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md)

## Papers using this cohort

- [PMID:26359337](../papers/26359337.md) — Van Allen et al. 2015, Science — "Genomic correlates of response to CTLA-4 blockade in metastatic melanoma."

## Notable findings derived from this cohort

- Nonsynonymous mutational load (median 197 per sample) was significantly higher in clinical-benefit patients than non-benefit patients (P=0.0076, Mann-Whitney); association held in multivariate models controlling for prior RAF inhibitor and M class [PMID:26359337](../papers/26359337.md).
- Predicted neoantigen load (9–10 aa peptides, HLA class I binding ≤500 nM; median 369 per sample) was significantly associated with clinical benefit (P=0.027); highly correlated with mutational load (Spearman ρ=0.97) [PMID:26359337](../papers/26359337.md).
- Cytolytic activity signature (geometric mean of [GZMA](../genes/GZMA.md) and [PRF1](../genes/PRF1.md) expression) was significantly elevated in clinical-benefit tumors (P=0.042); tumor [CTLA4](../genes/CTLA4.md) expression (P=0.033) and [PDCD1LG2](../genes/PDCD1LG2.md) / PD-L2 expression (P=0.041) also higher in responders [PMID:26359337](../papers/26359337.md).
- Of 77,803 unique neoantigens, only 28 (~0.04%) were shared across benefit patients; no recurrent peptide sequence signature validated — response-associated neoantigens are overwhelmingly private events [PMID:26359337](../papers/26359337.md).
- No individual genes (including [BRAF](../genes/BRAF.md) and [NRAS](../genes/NRAS.md)) were enriched for nonsynonymous mutations in either response subgroup; clinical covariates (age, gender, histology, LDH) did not correlate with response [PMID:26359337](../papers/26359337.md).

## Sources

- Van Allen EM et al. "Genomic correlates of response to CTLA-4 blockade in metastatic melanoma." Science. 2015;350(6257):207-211. [PMID:26359337](../papers/26359337.md). DOI: 10.1126/science.aad0095.

*This page was processed by **crosslinker** on **2026-05-14**.*
