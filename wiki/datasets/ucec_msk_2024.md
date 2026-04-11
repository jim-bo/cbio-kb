---
name: Endometrial and Gynecologic Cancers, Nivolumab Trial (MSK, 2024)
slug: ucec_msk_2024
institution: Memorial Sloan Kettering Cancer Center
size: 35
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [immunofluorescence, targeted-panel, whole-exome-seq]
panels: []
tags:
  - endometrial
  - UCEC
  - dMMR
  - MSI-H
  - nivolumab
  - immunotherapy
  - phase2
processed_by: crosslinker
processed_at: 2026-04-11
---

# Endometrial and Gynecologic Cancers, Nivolumab Trial (MSK, 2024)

## Overview

Single-center phase 2 clinical trial cohort (NCT03241745) of 35 patients with recurrent or advanced dMMR/MSI-H or hypermutated endometrial carcinoma ([UCEC](../cancer_types/UCEC.md)) and ovarian/fallopian tube/peritoneal cancers ([OVT](../cancer_types/OVT.md)) treated with [nivolumab](../drugs/nivolumab.md) at Memorial Sloan Kettering Cancer Center. Dataset designed to identify predictive biomarkers for response to PD-1 blockade beyond dMMR status. Data deposited in cBioPortal as `ucec_msk_2024`. [PMID:38653864](../papers/38653864.md)

## Composition

- 35 patients enrolled; 34 evaluable for response.
- 83% endometrioid histology; median age 64 years (range 36–87); 77% White, 11% Black, 6% Asian.
- Median follow-up: 42.1 months.
- Cancer types: endometrial carcinoma ([UCEC](../cancer_types/UCEC.md), primary) and ovarian/fallopian tube/peritoneal cancer ([OVT](../cancer_types/OVT.md)).
- All with dMMR (by IHC loss), MSI-H (by MSK-IMPACT), or hypermutation (≥20 somatic mutations on MSK-IMPACT). [PMID:38653864](../papers/38653864.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — MSI and TMB assessment, somatic profiling.
- [Whole-exome sequencing](../methods/whole-exome-seq.md) — 33 of 34 evaluable tumors.
- Multiplexed immunofluorescence (Vectra system) — 25 patients; 7-marker panel (CD8, PD-1, TOX, PD-L1, PAX8, FoxP3, DAPI) for tumor microenvironment analysis.

## Papers using this cohort

- [PMID:38653864](../papers/38653864.md) — Nivolumab for mismatch-repair-deficient or hypermutated gynecologic cancers: a phase 2 trial with biomarker analyses.

## Notable findings derived from this cohort

- ORR 58.8% (7 CR, 13 PR); PFS24 64.7% (97.5% one-sided CI: 46.5–100%); median PFS 21.6 months. [PMID:38653864](../papers/38653864.md)
- TMB and PD-L1 expression were not predictive of response within the dMMR-selected population. [PMID:38653864](../papers/38653864.md)
- Dysfunctional CD8+PD-1+ T cells (P = 0.006) and terminally dysfunctional CD8+PD-1+TOX+ T cells (P = 0.001) were strongly associated with PFS24; a multivariate model combining CD8+PD-1+TOX+ percentage and PD-L1+ cell proximity achieved AUC = 0.897 (P = 0.0007). [PMID:38653864](../papers/38653864.md)
- [MEGF8](../genes/MEGF8.md) mutations enriched in responders (32% vs. 0%; P = 0.027); [SETD1B](../genes/SETD1B.md) mutations enriched in responders (58% vs. 14%; P = 0.015). [PMID:38653864](../papers/38653864.md)
- Mechanism of dMMR (genetic vs. epigenetic/MLH1 hypermethylation) did not predict differential nivolumab response (P = 0.43). [PMID:38653864](../papers/38653864.md)

## Sources

- cBioPortal study `ucec_msk_2024`. [PMID:38653864](../papers/38653864.md)

*This page was processed by **crosslinker** on **2026-04-11**.*
