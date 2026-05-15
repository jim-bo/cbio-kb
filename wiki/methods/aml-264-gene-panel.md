---
name: AML 264-Gene Panel
slug: aml-264-gene-panel
kind: method
canonical_source: corpus
unverified: true
tags: [targeted-sequencing, aml, gene-panel, exome-capture]
processed_by: crosslinker
processed_at: 2026-05-14
---

# AML 264-Gene Panel

## Overview

The [AML](../cancer_types/AML.md) 264-gene panel is an enhanced whole-exome sequencing approach developed at Washington University in St. Louis that supplements standard NimbleGen v3 exome capture with biotinylated probes targeting 264 recurrently mutated AML genes. This hybrid capture approach increases sensitivity for AML driver genes beyond standard exome depth while retaining genome-wide coverage.

## Used by

- Applied to 39 AML/MDS patients on the WashU [decitabine](../drugs/decitabine.md) trial (157 serial exomes across multiple timepoints) to track clonal mutation dynamics during treatment; enhanced probe coverage of 264 AML genes enabled detection of low-VAF mutations and subclonal architecture at greater sensitivity than standard WES alone. [PMID:27959731](../papers/27959731.md)

## Notes

- Platform: Illumina HiSeq 2000/2500 with NimbleGen v3 exome capture supplemented by custom biotinylated probes for 264 recurrently mutated AML genes.
- Genes covered include [TP53](../genes/TP53.md), [DNMT3A](../genes/DNMT3A.md), [IDH1](../genes/IDH1.md), [IDH2](../genes/IDH2.md), [ASXL1](../genes/ASXL1.md), [SRSF2](../genes/SRSF2.md), [U2AF1](../genes/U2AF1.md), [SF3B1](../genes/SF3B1.md), and 256 additional AML-relevant genes.
- Serial timepoints (median 4 per patient) enabled longitudinal clonal tracking; 157 exomes from 39 patients.
- Complementary to the 8-gene AmpliSeq panel (45 additional patients) for breadth vs depth tradeoff in the same study.
- Data deposited in dbGaP (phs000159).

## Sources

*This page was processed by **crosslinker** on **2026-05-14**.*
