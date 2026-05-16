---
name: Breast Invasive Carcinoma (TCGA, PanCancer Atlas 2018)
studyId: brca_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 1084
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - brca
  - breast
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Breast Invasive Carcinoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Breast Invasive Carcinoma PanCancer Atlas 2018 cohort is the breast cancer arm of the TCGA PanCancer Atlas, available in cBioPortal as `brca_tcga_pan_can_atlas_2018`. It encompasses approximately 1,084 breast invasive carcinoma samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number profiles, and RNA-seq expression. The cohort spans all major molecular subtypes (luminal A, luminal B, HER2-enriched, basal-like, and claudin-low).

## Composition

- Cancer type: Breast Invasive Carcinoma ([BRCA](../cancer_types/BRCA.md)), OncoTree code [BRCA](../cancer_types/BRCA.md).
- Approximately 1,084 tumor samples.
- Data modalities: WES, RNA-seq, SNP array.
- Somatic mutations from MC3 ensemble pipeline; BRCA showed >90% concordance with legacy PanCan12 calls.
- Copy-number from Affymetrix SNP 6.0 / ABSOLUTE; includes HER2-amplified, copy-number-high basal, and diploid luminal subtypes.

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

- Pan-cancer RNA-seq fusion analysis (9,624 TCGA tumors) identified 9 [ESR1](../genes/ESR1.md) fusions in BRCA (8 luminal A/B), with strict mutual exclusivity with [ESR1](../genes/ESR1.md) point mutations; ESR1 expression was elevated in fusion-positive samples, suggesting a promoter-swap mechanism distinct from the resistance-associated ESR1 mutations seen in endocrine-treated metastatic BRCA [PMID:29617662](../papers/29617662.md).
- Four [ERBB2](../genes/ERBB2.md) fusions were identified across TCGA cancer types; 3 of 4 had HPV integration within 1 Mb of [ERBB2](../genes/ERBB2.md), with partner genes [PPP1R1B](../genes/PPP1R1B.md) and [IKZF3](../genes/IKZF3.md) being genomic neighbors suggesting local instability-driven rearrangement as an alternative mechanism of HER2 dysregulation distinct from amplification [PMID:29617662](../papers/29617662.md).
- Breast cancer (BRCA) had among the highest concordance (>90%) between MC3 mutation calls and the legacy PanCan12 MAF, indicating stable mutation calling across pipeline versions for this tumor type [PMID:29617662](../papers/29617662.md).
- Pan-cancer aneuploidy analysis placed BRCA in the epithelial cluster (alongside [LUAD](../cancer_types/LUAD.md) and [HCC](../cancer_types/HCC.md)) defined by 1q gain; copy-number-high serous-like endometrial cancers cluster with BRCA basal-like as a notable inter-disease grouping [PMID:29617662](../papers/29617662.md).
- BRCA samples contributed to the pan-cancer integrative molecular analysis; ERBB2-amplified C2 iCluster spanned BRCA, BLCA, and STAD; C19:BRCA (luminal) dominated by ER-α/AR signaling; HER2-enriched BRCA highlighted for cross-tissue actionability [PMID:29625048](../papers/29625048.md)
- BRCA cohort used in pan-cancer germline-somatic analysis; BRCA1/2 germline carriers had mean onset ~8 years earlier than somatic-only carriers (P=2.07e-10, FDR 1.15e-2 for BRCA); GATA3 frameshift/nonsense alleles show gain-of-function mRNA upregulation (FDR=4.54e-18) [PMID:29625049](../papers/29625049.md)
- BRCA cohort included in pan-cancer pathway analysis; RTK-RAS pathway altered in 82% of HER2-enriched BRCA; luminal-A BRCA leads OncoKB Level 3A actionability (PIK3CA, AKT1, ERBB2 mutations); HER2+PI3K co-targeting opportunity in 17% of HER2-enriched BRCA [PMID:29625050](../papers/29625050.md)
- BRCA cohort used in TCGA Pan-Cancer Clinical Data Resource (TCGA-CDR); PFI recommended over OS for BRCA (ER+ better than ER- for PFI p=0.005, DFI p=0.001, DSS p=0.009; OS not significant p=0.097); TCGA-CDR provides the canonical OS/PFI/DFI/DSS annotations for this cBioPortal study [PMID:29625055](../papers/29625055.md)

## Sources

- cBioPortal study: `brca_tcga_pan_can_atlas_2018`
- [PMID:29617662](../papers/29617662.md)
- [PMID:29625048](../papers/29625048.md)
- [PMID:29625049](../papers/29625049.md)
- [PMID:29625050](../papers/29625050.md)
- [PMID:29625055](../papers/29625055.md)

*This page was processed by **entity-page-writer** on **2026-05-16**.*
