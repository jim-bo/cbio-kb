---
name: Battenberg
slug: battenberg
kind: COPY_NUMBER_ALTERATION
canonical_source: corpus
unverified: true
tags: [copy-number, wgs, allele-specific, subclonal]
processed_by: crosslinker
processed_at: 2026-05-21
---

# Battenberg

## Overview

Battenberg is an allele-specific copy-number analysis tool designed for whole-genome sequencing data. It calls both clonal and subclonal copy-number alterations, accounting for tumour purity and ploidy, and outputs segment-level allele-specific copy-number states including loss of heterozygosity.

## Used by

- Applied in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS) for allele-specific somatic copy-number profiling of the [lung_nci_2022](../datasets/lung_nci_2022.md) cohort [PMID:34493867](../papers/34493867.md)
- Used for allele-specific copy-number analysis in cWGTS pipeline applied to 114 pediatric/AYA solid tumor patients ([mixed_kunga_msk_2022](../datasets/mixed_kunga_msk_2022.md)) with whole-genome sequencing at median 95× tumor depth [PMID:35585047](../papers/35585047.md)

## Notes

- Designed for high-coverage WGS (mean 85× tumour, 31× normal in the Sherlock-Lung study).
- Handles subclonal copy-number states, making it suitable for studies of tumour heterogeneity.
- Outputs are commonly used to infer whole-genome doubling and loss of heterozygosity events.

## Sources

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35585047](../papers/35585047.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
