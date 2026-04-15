---
name: MTLR (Multi-Task Logistic Regression)
slug: mtlr
kind: method
canonical_source: corpus
unverified: true
tags: [survival-analysis, prognostic-model, logistic-regression, multitask-learning, machine-learning]
processed_by: crosslinker
processed_at: 2026-04-16
---

# MTLR (Multi-Task Logistic Regression)

## Overview

Multi-Task Logistic Regression (MTLR), introduced by Yu et al., is a survival-prediction framework that discretizes the time axis into intervals and fits a sequence of dependent logistic regression models — one per interval — in a shared multitask learning objective. This yields a full predicted survival curve per patient (not just a single risk score or time-to-event point estimate), enabling both ranking of patients by risk and calibrated probability estimates at any time horizon. The multitask formulation encourages smoothness of the survival curve across adjacent intervals. MTLR can be extended with nonlinear feature transformations (e.g., a shallow neural network with ELU activations feeding into the MTLR head) to capture interactions among input features.

## Used by

- [PMID:37397861](../papers/37397861.md) — MTLR was the backbone of the top-performing model in the [RADCURE](../datasets/radcure.md) prognostic challenge for [HNSC](../cancer_types/HNSC.md) (n=2,552 training, n=750 internal test, n=873 external validation); the winning model combined MTLR with a single hidden layer of ELU-activated neurons fit on EMR features (age, sex, T/N/overall stage, disease site, performance status, HPV status, radiation dose, systemic-therapy use) and primary tumor volume; it achieved AUROC = 0.823, AP = 0.505, C-index = 0.801 on the internal test set — outperforming all deep-learning CT radiomics submissions and all simpler baselines (FDR < 5%); full survival curves enabled patient stratification with HR = 8.64 at the 0.5 risk threshold (p < 10⁻¹⁸) [PMID:37397861](../papers/37397861.md).

## Notes

- MTLR differs from standard Cox proportional hazards in that it does not assume proportional hazards and directly outputs calibrated survival probabilities at each discretized time interval.
- The multitask objective couples adjacent time intervals, providing implicit regularization and ensuring the predicted survival curve is monotonically non-increasing when the intervals are properly ordered.
- In the [RADCURE](../datasets/radcure.md) challenge, replacing tumor volume in the MTLR model with deep image embeddings from a 3D ConvNet degraded AUROC from 0.823 to 0.766, indicating that volume carried more prognostic signal than learned radiomics in this [HNSC](../cancer_types/HNSC.md) setting.
- The clinical utility of MTLR's full survival curves (vs. single risk scores) is that they support individualized time-to-event counseling and dynamic risk re-assessment.

## Sources

- [PMID:37397861](../papers/37397861.md)

*This page was processed by **crosslinker** on **2026-04-16**.*
