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
processed_by: entity-page-writer
processed_at: 2026-05-11
---

# ABSOLUTE

## Overview

ABSOLUTE (Absolute quantification of somatic DNA alterations Using Tumor Heterogeneity) is a computational method that infers tumor purity, ploidy, and the absolute allele-specific copy number of somatic alterations from high-throughput sequencing or SNP-array data. By modeling the distribution of variant allele fractions alongside copy-number profiles, ABSOLUTE converts relative copy-number signals into integer absolute copy numbers and estimates the cancer cell fraction (clonality) of each mutation. It was developed at the Broad Institute and is widely applied in cancer genome studies requiring accurate purity correction before downstream SCNA or mutation analyses.

## Used by

- Used in the WGS-based chromoplexy study of 57 prostate tumors alongside ChainFinder, CLONET, MuTect, Indelocator, dRanger, BreakPointer, and GISTIC v2 for comprehensive somatic variant characterization; WGS-vs-ABSOLUTE purity concordance was R²=0.99 [PMID:23622249](../papers/23622249.md)
- Applied to 203 multiple myeloma tumor/normal pairs for tumor purity estimation, integer copy-number reconstruction, LOH inference, and cancer-cell-fraction (CCF) estimation; enabled characterization of pervasive subclonal architecture including detection of subclonal driver mutations in [KRAS](../genes/KRAS.md), [NRAS](../genes/NRAS.md), and [BRAF](../genes/BRAF.md) [PMID:24434212](../papers/24434212.md)
- Used to estimate tumor purity and ploidy for copy-number calling from WES of 39 aggressive cSCC tumors; ABSOLUTE-adjusted copy number revealed gains on chr7, 8q, 9q and losses on 3p, 9p including CDKN2A focal deletions [PMID:25303977](../papers/25303977.md)

## Notes

- Requires matched tumor/normal data and a copy-number profile (from SNP arrays or WGS).
- Purity and ploidy estimates are presented as a ranked list of solutions; manual review of the top solutions is recommended.
- Output is used to determine whether mutations are clonal or subclonal based on cancer cell fraction.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-11**.*
- [PMID:24434212](../papers/24434212.md)

*This page was processed by **entity-page-writer** on **2026-05-11**.*
- [PMID:25303977](../papers/25303977.md)

*This page was processed by **entity-page-writer** on **2026-05-11**.*
