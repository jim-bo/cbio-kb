---
name: TITAN (CNA/LOH clonal inference)
slug: titan-cna
kind: method
canonical_source: corpus
unverified: true
tags: [copy-number, clonal-inference, loh, cna]
processed_by: entity-page-writer
processed_at: 2026-05-14
---

# TITAN (CNA/LOH clonal inference)

## Overview

TITAN is a probabilistic model for inferring subclonal copy number alterations (CNAs) and loss of heterozygosity (LOH) from tumour whole-genome sequencing data. It jointly models allele-specific copy number and cellular prevalence, producing clonal CNA profiles that can be compared with SNV-based clonal assignments (e.g., from PyClone) to confirm or refute clonal architecture inferences.

## Used by

- Used for CNA/LOH clonal inference in breast cancer PDX clonal-dynamics study; TITAN-based CNA clonal dynamics recapitulated SNV-based PyClone dynamics in minor-subclone expansion (SA494, SA495, SA532, SA533) and polyclonal engraftment (SA493, SA501), providing orthogonal validation of clonal selection at engraftment [PMID:25470049](../papers/25470049.md)

## Notes

- Requires whole-genome sequencing input (allele count data and read depth).
- Outputs clonal and subclonal CNA segments with associated cellular prevalence estimates.
- Frequently used alongside PyClone (SNV clustering) for multi-modal clonal analysis.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-14**.*
