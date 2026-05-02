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
processed_at: 2026-04-30
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

- [PMID:36862133](../papers/36862133.md) — Doe-Tetteh et al. list `msk_impact_2017` alongside `[makeanimpact_ccr_2023](../datasets/makeanimpact_ccr_2023.md)` as the cBioPortal dataset context for their rare-cancer Make-an-IMPACT outreach program, which itself used the MSK-IMPACT clinical platform to return results to patients and local physicians [PMID:36862133](../papers/36862133.md).
- [PMID:39506116](../papers/39506116.md) — Kehl et al. MSK-CHORD: the 24,950-patient MSK-CHORD real-world dataset was built on top of MSK-IMPACT sequencing; `msk_impact_2017` is cited as the foundational clinical sequencing backbone whose tumor genomics feed into MSK-CHORD [PMID:39506116](../papers/39506116.md).
- [PMID:39746944](../papers/39746944.md) — Ziegler et al. MiMSI: the global comparison cohort (n=45,112 samples from 40,414 patients) drawn from prospective MSK-IMPACT clinical sequencing (January 2014–April 2020) is the same pipeline documented in `msk_impact_2017`; concordance between MSISensor and MiMSI was evaluated on this cohort [PMID:39746944](../papers/39746944.md).

## Notable findings derived from this cohort

- The original Make-an-IMPACT report demonstrates that the MSK-IMPACT clinical platform underpinning msk_impact_2017 can be extended via direct-to-patient outreach to enroll international rare-cancer cohorts with 86.8% sequencing success [PMID:36862133](../papers/36862133.md).
- Across 45,112 MSK-IMPACT samples from the same clinical sequencing pipeline, MiMSI reduced MSI-indeterminate calls from 3.8% (n=1,724 by MSISensor) to 0.47% (n=210), with 96% concordance for definitive MSS/MSI-H calls [PMID:39746944](../papers/39746944.md).
- The MSK-CHORD real-world dataset integrates MSK-IMPACT tumor genomics with NLP-derived EHR annotations for 24,950 patients; multimodal models combining genomic and NLP features outperformed stage-alone [OS](../cancer_types/OS.md) prediction in [NSCLC](../cancer_types/NSCLC.md), breast, colorectal, prostate, and pancreatic cancers [PMID:39506116](../papers/39506116.md).

## Sources

- cBioPortal study `msk_impact_2017`.
- Zehir A, et al. *Mutational landscape of metastatic cancer revealed from prospective clinical sequencing of 10,000 patients.* Nat Med. 2017. PMID:28481359 — original cohort paper (not in the cbio-kb corpus).

*This page was processed by **crosslinker** on **2026-04-30**.*
