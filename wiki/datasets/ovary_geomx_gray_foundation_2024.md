---
name: "Ovarian HGSOC Precursor Lesions — GeoMx Spatial Profiling (Gray Foundation 2024)"
slug: ovary_geomx_gray_foundation_2024
institution: Multi-institutional (University of Pennsylvania, Swedish Cancer Institute, Seattle)
size: 44
reference_genome: hg38
canonical_source: cbioportal
unverified: false
assays: [immunofluorescence, spatial-transcriptomics]
panels: []
tags:
  - hgsoc
  - ovarian-cancer
  - fallopian-tube
  - stic
  - spatial-proteomics
  - geomx
  - cycif
  - tumor-microenvironment
processed_by: crosslinker
processed_at: 2026-04-11
---

# Ovarian HGSOC Precursor Lesions — GeoMx Spatial Profiling (Gray Foundation 2024)

## Overview

Multi-center spatial profiling dataset of 44 FFPE fallopian tube specimens from 43 individuals, spanning precursor lesions (p53 signatures, STICs) to co-occurring invasive high-grade serous ovarian carcinoma ([HGSOC](../cancer_types/HGSOC.md)). Profiled by NanoString GeoMx whole transcriptome analysis (WTA) and 31-antibody cyclic immunofluorescence (CyCIF). Data integrated into cBioPortal as `ovary_geomx_gray_foundation_2024`. [PMID:39386723](../papers/39386723.md)

## Composition

- 44 FFPE fallopian tube specimens from 43 individuals from University of Pennsylvania, Swedish Cancer Institute (Seattle), and collaborating sites. [PMID:39386723](../papers/39386723.md)
- Group 1 (n=24): invasive cancer with co-occurring STIC (STIC.C); 15/24 [BRCA](../cancer_types/BRCA.md) WT, 7/9 germline [BRCA1](../genes/BRCA1.md), 6/7 germline [BRCA2](../genes/BRCA2.md). [PMID:39386723](../papers/39386723.md)
- Group 2 (n=19): no invasive cancer; incidental p53 signatures (p53.I, n=10) and incidental STICs (STIC.I, n=9) from risk-reducing surgery. [PMID:39386723](../papers/39386723.md)

## Assays / panels (linked)

- NanoString GeoMx whole transcriptome analysis (WTA) across >600 regions of interest in 35/44 specimens. [PMID:39386723](../papers/39386723.md)
- CyCIF (31-antibody panel) in all 44 specimens; 4.22×10^7 single cells classified into 21 cell neighborhood topics via latent Dirichlet allocation. [PMID:39386723](../papers/39386723.md)

## Papers using this cohort

- [PMID:39386723](../papers/39386723.md) — Multimodal Spatial Profiling Reveals Immune Suppression and Microenvironment Remodeling in Fallopian Tube Precursors to High-Grade Serous Ovarian Carcinoma.

## Notable findings derived from this cohort

- IFN-alpha and IFN-gamma pathway genes ([STAT1](../genes/STAT1.md), [IFITM1](../genes/IFITM1.md), [IRF9](../genes/IRF9.md), [IRF7](../genes/IRF7.md), [ISG15](../genes/ISG15.md), TAP1, [HLA-A](../genes/HLA-A.md)) significantly upregulated beginning at the p53 signature stage and persisting through STIC and invasive cancer. [PMID:39386723](../papers/39386723.md)
- [HLA-E](../genes/HLA-E.md) progressively upregulated (p53.I median 4% to STIC.C 26% positive epithelial cells) as an immune evasion mechanism potentially inhibiting NK cell cytotoxicity via NKG2A engagement. [PMID:39386723](../papers/39386723.md)
- cGAS-STING pathway activation via micronuclear rupture (BANF1-positive ruptured micronuclei with cGAS co-localization) observed as early as STIC.I lesions. [PMID:39386723](../papers/39386723.md)

## Sources

- cBioPortal study `ovary_geomx_gray_foundation_2024` [PMID:39386723](../papers/39386723.md).

*This page was processed by **crosslinker** on **2026-04-11**.*
