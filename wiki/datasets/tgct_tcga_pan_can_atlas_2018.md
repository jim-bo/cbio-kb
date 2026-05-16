---
name: Testicular Germ Cell Tumors (TCGA, PanCancer Atlas 2018)
studyId: tgct_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 150
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - tgct
  - testicular
  - germ-cell
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-16
---

# Testicular Germ Cell Tumors (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Testicular Germ Cell Tumors PanCancer Atlas 2018 cohort is the [TGCT](../cancer_types/TGCT.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `tgct_tcga_pan_can_atlas_2018`. It covers approximately 150 testicular germ cell tumor samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. [TGCT](../cancer_types/TGCT.md) shows the strongest enrichment of both mRNA- and DNA-methylation-based stemness signatures in the pan-cancer analysis. Cell-cycle pathway is rarely altered in TGCT (alongside [LAML](../cancer_types/LAML.md), [THYM](../cancer_types/THYM.md), [UVM](../cancer_types/UVM.md)). Non-seminoma TGCT has among the lowest actionable-alteration rates (8.5% OncoKB Level 1/2A).

## Composition

- Cancer type: Testicular Germ Cell Tumors ([TGCT](../cancer_types/TGCT.md)), OncoTree code TGCT.
- Approximately 150 tumor samples; includes seminoma and non-seminoma subtypes.
- Data modalities: WES, RNA-seq, SNP array.
- Somatic mutations from MC3 ensemble pipeline.
- Copy-number from Affymetrix SNP 6.0 / ABSOLUTE.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)

## Papers using this cohort

- [PMID:29625048](../papers/29625048.md) — TCGA PanCancer Atlas integrative molecular analysis (Hoadley et al., 2018)

## Notable findings derived from this cohort

- TGCT shows the strongest enrichment of both mRNA-based and DNA-methylation-based stemness signatures across all 33 TCGA cancer types (Malta et al. 2018 companion to the pan-cancer analysis); LAML is enriched only for the mRNA-based stemness signature. [PMID:29625048](../papers/29625048.md)
- Cell-cycle pathway rarely altered in TGCT (alongside UVM, THYM, LAML) per pan-cancer pathway analysis. [PMID:29625048](../papers/29625048.md)
- Testicular non-seminoma has 8.5% OncoKB Level 1/2A actionable-alteration frequency — among the lowest rates pan-cancer (alongside UVM at 2.5%). [PMID:29625048](../papers/29625048.md)

## Sources

- cBioPortal study: `tgct_tcga_pan_can_atlas_2018`
- [PMID:29625048](../papers/29625048.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
