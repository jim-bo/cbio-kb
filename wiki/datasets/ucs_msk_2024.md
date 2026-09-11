---
name: Endometrial Carcinoma (MSK, Molecular Oncology 2024)
studyId: ucs_msk_2024
institution: Memorial Sloan Kettering Cancer Center
size: 69
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [targeted-panel, whole-exome-seq]
panels: [IMPACT341, IMPACT410, IMPACT468, IMPACT505]
tags: [endometrial-cancer, erbb2-mutation, her2, msi-h, tumor-mutational-burden, msk-impact]
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# Endometrial Carcinoma (MSK, Molecular Oncology 2024)

## Overview

Single-center cohort of 69 ERBB2-mutant endometrial carcinomas (ECs) with matched normals, identified from an institutional screening population of 2,638 consented EC patients who underwent clinical FDA-authorized tumor-normal [MSK-IMPACT](../methods/msk-impact-panel.md) sequencing between 01/2014 and 03/2022 (IRB #12-245) at Memorial Sloan Kettering Cancer Center. Deposited in cBioPortal as `ucs_msk_2024` (metadata per `schema/ontology/studies.json`). [PMID:39031567](../papers/39031567.md)

## Composition

- 69 pathogenic-[ERBB2](../genes/ERBB2.md)-mutant ECs and their matched normals (2.6% of the 2,638-patient screening cohort); 11 (16%) also ERBB2-amplified, 8 (12%) with more than one pathogenic ERBB2 mutation. [PMID:39031567](../papers/39031567.md)
- Histology (ERBB2-mut/non-amp, n = 58): endometrioid [UEC](../cancer_types/UEC.md) 66%, serous [USC](../cancer_types/USC.md) 6.9%, clear cell [UCCC](../cancer_types/UCCC.md) 6.9%, carcinosarcoma [UCS](../cancer_types/UCS.md) 6.9%, mixed/high-grade EC-NOS 10%, undifferentiated/dedifferentiated 3.4%. [PMID:39031567](../papers/39031567.md)
- Molecular subtypes assigned by an integrated molecular–IHC classifier (POLE > MSI-H > CN-H/TP53abn > CN-L/NSMP). [PMID:39031567](../papers/39031567.md)
- HER2 [immunohistochemistry](../methods/immunohistochemistry.md) performed on 41 of the 69 cases. [PMID:39031567](../papers/39031567.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) targeted panels: [IMPACT341](../methods/IMPACT341.md), [IMPACT410](../methods/IMPACT410.md), [IMPACT468](../methods/IMPACT468.md), [IMPACT505](../methods/IMPACT505.md).
- Copy number / LOH: [FACETS](../methods/facets.md); clonality: [ABSOLUTE](../methods/absolute.md); MSI status: [MSIsensor](../methods/msisensor.md); variant annotation: [OncoKB](../methods/oncokb.md).
- HER2 [immunohistochemistry](../methods/immunohistochemistry.md) and [FISH](../methods/fish.md) on a subset. [PMID:39031567](../papers/39031567.md)

## Papers using this cohort

- [PMID:39031567](../papers/39031567.md) — source publication defining and analyzing this cohort (Brodeur et al., Mol Oncol 2024).

## Notable findings derived from this cohort

- ERBB2 mutation hotspots: V842I (26/69, 38%) and R678Q (16/69, 23%); ERBB2 mutations were clonal in 87% (53/61 evaluable cases). [PMID:39031567](../papers/39031567.md)
- ERBB2-mut/non-amp ECs had significantly higher TMB (median 43.2 mut/Mb) and lower fraction of genome altered (median 0.5%) than ERBB2-wt/non-amp ECs (median 6.1 mut/Mb; FGA 5.1%; both P < 0.001). [PMID:39031567](../papers/39031567.md)
- ERBB2-mut/non-amp ECs were enriched for MSI-H (59% vs 24%) and POLE (11% vs 5.6%) molecular subtypes relative to ERBB2-wt/non-amp ECs (P < 0.001). [PMID:39031567](../papers/39031567.md)
- Most frequent co-mutations in ERBB2-mutated ECs: [ARID1A](../genes/ARID1A.md) 65%, [PTEN](../genes/PTEN.md) 57%, [PIK3CA](../genes/PIK3CA.md) 54%. [PMID:39031567](../papers/39031567.md)
- In a subset of 6 [trastuzumab](../drugs/trastuzumab.md)-treated recurrent patients, best responses ranged from complete response (1) to progressive disease (3); on multivariate survival analysis, ERBB2 status was not independently prognostic. [PMID:39031567](../papers/39031567.md)

## Sources

- cBioPortal study: `ucs_msk_2024` (schema/ontology/studies.json)
- [PMID:39031567](../papers/39031567.md)

*This page was processed by **entity-page-writer** on **2026-09-10**.*
