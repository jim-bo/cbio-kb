---
name: RADIA
slug: radia
kind: method
canonical_source: corpus
unverified: true
tags: [variant-calling, somatic-mutations, rna-dna-integration, multi-platform]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# RADIA

## Overview

RADIA (RNA and DNA Integrated Analysis) is a somatic variant-calling tool designed to leverage both DNA (exome or genome) and RNA-seq data simultaneously. By integrating matched tumor/normal DNA and tumor RNA evidence, RADIA can improve specificity and sensitivity for somatic SNV detection, particularly for variants with RNA-level support that may be filtered as artifacts in DNA-only callers. It was developed at UCSC and was part of the TCGA multi-caller consensus mutation-calling pipeline.

## Used by

- One of four mutation callers (MuTect, Indelocator, VarScan, RADIA) used in ≥2-caller consensus strategy for somatic mutation detection across 820 TCGA diffuse glioma exomes; combined calls contributed to identification of 75 significantly mutated genes including 45 novel glioma associations [PMID:26824661](../papers/26824661.md)
- One of seven somatic callers in the TCGA MC3 ensemble pipeline, run on DNAnexus cloud across ~10,510 TCGA tumor/normal pairs [PMID:29596782](../papers/29596782.md)
- One of seven somatic callers in the MC3 pipeline applied to 11,000 TCGA PanCancer Atlas tumors for the pan-cancer germline and somatic driver analysis [PMID:29625049](../papers/29625049.md).

## Notes

- Requires matched tumor/normal DNA and optionally tumor RNA-seq as input.
- Uses RNA evidence as a supporting filter rather than calling variants on RNA alone.
- Developed as part of the TCGA somatic mutation calling framework; frequently used in TCGA pan-cancer analyses with a ≥2-caller consensus filter.
- Consensus filtering (requiring variant support from ≥2 callers) reduces false-positive rate at the cost of some sensitivity for low-VAF variants.

## Sources

- [PMID:26824661](../papers/26824661.md)

*This page was processed by **entity-page-writer** on **2026-05-14**.*
- [PMID:29596782](../papers/29596782.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
