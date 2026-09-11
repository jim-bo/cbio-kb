---
name: CCRCC 12-Gene Panel
slug: ccrcc-12-gene-classifier
kind: method
canonical_source: corpus
unverified: true
tags: [targeted-sequencing, ccrcc, gene-panel]
processed_by: crosslinker
processed_at: 2026-09-11
---

# CCRCC 12-Gene Panel

## Overview

A custom 12-gene, clear-cell renal cell carcinoma (ccRCC)-focused targeted sequencing panel ([ATM](../genes/ATM.md), [ATP9B](../genes/ATP9B.md), [BAP1](../genes/BAP1.md), [COL11A1](../genes/COL11A1.md), [DMD](../genes/DMD.md), [KDM5C](../genes/KDM5C.md), [PBRM1](../genes/PBRM1.md), [PTK7](../genes/PTK7.md), [SETD2](../genes/SETD2.md), [TP53](../genes/TP53.md), [TRRAP](../genes/TRRAP.md), [VHL](../genes/VHL.md)) used to validate somatic mutation calls from larger discovery cohorts (WGS/WES/42-gene panel) in ccRCC.

## Used by

- The 12-gene ccRCC-focused panel (Lucigen AmpFree library prep, IDT xGen dual-index UMI adapters, NovaSeq 6000 2x150bp, mean coverage 1475X) sequenced the C3 validation cohort (n=474) of a 943-patient clear-cell [RCC](../cancer_types/RCC.md) adjuvant-therapy stratification study, replicating per-gene mutation rates found in the C1+C2 discovery cohort (WGS + WES/42-gene panel, n=469). [PMID:36815791](../papers/36815791.md)

## Notes

- Restricted to the 12 genes ATM, ATP9B, BAP1, COL11A1, DMD, KDM5C, PBRM1, PTK7, SETD2, TP53, TRRAP and VHL, recurrently mutated in ccRCC; the paper's main mutation-rate analysis used only these 12 genes regardless of which of the three sequencing platforms (WGS, WES, or the 42-gene/12-gene panels) generated the call.
- No significant differences in per-gene mutation rates, stage, grade or age were found between the discovery (C1+C2) and validation (C3) cohorts.

## Sources

- [PMID:36815791](../papers/36815791.md) — Vasudev et al. 2023, *Clin Cancer Res*, genomic sequencing to refine patient stratification for adjuvant therapy in RCC

*This page was processed by **crosslinker** on **2026-09-11**.*
