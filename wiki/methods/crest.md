---
name: CREST
slug: crest
kind: method
canonical_source: corpus
unverified: true
tags: [structural-variant, sv-caller, bioinformatics]
processed_by: entity-page-writer
processed_at: 2026-05-11
---

# CREST

## Overview

CREST (Clipping REveals STructure) is a structural variant detection algorithm that uses soft-clipped reads from short-read sequencing alignments to identify genomic rearrangements including translocations, inversions, and insertions at single-nucleotide resolution.

## Used by

- Applied in 60-sample ACC study (55 WES + 5 WGS) for structural variant detection alongside MuTect and SomaticSniper; contributed to characterization of MYB-NFIB translocations and other somatic rearrangements [PMID:23685749](../papers/23685749.md)
- Used in ICGC PedBrain pilocytic astrocytoma WGS study (96 cases) alongside [pindel](../methods/pindel.md) and [delly](../methods/delly.md) for SV detection; identified novel [BRAF](../genes/BRAF.md) fusion partners and [NTRK2](../genes/NTRK2.md) fusions [PMID:23817572](../papers/23817572.md)
- Used for structural-variant calling in Ewing sarcoma WGS (112 tumors); STAG2 mutations correlated with elevated SV count detected by CREST [PMID:25223734](../papers/25223734.md)

## Notes

- Corpus-grown slug; not found in cBioPortal canonical gene panel ontology.
- Commonly used with DELLY and Pindel in complementary SV calling pipelines.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-11**.*
- [PMID:25223734](../papers/25223734.md)

*This page was processed by **entity-page-writer** on **2026-05-11**.*
