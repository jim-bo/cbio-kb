---
name: ADMIXTURE (Supervised Ancestry Inference)
slug: admixture
kind: method
canonical_source: corpus
unverified: true
tags: [ancestry, population-genetics, genomics, supervised-learning, bioinformatics]
processed_by: crosslinker
processed_at: 2026-05-16
---

# ADMIXTURE (Supervised Ancestry Inference)

## Overview

ADMIXTURE is a software tool for maximum-likelihood estimation of individual ancestries from multi-locus SNP genotype data. In supervised mode (used in oncology cohort studies), reference population labels from a panel such as the 1000 Genomes Project (1KGP) are used to constrain ancestry fraction estimation, yielding per-individual proportions of African (AFR), European (EUR), East Asian (EAS), Native American (NAM), and South Asian (SAS) ancestry. In targeted sequencing contexts, SNPs within the bait footprint of the panel (e.g., MSK-IMPACT468) are used as the input genotype matrix. ADMIXTURE v1.3 is widely used for this purpose.

## Used by

- Genetic ancestry in 2,069 MSK-IMPACT-profiled prostate cancer patients was inferred from 5,072 bi-allelic autosomal SNPs within MSK-IMPACT468 baits using supervised ADMIXTURE v1.3 with 1000 Genomes Project reference populations; ancestry proportions (AFR, EUR, EAS, NAM, SAS) tracked self-reported race; 100% vs 0% AFR ancestry was associated with +13 pp chr8q gain (95% CI 4–23), suggesting a germline or environmental component to this somatic event [PMID:34667026](../papers/34667026.md)

## Notes

- ADMIXTURE SNP input from targeted panels is inherently sparse (thousands of SNPs vs millions in GWAS arrays); accuracy is adequate for continental-level ancestry but not fine-scale substructure.
- SNP selection within bait [footprints](../methods/footprints.md) may introduce ascertainment bias if the panel was designed for populations of European ancestry.
- The finding that self-reported race and inferred ancestry diverged for area-level income associations underscores that ancestry estimates and social race are distinct constructs with different confounders.

## Sources

- [PMID:34667026](../papers/34667026.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
