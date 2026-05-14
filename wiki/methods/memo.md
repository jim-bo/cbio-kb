---
name: MEMo (Mutual Exclusivity Modules in Cancer)
slug: memo
kind: BIOINFORMATICS
canonical_source: corpus
unverified: true
tags: [mutual-exclusivity, pathway-analysis, bioinformatics, statistical-method]
processed_by: crosslinker
processed_at: 2026-05-14
---

# MEMo (Mutual Exclusivity Modules in Cancer)

## Overview

MEMo (Mutual Exclusivity Modules in Cancer) is a computational method for identifying mutually exclusive patterns of genomic alterations across cancer samples. The algorithm searches for sets of genes that are altered in largely non-overlapping subsets of tumors, which is interpreted as evidence that the genes function in the same biological pathway (since co-mutation of pathway members provides no selective advantage). MEMo integrates mutation, copy-number, and epigenetic alteration data to identify pathway-level mutual exclusivity.

## Used by

- Applied in the TCGA [GBM](../cancer_types/GBM.md) 2013 study to test mutual exclusivity across 291 [GBM](../cancer_types/GBM.md) exomes; identified significant mutual exclusivity among chromatin modification gene (CMG) mutations (p=0.0008 across 135/291 samples with ≥1 CMG mutation), PI3K mutations vs. [PTEN](../genes/PTEN.md) alterations (p=0.0047), and [TP53](../genes/TP53.md) mutation vs. MDM amplification (p=0.0003) [PMID:24120142](../papers/24120142.md)
- Applied in TCGA PTC study to confirm mutual exclusivity of MAPK-pathway drivers ([BRAF](../genes/BRAF.md) + [NRAS](../genes/NRAS.md) + [HRAS](../genes/HRAS.md) + [KRAS](../genes/KRAS.md) in 300/402 tumors; MEMo-corrected P<0.01) and to test mutual exclusivity among DNA-repair-related mutations [PMID:25417114](../papers/25417114.md)
- Applied in the TCGA breast cancer ILC/IDC study to identify mutually exclusive oncogenic network alterations (MEMo analysis); identified AKT/mTOR pathway convergence in 45% of [ILC](../cancer_types/ILC.md) samples via upstream RTK, [PTEN](../genes/PTEN.md), and [PIK3CA](../genes/PIK3CA.md) alterations, with ~40% carrying upstream pathway events [PMID:26451490](../papers/26451490.md)

## Notes

- MEMo was developed at Memorial Sloan Kettering and Weill Cornell Medicine; published alongside cBioPortal.
- The mutual exclusivity test accounts for alteration frequency and sample size to compute statistical significance.
- Identification of mutual exclusivity supports pathway-level models of oncogenesis and helps delineate functional redundancy between genomic lesions.

## Sources

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25417114](../papers/25417114.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26451490](../papers/26451490.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
