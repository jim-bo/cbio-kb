---
name: Esophageal Squamous Cell Carcinoma (UCLA 2014)
studyId: escc_ucla_2014
institution: Cancer Institute/Hospital, Chinese Academy of Medical Sciences / UCLA
size: 139
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
  - MRNA_EXPRESSION
panels: []
tags:
  - escc
  - esophageal-cancer
  - whole-exome-seq
  - targeted-dna-seq
  - copy-number
processed_by: entity-page-writer
processed_at: 2026-05-11
---

# Esophageal Squamous Cell Carcinoma (UCLA 2014)

## Overview

Genomic characterization cohort of 139 paired ESCC germline/tumor samples using whole-exome or targeted deep sequencing, plus somatic copy-number analysis of over 184 ESCC cases. Discovery cohort (n=20) used whole-exome sequencing (mean 79×); frequency cohort (n=119 + 10 cell lines) used targeted deep sequencing of discovery-mutated genes plus 277 cancer-relevant genes (mean 111×). Additional SCNV analysis from SNP arrays (Affymetrix 250K) and array-CGH (44K Agilent) across 184 ESCC samples. FISH validation of FGFR1 amplification in 53 additional tumors; IHC validation on TMAs. Samples collected at CAMS and Linxian Cancer Hospital; sequence data deposited at SRA (SRP033394).

## Composition

- 139 paired ESCC tumor/germline cases ([ESCC](../cancer_types/ESCC.md)); exclusively from high-incidence Chinese centers.
- 20-case discovery cohort (WES) + 119-case + 10 cell-line frequency cohort (targeted).
- SCNV analysis on 184 primary ESCC samples; FISH on additional 53 tumors.
- Only tumors with >70% malignant cells included.

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md) — discovery cohort, mean 79×
- [Targeted DNA sequencing](../methods/targeted-dna-seq.md) — frequency cohort, mean 111×
- [RNA-seq](../methods/rna-seq.md) — 4 discovery-cohort tumors
- [Affymetrix 250K SNP array](../methods/affymetrix-250k-snp-array.md) — SCNV analysis
- [Array-CGH](../methods/array-cgh-agilent-1m.md) — SCNV analysis
- [FISH](../methods/fish.md) — FGFR1 amplification validation
- [MutSigCV](../methods/mutsig.md) — significantly mutated gene calling

## Papers using this cohort

- [PMID:24686850](../papers/24686850.md) — Lin et al. (2014): genomic and molecular characterization of ESCC identifying novel drivers and XPO1 as therapeutic target.

## Notable findings derived from this cohort

- 13 significantly mutated genes identified by MutSigCV (FDR q < 0.2); novel ESCC drivers include [FAT1](../genes/FAT1.md), [FAT2](../genes/FAT2.md), [ZNF750](../genes/ZNF750.md), and [KMT2D](../genes/KMT2D.md) alongside established drivers [TP53](../genes/TP53.md), [PIK3CA](../genes/PIK3CA.md), and [NOTCH1](../genes/NOTCH1.md) [PMID:24686850](../papers/24686850.md).
- [APOBEC3B](../genes/APOBEC3B.md) implicated as the major mutagen via trinucleotide signature analysis; mRNA up-regulated in ESCC tumors [PMID:24686850](../papers/24686850.md).
- [FGFR1](../genes/FGFR1.md) newly identified as recurrently amplified: FISH confirmed amplification in 11/53 additional ESCCs; IHC showed protein up-regulation in 17.3% of tumors [PMID:24686850](../papers/24686850.md).
- [XPO1](../genes/XPO1.md) carries a recurrent D624G missense mutation; protein and mRNA overexpressed in ESCC; [selinexor](../drugs/selinexor.md) (KPT-330) induced apoptosis and growth arrest in ESCC cell lines [PMID:24686850](../papers/24686850.md).
- [CCND1](../genes/CCND1.md) at 11q13.2 was the most frequent focal amplification; additional amplification peaks involved [EGFR](../genes/EGFR.md), [MYC](../genes/MYC.md), and [KRAS](../genes/KRAS.md); [CDKN2A](../genes/CDKN2A.md) was focally deleted [PMID:24686850](../papers/24686850.md).
- RTK-MAPK-PI3K, cell-cycle, and epigenetic pathways were significantly and frequently dysregulated; 31 candidate actionable alterations identified [PMID:24686850](../papers/24686850.md).

## Sources

- [PMID:24686850](../papers/24686850.md)

*This page was processed by **entity-page-writer** on **2026-05-11**.*
