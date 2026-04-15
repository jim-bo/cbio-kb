---
name: TCIA TCGA-OV CT Imaging Collection
studyId: tcia-tcga-ov
institution: The Cancer Imaging Archive / TCGA Research Network
size: 148
reference_genome: N/A
canonical_source: corpus
unverified: true
assays:
  - ct-imaging
panels: []
tags:
  - hgsoc
  - ovarian-cancer
  - tcia
  - tcga
  - ct
  - public-dataset
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# TCIA TCGA-OV CT Imaging Collection

## Overview

The TCIA TCGA-OV imaging collection pairs pre-treatment contrast-enhanced CT scans with the TCGA Ovarian Serous Cystadenocarcinoma genomic cohort ([ov_tcga](../datasets/ov_tcga.md)). The imaging data is hosted on The Cancer Imaging Archive and provides the radiology component for multimodal studies requiring paired CT + genomics in [HGSOC](../cancer_types/HGSOC.md). This is a corpus-grown slug (TCIA imaging collection); it is not a cBioPortal studyId. [PMID:35764743](../papers/35764743.md)

## Composition

- Cancer type: [HGSOC](../cancer_types/HGSOC.md), predominantly stage III/IV.
- 148 TCGA-OV patients contributed CT imaging to the Boehm et al. 2022 multimodal cohort; CT scans pulled from TCIA and paired with genomic data from cBioPortal [ov_tcga](../datasets/ov_tcga.md). [PMID:35764743](../papers/35764743.md)
- CT scans: pre-treatment contrast-enhanced abdominal/pelvic CT (median 120 kVp, 5 mm slice thickness); segmented by three fellowship-trained gynecologic radiologists using ITK-SNAP v3.8.0 for adnexal masses and omental implants. [PMID:35764743](../papers/35764743.md)

## Assays / panels (linked)

- Pre-treatment contrast-enhanced CT imaging (adnexal and omental lesion segmentation).

## Papers using this cohort

- [PMID:35764743](../papers/35764743.md) — Boehm et al. 2022, *Nature Cancer*: CT imaging from TCIA-TCGA-OV used as the radiology component for the 148 TCGA-OV patients in the multimodal HGSOC late-fusion prognostic study.

## Notable findings derived from this cohort

- Omental CT radiomics (Coif-wavelet GLCM autocorrelation, HLL wavelet) were prognostically informative (test c-index 0.53); adnexal radiomics were not significant after Benjamini–Hochberg correction. [PMID:35764743](../papers/35764743.md)
- TCGA-OV CT scans acquired on varying scanner hardware relative to MSKCC scans (GE Medical Systems); the omental radiomic feature identified as prognostic was invariant to CT vendor and segmenting radiologist. [PMID:35764743](../papers/35764743.md)

## Sources

- TCIA collection: TCGA-OV — https://www.cancerimagingarchive.net/collection/tcga-ov/
- [PMID:35764743](../papers/35764743.md) — Boehm et al. 2022, *Nature Cancer*.

*This page was processed by **entity-page-writer** on **2026-04-15**.*
