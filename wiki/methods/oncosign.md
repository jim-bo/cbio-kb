---
name: OncoSign
slug: oncosign
kind: method
canonical_source: corpus
unverified: true
tags: [classification, breast-cancer, subtype, signature]
processed_by: crosslinker
processed_at: 2026-05-14
---

# OncoSign

## Overview

OncoSign is a molecular classification tool that assigns tumor samples to predefined oncogenic subtypes using gene expression or multi-omic signatures. In the TCGA breast cancer ILC/IDC analysis, an OncoSign-adapted classifier was used as one of three orthogonal approaches to resolve the molecular identity of histologically mixed IDC/ILC tumors, determining whether they more closely resemble pure [ILC](../cancer_types/ILC.md) or pure [IDC](../cancer_types/IDC.md) at the genomic/transcriptomic level.

## Used by

- Applied (as OncoSign-adapted classifier) alongside ISOpure and ElasticNet to assign 88 mixed IDC/ILC breast tumors to ILC-like or IDC-like molecular classes in the TCGA breast cancer multi-platform study (n=817); concordant with the other two classifiers in placing 24/88 cases as ILC-like and 64/88 as IDC-like; [CDH1](../genes/CDH1.md) mutation was the dominant discriminating feature. [PMID:26451490](../papers/26451490.md)

## Notes

- Described in Ciriello et al. (2015) as an adaptation of the OncoSign framework for ILC/IDC distinction.
- Three-classifier concordance (OncoSign/ISOpure/ElasticNet) used to increase confidence in mixed-tumor classification calls.

## Sources

- [PMID:26451490](../papers/26451490.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
