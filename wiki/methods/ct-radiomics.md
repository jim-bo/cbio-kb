---
name: CT radiomics
slug: ct-radiomics
kind: method
canonical_source: corpus
unverified: true
tags: [imaging, radiomics, ct, feature-extraction, quantitative-imaging]
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# CT radiomics

## Overview

Quantitative extraction of a large panel of mathematical features (intensity statistics, shape descriptors, textural measures, wavelet transforms) from computed tomography (CT) images of tumors. Features are computed from manually or automatically delineated regions of interest and are used to build prognostic or predictive models. CT radiomics is a specific instantiation of the broader [radiomics](../methods/radiomics.md) framework applied to CT modality. See also [radiomic-signature-4-feature](../methods/radiomic-signature-4-feature.md) for the canonical four-feature prognostic signature derived from CT radiomic features.

**Cross-reference**: [radiomics](../methods/radiomics.md) is the umbrella term for quantitative imaging-feature extraction across modalities; CT radiomics is modality-specific. For downstream statistical modeling, see [radiomic-signature-4-feature](../methods/radiomic-signature-4-feature.md).

## Used by

- [PMID:24892406](../papers/24892406.md) — 440-feature CT radiomic library extracted from pre-treatment CT scans of 1,019 NSCLC and HNSCC patients across seven cohorts; features span intensity, shape, texture (GLCM, GLRLM), and wavelet decompositions; a locked four-feature Cox model built on the Lung1 training set achieved concordance indices of 0.65–0.69 in three independent validation cohorts [PMID:24892406](../papers/24892406.md).
- [PMID:30325352](../papers/30325352.md) — CT radiomic feature extraction from 144 segmented NSCLC tumors in the [nsclc-radiogenomics-stanford](../datasets/nsclc-radiogenomics-stanford.md) dataset; CT heterogeneity in acquisition parameters (slice thickness 0.625–3 mm, kVp 80–140) reflects real-world multi-institutional variability and is flagged as a bias risk for radiomic analyses [PMID:30325352](../papers/30325352.md).
- [PMID:37397861](../papers/37397861.md) — hand-crafted CT radiomic features extracted via PyRadiomics v2.2.0 (1,316 features, max-relevance/min-redundancy selection) were used as an engineered-radiomics baseline for the RADCURE prognostic challenge; no radiomics-only model outperformed any EMR-only model, and Spearman ρ = 0.85 between the hand-crafted-feature model's predictions and tumor volume suggested these features were dominated by tumor size [PMID:37397861](../papers/37397861.md).
- [PMID:35764743](../papers/35764743.md) — 600 Coif-wavelet-transformed CT radiomic features extracted per omental lesion via PyRadiomics from pre-treatment abdominal/pelvic CT scans of 444 HGSOC patients; nine omental features survived Benjamini-Hochberg correction; the final model used a single autocorrelation feature (GLCM HLL Coif wavelet) with log(HR) = 1.68 (P < 0.01); adnexal radiomic features yielded no significant prognostic signal [PMID:35764743](../papers/35764743.md).

## Notes

- CT radiomic feature values are sensitive to acquisition and reconstruction parameters (slice thickness, kVp, reconstruction kernel, pitch); the NSCLC radiogenomics cohort deliberately did not harmonize acquisitions, posing a known reproducibility challenge [PMID:30325352](../papers/30325352.md).
- Aerts et al. demonstrated that features with higher test–retest and inter-observer stability ranks also tend to have higher prognostic performance, motivating stability-based feature pre-filtering [PMID:24892406](../papers/24892406.md).
- CT radiomics differs from [radiomics](../methods/radiomics.md) (umbrella) and [dicom-rt-struct](../methods/dicom-rt-struct.md) (the contour data format used to define extraction ROIs).

## Sources

- [PMID:24892406](../papers/24892406.md)
- [PMID:30325352](../papers/30325352.md)
- [PMID:37397861](../papers/37397861.md)
- [PMID:35764743](../papers/35764743.md)

*This page was processed by **entity-page-writer** on **2026-04-15**.*
