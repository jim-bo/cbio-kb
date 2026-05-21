---
name: LINX (structural variant annotation tool)
slug: linx
kind: method
canonical_source: corpus
unverified: true
tags: [structural-variant, wgs, bioinformatics, annotation]
processed_by: crosslinker
processed_at: 2026-05-21
---

# LINX (structural variant annotation tool)

## Overview

LINX is an open-source structural variant (SV) annotation and interpretation tool developed by the Hartwig Medical Foundation. It takes SVs called by GRIDSS and copy-number profiles from PURPLE as input, then clusters and chains SVs into complex events, identifies driver gene disruptions (deletions, amplifications, fusions), and annotates chromoplexy, chromothripsis, and other complex rearrangement signatures. LINX is the third component of the Hartwig WGS analysis pipeline (GRIDSS → PURPLE → LINX).

## Used by

- Used for structural variant annotation in WGS of 25 metastatic [CSCC](../cancer_types/CSCC.md) lymph node specimens; together with PURPLE, produced a catalogued SV gene list including [SMAD4](../genes/SMAD4.md) (DEL), [CDKN2A](../genes/CDKN2A.md) (DEL), [MYC](../genes/MYC.md) (GAIN), [PTPRD](../genes/PTPRD.md) (DEL/LOH), [CALR](../genes/CALR.md) (GAIN), [EGFR](../genes/EGFR.md) (GAIN), [APC](../genes/APC.md) (DEL), [CREBBP](../genes/CREBBP.md) (DEL), [RAF1](../genes/RAF1.md), [CCND1](../genes/CCND1.md), [FGF3](../genes/FGF3.md), [MCL1](../genes/MCL1.md), [KDM6A](../genes/KDM6A.md) (DEL), and others [PMID:35982973](../papers/35982973.md)

## Notes

- Works downstream of GRIDSS (SV calling) and PURPLE (purity/ploidy estimation).
- Identifies gene fusions, exon-skipping events, and complex rearrangement signatures.
- Developed by Hartwig Medical Foundation; used in their national WGS program in the Netherlands.

## Sources

- [PMID:35982973](../papers/35982973.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
