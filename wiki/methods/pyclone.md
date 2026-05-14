---
name: PyClone
slug: pyclone
kind: method
canonical_source: corpus
unverified: true
tags: [clonal-inference, bayesian, mutation-clustering]
processed_by: entity-page-writer
processed_at: 2026-05-14
---

# PyClone

## Overview

PyClone is a Bayesian statistical method for inferring the clonal population structure of tumours from deep sequencing data. It clusters somatic single-nucleotide variants (SNVs) into groups that share the same cellular prevalence (cancer cell fraction), using a Dirichlet process mixture model. The resulting mutation clusters correspond to distinct clonal genotypes, enabling phylogenetic inference and tracking of clonal dynamics across samples or time-points.

## Used by

- Applied in a breast cancer patient-derived xenograft (PDX) clonal-dynamics study to cluster somatic SNVs into clonal populations; single-cell DNA sequencing of 210 nuclei from SA494 and SA501 PDX lines validated that PyClone clusters correspond to real clonal genotypes, and replicate transplants produced concordant clonal expansion patterns (median Pearson r 0.91–0.94) [PMID:25470049](../papers/25470049.md)

## Notes

- Uses copy-number and tumour purity estimates as inputs alongside variant allele frequencies to compute cancer cell fractions.
- Suitable for multi-region and longitudinal sampling designs where the same clones appear across multiple sequencing runs.
- Results are often paired with TITAN (for CNA-based clonal inference) or phylogenetic tree methods to cross-validate clonal structure.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-14**.*
