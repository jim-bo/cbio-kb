---
name: MuSE
slug: muse
kind: method
canonical_source: corpus
unverified: true
tags: [somatic-calling, snv, tumor-normal]
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# MuSE

## Overview

MuSE (Mutation calling using a Markov Substitution model for Evolution) is a somatic SNV caller for tumor/normal paired sequencing data. It models the evolutionary process of cancer cells using a Markov substitution model, enabling context-sensitive variant detection. MuSE showed the highest pair-wise agreement with MuTect among the seven callers in the TCGA MC3 project and detected the largest number of true positive SNVs alongside MuTect.

## Used by

- One of seven somatic callers in the TCGA MC3 ensemble pipeline run on DNAnexus cloud (~1.8M core-hours) across ~10,510 TCGA tumor/normal pairs from 33 cancer types; showed highest pair-wise agreement with MuTect and highest true-positive SNV detection rate alongside MuTect [PMID:29596782](../papers/29596782.md)

## Notes

- Performs best for SNV detection; indel calling is handled by other callers (Pindel, Indelocator).
- Run on the DNAnexus cloud platform in the MC3 project (not Broad Firehose).
- Non-default parameters were required for optimal performance in the MC3 context.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-15**.*
