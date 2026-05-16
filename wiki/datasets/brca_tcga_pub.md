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
processed_by: entity-page-writer
processed_at: 2026-05-16
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
- [PMID:32220886](../papers/32220886.md) — Pareja et al., used as an age-, menopausal-status-, and ER/HER2-matched IDC-NST comparator cohort (1:3 ratio) for synchronous DCIS genomic analysis at MSKCC.

## Notable findings derived from this cohort

- 35 significantly mutated genes identified from 510 tumor WES; only [TP53](../genes/TP53.md), [PIK3CA](../genes/PIK3CA.md), and [GATA3](../genes/GATA3.md) mutated at >10% across all subtypes [PMID:23000897](../papers/23000897.md).
- Four molecular subtypes (Luminal A, Luminal B, HER2-Enriched, Basal-like) confirmed with distinct mutational spectra and copy number landscapes [PMID:23000897](../papers/23000897.md).
- Basal-like breast cancers share striking molecular features with [HGSOC](../cancer_types/HGSOC.md) including [TP53](../genes/TP53.md) mutations, RB1/BRCA1 loss, and [MYC](../genes/MYC.md) amplification [PMID:23000897](../papers/23000897.md).
- ~20% of Basal-like tumors carry germline and/or somatic BRCA1/BRCA2 variants, identifying a population potentially amenable to [olaparib](../drugs/olaparib.md) and platinum therapy [PMID:23000897](../papers/23000897.md).
- Cross-species transcriptome concordance: 297 of 1,469 genes up-regulated in rat Pik3caH1047R/Tp53Indel tumors also enriched in TCGA [PIK3CA](../genes/PIK3CA.md)+[TP53](../genes/TP53.md) vs PIK3CA-only/WT-TP53 breast cancers (Fisher's p<1×10^-14) [PMID:26437033](../papers/26437033.md)
- Used as the 772-sample primary breast cancer reference cohort (419 HR+/HER2−, 100 HR−/HER2−, 145 HER2+) for comparison against 216 metastatic breast cancers; APOBEC signatures (2+13) contributed 31.9% of mutations in HR+/HER2− primary samples vs 58.8% in HR+/HER2− metastatic tumors (p<2e-16) [PMID:28027327](../papers/28027327.md)
- Used as a public reference cohort (n=959 RNA-seq) to show that PIK3CA + MAP3K1 co-altered tumors are significantly enriched for luminal A PAM50 subtype (p<0.0001), supporting the hypothesis that MAP3K1 loss is a surrogate for luminal A biology rather than a direct PI3K-sensitivity driver [PMID:31552290](../papers/31552290.md).
- Used as a 1:3 matched comparator cohort of age-/receptor-matched IDC-NSTs (n=81 total matches) to show that synchronous DCIS has a comparable number of non-synonymous mutations and overlapping cancer-gene mutation frequencies to invasive breast cancers; mutational frequencies of TP53, PIK3CA, and GATA3 in DCIS were indistinguishable from matched TCGA IDC-NSTs. [PMID:32220886](../papers/32220886.md)

## Sources

- [PMID:23000897](../papers/23000897.md)
- [PMID:26437033](../papers/26437033.md)
- [PMID:32220886](../papers/32220886.md)

*This page was processed by **entity-page-writer** on **2026-05-16**.*
- [PMID:28027327](../papers/28027327.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:31552290](../papers/31552290.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
