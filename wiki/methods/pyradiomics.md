---
name: PyRadiomics
slug: pyradiomics
kind: method
canonical_source: corpus
unverified: true
tags: [radiomics, feature-extraction, open-source, python, ct, mri]
processed_by: crosslinker
processed_at: 2026-04-16
---

# PyRadiomics

## Overview

PyRadiomics is an open-source Python library for extracting hand-engineered radiomic features from medical images (CT, MRI, PET). It implements the Image Biomarker Standardization Initiative (IBSI) feature definitions and computes features across multiple categories: first-order intensity statistics, shape, gray level co-occurrence matrix (GLCM), gray level run length matrix (GLRLM), gray level size zone matrix (GLSZM), neighborhood gray tone difference matrix (NGTDM), and gray level dependence matrix (GLDM). Wavelet decompositions can be applied prior to extraction to yield transformed-image feature variants. Version 2.2.0 yields approximately 1,316 features when all standard feature classes and wavelet filters are enabled.

## Used by

- [PMID:37397861](../papers/37397861.md) — PyRadiomics v2.2.0 used to extract 1,316 hand-crafted CT radiomic features from primary tumor GTV masks in the [RADCURE](../datasets/radcure.md) [HNSC](../cancer_types/HNSC.md) dataset (n=2,552); features were reduced via max-relevance/min-redundancy selection before model training; the resulting engineered-radiomics model's predictions correlated with tumor volume at Spearman ρ = 0.85, suggesting volume-dominance; no hand-crafted radiomics model outperformed any EMR-only model in the prognostic challenge [PMID:37397861](../papers/37397861.md).
- [PMID:35764743](../papers/35764743.md) — PyRadiomics used to extract 600 Coif-wavelet-transformed CT radiomic features per omental and adnexal lesion from pre-treatment abdominal/pelvic CT scans of 444 [HGSOC](../cancer_types/HGSOC.md) patients; nine omental features survived Benjamini-Hochberg correction; the final prognostic radiomic submodel used a single GLCM autocorrelation feature on the HLL Coif wavelet (log HR = 1.68, corrected P < 0.01) and achieved test c-index = 0.53 [PMID:35764743](../papers/35764743.md).

## Notes

- PyRadiomics is IBSI-compliant, making its feature values broadly comparable across implementations that follow the same standard.
- Feature stability to CT acquisition parameters (slice thickness, kVp, reconstruction kernel) varies by feature class; shape features tend to be more stable than texture features.
- Max-relevance/min-redundancy (MRMR) and univariate Cox regression followed by FDR correction are two common feature-selection strategies applied downstream of PyRadiomics extraction.
- The library is freely available at https://github.com/AIM-Harvard/pyradiomics.

## Sources

- [PMID:37397861](../papers/37397861.md)
- [PMID:35764743](../papers/35764743.md)

*This page was processed by **crosslinker** on **2026-04-16**.*
