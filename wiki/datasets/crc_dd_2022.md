---
name: "CRC Dual Driver Mutations (MSK, JCO PO 2022)"
studyId: crc_dd_2022
institution: Memorial Sloan Kettering Cancer Center
size: 47
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - msk-impact-panel
  - single-cell-genotyping
  - facets
  - absolute
  - sanger-sequencing
  - msi-pcr-pentaplex
panels: []
tags:
  - colorectal-cancer
  - dual-driver-mutations
  - RAS-hotspot
  - BRAF-V600E
  - mutual-exclusivity
  - microsatellite-instability
processed_by: crosslinker
processed_at: 2026-05-21
---

# CRC Dual Driver Mutations (MSK, JCO PO 2022)

## Overview

`crc_dd_2022` is a Memorial Sloan Kettering dataset comprising 47 treatment-naive colorectal cancer (CRC) patients who harbor concurrent (dual) RAS hotspot and/or [BRAF](../genes/BRAF.md) V600E driver mutations — a phenotype designated CRC-DD. These cases were identified by screening 4,561 CRC patients sequenced with [MSK-IMPACT](../methods/msk-impact-panel.md) at MSK and represent 1.03% of the full clinical cohort (the larger cohort is documented as [msk_impact_2017](../datasets/msk_impact_2017.md)). The dataset was released to support study of MAPK dosage biology and same-cell co-occurrence of dual oncogenic drivers.

## Composition

- **n = 47** CRC patients with dual RAS hotspot/BRAF V600E mutations (CRC-DD); predominantly primary tumor specimens (89.3% vs 59.4% in single-driver CRC, P=.0001).
- **Cancer type:** colorectal adenocarcinoma ([COAD](../cancer_types/COAD.md)) / [COADREAD](../cancer_types/COADREAD.md); subset includes [READ](../cancer_types/READ.md).
- **Dual-driver composition:** 32 dual [KRAS](../genes/KRAS.md)/KRAS, 11 [KRAS](../genes/KRAS.md)/[NRAS](../genes/NRAS.md), 2 KRAS/BRAF V600E, 1 NRAS/BRAF V600E, 1 dual NRAS/NRAS.
- **MSI-H prevalence:** 27% of CRC-DD cases vs 8.7% in single-driver CRC (P=.0004).

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — 468-gene targeted NGS panel for somatic mutations, CNAs, [select](../methods/select.md) fusions, and MSI status.
- [Single-cell genotyping (SCG)](../methods/single-cell-genotyping.md) — performed on 2,094 cells from 4 CRC-DD cases; FACS-isolated nuclei, multiplexed PCR, β-binomial mixture model genotype calling.
- [FACETS](../methods/facets.md) — clonality and allelic imbalance estimation.
- [ABSOLUTE](../methods/absolute.md) — cancer cell fraction re-estimation on SCG-genotyped mutations.
- [Sanger sequencing](../methods/sanger-sequencing.md) — technical and biological validation of SCG calls.

## Papers using this cohort

- [PMID:35235413](../papers/35235413.md) — Gularte-Mérida et al., *JCO Precision Oncology* 2022: Discovery study defining the CRC-DD phenotype; 47 cases identified from 4,561 MSK-IMPACT CRC patients; single-cell genotyping confirmed same-cell co-occurrence of dual drivers in 14%–95% of tumor cells across four cases. [PMID:35235413](../papers/35235413.md)

## Notable findings derived from this cohort

- 47/4,561 (1.03%) of CRC cases harbored dual RAS hotspot/BRAF V600E driver mutations; BRAF V600E + RAS co-occurrence was extremely rare (3/4,561, 0.06%) [PMID:35235413](../papers/35235413.md).
- Single-cell genotyping demonstrated same-cell co-occurrence of dual drivers in 14%–95% of tumor cells across four CRC-DD cases, directly contradicting MAPK-driver mutual exclusivity dogma [PMID:35235413](../papers/35235413.md).
- CRC-DD showed lower allelic imbalance favoring the oncogenic allele (32.5% vs 51.3% in single-driver CRC, P=.0026) and lower fraction of genome altered (P=7.99×10⁻⁹) [PMID:35235413](../papers/35235413.md).
- MSI-H enrichment in CRC-DD (27% vs 8.7%, P=.0004) and enrichment of C→T/G→A transitions suggest MMR-deficiency signature preceded MAPK mutations chronologically [PMID:35235413](../papers/35235413.md).

## Sources

- cBioPortal study `crc_dd_2022`.
- Gularte-Mérida R, et al. *Same-Cell Co-Occurrence of RAS Hotspot and BRAF V600E Mutations in Treatment-Naive Colorectal Cancer.* JCO Precis Oncol. 2022. [PMID:35235413](../papers/35235413.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
