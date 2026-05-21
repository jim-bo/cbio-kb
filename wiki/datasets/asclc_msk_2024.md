---
name: "Atypical Small Cell Lung Carcinoma — MSK 2024"
studyId: asclc_msk_2024
institution: Memorial Sloan Kettering Cancer Center
size: 20
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - msk-impact-panel
  - whole-genome-seq
  - rna-seq
  - fish
  - immunohistochemistry
panels:
  - msk-impact-panel
tags:
  - small-cell-lung-carcinoma
  - chromothripsis
  - ecdna
  - never-smoker
  - rb1-tp53-proficient
  - atypical-sclc
processed_by: crosslinker
processed_at: 2026-05-21
---

# Atypical Small Cell Lung Carcinoma — MSK 2024

## Overview

A Memorial Sloan Kettering cohort of 20 patients with atypical small cell lung carcinoma (aSCLC) — a rare subset of [SCLC](../cancer_types/SCLC.md) lacking dual [RB1](../genes/RB1.md) and [TP53](../genes/TP53.md) inactivation and occurring exclusively in never/light smokers (≤10 pack-years). Identified as 3% of 600 consecutive de novo [SCLC](../cancer_types/SCLC.md) patients sequenced by [MSK-IMPACT](../methods/msk-impact-panel.md) at MSKCC. Raw WGS/RNA-seq data are available via dbGAP phs003676.v1.p1.

## Composition

- **Cancer types:** [SCLC](../cancer_types/SCLC.md) (primary); comparators include [LNET](../cancer_types/LNET.md) (n=157 pulmonary carcinoids) and [LUAD](../cancer_types/LUAD.md)-to-SCLC transformation.
- **Sample count:** 20 patients; 49 pathologic specimens (1–7 per patient).
- **Sequencing breakdown:** 31 specimens by [MSK-IMPACT](../methods/msk-impact-panel.md) targeted NGS (341/468/505-gene versions); 12 by WGS (11 patients, ~100× tumor / ~80× normal on NovaSeq 6000); 7 by RNA-seq.
- **Key clinical fields:** never/light smoker status (≤10 pack-years), Ki67 proliferation index, histotype ([SCLC](../cancer_types/SCLC.md) vs carcinoid), clinical outcomes ([OS](../cancer_types/OS.md), treatment response).
- **Copy-number analysis:** [FACETS](../methods/facets.md); chromothripsis detection by [ShatterSeek](../methods/shatterseek.md) and manual tNGS oscillating-CNA review; MSI by [MSIsensor](../methods/msisensor.md) and [MiMSI](../methods/mimsi.md); clonal timing by MutationTimeR.

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) (341/468/505-gene versions) — targeted panel NGS.
- [WGS](../methods/whole-genome-seq.md) — Illumina NovaSeq 6000, ~100× tumor / ~80× normal.
- [RNA-seq](../methods/rna-seq.md) — transcriptomic profiling.
- FISH — 3-color for [CCND1](../genes/CCND1.md), [CCND2](../genes/CCND2.md), [CDK4](../genes/CDK4.md), [MDM2](../genes/MDM2.md).
- IHC — pRb, p16, [OTP](../genes/OTP.md), [ASCL1](../genes/ASCL1.md), [YAP1](../genes/YAP1.md), cyclin D1, [DLL3](../genes/DLL3.md), [SEZ6](../genes/SEZ6.md), [MGMT](../genes/MGMT.md).

## Papers using this cohort

- [PMID:39185963](../papers/39185963.md) — Rekhtman et al. (2025) "Chromothripsis-Mediated Small Cell Lung Carcinoma," *Cancer Discovery*.

## Notable findings derived from this cohort

- aSCLC constitutes 3% (20/600) of de novo SCLC at MSKCC, occurring exclusively in never/light smokers (mean age 53 years vs 67 for conventional SCLC, P < 0.0001); median [OS](../cancer_types/OS.md) 58 months — intermediate between smoking-associated SCLC (16 months) and atypical carcinoids (184 months). [PMID:39185963](../papers/39185963.md)
- 84% (16/19) of non-MSI aSCLC harbor extensive chromothripsis on chromosomes 11, 12, and 1, producing ecDNA amplifications of [CCND1](../genes/CCND1.md) (30%), [CCND2](../genes/CCND2.md)/[CDK4](../genes/CDK4.md)/[MDM2](../genes/MDM2.md) (15%), and [MYCL](../genes/MYCL.md) (10%); average 565 structural variants per case (range up to >1,900). [PMID:39185963](../papers/39185963.md)
- tNGS-based chromothripsis detection from FACETS oscillating CNA patterns achieves 100% specificity and 77% sensitivity vs WGS gold standard (minimum 5 consecutive oscillating segments, CCF ≥50%). [PMID:39185963](../papers/39185963.md)
- Carcinoid-like mutation spectrum: [ATM](../genes/ATM.md) 30%, [ARID1A](../genes/ARID1A.md) 25%, [MEN1](../genes/MEN1.md) 15%, [EIF1AX](../genes/EIF1AX.md) 10%; [ATM](../genes/ATM.md) rate enriched vs carcinoids (8%, P = 0.008) and conventional SCLC (3%, P = 0.0003). [PMID:39185963](../papers/39185963.md)
- Reduced platinum sensitivity: among 15 evaluable patients, 13% CR and 20% PR — well below the ~70% historical response rate for conventional SCLC; 3/5 patients on immune checkpoint inhibitors remained on therapy 2 to >5 years. [PMID:39185963](../papers/39185963.md)

## Sources

- cBioPortal study: `asclc_msk_2024`
- dbGAP: phs003676.v1.p1 (raw WGS/RNA-seq)
- DOI: [10.1158/2159-8290.CD-24-0286](https://doi.org/10.1158/2159-8290.CD-24-0286)

*This page was processed by **crosslinker** on **2026-05-21**.*
