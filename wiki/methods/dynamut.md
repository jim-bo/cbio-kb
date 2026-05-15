---
name: DynaMut
slug: dynamut
kind: method
canonical_source: corpus
unverified: true
tags: [variant-scoring, protein-stability, structural-bioinformatics]
processed_by: crosslinker
processed_at: 2026-05-14
---

# DynaMut

## Overview

DynaMut is a web server and computational tool for predicting the effect of amino acid substitutions on protein stability using normal mode analysis (NMA) and graph-based signatures derived from atomic interactions. It takes a PDB structure file and the variant of interest, then computes the change in free energy (ΔΔG) upon mutation. Positive ΔΔG values indicate predicted protein stabilization; negative values indicate destabilization. DynaMut2 is an updated version with improved accuracy.

## Used by

- Applied to predict the structural effect of [UBE2A](../genes/UBE2A.md) p.(Arg6Trp) in endometrial polyps using PDB structure 6CYO; computed ΔΔG = +1.650 kcal/mol, predicting a stabilizing effect consistent with a potential gain-of-function mechanism [PMID:28445112](../papers/28445112.md)

## Notes

- Requires a 3D protein structure (PDB entry or homology model) as input.
- Positive ΔΔG = stabilizing; negative ΔΔG = destabilizing (note: sign convention differs from some other tools — always check the tool's definition).
- Used in concert with sequence-based scores (CADD, REVEL, AlphaMissense) for comprehensive variant interpretation.

## Sources

- [PMID:28445112](../papers/28445112.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
