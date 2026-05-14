---
name: Consensus Hierarchical Clustering (ConsensusClusterPlus)
slug: consensus-hierarchical-clustering
kind: method
canonical_source: corpus
unverified: true
tags: [clustering, unsupervised, transcriptomics, bioinformatics]
processed_by: crosslinker
processed_at: 2026-05-14
---

# Consensus Hierarchical Clustering (ConsensusClusterPlus)

## Overview

Consensus hierarchical clustering (implemented in the R/Bioconductor package ConsensusClusterPlus) is an unsupervised subgroup discovery method that repeatedly subsamples items and features, applies agglomerative hierarchical clustering to each subsample, and accumulates a consensus matrix measuring the proportion of subsamples in which each pair of items clusters together. The optimal number of clusters k is selected by inspecting the area under the CDF of consensus matrix values. Distance metrics and linkage methods are user-specified; Spearman correlation distance with complete linkage is commonly used for transcriptome data.

## Used by

- Applied to RNA-seq data (Spearman distance, k=3) for 28 metastatic neuroendocrine neoplasms ([pog570_bcgsc_2020](../datasets/pog570_bcgsc_2020.md)); defined three transcriptome clusters: Cluster A (small-intestinal NETs/PanNETs with MEN1/DAXX/ATRX alterations), Cluster B (high-grade/MYC-driven mixed primary sites), and Cluster C (PulNETs/MTCs); NECs and NET-G3s did not form a distinct cluster [PMID:24326773](../papers/24326773.md).
- Applied in single-cell RNA-seq analysis (Deng M, cited) to classify cholangiocarcinoma into BA-active and BA-inactive metabolic subtypes; BA-active subtype associated with shorter [OS](../cancer_types/OS.md) and immunotherapy resistance [PMID:25608663](../papers/25608663.md)
- Consensus hierarchical clustering applied to top-1,500 variant genes in 329 melanoma RNA-seq samples, defining three transcriptomic subclasses (Immune 51%, Keratin 31%, MITF-low 18%) with distinct survival and mutational profiles. [PMID:26091043](../papers/26091043.md)
- Used to define three [ILC](../cancer_types/ILC.md) transcriptional subtypes (reactive-like, immune-related, proliferative) from 1,277 SAM-differentiating genes (q=0) in n=106 LumA [ILC](../cancer_types/ILC.md), with survival differences validated in METABRIC [PMID:26451490](../papers/26451490.md)

## Notes

- ConsensusClusterPlus requires a pre-selected feature set (e.g., top-variable genes); results can be sensitive to feature selection cutoff.
- Visualization typically accompanies the consensus matrix with heatmaps and silhouette plots.
- Related methods include NMF-based consensus clustering and k-means consensus clustering.

## Sources

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25608663](../papers/25608663.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26091043](../papers/26091043.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26451490](../papers/26451490.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
