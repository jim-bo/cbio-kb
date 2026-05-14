---
name: Agilent 1M Human Oligonucleotide aCGH
slug: array-cgh-agilent-1m
kind: COPY_NUMBER_ALTERATION
canonical_source: corpus
unverified: true
tags: [copy-number, array-cgh, agilent]
processed_by: wiki-cli
processed_at: 2026-05-14
---

# Agilent 1M Human Oligonucleotide aCGH

## Overview

Array comparative genomic hybridization (aCGH) using the Agilent 1M human oligonucleotide microarray platform. Tumor DNA is co-hybridized with reference normal DNA; resulting log2 ratios are segmented (e.g., by circular binary segmentation) and subjected to copy-number calling algorithms such as RAE. At ~1 million probes, the platform provides high-resolution somatic copy-number alteration (SCNA) detection across the genome.

## Used by

- Applied to 97 high-grade urothelial carcinomas of the bladder ([BLCA](../cancer_types/BLCA.md)) cohybridized with reference normal DNA; segmented by circular binary segmentation and analyzed with the RAE algorithm at FDR <1%; identified two distinct CNA-burden subsets and recurrent focal amplifications including [ERBB2](../genes/ERBB2.md) (17q12) and [CCND1](../genes/CCND1.md) (11q13.2–13.3) [PMID:23897969](../papers/23897969.md)
- 44K Agilent array-CGH performed on 59 [ESCC](../cancer_types/ESCC.md) samples as part of a 184-sample SCNV analysis identifying 14 recurrent focal copy-number events including [CCND1](../genes/CCND1.md) amplification and [CDKN2A](../genes/CDKN2A.md) deletion [PMID:24686850](../papers/24686850.md)
- Array CGH (Agilent) performed on 65 [TET](../cancer_types/TET.md) cases; data deposited in GEO (GSE55852); identified frequent arm-level gains (1q 55%) and losses (6q 29%, 6p 26%, 3p 22%, 13q 18%), with focal [BCL2](../genes/BCL2.md) amplification in aggressive histotypes [PMID:24974848](../papers/24974848.md)
- Profiling of 104 prostatectomy cases ([prad_mskcc_2014](../datasets/prad_mskcc_2014.md) contemporary cohort) by Agilent 1M-feature array-CGH on snap-frozen samples with >70% tumor content; used to compute CNA burden as a fraction of the autosomal genome, which was independently associated with [BCR](../genes/BCR.md) (HR 1.05, P=0.008) [PMID:25024180](../papers/25024180.md)
- Agilent SurePrint G3 1M array-CGH used to profile copy-number alterations in seven prostate cancer organoid lines; identified [PTEN](../genes/PTEN.md) homozygous deletions, [CHD1](../genes/CHD1.md) loss, [AR](../genes/AR.md) amplification, and RB1/CDKN2A alterations (note: missed a complete [RB1](../genes/RB1.md) deletion detected by RNA-seq). [PMID:25201530](../papers/25201530.md)
- Agilent Human Genome 244A + Sureprint G3 array-CGH applied to 18 [PCNSL](../cancer_types/PCNSL.md) cases; CNA calling via Nexus RANK segmentation filtered with TCAG and 10 in-house HapMap controls; identified median 21 copy-number abnormalities/patient. [PMID:25991819](../papers/25991819.md)
- Agilent 1M array-CGH used for copy-number alteration profiling in colorectal cancer [PMID:26343386](../papers/26343386.md)

## Notes

- Co-hybridization with reference normal DNA controls for dye bias; circular binary segmentation is the standard downstream segmentation approach.
- High-CNA-burden bladder tumors identified by this platform had structural-aberration loads second only to serous ovarian cancer across 14 tumor types (n=5,135).
- Superseded in large-scale studies by SNP 6.0 arrays and WGS-based CNA inference, but remains in use for clinical and research validation.

## Sources

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24686850](../papers/24686850.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24974848](../papers/24974848.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25024180](../papers/25024180.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25201530](../papers/25201530.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25991819](../papers/25991819.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26343386](../papers/26343386.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
