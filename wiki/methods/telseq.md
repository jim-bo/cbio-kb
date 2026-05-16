---
name: TelSeq
slug: telseq
kind: MUTATION_EXTENDED
canonical_source: corpus
unverified: true
tags: [telomere-length, wgs, computational]
processed_by: crosslinker
processed_at: 2026-05-16
---

# TelSeq

## Overview

TelSeq is a computational tool for estimating telomere length from whole-genome sequencing data. It quantifies reads containing telomeric repeat sequences (TTAGGG) relative to total sequencing depth to infer mean telomere length per sample without requiring telomere-specific capture or special library preparation.

## Used by

- Applied alongside TelomereHunter in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS); LCINS [LUAD](../cancer_types/LUAD.md) telomeres were significantly longer than LUAD-smoker telomeres (6.4 Kb, 95% CI 5.3–7.6, P=7.1e-11); passive-smoker tumours had shorter telomeres (P=0.005) [PMID:34493867](../papers/34493867.md)

## Notes

- Used together with TelomereHunter to provide cross-validated telomere length estimates from the same WGS data.
- Tumour-to-normal TL ratio differed by SCNA subtype: forte 0.9 (P=0.01), piano 1.1 (P=4.7e-3, longer than matched normal).
- Telomere elongation in piano tumours was not fully explained by [TERT](../genes/TERT.md) amplification (11.6%) or promoter mutations (0.9%).

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
