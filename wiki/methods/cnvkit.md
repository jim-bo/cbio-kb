---
name: CNVkit
slug: cnvkit
kind: method
canonical_source: corpus
unverified: true
tags: [copy-number, bioinformatics, cnv]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# CNVkit

## Overview

CNVkit is an open-source toolkit for copy-number variant (CNV) detection from targeted DNA sequencing or whole-exome/whole-genome sequencing data. It estimates read depth in on-target and off-target regions, normalizes against a pooled reference, and infers log2 copy-number ratios and segmented CNV calls. CNVkit is widely used in cancer genomics pipelines for somatic CNA profiling.

## Used by

- Applied to detect somatic copy-number alterations in endometrial polyps against a pooled normal reference of 18 matched bloods; identified chromosomal rearrangement-associated CNAs involving HMGA1/HMGA2 loci [PMID:28445112](../papers/28445112.md)
- Applied for somatic copy-number inference from whole-exome sequencing data (58 matched tumor/blood pairs) in the GBM anti-PD-1 immunotherapy cohort (gbm_columbia_2019) [PMID:30742119](../papers/30742119.md)
- Used for copy-number variation calling from WES data in the pan-Asia cHCC-ICC study (133 cases); identified focal amplifications in [MYC](../genes/MYC.md) (73%), [MET](../genes/MET.md) (24%), and [CCNE1](../genes/CCNE1.md) (24%), and deletions in [CDKN2A](../genes/CDKN2A.md) (37%) [PMID:31130341](../papers/31130341.md)

## Notes

- Requires a matched or pooled normal reference for somatic calling.
- Supports WGS, WES, and targeted panel data.
- Outputs segmented log2-ratio profiles and can call focal amplifications and deletions.

## Sources

- [PMID:28445112](../papers/28445112.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:30742119](../papers/30742119.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:31130341](../papers/31130341.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
