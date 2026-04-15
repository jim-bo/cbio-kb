---
name: Radiomics
slug: radiomics
kind: method
canonical_source: corpus
unverified: true
tags: [imaging, radiomics, quantitative-imaging, feature-extraction]
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# Radiomics

## Overview

Radiomics is the high-throughput extraction of a large number of quantitative imaging features from medical images (CT, MRI, PET) with the goal of capturing tumour phenotype non-invasively. Features include intensity statistics, shape descriptors, textural measures (GLCM, GLRLM, GLSZM, NGTDM), and wavelet-domain transforms. Extracted features are used in statistical or machine-learning models for prognosis, prediction, or diagnosis.

**Cross-reference**: [ct-radiomics](../methods/ct-radiomics.md) is the CT-specific instantiation; [radiomic-signature-4-feature](../methods/radiomic-signature-4-feature.md) is the locked four-feature prognostic model from Aerts et al. (2014). For DICOM contour formats used as ROI inputs, see [dicom-rt-struct](../methods/dicom-rt-struct.md).

## Used by

- [PMID:38362943](../papers/38362943.md) — RADCURE (3346-patient HNC RT planning CT dataset) is explicitly released to support radiomics and machine-learning research in head and neck radiation oncology; organ-at-risk and gross-tumor contours in [DICOM RT-STRUCT](../methods/dicom-rt-struct.md) format serve as the segmentation substrate for downstream radiomic feature extraction [PMID:38362943](../papers/38362943.md).
- [PMID:37397861](../papers/37397861.md) — RADCURE prognostic challenge benchmarked 12 ML models for 2-year OS prediction in 2,552 HNSC patients; both hand-engineered (PyRadiomics 1,316-feature) and deep-learning CT radiomics models were evaluated, with the finding that radiomic features added no prognostic value over EMR+tumor-volume; deep CNN approaches outperformed hand-crafted radiomics but neither beat simple clinical models [PMID:37397861](../papers/37397861.md).

## Notes

- Radiomics as a field was codified by Lambin et al. (2012) and Aerts et al. (2014 [PMID:24892406](../papers/24892406.md)); the latter demonstrated cross-disease prognostic transferability of a four-feature CT radiomic signature.
- Radiomic feature values are sensitive to image acquisition and reconstruction parameters; cross-institutional standardization remains an active challenge.

## Sources

- [PMID:38362943](../papers/38362943.md)
- [PMID:37397861](../papers/37397861.md)

*This page was processed by **entity-page-writer** on **2026-04-15**.*
