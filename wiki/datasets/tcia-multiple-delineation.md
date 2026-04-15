---
name: TCIA Multiple Delineation (Inter-Observer)
studyId: tcia-multiple-delineation
institution: Multiple (MAASTRO Clinic led)
size: 21
reference_genome: N/A
canonical_source: corpus
unverified: true
assays:
  - ct-imaging
panels: []
tags:
  - nsclc
  - radiomics
  - tcia
  - ct
  - inter-observer
  - stability
  - delineation
processed_by: entity-page-writer
processed_at: 2026-04-15
processed_by: crosslinker
---

# TCIA Multiple Delineation (Inter-Observer)

## Overview

The Multiple Delineation collection comprises 21 [NSCLC](../cancer_types/NSCLC.md) patients each delineated independently by five radiation oncologists. It was used by Aerts et al. 2014 to quantify inter-observer variability in the CT radiomic feature library and to identify stable features robust to delineation uncertainty. The dataset is hosted on TCIA. [PMID:24892406](../papers/24892406.md)

## Composition

- **Cancer type**: [NSCLC](../cancer_types/NSCLC.md), n=21 patients × 5 delineations each.
- **Modality**: CT; manual tumour delineations by five independent radiation oncologists per patient.
- **Purpose**: inter-observer reproducibility assessment of radiomic features.
- **Role in Aerts 2014**: stability sub-study; features with high inter-observer stability ranks tend to also have higher prognostic performance. [PMID:24892406](../papers/24892406.md)

## Assays / panels (linked)

- [CT radiomics](../methods/ct-radiomics.md) — 440-feature library inter-observer variability evaluation.

## Papers using this cohort

- [PMID:24892406](../papers/24892406.md) — Aerts et al. 2014, *Nature Communications*: Multiple Delineation used to quantify radiomic feature stability across delineators, complementing RIDER test-retest reproducibility.

## Notable findings derived from this cohort

- Features with higher inter-observer stability ranks tended to also have higher prognostic performance in validation cohorts, supporting delineation-robust feature selection. [PMID:24892406](../papers/24892406.md)

## Sources

- TCIA collection: NSCLC-Radiomics — https://www.cancerimagingarchive.net/collection/nsclc-radiomics/
- [PMID:24892406](../papers/24892406.md) — Aerts et al. 2014, *Nature Communications*, DOI 10.1038/ncomms5006.

*This page was processed by **crosslinker** on **2026-04-15**.*
