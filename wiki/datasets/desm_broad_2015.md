---
name: Desmoplastic Melanoma (Broad/UCSF 2015)
studyId: desm_broad_2015
institution: University of California San Francisco / Broad Institute / Memorial Sloan Kettering Cancer Center / Melanoma Institute Australia
size: 62
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
panels: []
tags:
  - melanoma
  - desmoplastic-melanoma
  - whole-exome-sequencing
  - whole-genome-sequencing
  - targeted-sequencing
  - high-tmb
  - uv-signature
processed_by: crosslinker
processed_at: 2026-05-14
---

# Desmoplastic Melanoma (Broad/UCSF 2015)

## Overview

Sixty-two desmoplastic melanomas assembled from three institutions: 20 fresh-frozen tumors with matched normal in the discovery cohort (10 from MSKCC, 10 from Melanoma Institute Australia) and 42 FFPE primary desmoplastic melanomas in the validation cohort (UCSF dermatopathology repository). This dataset was generated for the first comprehensive genomic characterization of desmoplastic melanoma and is notable for the highest tumor mutation burden among solid tumor subtypes characterized at the time (median 62 mutations/Mb). Raw aCGH copy number data deposited in GEO under accession GSE55150.

## Composition

- **Cancer types:** [DESM](../cancer_types/DESM.md) (desmoplastic melanoma), an OncoTree subtype of [MEL](../cancer_types/MEL.md); both pure and mixed subtypes included and found to be genetically similar.
- **Sample count:** 62 tumors total (20 discovery fresh-frozen + matched normal; 42 validation FFPE, 4 of which lacked non-lesional normal tissue).
- **Clinical fields:** tumor subtype (pure vs mixed), age, anatomic site (sun-exposed vs sun-shielded), germline [CDKN2A](../genes/CDKN2A.md) status.
- **Sequencing — discovery cohort:** low-coverage whole-genome sequencing (13×) + high-coverage whole-exome sequencing (89×, Agilent SureSelect Exome V4 + UTR), Illumina HiSeq 2500; reference genome hg19.
- **Sequencing — validation cohort:** targeted DNA sequencing of 293 genes at 216× (Nimblegen SeqCap EZ Libraries), Illumina HiSeq 2500.
- **Copy number:** high-resolution array CGH (Agilent 180K/244K/1M feature arrays) on 44 samples; CNVkit on all 62 sequenced samples.
- **Variant calling pipeline:** BWA alignment → GATK INDEL realignment/deduplication/recalibration → MuTect (point mutations) → Unified Genotyper and SomaticIndelDetector (INDELs) → Oncotator annotation. Sanger/deep PCR amplicon resequencing confirmed 329/336 mutations (97.9%).
- **GEO accession:** GSE55150 (aCGH data).

## Assays / panels (linked)

- [whole-genome-seq](../methods/whole-genome-seq.md) — discovery cohort low-coverage WGS (13×).
- [whole-exome-seq](../methods/whole-exome-seq.md) — discovery cohort high-coverage exome (89×).
- [targeted-dna-seq](../methods/targeted-dna-seq.md) — validation cohort 293-gene panel (216×).
- [array-cgh-agilent-1m](../methods/array-cgh-agilent-1m.md) — copy number on 44 samples.
- [sanger-sequencing](../methods/sanger-sequencing.md) — orthogonal validation.

## Papers using this cohort

- [PMID:26343386](../papers/26343386.md) — Shain et al. 2015, "Exome sequencing of desmoplastic melanoma identifies recurrent [NFKBIE](../genes/NFKBIE.md) promoter mutations and diverse activating mutations in the MAPK pathway," *Nature Genetics*.

## Notable findings derived from this cohort

- Desmoplastic melanoma carries an exceptionally high mutation burden (median 62 mutations/Mb) with a dominant UV-radiation C>T signature; canonical melanoma drivers [BRAF](../genes/BRAF.md) V600E and [NRAS](../genes/NRAS.md) Q61K/R are completely absent [PMID:26343386](../papers/26343386.md).
- Novel recurrent [NFKBIE](../genes/NFKBIE.md) promoter hotspot mutations in 14.5% of samples (not found in COSMIC or TCGA across any cancer type); 5/15 mutant tumors showed biallelic selection; [NFKBIE](../genes/NFKBIE.md) mutations suppress NFκB nuclear translocation in melanoma cell lines [PMID:26343386](../papers/26343386.md).
- RTK/RAS/MAPK or PI3K pathway activation achieved through a diverse non-mutually-exclusive set of alterations ([NF1](../genes/NF1.md), [CBL](../genes/CBL.md), [ERBB2](../genes/ERBB2.md), [MAP2K1](../genes/MAP2K1.md), [MAP3K1](../genes/MAP3K1.md), BRAF-non-V600, [EGFR](../genes/EGFR.md), [PTPN11](../genes/PTPN11.md), [MET](../genes/MET.md), [RAC1](../genes/RAC1.md), [SOS2](../genes/SOS2.md), [PIK3CA](../genes/PIK3CA.md)) in 73% of tumors; [TERT](../genes/TERT.md) promoter mutations in 90% [PMID:26343386](../papers/26343386.md).

## Sources

- cBioPortal study: `desm_broad_2015`
- GEO accession: GSE55150 (aCGH copy number data)

*This page was processed by **crosslinker** on **2026-05-14**.*
