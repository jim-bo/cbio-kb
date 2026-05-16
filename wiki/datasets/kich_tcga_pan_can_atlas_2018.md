---
name: Kidney Chromophobe (TCGA, PanCancer Atlas 2018)
studyId: kich_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 66
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - kich
  - kidney
  - chromophobe
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-16
---

# Kidney Chromophobe (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Kidney Chromophobe PanCancer Atlas 2018 cohort is the [KICH](../cancer_types/KICH.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `kich_tcga_pan_can_atlas_2018`. It covers approximately 66 kidney chromophobe samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. [KICH](../cancer_types/KICH.md) is notable for its hypodiploid copy-number profile, which caused it to co-cluster with adrenocortical carcinoma ([ACC](../cancer_types/ACC.md)) in pan-cancer integrative analyses despite having no histologic relationship. KICH also has the longest median follow-up (~48 months) in the TCGA PanCancer Atlas cohort.

## Composition

- Cancer type: Kidney Chromophobe ([KICH](../cancer_types/KICH.md)), OncoTree code KICH.
- Approximately 66 tumor samples.
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

- KICH co-clustered with [ACC](../cancer_types/ACC.md) in pan-cancer iCluster C9 due to shared hypodiploid copy-number profiles; this cross-tissue grouping is a notable example where chromosomal architecture overrides tissue-of-origin signal. [PMID:29625048](../papers/29625048.md)
- Pan-kidney iClusters ([KIRC](../cancer_types/KIRC.md)+[KIRP](../cancer_types/KIRP.md) in C28; KICH in C9 with [ACC](../cancer_types/ACC.md)) are an important pan-cancer finding: KICH does not co-cluster with its kidney-organ siblings due to distinct chromosomal architecture. [PMID:29625048](../papers/29625048.md)
- KICH has the longest median follow-up (~48 months) in the TCGA PanCancer Atlas, enabling reliable endpoint assessment; however, PFI is recommended "with caution" (not without reservation) for KICH by TCGA-CDR. [PMID:29625049](../papers/29625049.md)
- Cell-cycle pathway rarely altered in KICH (alongside [UVM](../cancer_types/UVM.md), [THYM](../cancer_types/THYM.md), [TGCT](../cancer_types/TGCT.md), and [LAML](../cancer_types/LAML.md)) per pan-cancer pathway analysis. [PMID:29625049](../papers/29625049.md)

## Sources

- cBioPortal study: `kich_tcga_pan_can_atlas_2018`
- [PMID:29625048](../papers/29625048.md)
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
