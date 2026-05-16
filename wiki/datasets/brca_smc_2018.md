---
name: Samsung Medical Center Breast Cancer WES Cohort (2018)
studyId: brca_smc_2018
institution: Samsung Medical Center, Seoul, Korea
size: 187
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
  - MRNA_EXPRESSION
panels: []
tags:
  - breast-cancer
  - brca
  - whole-exome-seq
  - rna-seq
  - korean
  - asian
  - young-breast-cancer
  - ega
  - geo
processed_by: crosslinker
processed_at: 2026-05-16
---

# Samsung Medical Center Breast Cancer WES Cohort (2018)

## Overview

Whole-exome sequencing and RNA-seq cohort of 187 primary breast tumors from patients diagnosed at Samsung Medical Center (SMC), Seoul, Korea. The cohort is enriched for younger, pre-menopausal Asian patients (88.2% pre-menopausal; 66.8% aged ≤40 years). It was designed for systematic comparison with the predominantly Caucasian, post-menopausal TCGA [BRCA](../cancer_types/BRCA.md) cohort ([brca_tcga_pub2015](../datasets/brca_tcga_pub2015.md)) to characterize molecular differences in Asian and young breast cancers. WES data deposited at EGA accession EGAS00001002621; RNA-seq data at GEO GSE113184.

## Composition

- **n = 187** primary breast tumors; WES on 186 tumor/normal pairs, RNA-seq on 168 tumors + 10 adjacent normals.
- 95% (179/187) treatment-naive; all tumors ≥60% tumor cells; 100% Asian.
- 88.2% pre-menopausal (n=165); 10.2% post-menopausal; mean age 39.3 ± 8.5 years.
- Age subgroups: YBC (young breast cancer, ≤40 years, n=125) and IBC (>40 years, n=62).
- Histology: 92.0% invasive ductal carcinoma ([IDC](../cancer_types/IDC.md)); 3.7% invasive lobular carcinoma ([ILC](../cancer_types/ILC.md)).
- Clinical subtype distribution: ER+ 55.1%, ER+/HER2+ 14.4%, HER2+ 8.0%, TNBC 19.8%.

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md): Agilent SureSelect XT Human All Exon V5 capture; Illumina HiSeq 2500 PE100.
- [RNA-seq](../methods/rna-seq.md): RSEM gene expression on hg19; 168 tumors + 10 adjacent normals.
- Somatic mutation calling: VarScan 2.4.1; significantly mutated genes by [MutSigCV v1.2](../methods/mutsig.md).
- Mutational signatures via deconstructSigs over 30 COSMIC signatures; pathway analysis via [GSEA](../methods/gsea.md)/GSVA; virtual microdissection by NMF.

## Papers using this cohort

- [PMID:29713003](../papers/29713003.md) — Kan et al. 2018, Nature Communications — "Multi-omics profiling of younger Asian breast cancers reveals distinct molecular subtypes and age-associated differences."

## Notable findings derived from this cohort

- Six significantly mutated genes (MutSigCV FDR<0.1): [TP53](../genes/TP53.md) (47.9%), [PIK3CA](../genes/PIK3CA.md) (28.5%), [GATA3](../genes/GATA3.md) (12.4%), [CBFB](../genes/CBFB.md) (2.7%), [PTEN](../genes/PTEN.md) (3.2%), [CDH1](../genes/CDH1.md) (2.2%) [PMID:29713003](../papers/29713003.md).
- Compared to TCGA BRCA: higher proportions of HER2+ and Luminal B subtypes; significantly higher [TP53](../genes/TP53.md) mutation rate (47.9% vs 32.0%, p=5.0e-5) and [ERBB2](../genes/ERBB2.md) somatic alteration rate (20% vs 9.1%) [PMID:29713003](../papers/29713003.md).
- Germline BRCA1/BRCA2 pathogenic mutations in 10.8% of SMC patients vs 4.7% in TCGA (p=0.0027); enriched in younger patients (YBC 13.7% vs IBC 4.8%) [PMID:29713003](../papers/29713003.md).
- HRD mutational signature S3 dominated TNBC: 85% of SMC TNBC were HRD-positive (S3 score >0.2) vs 52% of TCGA TNBC (Fisher's exact p=7e-4) [PMID:29713003](../papers/29713003.md).
- TIL factor (NMF F9) significantly higher in SMC vs TCGA (p=1.55e-06); [CD274](../genes/CD274.md) (PD-L1) and [CD8A](../genes/CD8A.md) over-expressed; TGF-β hallmark signature lower in SMC — independent of age, subtype, and histology [PMID:29713003](../papers/29713003.md).

## Sources

- Kan Z et al. "Multi-omics profiling of younger Asian breast cancers reveals distinct molecular subtypes and age-associated differences." Nature Communications. 2018;9(1):1725. [PMID:29713003](../papers/29713003.md). DOI: 10.1038/s41467-018-04129-4.
- EGA accession: EGAS00001002621 (WES + RNA-seq).
- GEO accession: GSE113184 (RNA-seq).

*This page was processed by **crosslinker** on **2026-05-16**.*
