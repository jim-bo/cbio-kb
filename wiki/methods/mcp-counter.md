---
name: MCP-counter
slug: mcp-counter
kind: method
canonical_source: corpus
unverified: true
tags: [deconvolution, tumor-microenvironment, rna-seq, immune-infiltration]
processed_by: crosslinker
processed_at: 2026-05-16
---

# MCP-counter

## Overview

MCP-counter (Microenvironment Cell Populations counter) is a transcriptomic deconvolution method that estimates the abundance of eight immune and two stromal cell populations from bulk RNA-seq or microarray data. It uses curated, cell-type-specific gene markers and generates continuous enrichment scores for each cell population.

## Used by

- Used for immune/stromal deconvolution in 40 [UTUC](../cancer_types/UTUC.md) tumors and in the TCGA MI-BLCA cohort ([blca_tcga_pub_2017](../datasets/blca_tcga_pub_2017.md)); projection onto TCGA-BLCA identified BLCA-C1 (hypermethylated/SWI/SNF-mutant) as enriched for fibroblasts, MDC, monocytes, B cells, T cells, and CD8 T cells relative to BLCA-C2 (FGFR3-mutant, neutrophil-enriched, P=1.4×10⁻⁸) [PMID:33397444](../papers/33397444.md)

## Notes

- Corpus-grown slug; not in cBioPortal gene-panel ontology.
- Estimates [absolute](../methods/absolute.md) (not relative) abundance scores for: T cells, CD8 T cells, cytotoxic lymphocytes, NK cells, B lineage, monocytic lineage, myeloid dendritic cells, neutrophils, endothelial cells, fibroblasts.
- Scores are not normalized to sum to 1 (unlike CIBERSORT), allowing independent estimation per cell type.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
