---
name: Elastic net regularization
slug: elastic-net
kind: method
canonical_source: corpus
unverified: true
tags: [machine-learning, statistical-model, regression, feature-selection, immunotherapy-prediction]
processed_by: entity-page-writer
processed_at: 2026-05-06
---

# Elastic net regularization

## Overview

Elastic net is a penalized regression method that combines L1 (LASSO) and L2 (Ridge) regularization. By balancing sparsity-inducing L1 penalty with coefficient-shrinkage L2 penalty, elastic net performs simultaneous feature selection and regularization, making it well suited to high-dimensional biomedical data where features are correlated (e.g., immune gene signatures). It is commonly used to build multi-feature predictive models from clinical, genomic, and transcriptomic inputs. When applied as a logistic model, it yields binary classifiers (e.g., responder vs. non-responder) with an interpretable, sparse feature set. When applied within a Cox framework (e.g., OncoCast-MPM), it yields survival risk scores.

## Used by

- A 25-predictor elastic net logistic regression model trained on IMvigor210 (atezolizumab-treated metastatic UC) was applied to predict ICI response in UC-GENOME (218 patients with metastatic urothelial carcinoma); achieved AUC = 0.84 (IMvigor210 validation), 0.82 (UNC-108), and 0.65 (UC-GENOME), significantly outperforming TMB alone (AUC 0.68, p = 0.038); the model integrated TMB, ECOG status, molecular subtype, and immune gene signatures [PMID:36333289](../papers/36333289.md)

## Notes

- Elastic net feature selection depends on the mixing parameter alpha (0 = Ridge, 1 = LASSO); intermediate alpha values retain correlated features.
- Cross-validation is required for hyperparameter tuning (alpha, lambda); overfitting risk increases with small training cohorts.
- Portability across cohorts (e.g., IMvigor210 to UC-GENOME) can be limited by differences in RNA-seq methodology (capture-based vs. total RNA-seq).
- In the UC-GENOME application, the EN model was ICI-specific (not predictive of chemotherapy response, AUC 0.536), supporting its mechanistic basis in immune biology.

## Sources

- [PMID:36333289](../papers/36333289.md) — UC-GENOME metastatic urothelial carcinoma study; elastic net model predicting ICI response from multivariate clinical and immunogenomic features.

*This page was processed by **entity-page-writer** on **2026-05-06**.*
