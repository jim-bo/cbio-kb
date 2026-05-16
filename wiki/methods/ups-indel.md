---
name: UPS-INDEL
slug: ups-indel
kind: MUTATION_EXTENDED
canonical_source: corpus
unverified: true
tags: [indel-calling, wgs, structural-variant]
processed_by: crosslinker
processed_at: 2026-05-16
---

# UPS-INDEL

## Overview

UPS-INDEL is a somatic insertion and deletion (indel) calling tool optimised for whole-genome sequencing data. It focuses on detecting small indels in tumour-normal paired WGS with high sensitivity and specificity, particularly in complex genomic regions.

## Used by

- Applied in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS) for somatic indel detection as part of the multi-caller variant-calling pipeline for the [lung_nci_2022](../datasets/lung_nci_2022.md) cohort [PMID:34493867](../papers/34493867.md)

## Notes

- Used alongside MuTect and Strelka for somatic SNV and indel calling in the Sherlock-Lung WGS pipeline.
- [ERBB2](../genes/ERBB2.md) mutations in the Sherlock-Lung cohort were all indels (3.9% of tumours), making accurate indel calling critical for driver identification.
- Indel burden was low overall (median 0.06 Mut/Mb), consistent with the never-smoker low-TMB context.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
