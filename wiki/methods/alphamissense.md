---
name: AlphaMissense
slug: alphamissense
kind: method
canonical_source: corpus
unverified: true
tags: [variant-scoring, pathogenicity, deep-learning]
processed_by: crosslinker
processed_at: 2026-05-14
---

# AlphaMissense

## Overview

AlphaMissense is a deep-learning pathogenicity predictor for amino acid substitutions developed by Google DeepMind. It leverages the AlphaFold2 protein structure framework combined with evolutionary and population-genetic features to classify missense variants as likely benign, ambiguous, or likely pathogenic. It achieves high discrimination between disease-causing and neutral variants across a wide range of genes.

## Used by

- Applied to score functional impact of somatic variants in endometrial polyps; [UBE2A](../genes/UBE2A.md) p.(Arg6Trp) received an AlphaMissense score of 0.96 (likely pathogenic), supporting its nomination as a driver alteration [PMID:28445112](../papers/28445112.md)

## Notes

- Scores range from 0 (benign) to 1 (pathogenic); threshold of ~0.56 is commonly used for "likely pathogenic."
- Best used in conjunction with other evidence (CADD, REVEL, population frequency, functional data).
- Pre-computed scores available for all possible human missense variants.

## Sources

- [PMID:28445112](../papers/28445112.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
