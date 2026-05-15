---
name: SNPs-seq
slug: snps-seq
kind: method
canonical_source: corpus
unverified: true
tags:
  - functional-genomics
  - gwas
  - allele-specific
  - transcription-factor-binding
  - prostate-cancer
processed_by: crosslinker
processed_at: 2026-05-15
---

# SNPs-seq

## Overview

SNPs-seq (also referred to as SNP-seq or high-throughput allele-specific protein-binding assay) is a functional genomics screening method that measures allele-specific protein binding across large numbers of SNP loci simultaneously. The method uses a competitive binding approach: paired oligonucleotides carrying the reference and alternate alleles of candidate SNPs are incubated with nuclear extracts, and differential protein binding is quantified by sequencing (giving a "biased allelic binding" or BAB score). This enables systematic prioritization of GWAS risk loci to identify the functional causal variant(s) driving disease association.

## Used by

- Applied to 374 prostate-cancer GWAS risk loci in the NOL10/USF1 prostate cancer study; identified rs4519489 ([NOL10](../genes/NOL10.md) intron, 2p25 locus) as exhibiting strong biased allelic binding with the risk A allele binding more protein than the T allele, leading to its nomination as the functional causal SNP [PMID:28927585](../papers/28927585.md)

## Notes

- Scales to hundreds or thousands of loci in a single experiment, outperforming traditional one-locus-at-a-time EMSA for GWAS functional prioritization.
- BAB scores are agnostic to identity of the binding protein; downstream ChIP-seq, EMSA, and proteomics are needed to identify specific TF binders.
- Corpus-grown slug; not registered as a canonical assay type in cBioPortal.

## Sources

*This page was processed by **crosslinker** on **2026-05-15**.*
