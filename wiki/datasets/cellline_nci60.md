---
name: NCI-60 Human Cancer Cell Line Panel (cellline_nci60)
studyId: cellline_nci60
institution: National Cancer Institute (NCI) Developmental Therapeutics Program
size: 60
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - MRNA_EXPRESSION
panels: []
tags:
  - cell-line
  - pharmacogenomics
  - drug-sensitivity
  - nci-60
processed_by: entity-page-writer
processed_at: 2026-05-06
---

# NCI-60 Human Cancer Cell Line Panel (cellline_nci60)

## Overview

The NCI-60 is a panel of 60 human cancer cell lines spanning 9 tissue types, maintained by the NCI Developmental Therapeutics Program (DTP). The CellMiner database integrates multi-platform genomic, transcriptomic, and drug activity data from this panel. Transcript data from 5 microarray platforms (Affymetrix HG-U95, HG-U133, HG-U133 Plus 2.0, GeneChip Human Exon 1.0 ST; Agilent Whole Human Genome Oligo Microarray) cover 22,217 genes. Drug activity data includes GI50 values for 18,549 compounds from 47,540 tested, determined by sulforhodamine B assay at 48 hours.

## Composition

- 60 cancer cell lines across 9 tissue types including colon ([COAD](../cancer_types/COAD.md)), lung, breast, ovary, kidney, prostate, CNS, melanoma, and leukemia.
- MicroRNA data: 360 microRNAs from Agilent Human miRNA Microarray V2.
- Drug activity: GI50 for 18,549 compounds via NCI DTP.

## Assays / panels (linked)

- [cellminer](../methods/cellminer.md) — integrated database and pattern comparison tool for NCI-60 multi-omics and drug activity data.
- 5 Affymetrix/Agilent microarray platforms — mRNA expression (22,217 genes).
- Agilent Human miRNA Microarray V2 — 360 microRNAs.
- Sulforhodamine B (SRB) assay — 48-hour GI50 drug activity.

## Papers using this cohort

- [PMID:22802077](../papers/22802077.md) — CellMiner: a web-based suite of genomic and pharmacological tools to explore transcript and drug patterns in the NCI-60 cell line set (Reinhold et al., 2012).

## Notable findings derived from this cohort

- [ABCB1](../genes/ABCB1.md) overexpression in NCI-ADR-RES and HCT-15 cell lines correlates with [doxorubicin](../drugs/doxorubicin.md) resistance via P-glycoprotein-mediated efflux [PMID:22802077](../papers/22802077.md).
- Erlotinib drug activity pattern retrieves [gefitinib](../drugs/gefitinib.md), [lapatinib](../drugs/lapatinib.md) (5th and 6th), and [afatinib](../drugs/afatinib.md) (3rd) among 18,549 compounds, demonstrating EGFR-class clustering [PMID:22802077](../papers/22802077.md).
- Colon-specific expression pattern identifies [RNF43](../genes/RNF43.md), TRIM15, and VIL1 as top correlated colon cancer marker genes [PMID:22802077](../papers/22802077.md).
- miR-17-92 oncogenic cluster members show high inter-correlation (r=0.77–0.96) and [MYC](../genes/MYC.md) correlation (r=0.61) consistent with MYC-driven transcription [PMID:22802077](../papers/22802077.md).
- [selumetinib](../drugs/selumetinib.md) and [sunitinib](../drugs/sunitinib.md) identified as candidate colorectal cancer therapies via colon-specific drug pattern matching [PMID:22802077](../papers/22802077.md).

## Sources

- [PMID:22802077](../papers/22802077.md)

*This page was processed by **entity-page-writer** on **2026-05-06**.*
