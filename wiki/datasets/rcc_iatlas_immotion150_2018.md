---
name: Renal Cell Carcinoma (IMmotion150 Clinical Trial, Nat Med. 2018) - iAtlas Harmonized
studyId: rcc_iatlas_immotion150_2018
institution: Multi-institutional IMmotion150 trial (96 institutions); reprocessed by CRI iAtlas
size: 263
reference_genome: hg38
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - rna-seq
panels: []
tags:
  - renal-cell-carcinoma
  - RCC
  - atezolizumab
  - bevacizumab
  - sunitinib
  - clinical-trial
processed_by: crosslinker
processed_at: 2026-09-11
---

# Renal Cell Carcinoma (IMmotion150 Clinical Trial, Nat Med. 2018) - iAtlas Harmonized

## Overview

IMmotion150: a randomized, open-label phase 2 trial (96 institutions) in 305 patients with treatment-naive metastatic renal cell carcinoma ([RCC](../cancer_types/RCC.md)), randomizing 1:1:1 to [atezolizumab](../drugs/atezolizumab.md) + [bevacizumab](../drugs/bevacizumab.md), atezolizumab alone, or [sunitinib](../drugs/sunitinib.md); sequencing data reprocessed and harmonized by CRI iAtlas. Name, institution, size (263) and reference genome (hg38) are taken from the cBioPortal study record in `schema/ontology/studies.json`, matching the 263 tumors with RNA-seq described in the paper [PMID:29867230](../papers/29867230.md).

## Composition

- ITT population N=305: [atezolizumab](../drugs/atezolizumab.md) + [bevacizumab](../drugs/bevacizumab.md) (n=101), atezolizumab alone (n=103), [sunitinib](../drugs/sunitinib.md) (n=101); predominant clear cell histology ([CCRCC](../cancer_types/CCRCC.md)) in 92–96% per arm, sarcomatoid component in 14–15% [PMID:29867230](../papers/29867230.md).
- Whole-transcriptome RNA-seq on 263 pretreatment tumors; tumor/PBMC whole-exome sequencing generated for 208 patients, with 201 tumors evaluable for mutation analysis [PMID:29867230](../papers/29867230.md).

## Assays / panels (linked)

- [RNA-seq](../methods/rna-seq.md) (Illumina TruSeq RNA Access, aligned to NCBI Build 38 with GSNAP) [PMID:29867230](../papers/29867230.md).
- [Whole-exome sequencing](../methods/whole-exome-seq.md) (Agilent SureSelect v5, 51 Mb); somatic calls from the union of LoFreq and Strelka [PMID:29867230](../papers/29867230.md).

## Papers using this cohort

- [PMID:29867230](../papers/29867230.md) — McDermott et al., source publication: reports the randomized phase 2 efficacy comparison and Angio/Teff/myeloid-inflammation gene-expression signature biomarker analysis.

## Notable findings derived from this cohort

- Neither atezolizumab arm improved PFS over sunitinib in the ITT population (HR 1.00 and 1.19); in patients with PD-L1 on ≥1% of tumor-infiltrating immune cells, atezolizumab + bevacizumab showed a favorable PFS trend (14.7 vs 7.8 months, HR 0.64) [PMID:29867230](../papers/29867230.md).
- Tumor mutation burden and neoantigen burden did not predict outcome; instead, Angio (angiogenesis), Teff (T-effector/IFN-γ) and myeloid-inflammation gene-expression signatures separated arms — sunitinib performed best in AngioHigh and *[PBRM1](../genes/PBRM1.md)*-mutant tumors, and atezolizumab + bevacizumab beat sunitinib in TeffHigh tumors, especially TeffHighMyeloidHigh [PMID:29867230](../papers/29867230.md).

## Sources

- cBioPortal study record: `rcc_iatlas_immotion150_2018` (name, institution, size, reference_genome taken from `schema/ontology/studies.json`).
- [PMID:29867230](../papers/29867230.md)

*This page was processed by **crosslinker** on **2026-09-11**.*
