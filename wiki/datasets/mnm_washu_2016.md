---
name: AML/MDS Decitabine Trial — Washington University (2016)
studyId: mnm_washu_2016
institution: Washington University in St. Louis
size: 116
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - amplicon-sequencing
  - hm450-methylation-array
panels:
  - aml-264-gene-panel
  - aml-8-gene-ampliseq-panel
tags:
  - aml
  - mds
  - decitabine
  - tp53
  - clonal-hematopoiesis
  - hypomethylating-agent
  - clinical-trial
processed_by: crosslinker
processed_at: 2026-05-14
---

# AML/MDS Decitabine Trial — Washington University (2016)

## Overview

A single-arm prospective clinical trial of 10-day [decitabine](../drugs/decitabine.md) cycles in adults with [AML](../cancer_types/AML.md) or [MDS](../cancer_types/MDS.md) at Washington University in St. Louis (NCT01687400, March 2013 – November 2015), with an extension cohort of 32 patients from the University of Chicago and WashU on 5-day schedules (combined N=116). The study paired serial enhanced exome and amplicon-panel sequencing with clinical response assessment to identify predictors of hypomethylating-agent response and to map clonal dynamics under therapy. Exome data are deposited in dbGaP (phs000159); methylation arrays in GEO (GSE80762). The [TCGA AML cohort (laml_tcga_pub)](../datasets/laml_tcga_pub.md) was used as a comparator to benchmark [TP53](../genes/TP53.md) mutation spectrum and methylation patterns. [PMID:27959731](../papers/27959731.md)

## Composition

- **Discovery cohort:** 84 adults on the WashU 10-day decitabine protocol (AML ≥60 yr, relapsed AML, or transfusion-dependent MDS; ECOG PS ≤2). [PMID:27959731](../papers/27959731.md)
- **Extension cohort:** 32 additional patients — 24 with relapsed AML (10-day decitabine, University of Chicago, 2005–2010) and 8 on a 5-day schedule at WashU (5 single-agent, 3 combined with [panobinostat](../drugs/panobinostat.md)). [PMID:27959731](../papers/27959731.md)
- **Combined cohort:** 116 patients; 99 had any sequencing performed. Cancer types: [AML](../cancer_types/AML.md) and [MDS](../cancer_types/MDS.md). [PMID:27959731](../papers/27959731.md)
- Drug: [decitabine](../drugs/decitabine.md) 20 mg/m²/day on days 1–10 of 28-day cycles (discovery cohort). [PMID:27959731](../papers/27959731.md)

## Assays / panels (linked)

- Enhanced [whole-exome sequencing](../methods/whole-exome-seq.md) (Illumina HiSeq 2000/2500, NimbleGen v3 capture) supplemented with 264-gene biotinylated-probe panel ([aml-264-gene-panel](../methods/aml-264-gene-panel.md)) — 39 patients, 157 exomes across serial timepoints. [PMID:27959731](../papers/27959731.md)
- Ion AmpliSeq 8-gene [amplicon sequencing](../methods/amplicon-sequencing.md) panel ([aml-8-gene-ampliseq-panel](../methods/aml-8-gene-ampliseq-panel.md)) covering [TP53](../genes/TP53.md), [DNMT3A](../genes/DNMT3A.md), [IDH1](../genes/IDH1.md), [IDH2](../genes/IDH2.md), [ASXL1](../genes/ASXL1.md), [SRSF2](../genes/SRSF2.md), [U2AF1](../genes/U2AF1.md), [SF3B1](../genes/SF3B1.md) — 45 additional patients. [PMID:27959731](../papers/27959731.md)
- Illumina [HumanMethylation450 BeadChip](../methods/hm450-methylation-array.md) on day 0 and day 10 of cycle 1. [PMID:27959731](../papers/27959731.md)

## Papers using this cohort

- [PMID:27959731](../papers/27959731.md) — Welch et al., *N Engl J Med* 2016: 10-day decitabine in AML/MDS; TP53 mutations predict blast clearance (100% vs 41%, P<0.001) but not survival benefit relative to TP53 wild-type.

## Notable findings derived from this cohort

- **[TP53](../genes/TP53.md) mutations predict decitabine response:** 21/21 (100%) TP53-mutant patients achieved bone-marrow blast clearance (<5% blasts) vs 32/78 (41%) wild-type-TP53 patients (P<0.001); effect replicated in discovery and extension cohorts independently. [PMID:27959731](../papers/27959731.md)
- **Unfavorable cytogenetics also predicted response:** blast clearance in 29/43 (67%) with unfavorable-risk karyotypes vs 24/71 (34%) with intermediate/favorable risk (P<0.001); 20/21 TP53-mutant patients had unfavorable-risk karyotypes. [PMID:27959731](../papers/27959731.md)
- **Response does not translate to survival advantage:** median overall survival 12.7 months (TP53-mutant) vs 15.4 months (TP53 wild-type), P=0.79; notably better than the 4–6 month survival with cytotoxic induction in TP53-mutant AML. [PMID:27959731](../papers/27959731.md)
- **Mutation clearance is universal but incomplete:** only [TP53](../genes/TP53.md) and [SF3B1](../genes/SF3B1.md) mutations consistently dropped to VAF <5%; founding-clone VAF at maximum clearance ranged from 0.06% to 18.43% in the 20 best responders; bone-marrow blast clearance preceded mutation reduction in 15/54 patients. [PMID:27959731](../papers/27959731.md)
- **Clonal hematopoiesis in remission:** 7/22 responders developed nonleukemic rising clones; 2 carried mutations in [DNMT3A](../genes/DNMT3A.md) or [PPM1D](../genes/PPM1D.md). [PMID:27959731](../papers/27959731.md)
- **All evaluable relapses (9/9) arose from preexisting subclones** detectable before therapy, confirming selection rather than de novo mutation as the resistance mechanism. [PMID:27959731](../papers/27959731.md)
- **TP53 mutation spectrum** (missense-dominant, hotspot distribution) was indistinguishable from the [TCGA AML cohort (laml_tcga_pub)](../datasets/laml_tcga_pub.md); no TP53-driven methylation signature identifiable in either dataset. [PMID:27959731](../papers/27959731.md)
- **Allogeneic SCT had the largest survival benefit** by Cox stepwise regression (P<0.001), regardless of TP53 status. [PMID:27959731](../papers/27959731.md)

## Sources

- ClinicalTrials.gov: NCT01687400
- dbGaP: phs000159 (exome data)
- GEO: GSE80762 (methylation arrays)
- cBioPortal study ID: mnm_washu_2016
- Welch et al., *N Engl J Med* 2016 — DOI: 10.1056/NEJMoa1609227

*This page was processed by **crosslinker** on **2026-05-14**.*
