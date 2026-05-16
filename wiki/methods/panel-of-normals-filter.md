---
name: Panel of Normals Filter
slug: panel-of-normals-filter
kind: method
canonical_source: corpus
unverified: true
tags: [quality-control, artifact-filtering, somatic-calling]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Panel of Normals Filter

## Overview

A Panel of Normals (PoN) filter removes recurrent technical artifacts and germline variants that appear as apparent somatic calls across multiple samples. A set of normal (non-tumor) samples is genotyped at candidate somatic sites; positions that are recurrently called in the normal samples are flagged and removed from the somatic call set. This filter is highly effective at removing systematic sequencing and alignment artifacts.

## Used by

- The Broad Panel of Normals v2 (broad_PoN_v2) was the single largest filter in the TCGA MC3 pipeline, removing ~30% of all called variants; identified as more effective than any individual caller-based filter at eliminating recurrent sequencing artifacts [PMID:29596782](../papers/29596782.md)
- Referenced as a validation-technology confounder: because validation used the same chemistry as discovery, PoN-filtered variants appearing in validation data can produce apparent "erroneous filtering" that is actually correct removal of artifacts [PMID:29596782](../papers/29596782.md)
- Panel-of-normals filter applied alongside ExAC frequency cutoff and germline-somatic log-odds filtering to call somatic events in 304 DLBCLs; developed specifically for 55% tumor-only samples in this cohort [PMID:29713087](../papers/29713087.md)

## Notes

- PoN size and composition affect sensitivity/specificity; larger and more diverse PoNs generally perform better.
- A limitation is that the normal panel cannot account for tumor-type-specific artifacts that are absent from the normals used.
- The Broad PoN v2 was specifically used in TCGA MC3; other versions may differ substantially in content.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29713087](../papers/29713087.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
