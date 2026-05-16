---
name: Ovarian Serous Cystadenocarcinoma (TCGA, PanCancer Atlas 2018)
studyId: ov_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 585
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - ov
  - ovarian
  - serous
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-16
---

# Ovarian Serous Cystadenocarcinoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Ovarian Serous Cystadenocarcinoma PanCancer Atlas 2018 cohort is the [OV](../cancer_types/OV.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `ov_tcga_pan_can_atlas_2018`. It covers approximately 585 ovarian serous cystadenocarcinoma samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. C6:[OV](../cancer_types/OV.md) was one of eight pan-cancer iClusters dominated by a single tumor type. OV is the cancer type most skewed toward genome-integrity disruption in both germline and somatic compartments, driven by BRCA1/BRCA2 germline variants and high-frequency [TP53](../genes/TP53.md) mutation. PFI is the preferred endpoint for OV per TCGA-CDR.

## Composition

- Cancer type: Ovarian Serous Cystadenocarcinoma ([OV](../cancer_types/OV.md)), OncoTree code [OVT](../cancer_types/OVT.md).
- Approximately 585 tumor samples.
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
- [PMID:29625055](../papers/29625055.md) — TCGA Pan-Cancer Clinical Data Resource (Liu et al., 2018)

## Notable findings derived from this cohort

- C6:OV was one of eight pan-cancer iClusters dominated by a single tumor type; [ESR1](../genes/ESR1.md) (ER-α), [AR](../genes/AR.md), and [IGFBP2](../genes/IGFBP2.md) high-expression RPPA groups include OV samples with luminal gene programs. [PMID:29625048](../papers/29625048.md)
- OV is the cancer type most skewed toward genome-integrity disruption in both germline and somatic compartments, driven by [BRCA1](../genes/BRCA1.md)/[BRCA2](../genes/BRCA2.md) germline variants (FDR 9.12e-6) and near-ubiquitous [TP53](../genes/TP53.md) mutation; germline [BRCA1](../genes/BRCA1.md)/[BRCA2](../genes/BRCA2.md) carriers showed ~8 years earlier onset (P=2.07e-10). [PMID:29625049](../papers/29625049.md)
- TCGA-CDR recommends PFI as the primary endpoint for OV; all four endpoints ([OS](../cancer_types/OS.md), PFI, DFI, DSS) are recommended without reservation, making OV one of 13 cancer types with the highest endpoint reliability. [PMID:29625055](../papers/29625055.md)

## Sources

- cBioPortal study: `ov_tcga_pan_can_atlas_2018`
- [PMID:29625048](../papers/29625048.md)
- [PMID:29625049](../papers/29625049.md)
- [PMID:29625055](../papers/29625055.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
