---
name: SNaPshot multiplex PCR
slug: snapshot-pcr
kind: method
canonical_source: corpus
unverified: true
tags: [genotyping, pcr, mutation-detection, single-base-extension]
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# SNaPshot multiplex PCR

## Overview

SNaPshot (Applied Biosystems) is a dideoxy single-base-extension assay run after multiplex PCR amplification. Primers are extended by a single fluorescently labelled dideoxynucleotide complementary to the target position; size and colour of the extension product identify the base at each interrogated locus. The method is well-suited to focused hotspot genotyping panels covering tens of positions with high sensitivity in FFPE or frozen tissue.

## Used by

- [PMID:30325352](../papers/30325352.md) — SNaPshot multiplex PCR used to detect single-nucleotide mutations in [EGFR](../genes/EGFR.md) (exons 18, 19, 20, 21) and [KRAS](../genes/KRAS.md) (exon 2, codons 12 and 13) in 206 and 205 of 211 NSCLC subjects, respectively, in the [nsclc-radiogenomics-stanford](../datasets/nsclc-radiogenomics-stanford.md) radiogenomic dataset; [ALK](../genes/ALK.md)/[EML4](../genes/EML4.md) fusion status was assessed separately by [FISH](../methods/fish.md) [PMID:30325352](../papers/30325352.md).

## Notes

- SNaPshot is a clinical-grade targeted assay; it detects only the specific codons included in the primer panel and cannot discover novel hotspots or indels outside the targeted regions.
- In the radiogenomics context, SNaPshot results are used as ground-truth mutation labels for training/validating CT-based radiogenomic prediction models [PMID:30325352](../papers/30325352.md).

## Sources

- [PMID:30325352](../papers/30325352.md)

*This page was processed by **entity-page-writer** on **2026-04-15**.*
