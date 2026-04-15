---
name: TCIA NSCLC-Radiomics Lung1 (MAASTRO)
studyId: tcia-nsclc-radiomics-lung1
institution: MAASTRO Clinic, Maastricht, Netherlands
size: 422
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
  - training-cohort
processed_by: entity-page-writer
processed_at: 2026-04-15
processed_by: crosslinker
---

# TCIA NSCLC-Radiomics Lung1 (MAASTRO)

## Overview

The Lung1 collection is the primary training cohort used by Aerts et al. 2014 to derive a 440-feature CT radiomic library and a four-feature prognostic radiomic signature in non-small cell lung cancer. It comprises 422 NSCLC patients treated with curative-intent radiotherapy at MAASTRO Clinic (Maastricht, Netherlands). CT scans, manual tumour delineations, clinical metadata, and survival data are publicly available on The Cancer Imaging Archive (TCIA) under the collection name NSCLC-Radiomics. [PMID:24892406](../papers/24892406.md)

## Composition

- **Cancer type**: [NSCLC](../cancer_types/NSCLC.md) (non-small cell lung cancer), n=422.
- **Modality**: CT (computed tomography); free-breathing acquisition.
- **Annotations**: manual tumour delineations per treating radiation oncologist.
- **Clinical data**: treatment records, clinical staging, and overall survival.
- **Role in Aerts 2014**: sole training cohort for the 440-feature [radiomics](../methods/radiomics.md) pipeline and the locked four-feature Cox signature. [PMID:24892406](../papers/24892406.md)

## Assays / panels (linked)

- [CT radiomics](../methods/ct-radiomics.md) — 440-feature library computed from manual tumour delineations.

## Papers using this cohort

- [PMID:24892406](../papers/24892406.md) — Aerts et al. 2014, *Nature Communications*: Lung1 training cohort for the four-feature radiomic prognostic signature validated across five NSCLC/HNSCC cohorts.

## Notable findings derived from this cohort

- Unsupervised radiomic clustering of Lung1 (n=422) yielded three clusters significantly associated with primary T-stage (P < 1 × 10⁻²⁰), overall stage (P=3.4 × 10⁻³), and histology (P=0.019, squamous over-represented in cluster II); no association with N-stage or M-stage. [PMID:24892406](../papers/24892406.md)
- The four-feature radiomic signature trained on Lung1 (Statistics Energy, Shape Compactness, Grey Level Nonuniformity, wavelet Grey Level Nonuniformity HLH) generalised to four independent validation cohorts without retraining, achieving concordance indices of 0.65–0.69. [PMID:24892406](../papers/24892406.md)

## Sources

- TCIA collection: NSCLC-Radiomics — https://www.cancerimagingarchive.net/collection/nsclc-radiomics/
- [PMID:24892406](../papers/24892406.md) — Aerts et al. 2014, *Nature Communications*, DOI 10.1038/ncomms5006.

*This page was processed by **crosslinker** on **2026-04-15**.*
