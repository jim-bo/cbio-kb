---
name: Mesothelioma (TCGA, PanCancer Atlas 2018)
studyId: meso_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 87
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - meso
  - mesothelioma
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-16
---

# Mesothelioma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Mesothelioma PanCancer Atlas 2018 cohort is the [MESO](../cancer_types/MESO.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `meso_tcga_pan_can_atlas_2018`. It covers approximately 87 mesothelioma samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. [MESO](../cancer_types/MESO.md) is among the cancer types with low rates of actionable alterations per pan-cancer pathway analysis, and stage-specific Cox hazard ratios are not significantly different by any endpoint in TCGA-CDR.

## Composition

- Cancer type: Mesothelioma ([MESO](../cancer_types/MESO.md)), OncoTree code MESO.
- Approximately 87 tumor samples.
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

- MESO included in pan-cancer integrative molecular analysis (33 cancer types, 11,286 tumors); part of the heterogeneous iCluster C20: mixed (stromal/immune) which spans 25 of 33 tumor types. [PMID:29625048](../papers/29625048.md)
- MESO is among cancer types with low actionable-alteration rates; stage-specific Cox HRs not significantly different by [OS](../cancer_types/OS.md), PFI, or DSS in TCGA-CDR (alongside [PAAD](../cancer_types/PAAD.md) and [UVM](../cancer_types/UVM.md)), indicating these endpoints may not reliably separate stage groups. [PMID:29625048](../papers/29625048.md)

## Sources

- cBioPortal study: `meso_tcga_pan_can_atlas_2018`
- [PMID:29625048](../papers/29625048.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
