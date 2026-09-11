---
name: LASSO Regression
slug: lasso-regression
kind: method
canonical_source: corpus
unverified: true
tags: [statistics, regularization, feature-selection]
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# LASSO Regression

## Overview

LASSO (Least Absolute Shrinkage and Selection Operator) regression is a regularized regression method that shrinks less-informative predictor coefficients toward zero, performing simultaneous variable selection and regularization. In cancer genomics it is commonly used to build parsimonious prognostic models from high-dimensional mutation, cytogenetic, and clinical covariates.

## Used by

- Used to select and weight driver-mutation, cytogenetic, and clinical variables for a revised prognostic model in myelodysplastic syndromes [PMID:24030381](../papers/24030381.md).

## Notes

- Corpus-grown slug; not in the cBioPortal gene-panel or molecular-profile ontology.
- Typically paired with Cox proportional hazards regression when the outcome is survival time.

## Sources

- [PMID:24030381](../papers/24030381.md)

*This page was processed by **entity-page-writer** on **2026-09-10**.*
