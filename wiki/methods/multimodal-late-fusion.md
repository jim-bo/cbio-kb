---
name: Multimodal Late Fusion
slug: multimodal-late-fusion
kind: method
canonical_source: corpus
unverified: true
tags: [multimodal, fusion, machine-learning, survival-analysis, computational-pathology, radiomics, genomics]
processed_by: crosslinker
processed_at: 2026-04-16
---

# Multimodal Late Fusion

## Overview

Multimodal late fusion is a machine-learning architecture in which separate unimodal submodels are first trained independently on each data modality (e.g., CT radiomics, histopathology, genomics, clinical variables), and then the outputs (risk scores or embeddings) of each trained submodel are combined by a final integrator model. This contrasts with early fusion (concatenating raw feature vectors before any modeling) and intermediate/joint fusion (coupling modalities within a shared latent space). Late fusion is particularly tolerant of missing-modality patients: unimodal submodels can be trained on all patients with data for that modality, while the integrator is fit only on patients with data for multiple modalities. The final integrator is typically a linear model (Cox proportional hazards, logistic regression) applied to the stacked unimodal risk scores.

## Used by

- [PMID:35764743](../papers/35764743.md) — two-stage Cox late-fusion scheme applied to 444 [HGSOC](../cancer_types/HGSOC.md) patients: unimodal Cox submodels trained separately on omental CT radiomics (n=245), H&E nuclear morphometry (n=243), and genomic HRD features (n=296); final Cox integrator fit on the patient intersection; the radiomic+histopathological (RH) model reached test concordance c = 0.62 (95% CI 0.604–0.638) and the genomic+radiomic+histopathological (GRH) model c = 0.61 (95% CI 0.594–0.625) — both significantly better than any unimodal model and HRD alone (c = 0.52) by 1000-fold permutation test; Kendall rank correlation between any pair of unimodal risk scores was < 0.14, confirming orthogonal prognostic information across modalities [PMID:35764743](../papers/35764743.md).

## Notes

- Late fusion's missing-data tolerance was a primary motivation in the [HGSOC](../cancer_types/HGSOC.md) study: restricting training to the 114 patients with complete data across all four modalities markedly degraded test performance relative to the full late-fusion model.
- In the [RADCURE](../datasets/radcure.md) [HNSC](../cancer_types/HNSC.md) challenge, all deep-learning submissions used a simpler late-concatenation approach (EMR features + image embeddings concatenated at the final layer), which the authors flag as a potential reason why image and EMR features appeared non-complementary; they suggest joint latent-space approaches as future work.
- Late fusion does not learn cross-modal interactions within the submodel training phase; gating or attention mechanisms that weight modalities per patient require larger cohorts and were not feasible with n=114 complete cases.
- The architecture is generalizable: the same recipe (independent Cox submodels + linear integrator) has been applied to radiology+pathology+genomics+clinical data in multiple cancer types.

## Sources

- [PMID:35764743](../papers/35764743.md)

*This page was processed by **crosslinker** on **2026-04-16**.*
