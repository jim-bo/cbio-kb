---
name: Skin
oncotree_code: SKIN
main_type: Skin Cancer
parent: TISSUE
tags:
  - skin
  - normal-tissue
  - melanocyte
  - UV-damage
processed_by: crosslinker
processed_at: 2026-04-30
---

# Skin (SKIN)

## Overview

SKIN is the OncoTree tissue-level node representing cutaneous/skin tissue, classified under Skin Cancer in OncoTree (parent: TISSUE). In the cbio-kb corpus this code is used to represent normal cutaneous skin in the context of somatic mutation and melanocyte biology studies, distinct from the melanoma ([MEL](../cancer_types/MEL.md)) and cutaneous squamous cell carcinoma ([CSCC](../cancer_types/CSCC.md)) entity pages.

## Cohorts in the corpus

- Normal skin melanocyte atlas: 297 single melanocytes from 58 skin biopsies of 31 donors (UCSF Willed Body Program and Northwestern University dermatology clinic). Donors spanned ages and sun-exposure histories; one FFPE Xenium specimen was non-lesional adjacent skin from a [MEL](../cancer_types/MEL.md) patient (63-year-old male). Dataset: [normal_skin_melanocytes_2024](../datasets/normal_skin_melanocytes_2024.md) (dbGaP phs001979.v1.p1 and phs003683.v2.p1). [PMID:39975212](../papers/39975212.md)

## Recurrent alterations

This is primarily a normal-tissue atlas study; no somatic drivers are nominated in skin. Somatic mutations profiled are from normal sun-exposed melanocytes.

- UV-attributable signature SBS7 (C>T transitions at dipyrimidines): dominant in HighMut melanocytes from sun-damaged skin. [PMID:39975212](../papers/39975212.md)
- Clock-like signatures SBS1/SBS5: dominant in LowMut melanocytes, enriched in hair-follicle niches. [PMID:39975212](../papers/39975212.md)

## Subtypes

Two coexisting melanocyte subpopulations identified within sun-damaged skin:
- **HighMut melanocytes**: UV-signature dominant (SBS7), dendritic morphology, large, transcriptionally "differentiated"; reside in interfollicular epidermis; upregulate [HMOX1](../genes/HMOX1.md), [ABCC2](../genes/ABCC2.md), [MC1R](../genes/MC1R.md), [HERC2](../genes/HERC2.md). [PMID:39975212](../papers/39975212.md)
- **LowMut melanocytes**: clock-like signature dominant (SBS1/SBS5), smaller, less dendritic, "stem-like" / neural-crest-lineage; enriched in hair follicles; upregulate [VCAN](../genes/VCAN.md), [TAGLN](../genes/TAGLN.md), [SEMA3C](../genes/SEMA3C.md), [TCF4](../genes/TCF4.md). [PMID:39975212](../papers/39975212.md)

## Therapeutic landscape

- No therapeutic interventions reported in this corpus entry. Authors hypothesize that the hair-follicle LowMut melanocyte reservoir could be co-opted to replace UV-damaged cells, paralleling vitiligo phototherapy models, but no validated intervention is described. [PMID:39975212](../papers/39975212.md)

## Sources

- [PMID:39975212](../papers/39975212.md) — Tandukar et al. *Nature* 2025. Clonal single-cell profiling of normal skin melanocytes reveals UV-protected stem-cell niche in hair follicles.

*This page was processed by **crosslinker** on **2026-04-30**.*
