---
name: Chronic Lymphocytic Leukemia (Broad, Nature 2013)
studyId: lcll_broad_2013
institution: Broad Institute
size: 160
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
panels: []
tags:
  - CLL
  - clonal-evolution
  - intratumoral-heterogeneity
  - ABSOLUTE
processed_by: entity-page-writer
processed_at: 2026-05-07
---

# Chronic Lymphocytic Leukemia (Broad, Nature 2013)

## Overview

A Broad Institute cohort of 160 matched CLL tumor/normal pairs profiled by whole-exome sequencing and Affymetrix SNP 6.0 copy number arrays, with longitudinal sampling in 18 patients. The study focused on intratumoral heterogeneity and clonal evolution, using the ABSOLUTE algorithm to classify mutations as clonal or subclonal and infer temporal ordering of driver acquisition.

## Composition

- 160 matched CLL tumor/normal pairs with WES (~130X average depth).
- 149 samples with both WES and copy number data analyzed by ABSOLUTE.
- 111 samples also profiled with [Affymetrix SNP 6.0](../methods/affymetrix-snp6.md) for somatic copy number analysis.
- 18 patients sampled at two timepoints (median 3.5 years apart); 12 received intervening chemotherapy, 6 untreated.
- Cancer type: [CLLSLL](../cancer_types/CLLSLL.md).

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md) — 160 tumor/normal pairs at ~130X depth.
- [Affymetrix SNP 6.0](../methods/affymetrix-snp6.md) — 111 samples for somatic copy number analysis.
- [MutSig](../methods/mutsig.md) — significantly mutated gene identification.
- [GISTIC](../methods/gistic.md) — recurrent copy number alteration detection.

## Papers using this cohort

- [PMID:23415222](../papers/23415222.md) — Clonal evolution in CLL (Broad, Nature 2013).

## Notable findings derived from this cohort

- 20 putative CLL driver genes (q<0.1) identified falling into 7 core signaling pathways [PMID:23415222](../papers/23415222.md).
- 54% of detected mutations were clonal, 46% subclonal; subclonal drivers present in 146/149 samples [PMID:23415222](../papers/23415222.md).
- [MYD88](../genes/MYD88.md), trisomy 12, and hemizygous del(13q) are early/clonal events; [SF3B1](../genes/SF3B1.md), [TP53](../genes/TP53.md), and [ATM](../genes/ATM.md) are predominantly late/subclonal events [PMID:23415222](../papers/23415222.md).
- Prior chemotherapy associated with significantly higher subclonal mutation burden (P=0.048) and clonal evolution in 10/12 treated cases vs. 1/6 untreated (P=0.012) [PMID:23415222](../papers/23415222.md).
- Subclonal driver presence is an independent prognostic factor: adjusted HR 3.61 (95% CI 1.42–9.18, P=0.007) for shorter failure-free survival [PMID:23415222](../papers/23415222.md).

## Sources

- [PMID:23415222](../papers/23415222.md)

*This page was processed by **entity-page-writer** on **2026-05-07**.*
