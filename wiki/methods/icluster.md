---
name: iCluster
slug: icluster
kind: method
canonical_source: corpus
unverified: true
tags: [clustering, integrative-genomics, multi-platform]
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# iCluster

## Overview

iCluster is a probabilistic latent variable model for joint dimensionality reduction and clustering of multi-platform genomic data. It simultaneously integrates copy-number, mutation, methylation, and expression data across the same sample set to define integrative subtypes that reflect concordant signals across data types.

## Used by

- Applied to 333 cutaneous melanoma samples integrating SNP6 copy-number, WES mutations, Illumina 450K methylation, miRNA-seq, and RNA-seq data; identified three integrative clusters including an Immune-mRNA + low-CN + normal-like methylation cluster, a hypomethylation + MITF-expression cluster, and a CIMP + keratin + miRNA-cluster-3 group. [PMID:26091043](../papers/26091043.md)
- Integrative clustering used to define seven mutually exclusive molecular subtypes (ERG/ETV1/ETV4/FLI1 fusions, SPOP/FOXA1/IDH1 mutations) across 333 primary prostate adenocarcinomas in the TCGA molecular taxonomy study [PMID:26544944](../papers/26544944.md).
- iCluster integrative clustering applied across SCNA, methylation, mRNA, and miRNA platforms in the TCGA esophageal/stomach study; cleanly separated squamous from adenocarcinoma histologies and defined three ESCC molecular subtypes (ESCC1, ESCC2, ESCC3) [PMID:28052061](../papers/28052061.md).

## Notes

- Produces integrative cluster assignments that can differ from single-platform subtypes (e.g., transcriptomic clusters).
- Core set of 199 samples with complete six-platform data used for iCluster analysis in TCGA [SKCM](../cancer_types/SKCM.md).

## Sources

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26544944](../papers/26544944.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28052061](../papers/28052061.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
