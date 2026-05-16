---
name: P-MACD
slug: p-macd
kind: MUTATION_EXTENDED
canonical_source: corpus
unverified: true
tags: [apobec, mutational-signatures, wgs, kataegis]
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# P-MACD

## Overview

P-MACD (Probabilistic Model for APOBEC Context Decomposition) is a computational framework for quantifying APOBEC-attributed mutations and verifying APOBEC mutational signature enrichment in tumour WGS data. It uses a probabilistic model to attribute individual mutations to APOBEC (SBS2/SBS13) activity with greater specificity than aggregate signature decomposition.

## Used by

- Used in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS) to verify APOBEC enrichment; APOBEC was dominant (>80% of SNVs) in 4 hypermutated tumours (TMB >8 Mut/Mb) and enriched in TP53-deficient (P=1.9e-8) and RTK-RAS+ (P=3.5e-8) tumours [PMID:34493867](../papers/34493867.md)

## Notes

- Applied to confirm APOBEC signature calls from SigProfiler in the Sherlock-Lung cohort.
- Approximately 58% of all 232 LCINS tumours had ≥100 SNVs attributed to APOBEC (SBS2+SBS13).
- Relevant for studies of kataegis events, which showed A3A-like and A3B-like signatures in the Sherlock-Lung cohort.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-16**.*
