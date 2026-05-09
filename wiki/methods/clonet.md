---
name: CLONET
slug: clonet
kind: method
canonical_source: corpus
unverified: false
tags:
  - clonality
  - tumor-purity
  - copy-number
  - whole-genome-seq
processed_by: crosslinker
processed_at: 2026-05-09
---

# CLONET

## Overview

CLONET (CLOnality and Ploidy Estimation from Tumor) is a computational method for estimating tumor clonality and ploidy from germline SNP allelic fractions in whole-genome sequencing data. By leveraging the allele-frequency distribution of heterozygous germline SNPs, CLONET infers local copy number, tumor purity, and the clonal versus subclonal status of somatic deletions and rearrangements. It was introduced alongside ChainFinder in a 2013 WGS study of prostate cancer to establish the temporal order of genomic events in chromoplexy-driven tumor evolution.

## Used by

- Introduced and applied to 57 prostate WGS genomes to infer clonality of somatic deletions and rearrangements; used to establish the consensus progression path — early NKX3-1/TMPRSS2-ERG, intermediate CDKN1B/TP53 loss, late subclonal [PTEN](../genes/PTEN.md) deletion (p=10⁻⁵ vs [NKX3-1](../genes/NKX3-1.md)); concordance with ABSOLUTE purity was R²=0.99 with two flagged discrepant samples [PMID:23622249](../papers/23622249.md)

## Notes

- Inputs are germline SNP allelic fractions from WGS; does not require SNP array data.
- Designed specifically for use with paired tumor/normal WGS; works in concert with SV callers (dRanger, BreakPointer) and GISTIC for SCNA calling.
- Two samples showed discordant CLONET/ABSOLUTE purity estimates and were flagged in the original publication.

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
