---
name: DFCI Advanced Melanoma Anti-PD1 ICB Cohort (2019)
studyId: mel_dfci_2019
institution: Dana-Farber Cancer Institute (DFCI)
size: 144
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - bulk-rna-seq
panels: []
tags:
  - melanoma
  - anti-pd1
  - nivolumab
  - pembrolizumab
  - immunotherapy
  - tumor-mutation-burden
  - MHC-II
  - biomarker
  - ICI
  - cutaneous
  - mucosal
  - acral
processed_by: crosslinker
processed_at: 2026-05-16
---

# DFCI Advanced Melanoma Anti-PD1 ICB Cohort (2019)

## Overview

This clinically annotated cohort of 144 patients with advanced melanoma was assembled at Dana-Farber Cancer Institute to identify genomic and transcriptomic predictors of response to anti-PD1 immune-checkpoint blockade. Pre-treatment tumor biopsies were profiled by whole-exome sequencing (matched normal) and bulk RNA-seq. The cohort includes cutaneous (72.9%), occult (13.2%), acral (6.9%), and mucosal (6.9%) melanoma subtypes, with patients treated by [nivolumab](../drugs/nivolumab.md) (n=59) or [pembrolizumab](../drugs/pembrolizumab.md) (n=85) and stratified by prior [ipilimumab](../drugs/ipilimumab.md) exposure (41.7% pretreated). The dataset was used to build parsimonious logistic-regression models of primary resistance stratified by prior ipilimumab status, and was cross-validated against the independent [mel_iatlas_riaz_nivolumab_2017](../datasets/mel_iatlas_riaz_nivolumab_2017.md) cohort.

## Composition

- **Total patients:** 144 (after WES QC; 206 initially identified); 121 with RNA-seq
- **Cancer subtypes:** cutaneous [SKCM](../cancer_types/SKCM.md) n=105 (72.9%), occult n=19 (13.2%), acral n=10 (6.9%), mucosal n=10 (6.9%) — collectively [MEL](../cancer_types/MEL.md) / [SKCM](../cancer_types/SKCM.md)
- **Treatment:** nivolumab n=59 (41.0%), pembrolizumab n=85 (59.0%)
- **Prior ipilimumab:** 41.7% (n=60) pretreated; 58.3% (n=84) naive
- **Stage:** 75.0% M1c (n=108); elevated LDH in 49.3%; ECOG 0 in 68.8%
- **Responses (RECIST v1.1):** 45% PD, 14% SD, 3% MR, 26% PR, 12% CR; ORR 38%
- **Median follow-up:** 29.9 months

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — pre-treatment tumor + matched normal; purity/ploidy via [absolute](../methods/absolute.md)
- [bulk-rna-seq](../methods/bulk-rna-seq.md) — pre-treatment tumor (n=121); immune deconvolution by [cibersortx](../methods/cibersortx.md) (LM22)
- [mutational-signatures](../methods/mutational-signatures.md) — COSMIC-based decomposition
- [gsea](../methods/gsea.md) — Hallmark gene-set enrichment analysis for pathway-level response associations

## Papers using this cohort

- [PMID:31792460](../papers/31792460.md) — Liu et al. 2019, tumor heterogeneity and MHC-II expression predict response to anti-PD1 ICB in melanoma

## Notable findings derived from this cohort

- Median nonsynonymous TMB was 6.5 mutations/Mb (IQR 2.0–14.4); [BRAF](../genes/BRAF.md) mutated in 39%, [NRAS](../genes/NRAS.md) in 30%, [NF1](../genes/NF1.md) in 17%. [PMID:31792460](../papers/31792460.md)
- TMB was higher in responders vs progressors (MWW P=0.026), but the association was abolished after adjusting for melanoma subtype (cutaneous/occult vs acral/mucosal; P=0.24 in multivariate regression), arguing against TMB as a generic melanoma biomarker. [PMID:31792460](../papers/31792460.md)
- [TAP2](../genes/TAP2.md) and MHC-I HLA-A/B/C focal amplifications (chr 6p21) were found exclusively in responders (combined n=8; Fisher's P=0.001); [JAK1](../genes/JAK1.md) LOH was associated with resistance (OR=0.33, P=0.02). [PMID:31792460](../papers/31792460.md)
- All 13 MHC-II HLA genes showed higher expression in responders (binomial P=0.0002); an MHC-II ssGSEA score was the strongest single predictor of response in ipilimumab-pretreated tumors and anchored a model (MHC-II + LDH + lymph-node metastasis) with AUC 0.90. [PMID:31792460](../papers/31792460.md)
- For ipilimumab-naive tumors, tumor heterogeneity + ploidy + purity yielded a complementary model (AUC 0.77); each model performed poorly on the opposite subgroup (interaction P=0.004 and P=0.018). [PMID:31792460](../papers/31792460.md)
- IFN-γ and IFN-α response pathways were enriched in responders overall and in the ipilimumab-treated subgroup, with validation in [mel_iatlas_riaz_nivolumab_2017](../datasets/mel_iatlas_riaz_nivolumab_2017.md). [PMID:31792460](../papers/31792460.md)

## Sources

- cBioPortal study: `mel_dfci_2019`
- Primary publication: [PMID:31792460](../papers/31792460.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
