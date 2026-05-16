---
name: "MSK Pediatric Clonal Hematopoiesis / Therapy-Related Leukemia Surveillance (2021)"
studyId: msk_ch_ped_2021
institution: "Memorial Sloan Kettering Cancer Center"
size: 657
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
  - rna-seq
panels:
  - msk-hemepact
  - msk-impact-panel
  - archer-fusionplex
tags:
  - pediatric-oncology
  - clonal-hematopoiesis
  - therapy-related-leukemia
  - neuroblastoma
  - longitudinal-surveillance
  - bone-marrow
  - msk-impact
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK Pediatric Clonal Hematopoiesis / Therapy-Related Leukemia Surveillance (2021)

## Overview

Two-cohort dataset from Memorial Sloan Kettering Cancer Center characterizing clonal hematopoiesis (CH) and therapy-related myeloid neoplasms (t-MDS/AL) in pediatric cancer survivors. The primary cohort comprises 52 high-risk neuroblastoma ([NBL](../cancer_types/NBL.md)) patients with 199 serial bone-marrow samples profiled by HemePACT targeted DNA capture and ArcherDX FusionPlex RNA sequencing. The extended cBioPortal-deposited cohort covers 657 pediatric solid-tumor patients (≤25 years) profiled by [MSK-IMPACT](../methods/msk-impact-panel.md), enabling single-timepoint CH prevalence estimates across tumor types. [PMID:35078859](../papers/35078859.md)

## Composition

- Extended cBioPortal cohort: 657 pediatric solid-tumor patients ≤25 years seen in MSKCC Pediatrics — 144 [NBL](../cancer_types/NBL.md) plus 513 other solid tumors — profiled by [MSK-IMPACT](../methods/msk-impact-panel.md). [PMID:35078859](../papers/35078859.md)
- Primary longitudinal cohort (not all in cBioPortal): 52 high-risk [NBL](../cancer_types/NBL.md) patients (diagnosed 1988–2009), 199 serial bone-marrow samples.
  - Transformation cohort ([TMN](../cancer_types/TMN.md)/[AML](../cancer_types/AML.md)/[MDS](../cancer_types/MDS.md)): 17 patients, 88 samples.
  - Transient cytogenetic abnormality cohort: 14 patients, 74 samples.
  - Neuroblastoma-treated control cohort: 21 patients, 37 samples.
- Reference genome: NCBI build 37 (BWA v0.7.17); variant calling with CaVEMan, Mutect, Strelka, Pindel. [PMID:35078859](../papers/35078859.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — 341/410/468-gene tumor + matched-blood panel on the 657-patient solid-tumor cohort.
- [HemePACT](../methods/msk-hemepact.md) v3/v4 — 585/576-gene hematologic-malignancy targeted DNA capture on serial BM samples (median 705× coverage).
- [ArcherDX FusionPlex Pan-Heme](../methods/archer-fusionplex.md) — RNA panel for recurrent fusions, including detection of novel [KMT2A](../genes/KMT2A.md) partners.
- [Droplet digital PCR](../methods/droplet-digital-pcr.md) — [TP53](../genes/TP53.md) hotspot backtracking on 28 additional time points.

## Papers using this cohort

- [PMID:35078859](../papers/35078859.md) — Spitzer et al. (2022) — primary study identifying pre-leukemic clones in pediatric [NBL](../cancer_types/NBL.md) survivors and estimating CH-PD prevalence in the extended solid-tumor cohort.

## Notable findings derived from this cohort

- Only 1.05% (7/657) of pediatric solid-tumor patients had clonal hematopoiesis involving myeloid genes (CH-PD) at single timepoint MSK-IMPACT profiling — vs. 17.6% in patients >25 years in the same dataset; argues for longitudinal rather than single-timepoint surveillance in pediatric survivors. [PMID:35078859](../papers/35078859.md)
- In the longitudinal NBL cohort, at least one t-MDS/AL-associated mutation was detected in 13/17 transformation patients a median of 15 months before overt leukemia diagnosis (range 1.3–32.4 months); relative risk for t-MDS/AL given an oncogenic mutation was 8.8 (95% CI 1.3–57.8, p<0.001). [PMID:35078859](../papers/35078859.md)
- [TP53](../genes/TP53.md) clones were only detectable after initiation of cytotoxic therapy in all 5 pediatric cases — a pattern distinct from adult CH — and expanded preferentially during chemotherapy/radiation windows. [PMID:35078859](../papers/35078859.md)
- [KMT2A](../genes/KMT2A.md) rearrangements were the most common structural driver (6/17 transformation patients); ArcherDX RNA capture detected 5/6 rearrangements a median of 28.5 months before diagnosis, vs. only 2/6 by conventional cytogenetics. Novel fusion partners [PRDM10](../genes/PRDM10.md) and [DDX6](../genes/DDX6.md) identified. [PMID:35078859](../papers/35078859.md)

## Sources

- cBioPortal study: `msk_ch_ped_2021` (https://www.cbioportal.org/study/summary?id=msk_ch_ped_2021)
- Primary publication: [PMID:35078859](../papers/35078859.md) · DOI: 10.1158/1078-0432.CCR-21-2451 · *Clinical Cancer Research* (2022)

*This page was processed by **crosslinker** on **2026-05-16**.*
