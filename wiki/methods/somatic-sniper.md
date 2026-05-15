---
name: SomaticSniper
slug: somatic-sniper
kind: method
canonical_source: corpus
unverified: true
tags: [somatic-calling, snv, tumor-normal]
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# SomaticSniper

## Overview

SomaticSniper is a somatic SNV caller for paired tumor/normal sequencing. It identifies single nucleotide positions with different genotypes between tumor and normal samples using a Bayesian model. In the TCGA MC3 benchmark, SomaticSniper made the fewest overall calls among the seven callers but showed the lowest false-positive rate.

## Used by

- One of seven somatic callers in the TCGA MC3 ensemble pipeline run on DNAnexus cloud across ~10,510 TCGA tumor/normal pairs; made the fewest calls overall but showed the lowest false-positive rate among all callers; run on DNAnexus cloud platform [PMID:29596782](../papers/29596782.md)

## Notes

- Lowest false-positive rate but at the cost of sensitivity relative to other callers.
- Best suited for applications where specificity is paramount (e.g., driver-gene discovery).
- Non-default parameters were required for optimal performance in the MC3 context.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-15**.*
