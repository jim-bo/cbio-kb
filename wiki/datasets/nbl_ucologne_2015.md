---
name: Neuroblastoma (University of Cologne, Nature 2015)
studyId: nbl_ucologne_2015
institution: University of Cologne / German Pediatric Oncology and Hematology (GPOH) network
size: 217
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
  - MRNA_EXPRESSION
  - METHYLATION
panels: []
tags:
  - neuroblastoma
  - pediatric-oncology
  - whole-genome-seq
  - structural-variants
  - enhancer-hijacking
  - telomere-maintenance
  - high-risk
processed_by: crosslinker
processed_at: 2026-05-14
---

# Neuroblastoma (University of Cologne, Nature 2015)

## Overview

The nbl_ucologne_2015 dataset is from Peifer et al. (Nature, 2015) and comprises whole-genome sequencing of 56 neuroblastomas (39 high-risk, 17 low-risk) with an extended validation cohort of 217 German patients diagnosed 1991–2014, enrolled through GPOH clinical trials. The study identified recurrent structural rearrangements at chromosome 5p15.33 upstream of [TERT](../genes/TERT.md) as a novel mechanism of telomerase activation in high-risk neuroblastoma. WGS data are deposited in the European Genome-phenome Archive (EGA accession EGAS00001001308). The cohort is mirrored in cBioPortal as study nbl_ucologne_2015.

## Composition

- Discovery cohort: 56 [NBL](../cancer_types/NBL.md) with matched normals (high-risk n=39, low-risk n=17); profiled by whole-genome sequencing (Illumina HiSeq 2000, 2×100 nt paired-end, hg19/BWA), RNA-seq, ChIP-seq, HM450 methylation array, and custom Agilent oligonucleotide microarrays.
- Validation cohort: 161 additional primary neuroblastomas profiled by FISH and hybrid-capture targeted sequencing over the TERT/CLPTM1L region.
- Extended combined cohort: 217 patients (German, single trial network GPOH).
- Mean WGS non-synonymous mutation rate: 13.3 per genome (low-risk 5.9 ± 5.5; high-risk 16.6 ± 9.9).
- Reference genome: hg19.

## Assays / panels (linked)

- [whole-genome-seq](../methods/whole-genome-seq.md)
- [targeted-dna-seq](../methods/targeted-dna-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [chip-seq](../methods/chip-seq.md)
- [fish](../methods/fish.md)
- [hm450-methylation-array](../methods/hm450-methylation-array.md)

## Papers using this cohort

- [PMID:26466568](../papers/26466568.md) — Peifer et al. 2015, Nature — "Telomerase activation by genomic rearrangements in high-risk neuroblastoma."

## Notable findings derived from this cohort

- Recurrent 5p15.33 structural rearrangements upstream of [TERT](../genes/TERT.md) found in 12/39 (31%) high-risk WGS cases and 27/114 (24%) of the extended high-risk cohort; absent in all 17 low-risk WGS cases (P=0.01) [PMID:26466568](../papers/26466568.md).
- [TERT](../genes/TERT.md) rearrangements, [MYCN](../genes/MYCN.md) amplification, and [ATRX](../genes/ATRX.md) mutations were mutually exclusive in high-risk disease (P=0.008), defining three convergent routes to telomere lengthening [PMID:26466568](../papers/26466568.md).
- TERT-rearranged patients had overall survival comparable to MYCN-amplified patients and significantly worse event-free survival than other high-risk patients (EFS P=0.038); [TERT](../genes/TERT.md) rearrangement was an independent prognostic factor in multivariable analysis controlling for stage and [MYCN](../genes/MYCN.md) [PMID:26466568](../papers/26466568.md).
- Mechanism is enhancer hijacking: rearrangements juxtapose TERT to strong super-enhancer clusters (H3K27ac/H3K4me1) without altering TERT copy number; TERT expression was 92-fold higher (median) than in low-risk tumors [PMID:26466568](../papers/26466568.md).
- [MYCN](../genes/MYCN.md) directly activates TERT transcription; TERT was the top downregulated gene upon [MYCN](../genes/MYCN.md) siRNA knockdown in MYCN-amplified IMR5/75 cells [PMID:26466568](../papers/26466568.md).

## Sources

- Peifer M et al. "Telomerase activation by genomic rearrangements in high-risk neuroblastoma." Nature. 2015;526(7575):700-704. [PMID:26466568](../papers/26466568.md). DOI: 10.1038/nature14980.

*This page was processed by **crosslinker** on **2026-05-14**.*
