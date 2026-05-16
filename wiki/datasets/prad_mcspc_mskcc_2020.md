---
name: MSK Metastatic Castration-Sensitive Prostate Cancer (Stopsack et al. 2020)
studyId: prad_mcspc_mskcc_2020
institution: Memorial Sloan Kettering Cancer Center
size: 424
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
panels:
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - prostate-cancer
  - metastatic
  - castration-sensitive
  - mCSPC
  - MSK-IMPACT
  - prognostic
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK Metastatic Castration-Sensitive Prostate Cancer (Stopsack et al. 2020)

## Overview

Prospective tumor–blood sequencing cohort of 424 patients with metastatic castration-sensitive prostate cancer (mCSPC) from Memorial Sloan Kettering Cancer Center, sequenced by the [MSK-IMPACT panel](../methods/msk-impact-panel.md) between May 2015 and September 2018. The study was designed to characterize the genomic landscape of mCSPC, identify alterations discriminating disease phenotypes (high- vs. low-volume; de-novo metastatic vs. metastatic recurrence), and evaluate which somatic alterations predict castration resistance and overall survival. [PMID:32220891](../papers/32220891.md)

## Composition

- 424 patients with metastatic castration-sensitive [prostate adenocarcinoma](../cancer_types/PRAD.md); median age at sampling 65.6 years (IQR 59.0–71.8); 88% white.
- Disease-volume split: 213 (50%) high-volume, 211 (50%) low-volume (modified criteria: visceral mets or ≥4 bone mets, no extra-axial requirement).
- Timing split: 275 (65%) de-novo metastatic, 149 (35%) metastatic recurrence.
- Sample tissue: prostate 204 (48%), lymph node 93 (22%), bone 61 (14%), lung 26 (6%), other soft tissue 25 (6%), liver 15 (4%).
- Median follow-up: 27.2 months for castration resistance, 30.5 months for overall survival. [PMID:32220891](../papers/32220891.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — FDA-authorized hybridization-capture panel (341–468 genes depending on version); paired tumor–blood design.
- Copy-number analysis by [FACETS](../methods/facets.md); tumor purity ≤20% excluded (6.7% of cases).
- Actionability annotated by [OncoKB](../methods/oncokb-annotation.md) (Aug 1, 2019). [PMID:32220891](../papers/32220891.md)

## Papers using this cohort

- [PMID:32220891](../papers/32220891.md) — Stopsack et al., genomic landscape and prognostic genomic features of mCSPC; [AR](../genes/AR.md), [TP53](../genes/TP53.md), cell-cycle, [MYC](../genes/MYC.md), [SPOP](../genes/SPOP.md), and WNT pathway alterations identified as prognostically significant.

## Notable findings derived from this cohort

- Median TMB 2.6 mut/Mb (IQR 1.8–4.4); median fraction genome altered 32% (IQR 24–48); high-volume disease had 4.6 pp higher mean [FGA](../genes/FGA.md) (95% CI 1.5–7.7). [PMID:32220891](../papers/32220891.md)
- 50% (211/424) of tumors carried at least one potentially actionable alteration per OncoKB. [PMID:32220891](../papers/32220891.md)
- [AR](../genes/AR.md) and [TP53](../genes/TP53.md) alterations and cell-cycle / MYC pathway alterations were associated with 1.6- to 5-fold higher castration-resistance rates; [SPOP](../genes/SPOP.md) and WNT pathway alterations associated with ~1.5-fold lower rates (multivariable models). [PMID:32220891](../papers/32220891.md)
- [CDK12](../genes/CDK12.md) alterations were 6.7 pp more frequent in de-novo metastatic disease vs. metastatic recurrence (95% CI 3.0–10.4; FDR 0.037) — the only single gene with statistically significant phenotype discrimination. [PMID:32220891](../papers/32220891.md)
- High-volume disease had significantly higher castration-resistance incidence (139/213 vs. 101/211; adjusted HR 1.84, 95% CI 1.40–2.41) and more deaths (77 vs. 25; adjusted HR 3.71, 95% CI 2.28–6.02). [PMID:32220891](../papers/32220891.md)
- PI3K/RAS/RAF/MAPK/DNA-repair pathway alterations were not prognostic for castration resistance or [OS](../cancer_types/OS.md) after multivariable adjustment; [PTEN](../genes/PTEN.md) only prognostic in unadjusted analyses. [PMID:32220891](../papers/32220891.md)

## Sources

- [PMID:32220891](../papers/32220891.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
