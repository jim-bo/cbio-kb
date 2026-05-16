---
name: MSK Gallbladder Cancer Multi-Regional IMPACT Cohort (2018)
studyId: gbc_msk_2018
institution: Memorial Sloan Kettering Cancer Center / Arturo Lopez Perez Foundation (Chile) / Yokohama City University (Japan)
size: 81
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
panels:
  - IMPACT341
  - IMPACT410
tags:
  - gallbladder-cancer
  - GBC
  - biliary-tract
  - regional-differences
  - smad4
  - actionable-alterations
  - international-cohort
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK Gallbladder Cancer Multi-Regional IMPACT Cohort (2018)

## Overview

An 81-patient, three-center, multi-regional cohort of primary gallbladder cancer (GBCA) tumors from the United States (MSKCC, n=49), Chile (Arturo Lopez Perez Foundation Cancer Institute, n=21), and Japan (Yokohama City University, n=11), collected between September 1999 and March 2016. Paired tumor/normal DNA was sequenced with the MSK-IMPACT targeted NGS assay (341–410 genes). The cohort was designed to assess regional differences in GBCA mutational landscape and identify convergent prognostic biomarkers. Data are deposited on cBioPortal. [PMID:30427539](../papers/30427539.md)

## Composition

- **81 patients** with primary [GBC](../cancer_types/GBC.md); adenocarcinoma and adenosquamous histologies only (14 metastatic-only and 6 other histologies excluded). [PMID:30427539](../papers/30427539.md)
- **By site:** 49 MSK (United States), 21 Arturo Lopez Perez (Chile), 11 Yokohama City University (Japan). [PMID:30427539](../papers/30427539.md)
- **Assay:** [MSK-IMPACT](../methods/msk-impact-panel.md) hybridization-capture targeted NGS; paired tumor + normal; [IMPACT341](../methods/IMPACT341.md) and [IMPACT410](../methods/IMPACT410.md) panel versions (1.2 Mb and 1.38 Mb). Mutation burden normalized by panel size. [PMID:30427539](../papers/30427539.md)
- **Reference genome:** GRCh37
- **Actionability annotation:** [OncoKB](../methods/oncokb-annotation.md)
- **Survival analysis:** [Kaplan-Meier](../methods/kaplan-meier.md) and [Cox proportional-hazards](../methods/cox-proportional-hazards.md)

## Assays / panels (linked)

- [msk-impact-panel](../methods/msk-impact-panel.md)
- [IMPACT341](../methods/IMPACT341.md)
- [IMPACT410](../methods/IMPACT410.md)

## Papers using this cohort

- [PMID:30427539](../papers/30427539.md) — Narayan et al. 2019, "Regional Differences in Gallbladder Cancer Pathogenesis: Insights From a Multi-Institutional Comparison of Tumor Mutations," *Cancer*

## Notable findings derived from this cohort

- **Most commonly mutated genes:** [TP53](../genes/TP53.md) 58% (47/81), [SMAD4](../genes/SMAD4.md) 31% (25/81), [ARID1A](../genes/ARID1A.md) 25% (20/81), [ATM](../genes/ATM.md) 19%, [CDKN2A](../genes/CDKN2A.md) 15%, [TERT](../genes/TERT.md) 12%, [PIK3CA](../genes/PIK3CA.md) 12%, [BRCA2](../genes/BRCA2.md) 10%. [PMID:30427539](../papers/30427539.md)
- **Regional mutation burden:** Chile median 7 mutations/Mb, Japan 6, United States 4 (P-adj=0.006). [PMID:30427539](../papers/30427539.md)
- **[SMAD4](../genes/SMAD4.md) prognosis:** mutated in ~31% across all three regions; independently associated with worse overall survival (HR 2.01, 95% CI 1.02–3.94; p=0.043) in multivariable Cox analysis adjusting for stage, gallstone status, and sex. Median [OS](../cancer_types/OS.md) 10.4 vs. 24.8 months (P-adj=0.039). [PMID:30427539](../papers/30427539.md)
- **Regional absence patterns:** [ARID1A](../genes/ARID1A.md) and [PIK3CA](../genes/PIK3CA.md) mutations were entirely absent in the Japanese cohort; [ERBB3](../genes/ERBB3.md) and [ARID2](../genes/ARID2.md) mutations were absent in Chilean patients. [PMID:30427539](../papers/30427539.md)
- **Actionable targets:** 80% of patients carried at least one mutation in a potentially actionable gene target per OncoKB or prior literature; p53 pathway altered in 73% and RTK-RAS pathway in 44%. [PMID:30427539](../papers/30427539.md)
- **Post-resection survival (n=46):** median OS 19.6 months (95% CI 14.5–28.8); 5-year survival 18% (95% CI 8–31%). [PMID:30427539](../papers/30427539.md)

## Sources

- cBioPortal study ID: `gbc_msk_2018`
- [PMID:30427539](../papers/30427539.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
