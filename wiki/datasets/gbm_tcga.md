---
name: TCGA Glioblastoma Multiforme
studyId: gbm_tcga
institution: The Cancer Genome Atlas (TCGA)
size: 592
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - bulk-rna-seq
panels: []
tags:
  - glioblastoma
  - gbm
  - glioma
  - TCGA
  - wes
  - rna-seq
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# TCGA Glioblastoma Multiforme

## Overview

The TCGA [GBM](../cancer_types/GBM.md) study is the canonical genomic and transcriptomic dataset for glioblastoma multiforme, assembled by The Cancer Genome Atlas Research Network. It comprises multi-platform molecular profiling of glioblastoma tumours and is hosted on cBioPortal as `gbm_tcga`. The companion TCIA imaging collection ([tcia-tcga-gbm](../datasets/tcia-tcga-gbm.md)) provides matched multi-parametric MRI scans with expert-revised tumour segmentation labels and extracted radiomic features published by Bakas et al. 2017. [PMID:28872634](../papers/28872634.md)

## Composition

- **Cancer type**: glioblastoma multiforme ([GB](../cancer_types/GB.md)), n=592.
- **Assays**: whole-exome sequencing, bulk RNA-seq, copy-number arrays, methylation arrays, and reverse-phase protein arrays.
- **Sample Selection**: Original interim analysis (n=206) required a minimum of 80% tumor nuclei and maximum 50% necrosis. 143 cases had matched normal peripheral blood DNA. [PMID:18772890](../papers/18772890.md)
- **Molecular counterpart**: paired with TCIA-hosted multi-parametric MRI scans (T1, T1-Gd, T2, T2-FLAIR) in [tcia-tcga-gbm](../datasets/tcia-tcga-gbm.md) (135 scans from 8 institutions).

## Assays / panels (linked)

- Whole-exome sequencing; bulk RNA-seq; copy-number arrays.

## Papers using this cohort

- [PMID:28872634](../papers/28872634.md) — Bakas et al. 2017, *Scientific Data*: Expert-revised MRI segmentation labels and >700 radiomic features released for 135 TCGA-GBM cases, complementing the genomic data in gbm_tcga to enable radiogenomic studies.
- [PMID:26824661](../papers/26824661.md) — Ceccarelli et al. 2016, *Cell*: TCGA pan-glioma integrated analysis using 606 GBM samples from this cohort combined with 516 LGG samples into lgggbm_tcga_pub.
- [PMID:30742119](../papers/30742119.md) — Zhao et al. 2019, *Nature Medicine*: PTEN mutations and MAPK alterations predict anti-PD-1 response in recurrent GBM; TCGA IDH1-wildtype GBM used as background reference cohort.

## Notable findings derived from this cohort

- Identified three core signaling pathways altered in nearly all GBMs: RTK/RAS/PI3K (88%), p53 (78%), and RB (88%). [PMID:18772890](../papers/18772890.md)
- Characterized the spectrum of somatic mutations, identifying significantly mutated genes including *[TP53](../genes/TP53.md)*, *[PTEN](../genes/PTEN.md)*, *[NF1](../genes/NF1.md)*, *[EGFR](../genes/EGFR.md)*, *[ERBB2](../genes/ERBB2.md)*, *[RB1](../genes/RB1.md)*, *[PIK3R1](../genes/PIK3R1.md)*, and *[PIK3CA](../genes/PIK3CA.md)*. [PMID:18772890](../papers/18772890.md)
- Discovered frequent activating mutations in *[PIK3R1](../genes/PIK3R1.md)* (p85α regulatory subunit of PI3K) that disrupt interaction with p110α. [PMID:18772890](../papers/18772890.md)
- Established that *[MGMT](../genes/MGMT.md)* promoter methylation, when combined with mismatch repair (MMR) gene mutations (e.g., *[MSH6](../genes/MSH6.md)*), is associated with a hypermutator phenotype in GBMs treated with alkylating agents. [PMID:18772890](../papers/18772890.md)
- Bakas et al. 2017 released expert-revised segmentation labels for 135 GBM cases (from the originating set of 262), achieving median DICE of 0.92 for whole tumour, 0.88 for tumour core, and 0.88 for enhancing tumour versus GLISTRboost automated labels. These labels became the reference for BraTS'17. [PMID:28872634](../papers/28872634.md)
- A panel of >700 radiomic features was extracted volumetrically from the manually revised labels, spanning intensity, volumetric, morphologic, texture (GLCM/GLRLM/GLSZM/NGTDM), wavelet, and glioma growth-model parameters — enabling downstream radiogenomic correlation with TCGA molecular profiles. [PMID:28872634](../papers/28872634.md)
- Used as a component cohort (606 GBM samples, grade IV, n=592 per cBioPortal) in the TCGA pan-glioma integrated analysis identifying 75 SMGs, six DNA-methylation subtypes (LGm1–6), and PA-like IDH-wildtype glioma as a distinct favorable-prognosis entity [PMID:26824661](../papers/26824661.md)
- Used as an IDH1-wildtype background reference (n=458 and n=503 samples) for mutation-frequency comparisons in the Columbia GBM immunotherapy cohort; PTEN mutation frequency in TCGA (33%, 154/458) contextualized PTEN enrichment among anti-PD-1 non-responders, and TCGA tumor purity estimates (ESTIMATE) supplemented the Columbia cohort transcriptomic analyses. [PMID:30742119](../papers/30742119.md)
- Included as a reference comparison cohort (re-processed TCGA-GBM samples) within the GLASS Consortium longitudinal glioma study alongside data from 33 other contributing centers. [PMID:31748746](../papers/31748746.md)
- Used as the driver-alteration frequency benchmark for the Mayo GBM PDX panel; frequencies of TERT, EGFR, PTEN, TP53, CDKN2A, BRAF, and IDH1 alterations in the PDX panel were compared against TCGA-GBM. [PMID:31852831](../papers/31852831.md)

## Sources

- cBioPortal study: `gbm_tcga` — https://www.cbioportal.org/study/summary?id=gbm_tcga
- TCGA GBM marker paper: Cancer Genome Atlas Research Network 2008, *Nature* (PMID 18772890).
- [PMID:28872634](../papers/28872634.md) — Bakas et al. 2017, *Scientific Data*, DOI 10.1038/sdata.2017.117.
- [PMID:26824661](../papers/26824661.md) — Ceccarelli et al. 2016, *Cell*, DOI 10.1016/j.cell.2015.12.028.
- [PMID:30742119](../papers/30742119.md)

*This page was processed by **entity-page-writer** on **2026-05-16**.*
