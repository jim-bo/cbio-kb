---
name: CharGer
slug: charger
kind: MUTATION_EXTENDED
canonical_source: corpus
unverified: true
tags: [germline, variant-classification, pathogenicity]
processed_by: crosslinker
processed_at: 2026-05-16
---

# CharGer

## Overview

CharGer (Characterization of Germline variants) is a tool for automated pathogenicity classification of germline variants following ACMG/AMP guidelines. It integrates evidence from ClinVar, ExAC/gnomAD, disease databases, and functional predictors to assign ACMG evidence codes and pathogenicity classes to candidate germline variants.

## Used by

- Applied in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS) for germline variant pathogenicity classification in HR-pathway and cancer-predisposition genes ([BRCA1](../genes/BRCA1.md), [BRCA2](../genes/BRCA2.md), [ATM](../genes/ATM.md), [RAD51D](../genes/RAD51D.md), [AR](../genes/AR.md), [CYP21A2](../genes/CYP21A2.md), [GLUD2](../genes/GLUD2.md)) [PMID:34493867](../papers/34493867.md)

## Notes

- Implements ACMG/AMP 2015 variant classification framework (pathogenic, likely pathogenic, uncertain significance, etc.).
- In the Sherlock-Lung cohort, germline variants in HR genes were identified in n=3 (BRCA1), n=2 (BRCA2), n=2 (ATM), and n=2 (RAD51D) cases.
- AR was the most frequently mutated cancer-susceptibility germline gene (n=5, 4 in the piano subtype).

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
