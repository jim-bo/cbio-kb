---
name: Small Cell Lung Cancer (JHU, Nature Genetics 2012)
studyId: sclc_jhu
institution: Johns Hopkins University (JHU)
size: 80
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - rna-seq
  - gistic
panels: []
tags:
  - SCLC
  - lung
  - WES
  - WGS
  - RNA-seq
  - GISTIC
processed_by: entity-page-writer
processed_at: 2026-05-06
---

# Small Cell Lung Cancer (JHU, Nature Genetics 2012)

## Overview

80 human [SCLC](../cancer_types/SCLC.md) samples (36 primary tumour-normal pairs, 17 matched cell lines, 4 unpaired primary tumours, and 23 unpaired cell lines) characterised by exome sequencing, whole-genome sequencing, RNA-seq, and copy-number analysis at Johns Hopkins University. Published in Nature Genetics 2012. The study identified [SOX2](../genes/SOX2.md) amplification as a major oncogenic event and discovered the recurrent RLF-MYCL fusion transcript. [PMID:22941189](../papers/22941189.md)

## Composition

- 80 human SCLC samples total: 36 primary tumour-normal pairs, 17 paired cell lines with matched lymphoblastoid lines, 4 unpaired primary tumours, 23 unpaired cell lines.
- 56 samples assayed by Illumina HumanOmni2.5 SNP arrays for copy-number analysis.
- 110 independent primary SCLC tumour samples used for SOX2 IHC/FISH validation.
- Reference genome: GRCh37/hg19.
- Cancer type: [SCLC](../cancer_types/SCLC.md). [PMID:22941189](../papers/22941189.md)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — 42 tumour-normal pairs (primary + cell lines)
- [whole-genome-seq](../methods/whole-genome-seq.md) — structural variant detection
- [rna-seq](../methods/rna-seq.md) — fusion transcript discovery (RLF-MYCL)
- [gistic](../methods/gistic.md) — copy-number analysis from Illumina HumanOmni2.5 SNP arrays

## Papers using this cohort

- [PMID:22941189](../papers/22941189.md) — primary characterisation study (Rudin et al., Nature Genetics 2012)

## Notable findings derived from this cohort

- 22 significantly mutated genes identified (q ≥ 1, FDR ≤ 10%) including [TP53](../genes/TP53.md) and [RB1](../genes/RB1.md). [PMID:22941189](../papers/22941189.md)
- Mean nonsynonymous mutation rate 5.5 mutations/Mb (excluding one hypermutated sample); G-to-T transversions predominant (tobacco). [PMID:22941189](../papers/22941189.md)
- [SOX2](../genes/SOX2.md) amplification (copy number ≥ 4) in ~27% (15/56) of samples; shRNA knockdown reduced proliferation (P < 0.01). [PMID:22941189](../papers/22941189.md)
- Recurrent RLF-[MYCL](../genes/MYCL.md) fusion found in 1 primary tumour and 4 cell lines; siRNA targeting [MYCL](../genes/MYCL.md) reduced proliferation in fusion-positive lines. [PMID:22941189](../papers/22941189.md)
- Mutations in PI3K pathway ([PIK3CA](../genes/PIK3CA.md), AKT1-3, [MTOR](../genes/MTOR.md)), SOX family, Notch/Hedgehog ([NOTCH1](../genes/NOTCH1.md), [SMO](../genes/SMO.md)), and chromatin-modifying genes ([EP300](../genes/EP300.md)). [PMID:22941189](../papers/22941189.md)
- Four kinase gene fusions identified: NPEPPS-EPHA6, SKP1-CDKL3, NEK4-SFMBT1, ZAK-RAPGEF4. [PMID:22941189](../papers/22941189.md)

## Sources

- [PMID:22941189](../papers/22941189.md)

*This page was processed by **entity-page-writer** on **2026-05-06**.*
