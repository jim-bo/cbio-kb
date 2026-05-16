---
name: MAPK on resistance to anti-HER2 therapy for breast cancer (MSK, Nat Commun 2022)
studyId: brca_mapk_hp_msk_2021
institution: Memorial Sloan Kettering Cancer Center
size: 733
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - TARGETED_SEQUENCING
panels:
  - msk-impact-panel
tags:
  - breast cancer
  - HER2+
  - MAPK
  - NF1
  - anti-HER2 resistance
  - MSK-IMPACT
  - metastatic
processed_by: crosslinker
processed_at: 2026-05-16
---

# MAPK on resistance to anti-HER2 therapy for breast cancer (MSK, Nat Commun 2022)

## Overview

brca_mapk_hp_msk_2021 is a Memorial Sloan Kettering cohort of 733 ERBB2-amplified primary and metastatic breast cancers from 664 patients with HER2+ disease, prospectively sequenced by MSK-IMPACT between April 2014 and February 2021 under IRB protocol NCT01775072. The dataset comprises 385 metastatic and 348 primary samples and was used to characterise somatic MAPK-pathway alterations that drive resistance to anti-HER2 therapy. A nested PFS-analysis cohort of 145 patients received first-line trastuzumab/pertuzumab-based therapy with pre-treatment sequencing. Reference genome: hg19.

## Composition

- Cancer type: [BRCA](../cancer_types/BRCA.md) (HER2-amplified; [ERBB2](../genes/ERBB2.md) amplification is the entry criterion)
- 733 samples (385 metastatic, 348 primary) from 664 patients
- Sequencing: [MSK-IMPACT](../methods/msk-impact-panel.md) hybridization-capture NGS (341–505 genes; ~663× average coverage)
- Copy number: [FACETS](../methods/facets.md); mutation annotation: [OncoKB](../methods/oncokb-annotation.md)
- Nested PFS cohort: 145 patients receiving first-line THP ([docetaxel](../drugs/docetaxel.md) + [trastuzumab](../drugs/trastuzumab.md) + [pertuzumab](../drugs/pertuzumab.md))

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — targeted panel NGS capturing SNVs, indels, CNAs, and rearrangements

## Papers using this cohort

- [PMID:34795269](../papers/34795269.md) — Smith et al., Nature Communications 2022: HER2+ breast cancers evade anti-HER2 therapy via a switch in driver pathway

## Notable findings derived from this cohort

- [NF1](../genes/NF1.md) biallelic loss in 8% of metastatic vs 4% of primary HER2+ tumors; ERBB2 activating mutations in 7% vs 3%; MAPK alterations were significantly enriched in metastatic samples (p = 0.020) [PMID:34795269](../papers/34795269.md)
- In 145 first-line THP-treated patients, MAPK-altered tumors had median PFS 9.9 months vs 21 months for MAPK-WT (HR 2.03, 95% CI 1.18–3.51, multivariate p = 0.011); effect independent of PI3K-pathway alterations ([PIK3CA](../genes/PIK3CA.md) 30%, [PTEN](../genes/PTEN.md) 2.6%, [AKT1](../genes/AKT1.md) 0.3%) [PMID:34795269](../papers/34795269.md)

## Sources

- cBioPortal study: `https://www.cbioportal.org/study/summary?id=brca_mapk_hp_msk_2021`
- Citation: Smith AE et al., Nature Communications 2022, [PMID:34795269](../papers/34795269.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
