---
name: Uterine Corpus Endometrial Carcinoma (CPTAC, 2020)
studyId: ucec_cptac_2020
institution: Clinical Proteomic Tumor Analysis Consortium (CPTAC) / Pacific Northwest National Laboratory (PNNL)
size: 95
reference_genome: hg38
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - rna-seq
  - mirna-seq
  - epic-methylation-array
  - tmt-proteomics
  - tmt-phosphoproteomics
panels: []
tags:
  - ucec
  - endometrial
  - uterine
  - cptac
  - proteogenomics
  - multi-omic
  - msi
  - pole
  - cnv-high
  - cnv-low
processed_by: crosslinker
processed_at: 2026-05-16
---

# Uterine Corpus Endometrial Carcinoma (CPTAC, 2020)

## Overview

The CPTAC endometrial carcinoma proteogenomic dataset (Dou et al., *Cell* 2020, [PMID:32059776](../papers/32059776.md)) is a prospectively collected cohort of 95 endometrial carcinoma (EC) tumors and 49 normal tissue samples comprehensively characterized by whole-exome sequencing, whole-genome sequencing, total and miRNA RNA-seq, DNA methylation (EPIC array), global TMT-based proteomics, phosphoproteomics, and acetylproteomics. The dataset integrates across the four TCGA-defined genomic subtypes ([POLE](../genes/POLE.md), MSI, CNV-low, CNV-high) to reveal mutation-type-specific proteomic effects, Wnt–histone-acetylation coupling, and antigen presentation machinery deficiency as a determinant of immunotherapy response independent of TMB. Data are publicly available via the Genomic Data Commons (GDC), CPTAC Data Portal, the `cptac` Python package, and LinkedOmics.

## Composition

- **95 prospectively collected endometrial carcinoma tumors** and 49 adjacent-normal tissue samples. Biospecimens collected April 2016–May 2017.
- Histology: 83 endometrioid, 12 serous.
- Genomic subtype: 7 [POLE](../genes/POLE.md), 25 MSI, 43 CNV-low (endometrioid-like), 20 CNV-high (serous-like).
- Cancer types: [UCEC](../cancer_types/UCEC.md) overall; [UEC](../cancer_types/UEC.md) endometrioid; [USC](../cancer_types/USC.md) serous histotypes.
- CNV-high subtype contains all 12 serous + the most aggressive endometrioid tumors.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — Illumina HiSeq4000, paired 76-cycle, min 150× on-target.
- [whole-genome-seq](../methods/whole-genome-seq.md) — PCR-free HiSeqX, min 15× coverage, 151 bp paired-end.
- [rna-seq](../methods/rna-seq.md) — total and miRNA RNA-seq; [mirna-seq](../methods/mirna-seq.md).
- [epic-methylation-array](../methods/epic-methylation-array.md) — Illumina Infinium MethylationEPIC, >850,000 CpG sites.
- [tmt-proteomics](../methods/tmt-proteomics.md) — isobaric 10-plex TMT-based global proteomics at PNNL; 1% protein-level FDR.
- [tmt-phosphoproteomics](../methods/tmt-phosphoproteomics.md) — IMAC enrichment phosphoproteomics.
- Acetylproteomics — PTMScan Acetyl-Lysine Motif IAP genome-wide acetylation profiling.

## Papers using this cohort

- [PMID:32059776](../papers/32059776.md) — Dou et al. 2020, *Cell*: CPTAC proteogenomic characterization of 95 ECs; identifies mutation-type-specific proteomic effects of [TP53](../genes/TP53.md) and [CTNNB1](../genes/CTNNB1.md), Wnt–acetylation coupling, circRNA/EMT axis, and APM deficiency as an ICI-response biomarker.

## Notable findings derived from this cohort

- [POLE](../genes/POLE.md)-subtype tumors (n=7, P286R hotspot in 5/7) account for ~61% of all somatic mutations; MSI tumors carry 88% of all indels [PMID:32059776](../papers/32059776.md).
- Novel MSI SMGs not previously reported in TCGA EC: [INPPL1](../genes/INPPL1.md) (56%, FDR=0), [KMT2B](../genes/KMT2B.md) (56%, FDR=0.001), [JAK1](../genes/JAK1.md) (44%, FDR=6.4e-07); higher mutation rates confirmed for [PTEN](../genes/PTEN.md) (92%), [ARID1A](../genes/ARID1A.md) (76%), [RPL22](../genes/RPL22.md) (64%) [PMID:32059776](../papers/32059776.md).
- [TP53](../genes/TP53.md) missense DNA-binding-domain hotspots (R248, R273) elevate p53 protein and dysregulate [AURKA](../genes/AURKA.md); truncating TP53 mutations increase PLK1-T210 phosphorylation and mitotic markers — mutation-type-specific effects not observed in CPTAC ovarian or colon cancer [PMID:32059776](../papers/32059776.md).
- [CTNNB1](../genes/CTNNB1.md) exon 3 hotspot mutations (n=23) increase Wnt-pathway activity and drive H2B N-terminal acetylation (K16/K20/K24) through [BRD3](../genes/BRD3.md)/[SIRT1](../genes/SIRT1.md) coupling [PMID:32059776](../papers/32059776.md).
- TMB and antigen processing/presentation machinery (APM) efficiency vary independently; TMB-H/APM-L tumors (enriched for [JAK1](../genes/JAK1.md)/[STAT1](../genes/STAT1.md) frameshifts and reduced [TAP1](../genes/TAP1.md)/[TAP2](../genes/TAP2.md)/HLA class I) have lower CD8+ T-cell infiltration — APM status should complement TMB for ICI patient selection [PMID:32059776](../papers/32059776.md).
- 78% of EC tumors harbor either a neoantigen or a high-expression cancer/testis antigen, supporting proteogenomics as a vaccine target-discovery approach [PMID:32059776](../papers/32059776.md).

## Sources

- cBioPortal study: `ucec_cptac_2020`
- Dou et al. *Cell* 180, 729–748.e26 (2020). [PMID:32059776](../papers/32059776.md)
- CPTAC Data Portal: https://proteomics.cancer.gov/programs/cptac
- Genomic Data Commons (GDC): https://portal.gdc.cancer.gov
- LinkedOmics: http://www.linkedomics.org

*This page was processed by **crosslinker** on **2026-05-16**.*
