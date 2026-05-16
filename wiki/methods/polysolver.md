---
name: POLYSOLVER
slug: polysolver
kind: method
canonical_source: corpus
unverified: true
tags: [hla-typing, somatic-mutation-calling, immune-escape]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# POLYSOLVER

## Overview

POLYSOLVER (POLYmorphic loci SOLVER) is a computational tool for HLA class I typing and somatic HLA mutation calling from whole-exome sequencing data. It infers patient-specific [HLA-A](../genes/HLA-A.md), [HLA-B](../genes/HLA-B.md), and [HLA-C](../genes/HLA-C.md) alleles from tumor/normal sequence reads, then detects somatic mutations within those polymorphic loci — a task that is challenging because standard mutation callers assume diploid non-repetitive reference regions.

## Used by

- [Giannakis et al. 2016 — CRC neoantigen-survival study](../papers/27149842.md): Applied to 619 CRC tumor/normal WES pairs (Illumina HiSeq 2000, SureSelect v.2; mean 90× coverage) to type HLA class I alleles and call somatic HLA mutations; 66/619 (11%) samples carried HLA mutations (96 total); mutated alleles were enriched for neoantigen-binding residues and for somatic hits in TIL-high tumors (chi-squared p = 1.2e-22), consistent with immune-escape selection [PMID:27149842](../papers/27149842.md).
- Used to detect HLA mutations from exome data in 412 BLCA tumors; HLA mutations detected in 4.6% (19/412), enriched in the high-APOBEC/high-burden MSig1 cluster (p=0.039) [PMID:28988769](../papers/28988769.md)
- Used for HLA typing in the MSK IMPACT neoantigen study to identify patient-specific HLA alleles for neoantigen prediction [PMID:29657128](../papers/29657128.md)

## Notes

- HLA loci are highly polymorphic; standard read mappers frequently misalign reads, making somatic variant calling unreliable without HLA-aware tools.
- Shukla et al. (2015, Nature Biotechnology) developed and validated POLYSOLVER; cited in multiple TCGA pan-cancer studies.
- In Giannakis et al., class II HLA loci were not analyzed — a stated limitation.
- Somatic HLA mutations detected by POLYSOLVER may represent immune-escape events under positive selection from tumor-infiltrating lymphocytes.

## Sources

- Shukla SA et al. (2015) Comprehensive analysis of cancer-associated somatic mutations in class I HLA genes. *Nature Biotechnology* 33:1152–1158.
- [PMID:27149842](../papers/27149842.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:28988769](../papers/28988769.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29657128](../papers/29657128.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
