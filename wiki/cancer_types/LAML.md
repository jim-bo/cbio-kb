---
name: Acute Myeloid Leukemia (TCGA)
oncotree_code: LAML
main_type: Leukemia
parent: MNM
tags:
  - leukemia
  - aml
  - tcga-cohort
  - liquid-tumor
unverified: true
canonical_source: corpus
processed_by: crosslinker
processed_at: 2026-05-15
---

# Acute Myeloid Leukemia / LAML (TCGA)

## Overview

LAML is the TCGA cohort identifier for acute myeloid leukemia. It corresponds to OncoTree [AML](AML.md) (Acute Myeloid Leukemia). LAML is used specifically in the TCGA PanCancer Atlas context. The liquid-tumor nature of [AML](../cancer_types/AML.md) creates unique challenges for matched-normal somatic variant calling, as skin biopsies used as "normals" are often contaminated with circulating tumor cells.

## Cohorts in the corpus

- TCGA LAML cohort: included as one of 33 cancer types in the MC3 pan-cancer mutation-calling project and the TCGA fusion landscape study; subset of the PanCancer Atlas ([laml_tcga_pan_can_atlas_2018](../datasets/laml_tcga_pan_can_atlas_2018.md)).

## Recurrent alterations

- MC3 pan-cancer mutation-calling project recovered only 44% of the LAML AWG calls because tumor-in-normal contamination (LAML skin "normals" enriched with tumor cells) causes conservative MC3 filtering to misclassify somatic calls as germline; the legacy LAML AWG MAF relied on Sanger-based manual recovery not in the exome data [PMID:29596782](../papers/29596782.md).
- Pan-cancer fusion study (9,624 TCGA samples) found 14.0% of LAML tumors had fusions but no driver-gene mutations; recovered fusions include [CBFB](../genes/CBFB.md)–[MYH11](../genes/MYH11.md) (n=3), [BCR](../genes/BCR.md)–[ABL1](../genes/ABL1.md) (n=2), [PML](../genes/PML.md)–[RARA](../genes/RARA.md) (n=2), and [NUP98](../genes/NUP98.md)–[NSD1](../genes/NSD1.md) (n=2); PML–RARA fusions annotated as druggable (16 samples); mutual exclusivity between CBFB fusions and CBFB point mutations observed [PMID:29617662](../papers/29617662.md).

## Subtypes

- LAML (TCGA) encompasses multiple AML cytogenetic/molecular subtypes including CBF-AML (CBFB–MYH11, [RUNX1](../genes/RUNX1.md)–[RUNX1T1](../genes/RUNX1T1.md)), APL (PML–RARA), and FLT3-ITD driven cases.

## Therapeutic landscape

- PML–RARA fusions are actionable with all-trans retinoic acid (ATRA) and arsenic trioxide; 16 LAML samples with PML–RARA fusions were annotated druggable in the pan-cancer fusion analysis [PMID:29617662](../papers/29617662.md).

## Sources

- [PMID:29596782](../papers/29596782.md) — MC3 multi-center mutation calling (Ellrott et al., 2018)
- [PMID:29617662](../papers/29617662.md) — Pan-cancer fusion landscape (Gao et al., 2018)

*This page was processed by **crosslinker** on **2026-05-15**.*
