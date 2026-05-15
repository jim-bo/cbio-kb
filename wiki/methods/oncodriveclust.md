---
name: OncodriveCLUST
slug: oncodriveclust
kind: method
canonical_source: corpus
unverified: true
tags: [driver-discovery, bioinformatics, mutation-clustering]
processed_by: crosslinker
processed_at: 2026-05-14
---

# OncodriveCLUST

## Overview

OncodriveCLUST is a bioinformatics method for detecting cancer driver genes based on the spatial clustering of somatic mutations within codons or protein regions. It tests whether observed mutation clustering is significantly higher than expected by chance given the background mutation rate, which is a hallmark of positive selection at functional sites. It is particularly effective for identifying gain-of-function oncogenes with hotspot mutations.

## Used by

- Applied to identify recurrently mutated driver genes in endometrial polyps; nominated [UBE2A](../genes/UBE2A.md) as a novel candidate driver gene based on recurrent codon-6 hotspot mutations (score 0.83, q = 1.51 × 10⁻⁵) [PMID:28445112](../papers/28445112.md)

## Notes

- Excels at detecting oncogenes with hotspot clustering; less powerful for broadly distributed tumor suppressor mutations.
- Requires a background mutation model calibrated to the cohort's trinucleotide composition.
- Complementary to OncodriveFM and dNdScv, which use different driver-detection frameworks.

## Sources

- [PMID:28445112](../papers/28445112.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
