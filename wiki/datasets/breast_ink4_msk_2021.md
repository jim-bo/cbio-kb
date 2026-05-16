---
name: Metastatic Breast Cancer — INK4/CDK4-6 Resistance (MSK, Cancer Discovery 2022)
studyId: breast_ink4_msk_2021
institution: Memorial Sloan Kettering Cancer Center
size: 1366
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - TARGETED_SEQUENCING
panels:
  - msk-impact-panel
tags:
  - breast cancer
  - HR+/HER2-
  - CDK4/6 inhibitor resistance
  - INK4
  - MSK-IMPACT
  - metastatic
processed_by: crosslinker
processed_at: 2026-05-16
---

# Metastatic Breast Cancer — INK4/CDK4-6 Resistance (MSK, Cancer Discovery 2022)

## Overview

breast_ink4_msk_2021 is a Memorial Sloan Kettering cohort of 1,366 metastatic tumors from 1,115 patients with HR+/HER2− metastatic breast cancer, prospectively sequenced by MSK-IMPACT between April 2014 and March 2020 under IRB protocol NCT01775072. The study was designed to characterise the genomic landscape of CDK4/6 inhibitor resistance, with particular focus on alterations in the CDK6/INK4 axis ([FAT1](../genes/FAT1.md), [PTEN](../genes/PTEN.md), [ARID1A](../genes/ARID1A.md), LATS1/2, [YAP1](../genes/YAP1.md), [CDK6](../genes/CDK6.md), [CDKN2A](../genes/CDKN2A.md), [RB1](../genes/RB1.md)). Reference genome: hg19.

## Composition

- Cancer type: [BRCA](../cancer_types/BRCA.md) (HR+/HER2− metastatic breast cancer)
- 1,366 tumor samples from 1,115 unique patients; multiple metastatic biopsies per patient are included
- Sequencing by [MSK-IMPACT](../methods/msk-impact-panel.md) targeted hybridization-capture NGS panel (341–468 cancer genes)
- 190/1,115 patients (17%) carry at least one alteration in a CDK6/INK4-axis gene

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — targeted panel NGS capturing SNVs, indels, CNAs, and rearrangements across 341–468 cancer-associated genes

## Papers using this cohort

- [PMID:34544752](../papers/34544752.md) — Li et al., Cancer Discovery 2022: INK4 tumor suppressor proteins mediate resistance to CDK4/6 kinase inhibitors

## Notable findings derived from this cohort

- 190/1,115 (17%) HR+/HER2− metastatic breast cancer patients carry at least one CDK6-axis alteration (FAT1 1.6%, PTEN 8%, ARID1A 8%, RB1 4%, [LATS1](../genes/LATS1.md) 0.5%, [LATS2](../genes/LATS2.md) 0.8%, YAP1 0.5%, CDK6 0.4%); these are hypothesised to confer intrinsic or early resistance to ATP-competitive CDK4/6i [PMID:34544752](../papers/34544752.md)

## Sources

- cBioPortal study: `https://www.cbioportal.org/study/summary?id=breast_ink4_msk_2021`
- Citation: Qing Li et al., Cancer Discovery 2022, [PMID:34544752](../papers/34544752.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
