---
name: Esophagogastric Cancer (MSK, JCO Oncology Practice 2023)
studyId: egc_msk_2023
institution: Memorial Sloan Kettering Cancer Center
size: 1123
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [germline-seq, targeted-panel]
panels: []
tags: [esophagogastric-cancer, stad, esca, early-onset, msk-impact]
processed_by: crosslinker
processed_at: 2026-04-11
---

# Esophagogastric Cancer (MSK, JCO Oncology Practice 2023)

## Overview

Single-center retrospective cohort of 1,123 patients with esophagogastric cancer ([EGC](../cancer_types/EGC.md), [STAD](../cancer_types/STAD.md), [ESCA](../cancer_types/ESCA.md), [GEJ](../cancer_types/GEJ.md) adenocarcinoma) treated at Memorial Sloan Kettering Cancer Center between 2005 and 2018. Designed to compare clinical and molecular characteristics of early-onset (age ≤50) vs. average-onset (age >50) EGC, integrating somatic and germline sequencing data. [PMID:37699004](../papers/37699004.md)

## Composition

- 1,123 patients total: early-onset n=219 (median age 43, range 18–50); average-onset n=904 (median age 67, range 50–94). [PMID:37699004](../papers/37699004.md)
- Somatic profiling via MSK-IMPACT ([IMPACT505](../methods/IMPACT505.md)) available for 902 patients (196 early-onset, 706 average-onset). [PMID:37699004](../papers/37699004.md)
- Germline analysis using 76- to 88-gene MSK-IMPACT panel on 466 patients (116 early-onset, 350 average-onset). [PMID:37699004](../papers/37699004.md)
- Cancer types: esophageal, gastroesophageal junction, and gastric adenocarcinoma. [PMID:37699004](../papers/37699004.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) (up to 505 genes) for somatic profiling. [PMID:37699004](../papers/37699004.md)
- 76- to 88-gene MSK-IMPACT germline panel. [PMID:37699004](../papers/37699004.md)

## Papers using this cohort

- [PMID:37699004](../papers/37699004.md) — Clinical and molecular characteristics of early-onset vs average-onset esophagogastric cancer.

## Notable findings derived from this cohort

- Early-onset EGC had higher proportion of women (39% vs. 28%, P=0.002), gastric primary site (64% vs. 44%), and signet ring cell/diffuse-type histology (31% vs. 9%, P<0.0001). [PMID:37699004](../papers/37699004.md)
- Early-onset tumors had lower TMB (median 3.3 vs. 4.9 mut/Mb, P<0.001) and lower fraction genome altered (0.055 vs. 0.132). [PMID:37699004](../papers/37699004.md)
- [CCNE1](../genes/CCNE1.md) alterations enriched in early-onset (16% vs. 7%, Q=0.011); [CDH1](../genes/CDH1.md) alterations enriched in early-onset (12% vs. 6%, Q=0.03); [CDKN2A](../genes/CDKN2A.md) enriched in average-onset (22% vs. 11%). [PMID:37699004](../papers/37699004.md)
- Multivariable analysis: [CDKN2A](../genes/CDKN2A.md) alterations associated with worse survival (HR=1.55, P<0.001); [ERBB2](../genes/ERBB2.md) associated with improved survival (HR=0.65, P=0.01). [PMID:37699004](../papers/37699004.md)

## Sources

- cBioPortal study `egc_msk_2023` [PMID:37699004](../papers/37699004.md).

*This page was processed by **crosslinker** on **2026-04-11**.*
