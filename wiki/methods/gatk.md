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
processed_by: crosslinker
processed_at: 2026-05-21
---

# GATK (Genome Analysis Toolkit)

## Overview

GATK (Genome Analysis Toolkit) is a software suite developed at the Broad Institute for variant discovery and genotyping in high-throughput sequencing data. Its core capabilities include base quality score recalibration (BQSR), local realignment around indels, HaplotypeCaller for germline SNP/indel calling, and Mutect2 for somatic variant calling. GATK is one of the most widely used pre-processing and variant-calling pipelines in cancer genomics, commonly applied to DNA sequencing data after read alignment with BWA. In clinical genomics pipelines, GATK is often used specifically for base-quality recalibration as a preprocessing step before somatic callers such as MuTect.

## Used by

- Bolton et al. used GATK v3.3-0 for base-quality score recalibration (BQSR) after BWA 0.7.5a alignment and ABRA 0.92 local realignment in the MSK-IMPACT CH calling pipeline for 24,146 cancer patients; SNVs were then called by MuTect + VarDict and indels by Somatic Indel Detector + VarDict [PMID:33106634](../papers/33106634.md)
- GATK v4.1.2.0 (with Picard v4.1.2.0) used for duplicate marking and base-quality score recalibration in the reprocessing pipeline for 88 [CSCC](../cancer_types/CSCC.md) tumors aligned to hg19 [PMID:34272401](../papers/34272401.md)
- Used in the MSK-ACCESS sequencing pipeline (alongside ABRA2) for local realignment and base quality score recalibration of cfDNA reads from 681 clinical plasma samples [PMID:34145282](../papers/34145282.md)
- Used in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS) for somatic variant calling and genomic analysis of the [lung_nci_2022](../datasets/lung_nci_2022.md) cohort [PMID:34493867](../papers/34493867.md)
- Used in [prostate_pcbm_swiss_2019](../datasets/prostate_pcbm_swiss_2019.md) for somatic variant calling pipeline in 168 prostate cancer brain metastasis WES samples; part of the standard somatic SNV/indel calling workflow [PMID:35504881](../papers/35504881.md)
- GATK (MuTect2) used for somatic variant calling in the GLASS longitudinal diffuse glioma cohort with b37-aligned whole-exome and whole-genome sequencing data [PMID:35649412](../papers/35649412.md)
- GATK 4.1.2.0 HaplotypeCaller used for germline variant calling and Mutect2 for somatic short-variant calling in WGS of 25 metastatic [CSCC](../cancer_types/CSCC.md) lymph node specimens aligned to GRCh38 [PMID:35982973](../papers/35982973.md)

## Notes

- In [PMID:33106634](../papers/33106634.md), GATK's role was specifically base-quality recalibration, not primary variant calling (SNVs were called by MuTect + VarDict).
- GATK also includes the GATK Somatic Indel Detector (a separate module); see [gatk-somatic-indel-detector](../methods/gatk-somatic-indel-detector.md).
- The GATK best-practices workflow is commonly paired with BWA-MEM for read alignment.
- Current GATK versions (4.x) incorporate Mutect2 directly; earlier versions (3.x) used the separate Somatic Indel Detector module.

## Sources

- [PMID:33106634](../papers/33106634.md) — Bolton et al., clonal hematopoiesis in 24,146 cancer patients; GATK v3.3-0 used for base-quality recalibration in MSK-IMPACT CH calling pipeline.

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34272401](../papers/34272401.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34145282](../papers/34145282.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34493867](../papers/34493867.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35504881](../papers/35504881.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35649412](../papers/35649412.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35982973](../papers/35982973.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
