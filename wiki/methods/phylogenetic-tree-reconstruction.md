---
name: Phylogenetic tree reconstruction
slug: phylogenetic-tree-reconstruction
kind: method
canonical_source: corpus
unverified: true
tags: [bioinformatics, evolution, intratumor-heterogeneity]
processed_by: entity-page-writer
processed_at: 2026-05-11
---

# Phylogenetic tree reconstruction

## Overview

Computational method applied to multiregion tumor sequencing data to infer the evolutionary history of tumor cell populations. Mutation presence/absence calls across regions are used to build phylogenetic trees (e.g., by maximum parsimony), distinguishing truncal (shared by all regions) from branch (subclonal) alterations.

## Used by

- Maximum parsimony phylogenetic trees built from regional mutation presence/absence calls across 10 ccRCC tumors (79 samples); used to classify driver mutations and SCNAs as truncal vs. branch and to identify parallel evolution events (e.g., independent PIK3CA hotspot mutations in EV005, convergent SETD2 hits in 3 tumors) [PMID:24487277](../papers/24487277.md).

## Notes

- Maximum parsimony is appropriate for tumor phylogenetics when SNP-array integer copy-number resolution is limited.
- Parallel (convergent) driver hits across independent branches can be misinterpreted as single truncal events without multiregion data [PMID:24487277](../papers/24487277.md).

## Sources

*This page was processed by **entity-page-writer** on **2026-05-11**.*
