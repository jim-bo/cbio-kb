---
name: TCGA Lower-Grade Glioma
studyId: lgg_tcga
institution: The Cancer Genome Atlas (TCGA)
size: 516
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [bulk-rna-seq, whole-exome-seq]
panels: []
tags:
  - glioma
  - lower-grade-glioma
  - IDH-mutant
  - 1p19q-codeletion
  - oligodendroglioma
  - astrocytoma
  - TCGA
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# TCGA Lower-Grade Glioma

## Overview

The TCGA Lower-Grade Glioma (LGG) cohort is a large, multi-institutional dataset assembled by The Cancer Genome Atlas program. It encompasses WHO grade II and grade III gliomas — a heterogeneous group that includes oligodendrogliomas, astrocytomas, and oligoastrocytomas. The cohort provides bulk genomic, transcriptomic, and clinical data across hundreds of samples, making it a widely used reference for validating findings derived from smaller or single-cell studies.

## Composition

- ~516 samples spanning WHO grade II–III gliomas (oligodendroglioma, astrocytoma, oligoastrocytoma); the oligodendroglioma subset (IDH-mutant, 1p/19q co-deleted) numbers approximately 69 samples used in validation analyses.
- Cancer types (OncoTree): [ODG](../cancer_types/ODG.md) and related lower-grade glioma subtypes.
- Key molecular features captured: IDH1/IDH2 mutation status, 1p/19q co-deletion status, TERT promoter mutation, MGMT methylation, CpG island methylator phenotype (G-CIMP), copy-number alterations (GISTIC), somatic point mutations (WES), and bulk RNA expression (RNA-seq).
- Reference genome: hg19.

## Assays / panels (linked)

- Bulk RNA-seq (gene expression profiles used for signature correlation analyses)
- Whole-exome sequencing (somatic mutation and copy-number calling)

## Papers using this cohort

- [PMID:27806376](../papers/27806376.md) — Tirosh et al. 2016, *Nature*: 69 bulk oligodendroglioma samples from TCGA LGG used as an external validation cohort for scRNA-seq-derived stem/progenitor and cell-cycle signatures.
- [PMID:28872634](../papers/28872634.md) — Bakas et al. 2017, *Scientific Data*: Expert-revised multi-parametric MRI segmentation labels and >700 radiomic features released for 108 TCGA-LGG cases (originating set n=199), enabling radiogenomic integration with lgg_tcga molecular data.

## Notable findings derived from this cohort

- The scRNA-seq-derived stem/progenitor gene signature (defined in 6 primary oligodendrogliomas) correlates positively with the cell-cycle signature across the 69 TCGA LGG oligodendroglioma bulk samples, supporting the single-cell developmental hierarchy model in a larger independent cohort [PMID:27806376](../papers/27806376.md).
- Bakas et al. 2017 released expert-revised MRI segmentation labels (whole tumour, tumour core, non-enhancing tumour) for 108 TCGA-LGG cases via the TCIA [tcia-tcga-lgg](../datasets/tcia-tcga-lgg.md) collection. LGG cases without apparent enhancing tumour were annotated as NET-only or NET+oedema, reflecting lower blood-brain-barrier disruption typical of low-grade glioma biology. These labels became the BraTS'17 reference standard and are paired with the molecular profiles in lgg_tcga for radiogenomic studies. [PMID:28872634](../papers/28872634.md)

## Sources

- cBioPortal study: `lgg_tcga` — https://www.cbioportal.org/study/summary?id=lgg_tcga
- TCGA LGG marker paper: Brat et al. 2015, *NEJM* (PMID 26061751).

*This page was processed by **entity-page-writer** on **2026-04-15**.*
