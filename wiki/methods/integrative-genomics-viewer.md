---
name: Integrative Genomics Viewer (IGV)
slug: integrative-genomics-viewer
kind: visualization
canonical_source: corpus
unverified: true
tags: [visualization, variant-review, genomics, BAM, VCF]
processed_by: crosslinker
processed_at: 2026-05-14
---

# Integrative Genomics Viewer (IGV)

## Overview

The Integrative Genomics Viewer (IGV) is a high-performance visualization tool developed at the Broad Institute for interactive exploration of large genomic datasets. It supports aligned read files (BAM/CRAM), variant call files (VCF), copy-number data, and gene expression tracks. IGV is commonly used for manual inspection and validation of somatic variant calls in tumor sequencing studies, enabling visual confirmation of putative mutations in their local genomic context.

## Used by

- [coad_caseccc_2015](../datasets/coad_caseccc_2015.md) — used for manual review and validation of somatic variant calls in 29 AA CRC discovery exomes and 74 validation cases; supported visual confirmation of candidate mutations in [EPHA6](../genes/EPHA6.md), [FLCN](../genes/FLCN.md), [HTR1F](../genes/HTR1F.md), and other significantly mutated genes [PMID:25583493](../papers/25583493.md)

## Notes

- Free, open-source Java application; supports local and cloud-hosted genomic data.
- Widely used for variant curation in cancer genomics pipelines prior to reporting.
- Supports visualization of structural variants, methylation tracks, and expression data in addition to standard BAM/VCF.
- Available at https://igv.org (Broad Institute).

## Sources

- [PMID:25583493](../papers/25583493.md) — Guda et al. 2015, WES of African American MSS CRC

*This page was processed by **crosslinker** on **2026-05-14**.*
