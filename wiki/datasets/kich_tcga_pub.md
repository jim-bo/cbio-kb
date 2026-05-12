---
name: TCGA Chromophobe Renal Cell Carcinoma (2014)
studyId: kich_tcga_pub
institution: The Cancer Genome Atlas Research Network
size: "66"
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - rna-seq
  - mirna-seq
  - hm450-methylation-array
  - affymetrix-snp6
panels: []
tags:
  - tcga
  - chromophobe-renal-cell-carcinoma
  - kidney-cancer
  - multi-platform
  - mitochondrial-genome
processed_by: entity-page-writer
processed_at: 2026-05-11
---

# TCGA Chromophobe Renal Cell Carcinoma (2014)

## Overview

TCGA multi-platform characterization of 66 primary chromophobe renal cell carcinomas ([CHRCC](../cancer_types/CHRCC.md)) with matched normal tissue/blood collected from BWH, MSKCC, NCI, and MD Anderson. The study applied whole-exome sequencing, whole-genome sequencing (n=50), mtDNA sequencing (n=61), RNA-seq, miRNA-seq, HM450 methylation arrays, and Affymetrix SNP6 copy-number arrays. It is one of the TCGA pan-kidney analyses.

## Composition

- 66 primary [CHRCC](../cancer_types/CHRCC.md) tumors; histologic subtypes: classic (n=47), eosinophilic (n=19).
- Platforms: [whole-exome-seq](../methods/whole-exome-seq.md) (NimbleGen VCRome 2.1 42 MB, 90% ≥20×), [whole-genome-seq](../methods/whole-genome-seq.md) (n=50, 60×/30×), [rna-seq](../methods/rna-seq.md), [mirna-seq](../methods/mirna-seq.md), [hm450-methylation-array](../methods/hm450-methylation-array.md), [affymetrix-snp6](../methods/affymetrix-snp6.md).
- Pipelines: Mercury alignment, [gistic](../methods/gistic.md), [mutsig](../methods/mutsig.md), [meerkat](../methods/meerkat.md).
- Reference genome: hg19.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [whole-genome-seq](../methods/whole-genome-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [mirna-seq](../methods/mirna-seq.md)
- [hm450-methylation-array](../methods/hm450-methylation-array.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)

## Papers using this cohort

- [PMID:25155756](../papers/25155756.md)

## Notable findings derived from this cohort

- ChRCC has a low exonic mutation rate (~0.4/Mb); only [TP53](../genes/TP53.md) (32%) and [PTEN](../genes/PTEN.md) (9%) reached MutSig significance; 86% of cases showed characteristic loss of whole chromosomes 1, 2, 6, 10, 13, and 17 [PMID:25155756](../papers/25155756.md).
- Recurrent genomic rearrangement breakpoints within ~10 kb upstream of the [TERT](../genes/TERT.md) TSS were found in 6/50 ChRCC by WGS, associated with >500-unit TERT expression — a novel TERT-upregulation mechanism distinct from C228T/C250T point mutations [PMID:25155756](../papers/25155756.md).
- mTOR-pathway alterations ([PTEN](../genes/PTEN.md), [MTOR](../genes/MTOR.md), [TSC1](../genes/TSC1.md)/[TSC2](../genes/TSC2.md), [NRAS](../genes/NRAS.md)) spanned 23% of cases; elevated [PPARGC1A](../genes/PPARGC1A.md) and ~4× mitochondrial copy number indicate oxidative phosphorylation activation counter to the Warburg pattern of ccRCC [PMID:25155756](../papers/25155756.md).

## Sources

*This page was processed by **entity-page-writer** on **2026-05-11**.*
