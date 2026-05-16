---
name: Kidney Renal Papillary Cell Carcinoma (TCGA, PanCancer Atlas 2018)
studyId: kirp_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 291
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - kirp
  - kidney
  - papillary
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-16
---

# Kidney Renal Papillary Cell Carcinoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Kidney Renal Papillary Cell Carcinoma PanCancer Atlas 2018 cohort is the [KIRP](../cancer_types/KIRP.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `kirp_tcga_pan_can_atlas_2018`. It covers approximately 291 kidney renal papillary cell carcinoma samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. [KIRP](../cancer_types/KIRP.md) co-clusters with [KIRC](../cancer_types/KIRC.md) in pan-kidney iCluster C28, enriched for hypoxia, PPAR-RXR, and immune checkpoint pathways. All four clinical endpoints ([OS](../cancer_types/OS.md), PFI, DFI, DSS) are recommended without reservation for KIRP by TCGA-CDR.

## Composition

- Cancer type: Kidney Renal Papillary Cell Carcinoma ([KIRP](../cancer_types/KIRP.md)), OncoTree code KIRP.
- Approximately 291 tumor samples.
- Data modalities: WES, RNA-seq, SNP array.
- Somatic mutations from MC3 ensemble pipeline.
- Copy-number from Affymetrix SNP 6.0 / ABSOLUTE.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)

## Papers using this cohort

- [PMID:29625048](../papers/29625048.md) — TCGA PanCancer Atlas integrative molecular analysis (Hoadley et al., 2018)
- [PMID:29625049](../papers/29625049.md) — TCGA PanCancer Atlas pan-cancer driver and germline analysis (Ding et al., 2018)

## Notable findings derived from this cohort

- KIRP and [KIRC](../cancer_types/KIRC.md) co-cluster almost entirely in pan-kidney iCluster C28; this pan-kidney iCluster is enriched for hypoxia, retinoid metabolism, PPAR-RXR signaling, and immune checkpoint genes [PDCD1](../genes/PDCD1.md) (PD-1) and [CTLA4](../genes/CTLA4.md). [PMID:29625048](../papers/29625048.md)
- All four clinical endpoints (OS, PFI, DFI, DSS) are recommended without reservation for KIRP by TCGA-CDR, making this one of 13 cancer types with the highest endpoint reliability. [PMID:29625049](../papers/29625049.md)
- Pan-cancer somatic driver network includes KIRP; Ras-pathway mutual exclusivity preserved across 33 cancer types including KIRP. [PMID:29625049](../papers/29625049.md)

## Sources

- cBioPortal study: `kirp_tcga_pan_can_atlas_2018`
- [PMID:29625048](../papers/29625048.md)
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
