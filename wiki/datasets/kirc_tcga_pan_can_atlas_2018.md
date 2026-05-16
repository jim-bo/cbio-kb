---
name: Kidney Renal Clear Cell Carcinoma (TCGA, PanCancer Atlas 2018)
studyId: kirc_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 538
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - kirc
  - kidney
  - renal-clear-cell
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-16
---

# Kidney Renal Clear Cell Carcinoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Kidney Renal Clear Cell Carcinoma PanCancer Atlas 2018 cohort is the [KIRC](../cancer_types/KIRC.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `kirc_tcga_pan_can_atlas_2018`. It covers approximately 538 kidney renal clear cell carcinoma samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. [KIRC](../cancer_types/KIRC.md) co-clusters with [KIRP](../cancer_types/KIRP.md) in the pan-kidney iCluster C28, which is enriched for hypoxia, retinoid metabolism, PPAR-RXR, and immune checkpoints PD-1/CTLA4 pathways. KIRC is among the cancer types with low rates of actionable alterations per pan-cancer pathway analysis.

## Composition

- Cancer type: Kidney Renal Clear Cell Carcinoma ([KIRC](../cancer_types/KIRC.md)), OncoTree code KIRC.
- Approximately 538 tumor samples.
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

- KIRC and [KIRP](../cancer_types/KIRP.md) co-cluster almost entirely in pan-kidney iCluster C28; this pan-kidney iCluster is enriched for hypoxia, retinoid metabolism, PPAR-RXR signaling, and immune checkpoint genes [PDCD1](../genes/PDCD1.md) (PD-1) and [CTLA4](../genes/CTLA4.md), supporting immunotherapy susceptibility of clear cell [RCC](../cancer_types/RCC.md). [PMID:29625048](../papers/29625048.md)
- KIRC shows low rates of actionable alterations per pan-cancer pathway analysis; KIRC is among the cancer types with low OncoKB Level 1/2A actionable-alteration frequency. [PMID:29625049](../papers/29625049.md)
- Pan-cancer somatic driver network includes KIRC; Ras-pathway mutual exclusivity preserved across 33 cancer types including KIRC. [PMID:29625049](../papers/29625049.md)

## Sources

- cBioPortal study: `kirc_tcga_pan_can_atlas_2018`
- [PMID:29625048](../papers/29625048.md)
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
