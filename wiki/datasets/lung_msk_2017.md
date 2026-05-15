---
name: MSK-IMPACT Lung Adenocarcinoma Cohort (Jordan 2017)
studyId: lung_msk_2017
institution: Memorial Sloan Kettering Cancer Center
size: 860
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
panels:
  - IMPACT341
  - IMPACT410
tags:
  - lung-adenocarcinoma
  - luad
  - msk-impact
  - prospective-sequencing
  - precision-oncology
  - actionability
  - oncokb-levels
  - matched-therapy
processed_by: crosslinker
processed_at: 2026-05-14
---

# MSK-IMPACT Lung Adenocarcinoma Cohort (Jordan 2017)

## Overview

Prospective MSK-IMPACT sequencing cohort of 860 patients with recurrent or metastatic lung adenocarcinoma ([LUAD](../cancer_types/LUAD.md)) profiled at Memorial Sloan Kettering Cancer Center between January 2014 and March 2016. The study assessed the clinical actionability of MSK-IMPACT findings using the OncoKB evidence framework and determined the fraction of patients receiving molecularly matched therapy and deriving clinical benefit. Clinical and genomic data are deposited in cBioPortal. Trial registration: NCT01775072.

## Composition

- **860 patients** with recurrent or metastatic [LUAD](../cancer_types/LUAD.md); 915 tumors profiled.
- **Demographics:** women 58.8% (506); men 41.2% (354); age 51–75 years 71.5%; never smokers 32.2% (277); former heavy smokers (>15 pack-years) 48.8% (420); 8.4% Asian.
- **Tissue origin:** lung 420, lymph node 169, pleura/pleural fluid 110, liver 59, brain 47, bone 29.
- **Sample timing:** median 28 days from collection to genomic analysis; 89% used tissue ≤1 year old; mean turnaround 17 days from receipt to report.
- **Cancer types:** [LUAD](../cancer_types/LUAD.md).

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) matched tumor:normal hybrid-capture NGS.
  - [IMPACT341](../methods/IMPACT341.md) (341 genes) — 296 samples; [IMPACT410](../methods/IMPACT410.md) (410 genes) — 619 samples.
  - Average coverage 615X; matched normal available for 97% of samples.
- [FACETS](../methods/facets.md) — allele-specific copy number and tumor purity estimation.

## Papers using this cohort

- [PMID:28336552](../papers/28336552.md) — Jordan et al. 2017, *Cancer Discovery*: prospective MSK-IMPACT profiling of 860 [LUAD](../cancer_types/LUAD.md) patients; OncoKB-stratified actionability and matched-therapy outcomes.

## Notable findings derived from this cohort

- Potentially actionable somatic alterations (OncoKB levels 1–4) identified in 86.9% (747/860) of patients; 37.1% (319/860) received a molecularly matched therapy [PMID:28336552](../papers/28336552.md).
- Excluding standard-of-care matches ([EGFR](../genes/EGFR.md) mutations, [ALK](../genes/ALK.md)/[ROS1](../genes/ROS1.md) fusions), only 14.4% (69/478) received matched therapy, with 52% deriving clinical benefit [PMID:28336552](../papers/28336552.md).
- [EGFR](../genes/EGFR.md) sensitizing mutations in 24.9% (214/860); T790M in 5.5% (47/860), all post-TKI; cohort enriched for [EGFR](../genes/EGFR.md) vs. TCGA LUAD (27% vs. 11%, p<0.001) reflecting referral bias [PMID:28336552](../papers/28336552.md).
- 103 patients (12%) lacked any level 1–4 driver ("unknown mitogenic driver"); [STK11](../genes/STK11.md) and [KEAP1](../genes/KEAP1.md) were significantly enriched in this subgroup and nominated as candidate targetable mitogenic drivers [PMID:28336552](../papers/28336552.md).
- 27.8% (239/860) harbored ≥2 co-occurring actionable alterations; [EGFR](../genes/EGFR.md)/[KRAS](../genes/KRAS.md) were mutually exclusive (only 2/214 co-occurring, p<0.0001) [PMID:28336552](../papers/28336552.md).
- Allele-specific analysis showed lower clinical benefit rates for [EGFR](../genes/EGFR.md) L861Q (43%) and exon 18 deletions (40%) versus exon 19 deletions and L858R (p<0.05), supporting genotype-specific TKI selection [PMID:28336552](../papers/28336552.md).

## Sources

- cBioPortal studyId: lung_msk_2017
- Trial registration: NCT01775072
- [PMID:28336552](../papers/28336552.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
