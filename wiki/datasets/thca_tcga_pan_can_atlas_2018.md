---
name: Thyroid Carcinoma (TCGA, PanCancer Atlas 2018)
studyId: thca_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 507
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - thca
  - thyroid
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Thyroid Carcinoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Thyroid Carcinoma PanCancer Atlas 2018 cohort is the thyroid arm of the TCGA PanCancer Atlas, available in cBioPortal as `thca_tcga_pan_can_atlas_2018`. It covers thyroid carcinoma samples with uniformly reprocessed somatic mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. Thyroid carcinoma is notable for having the lowest aneuploidy score and the highest rate of druggable kinase fusions in the pan-cancer landscape.

## Composition

- Cancer type: Thyroid Carcinoma ([THCA](../cancer_types/THCA.md)), OncoTree code [THCA](../cancer_types/THCA.md).
- Approximately 507 tumor samples.
- Data modalities: WES, RNA-seq, SNP array.
- Somatic mutations from MC3 ensemble pipeline.
- Copy-number from Affymetrix SNP 6.0 / ABSOLUTE; thyroid carcinoma has near-diploid profiles in most papillary cases.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)

## Papers using this cohort

- [PMID:29617662](../papers/29617662.md) — Pan-cancer fusion catalog (Gao et al., 2018)
- [PMID:29625048](../papers/29625048.md) — TCGA PanCancer Atlas integrative molecular analysis (Hoadley et al., 2018)
- [PMID:29625049](../papers/29625049.md) — TCGA PanCancer Atlas pan-cancer driver and germline analysis (Ding et al., 2018)
- [PMID:29625050](../papers/29625050.md) — TCGA PanCancer Atlas oncogenic pathway analysis (Sanchez-Vega et al., 2018)

## Notable findings derived from this cohort

- THCA is dramatically enriched for kinase fusions: 35.6% of THCA samples carry kinase fusions (Fisher p < 2.2e-16 vs. pan-cancer background), with 94.0% being 3′-kinase fusions that borrow a stronger upstream promoter; the top recurrent 3′-kinase partners are [RET](../genes/RET.md), [BRAF](../genes/BRAF.md), [NTRK1](../genes/NTRK1.md), [NTRK3](../genes/NTRK3.md), and [ALK](../genes/ALK.md) [PMID:29617662](../papers/29617662.md).
- [CCDC6](../genes/CCDC6.md)-[RET](../genes/RET.md) is the most recurrent fusion in THCA (4.2%); 33 THCA samples are flagged as harboring druggable fusions targeting [RET](../genes/RET.md) per DEPO annotation; both [RET](../genes/RET.md) and [NTRK](../genes/NTRK1.md) fusions occur as inframe 3′-kinase events with intact catalytic domains [PMID:29617662](../papers/29617662.md).
- THCA has among the lowest aneuploidy scores in the pan-cancer cohort (26% of samples with any arm-level event, mean score 0.87 — the lowest of all 33 TCGA disease types), consistent with the predominantly mutation/rearrangement-driven pathogenesis of papillary thyroid carcinoma [PMID:29617662](../papers/29617662.md).
- Median fusion burden in THCA is 0 (i.e., most samples have no detected fusions outside of the kinase-fusion-enriched subset), reflecting a bimodal distribution with a distinct fusion-positive subgroup driven by RET, NTRK, and [BRAF](../genes/BRAF.md) rearrangements [PMID:29617662](../papers/29617662.md).
- THCA samples in pan-cancer integrative analysis; C12:THCA was one of eight iClusters dominated by a single tumor type; >80% of THCA samples grouped together in the same iCluster [PMID:29625048](../papers/29625048.md)
- THCA included in pan-cancer somatic driver analysis across 33 cancer types [PMID:29625049](../papers/29625049.md)
- THCA included in pan-cancer pathway analysis; BRAF hotspots in 62% of THCA (RTK-RAS pathway); 84% of THCA carries RTK-RAS pathway alterations — among the highest rates pan-cancer [PMID:29625050](../papers/29625050.md)

## Sources

- cBioPortal study: `thca_tcga_pan_can_atlas_2018`
- [PMID:29617662](../papers/29617662.md)
- [PMID:29625048](../papers/29625048.md)
- [PMID:29625049](../papers/29625049.md)
- [PMID:29625050](../papers/29625050.md)

*This page was processed by **entity-page-writer** on **2026-05-16**.*
