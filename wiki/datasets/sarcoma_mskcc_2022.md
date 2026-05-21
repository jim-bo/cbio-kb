---
name: Sarcoma (MSK, Nat Commun. 2022)
studyId: sarcoma_mskcc_2022
institution: Memorial Sloan Kettering Cancer Center
size: 2138
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MSK-IMPACT (IMPACT341, IMPACT410, IMPACT468)
panels:
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - sarcoma
  - soft tissue
  - bone
  - paired tumor-normal
  - MSK-IMPACT
processed_by: crosslinker
processed_at: 2026-05-21
---

# Sarcoma (MSK, Nat Commun. 2022)

## Overview

Targeted sequencing of 2,138 bone and soft tissue sarcoma samples from distinct patients, each with paired normal DNA, profiled by MSK-IMPACT at Memorial Sloan Kettering Cancer Center. Three MSK-IMPACT panel versions were used: 341 genes (n=209, 9.8%), [IMPACT410](../methods/IMPACT410.md) (n=573, 26.8%), and [IMPACT468](../methods/IMPACT468.md) (n=1,356, 63.4%), with ≥500x median coverage on Illumina HiSeq 2500. Note: this dataset (MSK-IMPACT, paired tumor-normal) is distinct from `sarcoma_msk_2022` (FoundationOne Heme, tumor-only, N=7,494). The companion interactive dataset is available on cBioPortal as `sarcoma_mskcc_2022`.

## Composition

- 2,138 samples representing 45 distinct OncoTree-mapped pathological entities
- Median patient age 54 (range <1 to >90); 1,098 (51.4%) female
- 790 (36.9%) metastatic site biopsies; remainder primary
- 22 subtypes with n≥20 formed the core analysis set
- Most common subtypes: [GIST](../cancer_types/GIST.md) (n=395), [DDLS](../cancer_types/DDLS.md) (n=167), [ULMS](../cancer_types/ULMS.md) (n=165), [UPS](../cancer_types/UPS.md) (n=145), [OS](../cancer_types/OS.md) (n=129), [LMS](../cancer_types/LMS.md) (n=125), [ANGS](../cancer_types/ANGS.md) (n=101), [ES](../cancer_types/ES.md) (n=99)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md): [IMPACT410](../methods/IMPACT410.md) and [IMPACT468](../methods/IMPACT468.md) panels; paired tumor-normal
- [FACETS](../methods/facets.md) for allele-specific copy number and whole-genome doubling calls
- [MuSiC](../methods/genome-music.md) and [MutSigCV 1.4](../methods/mutsigcv.md) for recurrent-mutation discovery (q<0.1)
- [MSIsensor](../methods/msisensor.md) (≥10 threshold for MSI-high)
- COSMIC v3 mutational signature extraction

## Papers using this cohort

- [PMID:35705560](../papers/35705560.md) — Nacev et al., Nat Commun 2022. Primary study: MSK-IMPACT comparative genetic analysis of 2,138 sarcomas across 45 entities.

## Notable findings derived from this cohort

- Across 45 pathological entities: TMB highest in [ANGS](../cancer_types/ANGS.md) (3.0 mut/Mb), [UPS](../cancer_types/UPS.md), [ULMS](../cancer_types/ULMS.md); MSI-H in only 5/1,893 samples; WGD in ~50% of OS/UPS/ERMS/MPNST and associated with worse [OS](../cancer_types/OS.md) in metastatic disease (p=0.042); [TERT](../genes/TERT.md) amplifications in 44% of intimal sarcoma; SWI/SNF alterations in 43% of uterine adenosarcoma; 17 unsupervised genomic clusters crossing histology boundaries; [ATRX](../genes/ATRX.md) loss clusters across ULMS/PLLS/UPS/MFS/OS/ANGS/PECOMA/LMS [PMID:35705560](../papers/35705560.md)

## Sources

- cBioPortal study: `sarcoma_mskcc_2022`
- Citation: Nacev et al. Nat Commun. 2022 [PMID:35705560](../papers/35705560.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
