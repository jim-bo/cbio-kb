---
name: BraTS Challenge (Brain Tumor Segmentation)
slug: brats-challenge
kind: method
canonical_source: corpus
unverified: true
tags: [imaging, mri, segmentation, glioma, brain-tumor, benchmark, challenge]
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# BraTS Challenge (Brain Tumor Segmentation)

## Overview

The Brain Tumor Segmentation (BraTS) Challenge is an annual international benchmarking competition and community standard for automated multi-parametric MRI glioma segmentation. Participating algorithms are evaluated on their ability to delineate three tumor sub-regions — enhancing tumor (ET), non-enhancing tumor core (NET/TC), and peritumoral edema (ED/WT) — from T1, T1-Gd, T2, and T2-FLAIR MRI volumes, using DICE overlap and Hausdorff distance as primary metrics. BraTS provides standardized data, pre-processing pipelines, and evaluation protocols that serve as a community reference for developing and comparing segmentation methods including [GLISTRboost](../methods/glistrboost.md). Data from TCGA-GBM and TCGA-LGG glioma imaging collections are used as the benchmark dataset.

## Used by

- [PMID:28872634](../papers/28872634.md) — 200 GBM and 44 LGG cases from TCGA-GBM/TCGA-LGG overlap with the BraTS'15 training set; 23 GBM and 15 LGG cases overlap with the BraTS'15 testing set; GLISTRboost was the BraTS'15 winning segmentation algorithm; the manually revised labels from Bakas et al. became the reference labels for BraTS'17; median DICE on BraTS'15 GBM training set was 0.92 (whole tumor), 0.88 (tumor core), 0.88 (enhancing tumor) [PMID:28872634](../papers/28872634.md).

## Notes

- BraTS'17 used the manually revised labels from PMID:28872634 as its ground truth, making that paper directly foundational to the benchmark series [PMID:28872634](../papers/28872634.md).
- Quantitative BraTS'15 test-set performance for GLISTRboost was withheld by challenge organizers at time of Bakas et al. publication; reported DICE/Hausdorff numbers are cross-validated training-set estimates only [PMID:28872634](../papers/28872634.md).
- BraTS has evolved over successive years (BraTS'15 through BraTS'24+), expanding to adult and pediatric glioma sub-challenges and incorporating additional imaging features.

## Sources

- [PMID:28872634](../papers/28872634.md)

*This page was processed by **entity-page-writer** on **2026-04-15**.*
