---
name: GATK (Genome Analysis Toolkit)
slug: gatk
kind: method
canonical_source: corpus
unverified: true
tags:
  - variant-calling
  - base-quality-recalibration
  - bioinformatics
  - somatic
  - germline
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# GATK (Genome Analysis Toolkit)

## Overview

GATK (Genome Analysis Toolkit) is a software suite developed at the Broad Institute for variant discovery and genotyping in high-throughput sequencing data. Its core capabilities include base quality score recalibration (BQSR), local realignment around indels, HaplotypeCaller for germline SNP/indel calling, and Mutect2 for somatic variant calling. GATK is one of the most widely used pre-processing and variant-calling pipelines in cancer genomics, commonly applied to DNA sequencing data after read alignment with BWA. In clinical genomics pipelines, GATK is often used specifically for base-quality recalibration as a preprocessing step before somatic callers such as MuTect.

## Used by

- Bolton et al. used GATK v3.3-0 for base-quality score recalibration (BQSR) after BWA 0.7.5a alignment and ABRA 0.92 local realignment in the MSK-IMPACT CH calling pipeline for 24,146 cancer patients; SNVs were then called by MuTect + VarDict and indels by Somatic Indel Detector + VarDict [PMID:33106634](../papers/33106634.md)

## Notes

- In [PMID:33106634](../papers/33106634.md), GATK's role was specifically base-quality recalibration, not primary variant calling (SNVs were called by MuTect + VarDict).
- GATK also includes the GATK Somatic Indel Detector (a separate module); see [gatk-somatic-indel-detector](../methods/gatk-somatic-indel-detector.md).
- The GATK best-practices workflow is commonly paired with BWA-MEM for read alignment.
- Current GATK versions (4.x) incorporate Mutect2 directly; earlier versions (3.x) used the separate Somatic Indel Detector module.

## Sources

- [PMID:33106634](../papers/33106634.md) — Bolton et al., clonal hematopoiesis in 24,146 cancer patients; GATK v3.3-0 used for base-quality recalibration in MSK-IMPACT CH calling pipeline.

*This page was processed by **entity-page-writer** on **2026-05-16**.*
