---
name: Cancer Imaging Phenomics Toolkit (CaPTk)
slug: captk
kind: method
canonical_source: corpus
unverified: true
tags: [imaging, mri, radiomics, software, feature-extraction, brain-tumor]
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# Cancer Imaging Phenomics Toolkit (CaPTk)

## Overview

CaPTk (Cancer Imaging Phenomics Toolkit) is an open-source software platform developed at the Center for Biomedical Image Computing and Analytics (CBICA) at the University of Pennsylvania. It provides a graphical and command-line interface for neuroimaging analysis, including seed-point initialization for tumor segmentation, volumetric radiomic feature extraction, and pre-processing pipelines. CaPTk is tightly integrated with [GLISTRboost](../methods/glistrboost.md) and the [BraTS challenge](../methods/brats-challenge.md) ecosystem. Its radiomic feature extraction module generates >700 features from tumor sub-region labels across intensity, volumetric, morphologic, histogram, textural (GLCM/GLRLM/GLSZM/NGTDM), and wavelet domains.

## Used by

- [PMID:28872634](../papers/28872634.md) — CaPTk used for seed-point initialization of the GLISTRboost segmentation pipeline and for volumetric radiomic feature extraction (>700 features) from the manually revised tumor sub-region labels of 243 pre-operative glioma MRI scans (TCGA-GBM n=135, TCGA-LGG n=108); radiomic features extracted from ET, NET, and ED regions in 3D [PMID:28872634](../papers/28872634.md).

## Notes

- CaPTk is available at https://www.cbica.upenn.edu/captk; it is actively developed and has expanded beyond glioma segmentation to include other brain tumor and multi-cancer applications since the Bakas et al. 2017 paper.
- The >700 radiomic features extracted by CaPTk in Bakas et al. are explicitly described as hypothesis-generating; their individual biological significance is not established [PMID:28872634](../papers/28872634.md).

## Sources

- [PMID:28872634](../papers/28872634.md)

*This page was processed by **entity-page-writer** on **2026-04-15**.*
