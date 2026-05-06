---
name: UC-GENOME (BCAN/HCRN Metastatic Urothelial Carcinoma) 2022
studyId: blca_bcan_hcrn_2022
institution: Bladder Cancer Advocacy Network / Hoosier Cancer Research Network (multi-center)
size: 218
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-DNA-seq
  - RNA-seq
panels:
  - Caris MI TumorSeek 592-Gene NGS Panel
  - Archer FusionPlex Solid Tumor Panel
tags:
  - bladder
  - urothelial
  - metastatic
  - immunotherapy
  - APOBEC
processed_by: crosslinker
processed_at: 2026-05-06
---

# UC-GENOME (BCAN/HCRN Metastatic Urothelial Carcinoma) 2022

## Overview

The UC-GENOME study (NCT02643043) is a prospective multi-center cohort of 218 patients with metastatic urothelial carcinoma (mUC) enrolled at eight academic centers coordinated by the Bladder Cancer Advocacy Network (BCAN) and the Hoosier Cancer Research Network (HCRN). The study performed integrated DNA and RNA sequencing to characterize the molecular landscape of mUC and develop predictive models for immune checkpoint inhibitor (ICI) response. Dataset deposited in cBioPortal as `blca_bcan_hcrn_2022`.

## Composition

- 218 patients with metastatic urothelial carcinoma ([BLCA](../cancer_types/BLCA.md)) enrolled at 8 academic centers (UNC, Fox Chase, Mount Sinai, UW/Fred Hutch, JHU, U Chicago, MSK, [USC](../cancer_types/USC.md)).
- DNA sequencing on 191 patients (Caris MI TumorSeek 592-gene panel); total RNA-seq on 176 patients; 147 samples with complete molecular profiling plus clinical data.
- Comparator cohorts: TCGA-BLCA (non-metastatic), IMvigor210 (metastatic, atezolizumab-treated), Kamoun et al. consensus subtypes, UNC-108.

## Assays / panels (linked)

- [Targeted DNA sequencing](../methods/targeted-dna-seq.md) — Caris MI TumorSeek 592-gene NGS Panel (Agilent SureSelect XT on Illumina NextSeq)
- [RNA-seq](../methods/rna-seq.md) — Illumina TruSeq RiboZero Gold on HiSeq 4000
- Archer FusionPlex Solid Tumor Panel (fusions)
- IHC-based CD8 immune phenotyping (n = 155)

## Papers using this cohort

- [PMID:36333289](../papers/36333289.md) — Primary analysis of UC-GENOME: molecular landscape, subtype characterization, ICI predictive model development.

## Notable findings derived from this cohort

- Stroma-rich molecular subtype was significantly enriched in metastatic cohorts (UC-GENOME, IMvigor210) versus non-metastatic cohorts (TCGA, Kamoun; Mantel-Haenszel chi-squared p = 1.86e-10), and the Excluded immune phenotype was associated with ICI non-benefit (p = 0.0126) [PMID:36333289](../papers/36333289.md).
- [TP53](../genes/TP53.md) E285K hotspot variant was the most frequent TP53 mutation (11% of TP53-mutant cases); enriched in metastatic cohorts (UC-GENOME 10.8%, IMvigor210 6.9%) versus primary TCGA-BLCA (5.9%) [PMID:36333289](../papers/36333289.md).
- Low cosine similarity to APOBEC signature SBS13 independently predicted worse survival on both chemotherapy (HR 2.50, p = 0.013) and ICI (HR 2.19, p = 0.011), suggesting SBS13 is predictive rather than purely prognostic [PMID:36333289](../papers/36333289.md).
- A 25-predictor elastic net ICI response model trained on IMvigor210 achieved AUC = 0.84 in internal validation and AUC = 0.82 in UNC-108, significantly outperforming TMB alone (AUC = 0.68, p = 0.038); performance was lower in UC-GENOME (AUC = 0.65) likely due to RNA-seq methodology differences [PMID:36333289](../papers/36333289.md).
- [ERCC2](../genes/ERCC2.md) mutations associated with significantly higher chemotherapy response rate (p = 0.0134) but not ICI response, validating this biomarker in the metastatic setting; FGFR3-TACC3 fusions found in 4% of evaluable samples, enriched in LumP subtype (OR 7.2, p = 6.1e-5) [PMID:36333289](../papers/36333289.md).

## Sources

- cBioPortal study: `blca_bcan_hcrn_2022`
- ClinicalTrials.gov: NCT02643043

*This page was processed by **crosslinker** on **2026-05-06**.*
