---
name: MSK GIST Germline Study (2022)
studyId: gist_msk_2022
institution: Memorial Sloan Kettering Cancer Center
size: 499
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
panels:
  - msk-impact-panel
tags:
  - gist
  - germline
  - hereditary-cancer
  - tumor-normal-sequencing
  - sdh-deficiency
  - sarcoma
processed_by: crosslinker
processed_at: 2026-05-05
---

# MSK GIST Germline Study (2022)

## Overview

Institutional cohort from Memorial Sloan Kettering Cancer Center profiling gastrointestinal stromal tumor ([GIST](../cancer_types/GIST.md)) patients for germline pathogenic/likely pathogenic (P/LP) variants. The study includes 103 patients who consented to germline analysis (April 2015–June 2021) and an expanded de-identified cohort of 499 tumor-normal pairs sequenced by [MSK-IMPACT](../methods/msk-impact-panel.md). The dataset is publicly available on cBioPortal as `gist_msk_2022`.

## Composition

- 103 consented [GIST](../cancer_types/GIST.md) patients with paired germline sequencing; 499 tumor-normal pairs in the broader cohort.
- Sequenced with [MSK-IMPACT](../methods/msk-impact-panel.md) (341, 410, or 505 gene panels).
- Key clinical fields: age at diagnosis, syndromic history ([NF1](../genes/NF1.md), SDH-related paraganglioma/pheochromocytoma), KIT/PDGFRA mutation status.

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — targeted tumor-normal sequencing (341/410/505 gene panels)

## Papers using this cohort

- [PMID:36593350](../papers/36593350.md) — Mandelker et al., *npj Precision Oncology* 2023. Germline testing in GIST reveals high frequency of non-syndromic pathogenic variants.

## Notable findings derived from this cohort

- 69% (24/35) of KIT/PDGFRA-wildtype GIST patients harbored germline P/LP variants in GIST-associated genes ([SDHA](../genes/SDHA.md), [SDHB](../genes/SDHB.md), [SDHC](../genes/SDHC.md), NF1, [KIT](../genes/KIT.md)), and 63% of those had no personal or family history of syndromic features [PMID:36593350](../papers/36593350.md).
- 23% (24/103) of unselected GIST patients had a germline P/LP variant; patients with germline variants had younger median age-of-onset (39.5 vs 52 years, p=0.01) and higher rates of metastatic disease (50% vs 20%, p=0.01) [PMID:36593350](../papers/36593350.md).
- ESMO-recommended VAF thresholds (>30% for SNVs, >20% for indels) correctly distinguished all germline from somatic P/LP variants in the 499-patient tumor-only cohort [PMID:36593350](../papers/36593350.md).
- [SDHB](../genes/SDHB.md) and [BRCA2](../genes/BRCA2.md) variants in tumor-only sequencing were almost exclusively germline in origin (10/11 and 4/4 respectively), supporting reflex germline testing [PMID:36593350](../papers/36593350.md).

## Sources

- cBioPortal study: `gist_msk_2022`
- Associated publication: [PMID:36593350](../papers/36593350.md)

*This page was processed by **crosslinker** on **2026-05-05**.*
