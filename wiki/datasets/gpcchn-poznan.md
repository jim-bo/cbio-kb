---
name: Greater Poland Cancer Centre HNSCC Cohort (Poznań)
studyId: gpcchn-poznan
institution: Greater Poland Cancer Centre, Poznań, Poland
size: 298
reference_genome: N/A
canonical_source: corpus
unverified: true
assays:
  - ct-imaging
panels: []
tags:
  - hnscc
  - head-and-neck
  - radiomics
  - validation-cohort
  - private-dataset
processed_by: crosslinker
processed_at: 2026-04-16
---

# Greater Poland Cancer Centre HNSCC Cohort (Poznań)

## Overview

A private institutional cohort of 298 head and neck squamous cell carcinoma ([HNSC](../cancer_types/HNSC.md)) patients treated with definitive radiotherapy or chemoradiotherapy at the Greater Poland Cancer Centre in Poznań, Poland. This dataset is not publicly available on TCIA or cBioPortal and was used as an in-house external validation cohort in the HNSC prognostic modeling challenge. [PMID:37397861](../papers/37397861.md)

## Composition

- Cancer type: [HNSC](../cancer_types/HNSC.md), n=298.
- Notably HPV-negative enriched relative to the [RADCURE](../datasets/radcure.md) training cohort; distribution shifts in disease site, HPV status, and outcome prevalence were statistically significant (pairwise χ² FDR ≤ 5%) versus RADCURE. [PMID:37397861](../papers/37397861.md)
- No TCIA URL or cBioPortal studyId; no public access described in the paper.

## Assays / panels (linked)

- Pretreatment CT imaging (planning CT with GTV contours).

## Papers using this cohort

- [PMID:37397861](../papers/37397861.md) — Kim et al. 2023, *Radiotherapy and Oncology*: GPCCHN used as one of three external validation cohorts (GPCCHN, HN1, MDACC) in the HNSC multi-institutional prognostic challenge; validated in-house at Greater Poland Cancer Centre.

## Notable findings derived from this cohort

- Model ranking shifted on GPCCHN: the top combined model ([MTLR](../methods/mtlr.md) + EMR + volume, Model 1) was outperformed by the simpler linear EMR + volume model (Model 2), potentially attributed to the higher proportion of HPV-negative patients. [PMID:37397861](../papers/37397861.md)
- Overall model performance dropped relative to the RADCURE internal test set (still significantly better than random, p < 0.0001). [PMID:37397861](../papers/37397861.md)

## Sources

- [PMID:37397861](../papers/37397861.md) — Kim et al. 2023, *Radiotherapy and Oncology*.

*This page was processed by **crosslinker** on **2026-04-16**.*
