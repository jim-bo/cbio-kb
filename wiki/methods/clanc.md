---
name: CLANC
slug: clanc
kind: method
canonical_source: corpus
unverified: true
tags: [classification, centroid, breast-cancer, subtype]
processed_by: crosslinker
processed_at: 2026-05-14
---

# CLANC

## Overview

CLANC (Comparative Latent Neoantigen Classification, or alternatively a centroid-based nearest-centroid classifier framework) is a supervised classification approach used in multi-platform cancer genomics to assign tumor samples to predefined molecular classes. In the TCGA breast cancer ILC/IDC context, it was adapted as one of several orthogonal classifiers to determine whether mixed IDC/ILC tumors are molecularly ILC-like or IDC-like, using gene expression centroids trained on pure [ILC](../cancer_types/ILC.md) and [IDC](../cancer_types/IDC.md) cases.

## Used by

- Applied alongside ISOpure and ElasticNet as one of three orthogonal classifiers to assign 88 mixed IDC/ILC breast tumors to ILC-like or IDC-like molecular classes in the TCGA breast cancer multi-platform study (n=817); all three methods agreed that 24/88 mixed cases were ILC-like and 64 were IDC-like, with [CDH1](../genes/CDH1.md) mutation status as the dominant feature. [PMID:26451490](../papers/26451490.md)

## Notes

- Three-classifier concordance (CLANC/ISOpure/ElasticNet) required for a confident call in the TCGA ILC/IDC mixed-tumor analysis.
- [CDH1](../genes/CDH1.md) mutation status was the dominant feature driving classification; all CDH1-mutated mixed cases were classified ILC-like regardless of classifier.

## Sources

- [PMID:26451490](../papers/26451490.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
