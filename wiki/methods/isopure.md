---
name: ISOpure
slug: isopure
kind: method
canonical_source: corpus
unverified: true
tags: [tumor-purity, deconvolution, classification, breast-cancer]
processed_by: crosslinker
processed_at: 2026-05-14
---

# ISOpure

## Overview

ISOpure is a computational deconvolution method that estimates tumor purity (the fraction of cancer-cell-derived RNA) from bulk gene expression profiles by modeling the observed tumor RNA as a mixture of a cancer RNA signature and normal tissue RNA. Beyond purity estimation, it can be used as a classifier by projecting tumor samples onto a learned cancer-versus-normal axis, enabling separation of histologically ambiguous tumors into distinct molecular classes.

## Used by

- Applied as one of three orthogonal classifiers (alongside CLANC and ElasticNet) to assign 88 mixed IDC/ILC breast tumors to ILC-like or IDC-like molecular classes in the TCGA breast cancer multi-platform study (n=817); all three methods agreed that 24/88 mixed cases were ILC-like and 64 were IDC-like, with [CDH1](../genes/CDH1.md) mutation status as the dominant feature. [PMID:26451490](../papers/26451490.md)

## Notes

- Original ISOpure method published by Quon et al. (Genome Biology, 2013).
- Requires reference normal tissue expression profiles as input alongside the tumor sample profiles.
- In the TCGA breast ILC/IDC study, ISOpure was adapted for molecular subtype classification rather than pure purity quantification.

## Sources

- [PMID:26451490](../papers/26451490.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
