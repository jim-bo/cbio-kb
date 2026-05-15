---
name: SpliceAI
slug: splice-ai
kind: method
canonical_source: corpus
unverified: true
tags: [variant-scoring, splicing, deep-learning]
processed_by: crosslinker
processed_at: 2026-05-14
---

# SpliceAI

## Overview

SpliceAI is a deep residual neural network that predicts the impact of genetic variants on pre-mRNA splicing. It scores variants for their probability of creating or disrupting splice donor and acceptor sites within a 10 kb window. Delta scores range from 0 (no effect) to 1 (strong splice effect) for donor gain, donor loss, acceptor gain, and acceptor loss categories. SpliceAI is widely used to identify cryptic splice variants and to annotate the functional impact of intronic and exonic variants.

## Used by

- Applied to assess splice-site impact of somatic variants in endometrial polyps; [HMGA1](../genes/HMGA1.md) c.268C>G p.(Leu90Val) received a weak SpliceAI donor-site loss score of 0.25, flagging a possible but low-confidence splice effect [PMID:28445112](../papers/28445112.md)

## Notes

- Delta scores ≥0.2 are commonly used as a threshold for predicted splice disruption.
- Requires variant context (nearby exon/intron boundaries) for accurate prediction.
- Pre-computed scores available for all SNVs in the human genome.

## Sources

- [PMID:28445112](../papers/28445112.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
