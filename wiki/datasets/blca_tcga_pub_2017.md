---
name: TCGA Bladder Urothelial Carcinoma (2017, 412-tumor)
studyId: blca_tcga_pub_2017
institution: The Cancer Genome Atlas Research Network
size: 412
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - rna-seq
  - mirna-seq
  - hm450-methylation-array
  - affymetrix-snp6
  - rppa
panels: []
tags:
  - tcga
  - urothelial-carcinoma
  - muscle-invasive-bladder-cancer
  - apobec-mutagenesis
  - molecular-subtypes
  - chromatin-remodeling
  - multi-platform
processed_by: crosslinker
processed_at: 2026-05-15
---

# TCGA Bladder Urothelial Carcinoma (2017, 412-tumor)

## Overview

Robertson et al. (TCGA bladder analysis working group) report the comprehensive molecular characterization of the full TCGA cohort of 412 chemotherapy-naive muscle-invasive bladder cancers ([BLCA](../cancer_types/BLCA.md)). This dataset supersedes the earlier 131-tumor [blca_tcga_pub](../datasets/blca_tcga_pub.md) (2014) cohort and integrates whole-exome, SNP6 copy-number, RNA-seq, miRNA-seq, DNA methylation, and RPPA profiling. The study identifies 58 significantly mutated genes (34 novel vs the 131-tumor cohort), defines five mRNA expression subtypes including a newly recognized neuronal subtype, and confirms APOBEC3A/3B-driven mutagenesis as the dominant mutational source. Published in *Cell* (2017).

## Composition

- **412 chemotherapy-naive, invasive, high-grade urothelial tumors** (T1–T4a, N0–3, M0–1) from 36 tissue source sites; 4 expert genitourinary pathologists re-reviewed all cases.
- **Histology:** 52 (13%) had urothelial carcinoma with variant histology — 42 squamous, 4 small cell/neuroendocrine, 2 micropapillary, 4 plasmacytoid.
- Complete clinical data for 406; 35 patients had received prior intravesical BCG; at last follow-up 230 alive, 163 recurred, 182 died (≥122/67% cancer-related); median follow-up 20.9 months for the alive.
- Cancer type: Bladder Urothelial Carcinoma ([BLCA](../cancer_types/BLCA.md)).

## Assays / panels (linked)

- [whole-exome sequencing](../methods/whole-exome-seq.md) — Illumina HiSeq with Agilent SureSelect Human All Exon 50 Mb (n=412 tumor/normal pairs, mean coverage 85X)
- [whole-genome sequencing](../methods/whole-genome-seq.md) — n=136 tumors
- [Affymetrix SNP6.0](../methods/affymetrix-snp6.md) — copy-number arrays; [GISTIC 2.0](../methods/gistic.md) and [ABSOLUTE](../methods/absolute.md) analysis
- [HM450 methylation arrays](../methods/hm450-methylation-array.md)
- [RNA-seq](../methods/rna-seq.md) — n=408
- [miRNA-seq](../methods/mirna-seq.md)
- [RPPA](../methods/rppa.md) — n=343 with 208 antibodies
- [MuTect](../methods/mutect.md) — SNV calling (128,772 SNVs + 2,888 indels identified)
- [MutSig 2CV](../methods/mutsig.md) — significantly mutated gene analysis
- [Bayesian NMF](../methods/bayesian-nmf.md) — mutational signature discovery
- [COCA](../methods/coca.md) — integrative clustering

## Papers using this cohort

- [PMID:28988769](../papers/28988769.md) — Robertson et al., *Cell* (2017): Comprehensive Molecular Characterization of Muscle-Invasive Bladder Cancer.

## Notable findings derived from this cohort

- **58 significantly mutated genes** by MutSig 2CV (q < 0.1); 34 novel vs the 131-tumor cohort; 7 new SMGs mutated in >10% of samples: [KMT2C](../genes/KMT2C.md) (18%), [ATM](../genes/ATM.md) (14%), [FAT1](../genes/FAT1.md) (12%), [CREBBP](../genes/CREBBP.md) (12%), [ERBB2](../genes/ERBB2.md) (12%), [SPTAN1](../genes/SPTAN1.md) (12%), [KMT2A](../genes/KMT2A.md) (11%). [PMID:28988769](../papers/28988769.md)
- **APOBEC mutagenesis dominates** — APOBEC-a and APOBEC-b signatures account for 67% of all SNVs; 64% of APOBEC mutations are clonal, implying early activity in bladder cancer development. [PMID:28988769](../papers/28988769.md)
- **APOBEC-high (MSig1) tumors have the best survival** (75% 5-year [OS](../cancer_types/OS.md)); low-mutation-burden MSig2 tumors have worst (22% 5-year OS). [PMID:28988769](../papers/28988769.md)
- **Five mRNA expression subtypes** (NMF consensus clustering, n=408): luminal-papillary (35%), luminal-infiltrated (19%), luminal (6%), basal-squamous (35%), neuronal (5%); survival association p = 4×10⁻⁴. [PMID:28988769](../papers/28988769.md)
- **Neuronal subtype** (n=20) is newly recognized, includes tumors without neuroendocrine histology (17/20), enriched for [TP53](../genes/TP53.md)+[RB1](../genes/RB1.md) co-mutation or [E2F3](../genes/E2F3.md) amplification (85%), and has the poorest survival of all five subtypes. [PMID:28988769](../papers/28988769.md)
- **Luminal-papillary subtype** enriched for [FGFR3](../genes/FGFR3.md) mutations (42/57; p < 10⁻⁹), amplification, and [FGFR3](../genes/FGFR3.md)–[TACC3](../genes/TACC3.md) fusions (8/10); best candidate for pan-FGFR inhibitors. [PMID:28988769](../papers/28988769.md)
- **Luminal-infiltrated subtype** has highest [CD274](../genes/CD274.md) (PD-L1) and [PDCD1](../genes/PDCD1.md) (PD-1) expression; proposed checkpoint-immunotherapy-responsive subset. [PMID:28988769](../papers/28988769.md)
- **p53/cell-cycle pathway inactivated in 89%** of tumors; chromatin-modifier mutations pervasive and predominantly inactivating in 10 of 39 SMGs. [PMID:28988769](../papers/28988769.md)
- [FGFR3](../genes/FGFR3.md)–[TACC3](../genes/TACC3.md) fusion is the most common recurrent gene fusion (n=10) and is enriched in the luminal-papillary subtype. [PMID:28988769](../papers/28988769.md)
- Neoantigen load predicts survival independently of age, AJCC stage, and squamous differentiation (p = 8×10⁻⁴). [PMID:28988769](../papers/28988769.md)
- [PPARG](../genes/PPARG.md) recurrently fused (6 fusions; 4 *TSEN2-PPARG*, 2 *MKRN2-PPARG*), implicated as a luminal driver alongside [GATA3](../genes/GATA3.md) and [FOXA1](../genes/FOXA1.md). [PMID:28988769](../papers/28988769.md)
- RPPA proteomic clusters 1 and 2 (HER2-high) are candidates for [trastuzumab](../drugs/trastuzumab.md) or [ado-trastuzumab-emtansine](../drugs/ado-trastuzumab-emtansine.md); cluster 3 (EGFR-high proliferative) for [EGFR](../genes/EGFR.md) inhibitors. [PMID:28988769](../papers/28988769.md)

## Sources

- cBioPortal study ID: blca_tcga_pub_2017
- Supersedes [blca_tcga_pub](../datasets/blca_tcga_pub.md) (131-tumor 2014 TCGA [BLCA](../cancer_types/BLCA.md) cohort)
- TCGA data portal / GDC

*This page was processed by **crosslinker** on **2026-05-15**.*
