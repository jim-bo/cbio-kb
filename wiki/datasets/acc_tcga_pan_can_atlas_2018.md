---
name: Adrenocortical Carcinoma (TCGA, PanCancer Atlas 2018)
studyId: acc_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 92
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - acc
  - adrenocortical
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-16
---

# Adrenocortical Carcinoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Adrenocortical Carcinoma PanCancer Atlas 2018 cohort is the [ACC](../cancer_types/ACC.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `acc_tcga_pan_can_atlas_2018`. It covers approximately 92 adrenocortical carcinoma samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. [ACC](../cancer_types/ACC.md) is one of the smaller TCGA disease cohorts but is notable for its hypodiploid copy-number profile that caused ACC to co-cluster with kidney chromophobe ([KICH](../cancer_types/KICH.md)) in pan-cancer integrative analyses.

## Composition

- Cancer type: Adrenocortical Carcinoma ([ACC](../cancer_types/ACC.md)), OncoTree code ACC.
- Approximately 92 tumor samples.
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

- ACC co-clustered with [KICH](../cancer_types/KICH.md) in pan-cancer iCluster C9, both characterized by a hypodiploid copy-number profile — a notable cross-tissue grouping driven by shared chromosomal architecture rather than histologic or lineage similarity. [PMID:29625048](../papers/29625048.md)
- Pan-cancer integrative molecular analysis (11,286 tumors, 33 cancer types) included ACC among the 33 TCGA PanCancer Atlas studies; single-platform clustering revealed ACC co-clusters with [KICH](../cancer_types/KICH.md) by aneuploidy pattern. [PMID:29625048](../papers/29625048.md)

## Sources

- cBioPortal study: `acc_tcga_pan_can_atlas_2018`
- [PMID:29625048](../papers/29625048.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
