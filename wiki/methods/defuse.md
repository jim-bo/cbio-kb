---
name: deFuse
slug: defuse
kind: method
canonical_source: corpus
unverified: true
tags: [fusion-calling, rna-seq, bioinformatics]
processed_by: crosslinker
processed_at: 2026-05-09
---

# deFuse

## Overview

deFuse is a computational tool for fusion gene discovery from RNA-seq data. It uses discordant reads and split reads to detect gene fusions, applying multiple statistical filters to reduce false positives. It operates on paired-end RNA-seq reads without requiring a known list of fusion genes.

## Used by

- Applied in ICGC PedBrain pilocytic astrocytoma study (n=73 cases with matched RNA-seq) alongside TopHat-Fusion for comprehensive fusion gene discovery; identified novel [BRAF](../genes/BRAF.md) fusions ([RNF130](../genes/RNF130.md):BRAF, [CLCN6](../genes/CLCN6.md):BRAF, [MKRN1](../genes/MKRN1.md):BRAF, [GNAI1](../genes/GNAI1.md):BRAF) and [NTRK2](../genes/NTRK2.md) fusions ([QKI](../genes/QKI.md):NTRK2, [NACC2](../genes/NACC2.md):NTRK2) [PMID:23817572](../papers/23817572.md)

## Notes

- Corpus-grown slug; not found in cBioPortal canonical gene panel ontology.
- Typically used in tandem with TopHat-Fusion for complementary fusion-calling sensitivity.

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
