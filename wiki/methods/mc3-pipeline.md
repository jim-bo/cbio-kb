---
name: MC3 Pipeline
slug: mc3-pipeline
kind: method
canonical_source: corpus
unverified: true
tags: [somatic-calling, pipeline, pan-cancer, tcga]
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# MC3 Pipeline

## Overview

The Multi-Center Mutation Calling in Multiple Cancers (MC3) pipeline is a coordinated ensemble somatic variant-calling workflow developed for the TCGA PanCancer Atlas. It applies seven somatic callers (MuTect, VarScan2, Pindel, Indelocator, RADIA, MuSE, SomaticSniper) and eight filters to ~10,510 tumor/normal pairs across 33 cancer types. The pipeline produced two MAF files: a controlled-access file (22,485,627 variants) and an open-access PASS-filtered file (3,600,963 variants from 10,295 tumors), which became the canonical mutation substrate for all PanCancer Atlas analyses.

## Used by

- Describes the full ensemble somatic mutation-calling pipeline applied to the TCGA cohort; ~400 TB of raw BAMs processed over ~1.8M core-hours on DNAnexus; outputs serve as the somatic-variant backbone of cBioPortal PanCancer Atlas studies [PMID:29596782](../papers/29596782.md)
- MC3 Public MAF used as the source of mutation calls for pan-cancer fusion integration across 9,624 TCGA samples in 33 cancer types [PMID:29617662](../papers/29617662.md)
- MC3 pipeline mutation calls used for 9,756 of 10,522 samples in the pan-cancer aneuploidy analysis [PMID:29622463](../papers/29622463.md)

## Notes

- Distributed as CWL + Docker at https://github.com/OpenGenomics/mc3.
- Three compute environments used: DNAnexus (MuSE/RADIA/VarScan/Pindel/SomaticSniper), Broad Firehose (MuTect/Indelocator/ContEst/OxoG), and ISB Cancer Genomics Cloud / Broad FireCloud (OxoG and validation).
- Default parameters are insufficient for all callers; optimal performance required non-default settings and consultation with tool authors.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-15**.*
