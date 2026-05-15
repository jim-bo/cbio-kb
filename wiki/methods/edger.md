---
name: edgeR (Empirical Analysis of Digital Gene Expression)
slug: edger
kind: method
canonical_source: corpus
unverified: true
tags: [differential-expression, rna-seq, bioinformatics, statistics]
processed_by: wiki-cli
processed_at: 2026-05-15
---

# edgeR (Empirical Analysis of Digital Gene Expression)

## Overview

edgeR is an R/Bioconductor package for differential gene expression analysis of RNA-seq count data. It models read counts using a negative binomial distribution, estimating dispersion parameters empirically across genes using empirical Bayes shrinkage. edgeR supports the exact test (for simple two-group comparisons) and generalized linear models (glmLRT, glmQLFTest) for complex experimental designs. It is one of the two most widely used differential expression tools in cancer genomics (alongside DESeq2).

## Used by

- Used to perform differential gene expression analysis across transcriptome clusters in 28 metastatic neuroendocrine neoplasms ([pog570_bcgsc_2020](../datasets/pog570_bcgsc_2020.md)) using RSEM-quantified RNA-seq data; identified gene sets enriched in MYC-target programs in Cluster B NENs (high-grade/poorly differentiated), supporting master-regulator inference by VIPER [PMID:40328872](../papers/40328872.md).
- Used for differential gene expression analysis of RNA-seq data from AALE chr_3p-deleted vs. wild-type cells; identified 64% of 3p genes significantly down-regulated at early passage (FDR < 0.05) [PMID:29622463](../papers/29622463.md)

## Notes

- edgeR requires raw count data (not TPM or RPKM); RSEM expected counts should be rounded to integers before input.
- TMM normalization (trimmed mean of M-values) is the default normalization method in edgeR.
- For small sample sizes (n < 5 per group), the quasi-likelihood F-test (glmQLFTest) is preferred for more robust dispersion estimation.

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:29622463](../papers/29622463.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
