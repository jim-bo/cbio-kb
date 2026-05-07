---
name: Colorectal Adenocarcinoma (TCGA, Nature 2012)
studyId: coadread_tcga_pub
institution: The Cancer Genome Atlas (TCGA)
size: 276
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
panels: []
tags:
  - colorectal
  - tcga
  - coadread
processed_by: entity-page-writer
processed_at: "2026-05-06"
---

# Colorectal Adenocarcinoma (TCGA, Nature 2012)

## Overview

The TCGA colorectal cancer dataset comprises 276 colorectal carcinoma tumor/normal pairs collected as part of The Cancer Genome Atlas project. It is the landmark comprehensive molecular characterization of colorectal adenocarcinoma, covering [COADREAD](../cancer_types/COADREAD.md) (colon and rectal cancers together). Samples were collected from multiple institutions and subjected to multi-platform molecular profiling including exome sequencing, low-pass WGS, copy-number arrays, methylation profiling, and gene expression.

## Composition

- 276 colorectal carcinoma tumor/normal pairs
- Cancer type: [COADREAD](../cancer_types/COADREAD.md) (colorectal adenocarcinoma)
- 224 pairs analyzed by whole-exome sequencing; 97 by low-pass whole-genome sequencing (~3-4X)
- 257 tumors profiled for somatic copy-number alterations with [Affymetrix SNP 6.0](../methods/affymetrix-snp6.md) arrays
- 236 tumors profiled for promoter DNA methylation (Illumina HumanMethylation27)
- mRNA expression (Agilent microarrays + RNA-Seq), miRNA expression
- 16% of tumors classified as hypermutated; 84% non-hypermutated

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — 224 pairs, 103-fold mean coverage
- [whole-genome-seq](../methods/whole-genome-seq.md) — 97 pairs, ~3-4X low-pass coverage
- [affymetrix-snp6](../methods/affymetrix-snp6.md) — 257 tumors for somatic copy-number analysis
- [gistic](../methods/gistic.md) — applied to SNP 6.0 copy-number data
- [mutsig](../methods/mutsig.md) — significance testing for somatic mutations

## Papers using this cohort

- [PMID:22810696](../papers/22810696.md) — TCGA Nature 2012 primary analysis

## Notable findings derived from this cohort

- 24 significantly mutated genes identified including [APC](../genes/APC.md) (81%), [TP53](../genes/TP53.md) (60%), [KRAS](../genes/KRAS.md) (43%), [PIK3CA](../genes/PIK3CA.md) (18%), and novel candidates [ARID1A](../genes/ARID1A.md), [SOX9](../genes/SOX9.md), [AMER1](../genes/AMER1.md) [PMID:22810696](../papers/22810696.md)
- 16% of CRCs are hypermutated; of these 75% are MSI-H with [MLH1](../genes/MLH1.md) methylation/CIMP, 25% have somatic mismatch-repair or [POLE](../genes/POLE.md) mutations [PMID:22810696](../papers/22810696.md)
- Non-hypermutated colon and rectal cancers are genomically indistinguishable by copy number, methylation, mRNA, and miRNA patterns [PMID:22810696](../papers/22810696.md)
- WNT signaling pathway altered in 93% of all tumors; [ERBB2](../genes/ERBB2.md) amplification (4%) identified as potentially targetable with [trastuzumab](../drugs/trastuzumab.md) [PMID:22810696](../papers/22810696.md)

## Sources

- [PMID:22810696](../papers/22810696.md) — TCGA, Nature 2012

*This page was processed by **entity-page-writer** on **2026-05-06**.*
