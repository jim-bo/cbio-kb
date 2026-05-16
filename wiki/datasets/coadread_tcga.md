---
name: Colorectal Adenocarcinoma (TCGA, Firehose Legacy)
studyId: coadread_tcga
institution: 
size: 
reference_genome: GRCh37
canonical_source: 
unverified: 
assays: []
panels: []
tags: []
processed_by: entity-page-writer
processed_at: 2026-05-16
description: TCGA Colorectal Adenocarcinoma. Source data from GDAC Firehose. Previously known as TCGA Provisional.
cancerTypeId: coadread
pmid: null
allSampleCount: 1
---

# Colorectal Adenocarcinoma (TCGA, Firehose Legacy)

## Overview

TCGA colorectal adenocarcinoma cohort (GDAC Firehose legacy release), used as an external comparator in the cbio-kb corpus [PMID:37202560](../papers/37202560.md).

## Composition

- TCGA [colorectal adenocarcinoma](../cancer_types/COADREAD.md) samples from the Firehose legacy release [PMID:37202560](../papers/37202560.md).

## Assays / panels (linked)

- TCGA multi-platform profiling (WES, [RNA-seq](../methods/rna-seq.md), copy-number, methylation) as released through GDAC Firehose.

## Papers using this cohort

- [PMID:37202560](../papers/37202560.md) — Roelands et al. used TCGA-COAD as a comparator to the AC-ICAM ([coad_silu_2022](../datasets/coad_silu_2022.md)) cohort; they noted TCGA-COAD's limited survival follow-up and tumor-purity selection criteria as motivation for building the new fresh-frozen multi-omics resource [PMID:37202560](../papers/37202560.md).
- [PMID:32888432](../papers/32888432.md) — Liu et al. used TCGA CRC data via TIMER 2.0 and GEPIA2 (275 CRC samples + 349 normal; 17 matched pairs) to establish that CGREF1 is significantly upregulated in CRC versus normal colon tissue, providing the bioinformatic context for their in-house tissue microarray validation study.

## Notable findings derived from this cohort

- Used as a reference cohort for benchmarking AC-ICAM's ICR-based immune classification and for microbiome signature context [PMID:37202560](../papers/37202560.md).
- GEPIA2 analysis (275 CRC vs. 349 normal TCGA samples) confirmed CGREF1 significantly upregulated in CRC; matched-pair analysis (n=17) corroborated this finding [PMID:32888432](../papers/32888432.md).

## Sources

- cBioPortal study `coadread_tcga` (TCGA Firehose Legacy).
- Cancer Genome Atlas Network. *Comprehensive molecular characterization of human colon and rectal cancer.* Nature. 2012. PMID:22810696 — primary TCGA COAD/READ cohort paper (not in the cbio-kb corpus).

*This page was processed by **entity-page-writer** on **2026-05-16**.*
