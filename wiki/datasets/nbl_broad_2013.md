---
name: Neuroblastoma (Broad, TARGET 2013)
studyId: nbl_broad_2013
institution: Broad Institute / TARGET Initiative
size: 240
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
  - MRNA_EXPRESSION
panels: []
tags:
  - neuroblastoma
  - TARGET
  - pediatric
  - high-risk
processed_by: entity-page-writer
processed_at: 2026-05-07
---

# Neuroblastoma (Broad, TARGET 2013)

## Overview

A Broad Institute / TARGET Initiative cohort of 240 matched tumor/normal pairs from high-risk, metastatic (stage 4) neuroblastoma patients, profiled by whole-exome sequencing, whole-genome sequencing, and RNA-seq. This dataset provided the first large-scale characterization of the somatic mutational landscape of high-risk neuroblastoma.

## Composition

- 240 matched tumor/normal pairs from high-risk stage 4 [NBL](../cancer_types/NBL.md) patients (>18 months at diagnosis, metastatic).
- Males 62%, median age 3.4 years, [MYCN](../genes/MYCN.md) amplification in 32%.
- [Whole-exome sequencing](../methods/whole-exome-seq.md): 221 cases (~33 Mb targeted, 124X mean coverage).
- [Whole-genome sequencing](../methods/whole-genome-seq.md): 19 cases (10 Illumina at 29.7X, 10 Complete Genomics at 59.9X).
- [RNA-seq](../methods/rna-seq.md): 10 WGS cases (>10 Gbp per case).
- Reference genome: hg19/GRCh37.

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md) — primary discovery platform.
- [Whole-genome sequencing](../methods/whole-genome-seq.md) — structural variant discovery (19 cases).
- [RNA-seq](../methods/rna-seq.md) — fusion transcript analysis (10 cases).
- [MutSig](../methods/mutsig.md) — statistical significance testing.

## Papers using this cohort

- [PMID:23334666](../papers/23334666.md) — The landscape of somatic mutations in neuroblastoma (Broad/TARGET, Nature Genetics 2013).

## Notable findings derived from this cohort

- Low median exonic mutation frequency (0.60/Mb), consistent with other pediatric cancers and far below adult solid tumors [PMID:23334666](../papers/23334666.md).
- Only 5 recurrently mutated genes: [ALK](../genes/ALK.md) (9.2%), [PTPN11](../genes/PTPN11.md) (2.9%), [ATRX](../genes/ATRX.md) (9.6% including deletions), MYCN (1.7%), [NRAS](../genes/NRAS.md) (0.83%); RAS/MAPK pathway enriched in gene set analysis [PMID:23334666](../papers/23334666.md).
- ALK mutation was the only significantly mutated gene associated with decreased overall survival (p=0.0103) [PMID:23334666](../papers/23334666.md).
- ATRX alterations mutually exclusive with MYCN amplification and enriched in older children (p=0.0021) [PMID:23334666](../papers/23334666.md).
- Germline pathogenic variants enriched in ALK, [CHEK2](../genes/CHEK2.md), [PINK1](../genes/PINK1.md), and [BARD1](../genes/BARD1.md), suggesting broader predisposition than previously recognized [PMID:23334666](../papers/23334666.md).

## Sources

- [PMID:23334666](../papers/23334666.md)

*This page was processed by **entity-page-writer** on **2026-05-07**.*
