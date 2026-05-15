---
name: AGFusion
slug: agfusion
kind: method
canonical_source: corpus
unverified: true
tags: [fusion-annotation, protein-domain, gene-fusion]
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# AGFusion

## Overview

AGFusion (Annotate Gene Fusion) is a Python package for annotating and visualizing gene fusions. Given a fusion event (gene A and gene B with breakpoint coordinates), AGFusion predicts the protein domain structure of the resulting chimeric protein by mapping Pfam domain annotations (from UniProt/PFAM) onto the fusion junction. This allows automated determination of whether key functional domains (e.g., kinase domains) are retained or disrupted in the fusion protein.

## Used by

- Used to infer kinase-domain integrity for 2,892 kinase-partner fusions across 9,624 TCGA tumor samples; determined that 1,275 (44.1%) of kinase fusions retain an intact kinase domain, a key criterion for identifying potentially activating fusion events [PMID:29617662](../papers/29617662.md)

## Notes

- Annotations are based on UniProt/PFAM domain databases; results depend on database version.
- Domain-retention status is predictive but not equivalent to functional validation of kinase activity.
- Enables automated classification of 3′-kinase vs. 5′-kinase fusions for mechanistic interpretation.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-15**.*
