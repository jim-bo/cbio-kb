---
name: MSK Intrahepatic Cholangiocarcinoma IMPACT 2021
studyId: ihch_msk_2021
institution: Memorial Sloan Kettering Cancer Center / Erasmus MC
size: 412
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
  - cholangiocarcinoma
  - intrahepatic
  - targeted-sequencing
  - prognosis
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK Intrahepatic Cholangiocarcinoma IMPACT 2021

## Overview

Bi-institutional retrospective cohort of 412 patients with histologically confirmed intrahepatic cholangiocarcinoma (iCCA) profiled by [MSK-IMPACT](../methods/msk-impact-panel.md) targeted NGS at Memorial Sloan Kettering Cancer Center (n=390; resected 1993–2018, unresected 2008–2019) and Erasmus MC (n=22; resected 2005–2015). The study linked genomic profiles to overall survival in resected (n=209) and unresected (n=203) cohorts, identifying [TP53](../genes/TP53.md), [KRAS](../genes/KRAS.md), and [CDKN2A](../genes/CDKN2A.md) as independent prognostic biomarkers. Data are deposited on cBioPortal as `ihch_msk_2021`.

## Composition

- **Cancer type:** [Intrahepatic Cholangiocarcinoma (IHCH)](../cancer_types/IHCH.md)
- **N = 412** patients: 390 MSKCC + 22 Erasmus MC
- **Resected cohort:** n=209 (median RFS 18.4 months, median [OS](../cancer_types/OS.md) 46.4 months)
- **Unresectable cohort:** n=203 (locally advanced 24.1 months OS; distant metastases 13.1 months OS)
- **Assay versions:** 40 samples on [IMPACT341](../methods/IMPACT341.md), 147 on [IMPACT410](../methods/IMPACT410.md), 225 on [IMPACT468](../methods/IMPACT468.md); all against matched normal liver or blood, tumor content >60%
- **Key clinical fields:** resection status, lymph node status, multifocal liver disease, large bile duct type, periductal infiltration, lymphovascular invasion, etiology (cirrhosis, PSC)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — hybridization-capture targeted NGS
- [IMPACT341](../methods/IMPACT341.md), [IMPACT410](../methods/IMPACT410.md), [IMPACT468](../methods/IMPACT468.md)
- [OncoKB](../methods/oncokb-annotation.md) — oncogenicity annotation
- [Cox proportional-hazards regression](../methods/cox-proportional-hazards.md), [Kaplan-Meier estimates](../methods/kaplan-meier.md)

## Papers using this cohort

- [PMID:33765338](../papers/33765338.md) — MSK iCCA genomic prognostication study

## Notable findings derived from this cohort

- 1,551 genetic alterations across 412 tumors; most frequent oncogenic events: [IDH1](../genes/IDH1.md) 20%, [ARID1A](../genes/ARID1A.md) 20%, [TP53](../genes/TP53.md) 17%, [CDKN2A](../genes/CDKN2A.md) 15% (homozygous deletions 13%), [BAP1](../genes/BAP1.md) 15%, [FGFR2](../genes/FGFR2.md) 15% (fusions 11%), [PBRM1](../genes/PBRM1.md) 12%, [KRAS](../genes/KRAS.md) 10%. [PMID:33765338](../papers/33765338.md)
- [TP53](../genes/TP53.md) mutation (HR 1.82 resected, independent), [CDKN2A](../genes/CDKN2A.md) homozygous deletion (HR 3.40 resected, strongest effect), and [KRAS](../genes/KRAS.md) mutation were independent predictors of shorter OS; [IDH1/2](../genes/IDH1.md) mutations and [FGFR2](../genes/FGFR2.md) fusions were not prognostic. [PMID:33765338](../papers/33765338.md)
- [IDH1/2](../genes/IDH1.md) mutations were significantly mutually exclusive with [FGFR2](../genes/FGFR2.md) fusions (τ=−0.19, Q=0.002), [CDKN2A](../genes/CDKN2A.md) deletions, [TP53](../genes/TP53.md) mutations, and RTK/RAS pathway alterations. [PMID:33765338](../papers/33765338.md)
- Patients with both clinical high-risk features and [CDKN2A](../genes/CDKN2A.md) deep deletion had median OS 12.2 months (resected) vs 16.8 months (locally advanced unresected), suggesting no benefit from surgery in this subgroup. [PMID:33765338](../papers/33765338.md)
- Median TMB 2.6 mut/Mb (IQR 1.8–3.9); only 2 patients MSI-consistent (TMB >40); epigenetic regulator pathway altered in 60%, RTK/RAS in 48%. [PMID:33765338](../papers/33765338.md)
- Hepatic arterial infusion chemotherapy ([floxuridine](../drugs/floxuridine.md)) independently associated with improved OS in locally advanced unresectable disease (HR 0.45, 95% CI 0.27–0.77, P=0.003). [PMID:33765338](../papers/33765338.md)

## Sources

- cBioPortal study: `ihch_msk_2021`
- [PMID:33765338](../papers/33765338.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
