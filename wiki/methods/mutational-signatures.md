---
name: Mutational Signatures Analysis (COSMIC)
slug: mutational-signatures
kind: method
canonical_source: corpus
unverified: true
tags: [mutational-signatures, cosmic, somatic-mutation, snv, indel]
processed_by: crosslinker
processed_at: 2026-05-09
---

# Mutational Signatures Analysis (COSMIC)

## Overview

Decomposition of somatic mutation patterns (single-base substitution trinucleotide contexts, doublet substitutions, small indels) into a mixture of known COSMIC mutational signatures. Each COSMIC signature represents a characteristic mutation pattern attributed to a specific biological process (e.g., SBS1 = clock-like CpG deamination, SBS2/13 = APOBEC activity, SBS3 = HRD/BRCA deficiency, SBS4 = tobacco exposure, dMMR signatures). Decomposition is typically performed using non-negative matrix factorization (NMF) or maximum-likelihood fitting of a catalogue of 96 trinucleotide contexts against the COSMIC v2/v3 signature reference.

## Used by

- Applied to WGS data of 28 metastatic neuroendocrine neoplasms ([pog570_bcgsc_2020](../datasets/pog570_bcgsc_2020.md)) using COSMIC v3; identified AID/APOBEC and dMMR/replication-slippage contributions in multiple cases; PN12 showed kataegis; PN2 (germline biallelic [NTHL1](../genes/NTHL1.md) loss) carried a strong dMMR signature; PN19 (11 months prior platinum) exhibited platinum-therapy signatures [PMID:24326773](../papers/24326773.md).

## Notes

- COSMIC v3 (signatures SBS1–SBS60+) supersedes v2 (30 signatures); results are version-dependent and not always interchangeable.
- Accurate decomposition requires sufficiently large mutation catalogues; small samples or low-TMB tumors may yield unstable fits.
- dMMR ≠ MSI-High in all non-colorectal contexts (illustrated by PMID:24326773 PN4 — biallelic MSH6/MLH1 loss, predicted MSI-low by MSIsensor despite dMMR signatures).
- Tool variants: SigProfilerExtractor, MutationalPatterns, deconstructSigs, SigMA (for HRD).

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
