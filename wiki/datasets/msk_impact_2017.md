---
name: MSK-IMPACT Clinical Sequencing Cohort (MSK, Nat Med 2017)
studyId: msk_impact_2017
institution: 
size: 
reference_genome: GRCh37
canonical_source: 
unverified: 
assays: []
panels: []
tags: []
processed_by: crosslinker
processed_at: 2026-05-21
description: Targeted sequencing of 10,000 clinical cases using the MSK-IMPACT assay
cancerTypeId: mixed
pmid: 28481359
allSampleCount: 1
---

# MSK-IMPACT Clinical Sequencing Cohort (MSK, Nat Med 2017)

## Overview

The foundational MSK-IMPACT clinical sequencing cohort (Zehir et al. 2017) comprising 10,000 tumor/normal pairs sequenced with the MSK-IMPACT targeted panel across tumor types. Within the cbio-kb corpus, this dataset is referenced as the institutional context for subsequent MSK rare-cancer profiling efforts [PMID:36862133](../papers/36862133.md).

## Composition

- 10,000 prospective clinical cases across diverse tumor types profiled via MSK-IMPACT.

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) targeted DNA sequencing panel.

## Papers using this cohort

- [PMID:28481359](../papers/28481359.md) — Zehir et al., *Nat Med* 2017: Seminal MSK-IMPACT report; prospective CLIA-certified targeted sequencing of 10,945 tumors from 10,336 patients across 62 principal tumor types using IMPACT341/IMPACT410 panels; 36.7% of patients harbored an OncoKB-actionable alteration; 11% (527/5,009) matched to a genomically targeted clinical trial; full dataset deposited to cBioPortal as msk_impact_2017. [PMID:28481359](../papers/28481359.md)
- [PMID:36862133](../papers/36862133.md) — Doe-Tetteh et al. list `msk_impact_2017` alongside `[makeanimpact_ccr_2023](../datasets/makeanimpact_ccr_2023.md)` as the cBioPortal dataset context for their rare-cancer Make-an-IMPACT outreach program, which itself used the MSK-IMPACT clinical platform to return results to patients and local physicians [PMID:36862133](../papers/36862133.md).
- [PMID:39506116](../papers/39506116.md) — Kehl et al. MSK-CHORD: the 24,950-patient MSK-CHORD real-world dataset was built on top of MSK-IMPACT sequencing; `msk_impact_2017` is cited as the foundational clinical sequencing backbone whose tumor genomics feed into MSK-CHORD [PMID:39506116](../papers/39506116.md).
- [PMID:39746944](../papers/39746944.md) — Ziegler et al. MiMSI: the global comparison cohort (n=45,112 samples from 40,414 patients) drawn from prospective MSK-IMPACT clinical sequencing (January 2014–April 2020) is the same pipeline documented in `msk_impact_2017`; concordance between MSISensor and MiMSI was evaluated on this cohort [PMID:39746944](../papers/39746944.md).
- [PMID:33863915](../papers/33863915.md) — da Silva et al., *npj Breast Cancer* 2021: Three previously reported MSK-IMPACT [MBC](../cancer_types/MBC.md) cases from `msk_impact_2017` were included in a 60-sample [TERT](../genes/TERT.md) alteration study of metaplastic breast cancer; [TERT](../genes/TERT.md) promoter hotspot mutations or amplification found in 17% (10/60) of MBCs, mutually exclusive with [TP53](../genes/TP53.md) mutations (p<0.001) and co-occurring with [PIK3CA](../genes/PIK3CA.md) hotspots (p=0.001). [PMID:33863915](../papers/33863915.md)

## Notable findings derived from this cohort

- [TP53](../genes/TP53.md) was the most frequently altered gene (41% of 10,945 tumors, >10% in 43/62 principal tumor types); [KRAS](../genes/KRAS.md) was 2nd (15%), with G12 codons comprising 80% of all [KRAS](../genes/KRAS.md) mutations and 12% of all patients; 36.7% of patients harbored an OncoKB-actionable alteration. [PMID:28481359](../papers/28481359.md)
- 81% of all mutations fell outside the combined target regions of commercially available amplicon hotspot panels; ≥9% of mutations would have been missed by WES to 150× mean depth, including targetable [BRAF](../genes/BRAF.md), [EGFR](../genes/EGFR.md), and [MET](../genes/MET.md) alterations. [PMID:28481359](../papers/28481359.md)
- Mutation-signature calling identified MMR deficiency (MSI) in 102 patients across 11 tumor types; 45% had not been previously tested, including a prostate cancer patient who responded to anti-PD-L1 therapy. [PMID:28481359](../papers/28481359.md)
- 11% (527/5,009) of patients with ≥12-month follow-up were enrolled on a genomically matched targeted-therapy trial; 72% of matches occurred after MSK-IMPACT reporting itself. [PMID:28481359](../papers/28481359.md)
- The original Make-an-IMPACT report demonstrates that the MSK-IMPACT clinical platform underpinning msk_impact_2017 can be extended via direct-to-patient outreach to enroll international rare-cancer cohorts with 86.8% sequencing success [PMID:36862133](../papers/36862133.md).
- Across 45,112 MSK-IMPACT samples from the same clinical sequencing pipeline, MiMSI reduced MSI-indeterminate calls from 3.8% (n=1,724 by MSISensor) to 0.47% (n=210), with 96% concordance for definitive MSS/MSI-H calls [PMID:39746944](../papers/39746944.md).
- The MSK-CHORD real-world dataset integrates MSK-IMPACT tumor genomics with NLP-derived EHR annotations for 24,950 patients; multimodal models combining genomic and NLP features outperformed stage-alone [OS](../cancer_types/OS.md) prediction in [NSCLC](../cancer_types/NSCLC.md), breast, colorectal, prostate, and pancreatic cancers [PMID:39506116](../papers/39506116.md).
- 706 advanced prostate cancers from MSK-IMPACT in this cohort were used as validation for 97 significantly mutated genes discovered in the [prad_p1000](../datasets/prad_p1000.md) pan-1000 prostate meta-cohort, confirming novel drivers including [CUL3](../genes/CUL3.md) (9 cases), [SPEN](../genes/SPEN.md), [SF3B1](../genes/SF3B1.md), and [PIK3R2](../genes/PIK3R2.md) [PMID:29610475](../papers/29610475.md)
- da Silva et al. used three previously published [MBC](../cancer_types/MBC.md) cases from msk_impact_2017 as part of a 60-sample study of TERT promoter mutations and gene amplification in metaplastic breast cancer; TERT alterations were found in 17% (10/60) of MBCs and were mutually exclusive with [TP53](../genes/TP53.md) mutations (p<0.001) [PMID:33863915](../papers/33863915.md)
- 4,561 CRC patients were sequenced with MSK-IMPACT at MSK; 47 (1.03%) had dual RAS hotspot/BRAF V600E driver mutations, defining the [crc_dd_2022](../datasets/crc_dd_2022.md) sub-cohort; the backbone sequencing data lives in msk_impact_2017 [PMID:35235413](../papers/35235413.md)

## Sources

- cBioPortal study `msk_impact_2017`.
- Zehir A, et al. *Mutational landscape of metastatic cancer revealed from prospective clinical sequencing of 10,000 patients.* Nat Med. 2017. [PMID:28481359](../papers/28481359.md)
- [PMID:29610475](../papers/29610475.md)
- [PMID:33863915](../papers/33863915.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35235413](../papers/35235413.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
