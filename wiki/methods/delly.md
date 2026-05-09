---
name: DELLY
slug: delly
kind: method
canonical_source: corpus
unverified: true
tags: [structural-variant, sv-caller, bioinformatics]
processed_by: crosslinker
processed_at: 2026-05-09
---

# DELLY

## Overview

DELLY is a structural variant detection tool that discovers deletions, tandem duplications, inversions, and translocations in paired-end short-read sequencing data by combining paired-end mapping and split-read analysis. It is designed for both germline and somatic structural variant discovery.

## Used by

- Used in ICGC PedBrain pilocytic astrocytoma WGS study (96 cases, hg19) alongside [pindel](../methods/pindel.md) and [crest](../methods/crest.md) for somatic SV detection; helped identify the full spectrum of MAPK-pathway rearrangements including novel [BRAF](../genes/BRAF.md) fusions [PMID:23817572](../papers/23817572.md)

## Notes

- Corpus-grown slug; not found in cBioPortal canonical gene panel ontology.
- Commonly used in ensemble SV-calling pipelines with CREST and Pindel.

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
