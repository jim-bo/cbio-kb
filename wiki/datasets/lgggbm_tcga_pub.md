---
name: Merged Cohort of LGG and GBM (TCGA, Cell 2016)
studyId: lgggbm_tcga_pub
institution: The Cancer Genome Atlas (TCGA)
size: 1122
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - bulk-rna-seq
  - dna-methylation-array
  - snp-array
  - rppa
panels: []
tags:
  - glioma
  - lower-grade-glioma
  - glioblastoma
  - pan-glioma
  - IDH-mutant
  - TCGA
  - methylation
  - TERT
  - ATRX
  - G-CIMP
processed_by: crosslinker
processed_at: 2026-05-14
---

# Merged Cohort of LGG and GBM (TCGA, Cell 2016)

## Overview

The TCGA pan-glioma merged dataset (lgggbm_tcga_pub) integrates the [lgg_tcga](../datasets/lgg_tcga.md) (516 lower-grade glioma samples, WHO grades II–III) and [gbm_tcga](../datasets/gbm_tcga.md) (606 [GBM](../cancer_types/GBM.md) samples, WHO grade IV) cohorts into a single 1,122-patient resource. The primary publication by Ceccarelli et al. 2016 uses this merged resource for integrated analysis of exome sequencing, RNA-seq, DNA copy number, DNA methylation (27K+450K), and RPPA data to define a molecular taxonomy of adult diffuse glioma that supersedes WHO histological classification. [PMID:26824661](../papers/26824661.md)

## Composition

- 1,122 newly diagnosed adult diffuse glioma patients: 516 LGG (grades II–III) + 606 GBM (grade IV).
- Histology: 590 GBM (56%), 174 oligodendroglioma (17%), 169 astrocytoma (16%), 114 oligoastrocytoma (11%).
- Clinical data available for 1,046/1,122 (93%) cases.
- Cancer types: [DIFG](../cancer_types/DIFG.md) (umbrella), [GBM](../cancer_types/GBM.md), [ASTR](../cancer_types/ASTR.md), [ODG](../cancer_types/ODG.md). [PMID:26824661](../papers/26824661.md)

## Assays / panels (linked)

- Gene expression: n=1,045.
- DNA copy number: n=1,084.
- DNA methylation: n=932 (HM27 for 287 GBM; HM450 for 516 LGG + 129 GBM).
- Exome sequencing: n=820 (513 LGG + 307 GBM); mutation calling by [MuTect](../methods/mutect.md), Indelocator, VarScan, RADIA (≥2-caller consensus); SMGs by [MutSig](../methods/mutsig.md) (MutSigCV).
- RPPA: n=473.
- WGS available for telomere-length and TERT-promoter analyses.
- Copy number by [GISTIC](../methods/gistic.md) (GISTIC2); fusions by [PRADA](../methods/prada.md) and [deFuse](../methods/defuse.md). [PMID:26824661](../papers/26824661.md)

## Papers using this cohort

- [PMID:26824661](../papers/26824661.md) — Ceccarelli et al. 2016, *Cell*: Primary integrative pan-glioma study defining 75 significantly mutated genes, six DNA-methylation subtypes (LGm1–6), PA-like IDH-wildtype glioma, and G-CIMP-low as a high-risk IDH-mutant subgroup.

## Notable findings derived from this cohort

- 75 significantly mutated genes (SMGs) identified across 1,122 gliomas, of which 45 had not been previously associated with glioma; mutation frequencies for novel SMGs ranged from 0.5% to 2.6%. [PMID:26824661](../papers/26824661.md)
- Pan-glioma DNA methylation clustering of 932 samples yields six clusters (LGm1–6): LGm1/2/3 are IDH-mutant (99%) and LGm4/5/6 are IDH-wildtype (99%), with RNA-seq yielding four expression clusters (LGr1–4). [PMID:26824661](../papers/26824661.md)
- G-CIMP-low: a newly defined IDH-mutant non-codel subgroup with reduced genome-wide methylation and poor survival (comparable to IDH-wildtype); 15/18 G-CIMP-low cases carry cell-cycle pathway abnormalities ([CDK4](../genes/CDK4.md), [CDKN2A](../genes/CDKN2A.md)). [PMID:26824661](../papers/26824661.md)
- PA-like IDH-wildtype LGG: a favorable-prognosis IDH-wildtype subtype with MAPK-pathway alterations ([BRAF](../genes/BRAF.md), [NF1](../genes/NF1.md), [NTRK1](../genes/NTRK1.md)/[NTRK2](../genes/NTRK2.md), [FGFR1](../genes/FGFR1.md)/[FGFR2](../genes/FGFR2.md)) in 52% of cases and low [TERT](../genes/TERT.md) expression (8%); younger patients (mean 37.6 vs 50.8 yr). [PMID:26824661](../papers/26824661.md)
- [ATRX](../genes/ATRX.md), not TERT promoter, drives telomere lengthening: ATRX-mutant gliomas have significantly longer telomeres (t-test p<0.0001) consistent with ALT mechanism. [PMID:26824661](../papers/26824661.md)
- Cohesin pathway ([NIPBL](../genes/NIPBL.md), [STAG2](../genes/STAG2.md)) disrupted in 16% of LGG/GBM — nominated as a therapeutic vulnerability for PARP inhibitors. [PMID:26824661](../papers/26824661.md)
- Methylation subtype is independently prognostic (C-index 0.836 with age + grade + epigenetic subtype; LRT p<0.0001); outperforms histology-based and TERT-based classifiers. [PMID:26824661](../papers/26824661.md)

## Sources

- cBioPortal study: `lgggbm_tcga_pub` — https://www.cbioportal.org/study/summary?id=lgggbm_tcga_pub
- Component cohorts: [lgg_tcga](../datasets/lgg_tcga.md) (516 LGG), [gbm_tcga](../datasets/gbm_tcga.md) (606 GBM).
- [PMID:26824661](../papers/26824661.md) — Ceccarelli et al. 2016, *Cell*, DOI 10.1016/j.cell.2015.12.028.

*This page was processed by **crosslinker** on **2026-05-14**.*
