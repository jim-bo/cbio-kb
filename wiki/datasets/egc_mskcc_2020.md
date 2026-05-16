---
name: MSK Esophagogastric Cancer MSK-IMPACT 2020
studyId: egc_mskcc_2020
institution: Memorial Sloan Kettering Cancer Center
size: 487
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MSK-IMPACT
panels:
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - esophageal-cancer
  - esophagogastric-junction
  - adenocarcinoma
  - targeted-sequencing
  - prognosis
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK Esophagogastric Cancer MSK-IMPACT 2020

## Overview

Prospective genomic cohort of 487 patients with lower esophageal and esophagogastric junction adenocarcinoma ([EGC](../cancer_types/EGC.md) / [ESCA](../cancer_types/ESCA.md)) sequenced with [MSK-IMPACT](../methods/msk-impact-panel.md) at Memorial Sloan Kettering Cancer Center between 2014 and 2019. The study characterized 16 recurrent oncogenic drivers (≥5% prevalence) and linked genomic profiles to overall survival in curative-intent (CIT, N=230) and palliative-intent (PIT, N=257) treatment cohorts. Data are freely available on cBioPortal as `egc_mskcc_2020`.

## Composition

- **Cancer types:** [Esophagogastric carcinoma (EGC)](../cancer_types/EGC.md), [Esophageal carcinoma (ESCA)](../cancer_types/ESCA.md) — lower esophageal and esophagogastric junction adenocarcinomas only
- **N = 487** patients (filtered from 1,029 esophagogastric cases; gastric adenocarcinomas n=473, esophageal squamous n=53, other n=16 excluded)
- **Curative-intent therapy (CIT):** N=230, predominantly stage I–III
- **Palliative-intent therapy (PIT):** N=257, predominantly clinical stage IV
- **Assay versions:** 45 patients on [IMPACT341](../methods/IMPACT341.md), 104 on [IMPACT410](../methods/IMPACT410.md), 338 on [IMPACT468](../methods/IMPACT468.md); all 16 recurrent drivers covered on every version
- **Key clinical fields:** treatment intent, tumor grade, clinical stage, MSI status, prior therapy exposure, [OS](../cancer_types/OS.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — hybridization-capture targeted NGS
- [IMPACT341](../methods/IMPACT341.md), [IMPACT410](../methods/IMPACT410.md), [IMPACT468](../methods/IMPACT468.md)
- [FACETS](../methods/facets.md) — copy-number purity/ploidy correction
- [MSIsensor](../methods/msisensor.md) — MSI calling (cutoff ≥10)
- [OncoKB](../methods/oncokb.md) / [Cancer Hotspots](../methods/cancer-hotspots.md) — variant annotation

## Papers using this cohort

- [PMID:33795256](../papers/33795256.md) — MSK esophagogastric genomic landscape and survival study

## Notable findings derived from this cohort

- 16 recurrent oncogenic drivers (≥5%): 10 were gene amplifications ([ERBB2](../genes/ERBB2.md), [KRAS](../genes/KRAS.md), [CCNE1](../genes/CCNE1.md), [MYC](../genes/MYC.md), [CCND1](../genes/CCND1.md), [MDM2](../genes/MDM2.md), [VEGFA](../genes/VEGFA.md), [EGFR](../genes/EGFR.md), [CDK6](../genes/CDK6.md), [CCND3](../genes/CCND3.md)); [TP53](../genes/TP53.md) mutation present in ~80% of patients in each cohort. [PMID:33795256](../papers/33795256.md)
- [ERBB2](../genes/ERBB2.md) amplification enriched in PIT (30%) vs CIT (13%, p<0.001); independently associated with improved OS (multivariable HR 0.65, 95% CI 0.48–0.90, p=0.009), largely attributable to [trastuzumab](../drugs/trastuzumab.md) therapy (86/108 ERBB2-amplified patients received [trastuzumab](../drugs/trastuzumab.md)). [PMID:33795256](../papers/33795256.md)
- Independent predictors of worse OS on multivariable Cox model: [KRAS](../genes/KRAS.md) amplification (HR 1.83, p<0.001), [SMAD4](../genes/SMAD4.md) alteration (HR 1.61, p=0.007), [CDKN2A](../genes/CDKN2A.md) alteration (HR 1.50, p=0.004). [PMID:33795256](../papers/33795256.md)
- Genomic-instability metrics higher in PIT cohort: median fraction of genome altered 0.50 vs 0.40 (p<0.001); whole-genome doubling rate 46% vs 29% (p<0.001); median oncogenic drivers 3 vs 2 (p=0.001). [PMID:33795256](../papers/33795256.md)
- MSI-high prevalence: 15/487 (3.1%); median TMB 4.5 mutations/Mb overall; TMB negatively correlated with fraction of genome altered (Spearman ρ=0.113, p=0.017). [PMID:33795256](../papers/33795256.md)
- Adding genomic alterations to the clinicopathologic model improved prognostic discrimination (Harrell's C-index 0.68 to 0.71). [PMID:33795256](../papers/33795256.md)
- Median OS: 31.6 months overall; CIT 42.5 months vs PIT 22.8 months (p<0.001); median follow-up 39.2 months. [PMID:33795256](../papers/33795256.md)

## Sources

- cBioPortal study: `egc_mskcc_2020`
- [PMID:33795256](../papers/33795256.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
