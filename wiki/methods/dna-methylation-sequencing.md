---
name: DNA methylation sequencing
slug: dna-methylation-sequencing
kind: method
canonical_source: corpus
unverified: true
tags: [epigenomics, methylation, bisulfite-sequencing, wgbs]
processed_by: crosslinker
processed_at: 2026-05-21
---

# DNA methylation sequencing

## Overview

DNA methylation sequencing encompasses whole-genome bisulfite sequencing (WGBS) and reduced-representation bisulfite sequencing (RRBS), which chemically convert unmethylated cytosines to uracil and sequence the result to map CpG methylation at single-base resolution genome-wide. Unlike hybridization-based methylation arrays (e.g., Illumina 450K/EPIC), bisulfite sequencing provides unbiased coverage across the entire genome, including regions not covered by array probes. It is used to detect differentially methylated regions (DMRs), CpG island methylator phenotypes (CIMP), and epigenomic subgroups in cancer.

## Used by

- Reviewed as a core epigenomics modality in multi-omics integration for precision health and precision oncology; cited alongside WGS, RNA-seq, proteomics, [metabolomics](../methods/metabolomics.md), and [lipidomics](../methods/lipidomics.md) as orthogonal layers that together capture functional and mechanistic signal unavailable from any single assay. [PMID:37119971](../papers/37119971.md)
- DNA methylation integration (with CNV and gene expression) across 256 [HCC](../cancer_types/HCC.md) samples yielded five transcriptomic subgroups with distinct survival (Liu et al. 2016, cited in [PMID:37119971](../papers/37119971.md)).
- Multi-omics integration including DNA methylation applied to [SKCM](../cancer_types/SKCM.md) samples to build prognostic models with mean C-statistic 0.724 (Jiang et al. 2016, cited in [PMID:37119971](../papers/37119971.md)).
- CPTAC highlighted as a canonical multi-omics cancer repository providing DNA methylation alongside WGS/WES, RNA-seq, proteomics, and phosphoproteomics across multiple cancer types. [PMID:37119971](../papers/37119971.md)

## Notes

- Bisulfite sequencing is higher-cost and more data-intensive than array-based methylation profiling but provides complete genomic coverage and is not limited to pre-selected probe sites.
- TCGA and CPTAC both include DNA methylation data (primarily from 450K/EPIC arrays for TCGA; WGBS for some CPTAC studies) and are cited as reference repositories for multi-omics integration.
- Corpus-grown slug; no gene-panel ID in `schema/ontology/gene_panels.json`. See `schema/ontology/_observed.md`.

## Sources

- [PMID:37119971](../papers/37119971.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
