---
name: IntClust (Integrative Cluster)
slug: intclust
kind: method
canonical_source: corpus
unverified: true
tags:
  - breast-cancer
  - copy-number
  - gene-expression
  - integrative-subtype
  - classifier
processed_by: crosslinker
processed_at: 2026-05-16
---

# IntClust (Integrative Cluster)

## Overview

IntClust is an integrative genomic subtyping framework for breast cancer that jointly clusters copy-number profiles and gene-expression data to define 11 subtypes (IntClust 1–10, with IntClust 4 split by ER status). Developed from the METABRIC dataset, IntClust subtypes are characterized by recurrent copy-number drivers that distinguish biologically and prognostically distinct disease groups. Unlike PAM50, which uses expression alone, IntClust incorporates somatic genomic architecture and therefore captures subtype-specific chromosomal amplification events (e.g., 11q13 in IntClust2, 8p12 in IntClust6, 17q23 in IntClust1, 8q24 in IntClust9).

## Used by

- Applied to 1,980 METABRIC patients (Molecular Dataset) in a non-homogeneous semi-Markov multistate model of breast cancer recurrence; IntClust identified four ER+/HER2- subgroups (IntClust 1, 2, 6, 9; 26% of ER+ tumors) with 20-year relapse probability of 42–56%, and improved late-relapse prediction C-index from 0.63 to 0.70 (P=0.00011 at 10 years) over IHC + clinical variables alone [PMID:30867590](../papers/30867590.md)

## Notes

- The 11 IntClust subtypes are defined within the [brca_metabric](../datasets/brca_metabric.md) cohort and have been validated in external breast cancer cohorts.
- Copy-number driver associations by subtype: IntClust2 — CCND1/RSF1 at 11q13 (96% of cases); IntClust6 — ZNF703/FGFR1 at 8p12 (100%); IntClust1 — [RPS6KB1](../genes/RPS6KB1.md) at 17q23 (96% gained/amplified); IntClust9 — [MYC](../genes/MYC.md) at 8q24 (89% amplified); IntClust5 — [ERBB2](../genes/ERBB2.md) amplification (highest overall relapse probability at 0.65 at 20 years).
- IntClust4ER- (within TNBC) shows persistent late-relapse risk (0.49 at 20 years) compared to IntClust10/Basal-like (0.37 at 20 years) — a clinically important distinction within TNBC.
- Not in cBioPortal gene-panels ontology; corpus-grown slug.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
