---
name: NMF Clustering
slug: nmf-clustering
kind: method
canonical_source: corpus
unverified: true
tags: [transcriptomics, clustering, subtype-discovery, dimensionality-reduction]
processed_by: crosslinker
processed_at: 2026-05-21
---

# NMF Clustering

## Overview

Non-negative matrix factorization (NMF) clustering is an unsupervised machine-learning method that decomposes a non-negative data matrix (e.g., a gene-expression count matrix) into two lower-rank non-negative matrices representing latent factors (metagenes) and their sample-level coefficients. Sample assignment to a subtype is determined by the dominant factor for each sample. In transcriptomic cancer studies, NMF at a chosen rank (e.g., rank 3) is applied to RNA-seq data to discover reproducible molecular subtypes that capture coordinated gene-expression programs. The Brunet multiplicative update algorithm is commonly used via the R `NMF` package.

## Used by

- Applied in the Sherlock-Lung NS-LUAD study ([luad_oncosg_2020](../datasets/luad_oncosg_2020.md)) on RNA-seq from 684 treatment-naive never-smoker lung adenocarcinomas (610 Sherlock-Lung + 74 TCGA-LUAD); rank-3 NMF identified three transcriptomic subtypes — *steady* (normal-like, alveolar-enriched, best survival), *proliferative* (MYC-driven, TP53-mutant-enriched), and *chaotic* (EMT-high, fibroblast-enriched, worst prognosis); subtypes validated with a 60-gene [ClaNC](../methods/clanc.md)-derived signature in the GIS cohort (n=110) [PMID:32015526](../papers/32015526.md).
- Multi-omics NMF clustering across 10 data platforms in 99 treatment-naive GBMs recapitulated TCGA expression subtypes (proneural-like nmf1, mesenchymal-like nmf2, classical-like nmf3) but reclassified 29% of tumors; mixed-subtype tumors (n=12) had significantly worse survival (log-rank p=1.7e-4) [PMID:33577785](../papers/33577785.md)
- Used in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS) for somatic variant calling and genomic analysis of the [lung_nci_2022](../datasets/lung_nci_2022.md) cohort [PMID:34493867](../papers/34493867.md)
- Applied in [hcc_meric_2021](../datasets/hcc_meric_2021.md) to define single-omics subtypes from transcriptome, proteome, and phosphoproteome data independently in 122 [HCC](../cancer_types/HCC.md) biopsies; results integrated via iCluster to define three consensus molecular subtypes [PMID:35508466](../papers/35508466.md)

## Notes

- Rank selection is data-driven (consensus matrices, cophenetic correlation); rank 3 was optimal in the Sherlock-Lung NS-LUAD dataset.
- ComBat-Seq batch correction and DESeq2/TMM normalization are applied upstream of NMF to remove technical variation.
- NMF is not directly applicable without gene-expression data; unlike mutation-only or stage-based classifiers, it requires a transcriptome.
- Compressible to a gene-panel classifier (e.g., 60-gene [ClaNC](../methods/clanc.md) signature) for clinical translation.

## Sources

- [PMID:32015526](../papers/32015526.md) — Sherlock-Lung NS-LUAD transcriptomic subtyping

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:33577785](../papers/33577785.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34493867](../papers/34493867.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35508466](../papers/35508466.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
