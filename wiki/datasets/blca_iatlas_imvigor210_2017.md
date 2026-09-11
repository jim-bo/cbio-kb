---
name: Metastatic Bladder Urothelial Carcinoma (IMvigor210 Phase II Trial, ESMO Open. 2024) - iAtlas Harmonized
studyId: blca_iatlas_imvigor210_2017
institution: multi-center IMvigor210 trial (Genentech/Roche-sponsored); reprocessed by CRI iAtlas
size: 347
reference_genome: hg38
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
panels: []
tags:
  - urothelial-carcinoma
  - immune-checkpoint-blockade
  - atezolizumab
  - neoantigen-landscape
  - iatlas-harmonized
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# Metastatic Bladder Urothelial Carcinoma (IMvigor210 Phase II Trial, ESMO Open. 2024) - iAtlas Harmonized

## Overview

A CRI iAtlas-harmonized whole-exome sequencing and neoantigen-landscape reprocessing of 347 metastatic urothelial carcinomas (matched normals; hg38) drawn from both cohorts of the IMvigor210 single-arm phase II trial of [atezolizumab](../drugs/atezolizumab.md) monotherapy (NCT02108652 / NCT02951767): cohort 1 (cisplatin-ineligible, treatment-naive metastatic disease, n=119 treated) and cohort 2 (platinum-pretreated, n=310 treated). Neither of the two clinical-trial publications describes the WES/neoantigen generation itself — its genomic readouts in-text come from a FoundationOne targeted panel — so the WES data underlying this cBioPortal study is attributed to the iAtlas reprocessing rather than to either paper directly. [PMID:27939400](../papers/27939400.md) [PMID:39642637](../papers/39642637.md)

## Composition

- Cancer type: [BLCA](../cancer_types/BLCA.md) / metastatic urothelial carcinoma, including [UTUC](../cancer_types/UTUC.md) primaries (renal pelvis/ureter). [PMID:27939400](../papers/27939400.md)
- Cohort 1 (primary analysis, PMID:27939400): 119 treated patients, cisplatin-ineligible, treatment-naive for metastatic disease; median follow-up 17.2 months. [PMID:27939400](../papers/27939400.md)
- Cohort 2 (final analysis, PMID:39642637): 310 treated patients, progressed on/after platinum-based chemotherapy; median survival follow-up 46.2 months. [PMID:39642637](../papers/39642637.md)

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md) and neoantigen-landscape analysis — per cBioPortal study metadata; reprocessing coordinated by CRI iAtlas on hg38 (not described in either clinical-trial paper's own text). [PMID:27939400](../papers/27939400.md) [PMID:39642637](../papers/39642637.md)
- In-paper biomarkers: [FoundationOne](../methods/foundationone.md) targeted panel (somatic mutations, TMB, microsatellite status) and VENTANA SP142 PD-L1 [IHC](../methods/pd-l1-ihc-sp142.md). [PMID:27939400](../papers/27939400.md)

## Papers using this cohort

- [PMID:27939400](../papers/27939400.md) — Rosenberg et al.: cohort 1 primary analysis of atezolizumab in cisplatin-ineligible metastatic urothelial carcinoma.
- [PMID:39642637](../papers/39642637.md) — Rosenberg et al., *ESMO Open* (2024): long-term/final analysis of both IMvigor210 cohorts.

## Notable findings derived from this cohort

## Sources

- cBioPortal study ID: blca_iatlas_imvigor210_2017 (name, institution, size, reference_genome from `schema/ontology/studies.json`); co-listed pmid field cites both PMID:39642637 and PMID:27939400.

*This page was processed by **entity-page-writer** on **2026-09-10**.*
