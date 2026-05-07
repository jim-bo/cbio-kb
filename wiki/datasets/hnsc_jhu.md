---
name: HNSCC JHU (Agrawal 2011)
studyId: hnsc_jhu
institution: Johns Hopkins University
size: 32
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - affymetrix-snp6
  - sanger-sequencing
panels: []
tags:
  - HNSCC
  - head-and-neck
  - exome-sequencing
processed_by: entity-page-writer
processed_at: 2026-05-06
---

# HNSCC JHU (Agrawal 2011)

## Overview

Whole-exome sequencing study of 32 primary HNSCC tumors with matched normals from Johns Hopkins University. A prevalence set of up to 88 additional HNSCC tumors was included for targeted validation of 6 recurrently mutated genes, for 120 total tumors analyzed. Platforms included Illumina GAIIx/HiSeq (17 tumors) and SOLiD V3/V4 (15 tumors) for sequencing, with Affymetrix SNP6.0 copy number analysis on 42 tumor/normal pairs and Sanger sequencing for validation.

## Composition

- Cancer type: [HNSC](../cancer_types/HNSC.md), n = 32 discovery tumors + 88 prevalence set = 120 total.
- Platforms: Illumina GAIIx/HiSeq and SOLiD V3/V4 at 77-fold (Illumina) and 44-fold (SOLiD) average coverage.
- Assays: [whole-exome-seq](../methods/whole-exome-seq.md); [affymetrix-snp6](../methods/affymetrix-snp6.md) on 42 tumor/normal pairs; [sanger-sequencing](../methods/sanger-sequencing.md) for validation.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)
- [sanger-sequencing](../methods/sanger-sequencing.md)

## Papers using this cohort

- [PMID:21798897](../papers/21798897.md) — Agrawal et al. 2011, Science; discovery sequencing study.

## Notable findings derived from this cohort

- 911 candidate somatic mutations identified in 725 genes across 32 tumors; 609 (67%) confirmed by orthogonal sequencing [PMID:21798897](../papers/21798897.md).
- [NOTCH1](../genes/NOTCH1.md) was the second most frequently mutated gene (15%), with 39% truncating mutations and 7 patients harboring biallelic mutations; first report establishing tumor suppressor role in HNSCC [PMID:21798897](../papers/21798897.md).
- HPV-negative tumors had significantly more mutations than HPV-positive tumors (20.6 vs 4.8 per tumor; p < 0.05) [PMID:21798897](../papers/21798897.md).
- Recurrent copy number gains at 11q ([CCND1](../genes/CCND1.md)), 3q ([PIK3CA](../genes/PIK3CA.md)), and 7p ([EGFR](../genes/EGFR.md)); recurrent deletions at 9p21.3 ([CDKN2A](../genes/CDKN2A.md)) [PMID:21798897](../papers/21798897.md).

## Sources

- [PMID:21798897](../papers/21798897.md)

*This page was processed by **entity-page-writer** on **2026-05-06**.*
