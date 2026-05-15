---
name: Somatic Signatures
slug: somatic-signatures
kind: mutational_signature_analysis
canonical_source: corpus
unverified: true
tags: [mutational-signatures, NMF, somatic, base-substitution]
processed_by: wiki-cli
processed_at: 2026-05-15
---

# Somatic Signatures

## Overview

Somatic Signatures refers to the analysis framework for identifying and quantifying mutational signature patterns in cancer genomes, based on the trinucleotide context of somatic base substitutions. The approach decomposes the somatic mutation catalog into a mixture of known COSMIC mutational signatures (e.g., SBS1/aging, SBS2/APOBEC, SBS4/tobacco) or de-novo signatures derived by non-negative matrix factorization (NMF). In the context of the African American CRC study, somatic signatures analysis was used to characterize the predominant C>T transitions at CpG sites characteristic of MSS CRC and to compare the mutational landscape between African American and Caucasian MSS tumors.

## Used by

- [coad_caseccc_2015](../datasets/coad_caseccc_2015.md) — applied to characterize the mutational landscape of 29 AA CRC discovery exomes; documented C>T transitions as the predominant base substitution (consistent with age-related/CRC signature); contributed to comparison of AA vs Caucasian MSS CRC mutational profiles [PMID:25583493](../papers/25583493.md)
- SomaticSignatures R package (NMF) used to decompose mutational signatures in 15 Korean vulvar SCCs; signatures compared to 30 COSMIC reference signatures (cosine similarity) and four TCGA SCC cohorts [PMID:29422544](../papers/29422544.md)

## Notes

- C>T transitions at CpG sites (COSMIC SBS1/aging) are the dominant signature in MSS CRC.
- Somatic signature analysis can distinguish tumor etiologies (e.g., UV signature SBS7 in cSCC, tobacco SBS4 in [LUAD](../cancer_types/LUAD.md)) and inform neoantigen burden estimation.
- The `SomaticSignatures` R package (Gehring et al.) provides NMF-based de-novo decomposition; COSMIC reference signatures are used for known-signature attribution.

## Sources

- [PMID:25583493](../papers/25583493.md) — Guda et al. 2015, WES of African American MSS CRC

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:29422544](../papers/29422544.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
