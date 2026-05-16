---
name: TelomereHunter
slug: telomerehunter
kind: MUTATION_EXTENDED
canonical_source: corpus
unverified: true
tags: [telomere-length, wgs, computational]
processed_by: crosslinker
processed_at: 2026-05-16
---

# TelomereHunter

## Overview

TelomereHunter is a tool for estimating telomere content and length from whole-genome sequencing data. It extracts reads that align to telomeric repeat sequences, corrects for GC bias and tumour purity, and produces intratelomeric repeat composition and length estimates.

## Used by

- Applied alongside TelSeq in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS) to confirm telomere length differences across SCNA subtypes; LCINS [LUAD](../cancer_types/LUAD.md) tumours had significantly longer telomeres than LUAD-smoker tumours (P=7.1e-11) [PMID:34493867](../papers/34493867.md)

## Notes

- Provides complementary telomere-length estimates to TelSeq, enabling cross-validation within the same study.
- Differences in tumour-to-normal telomere length ratio (T/N TL) were statistically significant across the piano (1.1), mezzo-forte, and forte (0.9) SCNA subtypes.
- Passive-smoker tumours had shorter telomeres than non-passive-smoker tumours (P=0.005) despite no detectable SBS4 (tobacco) signature, suggesting telomere shortening as a non-mutational biological correlate of smoke exposure.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
