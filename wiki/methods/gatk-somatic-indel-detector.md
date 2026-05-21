---
name: GATK Somatic Indel Detector
slug: gatk-somatic-indel-detector
kind: somatic_variant_calling
canonical_source: corpus
unverified: true
tags: [variant-calling, indel, somatic, GATK]
processed_by: crosslinker
processed_at: 2026-05-21
---

# GATK Somatic Indel Detector

## Overview

GATK Somatic Indel Detector is a variant-calling tool from the Genome Analysis Toolkit (GATK) designed to detect somatic insertion and deletion (indel) events in paired tumor/normal sequencing data. It identifies candidate somatic indels by comparing allele frequencies between tumor and matched normal samples, with configurable thresholds for minimum allele fraction and read support.

## Used by

- [coad_caseccc_2015](../datasets/coad_caseccc_2015.md) — used alongside [mutect](../methods/mutect.md) and [varscan](../methods/varscan.md) for somatic indel calling in 29 AA CRC discovery exomes (paired tumor/normal); contributed to identification of 20 significantly mutated genes in African American MSS colorectal cancer including [EPHA6](../genes/EPHA6.md) and [FLCN](../genes/FLCN.md) as AA-specific drivers [PMID:25583493](../papers/25583493.md)
- GATK Somatic Indel Detector used for indel calling in 10 [PCNSL](../cancer_types/PCNSL.md) WES cases alongside SomaticSniper SNV calls; variants annotated with snpEFF/PolyPhen-2 via the TREAT workflow. [PMID:25991819](../papers/25991819.md)
- GATK Somatic Indel Detector used for indel calling in MSK-IMPACT targeted panel sequencing of pancreatic cancer [PMID:26278805](../papers/26278805.md)
- GATK Somatic Indel Detector used for indel calling in whole-exome and whole-genome sequencing of colorectal cancer [PMID:26343386](../papers/26343386.md)
- Used alongside MuTect for indel calling in 62 uRCC tumours sequenced on the MSK-IMPACT 230-gene panel with BWA-MEM-aligned reads. [PMID:27713405](../papers/27713405.md)
- Used as one of three somatic variant callers in the MSK-IMPACT bioinformatics pipeline (union of MuTect, Pindel, GATK somatic indel detector) for SNV/indel detection [PMID:28481359](../papers/28481359.md)
- GATK SomaticIndelDetector used for indel calling in 15 Korean vulvar SCC paired tumor/normal WES samples (BWA/hg19 pipeline); 21 mutations across 9 genes validated by digital PCR or Sanger sequencing [PMID:29422544](../papers/29422544.md)
- Used alongside MuTect for indel calling in 66 pretreatment BRAF-mutant melanoma tumors across the MSK/Vanderbilt cohort (mean 622× coverage) [PMID:32913971](../papers/32913971.md)
- GATK Somatic Indel Detector applied for indel calling in MSK-IMPACT sequencing of 42 [SCLC](../cancer_types/SCLC.md) PDX/CDX models [PMID:35440124](../papers/35440124.md).

## Notes

- Part of the GATK toolkit; intended for use with BWA-aligned BAM files.
- Typically used in combination with other somatic callers (MuTect for SNVs, VarScan for SNVs/indels) for increased sensitivity.
- Superseded in later GATK versions (GATK4+) by Mutect2, which handles both SNVs and indels.

## Sources

- [PMID:25583493](../papers/25583493.md) — Guda et al. 2015, WES of African American MSS CRC

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:25991819](../papers/25991819.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26278805](../papers/26278805.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26343386](../papers/26343386.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:27713405](../papers/27713405.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28481359](../papers/28481359.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29422544](../papers/29422544.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32913971](../papers/32913971.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35440124](../papers/35440124.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
