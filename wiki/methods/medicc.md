---
name: MEDICC
slug: medicc
kind: method
canonical_source: corpus
unverified: true
tags:
  - copy-number
  - phylogenetics
  - intratumor-heterogeneity
  - clonal-evolution
processed_by: crosslinker
processed_at: 2026-05-16
---

# MEDICC

## Overview

MEDICC (Minimum Event Distance for Intra-tumour Copy number Comparisons) is a computational tool for phylogenetic reconstruction from allele-specific copy-number data. It infers evolutionary trees of tumor subclones by computing the minimum number of copy-number change events separating allele-specific CNA profiles across multiple samples or bulk inferred subclones. MEDICC is particularly suited for bulk-sequencing studies where clonal decomposition tools (e.g., FACETS, ABSOLUTE, PyClone) produce subclone-level CNA profiles that can then be organized into phylogenetic trees reflecting tumor evolutionary history.

## Used by

- [brca_pareja_msk_2020](../datasets/brca_pareja_msk_2020.md) — phylogenetic analysis of synchronous [DCIS](../cancer_types/DCIS.md) and IDC-NST pairs [PMID:32220886](../papers/32220886.md)

## Notes

- Used in combination with [FACETS](../methods/facets.md), [ABSOLUTE](../methods/absolute.md), and [PyClone](../methods/pyclone.md) to reconstruct tumor evolutionary histories from bulk whole-exome sequencing data.
- Applied alongside SNV-based clonal decomposition in Pareja et al. (2020) to confirm bulk-derived phylogenies consistent with single-cell studies.
- No cBioPortal gene-panel or molecular-profile canonical ID exists; slug is corpus-derived.

## Sources

- Applied to 56-sample WES cohort of synchronous DCIS/IDC-NST pairs; bulk-derived phylogenies confirmed consistent with single-cell studies (Casasent 2018, Martelotto 2017) [PMID:32220886](../papers/32220886.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
