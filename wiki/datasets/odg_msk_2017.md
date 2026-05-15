---
name: MSK Anaplastic Oligodendroglioma Cohort (MSK, JCO 2017)
studyId: odg_msk_2017
institution: Memorial Sloan Kettering Cancer Center
size: 41
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - targeted-panel-seq
panels:
  - IMPACT410
tags:
  - oligodendroglioma
  - glioma
  - 1p19q-codeletion
  - idh-mutant
  - msk-impact
  - phase-ii-trial
  - hdc-asct
processed_by: crosslinker
processed_at: 2026-05-15
---

# MSK Anaplastic Oligodendroglioma Cohort (MSK, JCO 2017)

## Overview

The odg_msk_2017 dataset comprises clinical and genomic data from a multicenter, investigator-initiated phase II trial (NCT00588523) sponsored by Memorial Sloan Kettering Cancer Center (MSK), enrolling 41 patients with newly diagnosed anaplastic oligodendroglioma (AO) or anaplastic oligoastrocytoma (AOA) between August 2005 and November 2012. The study tested whether induction [temozolomide](../drugs/temozolomide.md) followed by myeloablative high-dose thiotepa/busulfan chemotherapy with autologous stem-cell transplant (HDC-ASCT) could defer radiotherapy. Of the 41 enrolled patients, 19 had adequate tissue for NGS using the MSK-IMPACT 410-gene panel ([IMPACT410](../methods/IMPACT410.md)), providing the genomic characterization deposited to cBioPortal. Eighty-five percent of patients had 1p/19q-codeleted tumors. Full clinical and genomic data are publicly available at cbioportal.org/study?id=odg_msk_2017.

## Composition

- **41 patients** enrolled; 38 received TMZ induction; 21 completed HDC-ASCT.
- **Histologies:** 36 anaplastic oligodendroglioma (AO; 88%), 5 anaplastic oligoastrocytoma (AOA; 12%).
- **1p/19q status (FISH):** 33/39 (85%) codeleted, 6 non-codeleted, 2 unknown.
- **Patient characteristics:** 27 men / 14 women; median age 44 years (range 30–66); median KPS 90.
- **NGS subset:** 19 tumors with adequate DNA sequenced on [IMPACT410](../methods/IMPACT410.md) (hybridization-capture, Illumina HiSeq 2500, full exon coverage of 410 cancer-related genes); 14 codeleted, 5 1p/19q-intact.
- **Actionability annotation:** OncoKB database (accessed 6 January 2017).
- **Median follow-up:** 65.7 months.
- **Cancer type:** [ODG3](../cancer_types/ODG3.md) — Oligodendroglioma, IDH-mutant, 1p/19q-codeleted, Grade 3.

## Assays / panels (linked)

- [IMPACT410](../methods/IMPACT410.md) — MSK-IMPACT 410-gene hybrid-capture targeted panel.
- [msk-impact-panel](../methods/msk-impact-panel.md) — platform.
- [fish-1p19q](../methods/fish-1p19q.md) — 1p/19q codeletion assessment.
- [oncokb-annotation](../methods/oncokb-annotation.md) — actionability classification.

## Papers using this cohort

- [PMID:28472509](../papers/28472509.md) — Thomas et al., *JCO* 2017: Phase II trial reporting 5-year PFS of 60% and 5-year [OS](../cancer_types/OS.md) of 100% in transplanted patients; NGS confirmed canonical oligodendroglioma genomic signatures ([TERT](../genes/TERT.md) 95%, [IDH1](../genes/IDH1.md) 68%, [CIC](../genes/CIC.md) 53%) and exposed a false-positive 1p/19q FISH call with a glioblastoma-like NGS profile; no transplanted patient had died at time of analysis. [PMID:28472509](../papers/28472509.md)

## Notable findings derived from this cohort

- Induction TMZ + HDC-ASCT achieves 2-year PFS 86% and 5-year OS 100% in 21 transplanted patients, enabling radiotherapy deferral in 52% of 1p/19q-codeleted patients at 5 years. [PMID:28472509](../papers/28472509.md)
- NGS on 19 tumors confirmed canonical oligodendroglioma signatures: [TERT](../genes/TERT.md) promoter mutation 95% (18/19), [IDH1](../genes/IDH1.md) R132H 68% (13/19), [CIC](../genes/CIC.md) 53% (10/19), [FUBP1](../genes/FUBP1.md) 26% (5/19), [NOTCH1](../genes/NOTCH1.md) 32% (6/19). [PMID:28472509](../papers/28472509.md)
- 1p/19q-intact tumors displayed glioblastoma-like NGS signatures ([EGFR](../genes/EGFR.md) amplification/mutation, [NF1](../genes/NF1.md), [MDM2](../genes/MDM2.md) amplification, wild-type [IDH1](../genes/IDH1.md)/[IDH2](../genes/IDH2.md)). [PMID:28472509](../papers/28472509.md)
- NGS exposed a false-positive 1p/19q FISH call: one patient classified as codeleted by FISH carried a glioblastoma-like NGS signature ([PTEN](../genes/PTEN.md) loss, [CDKN2A](../genes/CDKN2A.md)/[CDKN2B](../genes/CDKN2B.md) deletion, IDH1/2 wild-type) and died at 13 months after early progression. [PMID:28472509](../papers/28472509.md)
- OncoKB-actionable alterations were individually rare: [CDK4](../genes/CDK4.md) amplification (2/19), [TSC1](../genes/TSC1.md) (1/19) at Level 2B; [IDH1](../genes/IDH1.md)/[IDH2](../genes/IDH2.md), [KRAS](../genes/KRAS.md) Q61H, [PIK3CA](../genes/PIK3CA.md) at Level 3B. [PMID:28472509](../papers/28472509.md)

## Sources

- cBioPortal study `odg_msk_2017` (http://cbioportal.org/study?id=odg_msk_2017).
- Thomas AA, et al. *Temozolomide Induction Therapy Followed by High-Dose Chemotherapy With Autologous Stem-Cell Transplantation in Newly Diagnosed Anaplastic Oligodendroglioma: A Phase 2 Study.* JCO. 2017. [PMID:28472509](../papers/28472509.md)

*This page was processed by **crosslinker** on **2026-05-15**.*
