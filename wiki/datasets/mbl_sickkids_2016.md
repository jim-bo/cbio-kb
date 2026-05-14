---
name: Medulloblastoma — SickKids 2016
studyId: mbl_sickkids_2016
institution: The Hospital for Sick Children (SickKids) / BC Cancer Agency
size: 46
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-genome-seq
  - whole-exome-seq
  - targeted-deep-amplicon-seq
  - rna-seq
panels: []
tags:
  - medulloblastoma
  - MBL
  - clonal-evolution
  - recurrence
  - paired-primary-recurrent
  - shh-pathway
  - therapy-resistance
processed_by: crosslinker
processed_at: 2026-05-14
---

# Medulloblastoma — SickKids 2016

## Overview

Whole-genome sequencing of 33 patient-matched primary/recurrence medulloblastoma ([MBL](../cancer_types/MBL.md)) pairs (46 total human samples) from a multi-institutional pediatric brain tumor cohort, combined with whole-exome sequencing of 3 FFPE pairs. The study was designed to characterize clonal evolution between diagnosis and relapse. Raw sequencing deposited at EGA (EGAD00001000946). Reference genome GRCh37/hg19.

## Composition

- **15 matched primary + recurrent pairs** with germline controls: [whole-genome-seq](../methods/whole-genome-seq.md).
- **18 matched primary + recurrent pairs** without germline: [whole-genome-seq](../methods/whole-genome-seq.md).
- **10 recurrence-only samples** with germline: whole-genome-seq.
- **3 FFPE matched pairs**: [whole-exome-seq](../methods/whole-exome-seq.md) (Nextera Rapid Capture).
- **Total human samples: 46** from 33 patients.
- All four medulloblastoma molecular subgroups represented (Shh, Wnt, Group 3, Group 4).
- Cancer type: [MBL](../cancer_types/MBL.md) (medulloblastoma).

## Assays / panels (linked)

- [whole-genome-seq](../methods/whole-genome-seq.md) (BWA / GRCh37-lite alignment; Strelka + MutationSeq for SNVs)
- [whole-exome-seq](../methods/whole-exome-seq.md) (Nextera Rapid Capture for FFPE pairs)
- [targeted-deep-amplicon-seq](../methods/targeted-deep-amplicon-seq.md) (192 patient-specific SNVs across 20 patients)
- [strelka](../methods/strelka.md) / [varscan](../methods/varscan.md) (variant calling)
- [titan-cna](../methods/titan-cna.md) (allele-specific copy-number)
- [pyclone](../methods/pyclone.md) / EXPANDS (clonal-prevalence inference)

## Papers using this cohort

- [PMID:26760213](../papers/26760213.md) — Morrissy et al. 2016, "Divergent clonal selection dominates medulloblastoma at recurrence," *Nature*.

## Notable findings derived from this cohort

- On average only 11.8% of somatic SNVs/indels are shared between matched diagnostic and recurrent tumors, demonstrating massive clonal divergence at relapse [PMID:26760213](../papers/26760213.md).
- Somatic mutational burden increases ~5-fold post-therapy in 13/15 patient pairs (P = 2.7 × 10⁻⁴); structural-variant burden also rises [PMID:26760213](../papers/26760213.md).
- Recurrence arises from pre-existing minor subclones (<5% at diagnosis) confirmed in 16/20 patients by ultra-deep targeted resequencing [PMID:26760213](../papers/26760213.md).
- TP53-pathway alterations (including [TP53](../genes/TP53.md) mutations) and [DYNC1H1](../genes/DYNC1H1.md)/chr14q deficits together affect 79% of recurrent Shh medulloblastoma [PMID:26760213](../papers/26760213.md).
- Drug-actionable targets at recurrence differ from those at diagnosis in the majority of patients (5/9 with any actionable alteration); 2/9 had a complete actionable-target switch [PMID:26760213](../papers/26760213.md).
- Branched clonal evolution demonstrated in all 14 germline-matched cases; Group 4 tumors significantly more heterogeneous at recurrence (Shannon Index, P = 0.029) [PMID:26760213](../papers/26760213.md).

## Sources

- [PMID:26760213](../papers/26760213.md)
- EGA: EGAD00001000946

*This page was processed by **crosslinker** on **2026-05-14**.*
