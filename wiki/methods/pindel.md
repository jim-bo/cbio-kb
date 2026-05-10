---
name: Pindel
slug: pindel
kind: method
canonical_source: corpus
unverified: true
tags: [indel-calling, structural-variant, bioinformatics]
processed_by: wiki-cli
processed_at: 2026-05-09
---

# Pindel

## Overview

Pindel is a pattern growth algorithm for detecting break points of large deletions, medium-sized insertions, inversions, tandem duplications, and other structural variants at single-base resolution from paired-end short-read sequencing data. It is particularly sensitive for detecting insertion/deletion events that are difficult to call with standard short-read aligners.

## Used by

- Used in ICGC PedBrain pilocytic astrocytoma WGS study (96 cases, hg19) alongside [crest](../methods/crest.md) and [delly](../methods/delly.md) for somatic SV detection; contributed to identifying structural rearrangements including [BRAF](../genes/BRAF.md) fusions in the MAPK-pathway-driven pilocytic astrocytoma cohort [PMID:23817572](../papers/23817572.md)
- Used for small insertion/deletion detection in paired tumor/normal whole-exome sequencing of grade II glioma initial/recurrent pairs (n=23), complementing MuTect for SNV calling [PMID:24336570](../papers/24336570.md)

## Notes

- Corpus-grown slug; not found in cBioPortal canonical gene panel ontology.
- Specialized in detecting events that confound standard alignment-based variant callers, including medium-to-large indels.

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24336570](../papers/24336570.md)

*This page was processed by **wiki-cli** on **2026-05-09**.*
