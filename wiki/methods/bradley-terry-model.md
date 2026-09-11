---
name: Bradley-Terry Model
slug: bradley-terry-model
kind: method
canonical_source: corpus
unverified: true
tags: [statistical-method, clonal-ordering, ranking-model]
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# Bradley-Terry Model

## Overview

The Bradley-Terry model is a statistical model for paired-comparison data that estimates a latent ranking from pairwise "win/loss" outcomes. In cancer genomics it has been adapted to infer a global temporal order of mutation acquisition across a cohort by aggregating pairwise within-patient clonal-relationship calls.

## Used by

- A Bradley-Terry model inferred a global temporal ordering of driver-mutation acquisition across 738 myelodysplastic syndrome patients, built from within-patient pairwise clonal/subclonal relationships derived from variant allele fractions and Pearson goodness-of-fit testing. [PMID:24030381](../papers/24030381.md)

## Notes

- Applied downstream of phylogenetic tree reconstruction, after pairwise clonal-order calls were made within each patient's own mutation set.

## Sources

- [PMID:24030381](../papers/24030381.md) — Papaemmanuil et al. 2013, *Blood*, clinical and biological implications of driver mutations in myelodysplastic syndromes

*This page was processed by **entity-page-writer** on **2026-09-10**.*
