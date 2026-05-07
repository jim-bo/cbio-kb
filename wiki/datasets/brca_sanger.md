---
name: Breast Cancer — Sanger WES (brca_sanger)
studyId: brca_sanger
institution: Wellcome Trust Sanger Institute
size: 100
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
panels: []
tags:
  - breast-cancer
  - wes
  - copy-number
processed_by: entity-page-writer
processed_at: 2026-05-06
---

# Breast Cancer — Sanger WES (brca_sanger)

## Overview

A cohort of 100 primary breast cancers (79 ER+, 21 ER-) with matched normal DNA assembled by the Wellcome Trust Sanger Institute. Whole-exome sequencing covered 21,416 protein-coding genes and 1,664 microRNAs. Copy-number analysis used Affymetrix SNP 6.0 with ASCAT v2.1. Follow-up validation sequencing extended select findings to an additional 250 breast cancers.

## Composition

- 100 primary breast tumors with matched normal blood DNA.
- 79 ER-positive, 21 ER-negative cases.
- Cancer type: [BRCA](../cancer_types/BRCA.md).
- Key clinical fields: ER status, mitosis score, tubule score, age at diagnosis.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — 21,416 protein-coding genes + 1,664 microRNA genes.
- [affymetrix-snp6](../methods/affymetrix-snp6.md) — copy-number analysis with ASCAT v2.1.

## Papers using this cohort

- [PMID:22722201](../papers/22722201.md) — Landscape of somatic mutations in breast cancer (Stephens et al., 2012).

## Notable findings derived from this cohort

- Driver mutations in ~40 cancer genes; 7 genes mutated in >10% of cases: [TP53](../genes/TP53.md), [PIK3CA](../genes/PIK3CA.md), [ERBB2](../genes/ERBB2.md), [MYC](../genes/MYC.md), [FGFR1](../genes/FGFR1.md), [GATA3](../genes/GATA3.md), [CCND1](../genes/CCND1.md) [PMID:22722201](../papers/22722201.md).
- Nine novel cancer genes established: [AKT2](../genes/AKT2.md), [ARID1B](../genes/ARID1B.md), [CASP8](../genes/CASP8.md), [CDKN1B](../genes/CDKN1B.md), [MAP3K1](../genes/MAP3K1.md), [MAP3K13](../genes/MAP3K13.md), [NCOR1](../genes/NCOR1.md), [SMARCD1](../genes/SMARCD1.md), [TBX3](../genes/TBX3.md) [PMID:22722201](../papers/22722201.md).
- 73 different combinations of mutated cancer genes across 100 tumors; most tumors showed a unique driver combination [PMID:22722201](../papers/22722201.md).
- 1,712 homozygous deletions and 1,751 amplification events detected [PMID:22722201](../papers/22722201.md).

## Sources

- [PMID:22722201](../papers/22722201.md)

*This page was processed by **entity-page-writer** on **2026-05-06**.*
