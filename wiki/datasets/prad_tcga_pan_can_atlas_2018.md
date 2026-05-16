---
name: Prostate Adenocarcinoma (TCGA, PanCancer Atlas 2018)
studyId: prad_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 499
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - prad
  - prostate
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Prostate Adenocarcinoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Prostate Adenocarcinoma PanCancer Atlas 2018 cohort is the prostate cancer arm of the TCGA PanCancer Atlas, available in cBioPortal as `prad_tcga_pan_can_atlas_2018`. It covers prostate adenocarcinoma samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number profiles, and RNA-seq expression. Prostate cancer in TCGA is predominantly primary, treatment-naive disease; the meta-cohort [prad_p1000](../datasets/prad_p1000.md) augments this with metastatic samples.

## Composition

- Cancer type: Prostate Adenocarcinoma ([PRAD](../cancer_types/PRAD.md)), OncoTree code [PRAD](../cancer_types/PRAD.md).
- Approximately 499 tumor samples.
- Data modalities: WES, RNA-seq, SNP array.
- Somatic mutations from MC3 ensemble pipeline.
- Copy-number from Affymetrix SNP 6.0 / ABSOLUTE.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)

## Papers using this cohort

- [PMID:29617662](../papers/29617662.md) — Pan-cancer fusion catalog (Gao et al., 2018)
- [PMID:29625048](../papers/29625048.md) — TCGA PanCancer Atlas integrative molecular analysis (Hoadley et al., 2018)
- [PMID:29625049](../papers/29625049.md) — TCGA PanCancer Atlas pan-cancer driver and germline analysis (Ding et al., 2018)
- [PMID:29625050](../papers/29625050.md) — TCGA PanCancer Atlas oncogenic pathway analysis (Sanchez-Vega et al., 2018)
- [PMID:29625055](../papers/29625055.md) — TCGA Pan-Cancer Clinical Data Resource (Liu et al., 2018)

## Notable findings derived from this cohort

- [TMPRSS2](../genes/TMPRSS2.md)-[ERG](../genes/ERG.md) is the most-recurrent intra-cancer fusion in the entire TCGA pan-cancer cohort, occurring in 38.2% of PRAD samples (205 samples); all 205 are flagged as harboring a druggable fusion per DEPO annotation, making PRAD the single largest contributor to the pan-cancer druggable-fusion count (6.0% of pan-cancer samples overall) [PMID:29617662](../papers/29617662.md).
- [TMPRSS2](../genes/TMPRSS2.md)-[ERG](../genes/ERG.md) fusions predicted a mean of approximately 1.5 fusion-derived neoantigens per fusion-bearing sample (range varies by specific breakpoint), with the majority being inframe fusions yielding fewer epitopes than frameshifts [PMID:29617662](../papers/29617662.md).
- In the pan-cancer analysis spanning this cohort, PRAD had a median of 1 fusion per sample (pan-cancer median), but the TMPRSS2-ERG fusion drives a strong enrichment of the ETS-family fusion subtype specific to prostate epithelium [PMID:29617662](../papers/29617662.md).
- PRAD samples in pan-cancer integrative analysis; C16:PRAD was one of eight iClusters dominated by a single tumor type; high AR-signaling gene programs in RPPA groups containing PRAD [PMID:29625048](../papers/29625048.md)
- PRAD included in pan-cancer driver and germline analysis; somatic-somatic co-occurrence and mutual-exclusivity tested across 33 cancer types including PRAD [PMID:29625049](../papers/29625049.md)
- PRAD included in pan-cancer pathway analysis; 57% of pan-cancer tumors carry at least one potentially targetable alteration across 10 canonical pathways [PMID:29625050](../papers/29625050.md)
- PRAD clinical annotations provided by TCGA-CDR; OS/PFI/DFI/DSS standardized across 33 cancer types including PRAD; date of diagnosis used as t=0 for all endpoints [PMID:29625055](../papers/29625055.md)

## Sources

- cBioPortal study: `prad_tcga_pan_can_atlas_2018`
- [PMID:29617662](../papers/29617662.md)
- [PMID:29625048](../papers/29625048.md)
- [PMID:29625049](../papers/29625049.md)
- [PMID:29625050](../papers/29625050.md)
- [PMID:29625055](../papers/29625055.md)

*This page was processed by **entity-page-writer** on **2026-05-16**.*
