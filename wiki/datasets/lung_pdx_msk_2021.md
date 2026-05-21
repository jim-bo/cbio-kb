---
name: "SCLC Patient-Derived Xenograft Library (MSK, Nat Commun 2022)"
studyId: lung_pdx_msk_2021
institution: Memorial Sloan Kettering Cancer Center
size: 46
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - msk-impact-panel
  - rna-seq
  - immunohistochemistry
panels:
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - sclc
  - pdx
  - cdx
  - molecular-subtypes
  - neuroendocrine
  - pou2f3
  - multi-omics
processed_by: crosslinker
processed_at: 2026-05-21
---

# SCLC Patient-Derived Xenograft Library (MSK, Nat Commun 2022)

## Overview

`lung_pdx_msk_2021` is a Memorial Sloan Kettering resource of 46 small cell lung cancer ([SCLC](../cancer_types/SCLC.md)) patient-derived xenograft (PDX) and circulating tumor cell-derived xenograft (CDX) models from 33 patients, with paired clinical specimens for 18 cases. Multi-omic profiling — [MSK-IMPACT](../methods/msk-impact-panel.md) targeted DNA sequencing, bulk [RNA-seq](../methods/rna-seq.md), and IHC — confirmed retention of canonical [SCLC](../cancer_types/SCLC.md) genomic landscape and recapitulated the ASCL1/NEUROD1/POU2F3 transcriptional subtype framework in xenografts. Gene expression data are also deposited at ArrayExpress under accession E-MTAB-11230.

## Composition

- **n = 46** PDX/CDX models from 33 [SCLC](../cancer_types/SCLC.md) patients; 40/46 (87%) tissue-derived PDXs and 6/46 (13%) CDXs.
- **Patient cohort:** 55% male, 45% female; average age 66 at diagnosis; 82% current or former smokers; 58% extensive-stage, 42% limited-stage at presentation.
- **Cancer types:** primarily [SCLC](../cancer_types/SCLC.md); a subset of 4 never-smoker samples showed features consistent with histologic transformation from [LUAD](../cancer_types/LUAD.md).
- **Engraftment:** 45/198 (23.81%) pure SCLC samples and 13/29 (44.83%) mixed-histology samples successfully engrafted; mean engraftment time 112 days.
- **Key features:** includes 10 POU2F3-driven PDXs (SCLC-P subtype, all from one patient — MSK773), representing the first reported SCLC-P PDX models; 18 cases with paired clinical and matched PDX MSK-IMPACT data.

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — targeted NGS on 42 PDX and 26 clinical samples (341-, 410-, or 468-gene panel versions).
- [RNA-seq](../methods/rna-seq.md) — bulk transcriptomics on 43 PDXs (TruSeq Stranded mRNA; fusion calling via in-house metacaller).
- [Immunohistochemistry](../methods/immunohistochemistry.md) — protein-level subtype marker assessment on 37 PDX samples and 19 clinical samples.

## Papers using this cohort

- [PMID:35440124](../papers/35440124.md) — Caeser et al., *Nature Communications* 2022: Discovery study characterizing the 46 PDX/CDX models; confirmed near-universal [TP53](../genes/TP53.md) and [RB1](../genes/RB1.md) loss (92%/81% of clinical samples), ASCL1/NEUROD1/POU2F3 subtype recapitulation, and [YAP1](../genes/YAP1.md) protein absence across the cohort. [PMID:35440124](../papers/35440124.md)

## Notable findings derived from this cohort

- [TP53](../genes/TP53.md) and [RB1](../genes/RB1.md) alterations were retained in 90% and 76% of PDX samples, respectively; 89% of paired clinical-PDX pairs (16/18) retained alterations in both genes [PMID:35440124](../papers/35440124.md).
- 10 POU2F3-driven PDXs (MSK773 B–L) constitute the first SCLC-P (subtype P) PDX resource; all expressed [MYC](../genes/MYC.md) at protein and RNA level and upregulated YAP/TAZ downstream genes ([NOTCH2](../genes/NOTCH2.md), [NOTCH3](../genes/NOTCH3.md)) [PMID:35440124](../papers/35440124.md).
- [YAP1](../genes/YAP1.md) protein was consistently absent or very low across the cohort, questioning YAP1 IHC as a defining marker for the YAP1 SCLC subtype [PMID:35440124](../papers/35440124.md).
- The MSK773 case (SCLC-P) shared somatic mutations and copy-number changes between SCLC and admixed lung adenocarcinoma components, supporting clonal origin and possible type II pneumocyte cell of origin for SCLC-P [PMID:35440124](../papers/35440124.md).
- Two atypical clinical samples lacking [TP53](../genes/TP53.md) and [RB1](../genes/RB1.md) mutations harbored [KRAS](../genes/KRAS.md) and [MDM2](../genes/MDM2.md) co-amplifications, suggesting [MDM2](../genes/MDM2.md) amplification may phenocopy [TP53](../genes/TP53.md) inactivation [PMID:35440124](../papers/35440124.md).

## Sources

- cBioPortal study `lung_pdx_msk_2021`.
- ArrayExpress accession E-MTAB-11230 (gene expression data).
- Caeser R, et al. *Genomic and transcriptomic analysis of a library of small cell lung cancer patient-derived xenografts.* Nat Commun. 2022. [PMID:35440124](../papers/35440124.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
