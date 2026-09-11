---
name: SigProfiler
slug: sigprofiler
kind: method
canonical_source: corpus
unverified: true
tags: [mutational-signatures, bioinformatics, sbs]
processed_by: crosslinker
processed_at: 2026-09-11
---

# SigProfiler

## Overview

SigProfiler is a suite of computational tools for mutational signature analysis. It extracts de novo signatures from somatic mutation catalogs using non-negative matrix factorization (NMF) and maps them to the COSMIC reference signatures (SBS, DBS, ID). SigProfilerExtractor identifies the number and composition of active signatures; SigProfilerAssignment assigns known signatures to individual samples.

## Used by

- Applied to characterize mutational signatures from somatic SNVs in endometrial polyps; identified SBS1, SBS5, and SBS40 as dominant signatures, with SBS8 and SBS89 additionally called by MutationalPatterns [PMID:41137179](../papers/41137179.md)
- Used for de novo mutational signature extraction in the pan-Asia cHCC-ICC cohort (133 cases, 173 WES tumors); identified three signatures matching COSMIC 22 (aristolochic acid, prevalent in 63.5%), COSMIC 5 (clock-like), and COSMIC 24 (aflatoxin B1, prevalent in 38.8%) [PMID:31130341](../papers/31130341.md)
- Applied in the PCAWG pan-cancer WGS flagship study (n=2,658 tumors) to identify mutational signatures; APOBEC3B-like signatures dominated kataegis foci (81.7%), with a distinct alternative GpC/CpC deaminase signature in sarcomas [PMID:32025007](../papers/32025007.md).
- Used in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS) for somatic variant calling and genomic analysis of the [lung_nci_2022](../datasets/lung_nci_2022.md) cohort [PMID:34493867](../papers/34493867.md)
- Called COSMIC v3.1 mutational signatures from whole-genome sequencing of 3 invasive lobular carcinoma cases [PMID:38347189](../papers/38347189.md).

## Notes

- Companion tool MutationalPatterns can provide complementary or confirmatory signature assignments.
- SBS1/SBS5/SBS40 are associated with age-related processes and are common in normal tissues.
- SBS8 is associated with late-replication errors; its presence in benign lesions is notable.

## Sources

- [PMID:41137179](../papers/41137179.md)
- [PMID:31130341](../papers/31130341.md)
- [PMID:32025007](../papers/32025007.md)
- [PMID:34493867](../papers/34493867.md)
- [PMID:38347189](../papers/38347189.md)

*This page was processed by **crosslinker** on **2026-09-11**.*
