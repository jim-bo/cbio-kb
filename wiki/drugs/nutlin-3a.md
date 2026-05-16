---
name: nutlin-3a
targets:
  - MDM2
drug_class: MDM2 antagonist (p53-MDM2 interaction inhibitor)
canonical_source: corpus
unverified: true
tags:
  - targeted-therapy
  - mdm2-inhibitor
  - p53-pathway
processed_by: wiki-cli
processed_at: 2026-05-16
---

# nutlin-3a

## Overview

Nutlin-3a is a small-molecule cis-imidazoline compound that blocks the [MDM2](../genes/MDM2.md)–p53 protein-protein interaction, preventing MDM2-mediated ubiquitination and proteasomal degradation of p53. By stabilizing wild-type p53 protein, it activates p53 transcriptional programs (cell-cycle arrest, apoptosis) in tumors that retain WT [TP53](../genes/TP53.md). Approval status: investigational/preclinical tool compound; clinical-stage successors (e.g., AMG 232, idasanutlin) have entered trials.

## Evidence in the corpus

- [MDM2](../genes/MDM2.md) is focally amplified on chromosome 12q in ~90% of [DDLS](../cancer_types/DDLS.md) (dedifferentiated liposarcoma). An shRNA screen of 385 12q-resident genes in [DDLS](../cancer_types/DDLS.md) cell lines identified [MDM2](../genes/MDM2.md) as an anti-proliferative dependency (sustained knockdown >1 week required). [YEATS4](../genes/YEATS4.md) (GAS41) is co-amplified with MDM2 on 12q and proposed to cooperatively repress the p53 network; nutlin-3a is explicitly cited as a rationale compound for clinical evaluation targeting the MDM2–p53 axis in DDLS [PMID:20601955](../papers/20601955.md).
- Included in the CCLE pharmacogenomic screen across 947 cancer cell lines; sensitivity correlated with genomic features via elastic-net regression [PMID:22460905](../papers/22460905.md)
- In the CCLE (ccle_broad_2019), nutlin-3a (MDM2 inhibitor) sensitivity in TP53 wild-type cancer cell lines was most strongly correlated with MDM4 exon-6 inclusion (MDM4-FL isoform), outperforming total MDM4 mRNA; MDM4-FL was in turn predicted by RPL22L1 expression (driven by RPL22 loss in 68% of MSI lines), proposing a RPL22 → RPL22L1 → MDM4-FL → nutlin-3a sensitivity axis as a clinical patient-selection biomarker. [PMID:31068700](../papers/31068700.md)

## Resistance mechanisms

- Efficacy is contingent on wild-type TP53 status; tumors with TP53 mutation (17% of [PLLS](../cancer_types/PLLS.md) in this cohort) are expected to be insensitive [PMID:20601955](../papers/20601955.md).

## Cancer types (linked)

- [DDLS](../cancer_types/DDLS.md)

## Sources

- [PMID:20601955](../papers/20601955.md) — Barretina et al. 2010, Nature Genetics; MDM2 + [YEATS4](../genes/YEATS4.md) co-amplification on 12q in DDLS; nutlin-3a proposed as MDM2-antagonist therapeutic rationale.

*This page was processed by **crosslinker** on **2026-05-04**.*
- [PMID:22460905](../papers/22460905.md)

*This page was processed by **wiki-cli** on **2026-05-06**.*
- [PMID:31068700](../papers/31068700.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
