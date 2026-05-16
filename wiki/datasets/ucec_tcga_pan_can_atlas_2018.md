---
name: Uterine Corpus Endometrial Carcinoma (TCGA, PanCancer Atlas 2018)
studyId: ucec_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 529
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - ucec
  - uterine
  - endometrial
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-16
---

# Uterine Corpus Endometrial Carcinoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Uterine Corpus Endometrial Carcinoma PanCancer Atlas 2018 cohort is the [UCEC](../cancer_types/UCEC.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `ucec_tcga_pan_can_atlas_2018`. It covers approximately 529 uterine corpus endometrial carcinoma samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. C8:[UCEC](../cancer_types/UCEC.md) was one of eight pan-cancer iClusters dominated by a single tumor type, with POLE-mutation-driven hypermutation enriched in this iCluster. UCEC is notable for the highest PI3K-pathway alteration rates among CN-low (95%) and CN-high (86%) non-hypermutated subtypes, and for HER2+PI3K co-targeting opportunity in 7% of CN-high UCEC. All four clinical endpoints are recommended without reservation for UCEC by TCGA-CDR.

## Composition

- Cancer type: Uterine Corpus Endometrial Carcinoma ([UCEC](../cancer_types/UCEC.md)), OncoTree code UCEC.
- Approximately 529 tumor samples; encompasses POLE-ultramutated, MSI-high, copy-number-low, and copy-number-high molecular subtypes.
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

- C8:UCEC was one of eight pan-cancer iClusters dominated by a single tumor type; [POLE](../genes/POLE.md)-mutation signatures enriched in hypermutated C8:UCEC; [ESR1](../genes/ESR1.md) (ER-α)/AR/IGFBP2 RPPA groups include UCEC samples with luminal/estrogen-signaling programs alongside [BRCA](../cancer_types/BRCA.md), [OV](../cancer_types/OV.md), and [LIHC](../cancer_types/LIHC.md). [PMID:29625048](../papers/29625048.md)
- [TP53](../genes/TP53.md) drives one of two mutually-exclusive UCEC driver networks (with [PPP2R1A](../genes/PPP2R1A.md)); [TP53](../genes/TP53.md) mutually exclusive with [PIK3CA](../genes/PIK3CA.md), [HRAS](../genes/HRAS.md), [CTNNB1](../genes/CTNNB1.md), [ARID1A](../genes/ARID1A.md), [FGFR3](../genes/FGFR3.md) pan-cancer; MSI-H UCEC tumors over-express immune effectors GZMA/PRF1/GZMK/GZMH (KS P<0.01). [PMID:29625049](../papers/29625049.md)
- PI3K pathway dominant in UCEC: non-hypermutated CN-low 95% and CN-high 86% alteration frequencies — highest in the pan-cancer cohort; HER2+PI3K co-targeting opportunity in 7% of CN-high UCEC. [PMID:29625049](../papers/29625049.md)
- [SOS1](../genes/SOS1.md) activating mutations present in ~1% of uterine carcinomas independent of subtype. [PMID:29625049](../papers/29625049.md)
- All four clinical endpoints ([OS](../cancer_types/OS.md), PFI, DFI, DSS) are recommended without reservation for UCEC by TCGA-CDR. [PMID:29625055](../papers/29625055.md)

## Sources

- cBioPortal study: `ucec_tcga_pan_can_atlas_2018`
- [PMID:29625048](../papers/29625048.md)
- [PMID:29625049](../papers/29625049.md)
- [PMID:29625055](../papers/29625055.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
