---
name: ExomeDepth
slug: exomedepth
kind: method
canonical_source: corpus
unverified: true
tags: [copy-number, mitochondrial-dna, read-depth, whole-exome-seq]
processed_by: crosslinker
processed_at: 2026-09-11
---

# ExomeDepth

## Overview

ExomeDepth is a read-depth-based copy-number estimation tool for exome/targeted sequencing data. In the corpus it has been used to call mitochondrial DNA (mtDNA) copy number from whole-exome sequencing reads.

## Used by

- Used to [estimate](../methods/estimate.md) mitochondrial DNA copy number (corrected for tumor purity/ploidy) in 1,015 whole-exome-sequenced colorectal cancers, validated by D-loop/B2M qPCR [PMID:35487942](../papers/35487942.md).

## Notes

- In this corpus, ExomeDepth was applied specifically to mtDNA copy-number estimation after de novo assembly (SPAdes) of mitochondrial reads, rather than to nuclear exon-level CNV calling.

## Sources

- [PMID:35487942](../papers/35487942.md)

*This page was processed by **crosslinker** on **2026-09-11**.*
