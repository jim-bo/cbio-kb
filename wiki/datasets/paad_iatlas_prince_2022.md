---
name: Metastatic Pancreatic Adenocarcinoma (PRINCE Trial, Nat Med. 2022) - iAtlas Harmonized
studyId: paad_iatlas_prince_2022
institution: Multi-institutional PRINCE trial (Parker Institute for Cancer Immunotherapy consortium, 7 US academic centers); reprocessed by CRI iAtlas
size: 93
reference_genome: hg38
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - rna-seq
panels: []
tags:
  - pancreatic-cancer
  - PAAD
  - immunotherapy
  - nivolumab
  - sotigalimab
  - clinical-trial
processed_by: crosslinker
processed_at: 2026-09-11
---

# Metastatic Pancreatic Adenocarcinoma (PRINCE Trial, Nat Med. 2022) - iAtlas Harmonized

## Overview

PRINCE (NCT03214250): a randomized, open-label phase 1b/2 trial of first-line metastatic pancreatic ductal adenocarcinoma ([PAAD](../cancer_types/PAAD.md)) testing gemcitabine/nab-paclitaxel chemotherapy combined with [nivolumab](../drugs/nivolumab.md) (anti-PD-1), [sotigalimab](../drugs/sotigalimab.md) (CD40 agonist), or both. Conducted by the Parker Institute for Cancer Immunotherapy (PICI) pancreas cancer consortium at 7 US academic centers; sequencing data reprocessed and harmonized by CRI iAtlas. Name, institution, size (93) and reference genome (hg38) are taken from the cBioPortal study record in `schema/ontology/studies.json` [PMID:35662283](../papers/35662283.md).

## Composition

- 130 patients assessed for eligibility; 99 randomized in phase 2 (37 nivo/chemo, 31 sotiga/chemo, 31 sotiga/nivo/chemo); efficacy population n=105, safety population n=108 [PMID:35662283](../papers/35662283.md).
- 63 (60%) patients had pre-treatment tumor of sufficient quality for whole-exome sequencing; treatment arms were balanced for somatic mutation frequencies in *[KRAS](../genes/KRAS.md)*, *[SMAD4](../genes/SMAD4.md)* and *[TP53](../genes/TP53.md)*, with a single MSI-high tumor and a single pathogenic *[BRCA2](../genes/BRCA2.md)* variant [PMID:35662283](../papers/35662283.md).

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md) and transcriptome sequencing of tumor/normal pairs via ImmunoID NeXT (Personalis); bulk tumor [RNA-seq](../methods/rna-seq.md) (liver-metastasis biopsies only) [PMID:35662283](../papers/35662283.md).
- Seven-color [multiplexed immunofluorescence](../methods/multiplexed-immunofluorescence.md), 28-color multiparameter flow cytometry, [mass cytometry (CyTOF)](../methods/mass-cytometry.md), and Olink proximity-extension serum proteomics of paired blood/tumor biospecimens [PMID:35662283](../papers/35662283.md).

## Papers using this cohort

- [PMID:35662283](../papers/35662283.md) — PRINCE trial investigators, source publication: reports the randomized phase 1b/2 efficacy comparison and multi-omic biomarker analysis.

## Notable findings derived from this cohort

- In 105 efficacy-evaluable patients, the 1-year OS primary endpoint (vs. 35% historical control) was met for nivo/chemo (57.7%, P=0.006) but not for sotiga/chemo (48.1%, P=0.062) or the triple combination (41.3%, P=0.233) [PMID:35662283](../papers/35662283.md).
- Pre-treatment circulating T cell diversity (especially [CD4](../genes/CD4.md) subsets) correlated with survival for nivo/chemo, while cross-presenting dendritic cells plus circulating/tumor CD4 T cell activity correlated with survival for sotiga/chemo; the triple-combination arm showed no clear predictive biomarker and signs of possible immune over-activation [PMID:35662283](../papers/35662283.md).

## Sources

- cBioPortal study record: `paad_iatlas_prince_2022` (name, institution, size, reference_genome taken from `schema/ontology/studies.json`).
- [PMID:35662283](../papers/35662283.md)

*This page was processed by **crosslinker** on **2026-09-11**.*
