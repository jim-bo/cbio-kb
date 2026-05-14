---
name: Mendelian Randomization
slug: mendelian-randomization
kind: causal_inference
canonical_source: corpus
unverified: true
tags: [causal-inference, GWAS, epidemiology, instrumental-variable]
processed_by: entity-page-writer
processed_at: 2026-05-14
---

# Mendelian Randomization

## Overview

Mendelian randomization (MR) is an epidemiological method that uses genetic variants (typically SNPs identified by GWAS) as instrumental variables to estimate the causal effect of an exposure (e.g., gut microbiota abundance) on an outcome (e.g., cancer risk). Because genetic variants are randomly assigned at conception, MR is less susceptible to reverse causation and confounding than observational studies. Two-sample MR leverages summary statistics from independent GWAS datasets for the instrument–exposure and exposure–outcome associations.

## Used by

- Synthesized in a narrative review of gut-liver axis dysregulation in cholangiocarcinoma: Mendelian randomization analyses leveraging MiBioGen gut-microbiota GWAS and IEU GWAS data (Zhang Y, Chen Z, cited) implicated elevated *Eubacterium hallii* group, *Candidatus Soleaferrea*, and *Flavonifractor* as causally increasing biliary tract cancer risk; *Dorea* and *Lachnospiraceae* ND3007 were identified as protective; *Veillonellaceae*, *Alistipes*, *Enterobacteriales*, and *Firmicutes* were causally implicated in iCCA specifically [PMID:25608663](../papers/25608663.md)

## Notes

- MR requires three assumptions: (1) the instrument is associated with the exposure; (2) the instrument is independent of confounders; (3) the instrument affects outcome only through the exposure (exclusion restriction).
- MiBioGen consortium provides the largest GWAS of gut microbiota composition available to date.
- Sensitivity analyses (MR-Egger, weighted median, weighted mode) help detect and correct for pleiotropy.
- Results are causal estimates under the IV assumptions, which may be violated if the genetic variant has pleiotropic effects.

## Sources

- [PMID:25608663](../papers/25608663.md) — Gut-liver axis review in cholangiocarcinoma (narrative review synthesizing MR causal inference data)

*This page was processed by **entity-page-writer** on **2026-05-14**.*
