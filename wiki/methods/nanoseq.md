---
name: NanoSeq
slug: nanoseq
kind: method
canonical_source: corpus
unverified: true
tags: []
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# NanoSeq

## Overview

NanoSeq (Abascal et al. 2021) is a duplex single-molecule sequencing library preparation and analysis method designed to detect somatic mutations at extremely low error rates (<5 substitutions per billion base pairs). It works by generating unique molecular identifiers (UMIs) for both strands of each DNA fragment, then calling only mutations present in both strands — eliminating the PCR and sequencing errors that confound standard bulk sequencing. Coverage is typically ~1/3 of the genome per library, making it suitable for genome-wide mutation burden and mutational signature analysis but not for driver-gene discovery (insufficient sensitivity at specific loci). It can be applied to as little as 20–50 ng of DNA extracted from micro-dissected tissue.

## Used by

- Applied to epidermal DNA micro-dissected from 6-mm punch biopsies of buttock and dorsal forearm skin from 16 patients with psoriasis before and after a single course of narrowband UV-B (NB-UVB) phototherapy; quantified median mutation-burden increases of 0.55 substitutions/Mb (buttock) and 0.89 substitutions/Mb (forearm) attributable to UVR-associated COSMIC signatures SBS7a/SBS7b and DBS1. Sequencing data deposited in EGA (EGAD00001015249). [PMID:26950094](../papers/26950094.md)

## Notes

- Coverage of ~1/3 of the genome per library is not appropriate for identifying mutations in specific driver genes or quantifying clonal selection; findings are framed at the genome-wide mutation-burden and signature level.
- The error rate of <5 substitutions/billion bp enables detection of somatic mutations even in non-clonally expanded cells, unlike conventional sequencing which requires clonal amplification to rise above noise.
- The method revealed that NB-UVB-induced mutations persist beyond epidermal turnover time (no association between post-treatment biopsy timing and mutation burden; range 7–105 days post-treatment, P=0.23 buttock).

## Sources

*This page was processed by **entity-page-writer** on **2026-05-15**.*
