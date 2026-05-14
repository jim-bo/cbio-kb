---
name: MutComFocal
slug: mutcomfocal
kind: method
canonical_source: corpus
unverified: true
tags: [copy-number, mutation-integration, focal-events, multi-platform]
processed_by: entity-page-writer
processed_at: 2026-05-14
---

# MutComFocal

## Overview

MutComFocal is a computational tool developed to identify and prioritize genomic regions harboring both focal copy-number alterations and somatic point mutations within a cancer cohort. By integrating mutation frequency data with focal CNA calls (e.g., from GISTIC), it highlights candidate driver genes that are recurrently altered at both the sequence and copy-number level, providing a complementary signal to single-platform significance tests. The method helps focus attention on genomic loci under convergent selective pressure across multiple alteration classes.

## Used by

- Used as part of the integrated multi-platform genomic analysis of 1,122 TCGA diffuse gliomas to identify candidate driver loci supported by co-occurring focal CNA and somatic mutation evidence across the cohort [PMID:26824661](../papers/26824661.md)

## Notes

- Designed as a complement to GISTIC (focal CNA significance) and MutSig (mutation significance); integrates both signals to flag high-confidence driver candidates.
- Particularly useful in heterogeneous cohorts where single-platform significance thresholds may be under-powered.
- Developed in the context of TCGA pan-cancer analyses.

## Sources

- [PMID:26824661](../papers/26824661.md)

*This page was processed by **entity-page-writer** on **2026-05-14**.*
