---
name: IDH-Mutant Glioma CSF ctDNA — MSK-IMPACT 2018
studyId: glioma_msk_2018
institution: Memorial Sloan Kettering Cancer Center
size: 85
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-panel-seq
  - liquid-biopsy-csf
panels:
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - glioma
  - GBM
  - IDH-mutant
  - liquid-biopsy
  - csf-ctdna
  - MSK-IMPACT
  - clonal-evolution
  - diffuse-glioma
processed_by: crosslinker
processed_at: 2026-05-16
---

# IDH-Mutant Glioma CSF ctDNA — MSK-IMPACT 2018

## Overview

The glioma_msk_2018 cohort was assembled at Memorial Sloan Kettering Cancer Center (MSKCC) to evaluate cerebrospinal fluid (CSF) cell-free DNA (cfDNA) as a liquid-biopsy reservoir for adult diffuse glioma. The study enrolled 85 patients (113 CSF samples total) treated at MSKCC from January 2015 to April 2017, and profiled CSF DNA by MSK-IMPACT targeted NGS alongside matched tumor tissue and, in a subset, plasma cfDNA. The cohort establishes CSF ctDNA positivity as an independent prognostic factor for shorter [OS](../cancer_types/OS.md) (HR 4.16) and documents convergent/branched evolution in growth-factor-receptor pathways over time. Patient data are deposited on cBioPortal as glioma_msk_2018. A benchmark comparison cohort of 553 MSKCC glioma biopsies from 512 patients was sequenced separately with MSK-IMPACT.

## Composition

- **n = 85** adult glioma patients; **113 CSF samples** (22 patients had ≥2 serial CSF collections).
- **WHO grade:** grade IV [GBM](../cancer_types/GBM.md) 46/85 (54%), grade III glioma 26/85 (31%), grade II glioma 13/85 (15%); all classified under [DIFG](../cancer_types/DIFG.md); 39 LGG-grade tumors (grade II + III).
- **Prior treatment:** surgery 85/85 (100%), radiation 84/85 (99%), systemic chemotherapy ≥1 line 81/85 (95%).
- **Matched normal:** available for 73/85 (86%); remaining 12 used pool-of-normals plus 1000 Genomes filtering.
- **Plasma cfDNA:** profiled in a subset on a 129-gene duplex-UMI capture assay (>18,000× raw / 1,032× unique coverage).
- **Benchmark:** 553 MSKCC glioma tissue biopsies from 512 patients previously sequenced with MSK-IMPACT.

## Assays / panels (linked)

- [IMPACT341](../methods/IMPACT341.md) — 341-gene targeted NGS (tumor tissue)
- [IMPACT410](../methods/IMPACT410.md) — 410-gene targeted NGS with 46 intronic structural-variant windows (CSF ctDNA and tumor)
- [IMPACT468](../methods/IMPACT468.md) — 468-gene targeted NGS (tumor tissue)
- [facets](../methods/facets.md) — allele-specific copy-number analysis
- [integrative-genomics-viewer](../methods/integrative-genomics-viewer.md) — manual structural-variant review

## Papers using this cohort

- [PMID:30675060](../papers/30675060.md) — Miller et al. 2019, "Tracking tumour evolution in glioma through liquid biopsies of cerebrospinal fluid," *Nature*.

## Notable findings derived from this cohort

- Tumor-derived ctDNA detected in 42/85 (49.4%) CSF samples and 0/7 non-malignant controls; positivity correlated with disease progression (Fisher p = 0.0005), tumor burden (SPD, Wilcoxon p = 1.7×10⁻⁶), and ventricular/subarachnoid tumor spread (Fisher p = 0.02) [PMID:30675060](../papers/30675060.md).
- CSF ctDNA positivity carried HR 4.16 (95% CI 2.15–8.05, p = 2.43×10⁻⁵) for death in multivariable Cox model adjusting for extent of resection, tumor burden, and [IDH1](../genes/IDH1.md) status; median OS 3.15 months (ctDNA+) vs 11.91 months (ctDNA−) [PMID:30675060](../papers/30675060.md).
- 35/42 (83%) ctDNA-positive CSFs had no malignant cells by standard cytopathology — molecular detection outperformed cytology [PMID:30675060](../papers/30675060.md).
- Truncal glioma-defining alterations ([IDH1](../genes/IDH1.md)/[IDH2](../genes/IDH2.md), [TP53](../genes/TP53.md), [ATRX](../genes/ATRX.md), [TERT](../genes/TERT.md) promoter, 1p/19q codeletion) showed 100% concordance between CSF and matched tumor tissue in all 30 non-hypermutated pairs [PMID:30675060](../papers/30675060.md).
- Plasma was substantially inferior: 16/19 (84%) CSF-ctDNA-positive patients had no detectable mutations in plasma; average VAF 0.58% in plasma vs 23.96% in CSF (Wilcoxon p = 5.82×10⁻¹¹); all three plasma-positive cases had disseminated CNS disease [PMID:30675060](../papers/30675060.md).
- 5/42 (12%) CSFs displayed alkylator-induced hypermutation (G:C→A:T signature); all five had received [temozolomide](../drugs/temozolomide.md) [PMID:30675060](../papers/30675060.md).
- Convergent evolution in growth-factor-receptor pathways documented: patient #25 lost [EGFR](../genes/EGFR.md) amplification and gained [PDGFRA](../genes/PDGFRA.md) amplification + mutation over time; patient #28 (IDH-WT GBM) acquired amplifications in [MET](../genes/MET.md), [KIT](../genes/KIT.md), [CDK4](../genes/CDK4.md), and [MYC](../genes/MYC.md) in a branched pattern across serial tumor and CSF samples [PMID:30675060](../papers/30675060.md).
- Median tumor mutational burden in CSF ctDNA was 4.90 mut/Mb, not different from the MSK-IMPACT tissue benchmark (4.46/Mb in n = 553; Wilcoxon p not significant after excluding hypermutators: 3.92/Mb CSF vs 3.94/Mb tissue) [PMID:30675060](../papers/30675060.md).

## Sources

- [PMID:30675060](../papers/30675060.md)
- cBioPortal study: glioma_msk_2018

*This page was processed by **crosslinker** on **2026-05-16**.*
