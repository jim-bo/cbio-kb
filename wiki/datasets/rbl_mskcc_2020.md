---
name: MSK Retinoblastoma MSK-IMPACT 2020
studyId: rbl_mskcc_2020
institution: Memorial Sloan Kettering Cancer Center
size: 83
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MSK-IMPACT
panels:
  - IMPACT468
tags:
  - retinoblastoma
  - pediatric
  - targeted-sequencing
  - germline
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK Retinoblastoma MSK-IMPACT 2020

## Overview

Prospective cohort of 83 enucleated [retinoblastoma](../cancer_types/RBL.md) ([RBL](../cancer_types/RBL.md)) specimens accrued between May 2006 and August 2019 at Memorial Sloan Kettering Cancer Center (IRB #17-049). All tumors were profiled by [MSK-IMPACT](../methods/msk-impact-panel.md) hybridization-capture targeted NGS using the 468-gene panel ([IMPACT468](../methods/IMPACT468.md)) for somatic analysis and an 88-gene subset for germline analysis in 42 consented patients. Copy-number and clonality were called with [FACETS](../methods/facets.md) v0.5.14; microsatellite instability estimated with [MSIsensor](../methods/msisensor.md). The dataset is deposited at cBioPortal (`https://cbioportal.mskcc.org/study/summary?id=rbl_mskcc_2020`).

## Composition

- **Cancer type:** [Retinoblastoma (RBL)](../cancer_types/RBL.md)
- **N = 83** enucleated specimens (74 with matched normal tissue; 9 tumor-only)
- **Germline cohort:** 42/83 patients consented to germline [IMPACT468](../methods/IMPACT468.md) testing (88-gene panel)
- **Tissue input:** 10-µm FFPE microdissected sections, DNeasy extraction, ≥250 ng FFPE DNA
- **Key clinical fields:** vitreous seeding status, high-risk histopathological features, enucleation date, metastasis-free survival
- **Bilateral disease:** two patients with bilateral disease and germline [RB1](../genes/RB1.md) alterations had distinct somatic second hits per eye

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — hybridization-capture targeted NGS, 468 genes somatic, 88 genes germline
- [IMPACT468](../methods/IMPACT468.md) — version used for all somatic calls
- [FACETS](../methods/facets.md) — allele-specific copy-number and clonality analysis
- [MSIsensor](../methods/msisensor.md) — microsatellite instability estimation

## Papers using this cohort

- [PMID:33466343](../papers/33466343.md) — MSK retinoblastoma IMPACT genomic landscape study

## Notable findings derived from this cohort

- [RB1](../genes/RB1.md) biallelic loss detected in 79.5% (66/83) of specimens; pathognomonic [RB1](../genes/RB1.md) alterations in 97.5% (79/81) of patients; copy-neutral LOH was the dominant second-hit mechanism (31/42 LOH events, OR=19.8 vs. other TSGs). [PMID:33466343](../papers/33466343.md)
- [BCOR](../genes/BCOR.md) was the most common non-[RB1](../genes/RB1.md) somatic alteration (19/83, 22.9%), all putative loss-of-function; associated with worse metastasis-free survival (Kaplan-Meier p=0.03). [PMID:33466343](../papers/33466343.md)
- Tumor mutational burden was uniformly low (0–3 mutations/Mb); no MSI-high tumors detected. [PMID:33466343](../papers/33466343.md)
- Recurrent arm-level CNAs (n=69 evaluable eyes): 1q gain 67%, 6p gain 59%, 13q LOH 51%, 16q LOH 43%, 2p gain 32%; 1q gain and 16q LOH independently associated with vitreous seeding (BH p=0.008 and 0.004; OR=12.6 and 26.7). [PMID:33466343](../papers/33466343.md)
- Germline non-[RB1](../genes/RB1.md) cancer-predisposition mutations in 5/42 (~12%) of germline-tested patients, involving [NTHL1](../genes/NTHL1.md), [ERCC3](../genes/ERCC3.md), [MSH3](../genes/MSH3.md), [CHEK2](../genes/CHEK2.md), and [MITF](../genes/MITF.md). [PMID:33466343](../papers/33466343.md)

## Sources

- cBioPortal study: `rbl_mskcc_2020`
- [PMID:33466343](../papers/33466343.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
