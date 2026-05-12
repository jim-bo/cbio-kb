---
name: Agilent 1M Human Oligonucleotide aCGH
slug: array-cgh-agilent-1m
kind: COPY_NUMBER_ALTERATION
canonical_source: corpus
unverified: true
tags: [copy-number, array-cgh, agilent]
processed_by: wiki-cli
processed_at: 2026-05-11
---

# Agilent 1M Human Oligonucleotide aCGH

## Overview

Array comparative genomic hybridization (aCGH) using the Agilent 1M human oligonucleotide microarray platform. Tumor DNA is co-hybridized with reference normal DNA; resulting log2 ratios are segmented (e.g., by circular binary segmentation) and subjected to copy-number calling algorithms such as RAE. At ~1 million probes, the platform provides high-resolution somatic copy-number alteration (SCNA) detection across the genome.

## Used by

- Applied to 97 high-grade urothelial carcinomas of the bladder ([BLCA](../cancer_types/BLCA.md)) cohybridized with reference normal DNA; segmented by circular binary segmentation and analyzed with the RAE algorithm at FDR <1%; identified two distinct CNA-burden subsets and recurrent focal amplifications including [ERBB2](../genes/ERBB2.md) (17q12) and [CCND1](../genes/CCND1.md) (11q13.2–13.3) [PMID:23897969](../papers/23897969.md)
- 44K Agilent array-CGH performed on 59 ESCC samples as part of a 184-sample SCNV analysis identifying 14 recurrent focal copy-number events including CCND1 amplification and CDKN2A deletion [PMID:24686850](../papers/24686850.md)
- Array CGH (Agilent) performed on 65 TET cases; data deposited in GEO (GSE55852); identified frequent arm-level gains (1q 55%) and losses (6q 29%, 6p 26%, 3p 22%, 13q 18%), with focal BCL2 amplification in aggressive histotypes [PMID:24974848](../papers/24974848.md)
- Profiling of 104 prostatectomy cases (prad_mskcc_2014 contemporary cohort) by Agilent 1M-feature array-CGH on snap-frozen samples with >70% tumor content; used to compute CNA burden as a fraction of the autosomal genome, which was independently associated with BCR (HR 1.05, P=0.008) [PMID:25024180](../papers/25024180.md)

## Notes

- Co-hybridization with reference normal DNA controls for dye bias; circular binary segmentation is the standard downstream segmentation approach.
- High-CNA-burden bladder tumors identified by this platform had structural-aberration loads second only to serous ovarian cancer across 14 tumor types (n=5,135).
- Superseded in large-scale studies by SNP 6.0 arrays and WGS-based CNA inference, but remains in use for clinical and research validation.

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24686850](../papers/24686850.md)

*This page was processed by **wiki-cli** on **2026-05-11**.*
- [PMID:24974848](../papers/24974848.md)

*This page was processed by **wiki-cli** on **2026-05-11**.*
- [PMID:25024180](../papers/25024180.md)

*This page was processed by **wiki-cli** on **2026-05-11**.*
