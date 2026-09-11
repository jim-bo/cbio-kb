---
name: OncodriveFM
slug: oncodrivefm
kind: method
canonical_source: corpus
unverified: true
tags: [driver-gene-discovery, bioinformatics]
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# OncodriveFM

## Overview

A driver-gene discovery method that scores genes for a functional mutation bias — an excess accumulation of predicted high-impact/deleterious mutations relative to a null background — to nominate cancer driver genes from somatic mutation calls. Distinct from the related OncodriveFML, which folds in non-coding regions and a ratiometric functional-impact score.

## Used by

- One of five driver-discovery tools (with MutSig2CV, OncodriveCLUST, e-Driver and dNdScv) run on nonhypermutated colorectal tumors; genes called by more than one tool contributed to a 46-gene high-confidence significantly-mutated-gene set [PMID:35487942](../papers/35487942.md).

## Notes

- Complements MutSigCV-style frequency-based driver calling by scoring functional-impact bias rather than mutation recurrence alone.
- Typically combined with other driver-discovery tools; genes are kept as high-confidence when called by more than one method.

## Sources

- [PMID:35487942](../papers/35487942.md)

*This page was processed by **entity-page-writer** on **2026-09-10**.*
