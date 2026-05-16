---
name: Lung Adenocarcinoma (TCGA, PanCancer Atlas 2018)
studyId: luad_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 566
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - luad
  - lung
  - adenocarcinoma
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# Lung Adenocarcinoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Lung Adenocarcinoma PanCancer Atlas 2018 cohort is the [LUAD](../cancer_types/LUAD.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `luad_tcga_pan_can_atlas_2018`. It encompasses approximately 566 lung adenocarcinoma samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. LUAD is characterized by high mutation burden (tobacco-associated), a clinically important never-smoker subset with enrichment for druggable fusions, and arm-level aneuploidy patterns distinct from squamous lung carcinoma.

## Composition

- Cancer type: Lung Adenocarcinoma ([LUAD](../cancer_types/LUAD.md)), OncoTree code LUAD.
- Approximately 566 tumor samples.
- Data modalities: WES, RNA-seq, SNP array.
- Somatic mutations from MC3 ensemble pipeline; LUAD has one of the highest median SNVs per sample (tobacco-associated).
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
- [PMID:32015526](../papers/32015526.md) — Zhao et al. 2025, *bioRxiv*: Sherlock-Lung NS-LUAD transcriptomic subtyping; 74 TCGA-LUAD never-smoker cases contributed to the discovery cohort.

## Notable findings derived from this cohort

- [EML4](../genes/EML4.md)-[ALK](../genes/ALK.md) and other [ALK](../genes/ALK.md) fusions were identified in 5 LUAD samples (total 20 ALK fusions across 8 cancer types); [EML4](../genes/EML4.md) is the most frequent 5′ partner (7/17 of all ALK-fusion cases), with ALK overexpression copy-number neutral — supporting the rationale for [crizotinib](../drugs/crizotinib.md) and approved ALK inhibitors [PMID:29617662](../papers/29617662.md).
- Never-smoker LUAD cohort within this dataset is dramatically enriched for druggable fusions: 20% (15/75) of never-smokers vs. 2.1% (9/425) of smokers harbor a druggable fusion (chi-square p < 1e-6); data supports prioritizing fusion screening in non-smoking [NSCLC](../cancer_types/NSCLC.md) patients [PMID:29617662](../papers/29617662.md).
- [RET](../genes/RET.md) fusions (e.g., [CCDC6](../genes/CCDC6.md)-[RET](../genes/RET.md)) also seen in LUAD in addition to [THCA](../cancer_types/THCA.md) [PMID:29617662](../papers/29617662.md).
- Pan-cancer aneuploidy analysis placed LUAD in the epithelial cluster (alongside [BRCA](../cancer_types/BRCA.md) and [HCC](../cancer_types/HCC.md)) defined by 1q gain; fewer than 50% of LUAD tumors had 3p loss and only 13% had 3q gain — a pattern strikingly different from the squamous [LUSC](../cancer_types/LUSC.md) subtype where 3p loss is present in ~80% of tumors [PMID:29617662](../papers/29617662.md).
- LUAD has one of the highest median SNVs per sample in the MC3 pan-cancer analysis, consistent with tobacco-associated mutagenesis (C>A transversions), alongside [SKCM](../cancer_types/SKCM.md) and LUSC [PMID:29617662](../papers/29617662.md).
- LUAD samples in pan-cancer integrative analysis; C14:LUAD was one of eight single-tumor-type iClusters; smoking signature drives highest mutation rates in C14:LUAD; LUAD co-clusters with C10:pan-SCC for JAK2/STAT1/3/6 pathway activation [PMID:29625048](../papers/29625048.md)
- LUAD samples used in pan-cancer driver interaction analysis; TP53 and KRAS mutually exclusive in LUAD (but co-occur in PAAD); EGFR and KIT show elevated mRNA in missense mutants (FDR<0.1); RTK-RAS pathway altered in 74% of LUAD; SOS1 activating mutations present in ~1% of LUAD [PMID:29625049](../papers/29625049.md)
- LUAD included in pan-cancer pathway analysis; KRAS hotspots in 33% of LUAD; EGFR alterations in 13% of LUAD; NRF2-PI3K co-occurring alterations concentrated in LUAD/LUSC; SOS1 mutations present in ~1% of LUAD [PMID:29625050](../papers/29625050.md)
- Contributed 74 never-smoker LUAD cases to the 684-sample Sherlock-Lung NS-LUAD transcriptomic cohort; 13 cases also had matched WGS used for driver-mutation integration; transcriptomic subtypes (steady/proliferative/chaotic) were concordant across Sherlock and TCGA-derived never-smoker subsets [PMID:32015526](../papers/32015526.md)

## Sources

- cBioPortal study: `luad_tcga_pan_can_atlas_2018`
- [PMID:29617662](../papers/29617662.md)
- [PMID:29625048](../papers/29625048.md)
- [PMID:29625049](../papers/29625049.md)
- [PMID:29625050](../papers/29625050.md)
- [PMID:32015526](../papers/32015526.md)

*This page was processed by **entity-page-writer** on **2026-05-16**.*
