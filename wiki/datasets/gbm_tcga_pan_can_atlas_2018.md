---
name: Glioblastoma Multiforme (TCGA, PanCancer Atlas 2018)
studyId: gbm_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 617
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - gbm
  - glioblastoma
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-15
---

# Glioblastoma Multiforme (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA [GBM](../cancer_types/GBM.md) PanCancer Atlas 2018 cohort is the glioblastoma multiforme arm of the TCGA PanCancer Atlas, curated under the canonical cBioPortal study ID `gbm_tcga_pan_can_atlas_2018`. It aggregates 617 GBM tumor samples with uniformly reprocessed somatic mutation calls (MC3 pipeline), copy-number segmentation (Affymetrix SNP 6.0 / ABSOLUTE), and RNA-seq expression. It is one of the 33 disease-type cohorts constituting the TCGA PanCancer Atlas released in 2018.

## Composition

- Cancer type: Glioblastoma Multiforme ([GBM](../cancer_types/GBM.md)), OncoTree code GBM.
- Approximately 617 tumor samples with matched normals.
- Data modalities: whole-exome sequencing (WES), RNA-seq (Illumina), SNP array copy-number (Affymetrix SNP 6.0).
- Somatic mutations from the MC3 ensemble pipeline (7 callers, open-access PASS MAF).
- Arm-level and focal copy-number calls derived via ABSOLUTE and GISTIC 2.0.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)

## Papers using this cohort

- [PMID:29596782](../papers/29596782.md) — MC3 mutation calling (Ellrott et al., 2018)
- [PMID:29617662](../papers/29617662.md) — Pan-cancer fusion catalog (Gao et al., 2018)
- [PMID:29622463](../papers/29622463.md) — Pan-cancer aneuploidy landscape (Taylor et al., 2018)

## Notable findings derived from this cohort

- MC3 ensemble mutation calls (7 callers, 10,510 TCGA tumor/normal pairs, 33 cancer types) form the somatic-variant backbone of this PanCanAtlas cBioPortal study; GBM samples showed low median SNV burden consistent with non-tobacco/UV exposure [PMID:29596782](../papers/29596782.md).
- Pan-cancer RNA-seq fusion analysis (9,624 TCGA tumors) spanned GBM as one of 33 disease types, with the GBM fusion landscape anchored to this dataset; GBM showed a median of 1 fusion per sample consistent with the pan-cancer median [PMID:29617662](../papers/29617662.md).
- Pan-cancer aneuploidy analysis of 10,522 TCGA tumors found GBM to have the highest rate of any arm-level aneuploidy (99% of samples, mean aneuploidy score 8.2), clustering in a neural-lineage group with [LGG](../cancer_types/LGG.md) characterized by chromosome 7 gain and chromosome 10 loss; IDH-wildtype GBM was specifically defined by this chr7-gain/chr10-loss pattern [PMID:29622463](../papers/29622463.md).

## Sources

- cBioPortal study: `gbm_tcga_pan_can_atlas_2018`
- [PMID:29596782](../papers/29596782.md)
- [PMID:29617662](../papers/29617662.md)
- [PMID:29622463](../papers/29622463.md)

*This page was processed by **crosslinker** on **2026-05-15**.*
