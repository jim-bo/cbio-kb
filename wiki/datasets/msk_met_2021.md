---
name: "MSK-MET: Pan-Cancer Metastatic Cohort (MSK, 2021)"
studyId: msk_met_2021
institution: "Memorial Sloan Kettering Cancer Center"
size: 25775
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
panels:
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - pan-cancer
  - metastasis
  - organotropism
  - chromosomal-instability
  - msk-impact
  - prospective
  - ehr-linked
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK-MET: Pan-Cancer Metastatic Cohort (MSK, 2021)

## Overview

MSK-MET is a prospective pan-cancer cohort of 25,775 patients across 50 tumor types, all profiled with [MSK-IMPACT](../methods/IMPACT468.md) targeted sequencing (341–468-gene panels: [IMPACT341](../methods/IMPACT341.md), [IMPACT410](../methods/IMPACT410.md), [IMPACT468](../methods/IMPACT468.md)) between November 2013 and January 2020 at Memorial Sloan Kettering Cancer Center. The cohort includes 15,632 (61%) primary and 10,143 (39%) metastatic specimens, linked to 99,419 EHR-derived metastatic events across 21 anatomic sites from 21,546 metastatic patients. It is the largest linked genomic-metastatic dataset enabling genome-wide analysis of organotropism and chromosomal instability as determinants of metastatic propensity. An independent validation cohort of 9,215 samples (January 2020–August 2021) was also assembled. [PMID:35120664](../papers/35120664.md)

## Composition

- 25,775 patients spanning 50 tumor types; 15,632 primary and 10,143 metastatic specimens. [PMID:35120664](../papers/35120664.md)
- Most common metastatic biopsy sites: lymph nodes (n=2,305, 23%), liver (n=2,289, 23%), lung (n=982, 10%), bone (n=726, 7%). [PMID:35120664](../papers/35120664.md)
- Median sequencing coverage 653× (IQR 525–790); median tumor purity 40% (IQR 20–50%); median sample-to-sequencing interval 62 days. [PMID:35120664](../papers/35120664.md)
- Median age at sequencing 64 years; median follow-up 30 months; five-year survival 40% (range: 90% testicular seminoma to 10% pancreatic adenocarcinoma). [PMID:35120664](../papers/35120664.md)
- Allele-specific copy-number analysis on n=17,224 samples by [FACETS](../methods/facets.md) for purity/ploidy-adjusted [FGA](../genes/FGA.md), whole-genome doubling (WGD), and clonality estimates. [PMID:35120664](../papers/35120664.md)
- 99,419 metastatic events from EHR mapped to 21 reference anatomic locations. [PMID:35120664](../papers/35120664.md)
- Cancer types represented include [LUAD](../cancer_types/LUAD.md), [PRAD](../cancer_types/PRAD.md), [IDC](../cancer_types/IDC.md), [ILC](../cancer_types/ILC.md), [COAD](../cancer_types/COAD.md), [PAAD](../cancer_types/PAAD.md), [BLCA](../cancer_types/BLCA.md), [SKCM](../cancer_types/SKCM.md), [HGSOC](../cancer_types/HGSOC.md), [THPA](../cancer_types/THPA.md), [HNSC](../cancer_types/HNSC.md), [UEC](../cancer_types/UEC.md), [PANET](../cancer_types/PANET.md), [SCLC](../cancer_types/SCLC.md), and 36 others. [PMID:35120664](../papers/35120664.md)

## Assays / panels (linked)

- [IMPACT341](../methods/IMPACT341.md) / [IMPACT410](../methods/IMPACT410.md) / [IMPACT468](../methods/IMPACT468.md) — MSK-IMPACT targeted DNA sequencing panels identifying somatic mutations, rearrangements, and copy-number alterations.
- [FACETS](../methods/facets.md) — allele-specific copy-number analysis for FGA, WGD, purity, ploidy, and clonality on a subset of n=17,224 samples.

## Papers using this cohort

- [PMID:35120664](../papers/35120664.md) — Nguyen et al. (2022) — primary study characterizing pan-cancer genomic determinants of metastatic patterns, organotropism, and metastatic burden.

## Notable findings derived from this cohort

- Metastases are significantly more chromosomally unstable (higher FGA) than primaries in 16 of 50 tumor types; whole-genome doubling is more frequent in metastases in 7 tumor types. [PMID:35120664](../papers/35120664.md)
- TMB is higher in metastases in 10 tumor types; TMB-high rates rose from 19% to 27% in [LUAD](../cancer_types/LUAD.md) and from 2% to 7% in HR+/HER2- ductal breast (q<0.001). [PMID:35120664](../papers/35120664.md)
- FGA correlates with metastatic burden pan-cancer and in 11 individual tumor types; strongest in [PRAD](../cancer_types/PRAD.md) (rho=0.33, q=7.0E-45). No association in MSS [COAD](../cancer_types/COAD.md). [PMID:35120664](../papers/35120664.md)
- 67 statistically significant oncogenic-alteration frequency differences between primaries and metastases across 17 tumor types; 53 enriched in metastases — including [AR](../genes/AR.md) amplification/mutations in [PRAD](../cancer_types/PRAD.md) and [ESR1](../genes/ESR1.md) mutations in HR+/HER2- breast. [PMID:35120664](../papers/35120664.md)
- 57 oncogenic alterations and 48 oncogenic-pathway associations linked to specific organ-site metastasis across 10 and 12 tumor types, including [EGFR](../genes/EGFR.md)/[TP53](../genes/TP53.md) in [LUAD](../cancer_types/LUAD.md) CNS mets and WNT pathway/[CTNNB1](../genes/CTNNB1.md)/[APC](../genes/APC.md) in [PRAD](../cancer_types/PRAD.md) lung mets. [PMID:35120664](../papers/35120664.md)
- Higher metastatic burden associated with shorter overall survival in 39 of 50 (78%) tumor types. [PMID:35120664](../papers/35120664.md)

## Sources

- cBioPortal study: `msk_met_2021` (https://www.cbioportal.org/study?id=msk_met_2021)
- Zenodo: DOI 10.5281/zenodo.5801902
- Primary publication: [PMID:35120664](../papers/35120664.md) · DOI: 10.1016/j.cell.2022.01.003 · *Cell* (2022)

*This page was processed by **crosslinker** on **2026-05-16**.*
