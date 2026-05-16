---
name: NCI Sherlock-Lung (Nature Genetics 2021)
studyId: lung_nci_2022
institution: National Cancer Institute (NCI)
size: 232
reference_genome: GRCh38
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
  - STRUCTURAL_VARIANT
panels: []
tags:
  - lung
  - LUAD
  - never-smoker
  - whole-genome-sequencing
  - WGS
  - LCINS
  - Sherlock-Lung
processed_by: crosslinker
processed_at: 2026-05-16
---

# NCI Sherlock-Lung (Nature Genetics 2021)

## Overview

The Sherlock-Lung study is the largest whole-genome sequencing (WGS) cohort of lung cancers in never smokers (LCINS) to date, comprising 232 treatment-naive patients with paired tumor and germline WGS (mean tumor coverage 85×; mean normal coverage 31.6×). Collected and analyzed by the National Cancer Institute; published in Nature Genetics 2021. Available on cBioPortal as `lung_nci_2022`; raw BAMs in dbGaP `phs001697.v1.p1`; RNA-seq FASTQs in GEO `GSE171415`. The study defined three genomic subtypes of LCINS based on somatic copy number alteration (SCNA) patterns. [PMID:34493867](../papers/34493867.md)

## Composition

- **232 LCINS patients** with paired tumor + germline WGS; of 256 enrolled, 20 failed QC and 4 were excluded by mutational-signature analysis.
- Histology: 189 adenocarcinomas ([LUAD](../cancer_types/LUAD.md)), 36 carcinoids ([LNET](../cancer_types/LNET.md)), 5 sarcomatoid/undifferentiated [NSCLC](../cancer_types/NSCLC.md), 2 squamous-cell carcinomas.
- Ancestry: 226 European (97.4%), 4 Asian (1.7%), 2 African (0.9%).
- Mean age 64.8 (range 21–86); 75.4% female. 27.6% had second-hand ("passive") tobacco smoke exposure; all 232 were never smokers.
- 35 adenocarcinomas additionally underwent RNA-seq.
- Tumor WGS coverage: 70.6–141.5×, mean 85×; normal 26.2–57.2×, mean 31.6×.
- Used [pcawg](../datasets/pcawg.md) [LUAD](../cancer_types/LUAD.md) (n=38) as a smoker comparator for mutational burden and signature analyses. [PMID:34493867](../papers/34493867.md)

## Assays / panels (linked)

- [whole-genome-seq](../methods/whole-genome-seq.md) — high-coverage paired tumor/normal WGS; SNVs, indels, SCNAs, SVs, mutational signatures, WGD, kataegis, telomere length, HRDetect.
- [rna-seq](../methods/rna-seq.md) — gene expression in 35 adenocarcinomas.
- SigProfiler / COSMIC v3 — mutational signature decomposition (14 SBS signatures recovered).
- IntOGen — driver gene discovery under positive selection.
- TelSeq + TelomereHunter — telomere length estimation.
- HRDetect — homologous recombination deficiency scoring.

## Papers using this cohort

- [PMID:34493867](../papers/34493867.md) — Sherlock-Lung WGS study defining three SCNA-based subtypes of LCINS (*piano*, *mezzo-forte*, *forte*); absence of tobacco signature (SBS4) in all 232 tumors including 62 passive smokers; five independent genomic alterations each doubling mortality risk; [UBA1](../genes/UBA1.md) identified as a novel LCINS driver gene. [PMID:34493867](../papers/34493867.md)

## Notable findings derived from this cohort

- Median TMB = 1.1 Mut/Mb, >7-fold lower than LUAD in smokers (p=7.0e-73). [PMID:34493867](../papers/34493867.md)
- Three SCNA-based subtypes: *piano* (49.6%, low SCNA burden, carcinoid-enriched, stem-cell-like, long telomeres), *mezzo-forte* (30.2%, arm-level amplifications, 51.4% EGFR-mutant), *forte* (20.2%, dominated by whole-genome doubling in 95.7% of tumors). [PMID:34493867](../papers/34493867.md)
- Tobacco smoking signature (SBS4) absent in all 232 tumors, including 62 patients with passive smoke exposure; SBS4 detection threshold = 15% of somatic mutations. [PMID:34493867](../papers/34493867.md)
- RTK-RAS pathway drivers: [EGFR](../genes/EGFR.md) 30.6%, [KRAS](../genes/KRAS.md) 7.3%, [ALK](../genes/ALK.md) 6.0%, [MET](../genes/MET.md) 4.3%, [ERBB2](../genes/ERBB2.md) 3.9%, [ROS1](../genes/ROS1.md) 2.6%, [RET](../genes/RET.md) 1.3%; strong mutual exclusivity among RTK-RAS drivers. [PMID:34493867](../papers/34493867.md)
- [UBA1](../genes/UBA1.md) (E1 ubiquitin enzyme) identified as a likely novel LCINS driver; 6/9 mutated tumors in the piano subtype. [PMID:34493867](../papers/34493867.md)
- Five independent alterations each ~doubled mortality risk (Cox PH HR ~1.9 per alteration, p=3.7e-7): [TP53](../genes/TP53.md) mutation/MDM2 amplification (combined HR 2.9), [EGFR](../genes/EGFR.md) mutation, [CHEK2](../genes/CHEK2.md) LOH, 22q loss, 15q loss. [PMID:34493867](../papers/34493867.md)
- APOBEC signatures (SBS2/SBS13) present in ≥100 SNVs in ~58% of samples; enriched in TP53-deficient and RTK-RAS-positive tumors. [PMID:34493867](../papers/34493867.md)
- LCINS LUAD telomeres significantly longer than LUAD-smoker telomeres (6.4 kb, 95% CI 5.3–7.6, p=7.1e-11); passive smokers had shorter telomeres than never-smokers despite absent SBS4 (p=0.005). [PMID:34493867](../papers/34493867.md)
- Evolutionary timing: driver mutations in TP53, [RBM10](../genes/RBM10.md), [KRAS](../genes/KRAS.md), or EGFR generally precede WGD and most SCNAs; piano MRCAs estimated ~9 yr before clinical diagnosis, suggesting a long early-detection window. [PMID:34493867](../papers/34493867.md)

## Sources

- cBioPortal study: `lung_nci_2022` (canonical, verified).
- Raw WGS BAMs: dbGaP `phs001697.v1.p1`.
- RNA-seq FASTQs: GEO `GSE171415`.
- Primary publication: [PMID:34493867](../papers/34493867.md).

*This page was processed by **crosslinker** on **2026-05-16**.*
