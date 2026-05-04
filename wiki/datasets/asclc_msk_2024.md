---
name: Atypical Small Cell Lung Carcinoma MSK 2024
studyId: asclc_msk_2024
institution: Memorial Sloan Kettering Cancer Center
size: 20
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - msk-impact-panel
  - whole-genome-seq
  - rna-seq
  - fish
panels:
  - msk-impact-panel
tags:
  - small-cell-lung-cancer
  - never-smokers
  - chromothripsis
  - ecdna
  - neuroendocrine
processed_by: crosslinker
processed_at: 2026-05-03
---

# Atypical Small Cell Lung Carcinoma MSK 2024

## Overview

The asclc_msk_2024 dataset is a single-institution prospective cohort of 20 patients with atypical small cell lung carcinoma (aSCLC) identified at Memorial Sloan Kettering Cancer Center (MSKCC). aSCLC is defined by retained wild-type [[[RB1](../genes/RB1.md)]] and [[[TP53](../genes/TP53.md)]] and arises almost exclusively in never/light smokers (≤10 pack-years). Cases were identified from a consecutive series of 600 de novo [SCLC](../cancer_types/SCLC.md) patients profiled by [[MSK-IMPACT|[msk-impact-panel](../methods/msk-impact-panel.md)]], making aSCLC 3% of the overall SCLC cohort. The dataset was assembled and reported by Rekhtman et al. (Cancer Discovery, 2025) [PMID:39185963](../papers/39185963.md).

## Composition

- **20 patients** with aSCLC ([[RB1]]+/[[TP53]]+, never/light smokers ≤10 pack-years); all female or non-male-assigned-at-birth patients were not specified, but the cohort is younger than typical SCLC (mean age 53 vs. 67 yr; P < 0.0001). [PMID:39185963](../papers/39185963.md)
- Identified from 600 consecutive de novo SCLC patients; comparator cohorts include smoking-associated SCLC (sSCLC, n = 206), pulmonary carcinoids (n = 157), never-smoker RB1−/TP53− SCLC (n = 18), and atypical carcinoids (n = 50). [PMID:39185963](../papers/39185963.md)
- **Cancer types:** [[SCLC]] (primary), with evidence of progression from [[[LNET](../cancer_types/LNET.md)]] (pulmonary carcinoid) in a subset; comparator cohort includes [[[LUAD](../cancer_types/LUAD.md)]]-to-SCLC transformations. [PMID:39185963](../papers/39185963.md)
- **Key clinical fields:** pack-year history, Ki67, overall survival, treatment response (platinum-based chemotherapy, [temozolomide](../drugs/temozolomide.md), immune checkpoint inhibitors). [PMID:39185963](../papers/39185963.md)
- 49 pathology specimens (1–7 per patient); serial samples enabled multisample and temporal analyses. [PMID:39185963](../papers/39185963.md)

## Assays / panels (linked)

- [[MSK-IMPACT|msk-impact-panel]] targeted NGS on all 20 patients (mean 613× coverage). [PMID:39185963](../papers/39185963.md)
- [[[whole-genome-seq](../methods/whole-genome-seq.md)]] on 12 samples from 11 patients. [PMID:39185963](../papers/39185963.md)
- [[[rna-seq](../methods/rna-seq.md)]] on 7 samples. [PMID:39185963](../papers/39185963.md)
- [[[fish](../methods/fish.md)]] for [[[CCND1](../genes/CCND1.md)]] and [[[CCND2](../genes/CCND2.md)]]/[[[CDK4](../genes/CDK4.md)]]/[[[MDM2](../genes/MDM2.md)]] in 5 cases; confirmed extrachromosomal ("double-minute") amplification. [PMID:39185963](../papers/39185963.md)
- Copy-number segmentation by [[FACETS|[facets](../methods/facets.md)]]; mutational-signature analysis ([[[sigma-mutational-signatures](../methods/sigma-mutational-signatures.md)]]); IHC for pRb, p53, p16, neuroendocrine markers, OTP, and transcriptional-subtype markers. [PMID:39185963](../papers/39185963.md)

## Papers using this cohort

- [PMID:39185963](../papers/39185963.md) — Rekhtman et al. "Chromothripsis-Mediated Small Cell Lung Carcinoma." Cancer Discovery (2025).

## Notable findings derived from this cohort

- 16/19 (84%) non-MSI aSCLC cases harbored extensive chromothripsis, most often on chromosome 11 or 12, producing ecDNA amplification of [[CCND1]] (30%, up to 125 copies), co-amplification of [[CCND2]]/[[CDK4]]/[[MDM2]] (15%), or [[[MYCL](../genes/MYCL.md)]] amplification (10%). [PMID:39185963](../papers/39185963.md)
- Carcinoid-associated mutations are enriched: [[[ATM](../genes/ATM.md)]] 30%, [[[ARID1A](../genes/ARID1A.md)]] 25%, [[[MEN1](../genes/MEN1.md)]] 15%, [[[EIF1AX](../genes/EIF1AX.md)]] 10%; 55% of cases showed at least one line of evidence for a histogenetic link to pulmonary carcinoids ([[LNET]]). [PMID:39185963](../papers/39185963.md)
- aSCLC has intermediate overall survival (median 58 months) between smoking-associated SCLC (16 months) and atypical carcinoids (184 months); platinum-based chemotherapy ORR is only 33% (vs. ~70% historical for conventional SCLC). [PMID:39185963](../papers/39185963.md)
- [[[DLL3](../genes/DLL3.md)]] and [[[SEZ6](../genes/SEZ6.md)]] are uniformly highly expressed (mean H-scores 278 and 240, respectively) in all 9 evaluable cases, positioning aSCLC as a candidate for DLL3- and SEZ6-targeted therapy. [PMID:39185963](../papers/39185963.md)
- Chromothripsis events are clonally stable across primary and metastatic samples and pre/post-therapy time points; MutationTimeR placed amplifications early in tumorigenesis. [PMID:39185963](../papers/39185963.md)
- TMB is low (<2 mut/Mb) in most cases; the APOBEC signature absent, distinguishing aSCLC from EGFR-driven never-smoker SCLC. [PMID:39185963](../papers/39185963.md)

## Sources

- Rekhtman N et al. "Chromothripsis-Mediated Small Cell Lung Carcinoma." Cancer Discovery (2025). [PMID:39185963](../papers/39185963.md)

*This page was processed by **crosslinker** on **2026-05-03**.*
