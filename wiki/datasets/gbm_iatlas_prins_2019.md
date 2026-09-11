---
name: Glioblastoma (Randomized Clinical Trial, Nat Med. 2019) - iAtlas Harmonized
studyId: gbm_iatlas_prins_2019
institution: multi-institution trial (Dana-Farber, Huntsman, MD Anderson, MGH, MSKCC, UCLA, UCSF); reprocessed by CRI iAtlas
size: 30
reference_genome: hg38
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
panels: []
tags:
  - glioblastoma
  - immune-checkpoint-blockade
  - pembrolizumab
  - neoadjuvant
  - iatlas-harmonized
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# Glioblastoma (Randomized Clinical Trial, Nat Med. 2019) - iAtlas Harmonized

## Overview

A CRI iAtlas-harmonized whole-exome sequencing and neoantigen-landscape reprocessing (hg38) of 30 recurrent glioblastomas with matched normals, drawn from a randomized, multi-institution phase trial (35 patients randomized) comparing neoadjuvant vs adjuvant-only [pembrolizumab](../drugs/pembrolizumab.md) at first or second relapse. The trial paper's own text does not describe the WES/neoantigen analysis; its tumor profiling focuses on NanoString immune-panel and RNA-seq transcriptomics. [PMID:30742122](../papers/30742122.md)

## Composition

- Cancer type: [ADIFG](../cancer_types/ADIFG.md) (glioblastoma), recurrent disease. [PMID:30742122](../papers/30742122.md)
- ITT trial population: 35 patients randomized at 7 institutions (Dana-Farber, Huntsman, MD Anderson, MGH, MSKCC, UCLA, UCSF); 16 neoadjuvant + 19 adjuvant-only. [PMID:30742122](../papers/30742122.md)
- IDH status: predominantly wild-type (75%/81% across arms). [PMID:30742122](../papers/30742122.md)

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md) and neoantigen-landscape analysis — per cBioPortal study metadata; reprocessing coordinated by CRI iAtlas on hg38 (not described in the trial paper's own text). [PMID:30742122](../papers/30742122.md)
- In-paper biomarkers: 770-gene [NanoString nCounter PanCancer Immune Profiling panel](../methods/nanostring-pancancer-immune-profiling.md) (n=28 tumors) and [RNA-seq](../methods/rna-seq.md) aligned to GRCh38. [PMID:30742122](../papers/30742122.md)

## Papers using this cohort

- [PMID:30742122](../papers/30742122.md) — Cloughesy et al., *Nature Medicine* (2019): source publication for this trial cohort.

## Notable findings derived from this cohort

## Sources

- cBioPortal study ID: gbm_iatlas_prins_2019 (name, institution, size, reference_genome from `schema/ontology/studies.json`).

*This page was processed by **entity-page-writer** on **2026-09-10**.*
