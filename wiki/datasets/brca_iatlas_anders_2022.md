---
name: Metastatic Triple Negative Breast Cancer (UNC Phase II Trial, J Immunother Cancer 2022) - iAtlas Harmonized
studyId: brca_iatlas_anders_2022
institution: UNC-Chapel Hill (Lineberger Comprehensive Cancer Center) and affiliated NC sites; reprocessed by CRI iAtlas
size: 31
reference_genome: hg38
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - rna-seq
panels: []
tags:
  - triple-negative-breast-cancer
  - immune-checkpoint-blockade
  - pembrolizumab
  - cyclophosphamide
  - iatlas-harmonized
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# Metastatic Triple Negative Breast Cancer (UNC Phase II Trial, J Immunother Cancer 2022) - iAtlas Harmonized

## Overview

A CRI iAtlas-harmonized whole-exome sequencing and neoantigen-landscape reprocessing (hg38) of samples from a multicenter, open-label, single-arm phase II trial (NCT02768701) testing a single low dose of cyclophosphamide before pembrolizumab in 40 patients with pretreated metastatic triple-negative [breast cancer](../cancer_types/BRCA.md). The trial paper's own genomic arm reports WES for 26 of 40 patients using PBMCs as matched normal; cBioPortal's study metadata lists 31 samples for the harmonized dataset itself. [PMID:35121644](../papers/35121644.md)

## Composition

- Cancer type: metastatic triple-negative [BRCA](../cancer_types/BRCA.md) (OncoTree has no TNBC-specific code; filed under `brca`). [PMID:35121644](../papers/35121644.md)
- Trial population: 40 evaluable patients (39 for response); median age 54.5 (range 33–82); 76% White; median 2 prior lines of metastatic therapy. [PMID:35121644](../papers/35121644.md)
- In-paper WES subset: 26 patients with tumor/PBMC-matched-normal whole-exome sequencing. [PMID:35121644](../papers/35121644.md)

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md) — tumor vs PBMC matched-normal, TruSeq DNA PCR-Free/HiSeq 4000, aligned to hg38 with [BWA](../methods/bwa.md); variants via Strelka2, Cadabra and [Mutect2](../methods/mutect.md). [PMID:35121644](../papers/35121644.md)
- [RNA-seq](../methods/rna-seq.md) — TruSeq RNA Access/HiSeq 4000, used for [PAM50](../methods/pam50.md) subtyping, immune deconvolution and TCGA immune-subtype classification. [PMID:35121644](../papers/35121644.md)

## Papers using this cohort

- [PMID:35121644](../papers/35121644.md) — Anders et al., *J Immunother Cancer* (2022): source publication for this trial cohort.

## Notable findings derived from this cohort

## Sources

- cBioPortal study ID: brca_iatlas_anders_2022 (name, institution, size, reference_genome from `schema/ontology/studies.json`).

*This page was processed by **entity-page-writer** on **2026-09-10**.*
