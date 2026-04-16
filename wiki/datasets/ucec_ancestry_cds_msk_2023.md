---
name: Endometrial Carcinoma Ancestry Study (MSK, 2023)
studyId: ucec_ancestry_cds_msk_2023
institution: Memorial Sloan Kettering Cancer Center
size: 1882
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [targeted-panel]
panels: []
tags: [endometrial, uterine, ancestry, racial-disparities, UCEC]
processed_by: crosslinker
processed_at: 2026-04-11
---

# Endometrial Carcinoma Ancestry Study (MSK, 2023)

## Overview

Single-center retrospective cohort of 1,882 endometrial carcinoma patients (259 self-identified Black, 1,623 self-identified White) treated at Memorial Sloan Kettering Cancer Center from January 2014 through December 2021. Designed to characterize molecular differences between Black and White patients with endometrial cancer and identify racial disparities in actionable alterations. Sequenced with [MSK-IMPACT](../methods/msk-impact-panel.md) (341–505 gene panel), tumor-normal, FDA-authorized. Data deposited in cBioPortal as `ucec_ancestry_cds_msk_2023`. [PMID:37651310](../papers/37651310.md)

## Composition

- Cancer type: endometrial carcinoma ([UCEC](../cancer_types/UCEC.md)), including serous ([USC](../cancer_types/USC.md)), carcinosarcoma ([UCS](../cancer_types/UCS.md)), endometrioid, clear cell, and mixed/high-grade NOS subtypes.
- 259 self-identified Black patients (70% African ancestry, 30% Admixed by IMPACT-inferred genetic ancestry).
- 1,623 self-identified White patients.
- Molecular subtyping performed: [POLE](../genes/POLE.md), MSI-H, CN-H/TP53abn, CN-L/NSMP using integrated sequencing and IHC.
- Copy-number analysis with [FACETS](../methods/facets.md). [PMID:37651310](../papers/37651310.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) (341–505 gene panel) — somatic and germline profiling, tumor-normal pairs.
- [FACETS](../methods/facets.md) — allele-specific copy-number analysis.

## Papers using this cohort

- [PMID:37651310](../papers/37651310.md) — Molecular characterization of endometrial carcinomas in Black and White patients reveals disparate drivers with therapeutic implications.

## Notable findings derived from this cohort

- Black patients had more high-risk histologies: serous (29% vs. 13%), carcinosarcoma (20% vs. 11%), less low-grade endometrioid (21% vs. 47%; p < 0.01). [PMID:37651310](../papers/37651310.md)
- 69% of ECs in Black patients were CN-H/[TP53](../genes/TP53.md)abn vs. 35% in White patients (p < 0.001). POLE subtype was rare in Black patients (1.2% vs. 5.8%). [PMID:37651310](../papers/37651310.md)
- [TP53](../genes/TP53.md) mutations enriched in Black patients (72% vs. 42%; q < 0.001); median TMB 4 vs. 7 Mut/Mb (p < 0.001). [PMID:37651310](../papers/37651310.md)
- [CCNE1](../genes/CCNE1.md) amplification more prevalent in Black patients (15% vs. 4%; q < 0.001); [ERBB2](../genes/ERBB2.md) amplification enriched in Black patients (12% vs. 3%; q < 0.001). [PMID:37651310](../papers/37651310.md)
- PI3K pathway alterations less common in Black patients: [PTEN](../genes/PTEN.md) 26% vs. 55%, [PIK3R1](../genes/PIK3R1.md) 13% vs. 28%, [KRAS](../genes/KRAS.md) 12% vs. 21%. [PMID:37651310](../papers/37651310.md)
- Clinically actionable alterations (OncoKB Level 1/2/3A) less frequent in Black patients: 22.4% vs. 39.7% (p < 0.001). [PMID:37651310](../papers/37651310.md)
- Higher chromosomal instability in Black patients: FGA median 30% vs. 10% (p < 0.001); whole-genome doubling 32% vs. 18% (p < 0.001). [PMID:37651310](../papers/37651310.md)

## Sources

- cBioPortal study `ucec_ancestry_cds_msk_2023`. [PMID:37651310](../papers/37651310.md)

*This page was processed by **crosslinker** on **2026-04-11**.*
