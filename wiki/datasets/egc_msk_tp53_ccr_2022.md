---
name: "Esophageal/GEJ Adenocarcinoma MSK TP53 Pathway (MSK, CCR 2022)"
studyId: egc_msk_tp53_ccr_2022
institution: Memorial Sloan Kettering Cancer Center
size: 237
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - msk-impact-panel
  - facets
  - msisensor
  - oncokb-annotation
panels:
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - esophageal-adenocarcinoma
  - neoadjuvant-therapy
  - treatment-response
  - tp53-pathway
  - mdm2-amplification
  - biomarker
processed_by: crosslinker
processed_at: 2026-05-21
---

# Esophageal/GEJ Adenocarcinoma MSK TP53 Pathway (MSK, CCR 2022)

## Overview

`egc_msk_tp53_ccr_2022` is a Memorial Sloan Kettering retrospective cohort of 237 patients with locally advanced lower esophageal or gastroesophageal junction ([GEJ](../cancer_types/GEJ.md)) adenocarcinoma treated with curative-intent multimodality therapy from 2014–2020. All patients underwent prospective [MSK-IMPACT](../methods/msk-impact-panel.md) tumor sequencing. The dataset was assembled to evaluate the [TP53](../genes/TP53.md) pathway — including [MDM2](../genes/MDM2.md) amplification and bi-allelic [TP53](../genes/TP53.md) truncating mutations — as a predictor of neoadjuvant therapy response.

## Composition

- **n = 237** patients; 82% male, median age 61 (IQR 55–68); 78% clinical stage III.
- **Cancer types:** lower esophageal adenocarcinoma ([EAC](../cancer_types/EAC.md)) and gastroesophageal junction adenocarcinoma ([GEJ](../cancer_types/GEJ.md)); [ESCA](../cancer_types/ESCA.md) histology.
- **Treatment:** 49% [carboplatin](../drugs/carboplatin.md) + [paclitaxel](../drugs/paclitaxel.md) (Carbo-Taxol); 32% FOLFOX/FLOT regimens; 90% concurrent radiotherapy; 10 patients received neoadjuvant [trastuzumab](../drugs/trastuzumab.md) (HER2+); 33 received neoadjuvant immune checkpoint blockade.
- **Response definition:** major pathologic response (nT-R) = pN0 AND ≥90% treatment effect (CAP-TRG score 0–1); 14 MSI-H cases excluded → 64 nT-R vs 159 nT-NR (223 analyzed). Overall pCR rate: 12%.
- **Recurrent drivers (≥8%, after MSI-H exclusion):** [TP53](../genes/TP53.md) 79%, [CDKN2A](../genes/CDKN2A.md) 22%, [KRAS](../genes/KRAS.md) 19%, [ERBB2](../genes/ERBB2.md) 16%, [ARID1A](../genes/ARID1A.md) 14%, [SMAD4](../genes/SMAD4.md) 10%, [MDM2](../genes/MDM2.md) 9%, [CCNE1](../genes/CCNE1.md) 8%.

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — prospective targeted NGS using the 341-, 410-, or 468-gene panel versions ([IMPACT341](../methods/IMPACT341.md), [IMPACT410](../methods/IMPACT410.md), [IMPACT468](../methods/IMPACT468.md)).
- [FACETS](../methods/facets.md) — copy number, tumor purity, ploidy, and bi-allelic status assessment.
- [MSIsensor](../methods/msisensor.md) — MSI scoring (score ≥10 = MSI-H; 14 MSI-H cases excluded from response analyses).
- [OncoKB annotation](../methods/oncokb-annotation.md) — variant filtering and actionability classification.

## Papers using this cohort

- [PMID:35377946](../papers/35377946.md) — Sihag et al., *Clinical Cancer Research* 2022: Retrospective analysis of 237 patients showing [MDM2](../genes/MDM2.md) amplification is an independent predictor of poor neoadjuvant response (OR 0.10, 95% CI 0.01–0.55, p=0.032) and that severity of [TP53](../genes/TP53.md) pathway dysfunction stratifies responders. [PMID:35377946](../papers/35377946.md)

## Notable findings derived from this cohort

- [MDM2](../genes/MDM2.md) amplification was the only individual gene alteration significantly associated with neoadjuvant non-response on univariable testing (p=0.01, q=0.09) and remained an independent predictor on multivariable logistic regression (OR 0.10, 95% CI 0.01–0.55, p=0.032) [PMID:35377946](../papers/35377946.md).
- A 4-tier TP53 pathway severity classification ([MDM2](../genes/MDM2.md) amplification → TP53 truncating bi-allelic → other TP53 pathway mutation → TP53 pathway wild-type) stratified pathologic response rates (p=0.004, q=0.07) [PMID:35377946](../papers/35377946.md).
- MDM2 amplification and TP53 truncating bi-allelic mutations were almost entirely mutually exclusive (q<0.05), both producing critical TP53 pathway dysfunction [PMID:35377946](../papers/35377946.md).

## Sources

- cBioPortal study `egc_msk_tp53_ccr_2022`.
- Sihag S, et al. *The Role of the TP53 Pathway in Predicting Response to Neoadjuvant Therapy in Esophageal Adenocarcinoma.* Clin Cancer Res. 2022. [PMID:35377946](../papers/35377946.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
