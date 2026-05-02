---
name: OncoCast
slug: oncocast
kind: method
canonical_source: corpus
unverified: true
tags: [survival-modeling, machine-learning, elastic-net, cox, random-forest]
processed_by: crosslinker
processed_at: 2026-04-30
---

# OncoCast

## Overview

OncoCast is an elastic-net Cox regression model combined with a random-forest residual correction, designed for survival analysis in left-truncated observational oncology cohorts. It is used to predict overall survival from multi-modal clinical, genomic, and NLP-derived features while handling time-on-study biases inherent to real-world data.

## Used by

- [PMID:39506116](../papers/39506116.md) — OncoCast (elastic-net Cox plus random-forest residual correction, 500 trees, 5 terminal nodes, 50 runs) applied within the MSK-CHORD clinicogenomic dataset (24,950 patients) alongside [random survival forest](../methods/random-survival-forest.md) models for left-truncated [OS](../cancer_types/OS.md) prediction across five cancer types ([NSCLC](../cancer_types/NSCLC.md), [BRCA](../cancer_types/BRCA.md), [COADREAD](../cancer_types/COADREAD.md), [PRAD](../cancer_types/PRAD.md), [PAAD](../cancer_types/PAAD.md)); combined-modality models outperformed single-modality in every cancer type [PMID:39506116](../papers/39506116.md).

## Notes

- Corpus-grown slug; not present in canonical ontology. Note: a separate page exists for [oncocast-mpm](../methods/oncocast-mpm.md), which is a specialized variant.
- Designed specifically for left-truncation bias correction in real-world datasets where cohort entry time does not equal start of follow-up.

## Sources

- [PMID:39506116](../papers/39506116.md)

*This page was processed by **crosslinker** on **2026-04-30**.*
