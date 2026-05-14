---
name: Random Forest Classifier
slug: random-forest-classifier
kind: machine_learning
canonical_source: corpus
unverified: true
tags: [machine-learning, classification, ensemble, random-forest]
processed_by: wiki-cli
processed_at: 2026-05-14
---

# Random Forest Classifier

## Overview

Random forest is an ensemble machine learning algorithm that constructs multiple decision trees during training and outputs the mode (classification) or mean prediction (regression) of the individual trees. It is robust to overfitting relative to single decision trees, handles high-dimensional features well, and provides feature importance scores. In cancer biology, random forest classifiers have been applied to microbiome data, genomic features, and multi-omic profiles for diagnostic and prognostic classification.

## Used by

- Synthesized in a narrative review of gut-liver axis dysregulation in cholangiocarcinoma: a random forest classifier using eight bacterial genera achieved AUC 0.92–0.99 differentiating cholangiocarcinoma from hepatocellular carcinoma in gut microbiota profiles (Deng T et al., cited); an oral microbiota three-bacterial-biomarker classifier (Rao et al., cited) achieved AUC 0.981 for iCCA vs [HCC](../cancer_types/HCC.md) distinction [PMID:25608663](../papers/25608663.md)
- Random-forest classifier used for unsupervised clustering of pathway alteration profiles in 109 PDA cases, revealing subtypes where isolated KRAS-pathway alterations (clusters 1 & 2) correlated with poor prognosis. [PMID:25855536](../papers/25855536.md)

## Notes

- Feature importance from random forests can identify the most discriminating microbial taxa, genomic alterations, or clinical variables for a given classification task.
- Model performance should be evaluated on held-out test sets or by cross-validation; AUC values reported from single-cohort studies are subject to overfitting.
- Applied broadly across cancer genomics (e.g., mutation burden classification, subtype assignment, drug response prediction).

## Sources

- [PMID:25608663](../papers/25608663.md) — Gut-liver axis review in cholangiocarcinoma (narrative review reporting random forest classifier performance for CCA microbiome diagnostics)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25855536](../papers/25855536.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
