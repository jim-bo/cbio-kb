---
name: TCIA RIDER Lung CT (Test-Retest)
studyId: tcia-rider-lung
institution: Multiple (RIDER consortium)
size: 31
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
  - test-retest
  - stability
  - rider
processed_by: entity-page-writer
processed_at: 2026-04-15
processed_by: crosslinker
---

# TCIA RIDER Lung CT (Test-Retest)

## Overview

The RIDER Lung CT collection is a test-retest stability dataset comprising 31 [NSCLC](../cancer_types/NSCLC.md) patients who underwent two CT scans approximately 15 minutes apart under identical conditions. It was used by Aerts et al. 2014 to assess the reproducibility of the 440-feature CT radiomic library and to identify features suitable for stable prognostic modelling. The dataset is hosted on TCIA by the Reference Image Database to Evaluate Therapy Response (RIDER) consortium. [PMID:24892406](../papers/24892406.md)

## Composition

- **Cancer type**: [NSCLC](../cancer_types/NSCLC.md), n=31.
- **Modality**: CT; two acquisitions ~15 minutes apart per patient.
- **Purpose**: feature-level test-retest reproducibility assessment.
- **Role in Aerts 2014**: stability sub-study; features with high test-retest stability ranks tend to also have higher prognostic performance, supporting stability-based feature pre-filtering. [PMID:24892406](../papers/24892406.md)

## Assays / panels (linked)

- [CT radiomics](../methods/ct-radiomics.md) — 440-feature library reproducibility evaluation.

## Papers using this cohort

- [PMID:24892406](../papers/24892406.md) — Aerts et al. 2014, *Nature Communications*: RIDER used to quantify test-retest radiomic feature stability as a principled prefilter for prognostic feature selection.

## Notable findings derived from this cohort

- Features with higher test-retest stability ranks in RIDER also tended to have higher prognostic performance in validation cohorts, validating stability-based feature selection as an anti-overfitting prefilter. [PMID:24892406](../papers/24892406.md)

## Sources

- TCIA collection: RIDER Lung CT — https://www.cancerimagingarchive.net/collection/rider-lung-ct/
- [PMID:24892406](../papers/24892406.md) — Aerts et al. 2014, *Nature Communications*, DOI 10.1038/ncomms5006.

*This page was processed by **crosslinker** on **2026-04-15**.*
