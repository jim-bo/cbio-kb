---
name: spautin-1
targets:
  - USP10
  - USP13
drug_class: deubiquitinase inhibitor (USP10/USP13)
canonical_source: corpus
unverified: true
tags:
  - tool-compound
  - ubiquitin-proteasome
  - parp-inhibitor-sensitizer
  - prostate-cancer
processed_by: crosslinker
processed_at: 2026-05-14
---

# spautin-1

## Overview

Spautin-1 is a tool-compound inhibitor of the deubiquitinases [USP10](../genes/USP10.md) and USP13. In the context of DNA damage response (DDR) research, it was identified as an inhibitor of USP10, which stabilizes the tRNA methyltransferase [TRMT10A](../genes/TRMT10A.md)—a non-canonical regulator of homologous recombination (HR) that recruits [BRCA1](../genes/BRCA1.md) to DNA double-strand breaks via ATM-mediated Ser28 phosphorylation. By inhibiting USP10, spautin-1 promotes proteasomal degradation of TRMT10A, induces "BRCAness" in HR-proficient tumors, and sensitizes cells to PARP inhibitors such as [olaparib](olaparib.md). No clinical-grade USP10 inhibitor based on spautin-1 currently exists; its pharmacokinetics and on-target specificity in humans remain to be established.

## Evidence in the corpus

- In BRCA1/2-wild-type mCRPC cell lines (22Rv1, C4-2) and two patient-derived xenograft models (PDX#546, PDX#1092) with high USP10/TRMT10A expression, spautin-1 (20 mg/kg in vivo) combined with [olaparib](../drugs/olaparib.md) produced HSA synergy scores >10, CI=0.76 in 22Rv1 CDX, and 42.9% additional tumor-volume reduction vs olaparib alone in PDX#1092; the combination was well-tolerated in C57BL/6 mice with no additional hematologic toxicity beyond olaparib monotherapy [PMID:28068672](../papers/28068672.md).
- Spautin-1 dose-dependently reduced TRMT10A protein in 22Rv1 cells (rescued by the proteasome inhibitor MG-132, confirming proteasome-dependent degradation), decreased HR efficiency (DR-GFP reporter), and reduced BRCA1/RAD51 foci without affecting upstream DDR signaling (gamma-H2AX, 53BP1) [PMID:28068672](../papers/28068672.md).
- Synergy with olaparib was confirmed in BRCA2-WT-overexpressing 22Rv1 cells, demonstrating that the effect is independent of the line's monoallelic [BRCA2](../genes/BRCA2.md) T3033Nfs*11 background [PMID:28068672](../papers/28068672.md).

## Resistance mechanisms

- USP10 deep deletion (~10% of SU2C/PCF mCRPC cohorts) may create an intrinsically PARPi-sensitive state independently of spautin-1 treatment; conversely, high USP10/TRMT10A co-expression is hypothesized to confer intrinsic resistance to PARPi that spautin-1 can overcome [PMID:28068672](../papers/28068672.md).

## Cancer types (linked)

- [PRAD](../cancer_types/PRAD.md) — tested in mCRPC cell lines and PDX models; TRMT10A/USP10 axis validated as PARPi-sensitizing target.

## Sources

- [PMID:28068672](../papers/28068672.md) — Yang et al., TRMT10A/USP10 axis in mCRPC; spautin-1 as USP10 inhibitor synergizing with olaparib.

*This page was processed by **crosslinker** on **2026-05-14**.*
