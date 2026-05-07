---
name: Lung Squamous Cell Carcinoma (TCGA, Nature 2012)
studyId: lusc_tcga_pub
institution: The Cancer Genome Atlas (TCGA)
size: 178
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - rna-seq
  - affymetrix-snp6
  - gistic
  - mutsig
panels: []
tags:
  - LUSC
  - lung
  - TCGA
  - WES
  - WGS
  - RNA-seq
  - GISTIC
  - MutSig
processed_by: entity-page-writer
processed_at: 2026-05-06
---

# Lung Squamous Cell Carcinoma (TCGA, Nature 2012)

## Overview

178 previously untreated stage I-IV lung squamous cell carcinoma tumours with matched normals comprehensively profiled by the Cancer Genome Atlas consortium using whole-exome sequencing, whole-genome sequencing, RNA-seq, miRNA-seq, copy number arrays, and methylation arrays. Published in Nature 2012. The study defined the genomic landscape of [LUSC](../cancer_types/LUSC.md), identified near-universal [TP53](../genes/TP53.md) mutation, and proposed a potential therapeutic target in 64% of tumours. [PMID:22960745](../papers/22960745.md)

## Composition

- 178 previously untreated stage I-IV [LUSC](../cancer_types/LUSC.md) tumour-normal pairs.
- 96% of patients had a history of tobacco use; median follow-up 15.8 months.
- WES: 178 tumours + matched normals (mean 121x coverage).
- WGS: 19 tumour-normal pairs (mean 54x).
- RNA-seq: 178 samples; miRNA-seq: 159 samples.
- Affymetrix SNP 6.0 copy number arrays + DNA methylation arrays. [PMID:22960745](../papers/22960745.md)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — 178 tumour-normal pairs (mean 121x)
- [whole-genome-seq](../methods/whole-genome-seq.md) — 19 tumour-normal pairs (mean 54x)
- [rna-seq](../methods/rna-seq.md) — 178 samples
- [affymetrix-snp6](../methods/affymetrix-snp6.md) — genome-wide copy number profiling
- [gistic](../methods/gistic.md) — focal amplification/deletion calling from SNP array data
- [mutsig](../methods/mutsig.md) — significantly mutated gene discovery

## Papers using this cohort

- [PMID:22960745](../papers/22960745.md) — primary TCGA characterisation (Cancer Genome Atlas Research Network, Nature 2012)

## Notable findings derived from this cohort

- Mean somatic mutation rate of 8.1 mutations/Mb (median 8.4/Mb), highest of all TCGA tumour types at publication (P < 2.2e-16). [PMID:22960745](../papers/22960745.md)
- 10 significantly mutated genes (FDR q < 0.1): [TP53](../genes/TP53.md) (81–90%), [CDKN2A](../genes/CDKN2A.md), [PTEN](../genes/PTEN.md), [PIK3CA](../genes/PIK3CA.md), [KEAP1](../genes/KEAP1.md), [KMT2D](../genes/KMT2D.md), [HLA-A](../genes/HLA-A.md), [NFE2L2](../genes/NFE2L2.md), [NOTCH1](../genes/NOTCH1.md), [RB1](../genes/RB1.md). [PMID:22960745](../papers/22960745.md)
- NFE2L2/KEAP1/CUL3 oxidative-stress pathway altered in 34% of tumours. [PMID:22960745](../papers/22960745.md)
- Squamous differentiation pathway altered in 44%: SOX2/TP63 amplification/overexpression; NOTCH1/2 loss-of-function. [PMID:22960745](../papers/22960745.md)
- PI3K/AKT pathway altered in 47%; CDKN2A/RB1 pathway altered in 72%. [PMID:22960745](../papers/22960745.md)
- Potential therapeutic targets identified in 64% of tumours. [PMID:22960745](../papers/22960745.md)

## Sources

- [PMID:22960745](../papers/22960745.md)

*This page was processed by **entity-page-writer** on **2026-05-06**.*
