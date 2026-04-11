---
name: "Hepatocellular Carcinoma cfDNA (MSK, JCO Precision Oncology 2023)"
slug: hcc_jcopo_msk_2023
institution: Memorial Sloan Kettering Cancer Center
size: 51
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [ctdna, targeted-panel]
panels: []
tags:
  - hepatocellular-carcinoma
  - hcc
  - cfdna
  - msk-access
  - liquid-biopsy
processed_by: crosslinker
processed_at: 2026-04-11
---

# Hepatocellular Carcinoma cfDNA (MSK, JCO Precision Oncology 2023)

## Overview

Single-center cohort of 51 patients with histologically confirmed advanced hepatocellular carcinoma ([HCC](../cancer_types/HCC.md)) at Memorial Sloan Kettering Cancer Center (February 2019 – August 2021), profiling circulating cell-free DNA (cfDNA) using [MSK-ACCESS](../methods/ACCESS129.md). Matched tumor tissue [MSK-IMPACT](../methods/msk-impact-panel.md) data available for 37 patients (72.5%). Data deposited in cBioPortal as `hcc_jcopo_msk_2023`. [PMID:37769223](../papers/37769223.md)

## Composition

- 53 plasma samples from 51 patients with inoperable advanced [HCC](../cancer_types/HCC.md); AJCC stage IV (74%), III (18%), II (8%). [PMID:37769223](../papers/37769223.md)
- Median age 69 years; 76% male; 47% hepatitis B/C etiology, 53% non-viral. [PMID:37769223](../papers/37769223.md)
- 47% treatment-naive at cfDNA collection; 35% prior TKI; 18% prior anti-PD-1/PD-L1. [PMID:37769223](../papers/37769223.md)

## Assays / panels (linked)

- [MSK-ACCESS](../methods/ACCESS129.md) 129-gene plasma panel (~200,000x raw coverage with error suppression). [PMID:37769223](../papers/37769223.md)
- [MSK-IMPACT](../methods/msk-impact-panel.md) for matched tumor tissue in 37 patients. [PMID:37769223](../papers/37769223.md)
- Variant annotation via [OncoKB](../methods/oncokb.md). [PMID:37769223](../papers/37769223.md)

## Papers using this cohort

- [PMID:37769223](../papers/37769223.md) — Targeted Molecular Profiling of Circulating Cell-Free DNA in Patients With Advanced Hepatocellular Carcinoma.

## Notable findings derived from this cohort

- Genomic alterations detected in 90.6% of plasma samples. Median cfDNA yield 39.43 ng; median VAF 0.027. [PMID:37769223](../papers/37769223.md)
- Top cfDNA mutation frequencies: [TERT](../genes/TERT.md) promoter 57%, [TP53](../genes/TP53.md) 47%, [CTNNB1](../genes/CTNNB1.md) 37%, [ARID1A](../genes/ARID1A.md) 18%, [TSC2](../genes/TSC2.md) 14%. [PMID:37769223](../papers/37769223.md)
- cfDNA detected 92.5% of alterations previously called in matched tumor tissue; cfDNA-exclusive alterations found in 27% of paired samples, 40% of which were OncoKB level 3b actionable. [PMID:37769223](../papers/37769223.md)
- [TP53](../genes/TP53.md) significantly more prevalent in cfDNA vs. published tissue cohort (51% vs. 32%, P=0.024). [PMID:37769223](../papers/37769223.md)

## Sources

- cBioPortal study `hcc_jcopo_msk_2023` [PMID:37769223](../papers/37769223.md).

*This page was processed by **crosslinker** on **2026-04-11**.*
