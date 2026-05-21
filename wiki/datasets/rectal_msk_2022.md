---
name: "Rectal Cancer (MSK, Nature Medicine 2022)"
studyId: rectal_msk_2022
institution: "Memorial Sloan Kettering Cancer Center"
size: 738
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-ngs
  - whole-exome-seq
  - rna-seq
panels:
  - msk-impact-panel
tags:
  - rectal-cancer
  - READ
  - LARC
  - neoadjuvant
  - MSK-IMPACT
  - immune-profiling
  - KRAS
  - APC
processed_by: crosslinker
processed_at: 2026-05-21
---

# Rectal Cancer (MSK, Nature Medicine 2022)

## Overview

`rectal_msk_2022` is the largest multi-cohort genomic and transcriptomic profiling study of rectal adenocarcinoma, assembled at Memorial Sloan Kettering Cancer Center (MSK). It pools four clinical/research cohorts — ACOSOG Z6041, TIMING, MSK-Research, and MSK-Clinical — comprising 738 rectal adenocarcinoma patients. The primary scientific aim was to identify genomic and transcriptomic correlates of response to neoadjuvant therapy (NAT) in locally advanced rectal cancer (LARC). The dataset includes DNA sequencing (MSK-IMPACT), whole-exome sequencing, RNA-Seq, and clinical annotations including NAT regimen, tumor location, and treatment response. Data are published to cBioPortal as `rectal_msk_2022`.

## Composition

- **738 rectal adenocarcinoma patients** from four sources [PMID:35970919](../papers/35970919.md):
  - ACOSOG Z6041 (NCT00114231): n=25
  - TIMING (NCT00335816): n=71
  - MSK-Research (MSK-R): n=163
  - MSK-Clinical (MSK-C): n=479
- **Cancer type:** [READ](../cancer_types/READ.md) — rectal adenocarcinoma.
- **692 pre-treatment primary tumors** sequenced with the [MSK-IMPACT panel](../methods/msk-impact-panel.md) (341–505 cancer-related genes). Stage distribution: I=78, II=77, III=375, IV=162.
- **Anatomic location:** Lower rectum (LR, 0–4 cm from anal verge) n=257; Middle rectum (MR, 4–8 cm) n=197; Upper rectum (UR, 8–12 cm) n=204; unknown n=34.
- **MMR status:** 652/692 (94.2%) pMMR/MSS; 36/692 (5.2%) dMMR/MSI; 4/692 (0.6%) [POLE](../genes/POLE.md) hypermutant.
- **Whole-exome sequencing:** 97 tumors (mutational signature analysis).
- **RNA-Seq:** 114 pre-treatment endoscopic biopsies; 97 with NAT outcome data; 87 with paired DNA, RNA, and outcomes.
- **Outcome-focused subset:** 346 stage II–III LARC patients (290 pMMR/MSS with MSK-IMPACT) from TIMING, MSK-R, and MSK-C; median follow-up 45.2 months.
- **Comparator:** 178 proximal colon + 204 distal colon tumors from the published MSK-Colon cohort (identical MSK-IMPACT methods).

## Assays / panels (linked)

- [MSK-IMPACT panel](../methods/msk-impact-panel.md) — 341–505 cancer-related genes; primary sequencing platform.
- [Whole-exome-seq](../methods/whole-exome-seq.md) — subset of 97 tumors for mutational signature analysis.
- [RNA-Seq](../methods/rna-seq.md) — 114 pre-treatment biopsies for transcriptomic and immune profiling; ssGSEA used for immune deconvolution.

## Papers using this cohort

- [PMID:35970919](../papers/35970919.md) — Chatila et al., Nature Medicine 2022: primary publication characterizing the genomic and transcriptomic landscape of rectal adenocarcinoma, predictors of NAT response, and immune-hot pMMR/MSS subset identification.

## Notable findings derived from this cohort

- pMMR/MSS rectal cancer (n=652): most frequently altered genes were [APC](../genes/APC.md) (81%), [TP53](../genes/TP53.md) (81%), [KRAS](../genes/KRAS.md) (42%), [FBXW7](../genes/FBXW7.md) (14%), [PIK3CA](../genes/PIK3CA.md) (12%); top pathways WNT (85%), [TP53](../genes/TP53.md) (82%), RAS (51%) [PMID:35970919](../papers/35970919.md).
- [APC](../genes/APC.md)/WNT alteration frequency declined significantly toward the anal verge (upper rectum 92% / middle 90% / lower 77%, p<0.001), with APC-altered tumors sitting a median 6.85 cm vs 4 cm from the anal verge (p<0.001); replicated in an independent 157-patient MSK cohort [PMID:35970919](../papers/35970919.md).
- [KRAS](../genes/KRAS.md) mutations (42% of pMMR/MSS) predicted significantly shorter disease-free survival specifically in CRT-CNCT-treated patients (p=0.004) but not in INCT-CRT-treated patients, establishing [KRAS](../genes/KRAS.md) as a treatment-specific rather than treatment-agnostic prognostic biomarker in LARC [PMID:35970919](../papers/35970919.md).
- ~8% of pMMR/MSS tumors (n=7/96) formed an immune-hot cluster (IG3) with overexpression of [PDCD1](../genes/PDCD1.md), [CD274](../genes/CD274.md), [CTLA4](../genes/CTLA4.md), [HAVCR2](../genes/HAVCR2.md), and [LAG3](../genes/LAG3.md) — a candidate subpopulation for ICI trials in otherwise ICI-refractory pMMR/MSS LARC; replicated in 42 TCGA LARC cases [PMID:35970919](../papers/35970919.md).
- Transcriptomic profiling identified [IGF2](../genes/IGF2.md) and [L1CAM](../genes/L1CAM.md) overexpression as markers of incomplete response to NAT, both validated in an independent Kamran et al. cohort (n=15) [PMID:35970919](../papers/35970919.md).

## Sources

- cBioPortal study: `rectal_msk_2022`

*This page was processed by **crosslinker** on **2026-05-21**.*
