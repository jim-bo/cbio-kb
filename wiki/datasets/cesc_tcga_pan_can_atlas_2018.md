---
name: Cervical Squamous Cell Carcinoma and Endocervical Adenocarcinoma (TCGA, PanCancer Atlas 2018)
studyId: cesc_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas
size: 309
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [bulk-rna-seq, snp-microarray, targeted-panel]
panels: []
tags: [cervical-cancer, cesc, tcga, pan-can-atlas]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Cervical Squamous Cell Carcinoma and Endocervical Adenocarcinoma (TCGA, PanCancer Atlas 2018)

## Overview

TCGA PanCancer Atlas 2018 dataset for cervical squamous cell carcinoma and endocervical adenocarcinoma ([CESC](../cancer_types/CESC.md)). Used as a reference/comparison cohort in genomic landscape studies of cervical cancer. [PMID:37643132](../papers/37643132.md)

## Composition

- TCGA multi-platform genomic profiling of cervical squamous cell carcinoma and endocervical adenocarcinoma. [PMID:37643132](../papers/37643132.md)
- Used as a comparison dataset against MSK cohort ([cervix_msk_2023](../datasets/cervix_msk_2023.md)) for mutation frequency analysis. [PMID:37643132](../papers/37643132.md)
- [KRAS](../genes/KRAS.md) mutation frequency in TCGA was 5%, significantly lower than the MSK cohort (12%, P=0.019). [PMID:37643132](../papers/37643132.md)

## Assays / panels (linked)

- Multi-platform TCGA profiling: whole-exome sequencing, RNA-seq, copy-number arrays. [PMID:37643132](../papers/37643132.md)

## Papers using this cohort

- [PMID:37643132](../papers/37643132.md) — Assessing the Genomic Landscape of Cervical Cancers: Clinical Opportunities and Therapeutic Targets.
- [PMID:29625048](../papers/29625048.md) — TCGA PanCancer Atlas integrative molecular analysis (Hoadley et al., 2018)
- [PMID:29625049](../papers/29625049.md) — TCGA PanCancer Atlas pan-cancer driver and germline analysis (Ding et al., 2018)
- [PMID:29625050](../papers/29625050.md) — TCGA PanCancer Atlas oncogenic pathway analysis (Sanchez-Vega et al., 2018)

## Notable findings derived from this cohort

- Served as a reference for mutation frequency comparisons in [CESC](../cancer_types/CESC.md); [KRAS](../genes/KRAS.md) mutations were 5% in TCGA vs. 12% in the MSK cohort, highlighting potential enrichment in a clinical cancer center population. [PMID:37643132](../papers/37643132.md)
- MC3 ensemble mutation calls (7 callers, 10,510 TCGA tumor/normal pairs, 33 cancer types) form the somatic-variant backbone of this PanCanAtlas cBioPortal study [PMID:29596782](../papers/29596782.md)
- Pan-cancer aneuploidy analysis of 10,522 TCGA tumors placed this cohort in the squamous cluster (3p loss, 3q gain) alongside LUSC, ESCC, and HPV-negative HNSC [PMID:29622463](../papers/29622463.md)
- CESC samples contributed to pan-cancer integrative clustering; HPV+ CESC co-clusters with pan-squamous iCluster C27 (with HPV+ HNSC and some BLCA); 80%+ samples fell into a single iCluster [PMID:29625048](../papers/29625048.md)
- CESC included in pan-cancer somatic driver network; ERBB2 alterations in 23% of CESC; LUSC (a pan-squamous neighbor) showed highest somatic vs germline genome-integrity disruption ratio [PMID:29625049](../papers/29625049.md)
- CESC included in pan-cancer pathway analysis (9,125 tumors); CESC cervical adenocarcinoma subtype shows HER2+PI3K co-targeting opportunity in ~7% of samples [PMID:29625050](../papers/29625050.md)
- Used as part of the TCGA PanCancer Atlas cohort in a pan-cancer analysis of oncogenic signaling pathways across 9,125 tumors from 33 cancer types [PMID:29850653](../papers/29850653.md)

## Sources

- cBioPortal study `cesc_tcga_pan_can_atlas_2018` [PMID:37643132](../papers/37643132.md).
- [PMID:29596782](../papers/29596782.md)
- [PMID:29622463](../papers/29622463.md)
- [PMID:29625048](../papers/29625048.md)
- [PMID:29625049](../papers/29625049.md)
- [PMID:29625050](../papers/29625050.md)

*This page was processed by **entity-page-writer** on **2026-05-16**.*
- [PMID:29850653](../papers/29850653.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
