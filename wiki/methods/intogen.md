---
name: IntOGen
slug: intogen
kind: MUTATION_EXTENDED
canonical_source: corpus
unverified: true
tags: [driver-discovery, positive-selection, cancer-genomics]
processed_by: crosslinker
processed_at: 2026-05-16
---

# IntOGen

## Overview

IntOGen (Integrative OncoGenomics) is a framework for identifying cancer driver genes under positive selection in tumour cohorts. It integrates multiple complementary methods for detecting functional impact, mutational clustering, and excess of non-synonymous vs synonymous mutations, then combines their signals to nominate driver candidates.

## Used by

- Used for driver gene discovery in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS); IntOGen identified 25 recurrently mutated genes under positive selection, including [UBA1](../genes/UBA1.md) as a novel candidate LCINS driver (6/9 mutated cases in the piano subtype) [PMID:34493867](../papers/34493867.md)

## Notes

- Complementary to dNdScv; both were applied in the Sherlock-Lung study, leveraging WGS data at high coverage (mean 85×).
- UBA1 (E1 ubiquitin-activating enzyme, involved in DNA damage response) was highlighted as a piano-subtype-specific candidate driver based on IntOGen output.
- IntOGen is publicly accessible at intogen.org; analysis pipelines combine ONCODRIVEFML, ONCODRIVECLUSTL, SMREGIONS, MutPanning, and other methods.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
