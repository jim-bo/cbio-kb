---
name: TCGA Ovarian Serous Cystadenocarcinoma
studyId: ov_tcga_pub
institution: The Cancer Genome Atlas Research Network
size: 489
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
  - MRNA_EXPRESSION
  - METHYLATION
panels: []
tags:
  - ovarian-cancer
  - hgsoc
  - tcga
  - homologous-recombination-deficiency
  - brca
processed_by: entity-page-writer
processed_at: 2026-05-06
---

# TCGA Ovarian Serous Cystadenocarcinoma

## Overview

Comprehensive genomic characterization of 489 clinically annotated high-grade serous ovarian carcinoma ([HGSOC](../cancer_types/HGSOC.md)) samples from The Cancer Genome Atlas (TCGA). All patients had stage II-IV disease and received platinum-based chemotherapy (94% also received a taxane). The study integrated whole-exome sequencing (316 tumors with matched normals), DNA copy number profiling (all 489 samples via Affymetrix SNP6 arrays and Agilent arrays), mRNA expression from three platforms, miRNA expression, and Illumina 27K methylation arrays, making it one of the most comprehensive multi-platform genomic studies of ovarian cancer.

## Composition

- Cancer type: [HGSOC](../cancer_types/HGSOC.md)
- 489 stage II-IV HGSOC tumors; all received platinum-based chemotherapy; 94% received a taxane
- WES: 316 tumors with matched normals (~180,000 exons, ~18,500 genes)
- Copy number: all 489 samples via [affymetrix-snp6](../methods/affymetrix-snp6.md) and Agilent arrays
- mRNA expression from Agilent, Affymetrix HuEx, and Affymetrix U133A platforms
- Illumina 27K methylation arrays; miRNA expression
- Key clinical fields: stage, grade, overall survival, platinum response, [BRCA](../cancer_types/BRCA.md) status

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — 316 tumor/normal pairs, ~18,500 genes
- [affymetrix-snp6](../methods/affymetrix-snp6.md) — DNA copy number profiling in all 489 samples
- [gistic](../methods/gistic.md) — focal copy number analysis identifying 113 significant aberrations

## Papers using this cohort

- [PMID:21720365](../papers/21720365.md) — TCGA 2011, integrated genomic analysis of ovarian carcinoma

## Notable findings derived from this cohort

- [TP53](../genes/TP53.md) mutated in 303/316 (96%) of sequenced HGSOC samples; only 9 genes significantly mutated above background [PMID:21720365](../papers/21720365.md)
- [BRCA1](../genes/BRCA1.md) germline mutations in 9%, somatic in 3%, and promoter methylation in 11.5% of cases; [BRCA2](../genes/BRCA2.md) germline 8%, somatic 3% [PMID:21720365](../papers/21720365.md)
- Homologous recombination defects present in ~50% of tumors (BRCA1/2 mutation, [BRCA1](../genes/BRCA1.md) methylation, [PTEN](../genes/PTEN.md) deletion, EMSY amplification, [RAD51C](../genes/RAD51C.md) methylation, ATM/ATR mutation, Fanconi anemia gene mutation) [PMID:21720365](../papers/21720365.md)
- 113 significant focal DNA copy number aberrations; most common focal amplifications: [CCNE1](../genes/CCNE1.md), [MYC](../genes/MYC.md), [MECOM](../genes/MECOM.md) (each >20% of tumors) [PMID:21720365](../papers/21720365.md)
- Four transcriptional subtypes identified: Immunoreactive, Differentiated, Proliferative, Mesenchymal [PMID:21720365](../papers/21720365.md)
- [FOXM1](../genes/FOXM1.md) transcription factor network activated in 87% of cases; [RB1](../genes/RB1.md) pathway deregulated in 67%; PI3K/RAS in 45% [PMID:21720365](../papers/21720365.md)
- [CCNE1](../genes/CCNE1.md) amplification mutually exclusive with BRCA inactivation (FDR-adjusted P = 0.0048) [PMID:21720365](../papers/21720365.md)
- HR defects in ~50% of tumors provide rationale for [olaparib](../drugs/olaparib.md) PARP inhibitor therapy beyond germline BRCA carriers [PMID:21720365](../papers/21720365.md)

## Sources

- [PMID:21720365](../papers/21720365.md) — TCGA Research Network, "Integrated genomic analyses of ovarian carcinoma," *Nature* 2011
- cBioPortal: https://www.cbioportal.org/study/summary?id=ov_tcga_pub

*This page was processed by **entity-page-writer** on **2026-05-06**.*
