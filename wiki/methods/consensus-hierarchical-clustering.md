---
name: Consensus Hierarchical Clustering (ConsensusClusterPlus)
slug: consensus-hierarchical-clustering
kind: method
canonical_source: corpus
unverified: true
tags: [clustering, unsupervised, transcriptomics, bioinformatics]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Consensus Hierarchical Clustering (ConsensusClusterPlus)

## Overview

Consensus hierarchical clustering (implemented in the R/Bioconductor package ConsensusClusterPlus) is an unsupervised subgroup discovery method that repeatedly subsamples items and features, applies agglomerative hierarchical clustering to each subsample, and accumulates a consensus matrix measuring the proportion of subsamples in which each pair of items clusters together. The optimal number of clusters k is selected by inspecting the area under the CDF of consensus matrix values. Distance metrics and linkage methods are user-specified; Spearman correlation distance with complete linkage is commonly used for transcriptome data.

## Used by

- Applied to RNA-seq data (Spearman distance, k=3) for 28 metastatic neuroendocrine neoplasms ([pog570_bcgsc_2020](../datasets/pog570_bcgsc_2020.md)); defined three transcriptome clusters: Cluster A (small-intestinal NETs/PanNETs with MEN1/DAXX/ATRX alterations), Cluster B (high-grade/MYC-driven mixed primary sites), and Cluster C (PulNETs/MTCs); NECs and NET-G3s did not form a distinct cluster [PMID:40328872](../papers/40328872.md).
- Applied in single-cell RNA-seq analysis (Deng M, cited) to classify cholangiocarcinoma into BA-active and BA-inactive metabolic subtypes; BA-active subtype associated with shorter [OS](../cancer_types/OS.md) and immunotherapy resistance [PMID:25608663](../papers/25608663.md)
- Consensus hierarchical clustering applied to top-1,500 variant genes in 329 melanoma RNA-seq samples, defining three transcriptomic subclasses (Immune 51%, Keratin 31%, MITF-low 18%) with distinct survival and mutational profiles. [PMID:26091043](../papers/26091043.md)
- Used to define three [ILC](../cancer_types/ILC.md) transcriptional subtypes (reactive-like, immune-related, proliferative) from 1,277 SAM-differentiating genes (q=0) in n=106 LumA [ILC](../cancer_types/ILC.md), with survival differences validated in METABRIC [PMID:26451490](../papers/26451490.md)
- Consensus hierarchical clustering applied to 1,300 tumor-specific CpG probes from merged HM27 + HM450 methylation data to define six pan-glioma methylation subtypes (LGm1–6) in 932 TCGA glioma samples [PMID:26824661](../papers/26824661.md)
- Used for sub-group discovery across miRNA, mRNA, and methylation data in 40-66 MRT cases; yielded 2 miRNA sub-groups, 2 mRNA sub-groups (recapitulating AT/RT vs RTK distinction), and 2 WGBS methylation sub-groups (correlated with age >1 year at diagnosis). [PMID:26977886](../papers/26977886.md)
- Consensus hierarchical clustering used for mRNA-based subtype discovery across 173 PCPG tumors; yielded four subtypes (kinase signaling, pseudohypoxia, Wnt-altered, cortical admixture) validated in an independent Burnichon et al. cohort [PMID:28162975](../papers/28162975.md).
- Used for NMF consensus clustering of 408 BLCA RNA-seq samples defining five mRNA expression subtypes (luminal-papillary 35%, luminal-infiltrated 19%, luminal 6%, basal-squamous 35%, neuronal 5%) with distinct survival (p=4×10⁻⁴) [PMID:28988769](../papers/28988769.md)
- Applied in the high-grade UTUC molecular subtype analysis (37 WES / 32 RNA-seq tumors) using UNC BASE47, MDACC, and TCGA classifiers; showed that 84.3% of UTUC tumors are luminal by the UNC BASE47 classifier vs 46.1% of TCGA UCB [PMID:31278255](../papers/31278255.md)

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
- [PMID:26824661](../papers/26824661.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:26977886](../papers/26977886.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28162975](../papers/28162975.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28988769](../papers/28988769.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:31278255](../papers/31278255.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
