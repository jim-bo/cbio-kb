---
name: Normal Skin Melanocytes and Keratinocytes (2024)
studyId: normal_skin_melanocytes_2024
institution: Multi-institutional
size: 291
reference_genome: hg38
canonical_source: cbioportal
unverified: false
assays: [spatial-transcriptomics, whole-exome-seq]
panels: []
tags:
  - normal-tissue
  - skin
  - melanocytes
  - keratinocytes
  - csc-progression
  - single-cell
  - clonal-evolution
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Normal Skin Melanocytes and Keratinocytes (2024)

## Overview

Single-cell resolution clonal genomic study of normal skin cells (keratinocytes, melanocytes, fibroblasts) from 15 donors, combined with a matched cSCC-actinic keratosis (AK) cohort, to map the genetic evolution from normal keratinocytes to cutaneous squamous cell carcinoma. Data deposited in dbGaP (phs001979.v1.p1, phs003683.v2.p1, phs003282.v2.p1) and cBioPortal as `normal_skin_melanocytes_2024`. [PMID:39091884](../papers/39091884.md)

## Composition

- **Normal skin cells**: 137 keratinocytes, 131 melanocytes, and 23 fibroblasts from 22 biopsies across 15 donors (ages 35–95), profiled via clonal expansion and whole-exome sequencing (~95X coverage). [PMID:39091884](../papers/39091884.md)
- **cSCC-AK cohort**: 16 archival tissue cases with cSCC immediately adjacent to actinic keratosis (AK), sequenced with a cancer gene panel at ~380X depth. [PMID:39091884](../papers/39091884.md)

## Assays / panels (linked)

- Clonal expansion and whole-exome sequencing (~95X) for normal cells. [PMID:39091884](../papers/39091884.md)
- Cancer gene panel sequencing (~380X) for cSCC-AK cohort. [PMID:39091884](../papers/39091884.md)
- 10X Visium spatial transcriptomics on 5 cSCC-AK cases. [PMID:39091884](../papers/39091884.md)

## Papers using this cohort

- [PMID:39091884](../papers/39091884.md) — Genetic evolution of keratinocytes to cutaneous squamous cell carcinoma.
- [PMID:39975212](../papers/39975212.md) — Tandukar et al. 2025: Clonal joint DNA/RNA profiling of 297 single melanocytes from 58 skin biopsies of 31 donors identifies two coexisting subpopulations (HighMut and LowMut) with distinct UV mutational burdens, transcriptional states, and spatial niches; spatial Xenium profiling validates hair follicle as a UV-protected melanocyte stem-cell reservoir.

## Notable findings derived from this cohort

- Keratinocytes have lower mutation burdens (median 1.14 mut/Mb) vs. melanocytes (3.91 mut/Mb) despite shared UV exposure in basal epidermis. [PMID:39091884](../papers/39091884.md)
- Pathogenic mutations — especially dominant-negative [TP53](../genes/TP53.md) missense mutations — break UV repair capacity, producing the highest mutation burdens (up to 49.71 mut/Mb). [PMID:39091884](../papers/39091884.md)
- Cell-type-specific mutational signatures: keratinocytes show higher clock-like (SBS1, SBS5) vs. UV (SBS7a) signatures compared to melanocytes/fibroblasts. [PMID:39091884](../papers/39091884.md)
- AK-to-cSCC progression model: [TERT](../genes/TERT.md) promoter and [CDKN2A](../genes/CDKN2A.md) mutations emerged early (AK trunk), while [ARID2](../genes/ARID2.md) loss-of-function and RTK-RAS-MAPK activation marked the cSCC transition. [PMID:39091884](../papers/39091884.md)
- Within sun-damaged skin, HighMut melanocytes (UV signature SBS7-dominated, dendritic, differentiated) reside in the interfollicular epidermis; LowMut melanocytes (clock-like SBS1/SBS5-dominated, smaller, stem-like, neural-crest transcriptome) are concentrated in hair follicles — consistent with a model of follicular UV-protected stem-cell replenishment [PMID:39975212](../papers/39975212.md).
- HighMut melanocyte transcriptome upregulates pigmentation/metabolism genes ([HMOX1](../genes/HMOX1.md), [ABCC2](../genes/ABCC2.md), [MC1R](../genes/MC1R.md), [HERC2](../genes/HERC2.md)) and antigen-presentation markers; LowMut melanocytes upregulate neural-crest lineage genes ([VCAN](../genes/VCAN.md), [TAGLN](../genes/TAGLN.md), [SEMA3C](../genes/SEMA3C.md), [TCF4](../genes/TCF4.md)), aligning with MSC signatures from hair-follicle fetal atlases [PMID:39975212](../papers/39975212.md).
- 297 single melanocytes were profiled by clonal joint DNA/RNA amplification (G&T-Seq + SMART-Seq2) with whole-exome sequencing; a custom 360-gene spatial Xenium panel validated subpopulation spatial niche separation on FFPE skin in situ [PMID:39975212](../papers/39975212.md).
- 133 clonally expanded single melanocytes from 6 donors at 19 anatomic sites profiled by UCSF500 targeted sequencing + WES; mean 7.9 mut/Mb with UV-signature dominance; intermittently sun-exposed sites showed higher mutation burden than chronically exposed sites, mirroring melanoma anatomic distribution — [PMID:33029006](../papers/33029006.md)

## Sources

- cBioPortal study `normal_skin_melanocytes_2024` [PMID:39091884](../papers/39091884.md).
- Tandukar et al. single-melanocyte atlas, with data at dbGaP `phs001979.v1.p1` / `phs003683.v2.p1` (single-cell DNA/RNA) and GEO `GSE286964` (Xenium spatial) [PMID:39975212](../papers/39975212.md).

*This page was processed by **crosslinker** on **2026-04-30**.*
- [PMID:33029006](../papers/33029006.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
