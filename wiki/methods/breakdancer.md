---
name: BreakDancer
slug: breakdancer
kind: STRUCTURAL_VARIANT
canonical_source: corpus
unverified: true
tags: [structural-variant, sv-caller, wgs, bioinformatics]
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# BreakDancer

## Overview

BreakDancer is a computational tool for detecting genome-wide structural variation (SV) from paired-end sequencing data. It identifies candidate SVs — including deletions, insertions, inversions, and translocations — by analyzing anomalously mapped read pairs whose insert size, orientation, or mapping location deviate from the expected library distribution. BreakDancer has been widely used in cancer genomics studies as a SV discovery algorithm applied to whole-genome sequencing data.

## Used by

- Used alongside BamBam as a structural variant caller in the TCGA [GBM](../cancer_types/GBM.md) 2013 whole-genome sequencing analysis (n=42 tumor/normal pairs); together identified 238 high-confidence somatic rearrangements including 49 interchromosomal, 125 intrachromosomal, and 64 intragenic events, and one case of chromothripsis [PMID:24120142](../papers/24120142.md)
- BreakDancer used for structural-variant detection in the TCGA esophageal/stomach study of 164 oesophageal carcinomas and 359 gastric adenocarcinomas [PMID:28052061](../papers/28052061.md).

## Notes

- BreakDancer is based on anomalously mapped read pairs; it complements soft-clip–based callers (e.g., CREST) and assembly-based approaches.
- False-positive rates can be high in low-coverage WGS; orthogonal validation (e.g., PCR, long-read sequencing) is recommended for candidate SVs.
- Often run in ensemble with other callers (BamBam, DELLY, CREST) to increase specificity.

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:28052061](../papers/28052061.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
