---
name: fastNGSadmix
slug: fastngsadmix
kind: MUTATION_EXTENDED
canonical_source: corpus
unverified: true
tags: [ancestry, population-genetics, wgs]
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# fastNGSadmix

## Overview

fastNGSadmix is a tool for inferring population ancestry proportions from next-generation sequencing data. It estimates admixture proportions using a fast EM algorithm on genotype likelihoods from low- to high-coverage sequencing without requiring hard genotype calls, making it suitable for WGS tumour-normal pair analyses.

## Used by

- Applied in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS) to characterise the genetic ancestry of the cohort from germline WGS data; the cohort was 97.4% European, 1.7% Asian, and 0.9% African ancestry [PMID:34493867](../papers/34493867.md)

## Notes

- The near-complete European ancestry of the Sherlock-Lung cohort is acknowledged as a limitation, as EGFR-mutant LCINS is more prevalent in Asian populations.
- fastNGSadmix uses reference population panels (e.g., 1000 Genomes Project) to assign ancestry components.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-16**.*
