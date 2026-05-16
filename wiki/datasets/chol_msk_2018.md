---
name: MSK Cholangiocarcinoma IMPACT Cohort (2018)
studyId: chol_msk_2018
institution: Memorial Sloan Kettering Cancer Center
size: 195
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
  - STRUCTURAL_VARIANT
panels:
  - IMPACT341
  - IMPACT410
tags:
  - cholangiocarcinoma
  - chol
  - msk-impact
  - targeted-ngs
  - intrahepatic
  - extrahepatic
  - prospective
  - oncokb
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK Cholangiocarcinoma IMPACT Cohort (2018)

## Overview

Prospective targeted sequencing cohort of 195 patients with cholangiocarcinoma at Memorial Sloan Kettering Cancer Center, consented under clinical protocol NCT01775072 over a two-year period starting July 2014. All patients were profiled with the [MSK-IMPACT](../methods/msk-impact-panel.md) panel covering 341 or 410 cancer-associated genes. The cohort spans intrahepatic cholangiocarcinoma (IHC, n=158, 81%) and extrahepatic cholangiocarcinoma (EHC, n=37, 19%). Actionable alterations were classified using [OncoKB](../methods/oncokb-annotation.md) levels 1–4. 91% sequencing success rate (195/214 attempted).

## Composition

- **n = 195 patients** with cholangiocarcinoma; 158 (81%) intrahepatic ([IHCH](../cancer_types/IHCH.md)), 37 (19%) extrahepatic ([EHCH](../cancer_types/EHCH.md)).
- 141 (72%) primary tumor biopsy/resection; 54 (27%) biopsy of metastatic site; all archival FFPE tissue.
- Demographics: 51.8% male; median age 62 (range 24–86); 89% Caucasian; 12% (n=24) with hepatitis B.
- Outcome: 158 patients (81%) received first-line chemotherapy for advanced disease; 127/158 (80%) on gemcitabine/platinum. Median time to progression on first-line chemotherapy 8.8 months. Survival analyzed in 178 stage IV patients.

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) targeted DNA sequencing: [IMPACT341](../methods/IMPACT341.md) (n=20 samples) or [IMPACT410](../methods/IMPACT410.md) (n=318 samples). Median sample coverage 759X; matched germline DNA from blood for somatic calling.
- Structural variant detection integrated in the IMPACT panel design.
- Actionability annotation by [OncoKB](../methods/oncokb-annotation.md) levels 1–4.
- MSI-H detection by [MSIsensor](../methods/msisensor.md).

## Papers using this cohort

- [PMID:29848569](../papers/29848569.md) — Lowery et al. 2018, Annals of Oncology — "Comprehensive molecular profiling of intrahepatic and extrahepatic cholangiocarcinomas: potential targets for intervention."

## Notable findings derived from this cohort

- Most commonly altered genes in IHC: [IDH1](../genes/IDH1.md) (30%), [ARID1A](../genes/ARID1A.md) (23%), [BAP1](../genes/BAP1.md) (20%), [TP53](../genes/TP53.md) (20%), [FGFR2](../genes/FGFR2.md) fusions (14%); in EHC: [KRAS](../genes/KRAS.md), [SMAD4](../genes/SMAD4.md), [TP53](../genes/TP53.md), and [STK11](../genes/STK11.md) were enriched [PMID:29848569](../papers/29848569.md).
- [BAP1](../genes/BAP1.md) mutations and [FGFR2](../genes/FGFR2.md) fusions were observed exclusively in IHC; 38 structural alterations in 35 patients (18%), predominantly in-frame [FGFR2](../genes/FGFR2.md) fusions [PMID:29848569](../papers/29848569.md).
- 47.6% (93/195) of patients had at least one OncoKB level 3B or higher actionable alteration; 16% of advanced-disease patients received biomarker-matched therapy, with 64% showing evidence of response or clinical benefit [PMID:29848569](../papers/29848569.md).
- [CDKN2A](../genes/CDKN2A.md)/[CDKN2B](../genes/CDKN2B.md) deletions (8%) and [ERBB2](../genes/ERBB2.md) amplifications (4%) were associated with significantly shorter overall survival (p=0.0015 for both) and shorter time to progression on first-line chemotherapy [PMID:29848569](../papers/29848569.md).
- [KRAS](../genes/KRAS.md) mutations (enriched in EHC, 38% vs 7% in IHC) were associated with shorter [OS](../cancer_types/OS.md) in advanced disease (p=0.026) [PMID:29848569](../papers/29848569.md).
- MSI-H in 0.5% of cohort (single tumor), with [MLH1](../genes/MLH1.md) and [MSH6](../genes/MSH6.md) protein loss on IHC [PMID:29848569](../papers/29848569.md).

## Sources

- Lowery MA et al. "Comprehensive molecular profiling of intrahepatic and extrahepatic cholangiocarcinomas: potential targets for intervention." Clinical Cancer Research. 2018;24(17):4154-4161. [PMID:29848569](../papers/29848569.md). DOI: 10.1158/1078-0432.CCR-18-0040.
- Clinical trial: NCT01775072 (MSK IMPACT prospective consent protocol).

*This page was processed by **crosslinker** on **2026-05-16**.*
