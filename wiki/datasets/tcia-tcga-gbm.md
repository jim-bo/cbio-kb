---
name: TCIA TCGA-GBM MRI Collection
studyId: tcia-tcga-gbm
institution: Multiple (8 TCGA-contributing institutions)
size: 135
reference_genome: N/A
canonical_source: corpus
unverified: true
assays:
  - mri-imaging
panels: []
tags:
  - glioblastoma
  - gbm
  - glioma
  - tcia
  - mri
  - segmentation
  - radiomics
  - tcga
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# TCIA TCGA-GBM MRI Collection

## Overview

The TCIA TCGA-GBM collection provides pre-operative multi-parametric MRI scans for 135 glioblastoma multiforme ([GB](../cancer_types/GB.md)) patients drawn from the TCGA-GBM cohort (originating set n=262 from 8 institutions). Bakas et al. 2017 released expert-revised tumour segmentation labels (whole tumour, tumour core, enhancing tumour) and >700 extracted radiomic features for these cases. The molecular and genomic counterpart is the cBioPortal study [gbm_tcga](../datasets/gbm_tcga.md). [PMID:28872634](../papers/28872634.md)

## Composition

- **Cancer type**: glioblastoma multiforme ([GB](../cancer_types/GB.md)), n=135 (from originating set of 262).
- **Modality**: multi-parametric MRI — T1, T1-Gd (post-contrast), T2, T2-FLAIR; retrospective standard-of-care acquisitions from GE, Siemens, Philips, and Hitachi scanners at field strengths 0.5–3 T.
- **Pre-processing**: re-orientation to LPS, affine co-registration to T1 template via FSL FLIRT, resampling to 1 mm³, skull-stripping with BET, SUSAN smoothing.
- **Annotations**: expert-revised segmentation labels generated using [GLISTRboost](../methods/glistrboost.md) then manually corrected; labels cover whole tumour (WT), tumour core (TC), and enhancing tumour (ET) sub-regions. [PMID:28872634](../papers/28872634.md)

## Assays / panels (linked)

- [Volumetric MRI segmentation](../methods/volumetric-mri-segmentation.md) — expert-revised sub-region labels (WT/TC/ET).
- [GLISTRboost](../methods/glistrboost.md) — hybrid generative-discriminative automated segmentation.
- [CaPTk](../methods/captk.md) — radiomic feature extraction.

## Papers using this cohort

- [PMID:28872634](../papers/28872634.md) — Bakas et al. 2017, *Scientific Data*: primary data resource paper; releases expert-revised MRI segmentation labels and >700 radiomic features for 135 TCGA-GBM cases; labels became the BraTS'17 reference standard.

## Notable findings derived from this cohort

- Expert-revised labels vs. GLISTRboost automated labels: median DICE 0.92 (WT), 0.88 (TC), 0.88 (ET); median Jaccard 0.96 (WT), 0.87 (TC), 0.86 (ET) — manual revision most impacted core/enhancing sub-regions. [PMID:28872634](../papers/28872634.md)
- 95th-percentile Hausdorff distances: 3.61 mm (WT), 4.06 mm (TC), 2.00 mm (ET). [PMID:28872634](../papers/28872634.md)
- N=200 GBM cases overlap with BraTS'15 training set; N=23 with BraTS'15 testing set. The revised labels became the BraTS'17 reference standard. [PMID:28872634](../papers/28872634.md)

## Sources

- TCIA collection: TCGA-GBM — https://www.cancerimagingarchive.net/collection/tcga-gbm/
- cBioPortal genomic counterpart: [gbm_tcga](../datasets/gbm_tcga.md)
- [PMID:28872634](../papers/28872634.md) — Bakas et al. 2017, *Scientific Data*, DOI 10.1038/sdata.2017.117.

*This page was processed by **entity-page-writer** on **2026-04-15**.*
