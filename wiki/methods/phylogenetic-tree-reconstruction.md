---
name: Phylogenetic tree reconstruction
slug: phylogenetic-tree-reconstruction
kind: method
canonical_source: corpus
unverified: true
tags: [bioinformatics, evolution, intratumor-heterogeneity]
processed_by: crosslinker
processed_at: 2026-05-14
---

# Phylogenetic tree reconstruction

## Overview

Computational method applied to multiregion tumor sequencing data to infer the evolutionary history of tumor cell populations. Mutation presence/absence calls across regions are used to build phylogenetic trees (e.g., by maximum parsimony), distinguishing truncal (shared by all regions) from branch (subclonal) alterations.

## Used by

- Maximum parsimony phylogenetic trees built from regional mutation presence/absence calls across 10 ccRCC tumors (79 samples); used to classify driver mutations and SCNAs as truncal vs. branch and to identify parallel evolution events (e.g., independent [PIK3CA](../genes/PIK3CA.md) hotspot mutations in EV005, convergent [SETD2](../genes/SETD2.md) hits in 3 tumors) [PMID:24487277](../papers/24487277.md).
- MrBayes 3.2 used for single-cell Bayesian phylogenetic inference on SA494 and SA501 breast cancer PDX nuclei; confirmed pre-existing minor tumor clones as the origin of xenograft-dominant populations and resolved 5 clonal genotypes across serial passages of SA501 [PMID:25470049](../papers/25470049.md)
- Multi-region phylogenetic analysis of WGS data from 2 gastric cancer patients (3 primary-tumor regions + 2 lymph-node metastases each) showed substantial divergence among primary regions with lymph-node metastases sharing a common clonal ancestor from only one primary-tumor region [PMID:25583476](../papers/25583476.md)

## Notes

- Maximum parsimony is appropriate for tumor phylogenetics when SNP-array integer copy-number resolution is limited.
- Parallel (convergent) driver hits across independent branches can be misinterpreted as single truncal events without multiregion data [PMID:24487277](../papers/24487277.md).

## Sources

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25470049](../papers/25470049.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25583476](../papers/25583476.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
