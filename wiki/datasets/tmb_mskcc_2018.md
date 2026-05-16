---
name: Pan-Cancer TMB and ICI Survival — MSK-IMPACT 2018
studyId: tmb_mskcc_2018
institution: Memorial Sloan Kettering Cancer Center
size: 1662
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-panel-seq
panels:
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - pan-cancer
  - tumor-mutational-burden
  - immunotherapy
  - immune-checkpoint-inhibitor
  - MSK-IMPACT
  - biomarker
  - overall-survival
processed_by: crosslinker
processed_at: 2026-05-16
---

# Pan-Cancer TMB and ICI Survival — MSK-IMPACT 2018

## Overview

The tmb_mskcc_2018 cohort was assembled at Memorial Sloan Kettering Cancer Center to prospectively evaluate tumor mutational burden (TMB) as a pan-cancer predictive biomarker for overall survival ([OS](../cancer_types/OS.md)) after immune checkpoint inhibitor (ICI) therapy. The study enrolled 1,662 advanced cancer patients treated with ICI and 5,371 non-ICI-treated patients as a prognostic control, all profiled by MSK-IMPACT targeted next-generation sequencing using 341-, 410-, or 468-gene panels with matched germline normals. This is the primary dataset of the Samstein et al. 2019 *Nature Genetics* publication establishing TMB as a pan-cancer ICI survival predictor. Data are publicly available on cBioPortal.

## Composition

- **ICI-treated patients:** 1,662 with advanced cancer (94% stage IV / metastatic).
- **Non-ICI-treated control patients:** 5,371 profiled by MSK-IMPACT (same institution).
- **Key histologies (ICI cohort):** [NSCLC](../cancer_types/NSCLC.md) (n = 350), melanoma [SKCM](../cancer_types/SKCM.md) (n = 321), bladder cancer [BLCA](../cancer_types/BLCA.md) (n = 214), renal cell carcinoma [RCC](../cancer_types/RCC.md) (n = 151), head & neck squamous [HNSC](../cancer_types/HNSC.md) (n = 138), esophagogastric [EGC](../cancer_types/EGC.md), colorectal [COAD](../cancer_types/COAD.md), glioma [DIFG](../cancer_types/DIFG.md)/[GBM](../cancer_types/GBM.md).
- **ICI regimens:** anti-CTLA4 (n = 146: [ipilimumab](../drugs/ipilimumab.md), [tremelimumab](../drugs/tremelimumab.md)), anti-PD-1/PD-L1 (n = 1,447: [nivolumab](../drugs/nivolumab.md), [pembrolizumab](../drugs/pembrolizumab.md), [atezolizumab](../drugs/atezolizumab.md), [avelumab](../drugs/avelumab.md), [durvalumab](../drugs/durvalumab.md)), combination (n = 189).
- **TMB definition:** non-synonymous somatic mutations / exonic Mb sequenced; TMB-high defined as top 20th percentile within each histology.
- **Outcome:** OS from first ICI dose; median follow-up 19 months (range 0–80).

## Assays / panels (linked)

- [IMPACT341](../methods/IMPACT341.md) — 341-gene targeted NGS panel with matched germline normal
- [IMPACT410](../methods/IMPACT410.md) — 410-gene targeted NGS panel with matched germline normal
- [IMPACT468](../methods/IMPACT468.md) — 468-gene targeted NGS panel with matched germline normal

## Papers using this cohort

- [PMID:30643254](../papers/30643254.md) — Samstein et al. 2019, "Tumor mutational load predicts survival after immunotherapy across multiple cancer types," *Nature Genetics*.

## Notable findings derived from this cohort

- Across the entire ICI cohort, top-20%-by-histology TMB group had HR 0.52 (95% CI 0.42–0.64) for OS vs the bottom 80% (log-rank); robust across cutpoints from 10–50th percentile [PMID:30643254](../papers/30643254.md).
- Multivariable Cox regression adjusting for cancer type, age, ICI drug class, and year confirmed TMB as a continuous predictor (HR = 0.985/unit, p = 3.4×10⁻⁷) and binary predictor (top 20% per histology, HR 0.61, p = 1.3×10⁻⁷) [PMID:30643254](../papers/30643254.md).
- No OS benefit for higher TMB in the 5,371-patient non-ICI control cohort (HR 1.12, p = 0.11), confirming the benefit is ICI-specific [PMID:30643254](../papers/30643254.md).
- Histology-specific TMB-high cutpoints vary widely (e.g., 52.2 mut/Mb for colorectal, reflecting MSI-high enrichment), arguing against a single universal pan-cancer threshold [PMID:30643254](../papers/30643254.md).
- Glioma is an outlier: no OS benefit from high TMB in [GBM](../cancer_types/GBM.md)/[DIFG](../cancer_types/DIFG.md), possibly due to temozolomide-induced subclonal hypermutation or CNS-specific immune biology [PMID:30643254](../papers/30643254.md).
- Targeted MSK-IMPACT panels (sampling ~3% of the coding exome) provide sufficient TMB estimation for ICI-survival prediction, supporting clinical-grade targeted NGS over whole-exome sequencing for this biomarker [PMID:30643254](../papers/30643254.md).

## Sources

- [PMID:30643254](../papers/30643254.md)
- cBioPortal study: tmb_mskcc_2018 (http://www.cbioportal.org/study?id=tmb_mskcc_2018)

*This page was processed by **crosslinker** on **2026-05-16**.*
