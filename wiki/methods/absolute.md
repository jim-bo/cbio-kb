---
name: ABSOLUTE
slug: absolute
kind: method
canonical_source: corpus
unverified: false
tags:
  - copy-number
  - tumor-purity
  - clonality
  - somatic-copy-number
processed_by: wiki-cli
processed_at: 2026-05-14
---

# ABSOLUTE

## Overview

ABSOLUTE (Absolute quantification of somatic DNA alterations Using Tumor Heterogeneity) is a computational method that infers tumor purity, ploidy, and the absolute allele-specific copy number of somatic alterations from high-throughput sequencing or SNP-array data. By modeling the distribution of variant allele fractions alongside copy-number profiles, ABSOLUTE converts relative copy-number signals into integer absolute copy numbers and estimates the cancer cell fraction (clonality) of each mutation. It was developed at the Broad Institute and is widely applied in cancer genome studies requiring accurate purity correction before downstream SCNA or mutation analyses.

## Used by

- Used in the WGS-based chromoplexy study of 57 prostate tumors alongside ChainFinder, CLONET, MuTect, Indelocator, dRanger, BreakPointer, and GISTIC v2 for comprehensive somatic variant characterization; WGS-vs-ABSOLUTE purity concordance was R²=0.99 [PMID:23622249](../papers/23622249.md)
- Applied to 203 multiple myeloma tumor/normal pairs for tumor purity estimation, integer copy-number reconstruction, LOH inference, and cancer-cell-fraction (CCF) estimation; enabled characterization of pervasive subclonal architecture including detection of subclonal driver mutations in [KRAS](../genes/KRAS.md), [NRAS](../genes/NRAS.md), and [BRAF](../genes/BRAF.md) [PMID:24434212](../papers/24434212.md)
- Used to estimate tumor purity and ploidy for copy-number calling from WES of 39 aggressive cSCC tumors; ABSOLUTE-adjusted copy number revealed gains on chr7, 8q, 9q and losses on 3p, 9p including [CDKN2A](../genes/CDKN2A.md) focal deletions [PMID:25303977](../papers/25303977.md)
- Used to estimate cancer cell fractions (CCFs) for [BRAF](../genes/BRAF.md), [NRAS](../genes/NRAS.md), [HRAS](../genes/HRAS.md), [KRAS](../genes/KRAS.md), and [EIF1AX](../genes/EIF1AX.md) driver mutations in 402 PTCs; all driver mutations were confirmed as largely clonal, with one exception showing subclonal [EIF1AX](../genes/EIF1AX.md) on a background of clonal [KRAS](../genes/KRAS.md) and [BRAF](../genes/BRAF.md) mutations [PMID:25417114](../papers/25417114.md)
- ABSOLUTE used to estimate copy-number purity and ploidy from Affymetrix SNP 6.0 data in 333 cutaneous melanoma samples as part of the TCGA [SKCM](../cancer_types/SKCM.md) integrative analysis. [PMID:26091043](../papers/26091043.md)
- Used as copy-number absolute quantification method in whole-exome sequencing analysis of adrenocortical carcinoma [PMID:26095796](../papers/26095796.md)
- Applied in the TCGA breast cancer ILC/IDC multi-platform study (n=817) to estimate tumor purity and ploidy, supporting clonality-corrected genomic comparisons between invasive lobular and ductal carcinoma [PMID:26451490](../papers/26451490.md)
- Used in whole-exome sequencing of 538 CLL samples (CLL8 trial cohort) to estimate tumor purity and clonal fractions, enabling CCF-based temporal ordering of driver acquisition and tracking of clonal shifts at relapse [PMID:26466571](../papers/26466571.md)

## Notes

- Requires matched tumor/normal data and a copy-number profile (from SNP arrays or WGS).
- Purity and ploidy estimates are presented as a ranked list of solutions; manual review of the top solutions is recommended.
- Output is used to determine whether mutations are clonal or subclonal based on cancer cell fraction.

## Sources

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24434212](../papers/24434212.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25303977](../papers/25303977.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25417114](../papers/25417114.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26091043](../papers/26091043.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26095796](../papers/26095796.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:26451490](../papers/26451490.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:26466571](../papers/26466571.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
