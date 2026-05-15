---
name: MSK Esophagogastric Cancer (Janjigian et al. 2017)
studyId: egc_msk_2017
institution: Memorial Sloan Kettering Cancer Center
size: 295
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - msk-impact-panel
  - immunohistochemistry
  - fish
panels:
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - esophagogastric-cancer
  - gastric-cancer
  - metastatic
  - erbb2
  - trastuzumab
  - msi-h
  - immunotherapy
  - targeted-sequencing
  - aacr-genie
processed_by: crosslinker
processed_at: 2026-05-15
---

# MSK Esophagogastric Cancer (Janjigian et al. 2017)

## Overview

Janjigian et al. report the first 295 patients with stage IV [esophagogastric adenocarcinoma](../cancer_types/EGC.md) prospectively profiled at MSKCC using the [MSK-IMPACT](../methods/msk-impact-panel.md) targeted next-generation sequencing assay. With mature clinical annotation including treatment response and survival, this dataset characterizes the genomic landscape of metastatic [EGC](../cancer_types/EGC.md), evaluates [ERBB2](../genes/ERBB2.md) NGS vs IHC/FISH concordance for [trastuzumab](../drugs/trastuzumab.md) selection, defines MSI-H as chemotherapy-refractory but immunotherapy-sensitive, and identifies acquired resistance mechanisms to trastuzumab and checkpoint inhibitors. The dataset is committed to AACR Project GENIE and publicly available on cBioPortal. Published in *Nature Medicine* (2017).

## Composition

- **295 patients with metastatic (stage IV) esophageal, gastric, and gastroesophageal junction adenocarcinoma**; 318 tumor samples (some patients with paired pre- and post-treatment biopsies). Consented February 2014–February 2017.
- **Cancer types:** [Esophagogastric Adenocarcinoma (EGC)](../cancer_types/EGC.md), spanning [ESCA](../cancer_types/ESCA.md), [STAD](../cancer_types/STAD.md) including [DSTAD](../cancer_types/DSTAD.md), and [GEJ](../cancer_types/GEJ.md) tumors.
- **Molecular subtypes:** CIN subtype dominated (63%); GS tumors 34% (enriched for diffuse histology 32% vs 9%, P=3e-5, and [CDH1](../genes/CDH1.md) mutations 20% vs 7%, P=0.01); MSI-H 3% (9/295).
- **Treatment subsets analyzed:** 187 HER2-negative on first-line fluoropyrimidine/platinum; 50 HER2+ on first-line [trastuzumab](../drugs/trastuzumab.md)/chemotherapy; 23 paired pre-/post-trastuzumab tumor pairs; 40 patients on immune checkpoint inhibitors.
- 90% ECOG 0–1 status reflecting specialty care selection.

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — CLIA-certified hybrid-capture targeted NGS, run as [IMPACT341](../methods/IMPACT341.md), [IMPACT410](../methods/IMPACT410.md), or [IMPACT468](../methods/IMPACT468.md) panels on paired tumor/normal blood; mean coverage 744X
- [FACETS](../methods/facets.md) — allele-specific copy number and tumor purity estimation
- [MSIsensor](../methods/msisensor.md) — MSI status from sequencing data (MSI-H threshold ≥10)
- [OncoKB](../methods/oncokb-annotation.md) — oncogenic effect annotation
- [IHC](../methods/immunohistochemistry.md) — HER2 (3+ positive) per CAP/ASCO criteria; [B2M](../genes/B2M.md) protein confirmation
- [FISH](../methods/fish.md) — HER2 status per CAP/ASCO criteria
- EBER-ISH — EBV detection (n=26 immunotherapy-treated patients)

## Papers using this cohort

- [PMID:29122777](../papers/29122777.md) — Janjigian et al., *Nat Med* (2017): Genomics of Trastuzumab Resistance in HER2 Positive Advanced Esophagogastric Adenocarcinoma.

## Notable findings derived from this cohort

- **53% of patients had at least one OncoKB-defined potentially actionable alteration.** Most frequent oncogenic alterations in the CIN subset: [ERBB2](../genes/ERBB2.md) (25%), [KRAS](../genes/KRAS.md) (16%), [EGFR](../genes/EGFR.md) (8%), [ERBB3](../genes/ERBB3.md) (7%), [PIK3CA](../genes/PIK3CA.md) (7%), [FGFR2](../genes/FGFR2.md) (5%), [MET](../genes/MET.md) (5%). Most-mutated genes: [TP53](../genes/TP53.md) (73%), [ARID1A](../genes/ARID1A.md) (15%), [CDKN2A](../genes/CDKN2A.md) (12%). [PMID:29122777](../papers/29122777.md)
- **MSI-H tumors (3%) are chemotherapy-refractory but immunotherapy-sensitive.** Median PFS on first-line chemotherapy 4.8 months (MSI-H) vs 6.9 months (non-MSI-H), HR=0.4, P=0.027. MSI-H frequency significantly lower than TCGA's 16% (P=8e-10), attributable to the metastatic-enriched MSK cohort. [PMID:29122777](../papers/29122777.md)
- **HRD/LST is not a platinum-chemotherapy biomarker in EGC.** LST score did not predict PFS on first-line platinum (HR=0.99, P=0.947); two longest outlier responders (68 and 104 months) had no [BRCA1](../genes/BRCA1.md)/[BRCA2](../genes/BRCA2.md) alterations. [PMID:29122777](../papers/29122777.md)
- **NGS-based ERBB2 amplification is concordant with IHC/FISH** (PPV 90%, NPV 96.9%, concordance 93.7%) and captures dose-dependent response gradient: top-quartile ERBB2-amplification patients had median PFS of 24.3 months on first-line [trastuzumab](../drugs/trastuzumab.md). [PMID:29122777](../papers/29122777.md)
- **Loss of ERBB2 amplification is a common acquired-resistance mechanism:** 7/44 (16%) post-trastuzumab samples became ERBB2-negative by NGS with HER2 protein loss confirmed by IHC. [PMID:29122777](../papers/29122777.md)
- **RTK-RAS-PI3K co-alterations shorten trastuzumab PFS** (median 8.4 months vs longer in pathway-wildtype); acquired [KRAS](../genes/KRAS.md) (2% pre vs 13% post) and [PIK3CA](../genes/PIK3CA.md) (2% pre vs 8.6% post) activating mutations enriched post-trastuzumab. [PMID:29122777](../papers/29122777.md)
- **[B2M](../genes/B2M.md) loss is a recurrent immunotherapy-resistance mechanism:** 4/9 (44%) MSI-H tumors carry likely deleterious B2M alterations; acquired exon-1 loss-of-function confirmed by IHC in a patient with acquired resistance to anti-PD-1. [PMID:29122777](../papers/29122777.md)
- **High TMB (>9.7 mut/Mb) supports immunotherapy:** top-quartile TMB associated with median [OS](../cancer_types/OS.md) 16.8 vs 6.62 months and 2-year OS 44% vs 14% (HR=0.40, P=0.058). [PMID:29122777](../papers/29122777.md)
- **EBV+ exceptional response:** the single EBV+ patient achieved a complete and durable response (>30 months) to anti-PD-1 therapy. [PMID:29122777](../papers/29122777.md)
- No primary-vs-metastatic differences in alteration frequencies detected. [PMID:29122777](../papers/29122777.md)

## Sources

- cBioPortal study ID: egc_msk_2017
- AACR Project GENIE
- MSK-IMPACT clinical sequencing program

*This page was processed by **crosslinker** on **2026-05-15**.*
