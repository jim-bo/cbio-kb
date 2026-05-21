---
name: CSYS 450-gene NGS panel (OrigiMed)
slug: csys-450-gene-panel
kind: method
canonical_source: corpus
unverified: true
tags: [targeted-panel, ngs, oncology]
processed_by: crosslinker
processed_at: 2026-05-21
---

# CSYS 450-gene NGS panel (OrigiMed)

## Overview

The CSYS 450-gene panel is a CLIA-certified, CAP-accredited targeted next-generation sequencing assay developed by OrigiMed (Shanghai). It captures ~2.6 Mb of coding exons from 450 cancer-related genes, the [TERT](../genes/TERT.md) promoter, and [select](../methods/select.md) introns of 39 rearrangement-prone genes. The panel supports calling of SNVs, InDels, CNVs (via EXCAVATOR), gene fusions, MSI, and TMB from tumor/blood pairs sequenced on Illumina NextSeq 500 or NovaSeq 6000. Median tumor unique coverage is ~1,202x; matched normal blood mean unique coverage ~300x.

## Used by

- Applied to 10,194 Chinese solid-tumor patients (92% Han) across 25 tumor types in the OrigiMed pan-cancer cohort ([pan_origimed_2020](../datasets/pan_origimed_2020.md)); identified 80,703 SNVs/InDels, 19,192 truncations, 17,779 amplifications, 1,688 homozygous deletions, and 3,111 fusions/rearrangements; 64% of patients harbored ≥1 OncoKB Level 1–4 actionable variant [PMID:35871175](../papers/35871175.md)

## Notes

- SNVs called by MuTect; InDels by Pindel; CNVs by EXCAVATOR; fusions by an in-house algorithm; all variants manually reviewed in IGV.
- PD-L1 IHC in this cohort used clone 28-8 (Abcam ab205921), distinct from the regulatory companion diagnostic clone 22C3.
- Panel covers ~2.6 Mb, limiting mutational-signature and HRD analyses compared with WGS/WES.
- TMB calculated by an in-house algorithm; values are panel-specific and not portable between assays.

## Sources

- [PMID:35871175](../papers/35871175.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
