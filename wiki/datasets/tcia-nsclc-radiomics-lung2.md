---
name: TCIA NSCLC-Radiomics Lung2 (Radboud)
studyId: tcia-nsclc-radiomics-lung2
institution: Radboud University Medical Center, Nijmegen, Netherlands
size: 225
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
  - lung
  - validation-cohort
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# TCIA NSCLC-Radiomics Lung2 (Radboud)

## Overview

The Lung2 collection is an independent NSCLC validation cohort assembled at Radboud University Medical Center (Nijmegen, Netherlands). It was used by Aerts et al. 2014 as the primary external validation set for the four-feature radiomic prognostic signature trained on Lung1. The dataset comprises 225 NSCLC patients with CT scans, manual delineations, and survival data. [PMID:24892406](../papers/24892406.md)

## Composition

- **Cancer type**: [NSCLC](../cancer_types/NSCLC.md), n=225.
- **Modality**: CT; free-breathing acquisition.
- **Annotations**: manual tumour delineations.
- **Clinical data**: treatment records and overall survival.
- **Role in Aerts 2014**: first independent validation cohort for the locked four-feature radiomic signature. [PMID:24892406](../papers/24892406.md)

## Assays / panels (linked)

- [CT radiomics](../methods/ct-radiomics.md) — 440-feature library applied from Lung1-defined feature definitions.

## Papers using this cohort

- [PMID:24892406](../papers/24892406.md) — Aerts et al. 2014, *Nature Communications*: Lung2 used as primary NSCLC validation; the four-feature signature achieved concordance index 0.65 (P=2.91 × 10⁻⁹, Wilcoxon).

## Notable findings derived from this cohort

- 238 / 440 radiomic features (54%) were significantly prognostic in Lung2 at FDR 10% using Lung1-derived median thresholds applied without retraining. [PMID:24892406](../papers/24892406.md)
- The four-feature radiomic signature outperformed TNM staging in Lung2 (P significant, Wilcoxon); combining signature + TNM was significantly better than TNM alone. [PMID:24892406](../papers/24892406.md)

## Sources

- TCIA collection: NSCLC-Radiomics — https://www.cancerimagingarchive.net/collection/nsclc-radiomics/
- [PMID:24892406](../papers/24892406.md) — Aerts et al. 2014, *Nature Communications*, DOI 10.1038/ncomms5006.

*This page was processed by **entity-page-writer** on **2026-04-15**.*
