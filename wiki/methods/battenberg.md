---
name: Battenberg
slug: battenberg
kind: COPY_NUMBER_ALTERATION
canonical_source: corpus
unverified: true
tags: [copy-number, wgs, allele-specific, subclonal]
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# Battenberg

## Overview

Battenberg is an allele-specific copy-number analysis tool designed for whole-genome sequencing data. It calls both clonal and subclonal copy-number alterations, accounting for tumour purity and ploidy, and outputs segment-level allele-specific copy-number states including loss of heterozygosity.

## Used by

- Applied in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS) for allele-specific somatic copy-number profiling of the [lung_nci_2022](../datasets/lung_nci_2022.md) cohort [PMID:34493867](../papers/34493867.md)

## Notes

- Designed for high-coverage WGS (mean 85× tumour, 31× normal in the Sherlock-Lung study).
- Handles subclonal copy-number states, making it suitable for studies of tumour heterogeneity.
- Outputs are commonly used to infer whole-genome doubling and loss of heterozygosity events.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-16**.*
