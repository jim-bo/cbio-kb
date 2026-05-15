---
name: SUMMIT Basket Trial — Neratinib in HER2/HER3-Mutant Cancers (2018)
studyId: summit_2018
institution: Multi-institutional (Memorial Sloan Kettering Cancer Center lead)
size: 141
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - msk-impact-panel
  - facets
  - cell-free-dna
panels:
  - IMPACT341
  - IMPACT410
tags:
  - basket-trial
  - her2-mutant
  - her3-mutant
  - pan-her-tki
  - tumor-agnostic
  - allele-specific-response
  - co-mutation
  - clonality
processed_by: crosslinker
processed_at: 2026-05-15
---

# SUMMIT Basket Trial — Neratinib in HER2/HER3-Mutant Cancers (2018)

## Overview

SUMMIT (NCT01953926) is a multi-histology, genomically selected basket trial of the irreversible pan-HER tyrosine kinase inhibitor [neratinib](../drugs/neratinib.md) in patients with advanced solid tumours harbouring somatic [ERBB2](../genes/ERBB2.md) (HER2) or [ERBB3](../genes/ERBB3.md) (HER3) mutations. The dataset deposited in cBioPortal covers 141 patients (125 HER2-mutant, 16 HER3-mutant) across 21 cancer types; data were interim as of March 2017. Central sequencing used the [MSK-IMPACT](../methods/msk-impact-panel.md) panel at mean 738x coverage; local mutation testing from 30 unique assays across 25 laboratories was accepted for enrollment. The trial established that HER2-mutant sensitivity to [neratinib](../drugs/neratinib.md) is jointly determined by tumour lineage and specific mutant allele. [PMID:29420467](../papers/29420467.md)

## Composition

- **141 patients** (125 [ERBB2](../genes/ERBB2.md)-mutant, 16 [ERBB3](../genes/ERBB3.md)-mutant) across 21 cancer types; most common: [BRCA](../cancer_types/BRCA.md) (breast), [NSCLC](../cancer_types/NSCLC.md)/[LUAD](../cancer_types/LUAD.md), [BLCA](../cancer_types/BLCA.md) (bladder/urinary tract), and [COAD](../cancer_types/COAD.md) (colorectal) — 61% of treated patients. [PMID:29420467](../papers/29420467.md)
- **Pre-specified disease cohorts:** endometrial, gastroesophageal, ovarian, colorectal, bladder/urinary tract, plus a histology-agnostic "Solid tumour (NOS)" cohort. Breast, [CESC](../cancer_types/CESC.md), [CHOL](../cancer_types/CHOL.md), [SACA](../cancer_types/SACA.md), and lung accrued sufficient patients in NOS for independent efficacy analysis. [PMID:29420467](../papers/29420467.md)
- **Treatment:** [neratinib](../drugs/neratinib.md) 240 mg PO daily continuous with mandatory loperamide prophylaxis during cycle 1. [PMID:29420467](../papers/29420467.md)
- **Primary endpoint:** ORR at week 8 (ORR8) by RECIST v1.1; PET Response Criteria (PRC, modified PERCIST v1.0) used for non-RECIST-evaluable patients. [PMID:29420467](../papers/29420467.md)
- **Data interim cut:** 10 March 2017 (enrollment through 16 December 2016). [PMID:29420467](../papers/29420467.md)

## Assays / panels (linked)

- **Central sequencing** (n=91 tissue + n=15 plasma cfDNA with n=102 matched germline): [MSK-IMPACT](../methods/msk-impact-panel.md) — [IMPACT341](../methods/IMPACT341.md) (n=18) or [IMPACT410](../methods/IMPACT410.md) (n=88), mean 738x coverage. [PMID:29420467](../papers/29420467.md)
- **Local sequencing:** 30 unique assays from 25 laboratories; 85% (120/141) by NGS; concordance with central calls 95% for HER2, 75% for HER3. [PMID:29420467](../papers/29420467.md)
- **Copy-number / purity:** [FACETS](../methods/facets.md) v0.3.9; clonality by [ABSOLUTE](../methods/absolute.md) v1.0.6; MSI by [MSIsensor](../methods/msisensor.md); pathway calls from [OncoKB](../methods/oncokb-annotation.md) (September 2017); [mutational signatures](../methods/mutational-signatures.md) decomposed into 30 COSMIC processes. [PMID:29420467](../papers/29420467.md)

## Papers using this cohort

- [PMID:29420467](../papers/29420467.md) — Hyman et al. 2018, *Nature* — "HER kinase inhibition in patients with HER2- and HER3-mutant cancers"

## Notable findings derived from this cohort

- Breast cancer met its pre-specified efficacy endpoint with ORR8 32% (8/25, 95% CI 15–54%) across extracellular and kinase domain mutations and ER subtypes, all in centrally HER2-non-amplified tumours. [PMID:29420467](../papers/29420467.md)
- Bladder (n=16) and colorectal (n=12) cohorts produced no RECIST responses, establishing lineage-based resistance to single-agent pan-HER kinase inhibition independent of allele. [PMID:29420467](../papers/29420467.md)
- No responses among 16 [ERBB3](../genes/ERBB3.md)-mutant patients; 95% (70/74) of HER2 mutations were clonal (CCF >0.85 by ABSOLUTE); no subclonal HER2 patient achieved benefit. [PMID:29420467](../papers/29420467.md)
- Concurrent [TP53](../genes/TP53.md) mutation was enriched in non-responders (nominal p=0.018); concurrent [ERBB3](../genes/ERBB3.md) mutation also enriched in non-responders (p=0.064). [PMID:29420467](../papers/29420467.md)
- PI3K/AKT/mTOR activation did NOT adversely affect benefit (p=0.753), diverging from its established negative-predictor role in HER2-amplified breast cancer. [PMID:29420467](../papers/29420467.md)
- 17% (15/86) of centrally profiled patients had concurrent [ERBB2](../genes/ERBB2.md) mutation + amplification; amplification did not correlate with clinical benefit (p=0.50). [PMID:29420467](../papers/29420467.md)
- Grade 3 diarrhoea rate 22% with mandatory prophylaxis; only 2.8% permanently discontinued due to diarrhoea. [PMID:29420467](../papers/29420467.md)

## Sources

- cBioPortal study: `summit_2018`
- ClinicalTrials.gov: NCT01953926
- DOI: [10.1038/nature25475](https://doi.org/10.1038/nature25475)

*This page was processed by **crosslinker** on **2026-05-15**.*
