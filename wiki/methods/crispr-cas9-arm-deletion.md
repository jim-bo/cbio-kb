---
name: CRISPR-Cas9 Chromosome Arm Deletion
slug: crispr-cas9-arm-deletion
kind: method
canonical_source: corpus
unverified: true
tags: [functional-genomics, crispr, chromosome, aneuploidy]
processed_by: crosslinker
processed_at: 2026-05-15
---

# CRISPR-Cas9 Chromosome Arm Deletion

## Overview

A functional genomics strategy that uses CRISPR-Cas9 to introduce a double-strand break near the centromere of a specific chromosome arm, combined with co-transfection of an artificial-telomere construct bearing homology to the break site and a selection cassette. Puromycin selection and single-cell cloning then isolate cells that have undergone telomere capture, resulting in a stable deletion of the entire chromosome arm distal to the break. This approach enables in vitro modeling of the arm-level somatic copy-number alterations observed in cancer.

## Used by

- Applied to human immortalized lung epithelial AALE cells to delete the chr_3p arm: co-transfection of (i) a CRISPR plasmid generating DSBs centromeric to all 3p genes and (ii) an artificial-telomere/puromycin plasmid with ~1 kb of homology to the centromeric break; recombination confirmed by Sanger sequencing, 3p hemizygosity by qPCR, WGS, and [karyotyping](../methods/karyotyping.md); reproduced the IFN/immune gene up-regulation and cis 3p-gene down-regulation predicted by pan-cancer TCGA analysis [PMID:29622463](../papers/29622463.md)

## Notes

- The method is based on the artificial-telomere strategy described by Uno et al. (2017).
- Engineered clones initially proliferated more slowly (G1 accumulation, p < 0.001) but recovered after ~10 additional doublings, often via spontaneous duplication of the remaining chromosome 3.
- Anchorage-independent growth (soft agar) was not induced by chr_3p deletion alone in AALE cells.
- Generalizability to other arms or cell lines requires separate validation.

## Sources

*This page was processed by **crosslinker** on **2026-05-15**.*
