---
name: Plackett-Luce Ordering
slug: plackett-luce-ordering
kind: MUTATION_EXTENDED
canonical_source: corpus
unverified: true
tags: [evolutionary-timing, statistical-model, ordering]
processed_by: crosslinker
processed_at: 2026-05-16
---

# Plackett-Luce Ordering

## Overview

Plackett-Luce ordering is a probabilistic ranking model applied to infer the temporal ordering of genomic events (mutations, copy-number alterations, whole-genome doubling) in tumour evolution. It models the probability of an observed ranked list of events as the product of conditional selection probabilities, enabling statistical inference of which alterations are most likely to occur first in the evolutionary sequence.

## Used by

- Applied in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS) to infer the temporal ordering of driver mutations and copy-number events across the piano, mezzo-forte, and forte SCNA subtypes; [TP53](../genes/TP53.md), [EGFR](../genes/EGFR.md), [KRAS](../genes/KRAS.md), and [RBM10](../genes/RBM10.md) mutations were inferred to precede WGD in most subtypes [PMID:34493867](../papers/34493867.md)

## Notes

- Used alongside DPClust-based subclonal analysis to place events in tumour time (MRCA-relative timing).
- Sherlock-Lung findings: EGFR-mutant tumours had an estimated MRCA at age 61, with clinical diagnosis ~8 years later; median tumour latency was 9.10 years (piano) vs 0.08 years (forte).
- The model is particularly suited to studies where multiple alterations are observed in each tumour and ranked by cancer-cell fraction.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
