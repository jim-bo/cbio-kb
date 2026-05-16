---
name: SigProfiler
slug: sigprofiler
kind: method
canonical_source: corpus
unverified: true
tags: [mutational-signatures, bioinformatics, sbs]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# SigProfiler

## Overview

SigProfiler is a suite of computational tools for mutational signature analysis. It extracts de novo signatures from somatic mutation catalogs using non-negative matrix factorization (NMF) and maps them to the COSMIC reference signatures (SBS, DBS, ID). SigProfilerExtractor identifies the number and composition of active signatures; SigProfilerAssignment assigns known signatures to individual samples.

## Used by

- Applied to characterize mutational signatures from somatic SNVs in endometrial polyps; identified SBS1, SBS5, and SBS40 as dominant signatures, with SBS8 and SBS89 additionally called by MutationalPatterns [PMID:28445112](../papers/28445112.md)
- Used for de novo mutational signature extraction in the pan-Asia cHCC-ICC cohort (133 cases, 173 WES tumors); identified three signatures matching COSMIC 22 (aristolochic acid, prevalent in 63.5%), COSMIC 5 (clock-like), and COSMIC 24 (aflatoxin B1, prevalent in 38.8%) [PMID:31130341](../papers/31130341.md)

## Notes

- Companion tool MutationalPatterns can provide complementary or confirmatory signature assignments.
- SBS1/SBS5/SBS40 are associated with age-related processes and are common in normal tissues.
- SBS8 is associated with late-replication errors; its presence in benign lesions is notable.

## Sources

- [PMID:28445112](../papers/28445112.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:31130341](../papers/31130341.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
