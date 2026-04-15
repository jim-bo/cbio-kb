---
name: GLISTRboost
slug: glistrboost
kind: method
canonical_source: corpus
unverified: true
tags: [imaging, mri, segmentation, glioma, brain-tumor, deep-learning]
processed_by: entity-page-writer
processed_at: 2026-04-15
processed_by: crosslinker
---

# GLISTRboost

## Overview

GLISTRboost is a hybrid generative-discriminative brain tumor MRI segmentation algorithm that won the [BraTS](../methods/brats-challenge.md)'15 challenge. It combines a generative probabilistic tumor growth model (GLISTR) with a discriminative gradient-boosting classifier to delineate three tumor sub-regions from multi-parametric MRI: enhancing tumor (ET), non-enhancing tumor core (NET), and peritumoral edema (ED). Input modalities are T1, T1-Gd (post-contrast), T2, and T2-FLAIR. GLISTRboost is used to generate initial automated segmentation labels that are then refined by expert annotators for large-scale imaging data releases. See also [brats-challenge](../methods/brats-challenge.md) for the benchmark framework and [captk](../methods/captk.md) for the software toolkit used alongside GLISTRboost for feature extraction.

## Used by

- [PMID:28872634](../papers/28872634.md) — GLISTRboost used to generate initial tumor sub-region labels (ET, NET, ED) for 243 pre-operative mMRI scans (TCGA-GBM n=135, TCGA-LGG n=108); automated labels were then manually revised by a board-certified neuroradiologist; median DICE on BraTS'15 GBM training set was 0.92 (whole tumor), 0.88 (tumor core), 0.88 (enhancing tumor); median Jaccard agreement between automated and final manually-revised labels was 0.96 (whole tumor), 0.87 (tumor core), 0.86 (enhancing tumor) [PMID:28872634](../papers/28872634.md).

## Notes

- Manual revision impacted the core/enhancing-tumor labels substantially more than the whole-tumor extent, reflecting the higher segmentation uncertainty in ET and NET boundaries [PMID:28872634](../papers/28872634.md).
- The GLISTRboost-generated labels, after manual revision, became the reference labels used in the BraTS'17 challenge [PMID:28872634](../papers/28872634.md).
- Ambiguous regions at the NET/ED boundary were left as automated labels without manual correction, introducing a known noise floor in fine-grained sub-region labels [PMID:28872634](../papers/28872634.md).

## Sources

- [PMID:28872634](../papers/28872634.md)

*This page was processed by **crosslinker** on **2026-04-15**.*
