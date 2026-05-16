---
name: Beat AML — OHSU Functional Genomic Landscape (2018)
studyId: aml_ohsu_2018
institution: Oregon Health & Science University (OHSU) and 9 partner sites
size: 562
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - rna-seq
  - ex-vivo-drug-sensitivity-screen
panels: []
tags:
  - AML
  - functional-genomics
  - drug-sensitivity
  - beat-aml
  - ex-vivo
processed_by: crosslinker
processed_at: 2026-05-16
---

# Beat AML — OHSU Functional Genomic Landscape (2018)

## Overview

The Beat [AML](../cancer_types/AML.md) program is a prospective multi-institutional study that assembled one of the largest integrated genomic and pharmacologic AML datasets to date. Tumor specimens from 562 unique AML patients (672 total specimens, including serial samples) were collected across OHSU and 9 partner sites (University of Utah, UT Southwestern, Stanford, University of Miami, University of Colorado, University of Florida, NIH, Fox Chase, and KUMC). The dataset integrates whole-exome sequencing, RNA-sequencing, and a 122-compound ex vivo drug sensitivity screen. All data are publicly accessible via dbGaP (phs001657.v1.p1), GDC, and cBioPortal, and are browsable interactively at www.vizome.org. [PMID:30333627](../papers/30333627.md)

## Composition

- **562 unique AML patients**, 672 primary tumor specimens (bone marrow aspirate or peripheral blood), including 110 patients with multiple time-point samples. [PMID:30333627](../papers/30333627.md)
- **Cancer type:** [AML](../cancer_types/AML.md)
- **Whole-exome sequencing:** 622 specimens / 531 patients; Illumina Nextera RapidCapture (37 Mb); aligned with BWA MEM; somatic variants from MuTect v1.1.7, VarScan 2 v2.4.1, and Pindel (FLT3-ITD calls); annotated with VEP v83 / [vcf2maf](../methods/vcf2maf.md). 11.9-Mb custom validation library applied to 96 specimens (94% SNV / 82% indel validation rate). [PMID:30333627](../papers/30333627.md)
- **RNA-sequencing:** 451 specimens / 411 patients; Agilent SureSelect Strand-Specific kit; Illumina HiSeq 2500. [PMID:30333627](../papers/30333627.md)
- **Ex vivo drug sensitivity:** 409 specimens / 363 patients screened within 24 hours of isolation against 122 small-molecule inhibitors; AUC summarized per drug. [PMID:30333627](../papers/30333627.md)
- **Reference genome:** GRCh37 / b37 (Broad bundle 2.8). [PMID:30333627](../papers/30333627.md)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — 622 specimens / 531 patients
- [rna-seq](../methods/rna-seq.md) — 451 specimens / 411 patients
- [ex-vivo-drug-sensitivity-screen](../methods/ex-vivo-drug-sensitivity-screen.md) — 409 specimens / 363 patients, 122-compound panel

## Papers using this cohort

- [PMID:30333627](../papers/30333627.md) — Tyner et al. 2018, "Functional Genomic Landscape of Acute Myeloid Leukemia," *Nature*

## Notable findings derived from this cohort

- **Mutational landscape:** median 13 somatic variants per patient (range 1–80); top 33 most commonly mutated genes overlapped with TCGA AML, except [SRSF2](../genes/SRSF2.md) which was significantly more frequent in Beat AML. [PMID:30333627](../papers/30333627.md)
- **Novel rare events:** ~1,500 mutant genes unique to Beat AML; 11 genes mutated in ≥1% of Beat AML patients had not been observed in prior AML sequencing studies. [PMID:30333627](../papers/30333627.md)
- **Drug-sensitivity associations:** of 122 compounds, 64 were significantly more sensitive in de novo versus transformed AML (FDR <0.1); single-gene associations identified for [FLT3](../genes/FLT3.md)-ITD, [TP53](../genes/TP53.md), [ASXL1](../genes/ASXL1.md), [NRAS](../genes/NRAS.md)/[KRAS](../genes/KRAS.md), [IDH1](../genes/IDH1.md), [IDH2](../genes/IDH2.md), [RUNX1](../genes/RUNX1.md), [U2AF1](../genes/U2AF1.md), and [ZRSR2](../genes/ZRSR2.md). [PMID:30333627](../papers/30333627.md)
- **Combinatorial biomarkers:** [FLT3](../genes/FLT3.md)-ITD + [NPM1](../genes/NPM1.md) co-mutation (regardless of [DNMT3A](../genes/DNMT3A.md) status) sensitized to [ibrutinib](../drugs/ibrutinib.md) and [entospletinib](../drugs/entospletinib.md) ex vivo; [BCOR](../genes/BCOR.md) + [RUNX1](../genes/RUNX1.md) co-mutation sensitized to JAK inhibitors ([momelotinib](../drugs/momelotinib.md), [ruxolitinib](../drugs/ruxolitinib.md), [tofacitinib](../drugs/tofacitinib.md)). [PMID:30333627](../papers/30333627.md)
- **Expression signatures:** 65.5% of testable drugs (78/119) had FDR<0.05 expression signatures; a 17-gene signature stratified [ibrutinib](../drugs/ibrutinib.md) response. [PMID:30333627](../papers/30333627.md)
- **WGCNA integration:** 14 co-expression gene clusters; a 110-gene "magenta" subnetwork associated with ibrutinib resistance tracked with adverse ELN 2017 risk. [PMID:30333627](../papers/30333627.md)

## Sources

- cBioPortal study ID: `aml_ohsu_2018`
- dbGaP: phs001657.v1.p1 (study ID 30641)
- GDC data release
- Vizome interactive browser: www.vizome.org
- [PMID:30333627](../papers/30333627.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
