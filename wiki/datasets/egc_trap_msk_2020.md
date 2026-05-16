---
name: MSK TRAP Phase 2 HER2+ Esophagogastric Cancer (pembrolizumab + trastuzumab)
studyId: egc_trap_msk_2020
institution: Memorial Sloan Kettering Cancer Center (MSK)
size: 37
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - msk-impact-panel
  - whole-exome-seq
  - guardant360
panels:
  - msk-impact-panel
tags:
  - her2-positive
  - esophagogastric-cancer
  - immunotherapy
  - ctdna
  - phase-2-trial
  - trastuzumab-resistance
  - keynote-811-rationale
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK TRAP Phase 2 HER2+ Esophagogastric Cancer

## Overview

The egc_trap_msk_2020 cohort is the genomic and clinical dataset from NCT02954536 — a single-arm phase 2 trial at Memorial Sloan Kettering Cancer Center testing first-line [pembrolizumab](../drugs/pembrolizumab.md) plus [trastuzumab](../drugs/trastuzumab.md) with fluoropyrimidine/platinum chemotherapy in HER2-positive metastatic esophagogastric adenocarcinoma. Integrated tumor (MSK-IMPACT / WES) and ctDNA (Guardant360) profiling identified plasma [ERBB2](../genes/ERBB2.md) amplification as a predictor of longer PFS and RTK-RAS pathway co-alterations as a predictor of shorter PFS. Results provided the rationale for the randomized phase 3 KEYNOTE-811 trial. [PMID:32437664](../papers/32437664.md)

## Composition

- **37 patients** with HER2-positive (IHC 3+ or HER2:CEP17 FISH ≥2.0) metastatic esophagogastric adenocarcinoma: esophageal ([ESCA](../cancer_types/ESCA.md)) 14 (38%), gastroesophageal junction ([GEJ](../cancer_types/GEJ.md)) 12 (32%), gastric ([STAD](../cancer_types/STAD.md)) 11 (30%).
- Median age 60 (range 21–84); 78% male; 86% White; ECOG 0–1.
- 32/37 tumors profiled by [MSK-IMPACT](../methods/msk-impact-panel.md) (468-gene panel); 31/37 by [whole-exome-seq](../methods/whole-exome-seq.md); 33/37 with plasma ctDNA by [Guardant360](../methods/guardant360.md). [PMID:32437664](../papers/32437664.md)
- No MSI-H or EBV-positive tumors in the cohort; median TMB 3.3 mut/Mb (range 0.3–7.8). [PMID:32437664](../papers/32437664.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — 468-gene targeted panel, tumor + matched normal.
- [whole-exome-seq](../methods/whole-exome-seq.md) — TEMPO pipeline; BWA-mem + Strelka2/Mutect2; [FACETS](../methods/facets.md) for copy number; [MSIsensor](../methods/msisensor.md) for MSI; [mutational-signatures](../methods/mutational-signatures.md) for samples with ≥5 SNVs. [PMID:32437664](../papers/32437664.md)
- [Guardant360](../methods/guardant360.md) — plasma ctDNA; VAF-adjusted ERBB2 amplification normalization derived across 1,630 EG patients (HERACLES trial). [PMID:32437664](../papers/32437664.md)
- HER2 expression by [IHC](../methods/immunohistochemistry.md) and [FISH](../methods/fish.md). [PMID:32437664](../papers/32437664.md)

## Papers using this cohort

- [PMID:32437664](../papers/32437664.md) — Janjigian et al. (2020), *Lancet Oncology*: First-line pembrolizumab and trastuzumab in HER2-positive esophagogastric cancer.

## Notable findings derived from this cohort

- 70% (26/37) 6-month progression-free survival rate (95% CI 54–83%), meeting the primary endpoint; ORR 91%, median [OS](../cancer_types/OS.md) 27.2 months — numerically far exceeding historical ToGA benchmark (47% ORR, ~13.8-month OS for trastuzumab + chemotherapy alone). [PMID:32437664](../papers/32437664.md)
- [ERBB2](../genes/ERBB2.md) amplification detected in 21/32 (66%) tumors by NGS and 18/33 (54%) plasma ctDNA samples; tissue vs. plasma concordance 93% (27/29). [PMID:32437664](../papers/32437664.md)
- Plasma ctDNA VAF-adjusted [ERBB2](../genes/ERBB2.md) amplification was significantly associated with longer PFS (median 16.4 vs. 6.2 months; p=0.013); tissue NGS ERBB2 trended but did not reach significance (p=0.12). [PMID:32437664](../papers/32437664.md)
- [KRAS](../genes/KRAS.md)/RTK-RAS pathway co-alterations were associated with significantly shorter PFS (median 5.9 vs. 14.6 months; p=0.011). [PMID:32437664](../papers/32437664.md)
- PD-L1 CPS status did not predict outcome (median PFS 10.3 vs. 14.6 months; p=0.56). [PMID:32437664](../papers/32437664.md)

## Sources

- cBioPortal study: `egc_trap_msk_2020`
- Trial registration: NCT02954536
- DOI: [10.1016/S1470-2045(20)30169-8](https://doi.org/10.1016/S1470-2045(20)30169-8)

*This page was processed by **crosslinker** on **2026-05-16**.*
