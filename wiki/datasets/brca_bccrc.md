---
name: BCCRC Breast Cancer WGS (brca_bccrc)
studyId: brca_bccrc
institution: BC Cancer Research Centre (BCCRC)
size: 104
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
  - MRNA_EXPRESSION
panels: []
tags:
  - breast cancer
  - TNBC
  - WGS
  - structural rearrangements
processed_by: entity-page-writer
processed_at: 2026-05-06
---

# BCCRC Breast Cancer WGS (brca_bccrc)

## Overview

The BCCRC cohort is a whole-genome and whole-exome sequencing study of primary triple-negative breast cancers (TNBC) generated at the BC Cancer Research Centre. It encompasses 104 treatment-naive primary TNBC cases with Affymetrix SNP 6.0 copy-number profiling, RNA-seq on 80 cases, and WGS/WES on 65 cases. Somatic mutations were deep-resequenced (median >20,000x) for 2,414 somatic SNVs. A validation cohort of 159 additional breast cancers (82 ER+, 77 ER-) with targeted exon resequencing of 29 genes was also included. Data are deposited at the European Genome-phenome Archive (EGAS00001000132).

## Composition

- 104 primary TNBC cases (treatment-naive)
- Cancer type: [BRCA](../cancer_types/BRCA.md)
- WGS/WES on 65 cases; RNA-seq on 80 cases; Affymetrix SNP 6.0 on 104 cases
- Validation cohort: 159 additional breast cancers (82 ER+, 77 ER-)

## Assays / panels (linked)

- [Whole-genome sequencing](../methods/whole-genome-seq.md)
- [Whole-exome sequencing](../methods/whole-exome-seq.md)
- [RNA sequencing](../methods/rna-seq.md)
- [Affymetrix SNP 6.0](../methods/affymetrix-snp6.md)

## Papers using this cohort

- [PMID:22495314](../papers/22495314.md)

## Notable findings derived from this cohort

- [TP53](../genes/TP53.md) was mutated in 62% of basal TNBC and 43% of non-basal TNBC cases; [PIK3CA](../genes/PIK3CA.md) mutated in 10.2% (7/65), [USH2A](../genes/USH2A.md) in 9.2% (6/65), [MYO3A](../genes/MYO3A.md) in 9.2% (6/65) [PMID:22495314](../papers/22495314.md)
- Somatic mutation abundance varies continuously across TNBC; ~36% of validated somatic SNVs are expressed in matched RNA-seq, consistent with subclonal heterogeneity [PMID:22495314](../papers/22495314.md)
- ~20% of cases harbor potentially actionable aberrations including [BRAF](../genes/BRAF.md) V600E, high-level [EGFR](../genes/EGFR.md) amplifications, and ERBB2/ERBB3 mutations [PMID:22495314](../papers/22495314.md)
- Structural rearrangements extensively characterized by WGS across the 65-tumor subset [PMID:22495314](../papers/22495314.md)

## Sources

- [PMID:22495314](../papers/22495314.md)

*This page was processed by **entity-page-writer** on **2026-05-06**.*
