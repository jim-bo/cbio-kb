---
name: Sarcoma (TCGA, PanCancer Atlas 2018)
studyId: sarc_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 261
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - sarc
  - sarcoma
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-16
---

# Sarcoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Sarcoma PanCancer Atlas 2018 cohort is the [SARC](../cancer_types/SARC.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `sarc_tcga_pan_can_atlas_2018`. It covers approximately 261 sarcoma samples (multiple histologic subtypes including dedifferentiated liposarcoma, leiomyosarcoma, synovial sarcoma, and others) with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. [SARC](../cancer_types/SARC.md) is notable for the [CDK4](../genes/CDK4.md)+[MDM2](../genes/MDM2.md) co-amplification co-targeting opportunity (78% of dedifferentiated liposarcomas) and for the disease-defining SS18/SSX1 or [SSX2](../genes/SSX2.md) fusions in synovial sarcoma. All four clinical endpoints are recommended without reservation for SARC by TCGA-CDR.

## Composition

- Cancer type: Sarcoma ([SARC](../cancer_types/SARC.md)), OncoTree code SARC; encompasses multiple histologic subtypes.
- Approximately 261 tumor samples.
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

- CDK4+MDM2 co-amplification co-targeting opportunity (CDK4 inhibitor + MDM2 inhibitor) identified in 78% of dedifferentiated liposarcomas in this cohort — one of the highest co-occurring actionable pair frequencies across all cancer types. [PMID:29625049](../papers/29625049.md)
- SS18/SSX1 or SSX2 fusions are disease-defining in synovial sarcoma; SARC included in the pan-cancer splicing and fusion driver landscape analysis identifying spliceosome pathway mutations across 8,656 tumors. [PMID:29625049](../papers/29625049.md)
- SARC included in pan-cancer integrative molecular analysis; part of C20: mixed (stromal/immune) iCluster with high stromal fraction. [PMID:29625048](../papers/29625048.md)
- All four clinical endpoints ([OS](../cancer_types/OS.md), PFI, DFI, DSS) are recommended without reservation for SARC by TCGA-CDR, making this one of 13 cancer types with the highest endpoint reliability. [PMID:29625048](../papers/29625048.md)

## Sources

- cBioPortal study: `sarc_tcga_pan_can_atlas_2018`
- [PMID:29625048](../papers/29625048.md)
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
