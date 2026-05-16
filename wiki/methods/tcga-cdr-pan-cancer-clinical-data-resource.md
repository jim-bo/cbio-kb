---
name: TCGA Pan-Cancer Clinical Data Resource (TCGA-CDR)
slug: tcga-cdr-pan-cancer-clinical-data-resource
kind: method
canonical_source: corpus
unverified: true
tags: [clinical-data, survival-analysis, pan-cancer, tcga]
processed_by: crosslinker
processed_at: 2026-05-16
---

# TCGA Pan-Cancer Clinical Data Resource (TCGA-CDR)

## Overview

The TCGA Pan-Cancer Clinical Data Resource (TCGA-CDR) is a standardized, quality-assessed clinical annotation resource covering 11,160 TCGA patients across 33 cancer types. It derives four harmonized clinical outcome endpoints — overall survival ([OS](../cancer_types/OS.md)), progression-free interval (PFI), disease-free interval (DFI), and disease-specific survival (DSS) — using date of diagnosis as a uniform time-zero. The resource was built by processing 225 TCGA clinical data files from the GDC legacy archive and resolving over 1,000 QA issues. It provides per-cancer-type endpoint-usage recommendations (Table 3) and serves as the canonical survival annotation underlying all subsequent TCGA PanCanAtlas analyses and corresponding cBioPortal study annotations.

## Used by

- The TCGA-CDR processed 225 clinical data files for 11,160 patients across 33 cancer types; PFI is recommended for 27/33 cancer types without reservation; PFI and OS showed high logHR correlation (r = 0.96, 95% CI 0.77–0.99) [PMID:29625055](../papers/29625055.md).

## Notes

- Four endpoints: OS (overall survival), PFI (progression-free interval), DFI (disease-free interval), DSS (disease-specific survival).
- All four endpoints recommended without reservation in 13/33 cancer types: [BLCA](../cancer_types/BLCA.md), [CESC](../cancer_types/CESC.md), [COAD](../cancer_types/COAD.md), [ESCA](../cancer_types/ESCA.md), [HNSC](../cancer_types/HNSC.md), [KIRP](../cancer_types/KIRP.md), [LUAD](../cancer_types/LUAD.md), [LUSC](../cancer_types/LUSC.md), [OV](../cancer_types/OV.md), [PAAD](../cancer_types/PAAD.md), [SARC](../cancer_types/SARC.md), [STAD](../cancer_types/STAD.md), [UCEC](../cancer_types/UCEC.md).
- [PCPG](../cancer_types/PCPG.md): no endpoint recommended; [LAML](../cancer_types/LAML.md): no PFI available.
- Analysis performed in R 3.2.2 using Kaplan-Meier and Cox proportional hazards regression (Grambsch & Therneau 1994 PH-assumption test).
- Deliberately excludes treatment data; therapeutic-effect inference requires per-cancer-type analysis.
- HIPAA de-identification forces patient ages ≥90 to be reported as exactly 90 (46 patients affected).
- Available as a data descriptor publication (Liu et al. 2018, Cell); survival fields exposed in cBioPortal PanCancer Atlas 2018 studies.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
