---
name: JQ1
targets:
  - BRD4
  - BRD2
  - BRD3
drug_class: BET bromodomain inhibitor (tool compound)
canonical_source: corpus
unverified: true
tags:
  - BET-inhibitor
  - bromodomain
  - SCLC
  - synthetic-lethality
  - tool-compound
processed_by: entity-page-writer
processed_at: 2026-05-14
---

# JQ1

## Overview

JQ1 is a potent, selective BET (bromodomain and extra-terminal) bromodomain inhibitor developed as a tool compound. It targets [BRD4](../genes/BRD4.md) (and related BRD2/BRD3), displacing them from acetylated histone marks and suppressing transcription of oncogenes including [MYC](../genes/MYC.md). JQ1 has known pharmacokinetic limitations and is not clinically approved, but is widely used to establish preclinical proof-of-concept for BET inhibition.

## Evidence in the corpus

- JQ1 IC50 values positively correlate with [ARID1A](../genes/ARID1A.md) expression levels in [SCLC](../cancer_types/SCLC.md) cell lines (r = 0.368, P = 0.032, GDSC1 dataset), indicating enhanced JQ1 sensitivity upon [ARID1A](../genes/ARID1A.md) loss [PMID:22037554](../papers/22037554.md).
- JQ1 dose-dependently reduces [RAD51](../genes/RAD51.md) expression and suppresses p-CHK1 levels in [SCLC](../cancer_types/SCLC.md) cells [PMID:22037554](../papers/22037554.md).
- Combination of JQ1 and [brd-k98645985](../drugs/brd-k98645985.md) (targeting the ARID1A-containing BAF complex) achieves superior tumor suppression vs. either agent alone in xenograft models (p < 0.0001) [PMID:22037554](../papers/22037554.md).
- Bliss synergy between JQ1 and BRD-K98645985 demonstrated in vitro in [SCLC](../cancer_types/SCLC.md) cell lines [PMID:22037554](../papers/22037554.md).
- [MYC](../genes/MYC.md) amplification (~14% of pancreatic ductal adenocarcinoma cases, associated with poor overall survival and adenosquamous histology) nominates BET-bromodomain inhibitor JQ1 as a therapeutic candidate [PMID:25855536](../papers/25855536.md)
- JQ1 (50 mg/kg daily orally) significantly slowed tumor growth in 2 grade-2 adenoid cystic carcinoma (ACC) primagrafts (X5M1, X9), with modest decreases in [MYB](../genes/MYB.md) and MYB-target gene expression; both grade-3 Notch-activated primagrafts failed to respond, implicating [BRD4](../genes/BRD4.md) occupancy at [MYB](../genes/MYB.md) super-enhancers as a grade-2-specific dependency [PMID:26829750](../papers/26829750.md)

## Resistance mechanisms

- ARID1A-high [SCLC](../cancer_types/SCLC.md) tumors show reduced sensitivity to JQ1, as high [ARID1A](../genes/ARID1A.md) expression positively correlates with IC50 [PMID:22037554](../papers/22037554.md).
- Grade-3 ACC primagrafts with activating [NOTCH1](../genes/NOTCH1.md) mutations or [SPEN](../genes/SPEN.md) loss-of-function are insensitive to JQ1 in vivo, indicating that Notch pathway activation confers intrinsic BET-inhibitor resistance in ACC [PMID:26829750](../papers/26829750.md)

## Cancer types (linked)

- [SCLC](../cancer_types/SCLC.md)
- ACC (adenoid cystic carcinoma) — grade-2 tumors sensitive; grade-3 Notch-activated tumors resistant [PMID:26829750](../papers/26829750.md)

## Sources

- [PMID:22037554](../papers/22037554.md)
- [PMID:25855536](../papers/25855536.md)
- [PMID:26829750](../papers/26829750.md)

*This page was processed by **entity-page-writer** on **2026-05-14**.*
