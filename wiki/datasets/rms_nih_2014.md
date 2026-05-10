---
name: NCI/NIH Rhabdomyosarcoma Genomic Cohort (2014)
studyId: rms_nih_2014
institution: National Cancer Institute (NCI) / Children's Oncology Group / Broad Institute
size: 147
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-genome-seq
  - whole-exome-seq
  - rna-seq
  - affymetrix-snp6
panels: []
tags:
  - rhabdomyosarcoma
  - pediatric-cancer
  - sarcoma
  - PAX-FOXO1-fusion
  - RTK-RAS-PI3K-axis
  - clonal-evolution
processed_by: crosslinker
processed_at: 2026-05-09
---

# NCI/NIH Rhabdomyosarcoma Genomic Cohort (2014)

## Overview

The rms_nih_2014 cohort is a comprehensive multi-platform genomic study of 147 rhabdomyosarcoma ([RMS](../cancer_types/RMS.md)) tumor/normal pairs assembled through a collaboration between the Pediatric Oncology Branch (NCI), the Children's Oncology Group (COG), The Tumour Bank at The Children's Hospital at Westmead (NSW, Australia), and Hospital Sant Joan de Deu de Barcelona. The study, led by Shern et al., used whole-genome sequencing, whole-exome sequencing, RNA-seq, and SNP-array profiling to define the molecular landscape of RMS and establish PAX-fusion status (rather than classical ARMS/ERMS histology) as the dominant axis of biological classification. All sequence data were uploaded to dbGaP.

## Composition

- **147 tumor/normal pairs** total; samples from NCI Pediatric Oncology Branch, Children's Oncology Group, Australian and Spanish pediatric oncology banks.
- Cancer types: [RMS](../cancer_types/RMS.md) (rhabdomyosarcoma), classified as alveolar ([ARMS](../cancer_types/ARMS.md)) and embryonal ([ERMS](../cancer_types/ERMS.md)); molecularly re-partitioned into PAX-fusion-positive (PFP, n=50) and PAX-fusion-negative (PFN) subgroups.
- Mean non-synonymous somatic mutations per tumor: PFN 17.8 vs PFP 6.4 (P=2×10⁻⁴).
- PFN tumors showed greater aneuploidy than PFP (P=1×10⁻⁵).

## Assays / panels (linked)

- [whole-genome-seq](../methods/whole-genome-seq.md) — 44 tumors on Complete Genomics platform, mean 105× depth, 97% genome coverage.
- [whole-exome-seq](../methods/whole-exome-seq.md) — 103 additional tumors; SOLiD 4 with Agilent SureSelect 37.8 Mb bait (90 pairs) or Illumina HiSeq with SureSelect v2 (13 pairs); processed with [mutect](../methods/mutect.md) / [mutsig](../methods/mutsig.md).
- [rna-seq](../methods/rna-seq.md) — 80 tumors; polyA RNA-seq on Illumina HiSeq2000 (100 bp PE), fusions called by [tophat-fusion](../methods/tophat-fusion.md) and [defuse](../methods/defuse.md).
- [affymetrix-snp6](../methods/affymetrix-snp6.md) — all tumors profiled with Illumina Omni 2.5M or 5M SNP arrays (SNP6-equivalent workflow).
- Variant annotation via [annovar](../methods/annovar.md) and [oncotator](../methods/oncotator.md); reference build hg19.
- Verification: SOLiD exome on 30/44 WGS samples; custom AmpliSeq Cancer Panel on Ion Torrent PGM (sensitivity 84%, specificity 93%); Sanger sequencing for curated calls.

## Papers using this cohort

- [PMID:24436047](../papers/24436047.md) — Shern et al., *Cancer Discovery* (2014): Comprehensive genomic analysis of rhabdomyosarcoma reveals a landscape of alterations affecting a common genetic axis in fusion-positive and fusion-negative tumors.

## Notable findings derived from this cohort

- RMS partitions cleanly by PAX-fusion status rather than by classical ARMS/ERMS histology; 7 fusion-negative [ARMS](../cancer_types/ARMS.md) tumors clustered with [ERMS](../cancer_types/ERMS.md) by expression and mutation profile. [PMID:24436047](../papers/24436047.md)
- Three histologically fusion-negative ARMS tumors harbored cryptic PAX rearrangements: [PAX3](../genes/PAX3.md)–[NCOA1](../genes/NCOA1.md) (n=2) and a novel [PAX3](../genes/PAX3.md)–[INO80D](../genes/INO80D.md) fusion. [PMID:24436047](../papers/24436047.md)
- Receptor tyrosine kinase / RAS / [PIK3CA](../genes/PIK3CA.md) axis alterations were found in **93% (41/44)** of WGS-surveyed tumors, establishing this axis as the dominant therapeutic target in RMS. [PMID:24436047](../papers/24436047.md)
- Novel recurrent RMS drivers identified: [FBXW7](../genes/FBXW7.md) (7.4% of PFN tumors, exclusively at WD40-domain arginines) and [BCOR](../genes/BCOR.md) (7% of all RMS, predominantly PFN). [PMID:24436047](../papers/24436047.md)
- RAS mutations ([NRAS](../genes/NRAS.md) 11.7%, [KRAS](../genes/KRAS.md) 6.4%, [HRAS](../genes/HRAS.md) 4.3%) occurred exclusively at codons 12/13/61 and only in PFN tumors; no RAS mutations were found in PFP tumors. [PMID:24436047](../papers/24436047.md)
- [PAX7](../genes/PAX7.md)–[FOXO1](../genes/FOXO1.md) fusion gene was amplified in 12/15 PAX7-FOXO1 tumors. [PMID:24436047](../papers/24436047.md)

## Sources

- dbGaP accession: uploaded (specific accession listed in supplementary materials of PMID:24436047)
- cBioPortal study ID: rms_nih_2014

*This page was processed by **crosslinker** on **2026-05-09**.*
