---
name: Thymoma (TCGA, PanCancer Atlas 2018)
studyId: thym_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 124
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - thym
  - thymoma
  - thymus
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-16
---

# Thymoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Thymoma PanCancer Atlas 2018 cohort is the [THYM](../cancer_types/THYM.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `thym_tcga_pan_can_atlas_2018`. It covers approximately 124 thymoma samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. [THYM](../cancer_types/THYM.md) is among cancer types with low cell-cycle pathway alteration rates and low actionable-alteration rates per pan-cancer analysis. TCGA-CDR recommends only one endpoint (PFI with caution) for THYM.

## Composition

- Cancer type: Thymoma ([THYM](../cancer_types/THYM.md)), OncoTree code THYM.
- Approximately 124 tumor samples.
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

- THYM included in pan-cancer integrative molecular analysis (33 cancer types, 11,286 tumors); part of iCluster C8: UCEC-dominated cluster (immune/stromal context); cell-cycle pathway rarely altered in THYM (alongside [UVM](../cancer_types/UVM.md), [TGCT](../cancer_types/TGCT.md), [LAML](../cancer_types/LAML.md)). [PMID:29625048](../papers/29625048.md)
- TCGA-CDR endpoint recommendations for THYM: only one endpoint can be recommended (PFI used with caution, alongside DLBC and LAML). [PMID:29625048](../papers/29625048.md)
- THYM is among cancer types with low actionable-alteration rates per pan-cancer pathway analysis. [PMID:29625048](../papers/29625048.md)

## Sources

- cBioPortal study: `thym_tcga_pan_can_atlas_2018`
- [PMID:29625048](../papers/29625048.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
