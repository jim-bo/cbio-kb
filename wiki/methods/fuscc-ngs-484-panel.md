---
name: FUSCC 484-Gene NGS Panel
slug: fuscc-ngs-484-panel
kind: gene-panel
canonical_source: corpus
unverified: true
tags: [targeted-sequencing, breast-cancer, tnbc, germline, somatic]
processed_by: crosslinker
processed_at: 2026-05-16
---

# FUSCC 484-Gene NGS Panel

## Overview

The FUSCC 484-gene targeted next-generation sequencing panel is a hybrid-capture NGS assay developed at Fudan University Shanghai Cancer Center (FUSCC). It covers 484 cancer-related genes and supports both somatic and germline variant calling from tumor biopsies. The panel was deployed in the FUTURE umbrella trial (NCT03805399) to comprehensively profile refractory metastatic triple-negative breast cancer (TNBC) at the time of recurrence or metastasis, enabling biomarker-matched treatment assignment across seven arms including PARP inhibitor, anti-PD-1, anti-VEGFR, and anti-AR/CDK4/6 strategies.

## Used by

- Tumor biopsies from 69 refractory metastatic TNBC patients enrolled in the FUTURE phase Ib/II umbrella trial at FUSCC profiled using this panel for somatic and germline calling; top mutated genes: [TP53](../genes/TP53.md) (72%), [PIK3CA](../genes/PIK3CA.md) (18%), [PTEN](../genes/PTEN.md) (10%), [KMT2D](../genes/KMT2D.md) (9%), [TSC2](../genes/TSC2.md) (9%); panel results stratified BRCA1/2 germline status for PARP-inhibitor arm assignment [PMID:32719455](../papers/32719455.md)

## Notes

- 484-gene coverage designed for both somatic and germline variant identification from tumor tissue.
- Used in combination with IHC ([AR](../genes/AR.md), CD8, [FOXC1](../genes/FOXC1.md)) for TNBC molecular subtyping into LAR, IM, BLIS, and MES subtypes in the FUTURE trial.
- Not registered in cBioPortal gene_panels ontology as of 2026-05-16; slug is corpus-derived.
- Institutionally developed at FUSCC (Fudan University Shanghai Cancer Center); no public genePanelId.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
