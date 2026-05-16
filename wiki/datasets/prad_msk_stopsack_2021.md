---
name: Race Differences in Prostate Cancer (MSK, 2021)
studyId: prad_msk_stopsack_2021
institution: Memorial Sloan Kettering Cancer Center
size: 2069
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - TARGETED_SEQUENCING
panels:
  - msk-impact-panel
tags:
  - prostate cancer
  - race
  - ancestry
  - MSK-IMPACT
  - disparities
  - AR
  - chromosome 8q
processed_by: crosslinker
processed_at: 2026-05-16
---

# Race Differences in Prostate Cancer (MSK, 2021)

## Overview

prad_msk_stopsack_2021 is a single-institution Memorial Sloan Kettering cohort of 2,069 men with histologically confirmed prostate adenocarcinoma who received clinical-grade MSK-IMPACT tumor–normal sequencing (1,841 self-reported White, 165 Black, 63 Asian). The study examines somatic genomic differences by self-reported race and genetic ancestry (inferred from 5,072 1KGP SNPs via ADMIXTURE), adjusting for age, PSA, disease extent, stage, and sample type. Reference genome: hg19.

## Composition

- Cancer type: [PRAD](../cancer_types/PRAD.md) (prostate adenocarcinoma)
- 2,069 men: 1,841 self-reported White, 165 Black, 63 Asian
- 1,781 (86%) consented to germline analysis
- Sequencing: [MSK-IMPACT](../methods/msk-impact-panel.md), 341–468 gene versions ([IMPACT341](../methods/IMPACT341.md), [IMPACT410](../methods/IMPACT410.md), [IMPACT468](../methods/IMPACT468.md))
- Arm-level CNAs by [ASCETS](../methods/ascets.md); OncoKB annotation v2.8; ancestry inference by [ADMIXTURE](../methods/admixture.md) v1.3

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — multiple panel versions capturing SNVs, indels, CNAs, and rearrangements

## Papers using this cohort

- [PMID:34667026](../papers/34667026.md) — Stopsack et al., Clin Cancer Res 2022: Race differences in somatic tumor genomics of prostate cancer

## Notable findings derived from this cohort

- [AR](../genes/AR.md) alterations were enriched in Black men (18%) vs White men (12%) after clinical-feature adjustment (+5 pp, 95% CI 1–8); [FOXA1](../genes/FOXA1.md) class-1 forkhead-domain mutations enriched in Asian men (21% vs 8% White); [TP53](../genes/TP53.md) alterations less common in Black men (19% vs 30%), driven by fewer missense mutations [PMID:34667026](../papers/34667026.md)
- Chr8q gain present in 49% of Black, 47% of Asian, and 37% of White tumors; Black–White difference (11 pp) persisted after adjustment and was prognostic for [OS](../cancer_types/OS.md) (HR 2.00, 95% CI 1.00–4.01 in Black men); area-level household income was an independent predictor of chr8q gain [PMID:34667026](../papers/34667026.md)
- No difference in DNA-repair gene alteration frequency by race ([BRCA1](../genes/BRCA1.md), [BRCA2](../genes/BRCA2.md), [ATM](../genes/ATM.md), [ATR](../genes/ATR.md), [MSH2](../genes/MSH2.md), [MSH6](../genes/MSH6.md), [POLE](../genes/POLE.md), etc.); germline contribution was minimal (≤1 germline mutation per race-associated gene across 1,781 consented patients) [PMID:34667026](../papers/34667026.md)

## Sources

- cBioPortal study: `https://www.cbioportal.org/study/summary?id=prad_msk_stopsack_2021`
- Citation: Stopsack et al., Clin Cancer Res 2022, [PMID:34667026](../papers/34667026.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
