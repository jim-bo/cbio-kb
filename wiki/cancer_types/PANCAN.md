---
name: Pan-Cancer (TCGA PanCancer Atlas)
oncotree_code: PANCAN
main_type: Pan-Cancer
parent:
tags:
  - pan-cancer
  - tcga
  - multi-cancer
  - corpus-identifier
unverified: true
canonical_source: corpus
processed_by: crosslinker
processed_at: 2026-05-15
---

# Pan-Cancer / PANCAN (TCGA PanCancer Atlas)

## Overview

PANCAN is not an OncoTree cancer-type code but is used in this wiki as a corpus identifier for studies that span all 33 TCGA cancer types in the PanCancer Atlas. It indicates findings that are genuinely pan-cancer in scope rather than specific to any single tumor type. The TCGA PanCancer Atlas comprises ~10,000–11,000 tumor samples analyzed uniformly across molecular platforms.

## Cohorts in the corpus

- TCGA PanCancer Atlas: 33 cancer types analyzed jointly across somatic mutation (MC3), RNA-seq, copy number (SNP6/ABSOLUTE), and methylation platforms.
- Reference datasets: [gbm_tcga_pan_can_atlas_2018](../datasets/gbm_tcga_pan_can_atlas_2018.md), [coadread_tcga_pan_can_atlas_2018](../datasets/coadread_tcga_pan_can_atlas_2018.md), [cesc_tcga_pan_can_atlas_2018](../datasets/cesc_tcga_pan_can_atlas_2018.md), and equivalent study slugs for all 33 disease types.

## Recurrent alterations

- Pan-cancer fusion study (9,624 TCGA samples, 33 cancer types) identified 25,664 fusions with 63.3% WGS validation rate; 6.0% of pan-cancer samples harbor at least one druggable fusion; fusions are the sole driver in ~1.8% of tumors; [TP53](../genes/TP53.md) is predominantly mutated rather than fused across cancer types [PMID:29617662](../papers/29617662.md).

## Subtypes

- Each of the 33 TCGA cancer types is a subtype of the PANCAN scope; see individual cancer-type pages for disease-specific findings.

## Therapeutic landscape

- 6.0% of pan-cancer samples (574/9,624) harbor at least one druggable fusion by DEPO annotation across 29 cancer types; major recurrent druggable targets include [TMPRSS2](../genes/TMPRSS2.md) in [PRAD](../cancer_types/PRAD.md), [RET](../genes/RET.md) in [THCA](../cancer_types/THCA.md), and [PML](../genes/PML.md)–[RARA](../genes/RARA.md) in [LAML](../cancer_types/LAML.md) [PMID:29617662](../papers/29617662.md).

## Sources

- [PMID:29617662](../papers/29617662.md) — Pan-cancer fusion landscape (Gao et al., 2018)

*This page was processed by **crosslinker** on **2026-05-15**.*
