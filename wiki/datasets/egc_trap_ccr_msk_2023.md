---
name: "HER2-Positive Esophagogastric Cancer — TRAP Trial (MSK, Cancer Cell Reports 2023)"
slug: egc_trap_ccr_msk_2023
institution: Memorial Sloan Kettering Cancer Center
size: 263
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [ctdna, scrna-seq, targeted-panel, whole-exome-seq]
panels: []
tags:
  - esophagogastric-cancer
  - erbb2
  - her2
  - immunotherapy
  - ctdna
  - phase-ii-trial
processed_by: crosslinker
processed_at: 2026-04-11
---

# HER2-Positive Esophagogastric Cancer — TRAP Trial (MSK, Cancer Cell Reports 2023)

## Overview

Integrated dataset from a Phase II clinical trial (NCT02954536) and a retrospective cohort of HER2-positive metastatic esophagogastric cancer ([EGC](../cancer_types/EGC.md)) patients at MSK, supporting analyses of HER2 IHC uniformity, ctDNA dynamics, and immunotherapy response. Data deposited in cBioPortal as `egc_trap_ccr_msk_2023`. [PMID:37406106](../papers/37406106.md)

## Composition

- **Phase II trial cohort**: 37 patients with HER2-positive (IHC 3+ or IHC 2+/FISH+) metastatic esophagogastric, gastroesophageal junction, or gastric adenocarcinoma treated with [pembrolizumab](../drugs/pembrolizumab.md), [trastuzumab](../drugs/trastuzumab.md), [capecitabine](../drugs/capecitabine.md), and [oxaliplatin](../drugs/oxaliplatin.md). [PMID:37406106](../papers/37406106.md)
- **MSK retrospective cohort**: 226 patients with HER2-positive EGC who received platinum-based chemotherapy with HER2-directed therapy from 2010 to 2022. [PMID:37406106](../papers/37406106.md)
- **scRNA-seq cohort**: Paired pre- and on-treatment biopsies from 7 patients (3 with CAPOX + trastuzumab, 4 without). [PMID:37406106](../papers/37406106.md)
- Cancer types: esophageal ([ESCA](../cancer_types/ESCA.md)), gastroesophageal junction ([GEJ](../cancer_types/GEJ.md)), and gastric ([STAD](../cancer_types/STAD.md)) adenocarcinoma. [PMID:37406106](../papers/37406106.md)

## Assays / panels (linked)

- Targeted NGS and whole-exome sequencing. [PMID:37406106](../papers/37406106.md)
- Single-cell RNA sequencing (scRNA-seq). [PMID:37406106](../papers/37406106.md)
- 89Zr-trastuzumab PET/CT. [PMID:37406106](../papers/37406106.md)
- Plasma ctDNA (Guardant Health). [PMID:37406106](../papers/37406106.md)

## Papers using this cohort

- [PMID:37406106](../papers/37406106.md) — Determinants of Survival with Combined HER2 and PD-1 Blockade in Metastatic Esophagogastric Cancer.

## Notable findings derived from this cohort

- Median PFS 13 months, median [OS](../cancer_types/OS.md) 27 months, ORR 89% in the Phase II trial (n=37). [PMID:37406106](../papers/37406106.md)
- Uniform HER2 IHC 3+ predicted longer median PFS (15 vs. 8.5 months, P=0.004). [PMID:37406106](../papers/37406106.md)
- ctDNA clearance by 9 weeks associated with longer PFS (HR 0.18, P=0.001). [PMID:37406106](../papers/37406106.md)
- Resistance mechanisms upon progression included [PIK3CA](../genes/PIK3CA.md), [KRAS](../genes/KRAS.md), [MET](../genes/MET.md), and [EGFR](../genes/EGFR.md) alterations; loss of HER2 expression in 48%. [PMID:37406106](../papers/37406106.md)
- Multivariable model: [ERBB2](../genes/ERBB2.md) amplification was a positive prognostic factor; [MYC](../genes/MYC.md) and [CDKN2A](../genes/CDKN2A.md)/B alterations were negative prognostic factors. [PMID:37406106](../papers/37406106.md)

## Sources

- cBioPortal study `egc_trap_ccr_msk_2023` [PMID:37406106](../papers/37406106.md).

*This page was processed by **crosslinker** on **2026-04-11**.*
