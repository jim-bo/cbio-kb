---
symbol: ERBB2
aliases:
  - HER2
  - NEU
cancer_types:
  - EAC
  - MEL
  - IHCH
tags: []
processed_by: crosslinker
processed_at: 2026-05-21
---

# ERBB2

## Overview

ERBB2 (HER2/NEU) is a receptor tyrosine kinase of the ERBB family that lacks a known activating ligand but serves as a preferred dimerization partner for other ERBB family members. ERBB2 amplification is a major oncogenic driver and therapeutic target across multiple cancer types, most prominently breast and gastric/gastroesophageal junction ([GEJ](../cancer_types/GEJ.md)) cancers. HER2-targeted therapies ([trastuzumab](../drugs/trastuzumab.md), [pertuzumab](../drugs/pertuzumab.md), trastuzumab deruxtecan) have established clinical benefit in HER2-amplified tumors.

## Alterations observed in the corpus

- ERBB2 amplification in 108/487 (22%) esophageal/GEJ adenocarcinoma tumors ([egc_mskcc_2020](../datasets/egc_mskcc_2020.md)); enriched in perioperative intent-to-treat (PIT) cohort (30%) vs. curative intent-to-treat (CIT) cohort (13%), p<0.001; 81% of ERBB2-amplified tumors confirmed HER2+ by IHC or FISH; 86/108 received trastuzumab. Associated with longer [OS](../cancer_types/OS.md) (adjusted HR 0.62, p=0.003 univariable; HR 0.65 multivariable, p=0.009) and with well/moderate tumor differentiation (38% vs. 11%, p<0.001). Trended toward mutual exclusivity with [MDM2](../genes/MDM2.md) and other RTK-RAS-PIK3 alterations [PMID:33795256](../papers/33795256.md).
- ERBB2 is an RTK gene in the 28-gene driver list for melanoma ([mel_mskimpact_2020](../datasets/mel_mskimpact_2020.md), n=1,145); appears more often as a co-alteration rather than a standalone driver in this cohort [PMID:33509808](../papers/33509808.md).
- ERBB2 rare amplification in 7 cases of intrahepatic cholangiocarcinoma ([ihch_msk_2021](../datasets/ihch_msk_2021.md), n=412) [PMID:33765338](../papers/33765338.md).
- Recurrent targetable driver mutations and amplifications in [NSCLC](../cancer_types/NSCLC.md) and breast cancer detected by MSK-ACCESS liquid biopsy; included among 10 genes used to assemble the orthogonal-truth accuracy cohort [PMID:34145282](../papers/34145282.md)
- Assessed among targetable [LUAD](../cancer_types/LUAD.md) driver genes (n=9 genes) without significant difference in alteration frequency between pN-positive and pN-negative tumors [PMID:34290393](../papers/34290393.md)
- Mutated in 3.9% of LCINS (all indels); overall survival HR = 5.7 (95% CI 1.6-20.4, P=7.2e-3), partially confounded by [TP53](../genes/TP53.md) co-alteration in 4/7 ERBB2+ tumors [PMID:34493867](../papers/34493867.md)
- ERBB2 amplification is the cohort entry criterion for 733 HER2+ breast tumors; activating mutations (e.g., L755S) found in 7% of metastatic vs 3% of primary samples drive MAPK reactivation and anti-HER2 resistance; MAPK-altered subgroup has HR 2.03 for PFS on first-line anti-HER2 therapy (p=0.023). [PMID:34795269](../papers/34795269.md)
- Amplification more frequent in esophageal cancer patients with lung metastasis (16% primary vs 37% lung met, q<0.001), identifying ERBB2 as a marker of lung-tropic dissemination in esophageal adenocarcinoma [PMID:35120664](../papers/35120664.md)
- ERBB2/3/4 together with [EGFR](../genes/EGFR.md) accounted for ~5% of CNS-tumor oncomap alterations in the MAPPYACTS pediatric relapsed/refractory WES cohort (n=787); investigational ERBB-inhibitor matches were generated. [PMID:35292802](../papers/35292802.md)
- ERBB2 was altered in 16% of MSI-stable esophageal adenocarcinoma ([EAC](../cancer_types/EAC.md)) patients (predominantly amplification) in a neoadjuvant chemoradiotherapy cohort (n=237); alteration was not significantly associated with pathologic treatment response. Ten patients received neoadjuvant trastuzumab based on clinical HER2 status. [PMID:35377946](../papers/35377946.md)

## Cancer types (linked)

- **Esophageal/gastroesophageal junction adenocarcinoma (EAC):** amplification in 22%; independently associated with longer OS (multivariable HR 0.65, p=0.009), enriched in advanced-stage PIT cohort; survival benefit largely attributable to trastuzumab treatment in 86/108 patients; associated with better differentiation and trended mutually exclusive with MDM2/RTK-RAS-PIK3 alterations [PMID:33795256](../papers/33795256.md).
- **Melanoma ([MEL](../cancer_types/MEL.md)):** part of 28-gene RTK driver landscape; appears primarily as a co-alteration in the MSK-IMPACT melanoma cohort [PMID:33509808](../papers/33509808.md).
- **Intrahepatic cholangiocarcinoma ([IHCH](../cancer_types/IHCH.md)):** rare amplification (n=7); not independently prognostic in this cohort [PMID:33765338](../papers/33765338.md).

## Co-occurrence and mutual exclusivity

- Trended toward mutual exclusivity with MDM2 amplification and RTK-RAS-PIK3 alterations in EAC (known mediators of chemo/trastuzumab resistance); not statistically confirmed at q<0.05 in this cohort [PMID:33795256](../papers/33795256.md).
- In melanoma, ERBB2 co-occurs with other RTK-RAS pathway alterations [PMID:33509808](../papers/33509808.md).

## Therapeutic relevance

- trastuzumab (anti-HER2) administered to 86/108 ERBB2-amplified EAC patients (64 first-line, 22 second-line); survival benefit of ERBB2 amplification in EAC cannot be cleanly separated from trastuzumab effect vs. intrinsic biology [PMID:33795256](../papers/33795256.md).
- Authors of EAC study note that mutual exclusivity with MDM2/RTK-RAS-PIK3 alterations may contribute to superior trastuzumab outcomes in ERBB2-amplified tumors, as these co-alterations are known mediators of resistance [PMID:33795256](../papers/33795256.md).

## Open questions

- The survival benefit of ERBB2 amplification in EAC is confounded by trastuzumab treatment; cannot distinguish intrinsic biology from drug effect in this retrospective cohort [PMID:33795256](../papers/33795256.md).
- The frequency and therapeutic relevance of ERBB2 amplification in iCCA beyond the 7 observed cases requires larger studies [PMID:33765338](../papers/33765338.md).

## Sources

- [PMID:33509808](../papers/33509808.md)
- [PMID:33765338](../papers/33765338.md)
- [PMID:33795256](../papers/33795256.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34145282](../papers/34145282.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34290393](../papers/34290393.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34493867](../papers/34493867.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34795269](../papers/34795269.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35120664](../papers/35120664.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35292802](../papers/35292802.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35377946](../papers/35377946.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
