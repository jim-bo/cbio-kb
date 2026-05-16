---
name: MSK Alpelisib + Aromatase Inhibitor Phase I/II Cohort (2020)
studyId: breast_alpelisib_2020
institution: Memorial Sloan Kettering Cancer Center
size: 51
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
  - liquid-biopsy
panels:
  - msk-impact-panel
  - guardant360
tags:
  - breast-cancer
  - hr-positive
  - metastatic
  - pi3k-inhibitor
  - aromatase-inhibitor
  - ctdna
  - resistance
  - phase-1-2-trial
  - NCT01870505
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK Alpelisib + Aromatase Inhibitor Phase I/II Cohort (2020)

## Overview

The breast_alpelisib_2020 cohort is a prospective single-institution phase I/II dose-escalation trial cohort (NCT01870505) of the PI3Kα-selective inhibitor [alpelisib](../drugs/alpelisib.md) combined with an aromatase inhibitor ([letrozole](../drugs/letrozole.md) or [exemestane](../drugs/exemestane.md)) in patients with hormone-receptor-positive (HR+) metastatic breast cancer ([BRCA](../cancer_types/BRCA.md)). The dataset includes prospective somatic mutational data from both tumor tissue (MSK-IMPACT) and serial ctDNA (Guardant360) deposited in cBioPortal. Data lock was April 30, 2018. [PMID:32864625](../papers/32864625.md)

## Composition

- **n = 51** patients enrolled June 2013 – September 2015 across four arms: Arm A (n=7, continuous [alpelisib](../drugs/alpelisib.md) + [letrozole](../drugs/letrozole.md)), Arm B (n=7, continuous alpelisib + [exemestane](../drugs/exemestane.md)), Arm C (n=12, intermittent 7-on/7-off alpelisib + letrozole), Arm D (n=25, intermittent 5-on/2-off alpelisib + exemestane).
- Median age 58 (range 28–83); all HR+, HER2 non-amplified; 69% visceral disease, 31% bone-only; 88% with ≥1 prior line endocrine therapy for metastatic disease.
- Tissue sequencing: [MSK-IMPACT](../methods/msk-impact-panel.md) on n=39 baseline tumors; Foundation Medicine NGS on n=2; [Sequenom](../methods/sequenom-genotyping.md) hotspot panel on n=9.
- ctDNA: 73-gene [Guardant360](../methods/guardant360.md) cfDNA panel on 90 pre-/on-/post-treatment plasma samples from 47 patients, including 32 paired pre/post pairs.
- Copy-number analysis by [FACETS](../methods/facets.md); mutational signatures by [deconstructSigs](../methods/deconstructsigs.md). [PMID:32864625](../papers/32864625.md)

## Assays / panels (linked)

- [MSK-IMPACT panel](../methods/msk-impact-panel.md) — tumor tissue targeted NGS at baseline.
- [Guardant360](../methods/guardant360.md) — 73-gene ctDNA panel for longitudinal liquid biopsy monitoring.
- [FACETS](../methods/facets.md) — allele-specific copy-number and cancer cell fraction analysis.
- [deconstructSigs](../methods/deconstructsigs.md) — APOBEC and other mutational signature decomposition.

## Papers using this cohort

- [PMID:32864625](../papers/32864625.md) — Razavi et al. (2020): [PTEN](../genes/PTEN.md) loss (25% of paired-ctDNA patients) and [ESR1](../genes/ESR1.md) mutations are recurrent mechanisms of resistance to alpelisib + aromatase inhibitor; CBR 52% (23/44) among evaluable HR+ [MBC](../cancer_types/MBC.md) patients.

## Notable findings derived from this cohort

- Clinical benefit rate (CBR: CR + PR + SD ≥16 weeks) among 44 evaluable patients was 52% (23/44; 95% CI 37–68%); overall response rate among 31 with measurable disease was 19% (6/31). [PMID:32864625](../papers/32864625.md)
- Clinical benefit was confined to [PIK3CA](../genes/PIK3CA.md)-mutant tumors: CBR 57.5% (23/40) in PIK3CA-mutant vs. 0/6 in PIK3CA-WT (p=0.025). [PMID:32864625](../papers/32864625.md)
- Baseline activating [ESR1](../genes/ESR1.md) mutations (D538G or Y537S) were present in 6 patients, all of whom had no clinical benefit (p=0.0067). [PMID:32864625](../papers/32864625.md)
- [PTEN](../genes/PTEN.md) loss-of-function alterations found in 25% (8/32) of paired-ctDNA patients: 3 pre-existing (intrinsic resistance), 5 emergent on therapy (acquired resistance). [PMID:32864625](../papers/32864625.md)
- Combined PTEN loss + ESR1 mutations present in ~47% (15/32) of paired-ctDNA patients and associated with progression. [PMID:32864625](../papers/32864625.md)
- MAPK pathway alterations ([ERBB2](../genes/ERBB2.md), [HRAS](../genes/HRAS.md), [NF1](../genes/NF1.md), [BRAF](../genes/BRAF.md), [MAP2K1](../genes/MAP2K1.md)) selectively expanded in post-treatment ctDNA, indicating bypass resistance pathways. [PMID:32864625](../papers/32864625.md)

## Sources

- cBioPortal study `breast_alpelisib_2020`.
- Razavi et al. (2020) *Nature Cancer* [PMID:32864625](../papers/32864625.md).

*This page was processed by **crosslinker** on **2026-05-16**.*
