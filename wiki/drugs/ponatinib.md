---
name: ponatinib
targets:
  - BCR
  - ABL1
  - FGFR1
  - FLT3
  - PDGFRA
  - KIT
  - PTPN11
drug_class: multi-targeted tyrosine kinase inhibitor
canonical_source: corpus
unverified: true
tags:
  - kinase-inhibitor
  - aml
  - cml
  - rtk-inhibitor
processed_by: crosslinker
processed_at: 2026-05-16
---

# ponatinib

## Overview

Ponatinib is an oral multi-targeted tyrosine kinase inhibitor (TKI) with potent activity against [BCR](../genes/BCR.md)–[ABL1](../genes/ABL1.md) (including the T315I gatekeeper mutation), [FGFR1](../genes/FGFR1.md), [FLT3](../genes/FLT3.md), [PDGFRA](../genes/PDGFRA.md), [KIT](../genes/KIT.md), and the downstream phosphatase SHP2 ([PTPN11](../genes/PTPN11.md)). It is FDA-approved for chronic myeloid leukemia ([CML](../cancer_types/CML.md)) and Philadelphia chromosome-positive acute lymphoblastic leukemia (Ph+ ALL). Its activity against a broad spectrum of receptor tyrosine kinases positions it as an investigational agent in [AML](../cancer_types/AML.md) and other RTK-driven malignancies.

## Evidence in the corpus

- In the CCLE next-generation resource ([ccle_broad_2019](../datasets/ccle_broad_2019.md)), RPPA-based dependency modelling identified pSHP2 (Y542) as the top predictor of ponatinib sensitivity, outperforming [PTPN11](../genes/PTPN11.md) mRNA; adding RPPA data produced the largest improvement in sensitivity prediction for ponatinib among all TKIs tested. In a validation set of AML lines plus CML BCR–ABL controls, 4/5 previously untested AML lines with high pSHP2 were ponatinib-sensitive (CTV1, NKM1, EOL1, MonoMAC1; HEL9217 was the lone exception); 7/9 ponatinib-sensitive AML lines harbored alterations in FLT3, PDGFRA, FGFR1, or KIT. In vivo, AML primagrafts with high pSHP2 (BCR–ABL and FLT3-ITD bearing) showed extended survival on ponatinib relative to a low-pSHP2 primagraft. pSHP2 abundance is proposed as a unified screening biomarker for RTK-driven tumors likely to respond to ponatinib, with relevance to AML, CML, thyroid, and rhabdoid sarcoma lineages. [PMID:31068700](../papers/31068700.md)

## Resistance mechanisms

*(No resistance mechanism data in the current corpus.)*

## Cancer types (linked)

- Acute myeloid leukemia ([AML](../cancer_types/AML.md))
- Chronic myelogenous leukemia ([CML](../cancer_types/CML.md))

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
