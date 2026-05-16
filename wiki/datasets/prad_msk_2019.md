---
name: Prostate Cancer Hyperpolarized MRI Cohort (MSK, 2019)
studyId: prad_msk_2019
institution: Memorial Sloan Kettering Cancer Center
size: 12
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-ngs
  - hyperpolarized-13c-mri
  - immunohistochemistry
panels:
  - msk-impact-panel
tags:
  - prostate-cancer
  - prad
  - hyperpolarized-mri
  - metabolic-imaging
  - biomarker
processed_by: crosslinker
processed_at: 2026-05-16
---

# Prostate Cancer Hyperpolarized MRI Cohort (MSK, 2019)

## Overview

A prospective imaging-genomics cohort of 12 men with biopsy-proven [prostate adenocarcinoma (PRAD)](../cancer_types/PRAD.md) imaged with hyperpolarized [1-13C] pyruvate MRI immediately before radical prostatectomy at Memorial Sloan Kettering Cancer Center (IRB#14–205; NCT02421380; enrolled May 2015–July 2018). Targeted sequencing via [MSK-IMPACT](../methods/msk-impact-panel.md) (468-gene [IMPACT468](../methods/IMPACT468.md) panel) was performed on all resected specimens. Raw IMPACT data are deposited at EVA accession PRJEB33969 and as cBioPortal study `prad_msk_2019`. The dataset links non-invasive metabolic imaging to genomic and histological features of localized prostate cancer [PMID:31564440](../papers/31564440.md).

## Composition

- **12 patients** with histologically confirmed prostate adenocarcinoma (>1 cm), scheduled for radical prostatectomy; mean age 62 ± 7 yrs [PMID:31564440](../papers/31564440.md).
- **17 hyperpolarized [1-13C] pyruvate MRI injections** (5 patients imaged twice for test/re-test reproducibility) [PMID:31564440](../papers/31564440.md).
- **Cancer type:** [Prostate adenocarcinoma (PRAD)](../cancer_types/PRAD.md); Gleason grades 3–5; whole-mount step-section prostatectomy pathology [PMID:31564440](../papers/31564440.md).
- **Genomic profiling:** 12 patients by [MSK-IMPACT](../methods/msk-impact-panel.md) [IMPACT468](../methods/IMPACT468.md); allele-specific copy number by [FACETS](../methods/facets.md) [PMID:31564440](../papers/31564440.md).

## Assays / panels (linked)

- [Hyperpolarized 13C MRI](../methods/hyperpolarized-13c-mri.md) — 3T wide-bore scanner with dual-tuned ¹H/¹³C endorectal coil; 2D dynamic EPSI at 1×1×1.5-cm³ voxels, 4.9-s temporal resolution; 0.43 mL/kg of 250 mM [1-13C] pyruvate IV [PMID:31564440](../papers/31564440.md).
- [MSK-IMPACT](../methods/msk-impact-panel.md) [IMPACT468](../methods/IMPACT468.md) — 468-gene hybridization-capture targeted sequencing with FACETS for allele-specific copy number [PMID:31564440](../papers/31564440.md).
- [Immunohistochemistry](../methods/immunohistochemistry.md) — MCT1 ([SLC16A1](../genes/SLC16A1.md)) at 1:100 dilution on whole-mount prostatectomy sections [PMID:31564440](../papers/31564440.md).

## Papers using this cohort

- [PMID:31564440](../papers/31564440.md) — Granlund, Tee et al. Hyperpolarized MRI of prostate cancer at MSK; demonstrates Lac_max rises with Gleason grade, is driven by MCT1/SLC16A1, and tracks with homozygous [PTEN](../genes/PTEN.md) loss.

## Notable findings derived from this cohort

- Maximum lactate ratio (Lac_max) was significantly higher in tumor regions than normal prostate (p=0.0001 for Gleason grade 3; p<0.0001 for Gleason ≥4) and rose with increasing Gleason grade [PMID:31564440](../papers/31564440.md).
- Test/re-test reproducibility confirmed: neither time-to-max pyruvate, time-to-max lactate, nor Lac_max differed significantly between paired injections after perfusion correction (p=0.24, p=0.78, p=0.2 respectively) [PMID:31564440](../papers/31564440.md).
- MCT1 ([SLC16A1](../genes/SLC16A1.md)) IHC-positive ROIs had Lac_max 60% higher than low-MCT1 ROIs (0.38±0.3 vs. 0.23±0.04; P=0.028), identifying MCT1 as the rate-limiting transporter driving the HP lactate signal in vivo [PMID:31564440](../papers/31564440.md).
- Homozygous [PTEN](../genes/PTEN.md) loss (n=2 ROIs by IMPACT468/FACETS) tracked with the highest Lac_max (P=0.059), suggesting HP-MRI as a non-invasive readout of PI3K-pathway activation [PMID:31564440](../papers/31564440.md).
- [TMPRSS2](../genes/TMPRSS2.md)-[ERG](../genes/ERG.md) fusion status did not segregate Lac_max in this 12-patient cohort [PMID:31564440](../papers/31564440.md).

## Sources

- cBioPortal study: `prad_msk_2019`
- EVA accession: PRJEB33969
- Primary publication: [PMID:31564440](../papers/31564440.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
