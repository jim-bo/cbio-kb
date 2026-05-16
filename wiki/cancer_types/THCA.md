---
name: Thyroid Carcinoma (TCGA)
oncotree_code: THCA
main_type: Thyroid Cancer
parent: THYC
tags:
  - thyroid
  - kinase-fusion
  - ret
  - braf
  - tcga-cohort
  - low-aneuploidy
unverified: true
canonical_source: corpus
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Thyroid Carcinoma / THCA (TCGA)

## Overview

THCA is the TCGA cohort identifier for thyroid carcinoma (predominantly papillary thyroid carcinoma). The closest OncoTree codes are [THPA](THPA.md) (Papillary Thyroid Cancer) and [THYC](THYC.md) (Thyroid Cancer, parent node). THCA is characterized by extraordinarily low mutation burden and arm-level aneuploidy, with driver oncogenesis predominantly through kinase fusions ([RET](../genes/RET.md), NTRK1/3, [BRAF](../genes/BRAF.md) fusions) or point mutations (BRAF V600E, RAS).

## Cohorts in the corpus

- TCGA THCA cohort: included as one of 33 cancer types in the pan-cancer fusion landscape study; subset of the PanCancer Atlas ([thca_tcga_pan_can_atlas_2018](../datasets/thca_tcga_pan_can_atlas_2018.md)).

## Recurrent alterations

- Pan-cancer fusion study (9,624 TCGA samples) found THCA is dramatically enriched for kinase fusions (35.6% of THCA samples; Fisher p < 2.2e-16); 94.0% are 3′-kinase fusions; top recurrent partners are tyrosine kinases RET, BRAF, [NTRK1](../genes/NTRK1.md), [NTRK3](../genes/NTRK3.md), and [ALK](../genes/ALK.md); [CCDC6](../genes/CCDC6.md)–RET was detected in 4.2% of THCA (33 samples flagged druggable); THCA has a median of 0 fusions/sample overall but the kinase-fusion subset is striking [PMID:29617662](../papers/29617662.md).
- Pan-cancer aneuploidy study found thyroid carcinoma has the lowest aneuploidy score of all 33 TCGA cancer types (26% of THCA samples with any arm event, mean score 0.87), consistent with its known low CNA burden and near-diploid genomes [PMID:29622463](../papers/29622463.md).
- Included in TCGA PanCancer Atlas; THCA dominated iCluster C12; >80% of THCA samples grouped in single iCluster demonstrating high molecular homogeneity [PMID:29625048](../papers/29625048.md)
- Included in TCGA PanCancer Atlas integrative driver/immune analysis (11,000 tumors, 33 cancer types) [PMID:29625049](../papers/29625049.md)
- BRAF hotspot mutations in 62% of THCA; RTK-RAS alteration rate 84% in THCA; included in pan-cancer pathway analysis of 9,125 TCGA tumors [PMID:29625050](../papers/29625050.md)
- Included in TCGA Pan-Cancer Clinical Data Resource (11,160 patients, 33 cancer types); standardized OS, PFI, DFI, and DSS endpoints derived for THCA [PMID:29625055](../papers/29625055.md)

## Subtypes

- **Papillary thyroid carcinoma (PTC):** most common; driven by BRAF V600E (~60%), RET fusions (~10–20%), NTRK fusions.
- **Follicular thyroid carcinoma (FTC):** driven by RAS mutations, [PAX8](../genes/PAX8.md)–[PPARG](../genes/PPARG.md) fusions.
- **Anaplastic thyroid carcinoma (ATC):** highest mutation burden among thyroid tumors.

## Therapeutic landscape

- RET fusions (CCDC6–RET and others) in THCA are actionable with selective RET inhibitors ([selpercatinib](../drugs/selpercatinib.md), pralsetinib) and were annotated as druggable in 33 THCA samples in the pan-cancer fusion analysis [PMID:29617662](../papers/29617662.md).
- NTRK1/NTRK3 fusions are actionable with [larotrectinib](../drugs/larotrectinib.md) or [entrectinib](../drugs/entrectinib.md) (tumor-agnostic FDA approval).
- ALK fusions are a minor subgroup potentially actionable with ALK inhibitors.

## Sources

- [PMID:29617662](../papers/29617662.md) — Pan-cancer fusion landscape (Gao et al., 2018)
- [PMID:29622463](../papers/29622463.md) — Pan-cancer aneuploidy landscape (Taylor et al., 2018)

*This page was processed by **crosslinker** on **2026-05-15**.*
- [PMID:29625048](../papers/29625048.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29625050](../papers/29625050.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29625055](../papers/29625055.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
