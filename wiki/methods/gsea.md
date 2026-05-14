---
name: GSEA
slug: gsea
kind: method
canonical_source: corpus
unverified: true
tags: [pathway-analysis, gene-sets, transcriptomics, enrichment]
processed_by: wiki-cli
processed_at: 2026-05-14
---

# GSEA

## Overview

Gene Set Enrichment Analysis (GSEA) is a computational method for determining whether a predefined gene set (e.g., a biological pathway, GO term, or curated gene signature) shows statistically significant, concordant differences between two biological states. It uses a ranked gene list (by differential expression, correlation, or other metric) and calculates an enrichment score for each gene set, testing for nonrandom distribution of the set's genes within the ranked list. GSEA is widely used for pathway-level interpretation of transcriptomic data and for cross-dataset comparison of gene expression programs.

## Used by

- GSEA of 486 fulvestrant-responsive differentially expressed genes in Nf1Indel rat mammary tumors showed significant enrichment of genes induced by neoadjuvant [letrozole](../drugs/letrozole.md) (GSE5462) and [fulvestrant](../drugs/fulvestrant.md) (GSE71791) in patient datasets; 58-gene overlap included [PGR](../genes/PGR.md), AREG, SGK3, and other ER-response genes, validating cross-species transcriptome concordance. [PMID:26437033](../papers/26437033.md)
- Used to compare gene expression between long-fusion (breakpoint after exon 11) and short-fusion (exons 8/9) MYBL1/MYB ACC subsets; identified 19 gene sets enriched in long fusions (RNA processing/translation) and 5 in short fusions (tissue development) [PMID:26631609](../papers/26631609.md).

## Notes

- Standard GSEA uses a Kolmogorov-Smirnov-like statistic with permutation-based FDR correction (Subramanian et al. 2005).
- MSigDB (Molecular Signatures Database) is the primary curated gene set library used with GSEA.
- Pre-ranked GSEA (fgsea/GSEA Preranked) is commonly used when the ranked list is derived from an external statistic (e.g., DESeq2 Wald statistic).

## Sources

- [PMID:26437033](../papers/26437033.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26631609](../papers/26631609.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
