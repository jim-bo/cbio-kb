---
name: MSK-MIND Lung Cancer Multimodal 2020
studyId: lung_msk_mind_2020
institution: Memorial Sloan Kettering Cancer Center
size: 247
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MSK-IMPACT
  - CT-radiomics
  - PD-L1-IHC
panels:
  - msk-impact-panel
tags:
  - NSCLC
  - lung
  - immunotherapy
  - multimodal
  - radiomics
processed_by: crosslinker
processed_at: 2026-05-06
---

# MSK-MIND Lung Cancer Multimodal 2020

## Overview

The MSK-MIND (Multimodal Integration of Imaging, pathology aND genomics) dataset from Memorial Sloan Kettering Cancer Center comprises 247 patients with advanced non-small cell lung cancer ([NSCLC](../cancer_types/NSCLC.md)) treated with PD-(L)1 blockade between 2014 and 2019. The cohort integrates baseline CT [radiomics](../methods/radiomics.md), digitized PD-L1 immunohistochemistry texture features, and [MSK-IMPACT](../methods/msk-impact-panel.md) genomic data to support multimodal immunotherapy response prediction. Dataset deposited in cBioPortal as `lung_msk_mind_2020`.

## Composition

- 247 patients with advanced [NSCLC](../cancer_types/NSCLC.md) treated with PD-(L)1 blockade at MSK, 2014–2019.
- Histology: 79% adenocarcinoma ([LUAD](../cancer_types/LUAD.md)), 15% squamous ([LUSC](../cancer_types/LUSC.md)), 3% large cell, 3% NSCLC NOS.
- Response binarized as responders (CR/PR, 25%) vs. nonresponders (SD/PD, 75%) per RECIST v1.1.
- Median PFS 2.7 months (95% CI 2.5–3.0); median [OS](../cancer_types/OS.md) 11.4 months (95% CI 10.3–12.8).
- Additional hold-out cohorts: radiology validation (n = 50), pathology validation (n = 52).

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — targeted genomic sequencing; TMB median 7 mt/Mb (range 0–90)
- CT radiomics — baseline CT scan lesion segmentation and feature extraction
- PD-L1 IHC — digitized whole-slide images; texture feature extraction (IHC-G) and pathologist-scored TPS

## Papers using this cohort

- [PMID:36038778](../papers/36038778.md) — Primary analysis using DyAM multimodal ML model for PD-(L)1 blockade response prediction in advanced NSCLC.

## Notable findings derived from this cohort

- The DyAM multimodal model integrating CT radiomics, PD-L1 IHC texture features, and MSK-IMPACT genomic data achieved AUC = 0.80 (95% CI 0.74–0.86), significantly outperforming all unimodal approaches including TMB alone (AUC = 0.61) and PD-L1 TPS alone (AUC = 0.73) [PMID:36038778](../papers/36038778.md).
- [STK11](../genes/STK11.md) mutation (17.8% of cohort) and [EGFR](../genes/EGFR.md) mutation (8.9%) were independently associated with worse immunotherapy outcomes on multivariate analysis (STK11: aHR = 2.53, p < 0.005; EGFR: aHR = 2.14, p = 0.03); higher TMB was independently associated with better outcomes (aHR = 0.14, p = 0.04) [PMID:36038778](../papers/36038778.md).
- Multimodal DyAM risk stratification separated high- and low-risk patients significantly: progression at 4 months was 21% for the lowest (protective) quartile vs. 79% for the highest (risk) quartile [PMID:36038778](../papers/36038778.md).

## Sources

- cBioPortal study: `lung_msk_mind_2020`

*This page was processed by **crosslinker** on **2026-05-06**.*
