---
name: OncoCast-MPM
slug: oncocast-mpm
kind: method
canonical_source: corpus
unverified: true
tags: [machine-learning, risk-stratification, computational, sarcoma]
processed_by: crosslinker
processed_at: 2026-04-11
---

# OncoCast-MPM

## Overview

OncoCast-MPM is a machine-learning elastic-net penalized Cox regression risk-prediction tool for genomic risk stratification in leiomyosarcoma (soft tissue and uterine). It integrates somatic genomic alterations from targeted panel sequencing to predict disease-specific survival [PMID:38488807](../papers/38488807.md).

## Used by

- [PMID:38488807](../papers/38488807.md) — OncoCast-MPM was developed using 195 STLMS and 238 [ULMS](../cancer_types/ULMS.md) cases from MSKCC profiled by [MSK-IMPACT](../methods/msk-impact-panel.md) (341–505 genes); defined a 3-tier genomic risk stratification for disease-specific survival; validated using 317 STLMS cases from AACR GENIE; high-risk patients (co-occurrence of [RB1](../genes/RB1.md) mutation + chr12q deletion or [ATRX](../genes/ATRX.md) mutation) had 5-year DSS of 43% vs. 79% for low-risk (no alterations) [PMID:38488807](../papers/38488807.md).

## Notes

- The elastic-net Cox model was preferred over more complex ML approaches to maintain interpretability for clinical application [PMID:38488807](../papers/38488807.md).
- Corpus-grown slug; not present in canonical ontology.

## Sources

- [PMID:38488807](../papers/38488807.md)

*This page was processed by **crosslinker** on **2026-04-11**.*
