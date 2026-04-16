---
name: NSCLC Radiogenomics (Stanford / AMC)
studyId: nsclc-radiogenomics-stanford
institution: Stanford University; Amsterdam Medical Center
size: 211
reference_genome: hg19
canonical_source: corpus
unverified: true
assays:
  - ct-imaging
  - fdg-pet-ct
  - rna-seq
  - gene-expression-microarray
  - snapshot-pcr
  - fish
panels: []
tags:
  - nsclc
  - luad
  - lusc
  - radiogenomics
  - tcia
  - ct
  - pet-ct
  - rna-seq
  - dataset-paper
processed_by: entity-page-writer
processed_at: 2026-04-15
processed_by: crosslinker
---

# NSCLC Radiogenomics (Stanford / AMC)

## Overview

A multi-modal radiogenomics dataset of 211 [NSCLC](../cancer_types/NSCLC.md) patients from two cohorts: 162 in the R01 cohort (Stanford / Stanford-affiliated institutions) and 49 in the AMC cohort (Amsterdam Medical Center). The dataset pairs pretreatment CT and FDG PET/CT imaging with clinical mutational testing ([EGFR](../genes/EGFR.md), [KRAS](../genes/KRAS.md), [ALK](../genes/ALK.md) / [EML4](../genes/EML4.md) fusion), bulk RNA-seq (n=130), Illumina HT-12 microarray (n=26), semantic CT annotations (n=190), and longitudinal clinical outcomes. Published by Bakr et al. 2018 and hosted on TCIA (DOI 10.7937/K9/TCIA.2017.7hs46erv); gene expression data also deposited at GEO (GSE28827 microarray; GSE103584 RNA-seq). [PMID:30325352](../papers/30325352.md)

## Composition

- **Cancer types**: [NSCLC](../cancer_types/NSCLC.md) — 172 [LUAD](../cancer_types/LUAD.md) (adenocarcinoma), 35 [LUSC](../cancer_types/LUSC.md) (squamous cell carcinoma), 4 NOS.
- **R01 cohort**: n=162 (38F/124M, mean age 68, range 42–86); AMC cohort: n=49 (33F/16M, mean age 67, range 24–80).
- **Imaging**: CT for all 211; FDG PET/CT for 201; CT tumour segmentations for 144; semantic CT annotations for 190.
- **Molecular**: EGFR mutational testing (n=206), KRAS (n=205), ALK by FISH (n=196); RNA-seq (n=130, Illumina HiSeq 2500, aligned to hg19 with STAR, quantified with Cufflinks FPKM); microarray (n=26 Illumina HT-12, 17 overlapping with RNA-seq).
- **Clinical**: survival, recurrence, smoking history, pathological TNM stage (n=161), histopathological grade (n=162), adjuvant and systemic therapy.
- **Semantic annotations**: 28 nodule analysis features + parenchymal features encoded in AIM format using ePAD; annotated by a single radiologist with >20 years experience. [PMID:30325352](../papers/30325352.md)

## Assays / panels (linked)

- [CT radiomics](../methods/ct-radiomics.md) and FDG-PET/CT imaging.
- RNA-seq (Illumina HiSeq 2500, TruSeq Total Stranded RNA + Ribo-Zero, STAR v2.3 / Cufflinks v2.0.2, hg19).
- Illumina HT-12 gene expression microarray (GEO: GSE28827).
- SNaPshot multiplex PCR for EGFR / KRAS; FISH for EML4-ALK.

## Papers using this cohort

- [PMID:30325352](../papers/30325352.md) — Bakr et al. 2018, *Scientific Data*: primary dataset descriptor; 211 NSCLC patients with paired CT, PET/CT, RNA-seq, and mutational data; TCIA DOI 10.7937/K9/TCIA.2017.7hs46erv.

## Notable findings derived from this cohort

- 130 of 211 subjects have the complete quartet of clinical, CT, PET/CT, and RNA-seq data, enabling multi-modal radiogenomic analysis. [PMID:30325352](../papers/30325352.md)
- EGFR and KRAS mutation status were clinically tested in 206/211 and 205/211 subjects respectively using SNaPshot PCR covering EGFR exons 18–21 and KRAS exon 2; prior published work used subsets to build radiomic–genomic association maps. [PMID:30325352](../papers/30325352.md)

## Sources

- TCIA collection: NSCLC-Radiogenomics — TCIA DOI 10.7937/K9/TCIA.2017.7hs46erv
- GEO microarray: GSE28827; GEO RNA-seq: GSE103584
- [PMID:30325352](../papers/30325352.md) — Bakr et al. 2018, *Scientific Data*, DOI 10.1038/sdata.2018.202.

*This page was processed by **crosslinker** on **2026-04-15**.*
