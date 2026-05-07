---
name: Illumina gene-expression microarray
slug: illumina-microarray
kind: method
canonical_source: corpus
unverified: true
tags: [transcriptomics, microarray, gene-expression]
processed_by: wiki-cli
processed_at: 2026-05-06
---

# Illumina gene-expression microarray

## Overview

Hybridization-based gene-expression profiling using Illumina BeadChip arrays (e.g., HT-12). RNA from tumor or normal tissue is labelled and hybridized to bead-bound oligonucleotide probes; signal intensities proxy mRNA abundance for ~47,000 transcripts. Output is FPKM-scale expression per probe set, suitable for differential expression, clustering, and correlation with imaging or clinical features.

## Used by

- [PMID:30325352](../papers/30325352.md) — Illumina HT-12 gene-expression microarrays applied to 26 of 211 [NSCLC](../cancer_types/NSCLC.md) subjects in the [nsclc-radiogenomics-stanford](../datasets/nsclc-radiogenomics-stanford.md) radiogenomic dataset; 17 subjects have overlapping RNA-seq data; raw data deposited at GEO accession GSE28827 [PMID:30325352](../papers/30325352.md).
- Illumina gene-expression microarray used alongside SNP arrays in METABRIC to derive integrative clustering of ~2,000 breast tumors into 10 subtypes [PMID:22522925](../papers/22522925.md)

## Notes

- In the NSCLC radiogenomics dataset, the microarray arm (n=26) is substantially smaller than the RNA-seq arm (n=130) and is provided for completeness rather than as the primary expression layer [PMID:30325352](../papers/30325352.md).
- The Illumina HT-12 array targets ~47,000 transcripts; direct comparison with RNA-seq FPKM values requires normalization and probe-gene mapping.

## Sources

- [PMID:30325352](../papers/30325352.md)

*This page was processed by **crosslinker** on **2026-05-04**.*
- [PMID:22522925](../papers/22522925.md)

*This page was processed by **wiki-cli** on **2026-05-06**.*
