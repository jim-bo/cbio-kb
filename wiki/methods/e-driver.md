---
name: e-Driver
slug: e-driver
kind: method
canonical_source: corpus
unverified: true
tags: [driver-discovery, somatic-mutation, bioinformatics]
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# e-Driver

## Overview

e-Driver is a driver-gene discovery method that tests for significant clustering of somatic mutations within protein domains and functional regions, complementing frequency-based and dN/dS-based significance tools.

## Used by

- One of five driver-discovery tools (with MutSig2CV, OncodriveCLUST, OncodriveFM, dNdScv) run on nonhypermutated colorectal tumors; genes called by more than one tool were kept, yielding 46 high-confidence significantly mutated genes [PMID:35487942](../papers/35487942.md)

## Notes

- Used as part of a consensus (≥2 tools) driver-calling strategy alongside frequency-based and dN/dS-based methods such as [dNdScv](../methods/dndscv.md) and [MutSigCV](../methods/mutsigcv.md).

## Sources

- [PMID:35487942](../papers/35487942.md) — Asian colorectal cancer WES cohort; e-Driver used as one of five driver-discovery tools in a consensus calling scheme.

*This page was processed by **entity-page-writer** on **2026-09-10**.*
