---
title: "Open questions across the corpus"
slug: open_questions
tags:
  - open-questions
  - cross-paper-conflicts
processed_by: theme-synthesizer
processed_at: 2026-04-15
---

# Open questions across the corpus

This page records cross-paper disagreements that the corpus does not resolve.
Each bullet names the conflicting papers explicitly and the point of contention.
New theme-synthesizer runs append to this list; conflicts are recorded, not
resolved (see `schema/CLAUDE.md` §"Hard rules" #6).

## Radiation biology

- **CT radiomic signature generalizability in head-and-neck cancer.**
  [PMID:24892406](../papers/24892406.md) (Aerts 2014) vs
  [PMID:37397861](../papers/37397861.md) (Kazmierski 2023). Aerts reports a
  fixed 4-feature NSCLC-trained signature generalizes without retraining to
  two independent HNSCC cohorts (CI=0.69 in both) and retains performance in
  HPV-negative HNSCC. Kazmierski, benchmarking on RADCURE (n=2,552) with
  three external HNSCC cohorts (n=873), reports that no radiomics-only model
  beat any EMR-only model, the best deep-radiomics model added to EMR
  *dropped* AUROC vs EMR+volume, and external performance degraded on 2 of 3
  sites with significant HPV/disease-site/outcome-prevalence distribution
  shift. Point of contention: whether HNSCC CT radiomics generalizes across
  institutions without retraining.
- **Added value of image features beyond tumor volume + EMR in HNSCC
  prognosis.** [PMID:24892406](../papers/24892406.md) (Aerts 2014) reports
  signature+volume beats volume alone in all NSCLC/HNSCC validation cohorts.
  [PMID:37397861](../papers/37397861.md) (Kazmierski 2023) reports no
  radiomics-only model beat any EMR-only model on RADCURE, replacing tumor
  volume with deep CNN features *lowered* AUROC from 0.823 to 0.766, and the
  top model only modestly beat volume alone on MDACC external validation.
  Point of contention: whether volume-independent image information adds
  meaningful prognostic value on top of EMR+volume in definitive-RT HNSCC.
- **PD-L1 CPS as a predictor of benefit with RT + PD-1 blockade in HNSCC.**
  [PMID:38780927](../papers/38780927.md) (Saba 2024) reports PD-L1 CPS
  (22C3) <20 vs ≥20 does **not** stratify PFS (P=0.86) or OS (P=0.74) in
  IMRT reirradiation + nivolumab, explicitly divergent from recurrent/
  metastatic HNSCC with single-agent PD-1 blockade. Point of contention:
  whether PD-L1 CPS retains predictive value when PD-1 blockade is combined
  with radiation in a previously irradiated field.
- **Direction of the early peripheral PD-1+Ki-67+ CD4+ T-cell surge under
  PD-1 blockade.** [PMID:38780927](../papers/38780927.md) (Saba 2024)
  reports a ≥1.5-fold surge at week 2–4 trends toward **worse** PFS (HR
  2.09; median 16.0 vs 27.1 months) in HNSCC reirradiation + nivolumab,
  opposite in direction to prior reports in lung cancer and melanoma under
  PD-1 blockade alone (external literature cited by the paper, not present
  as a primary paper in this corpus). Point of contention: whether the
  peripheral PD-1+Ki-67+ CD4+ pharmacodynamic biomarker has opposite sign
  in RT-combined immunotherapy vs immunotherapy alone.
- **Ketogenic diet as a radiosensitizer vs radioresistance promoter.**
  [PMID:41941260](../papers/41941260.md) (ROBIN consortium, OligoMET
  Project 2) reports that ketogenic diets *unexpectedly* promoted
  radio-resistance in preclinical prostate-cancer models, while low-fat and
  calorie-restricted regimens enhanced radiation response. The paper
  explicitly flags this as contrary to prior expectation in the preclinical
  literature. Point of contention: the direction of the ketogenic-diet
  effect on RT response.

*This page was processed by **theme-synthesizer** on **2026-04-15**.*
