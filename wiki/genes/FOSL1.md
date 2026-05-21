---
symbol: FOSL1
aliases:
  - FRA-1
cancer_types:
  - PRAD
  - PRSCC
tags:
  - ap-1
  - transcription-factor
  - pioneer-factor
  - crpc
  - lineage-plasticity
canonical_source: cbioportal
unverified: false
processed_by: crosslinker
processed_at: 2026-05-21
---

# FOSL1

## Overview

FOSL1 ([FOS](../genes/FOS.md) Like 1, AP-1 Transcription Factor Subunit; also known as FRA-1) encodes a leucine zipper protein and member of the AP-1 transcription factor family. It acts as a pioneer transcription factor capable of remodeling chromatin accessibility. In metastatic castration-resistant prostate cancer (CRPC), FOSL1 is the highest-ranked key transcription factor for the newly described CRPC-SCL (stem cell-like) subtype, cooperating with YAP1/WWTR1 (TAZ) and TEAD to drive lineage plasticity away from androgen receptor dependence.

## Alterations observed in the corpus

- Highest-ranked key TF for CRPC-SCL subtype in chromatin-based molecular subtyping of metastatic CRPC across 22 patient-derived organoids, 6 PDXs, and 12 cell lines; CRPC-SCL was the second-most-common subtype (~28%) in 366 CRPC patients across SU2C and WCM cohorts [PMID:35617398](../papers/35617398.md)
- Stable FOSL1 overexpression in AR-high LNCaP cells increased chromatin accessibility at CRPC-SCL-specific sites and decreased CRPC-AR-specific accessibility (permutation P < 0.001), with concordant upregulation of CRPC-SCL signature genes (FDR < 1e-5) — direct evidence of lineage transformation [PMID:35617398](../papers/35617398.md)
- sgRNA depletion of FOSL1 in MSKPCa3 and DU145 (CRPC-SCL) reduced cell growth but not in CRPC-AR organoid MSKPCa2 [PMID:35617398](../papers/35617398.md)

## Cancer types (linked)

- [PRAD](../cancer_types/PRAD.md) / [PRSCC](../cancer_types/PRSCC.md): FOSL1 as the top pioneer TF driving the CRPC-SCL chromatin state; CRPC-SCL patients have significantly shorter time on enzalutamide/abiraterone (ARSI) [PMID:35617398](../papers/35617398.md)

## Co-occurrence and mutual exclusivity

- Functional cooperation with [YAP1](../genes/YAP1.md) and [WWTR1](../genes/WWTR1.md) (TAZ): ChIP-seq in MSKPCa3 and DU145 showed significant overlap of FOSL1/TEAD/YAP/TAZ peaks (Fisher's exact P < 0.001) at CRPC-SCL ATAC-seq peaks [PMID:35617398](../papers/35617398.md)
- Part of broader AP-1 network with [FOS](../genes/FOS.md), [FOSB](../genes/FOSB.md), [FOSL2](../genes/FOSL2.md), [JUN](../genes/JUN.md), [JUNB](../genes/JUNB.md), [JUND](../genes/JUND.md) [PMID:35617398](../papers/35617398.md)

## Therapeutic relevance

- The c-Fos/AP-1 DNA-binding inhibitor T-5224 preferentially inhibited proliferation of CRPC-SCL models (MSKPCa3 and DU145) vs CRPC-AR models, nominating the YAP/TAZ/AP-1 axis as a therapeutic vulnerability [PMID:35617398](../papers/35617398.md)
- [verteporfin](../drugs/verteporfin.md) (YAP/TAZ inhibitor) also selectively reduced CRPC-SCL model growth [PMID:35617398](../papers/35617398.md)

## Open questions

- Verteporfin's clinical translation may be limited by YAP-independent effects [PMID:35617398](../papers/35617398.md)
- CRPC-SCL identification leans heavily on in vitro/PDX models — subtype projections onto bulk RNA-seq from patients may miss intratumoral heterogeneity [PMID:35617398](../papers/35617398.md)

## Sources

- [PMID:35617398](../papers/35617398.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
