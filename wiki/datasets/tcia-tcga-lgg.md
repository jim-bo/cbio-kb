---
name: TCIA TCGA-LGG MRI Collection
studyId: tcia-tcga-lgg
institution: Multiple (5 TCGA-contributing institutions)
size: 108
reference_genome: N/A
canonical_source: corpus
unverified: true
assays:
  - mri-imaging
panels: []
tags:
  - lower-grade-glioma
  - lgg
  - glioma
  - tcia
  - mri
  - segmentation
  - radiomics
  - tcga
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# TCIA TCGA-LGG MRI Collection

## Overview

The TCIA TCGA-LGG collection provides pre-operative multi-parametric MRI scans for 108 lower-grade diffuse glioma ([DIFG](../cancer_types/DIFG.md)) patients drawn from the TCGA-LGG cohort (originating set n=199 from 5 institutions). Bakas et al. 2017 released expert-revised tumour segmentation labels (whole tumour, tumour core, enhancing/non-enhancing tumour) and >700 extracted radiomic features for these cases. The molecular and genomic counterpart is the cBioPortal study [lgg_tcga](../datasets/lgg_tcga.md). [PMID:28872634](../papers/28872634.md)

## Composition

- **Cancer type**: lower-grade diffuse glioma ([DIFG](../cancer_types/DIFG.md)), n=108 (from originating set of 199).
- **Modality**: multi-parametric MRI — T1, T1-Gd (post-contrast), T2, T2-FLAIR; retrospective standard-of-care acquisitions from GE, Siemens, Philips, and Hitachi scanners at field strengths 0.5–3 T.
- **Pre-processing**: identical pipeline to TCGA-GBM — re-orientation to LPS, affine co-registration via FSL FLIRT, 1 mm³ resampling, skull-stripping with BET.
- **Annotations**: expert-revised segmentation labels; LGG cases without an apparent enhancing tumour region were labelled as non-enhancing tumour (NET) only or NET+oedema, reflecting the lower blood-brain-barrier disruption typical of low-grade glioma biology. [PMID:28872634](../papers/28872634.md)

## Assays / panels (linked)

- [Volumetric MRI segmentation](../methods/volumetric-mri-segmentation.md) — expert-revised sub-region labels.
- [GLISTRboost](../methods/glistrboost.md) — automated segmentation baseline.
- [CaPTk](../methods/captk.md) — radiomic feature extraction.

## Papers using this cohort

- [PMID:28872634](../papers/28872634.md) — Bakas et al. 2017, *Scientific Data*: primary data resource paper; releases expert-revised MRI segmentation labels and >700 radiomic features for 108 TCGA-LGG cases.

## Notable findings derived from this cohort

- N=44 LGG cases overlap with BraTS'15 training set; N=15 with BraTS'15 testing set. The revised labels became the BraTS'17 reference standard. [PMID:28872634](../papers/28872634.md)
- LGG cases without apparent enhancing tumour are annotated as NET-only or NET+oedema, creating a biologically grounded labelling scheme distinct from the GBM annotation protocol. [PMID:28872634](../papers/28872634.md)

## Sources

- TCIA collection: TCGA-LGG — https://www.cancerimagingarchive.net/collection/tcga-lgg/
- cBioPortal genomic counterpart: [lgg_tcga](../datasets/lgg_tcga.md)
- [PMID:28872634](../papers/28872634.md) — Bakas et al. 2017, *Scientific Data*, DOI 10.1038/sdata.2017.117.

*This page was processed by **entity-page-writer** on **2026-04-15**.*
