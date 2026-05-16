---
name: LOFsigrank
slug: lofsigrank
kind: method
canonical_source: corpus
unverified: true
tags: [cancer-gene-discovery, loss-of-function, statistical-test]
processed_by: crosslinker
processed_at: 2026-05-16
---

# LOFsigrank

## Overview

LOFsigrank is a statistical method for identifying cancer driver genes enriched for loss-of-function (LOF) mutations — nonsense, frameshift, and splice-site variants — relative to background mutation rates. It ranks genes by the excess of inactivating mutations beyond what is expected given local sequence context and mutation burden, and is typically applied alongside complementary tools ([MutSig](../methods/mutsig.md), [dN/dS](../methods/dndscv.md), [OncodriveFML](../methods/oncodrivefml.md)) to increase sensitivity for tumor suppressor gene discovery.

## Used by

- Applied as one of four cancer-gene discovery tools (alongside [MutSig](../methods/mutsig.md), [dN/dS](../methods/dndscv.md), and [OncodriveFML](../methods/oncodrivefml.md)) in a cutaneous squamous cell carcinoma ([CSCC](../cancer_types/CSCC.md)) meta-analysis of 88 QC-passed tumors from 10 WES/WGS studies; collectively the four tools nominated 12 genes, 7 of which were called by ≥2 tools [PMID:34272401](../papers/34272401.md)

## Notes

- Corpus-grown slug; not listed in `schema/ontology/gene_panels.json` or any cBioPortal canonical list.
- LOFsigrank is specifically sensitive to genes under purifying (LOF) selection; complementary to hotspot-based tools that are more sensitive to dominant gain-of-function oncogenes.
- Results are typically interpreted in the union of multiple discovery tools to minimize false-negative rates in smaller cohorts.

## Sources

- [PMID:34272401](../papers/34272401.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
