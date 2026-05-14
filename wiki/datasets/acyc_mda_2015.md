---
name: Adenoid Cystic Carcinoma — MD Anderson 2015
studyId: acyc_mda_2015
institution: MD Anderson Cancer Center
size: 102
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-genome-seq
  - fish
  - sanger-sequencing
  - quantitative-rt-pcr
  - immunohistochemistry
  - microarray-gene-expression
panels: []
tags:
  - salivary-gland-cancer
  - adenoid-cystic-carcinoma
  - ACYC
  - rare-cancers
  - gene-fusion
  - myb-family
processed_by: crosslinker
processed_at: 2026-05-14
---

# Adenoid Cystic Carcinoma — MD Anderson 2015

## Overview

Whole-genome sequencing of 21 salivary adenoid cystic carcinoma (ACC; [ACYC](../cancer_types/ACYC.md)) tumors from MD Anderson Cancer Center (1981–2011), with FISH/RT-PCR validation extended to 81 additional tumors (total n=102). The study was designed to characterize the genetic landscape of t(6;9)-negative ACCs lacking the canonical MYB-NFIB fusion. WGS was performed on the Complete Genomics cPAL platform aligned to NCBI Build 37 (hg19).

## Composition

- **Test set (n=21):** WGS-profiled; 9 t(6;9)-positive (6 with confirmed MYB-NFIB fusion), 12 t(6;9)-negative.
- **Validation set (n=81):** 45 t(6;9)-positive, 36 t(6;9)-negative; characterized by FISH, RT-PCR, and Sanger sequencing.
- Cancer type: [ACYC](../cancer_types/ACYC.md) (adenoid cystic carcinoma — salivary gland).
- Expression profiling: Illumina HumanHT-12 V4 microarrays (ArrayExpress E-MTAB-1397) on a subset.

## Assays / panels (linked)

- [whole-genome-seq](../methods/whole-genome-seq.md) (Complete Genomics cPAL; hg19/NCBI Build 37)
- [fish](../methods/fish.md) ([MYBL1](../genes/MYBL1.md) RP11-271O1 and [NFIB](../genes/NFIB.md) RP11-54D21/RP11-79B9 BAC probes)
- [quantitative-rt-pcr](../methods/quantitative-rt-pcr.md)
- [sanger-sequencing](../methods/sanger-sequencing.md)
- [immunohistochemistry](../methods/immunohistochemistry.md) (anti-MYBL1 HPA008791)
- [microarray-gene-expression](../methods/microarray-gene-expression.md)
- [gsea](../methods/gsea.md)

## Papers using this cohort

- [PMID:26631609](../papers/26631609.md) — Mitani et al. 2016, "Novel [MYBL1](../genes/MYBL1.md) gene rearrangements with recurrent MYBL1-NFIB fusions in salivary adenoid cystic carcinomas lacking t(6;9) translocations," *Clinical Cancer Research*.

## Notable findings derived from this cohort

- [MYBL1](../genes/MYBL1.md)-[NFIB](../genes/NFIB.md) fusions (t(8;9) translocation) identified in 12% of the full 102-tumor cohort; all MYBL1 alterations (including MYBL1-YTHDF3 fusions and MYBL1 truncations) account for 17% of cases [PMID:26631609](../papers/26631609.md).
- Among t(6;9)-negative cases (n=48), MYBL1-NFIB fusions represent 25% (12/48), establishing a second major fusion driver in ACC [PMID:26631609](../papers/26631609.md).
- [MYB](../genes/MYB.md) and MYBL1 expression are mutually exclusive across the cohort; both fusion types delete the C-terminal negative regulatory domain of their respective transcription factors [PMID:26631609](../papers/26631609.md).
- [MYB](../genes/MYB.md) alterations associated with recurrence, metastasis (P = 0.042), and shorter survival vs MYBL1-altered tumors (P = 0.010, log-rank) [PMID:26631609](../papers/26631609.md).
- 5'-NFIB fusions to non-MYB/MYBL1 partners ([XRCC4](../genes/XRCC4.md), [PTPRD](../genes/PTPRD.md)/[NKAIN2](../genes/NKAIN2.md), [AIG1](../genes/AIG1.md)) found in a subset of t(6;9)-positive/MYB-NFIB-negative tumors; all had high MYB expression driven by upstream genomic rearrangements [PMID:26631609](../papers/26631609.md).

## Sources

- [PMID:26631609](../papers/26631609.md)
- ArrayExpress: E-MTAB-1397 (expression microarrays)

*This page was processed by **crosslinker** on **2026-05-14**.*
