---
name: MSK Non-Muscle-Invasive Bladder Cancer Cohort (MSK, JCO 2017)
studyId: blca_nmibc_2017
institution: Memorial Sloan Kettering Cancer Center
size: 105
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - targeted-panel-seq
panels:
  - IMPACT341
  - IMPACT410
tags:
  - bladder-cancer
  - nmibc
  - urothelial-carcinoma
  - bcg-therapy
  - msk-impact
  - tert-promoter
  - chromatin-remodeling
  - ddr
  - prospective
processed_by: crosslinker
processed_at: 2026-05-15
---

# MSK Non-Muscle-Invasive Bladder Cancer Cohort (MSK, JCO 2017)

## Overview

The blca_nmibc_2017 dataset is the largest NGS-focused cohort of non-muscle-invasive bladder cancer (NMIBC) published to date, assembled at Memorial Sloan Kettering Cancer Center. Pietzak et al. profiled pretreatment index tumors and matched germline DNA from 105 NMIBC patients using the MSK-IMPACT 341- or 410-gene targeted panels under an IRB-approved protocol. The cohort spans all NMIBC stages (LGTa, HGTis, HGTa, HGT1) and includes a 62-patient sub-cohort treated with induction BCG for whom genomic correlates of recurrence were evaluated. Comparator data from 40 MSK muscle-invasive bladder cancers (MIBC) sequenced on the same platform and 98 TCGA MIBC specimens were used to contextualize findings across stage. Data are publicly available through the cBioPortal for Cancer Genomics as study blca_nmibc_2017.

## Composition

- **105 patients** with NMIBC; all treatment-naive index tumors with matched germline DNA.
- **Stages:** Low-grade Ta (LGTa, n=23), high-grade Tis (HGTis, n=12), high-grade Ta (HGTa, n=32), high-grade T1 (HGT1, n=38).
- **BCG sub-cohort:** 62 of 82 high-grade NMIBC patients who received 6-week induction BCG without maintenance therapy.
- **Sequencing:** [IMPACT341](../methods/IMPACT341.md) or [IMPACT410](../methods/IMPACT410.md) targeted panels; matched germline normal DNA from peripheral blood.
- **Comparators:** 40 MSK-MIBC tumors on same protocol + 98 TCGA MIBC specimens ([blca_tcga_pub](../datasets/blca_tcga_pub.md)).
- **Median follow-up:** 24.4 months; 46/100 patients experienced recurrence.
- **Cancer type:** [BLCA](../cancer_types/BLCA.md) — urothelial carcinoma of the bladder.

## Assays / panels (linked)

- [IMPACT341](../methods/IMPACT341.md) — MSK-IMPACT 341-gene targeted panel.
- [IMPACT410](../methods/IMPACT410.md) — MSK-IMPACT 410-gene targeted panel.
- [msk-impact-panel](../methods/msk-impact-panel.md) — hybrid-capture sequencing platform.

## Papers using this cohort

- [PMID:28583311](../papers/28583311.md) — Pietzak et al., *JCO* 2017: Targeted sequencing of 105 NMIBC tumors; [TERT](../genes/TERT.md) promoter mutations in 73%, chromatin-modifying gene alterations in 69%, ERBB2/FGFR3 alterations in 57% of high-grade NMIBC (mutually exclusive), DDR alterations in 30% of high-grade NMIBC; [ARID1A](../genes/ARID1A.md) mutations uniquely predict BCG recurrence (HR=3.14, p=0.002). [PMID:28583311](../papers/28583311.md)

## Notable findings derived from this cohort

- [TERT](../genes/TERT.md) promoter mutations are the most frequent alteration (73% overall) and occur at similar rates across grade and stage, supporting their role as an early urothelial carcinogenesis event. [PMID:28583311](../papers/28583311.md)
- Chromatin-modifying gene alterations present in 69% of NMIBC: [KDM6A](../genes/KDM6A.md) altered in 38% overall (52% LGTa, most common chromatin modifier), [ARID1A](../genes/ARID1A.md) in 21%. [PMID:28583311](../papers/28583311.md)
- [ERBB2](../genes/ERBB2.md) and [FGFR3](../genes/FGFR3.md) alterations occur in a mutually exclusive pattern in 57% of high-grade NMIBC; [FGFR3](../genes/FGFR3.md) alterations decrease with grade/stage, while [ERBB2](../genes/ERBB2.md) alterations concentrate in high-grade disease (especially HGTis). [PMID:28583311](../papers/28583311.md)
- DDR gene alterations in 30% of high-grade NMIBC (similar to MIBC rate of 33%); [ERCC2](../genes/ERCC2.md) missense mutations are the most common (17%), associated with markedly elevated mutational burden (median 26 vs 8 mutations/Mb, p<0.001). [PMID:28583311](../papers/28583311.md)
- [ARID1A](../genes/ARID1A.md) mutations are the only gene alteration significantly associated with BCG recurrence (HR=3.14, 95% CI 1.51–6.51, p=0.002, surviving multiple-comparison correction); [TP53](../genes/TP53.md), [ERBB2](../genes/ERBB2.md)/[FGFR3](../genes/FGFR3.md) status, and mutational count did not predict BCG response. [PMID:28583311](../papers/28583311.md)
- [STAG2](../genes/STAG2.md) truncating mutations are enriched in LGTa (39%) vs higher-grade/stage tumors (p=0.046), consistent with a low-grade-specific driver role. [PMID:28583311](../papers/28583311.md)
- [TP53](../genes/TP53.md)/[MDM2](../genes/MDM2.md) and cell-cycle alterations ([RB1](../genes/RB1.md), [CCND1](../genes/CCND1.md), [CDKN1A](../genes/CDKN1A.md), [CDKN2A](../genes/CDKN2A.md)) increase stepwise with stage and grade (p<0.001). [PMID:28583311](../papers/28583311.md)

## Sources

- cBioPortal study `blca_nmibc_2017`.
- Pietzak EJ, et al. *Next-Generation Sequencing of Nonmuscle Invasive Bladder Cancer Reveals Potential Biomarkers and Rational Therapeutic Targets.* JCO. 2017. [PMID:28583311](../papers/28583311.md)

*This page was processed by **crosslinker** on **2026-05-15**.*
