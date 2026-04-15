---
name: Four-feature radiomic signature (Aerts 2014)
slug: radiomic-signature-4-feature
kind: method
canonical_source: corpus
unverified: true
tags: [imaging, radiomics, prognostic-signature, ct, cox-model]
processed_by: entity-page-writer
processed_at: 2026-04-15
processed_by: crosslinker
---

# Four-feature radiomic signature (Aerts 2014)

## Overview

A locked four-feature Cox proportional hazards prognostic model built from [CT radiomics](../methods/ct-radiomics.md) features, derived by Aerts et al. (2014) on the [Lung1](../datasets/tcia-nsclc-radiomics-lung1.md) [NSCLC](../cancer_types/NSCLC.md) training cohort (n=422) and validated without retraining in three independent cohorts. The four features are: (I) Statistics Energy (overall CT density), (II) Shape Compactness, (III) Grey Level Nonuniformity (intratumour heterogeneity), and (IV) wavelet Grey Level Nonuniformity HLH (mid-frequency heterogeneity). Validated concordance indices ranged from 0.65 (Lung2) to 0.69 (H&N1, H&N2). The signature is the canonical example of cross-cancer-type transferability of a radiomic prognostic marker.

## Used by

- [PMID:24892406](../papers/24892406.md) — four-feature radiomic signature trained on Lung1 NSCLC (n=422), validated in Lung2 NSCLC (CI=0.65, P=2.91×10⁻⁹), H&N1 HNSCC (CI=0.69, P=7.99×10⁻⁷), and H&N2 HNSCC (CI=0.69, P=3.53×10⁻⁶); outperformed or significantly complemented TNM staging in all validation cohorts; intratumour-heterogeneity features (III and IV) correlated with cell-cycling gene-expression pathways in the Lung3 radiogenomics cohort (n=89) [PMID:24892406](../papers/24892406.md).

## Notes

- The signature was intentionally fixed (locked weights) to avoid overfitting; only a single four-feature Cox model was evaluated in validation — a deliberate anti-overfitting design choice [PMID:24892406](../papers/24892406.md).
- HPV status in HNSCC did not associate with signature score (P=0.17, Wilcoxon); the signature retained prognostic value specifically in the HPV-negative majority subgroup (CI=0.66, n=130) [PMID:24892406](../papers/24892406.md).
- The mechanistic link between imaging heterogeneity and proliferation (cell-cycling pathways) is correlative; causal interpretation is not established [PMID:24892406](../papers/24892406.md).

## Sources

- [PMID:24892406](../papers/24892406.md)

*This page was processed by **crosslinker** on **2026-04-15**.*
