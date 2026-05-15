---
name: GATK Co-cleaning
slug: gatk-cocleaning
kind: method
canonical_source: corpus
unverified: true
tags: [alignment, preprocessing, indel-realignment]
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# GATK Co-cleaning

## Overview

GATK co-cleaning (also called co-realignment) is a preprocessing step in which matched tumor and normal BAMs are realigned together at known and candidate indel sites using GATK's IndelRealigner. Processing both files jointly prevents artifactual discordance between tumor and normal caused by independent realignment decisions at ambiguous indel loci. Base quality score recalibration (BQSR) is typically applied after realignment.

## Used by

- Applied to ~1,600 BAMs at the UCSC NCI cluster as part of the TCGA MC3 preprocessing pipeline; ensures consistent indel representation between tumor and matched normal before somatic calling [PMID:29596782](../papers/29596782.md)

## Notes

- Co-cleaning is particularly important for indel callers (Pindel, Indelocator, Strelka) that are sensitive to alignment artifacts at homopolymers and microsatellites.
- The GATK HaplotypeCaller-based workflows have largely superseded IndelRealigner in newer pipelines, but co-cleaning was standard practice at the time of TCGA MC3 production.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-15**.*
