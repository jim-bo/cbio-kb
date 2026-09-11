---
name: NetMHCcons
slug: netmhccons
kind: method
canonical_source: corpus
unverified: true
tags: [neoantigen-prediction, hla-binding, immunogenomics]
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# NetMHCcons

## Overview

A consensus MHC class I peptide-binding prediction method that combines NetMHC, NetMHCpan and PickPocket to score candidate 8-11-mer peptide-HLA binding affinity, used to nominate neoepitopes from expressed somatic mutations.

## Used by

- Predicted 8-11-mer neoepitope binding for expressed somatic mutations (confirmed in RNA-seq) after Polysolver HLA typing on PBMC exomes, in a study of PD-L1 blockade biomarkers [PMID:29867230](../papers/29867230.md).

## Notes

- Consensus method combining NetMHC, NetMHCpan and PickPocket predictions.
- Typically applied only to mutations confirmed as expressed in matched RNA-seq.

## Sources

- [PMID:29867230](../papers/29867230.md)

*This page was processed by **entity-page-writer** on **2026-09-10**.*
