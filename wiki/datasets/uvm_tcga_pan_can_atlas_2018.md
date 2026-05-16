---
name: Uveal Melanoma (TCGA, PanCancer Atlas 2018)
studyId: uvm_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 80
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - uvm
  - uveal-melanoma
  - eye
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-16
---

# Uveal Melanoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Uveal Melanoma PanCancer Atlas 2018 cohort is the [UVM](../cancer_types/UVM.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `uvm_tcga_pan_can_atlas_2018`. It covers approximately 80 uveal melanoma samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. [UVM](../cancer_types/UVM.md) co-clusters with [SKCM](../cancer_types/SKCM.md) in the high-mutation iCluster C15 (UVB signature); [GNAQ](../genes/GNAQ.md)/[GNA11](../genes/GNA11.md) mutual exclusivity dominates UVM's driver landscape. UVM has the lowest actionable-alteration rate (2.5% OncoKB Level 1/2A) of any cancer type in the pan-cancer cohort. Cell-cycle pathway rarely altered in UVM.

## Composition

- Cancer type: Uveal Melanoma ([UVM](../cancer_types/UVM.md)), OncoTree code [UM](../cancer_types/UM.md).
- Approximately 80 tumor samples.
- Data modalities: WES, RNA-seq, SNP array.
- Somatic mutations from MC3 ensemble pipeline; relatively low mutation burden compared to cutaneous SKCM.
- Copy-number from Affymetrix SNP 6.0 / ABSOLUTE.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)

## Papers using this cohort

- [PMID:29625048](../papers/29625048.md) — TCGA PanCancer Atlas integrative molecular analysis (Hoadley et al., 2018)
- [PMID:29625049](../papers/29625049.md) — TCGA PanCancer Atlas pan-cancer driver and germline analysis (Ding et al., 2018)

## Notable findings derived from this cohort

- UVM co-clusters with SKCM in pan-cancer iCluster C15 (C15:SKCM/UVM, UVB mutational signature drives highest mutation rates in this iCluster). [PMID:29625048](../papers/29625048.md)
- [GNAQ](../genes/GNAQ.md)/[GNA11](../genes/GNA11.md) homologous pair shows strong mutual exclusivity dominating UVM's driver landscape; this pair exclusivity is maintained pan-cancer and represents a hallmark of UVM biology. [PMID:29625049](../papers/29625049.md)
- UVM has the lowest actionable-alteration rate (2.5% OncoKB Level 1/2A) of any cancer type pan-cancer; cell-cycle pathway rarely altered in UVM. [PMID:29625049](../papers/29625049.md)
- Stage-specific Cox HRs not significantly different by any endpoint in TCGA-CDR (alongside [MESO](../cancer_types/MESO.md) and [PAAD](../cancer_types/PAAD.md)); despite this, pan-cancer driver network includes UVM. [PMID:29625048](../papers/29625048.md)

## Sources

- cBioPortal study: `uvm_tcga_pan_can_atlas_2018`
- [PMID:29625048](../papers/29625048.md)
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
