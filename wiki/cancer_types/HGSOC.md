---
name: High-Grade Serous Ovarian Cancer
oncotree_code: HGSOC
main_type: Ovarian Cancer
parent: SOC
tags: []
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# High-Grade Serous Ovarian Cancer (HGSOC)

## Overview

High-grade serous ovarian carcinoma (HGSOC) is the most common and lethal ovarian cancer subtype, originating from fallopian tube precursors (serous tubal intraepithelial carcinomas, STICs) and p53 signature lesions. On OncoTree it is a child of Serous Ovarian Cancer (SOC). Nearly all HGSOCs harbor [TP53](../genes/TP53.md) mutations, and nearly half exhibit homologous recombination deficiency via BRCA1/2 alterations or epigenetic silencing. More than 80% of patients with stage III/IV disease develop resistance to platinum-based chemotherapy.

## Cohorts in the corpus

- 44 FFPE fallopian tube specimens from 43 individuals profiled by CyCIF (31-antibody panel) and NanoString GeoMx whole transcriptome analysis across >600 ROIs, spanning the full progression spectrum from p53 signatures through STICs to invasive cancer. Multi-center (University of Pennsylvania, Swedish Cancer Institute, Seattle). Dataset: [ovary_geomx_gray_foundation_2024](../datasets/ovary_geomx_gray_foundation_2024.md). [PMID:39386723](../papers/39386723.md)
- MSK MIND multimodal cohort: 296 HGSOC patients from MSKCC (including 36 from the prospective [MSK-SPECTRUM](../datasets/msk_spectrum_tme_2022.md) project) combined with 148 patients from [TCGA-OV](../datasets/ov_tcga.md); predominantly stage III/IV (160 stage IV, 225 stage III in training). Modalities: pre-treatment contrast-enhanced CT (omental + adnexal segmentations), H&E WSIs, [MSK-IMPACT](../methods/msk-impact-panel.md) targeted sequencing (HRD/HRD status). Train n=404, held-out test n=40. [PMID:35764743](../papers/35764743.md)

## Recurrent alterations

- [TP53](../genes/TP53.md) — mutations define p53 signatures, the earliest precursor lesions; clonally shared across p53 signatures, STICs, and concurrent HGSOC. [PMID:39386723](../papers/39386723.md)
- [BRCA1](../genes/BRCA1.md) / [BRCA2](../genes/BRCA2.md) — germline mutations in ~30% of HGSOC cohort ([BRCA1](../genes/BRCA1.md) n=12, [BRCA2](../genes/BRCA2.md) n=12); nearly half of HGSOCs exhibit HRD via somatic or germline BRCA1/2 alterations or epigenetic silencing. [PMID:39386723](../papers/39386723.md)
- [CCNE1](../genes/CCNE1.md) — amplification noted as an early copy-number alteration event in STICs, linked to breakage-fusion-bridge cycles. [PMID:39386723](../papers/39386723.md)
- [HLA-E](../genes/HLA-E.md) — progressive upregulation from p53 signatures through cancer; proposed mechanism of NK cell immune evasion via NKG2A receptor engagement. [PMID:39386723](../papers/39386723.md)
- [STAT1](../genes/STAT1.md), [CGAS](../genes/CGAS.md) / [STING1](../genes/STING1.md) — IFN pathway and cGAS-STING pathway activated early by chromosomal instability (micronuclear rupture) in STIC precursors. [PMID:39386723](../papers/39386723.md)
- [BRCA1](../genes/BRCA1.md) / [BRCA2](../genes/BRCA2.md) — pathogenic germline/somatic variants are the primary driver of HRD-subtype assignment in the MSK MIND cohort; HRD status alone provided only modest OS stratification (test c = 0.52), consistent with HRD being a necessary but insufficient prognostic variable in late-stage HGSOC. Training HRD/HRP/ambiguous split: 119/218/67. [PMID:35764743](../papers/35764743.md)
- [CDK12](../genes/CDK12.md) — SNVs used to assign patients to the tandem-duplicator-enriched subtype (per Wang et al.), overriding HRD-DDR variant evidence when present. [PMID:35764743](../papers/35764743.md)
- [CCNE1](../genes/CCNE1.md) — amplification used to assign patients to the foldback-inversion-enriched subtype; copy number analyzed via MSK-IMPACT pipeline for MSKCC cases and downloaded from cBioPortal for TCGA-OV cases. [PMID:35764743](../papers/35764743.md)

## Subtypes

- Precursor spectrum: normal fallopian tube → p53 signature → STIC.I (incidental) → STIC.C (concurrent with invasive cancer) → invasive HGSOC. [PMID:39386723](../papers/39386723.md)
- IFN-alpha and IFN-gamma pathway genes significantly upregulated beginning at the p53 signature stage and persisting through invasion. [PMID:39386723](../papers/39386723.md)
- cGAS-STING pathway activated via micronuclear rupture as early as STIC.I lesions. [PMID:39386723](../papers/39386723.md)
- NK-cDC1 axis declines progressively: NK cells become nearly undetectable in STIC.I and later stages. [PMID:39386723](../papers/39386723.md)
- CD8+ T cell exhaustion (LAG3, PD1 upregulation) increases 3- to 7-fold in later stages. [PMID:39386723](../papers/39386723.md)
- HRD genomic subtypes in MSK MIND cohort: HRD (enriched for BRCA1/2 and other DDR-pathway variants), HRP (homologous-recombination proficient), tandem-duplicator ([CDK12](../genes/CDK12.md) SNV-enriched), foldback-inversion ([CCNE1](../genes/CCNE1.md) amplification-enriched), and ambiguous. Omental CT autocorrelation and mean tumor nuclear area (H&E) were independently prognostic and largely orthogonal to HRD genomic subtype (absolute Kendall rank correlation between any modality pair < 0.14). [PMID:35764743](../papers/35764743.md)

## Therapeutic landscape

- [HLA-E](../genes/HLA-E.md) upregulation in precursor lesions suggests anti-NKG2A antibodies (e.g., [monalizumab](../drugs/monalizumab.md)) as a potential early interception strategy, particularly in high-risk patients with incidental STICs. [PMID:39386723](../papers/39386723.md)
- IFN-related DNA damage resistance signature (IRDS; [STAT1](../genes/STAT1.md), [MX1](../genes/MX1.md), [MCL1](../genes/MCL1.md)) emerges in STIC.C and cancer, potentially contributing to chemoresistance in >80% of stage III/IV patients. [PMID:39386723](../papers/39386723.md)
- Progressive CD8+ T cell exhaustion with upregulation of PD1, LAG3, TIM3, and [CTLA4](../genes/CTLA4.md) supports investigation of immune checkpoint inhibitors in the HGSOC precancer setting. [PMID:39386723](../papers/39386723.md)
- Multimodal late-fusion risk model (GRH: genomic + radiomic + histopathological) stratified OS in the held-out test set (median 30 vs. 50 months, P=0.023; 36-month OS 34% vs. 68%) and PFS (P=0.040), outperforming HRD-status alone (c=0.52) and the clinical model (c=0.51). Intended uses: primary treatment selection (PDS vs. NACT-IDS), surveillance planning, maintenance-therapy decisions, and enrollment in investigative trials. [PMID:35764743](../papers/35764743.md)
- Omental-implant radiomic model is a practical prognostic tool for advanced HGSOC: omental disease is ubiquitous (including primary peritoneal cases), omental implants are segmentable by less-experienced radiologists, and the single prognostic feature (GLCM autocorrelation on HLL Coif wavelet) is vendor-invariant. [PMID:35764743](../papers/35764743.md)

## Sources

- [PMID:39386723](../papers/39386723.md) — Multimodal Spatial Profiling Reveals Immune Suppression and Microenvironment Remodeling in Fallopian Tube Precursors to High-Grade Serous Ovarian Carcinoma (bioRxiv, 2024)
- [PMID:35764743](../papers/35764743.md) — Multimodal data integration using machine learning improves risk stratification of high-grade serous ovarian cancer; Boehm et al. 2022, Nature Cancer.

*This page was processed by **entity-page-writer** on **2026-04-15**.*
