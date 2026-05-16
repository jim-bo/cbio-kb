---
name: MSK Pancreatic Neuroendocrine Tumors (panet_msk_2018)
studyId: panet_msk_2018
institution: Memorial Sloan Kettering Cancer Center
size: 96
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-panel-seq
  - matched-tumor-normal
panels:
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - pancreatic neuroendocrine tumor
  - panNET
  - MSK-IMPACT
  - metastatic
  - serial biopsy
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK Pancreatic Neuroendocrine Tumors (panet_msk_2018)

## Overview

Prospective, single-institution cohort of 80 patients with metastatic well-differentiated pancreatic neuroendocrine tumors ([PANET](../cancer_types/PANET.md)) enrolled at Memorial Sloan Kettering Cancer Center (ClinicalTrials.gov NCT01775072) between May 2014 and March 2017. 96 tumor samples (8 patients contributed 2 samples; 4 contributed 3) were profiled by matched tumor-normal [MSK-IMPACT](../methods/msk-impact-panel.md) hybridization-capture NGS. The cohort was designed to characterize the somatic and germline landscape of metastatic panNETs, to assess serial genomic changes during treatment, and to evaluate the actionability of detected alterations.

## Composition

- **80 patients / 96 samples**; metastatic disease in all; WHO grade: 30% G1, 46% G2, 24% G3; median Ki-67 10% (range 1–80%).
- **Demographics:** median age 54 (range 10–79); 56% female; liver metastases 81%, lymph-node metastases 33%.
- **Cancer type:** [PANET](../cancer_types/PANET.md) — pancreatic neuroendocrine tumors, metastatic, well-differentiated.
- **Germline assessment:** 76 cancer-susceptibility genes called from matched normal; ExAC <1% population-frequency cutoff; ACMG variant interpretation.
- **Loss of heterozygosity:** quantified by [FACETS](../methods/facets.md) allele-specific copy-number analysis on 95 of 96 samples; median sequencing depth 665.5× (range 75×–1255×).

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — matched tumor-normal hybridization-capture NGS; panel versions: pilot 275-gene, [IMPACT410](../methods/IMPACT410.md) (17% of samples), [IMPACT468](../methods/IMPACT468.md) (59%), and version 4 (22%).
- [FACETS](../methods/facets.md) — allele-specific copy-number and LOH analysis.

## Papers using this cohort

- [PMID:30687805](../papers/30687805.md) — Raj et al. 2018, *Journal of Clinical Oncology*: somatic and germline landscape of metastatic panNETs; serial sequencing for resistance and grade-progression mechanisms.

## Notable findings derived from this cohort

- Somatic alterations identified in 95% of patients (76/80); dominant drivers: [MEN1](../genes/MEN1.md) 56%, [DAXX](../genes/DAXX.md) 40%, [ATRX](../genes/ATRX.md) 25%, [TSC2](../genes/TSC2.md) 25%, [SETD2](../genes/SETD2.md) 18%, [BRAF](../genes/BRAF.md) 8%. [PMID:30687805](../papers/30687805.md)
- Genome-wide LOH (≥50% of genome) detected in 58% of samples (55/95); significantly enriched in tumors carrying [MEN1](../genes/MEN1.md), [DAXX](../genes/DAXX.md), [PTEN](../genes/PTEN.md), or [TSC2](../genes/TSC2.md) alterations (q < 0.05). [PMID:30687805](../papers/30687805.md)
- TMB tracks with grade: average 2.74 mut/Mb (G1), 4.20 (G2), 23.64 (G3); alkylator chemotherapy ([temozolomide](../drugs/temozolomide.md), [dacarbazine](../drugs/dacarbazine.md)) induced hypermutation (117–267 new mutations) with C>T signature and acquired MMR-gene mutations in three patients, all of whom progressed G1→G3. [PMID:30687805](../papers/30687805.md)
- Resistance mechanisms to [everolimus](../drugs/everolimus.md) identified on serial biopsy: acquired [PTEN](../genes/PTEN.md) Q298*, [RHEB](../genes/RHEB.md) Y35S, [TSC2](../genes/TSC2.md) splice, [AKT2](../genes/AKT2.md) G16D; [NRAS](../genes/NRAS.md) Q61R acquired at [vemurafenib](../drugs/vemurafenib.md) progression in one [BRAF](../genes/BRAF.md) V600E patient. [PMID:30687805](../papers/30687805.md)
- Germline pathogenic/likely-pathogenic variants in 16% (14/88 patients tested): high-penetrance [MEN1](../genes/MEN1.md), [VHL](../genes/VHL.md), [TSC2](../genes/TSC2.md) (1 each); moderate-penetrance [CHEK2](../genes/CHEK2.md) (4 patients); low-penetrance [MUTYH](../genes/MUTYH.md) (4), [APC](../genes/APC.md) I1307K (3). Supporting universal germline testing for panNET patients. [PMID:30687805](../papers/30687805.md)
- [MEN1](../genes/MEN1.md) and [DAXX](../genes/DAXX.md)/[ATRX](../genes/ATRX.md) alterations were associated with improved 1-year [OS](../cancer_types/OS.md) in this metastatic cohort ([MEN1](../genes/MEN1.md): 98% vs 82%, P=.01; DAXX/ATRX: 97% vs 83%, P<.01), contrasting with prior reports in resected disease. [BRAF](../genes/BRAF.md) alterations had significantly worse 1-year OS (75% vs 95%, P<.01). [PMID:30687805](../papers/30687805.md)
- mTOR-pathway mutation status did not predict [everolimus](../drugs/everolimus.md) benefit (response rates 17% vs 29% in mTOR-mutant vs mTOR-WT). [PMID:30687805](../papers/30687805.md)
- OncoKB-actionable somatic alterations affected 47% of patients (Levels 2b–4); no Level 1 or 2a evidence available at time of publication. [PMID:30687805](../papers/30687805.md)

## Sources

- cBioPortal study: `panet_msk_2018` — https://www.cbioportal.org/study/summary?id=panet_msk_2018
- [PMID:30687805](../papers/30687805.md) — Raj et al. 2018, *Journal of Clinical Oncology*, DOI 10.1200/JCO.18.01133

*This page was processed by **crosslinker** on **2026-05-16**.*
