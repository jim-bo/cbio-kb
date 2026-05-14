---
name: "HCC INSERM France 2015 (Schulze et al.)"
studyId: hcc_inserm_fr_2015
institution: "INSERM / Institut Curie / Créteil / Bordeaux / Milan / Barcelona"
size: 243
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
panels: []
tags:
  - hepatocellular-carcinoma
  - mutational-signatures
  - aflatoxin
  - driver-genes
  - tert-promoter
processed_by: crosslinker
processed_at: 2026-05-14
---

# HCC INSERM France 2015 (Schulze et al.)

## Overview

Multi-institutional European whole-exome sequencing cohort of 243 surgically resected hepatocellular carcinomas ([HCC](../cancer_types/HCC.md)) with matched non-tumor liver, assembled by Schulze, Letouzé, Zucman-Rossi and colleagues at INSERM (Paris-Créteil, Bordeaux), with additional cases from Milan (n=41) and Barcelona (n=9). Published in *Nature Genetics* 2015 (PMID:25822088). Raw data deposited in EGA (EGAS00001000217, EGAS00001000679, EGAS00001001002) and ICGC data portal (release 18, 10 December 2014).

## Composition

- **N = 243** surgically resected liver tumors (193 France, 41 Italy, 9 Spain); matched non-tumor liver for all.
- **Cancer type:** [HCC](../cancer_types/HCC.md).
- **Fibrosis:** F4 cirrhosis n=118; F2–F3 n=46; F0–F1 non-fibrotic n=79.
- **Risk factors:** alcohol 41%, HCV 26%, NASH/metabolic syndrome 18%, HBV 14%, hemochromatosis 7%, unknown etiology 11%.
- **Tumor progression stages:** 7 dysplastic macronodules, 7 early [HCC](../cancer_types/HCC.md), 17 small-progressed [HCC](../cancer_types/HCC.md), 58 classic [HCC](../cancer_types/HCC.md), 29 poor-prognosis [HCC](../cancer_types/HCC.md).

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — Agilent SureSelect v2/v3/v4/v5+UTRs on Illumina HiSeq 2000 (paired-end 75 bp); mean depth 72× (~92.6% targeted bases at ≥10×).
- [sanger-sequencing](../methods/sanger-sequencing.md) — validation of 11 genes in 155 tumors; 88% sensitivity (95% CI 82–92%), 99% specificity.
- [mutational-signatures](../methods/mutational-signatures.md) — Wellcome Trust Sanger Institute NMF framework; identified 8 signatures including novel signatures 23 and 24.
- [mutsig](../methods/mutsig.md) — MutSigCV for significantly mutated gene discovery.
- [oncotator](../methods/oncotator.md) — variant annotation (alongside Alamut).

## Papers using this cohort

- [PMID:25822088](../papers/25822088.md) — Schulze et al., *Nature Genetics* 2015: whole-exome sequencing of 243 HCC; primary discovery study for this cohort.

## Notable findings derived from this cohort

- 14 significantly mutated genes (MutSigCV q < 0.05): [TP53](../genes/TP53.md), [CTNNB1](../genes/CTNNB1.md), [AXIN1](../genes/AXIN1.md), [ALB](../genes/ALB.md), [ARID1A](../genes/ARID1A.md), [ARID2](../genes/ARID2.md), [ACVR2A](../genes/ACVR2A.md), [NFE2L2](../genes/NFE2L2.md), [RPS6KA3](../genes/RPS6KA3.md), [KEAP1](../genes/KEAP1.md), [RPL22](../genes/RPL22.md), [CDKN2A](../genes/CDKN2A.md), [CDKN1A](../genes/CDKN1A.md), and [RB1](../genes/RB1.md). [PMID:25822088](../papers/25822088.md)
- Two novel mutational signatures discovered (23 and 24); signature 24 (high C>A rate) implicates aflatoxin B1 exposure and co-segregates with [TP53](../genes/TP53.md) R249S in HBV-infected patients of sub-Saharan African origin. [PMID:25822088](../papers/25822088.md)
- [TERT](../genes/TERT.md) promoter mutation is the earliest genomic event during cirrhosis-to-HCC progression; [CDKN2A](../genes/CDKN2A.md) inactivation and [FGF3](../genes/FGF3.md)/[FGF4](../genes/FGF4.md)/[FGF19](../genes/FGF19.md)/[CCND1](../genes/CCND1.md) amplification independently predict poor 60-month overall survival in R0-resected patients. [PMID:25822088](../papers/25822088.md)
- 161 putative driver genes spanning 11 recurrently altered pathways; 28% of HCC harbored at least one alteration potentially targetable by an FDA-approved drug; 86% by a drug in phase I–III trials. [PMID:25822088](../papers/25822088.md)
- Etiology-specific mutation enrichments: alcohol-related HCC enriched for [CTNNB1](../genes/CTNNB1.md), [TERT](../genes/TERT.md), [CDKN2A](../genes/CDKN2A.md), [SMARCA2](../genes/SMARCA2.md), [HGF](../genes/HGF.md); HBV-related HCC enriched for [TP53](../genes/TP53.md) mutation. [PMID:25822088](../papers/25822088.md)

## Sources

- cBioPortal study: `hcc_inserm_fr_2015`
- EGA: EGAS00001000217, EGAS00001000679, EGAS00001001002
- ICGC data portal release 18 (10 December 2014)

*This page was processed by **crosslinker** on **2026-05-14**.*
