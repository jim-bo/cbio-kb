---
name: TCGA Pan-Cancer Atlas Colorectal Adenocarcinoma 2018
studyId: coadread_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 526
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - colorectal
  - TCGA
  - pan-cancer
  - copy-number
processed_by: wiki-cli
processed_at: 2026-05-16
---

# TCGA Pan-Cancer Atlas Colorectal Adenocarcinoma 2018

## Overview

The TCGA Pan-Cancer Atlas colorectal adenocarcinoma cohort, accessed via cBioPortal, comprising 526 cases profiled with whole-exome sequencing, RNA-seq, and SNP arrays as part of the broader TCGA Pan-Cancer Atlas initiative. Widely used as a reference cohort for copy number, mutation frequency, and survival analyses in colorectal cancer.

## Composition

- 526 colorectal adenocarcinoma ([COADREAD](../cancer_types/COADREAD.md)) cases.
- Includes colon ([COAD](../cancer_types/COAD.md)) and rectal ([READ](../cancer_types/READ.md)) adenocarcinomas.
- Multi-omic profiling: whole-exome sequencing, copy number (SNP array), RNA-seq.
- Accessible via cBioPortal.

## Assays / panels (linked)

- Whole-exome sequencing (WES)
- RNA-seq
- SNP array (copy number)

## Papers using this cohort

- [PMID:36334560](../papers/36334560.md) — Bioinformatic analysis of [FBXO7](../genes/FBXO7.md) copy number loss in CRC; 526 cases used for copy number, expression, and survival analyses.
- [PMID:29625048](../papers/29625048.md) — TCGA PanCancer Atlas integrative molecular analysis (Hoadley et al., 2018)
- [PMID:29625049](../papers/29625049.md) — TCGA PanCancer Atlas pan-cancer driver and germline analysis (Ding et al., 2018)
- [PMID:29625050](../papers/29625050.md) — TCGA PanCancer Atlas oncogenic pathway analysis (Sanchez-Vega et al., 2018)

## Notable findings derived from this cohort

- FBXO7 shallow deletions (heterozygous loss) occur in 32.5% (169/526) of CRC cases; deep deletions are rare (<0.2%); FBXO7 shallow deletions associate with increased genome instability (fraction altered, aneuploidy score, tumor break load; q < 0.0001) and worse overall, progression-free, and disease-specific survival (log rank, p < 0.05) [PMID:36334560](../papers/36334560.md).
- MC3 ensemble mutation calls (7 callers, 10,510 TCGA tumor/normal pairs, 33 cancer types) form the somatic-variant backbone of this PanCanAtlas cBioPortal study [PMID:29596782](../papers/29596782.md)
- Pan-cancer aneuploidy analysis of 10,522 TCGA tumors used this cohort as part of the gastrointestinal cluster (COAD/READ) analysis of arm-level copy-number alterations [PMID:29622463](../papers/29622463.md)
- COAD/READ samples contributed to pan-cancer iCluster analysis; C4:pan-GI (CRC, chromosomal instability) and C18:pan-GI (MSI, STAD+COAD) were two of the 28 identified integrative subtypes; C1:STAD (EBV-CIMP) also contains CRC tumors [PMID:29625048](../papers/29625048.md)
- COADREAD used in pan-cancer driver interaction analysis; TP53 and KRAS are mutually exclusive in COAD/READ (but co-occur in PAAD); MSI-H COADREAD tumors over-express GZMA/PRF1/GZMK/GZMH (KS P<0.01); C4:pan-GI enriched for POLE signatures [PMID:29625049](../papers/29625049.md)
- COADREAD included in pan-cancer pathway analysis; KRAS hotspots in colorectal GS subtype at 69% frequency; C4:pan-GI (CRC with CIN) and MSI-H subtypes carry highest pathway alteration frequency dominated by inactivating mutations [PMID:29625050](../papers/29625050.md)

## Sources

- cBioPortal study: `coadread_tcga_pan_can_atlas_2018`
- [PMID:29596782](../papers/29596782.md)
- [PMID:29622463](../papers/29622463.md)
- [PMID:29625048](../papers/29625048.md)
- [PMID:29625049](../papers/29625049.md)
- [PMID:29625050](../papers/29625050.md)

*This page was processed by **entity-page-writer** on **2026-05-16**.*
