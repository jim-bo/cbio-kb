---
name: "Acute Myeloid Leukemia (OHSU, Cancer Cell 2022)"
studyId: aml_ohsu_2022
institution: "Oregon Health & Science University (OHSU) and 9 partner sites"
size: 942
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - rna-seq
  - ex-vivo-drug-sensitivity-screen
panels: []
tags:
  - AML
  - beat-aml
  - functional-genomics
  - drug-sensitivity
  - ex-vivo
  - PEAR1
processed_by: crosslinker
processed_at: 2026-05-21
---

# Acute Myeloid Leukemia (OHSU, Cancer Cell 2022)

## Overview

The Beat [AML](../cancer_types/AML.md) 2.0 dataset (`aml_ohsu_2022`) is the expanded, harmonized version of the Beat AML functional-genomic resource, produced by the Druker/Tyner labs at OHSU in collaboration with nine partner sites. It unifies four accrual waves — Waves 1+2 (the original [aml_ohsu_2018](../datasets/aml_ohsu_2018.md) cohort published by Tyner et al. 2018) with two new Waves 3+4 — into a single cBioPortal study of 942 specimens from 805 AML patients with paired ex vivo drug-sensitivity screening, DNA sequencing (custom 11.9 Mb capture library), and RNA-Seq. It represents one of the largest multi-omic, functional-genomic AML datasets available publicly. Data are accessible at cBioPortal and at Vizome (www.vizome.org/aml2); raw data reside in dbGaP study ID 30641 (phs001657.v2.p1) and the Genomic Data Commons.

## Composition

- **942 specimens from 805 patients** — real-world AML cohort (de novo, transformed, and therapy-related; 70% collected at initial diagnosis) [PMID:35868306](../papers/35868306.md).
- **Waves 3+4 contribution:** 293 specimens from 279 patients (243 unique to Waves 3+4), collected over 2.5 years.
- **Analysis subset:** Cohort-level analyses restricted to first-timepoint specimen per patient, excluding remission samples.
- **Cancer type:** [AML](../cancer_types/AML.md) — acute myeloid leukemia.
- **Key clinical fields:** ELN 2017 risk category (initial-diagnosis specimens only), FAB classification, specimen type (bone marrow / peripheral blood), age, ethnicity; structured clinical elements extracted from EHR notes via NLP (Linguamatics I2E + Python; accuracy 79–93%, precision 85–96%).
- **Stage/setting:** Predominantly treatment-naive; both academic center and community-hospital patients.

## Assays / panels (linked)

- [Ex vivo drug sensitivity screen](../methods/ex-vivo-drug-sensitivity-screen.md) — probit dose-response curve fitting across a broad drug panel; extended from Waves 1+2 protocol.
- [RNA-Seq](../methods/rna-seq.md) — conditional quantile normalization (CQN) parameters carried over from Waves 1+2 for cross-wave comparability; used for WGCNA module construction and single-cell maturation-state deconvolution.
- [Whole-exome-seq](../methods/whole-exome-seq.md) — upgraded in Waves 3+4 to a custom 11.9 Mb capture library covering all variants previously reported in AML (extending the WES panel used in Waves 1+2).
- FLT3-ITD and [NPM1](../genes/NPM1.md) 4-bp insertion calls via PCR amplicon size-based methodology.

## Papers using this cohort

- [PMID:35868306](../papers/35868306.md) — Bottomly et al., Cancer Cell 2022: primary publication describing the expanded Beat AML 2.0 resource, [PEAR1](../genes/PEAR1.md) as an AML prognostic hub, cell-state–drug sensitivity interactions, and pharmacogenomic associations.

## Notable findings derived from this cohort

- The cumulative harmonized cohort of 942 specimens from 805 AML patients was published as this cBioPortal study; 89% concordance for mutation–drug-sensitivity associations and 98% concordance for WGCNA-eigengene–drug-response associations between Waves 1+2 and Waves 3+4 validated cross-wave reproducibility [PMID:35868306](../papers/35868306.md).
- WGCNA module 3 hub gene [PEAR1](../genes/PEAR1.md) (a.k.a. JEDI/MEGF12) was identified as a single-gene prognostic biomarker for overall survival in AML, performing equivalently to the LSC17 leukemic stem-cell signature across age strata; PEAR1 surface expression on AML blasts was confirmed by flow cytometry, supporting antibody-based targeting [PMID:35868306](../papers/35868306.md).
- AML cell-maturation state (deconvolved from bulk RNA-Seq into six Van Galen et al. single-cell signatures) was shown to broadly govern ex vivo drug sensitivity and to modify known mutation–drug associations (e.g., Monocyte-like state confers [sorafenib](../drugs/sorafenib.md) resistance in FLT3-ITD AML, overriding the expected ITD-driven sensitivity) [PMID:35868306](../papers/35868306.md).
- Harmonized analysis yielded 65 additional mutation–drug associations not significant in Waves 1+2 alone (a 27% increase), demonstrating the statistical benefit of the expanded cohort [PMID:35868306](../papers/35868306.md).

## Sources

- cBioPortal study: `aml_ohsu_2022`
- Vizome portal: www.vizome.org/aml2
- dbGaP: phs001657.v2.p1 (study ID 30641)
- Code: https://github.com/biodev/beataml2_manuscript

*This page was processed by **crosslinker** on **2026-05-21**.*
