---
name: xCell
slug: xcell
kind: method
canonical_source: corpus
unverified: true
tags: [deconvolution, tumor-microenvironment, rna-seq, immune-infiltration]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# xCell

## Overview

xCell is an RNA-based cell-type deconvolution method that estimates the relative abundance of 64 immune and stromal cell types from bulk RNA-seq or microarray data. It uses a gene-signature approach with a non-linear spillover compensation model to infer the tumor microenvironment composition from gene expression profiles.

## Used by

- Applied to RNA-seq data from 218 pediatric brain tumor samples (N=218, 7 histologies) in [brain_cptac_2020](../datasets/brain_cptac_2020.md), producing five tumor microenvironment groups (Cold-medullo, Cold-mixed, Neuronal, Epithelial, Hot); the Hot cluster was enriched for adenosine producers (ENTPD1, [NT5E](../genes/NT5E.md)), and the Epithelial cluster (all craniopharyngioma) upregulated [CTLA4](../genes/CTLA4.md) and PD-1 [PMID:33242424](../papers/33242424.md)
- xCell deconvolution of bulk RNA-seq data used to define four immune subtypes (im1–im4) in 99 GBM tumors; im4 was uniformly immunologically cold (1.3% T cells, 6% TAM by snRNA-seq validation); subtypes confirmed by IHC (CD3, CD68, CD163, PD-1, PD-L1) [PMID:33577785](../papers/33577785.md)

## Notes

- Corpus-grown slug; validated as a widely used tool but not registered in cBioPortal gene-panel ontology.
- Output: dimensionless enrichment scores per cell type per sample; not [absolute](../methods/absolute.md) cell counts.
- Complements protein/phosphoproteomic data when RNA is the only profiling modality.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
- [PMID:33577785](../papers/33577785.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
