---
name: Integrative Genomics Viewer (IGV)
slug: integrative-genomics-viewer
kind: visualization
canonical_source: corpus
unverified: true
tags: [visualization, variant-review, genomics, BAM, VCF]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Integrative Genomics Viewer (IGV)

## Overview

The Integrative Genomics Viewer (IGV) is a high-performance visualization tool developed at the Broad Institute for interactive exploration of large genomic datasets. It supports aligned read files (BAM/CRAM), variant call files (VCF), copy-number data, and gene expression tracks. IGV is commonly used for manual inspection and validation of somatic variant calls in tumor sequencing studies, enabling visual confirmation of putative mutations in their local genomic context.

## Used by

- [coad_caseccc_2015](../datasets/coad_caseccc_2015.md) — used for manual review and validation of somatic variant calls in 29 AA CRC discovery exomes and 74 validation cases; supported visual confirmation of candidate mutations in [EPHA6](../genes/EPHA6.md), [FLCN](../genes/FLCN.md), [HTR1F](../genes/HTR1F.md), and other significantly mutated genes [PMID:25583493](../papers/25583493.md)
- Used for visual inspection and validation of somatic mutations and CNAs called from MSK-IMPACT and array-CGH data in 117 advanced thyroid tumors. [PMID:26878173](../papers/26878173.md)
- Used for visual inspection and validation of somatic mutations and CNAs in WES and array-CGH data from 176 tumors of 63 men with metastatic CRPC. [PMID:26928463](../papers/26928463.md)
- Every alteration called in the MSK-IMPACT pipeline was manually reviewed in IGV as a quality control step across 10,945 tumors [PMID:28481359](../papers/28481359.md)
- Used to visually inspect sequencing alignments and verify CRISPR base-editing outcomes (T→A and A→T conversions at rs4519489) and allele-specific read distributions in the NOL10/USF1 prostate cancer study [PMID:28927585](../papers/28927585.md)
- IGV used for visual review of variant calls from MSK-IMPACT sequencing of 127 advanced HCC tumors [PMID:30373752](../papers/30373752.md)

## Notes

- Free, open-source Java application; supports local and cloud-hosted genomic data.
- Widely used for variant curation in cancer genomics pipelines prior to reporting.
- Supports visualization of structural variants, methylation tracks, and expression data in addition to standard BAM/VCF.
- Available at https://igv.org (Broad Institute).

## Sources

- [PMID:25583493](../papers/25583493.md) — Guda et al. 2015, WES of African American MSS CRC

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26878173](../papers/26878173.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:26928463](../papers/26928463.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28481359](../papers/28481359.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:28927585](../papers/28927585.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:30373752](../papers/30373752.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
