---
name: Kidney Renal Clear Cell Carcinoma (TCGA)
oncotree_code: KIRC
main_type: Renal Cell Carcinoma
parent: RCC
tags:
  - kidney
  - renal
  - clear-cell
  - tcga-cohort
unverified: true
canonical_source: corpus
processed_by: crosslinker
processed_at: 2026-05-15
---

# Kidney Renal Clear Cell Carcinoma / KIRC (TCGA)

## Overview

KIRC is the TCGA cohort identifier for kidney renal clear cell carcinoma. The closest OncoTree equivalent is [CCRCC](CCRCC.md) (Renal Clear Cell Carcinoma). This page covers findings specifically attributed to the TCGA KIRC cohort in the corpus. KIRC has been used as a benchmark cancer type for somatic variant calling quality assessment in pan-cancer projects.

## Cohorts in the corpus

- TCGA KIRC cohort: included as one of 33 cancer types in the MC3 pan-cancer mutation-calling project and the TCGA fusion landscape study; subset of the PanCancer Atlas ([kirc_tcga_pan_can_atlas_2018](../datasets/kirc_tcga_pan_can_atlas_2018.md)).

## Recurrent alterations

- MC3 pan-cancer mutation-calling project used KIRC as a benchmark: running MutSig2CV and MuSiC2 on PASS variants yielded 10 SMGs each ([TP53](../genes/TP53.md), [PTEN](../genes/PTEN.md), [VHL](../genes/VHL.md), [SETD2](../genes/SETD2.md), [PBRM1](../genes/PBRM1.md), [BAP1](../genes/BAP1.md), [MTOR](../genes/MTOR.md), [PIK3CA](../genes/PIK3CA.md), [ATM](../genes/ATM.md), [ELOC](../genes/ELOC.md)); the unfiltered controlled MAF inflated these to 1,203 and 321 respectively, demonstrating the critical importance of filtering [PMID:29596782](../papers/29596782.md).
- Pan-cancer fusion study (9,624 TCGA samples) found KIRC has a median of 0 fusions per sample [PMID:29617662](../papers/29617662.md).

## Subtypes

- Clear cell [RCC](../cancer_types/RCC.md) is the most common RCC subtype; KIRC (TCGA) corresponds approximately to OncoTree [CCRCC](../cancer_types/CCRCC.md).

## Therapeutic landscape

*No drug-specific findings for KIRC reported in the current corpus beyond the general significance of VHL and mTOR pathway mutations.*

## Sources

- [PMID:29596782](../papers/29596782.md) — MC3 multi-center mutation calling (Ellrott et al., 2018)
- [PMID:29617662](../papers/29617662.md) — Pan-cancer fusion landscape (Gao et al., 2018)

*This page was processed by **crosslinker** on **2026-05-15**.*
