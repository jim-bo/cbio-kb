---
name: Footprints
slug: footprints
kind: method
canonical_source: corpus
unverified: true
tags: [quality-control, callable-bases, sequencing-coverage, normalization]
processed_by: crosslinker
processed_at: 2026-05-16
---

# Footprints

## Overview

Footprints is a software tool that quantifies the per-sample "callable footprint" — the number of base pairs in a targeted sequencing experiment that have sufficient coverage to call somatic mutations with acceptable sensitivity. It accounts for variation in sequencing depth, capture efficiency, and target-region coverage across samples, producing a sample-specific effective coverage estimate. This callable-basepair count is used to normalize somatic mutation burden comparisons across samples and cohorts with heterogeneous sequencing depth.

## Used by

- Applied in a CSCC ([CSCC](../cancer_types/CSCC.md)) meta-analysis of 88 tumors from 10 heterogeneous WES/WGS studies to quantify each sample's callable footprint; mean callable coverage was 91.2% of target bases (range 52.3%–~100%), and per-sample footprint estimates were used to mitigate batch effects from differing sequencing depths and capture kits across the 10 source studies [PMID:34272401](../papers/34272401.md)

## Notes

- Corpus-grown slug; not listed in `schema/ontology/gene_panels.json` or any cBioPortal canonical list.
- Callable-footprint normalization is especially important in multi-study meta-analyses where samples from different labs and capture protocols cannot be assumed to have equivalent effective coverage.
- The authors of the CSCC meta-analysis document that without footprint correction, lower-coverage samples would artifactually appear to have lower mutation burdens, confounding driver-gene frequency comparisons.

## Sources

- [PMID:34272401](../papers/34272401.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
