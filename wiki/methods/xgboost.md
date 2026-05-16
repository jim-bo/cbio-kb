---
name: XGBoost
slug: xgboost
kind: method
canonical_source: corpus
unverified: true
tags: [machine-learning, gradient-boosting, classification, computational]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# XGBoost

## Overview

XGBoost (eXtreme Gradient Boosting) is a gradient-boosted decision tree machine learning framework known for high performance on structured data. It is widely used for classification and regression tasks in cancer genomics [PMID:27634761](../papers/27634761.md).

## Used by

- [PMID:27634761](../papers/27634761.md) — XGBoost was used as the core machine learning framework for the ATLAS (AI Tumor Lineage and Site) classifier; trained on 8,249 RNA-seq samples from TCGA and CCLE to classify 22 cancer sites of origin and 8 cancer lineages; achieved 91.4% site-of-origin accuracy and 97.1% lineage accuracy on a validation set of 10,376 samples; high-confidence predictions (score >= 0.99) achieved 98–99% accuracy [PMID:27634761](../papers/27634761.md).
- Gradient boosting (XGBoost-class) model trained to predict ICI response (ROC-AUC=0.77 training, 0.78 JAVELIN validation) and TKI response (ROC-AUC=0.74 validation, n=822) in ccRCC, outperforming all published single-biomarker signatures [PMID:22138691](../papers/22138691.md)
- Evaluated as a baseline comparator in the OncoMark cancer hallmark-activity study; like other standard classifiers (logistic regression, SVC, random forest, MLP), XGBoost collapsed to near-zero hallmark probabilities on bulk cancer samples — failing the discrimination task that OncoMark's multi-task neural network solved [PMID:35121966](../papers/35121966.md)

## Notes

- XGBoost outperformed random forests and SVMs in the ATLAS cancer classifier benchmark; RNA expression alone sufficed without requiring DNA mutation or copy number features [PMID:27634761](../papers/27634761.md).
- Corpus-grown slug; not present in canonical ontology.

## Sources

- [PMID:27634761](../papers/27634761.md)

*This page was processed by **entity-page-writer** on **2026-04-11**.*
- [PMID:22138691](../papers/22138691.md)

*This page was processed by **wiki-cli** on **2026-05-06**.*
- [PMID:35121966](../papers/35121966.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
