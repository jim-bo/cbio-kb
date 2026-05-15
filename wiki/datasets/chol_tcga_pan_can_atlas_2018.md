---
name: Cholangiocarcinoma (TCGA, PanCancer Atlas 2018)
studyId: chol_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 51
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - chol
  - cholangiocarcinoma
  - bile-duct
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-15
---

# Cholangiocarcinoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Cholangiocarcinoma PanCancer Atlas 2018 cohort is the [CHOL](../cancer_types/CHOL.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `chol_tcga_pan_can_atlas_2018`. It covers cholangiocarcinoma (bile duct cancer) samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. CHOL is a relatively small TCGA disease cohort (~51 samples) but is notable for harboring the highest rate of the recurrent [FGFR2](../genes/FGFR2.md)-[BICC1](../genes/BICC1.md) fusion, an actionable target with approved FGFR inhibitors.

## Composition

- Cancer type: Cholangiocarcinoma ([CHOL](../cancer_types/CHOL.md)), OncoTree code CHOL.
- Approximately 51 tumor samples.
- Data modalities: WES, RNA-seq, SNP array.
- Somatic mutations from MC3 ensemble pipeline.
- Copy-number from Affymetrix SNP 6.0 / ABSOLUTE.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)

## Papers using this cohort

- [PMID:29617662](../papers/29617662.md) — Pan-cancer fusion catalog (Gao et al., 2018)

## Notable findings derived from this cohort

- [FGFR2](../genes/FGFR2.md)-[BICC1](../genes/BICC1.md) is the most recurrent fusion in CHOL (5.6% of samples), the highest rate of this specific fusion in any TCGA disease type; [FGFR2](../genes/FGFR2.md) is among the most recurrent 5′-kinase fusion partners in the pan-cancer landscape, actionable with FGFR inhibitors [PMID:29617662](../papers/29617662.md).
- Pan-cancer RNA-seq fusion analysis (9,624 TCGA tumors) identified CHOL as having cancer-type-specific enrichment of FGFR2 fusions with intact kinase domains; FGFR2 and [FGFR3](../genes/FGFR3.md) together dominate the 5′-kinase recurrent fusion set across all 33 TCGA cancer types [PMID:29617662](../papers/29617662.md).

## Sources

- cBioPortal study: `chol_tcga_pan_can_atlas_2018`
- [PMID:29617662](../papers/29617662.md)

*This page was processed by **crosslinker** on **2026-05-15**.*
