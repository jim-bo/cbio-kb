---
name: TCGA Breast Invasive Carcinoma (TCGA, Nature 2012)
studyId: brca_tcga_pub
institution: The Cancer Genome Atlas Network
size: 825
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - COPY_NUMBER_ALTERATION
  - MUTATION_EXTENDED
  - MRNA_EXPRESSION
  - METHYLATION
  - PROTEIN_LEVEL
  - MIRNA_EXPRESSION
panels: []
tags:
  - TCGA
  - breast-cancer
  - multi-platform
  - intrinsic-subtypes
processed_by: crosslinker
processed_at: 2026-05-14
---

# TCGA Breast Invasive Carcinoma (TCGA, Nature 2012)

## Overview

Landmark multi-platform molecular characterization of 825 primary breast cancers assembled by The Cancer Genome Atlas (TCGA) Network and published in *Nature* (2012). The study integrated six genomic and proteomic platforms to define the molecular landscape of breast cancer across its major subtypes.

## Composition

- 825 patients with primary breast cancer; 466 tumors assayed across 5 platforms, 348 across all 6 platforms.
- Cancer type: [BRCA](../cancer_types/BRCA.md).
- Platforms: Agilent mRNA expression microarrays (n=547), Illumina 450k methylation arrays (n=802), [Affymetrix SNP 6.0](../methods/affymetrix-snp6.md) (n=773), microRNA sequencing (n=697), [whole-exome sequencing](../methods/whole-exome-seq.md) (n=507), Reverse Phase Protein Arrays (n=403).
- PAM50 classifier used for mRNA subtype assignment.

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md) — 507 tumors, somatic mutation discovery.
- [Affymetrix SNP 6.0](../methods/affymetrix-snp6.md) — 773 tumors, somatic copy number alterations.
- [Illumina 450k methylation array](../methods/450k-methylation-array.md) — 802 tumors, DNA methylation profiling.
- [RNA-seq](../methods/rna-seq.md) — microRNA sequencing of 697 tumors.

## Papers using this cohort

- [PMID:23000897](../papers/23000897.md) — Comprehensive molecular portraits of human breast tumors (TCGA, Nature 2012).

## Notable findings derived from this cohort

- 35 significantly mutated genes identified from 510 tumor WES; only [TP53](../genes/TP53.md), [PIK3CA](../genes/PIK3CA.md), and [GATA3](../genes/GATA3.md) mutated at >10% across all subtypes [PMID:23000897](../papers/23000897.md).
- Four molecular subtypes (Luminal A, Luminal B, HER2-Enriched, Basal-like) confirmed with distinct mutational spectra and copy number landscapes [PMID:23000897](../papers/23000897.md).
- Basal-like breast cancers share striking molecular features with [HGSOC](../cancer_types/HGSOC.md) including [TP53](../genes/TP53.md) mutations, RB1/BRCA1 loss, and [MYC](../genes/MYC.md) amplification [PMID:23000897](../papers/23000897.md).
- ~20% of Basal-like tumors carry germline and/or somatic BRCA1/BRCA2 variants, identifying a population potentially amenable to [olaparib](../drugs/olaparib.md) and platinum therapy [PMID:23000897](../papers/23000897.md).
- Cross-species transcriptome concordance: 297 of 1,469 genes up-regulated in rat Pik3caH1047R/Tp53Indel tumors also enriched in TCGA [PIK3CA](../genes/PIK3CA.md)+[TP53](../genes/TP53.md) vs PIK3CA-only/WT-TP53 breast cancers (Fisher's p<1×10^-14) [PMID:26437033](../papers/26437033.md)

## Sources

- [PMID:23000897](../papers/23000897.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26437033](../papers/26437033.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
