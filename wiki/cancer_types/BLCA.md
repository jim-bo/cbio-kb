---
name: Bladder Urothelial Carcinoma
oncotree_code: BLCA
parent: BLADDER
tags:
  - urothelial
  - fgfr3
processed_by: crosslinker
processed_at: 2026-04-11
---

# Bladder Urothelial Carcinoma (BLCA)

## Overview

Urothelial carcinoma arising in the bladder; OncoTree code `BLCA` under the bladder/urinary tract lineage. Spans non-muscle-invasive (NMIBC), muscle-invasive (MIBC), and metastatic disease states with distinct genomic landscapes ([PMID:37682528](../papers/37682528.md)).

## Cohorts in the corpus

- [bladder_msk_2023](../datasets/bladder_msk_2023.md) — 1,421 patients / 1,507 urothelial carcinoma tumors sequenced at MSK, including 504 NMIBC and 526 MIBC bladder specimens alongside upper-tract and metastatic cases ([PMID:37682528](../papers/37682528.md)).

## Recurrent alterations

- [FGFR3](../genes/FGFR3.md) — oncogenic alterations in 39% (199/504) of NMIBC and 14% (75/526) of MIBC bladder tumors; S249C is the dominant hotspot, and R248C is less frequent in bladder (11%, 37/333) than upper-tract disease ([PMID:37682528](../papers/37682528.md)).
- [ERBB2](../genes/ERBB2.md) — co-altered in 11% of FGFR3-altered MIBC (vs 2.5% in NMIBC) ([PMID:37682528](../papers/37682528.md)).
- [TP53](../genes/TP53.md), [RB1](../genes/RB1.md) — inversely associated with [FGFR3](../genes/FGFR3.md) alterations in urothelial carcinoma ([PMID:37682528](../papers/37682528.md)).
- [PIK3CA](../genes/PIK3CA.md), [TSC1](../genes/TSC1.md), [AKT1](../genes/AKT1.md) — PI3K pathway co-alterations in 37% of FGFR2/3-altered tumors ([PMID:37682528](../papers/37682528.md)).
- [CDKN2A](../genes/CDKN2A.md), [CDKN2B](../genes/CDKN2B.md), [KDM6A](../genes/KDM6A.md) — frequently co-altered with [FGFR3](../genes/FGFR3.md) ([PMID:37682528](../papers/37682528.md)).

## Subtypes

- NMIBC vs MIBC disease states show markedly different [FGFR3](../genes/FGFR3.md) alteration frequencies (39% vs 14%), supporting distinct molecular biology ([PMID:37682528](../papers/37682528.md)).
- FGFR3-fusion tumors carry lower TMB than FGFR3-mutant tumors (median 5 vs 9 mut/Mb, p=0.0006) ([PMID:37682528](../papers/37682528.md)).

## Therapeutic landscape

- [erdafitinib](../drugs/erdafitinib.md) — real-world ORR 40%, median PFS 2.8 months, [OS](../cancer_types/OS.md) 6.6 months in 32 metastatic FGFR3-altered urothelial carcinoma patients; tolerability-limited with 38% dose reductions ([PMID:37682528](../papers/37682528.md)).
- Immune checkpoint blockade outcomes did not differ by [FGFR3](../genes/FGFR3.md) status (n=26 altered vs 155 wildtype) ([PMID:37682528](../papers/37682528.md)).
- [BRAF](../genes/BRAF.md) fusions were identified as acquired resistance mechanisms to [EGFR](../genes/EGFR.md) TKIs in BLCA patients [PMID:38922339](../papers/38922339.md).
- ctDNA detection (MSK-ACCESS) was associated with higher VTE risk in BLCA patients, though the association was not significant for BLCA specifically [PMID:39147831](../papers/39147831.md).
- [enfortumab-vedotin](../drugs/enfortumab-vedotin.md) and next-generation FGFR3-selective inhibitors (e.g., TYRA300, LOXO435) cited as alternative options given [erdafitinib](../drugs/erdafitinib.md)'s modest durability ([PMID:37682528](../papers/37682528.md)).

## Sources

- [PMID:37682528](../papers/37682528.md) — Guercio et al., Clinical Cancer Research 2023.
- [PMID:38922339](../papers/38922339.md)
- [PMID:39147831](../papers/39147831.md)

*This page was processed by **crosslinker** on **2026-04-11**.*
