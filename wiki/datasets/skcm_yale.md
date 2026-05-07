---
name: Skin Cutaneous Melanoma (Yale, Nat Genet 2012)
studyId: skcm_yale
institution: Yale University
size: 147
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - MUTATION_EXTENDED
panels: []
tags:
  - melanoma
  - cutaneous
  - yale
  - skcm
processed_by: entity-page-writer
processed_at: "2026-05-06"
---

# Skin Cutaneous Melanoma (Yale, Nat Genet 2012)

## Overview

The Yale melanoma dataset comprises 147 melanoma tumors with matched germline DNA subjected to whole-exome sequencing (Krauthammer et al., Nature Genetics 2012). The study is the discovery cohort for [RAC1](../genes/RAC1.md) P29S as a recurrent activating UV-signature mutation in cutaneous melanoma and for the comprehensive characterization of [PPP6C](../genes/PPP6C.md) as a melanoma driver gene. It also defines three molecular classes of melanoma based on mutation burden and copy-number alterations. The exome was expanded to 364 melanomas for RAC1 P29S validation via Sanger sequencing.

## Composition

- 147 melanoma primary and metastatic tumors with matched germline DNA
- Cancer types: cutaneous melanoma (sun-exposed), acral melanoma, mucosal melanoma, [UM](../cancer_types/UM.md) (uveal)
- Sun-exposed melanomas: median 171 somatic mutations per tumor
- Sun-shielded melanomas: median 9 somatic mutations per tumor
- Validation cohort: 76 Australian melanoma cell lines (independent)
- Extended validation cohort: 364 melanomas (Sanger sequencing for RAC1 P29S)
- Exome capture: Roche/NimbleGen SeqCap EZ; 22.4 Mb covering 15,714 genes
- Sequencing: Illumina GAIIx and HiSeq 2000

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — 147 tumor/normal pairs; Roche/NimbleGen SeqCap EZ
- [sanger-sequencing](../methods/sanger-sequencing.md) — validation of RAC1 P29S in 364-melanoma cohort

## Papers using this cohort

- [PMID:22842228](../papers/22842228.md) — Krauthammer et al. Nat Genet 2012 primary analysis

## Notable findings derived from this cohort

- RAC1 P29S identified in 9.2% (20/217) of sun-exposed melanomas as a recurrent UV-signature activating mutation (third most frequent driver after [BRAF](../genes/BRAF.md) and [NRAS](../genes/NRAS.md)) [PMID:22842228](../papers/22842228.md)
- PPP6C mutated in 12.4% of sun-exposed tumors; all co-occurring with BRAF or NRAS mutations (P=0.007); mutations cluster in catalytic active site suggesting loss-of-function [PMID:22842228](../papers/22842228.md)
- [NF1](../genes/NF1.md) inactivation in 30% of BRAF/NRAS-WT sun-exposed melanomas [PMID:22842228](../papers/22842228.md)
- Three melanoma molecular classes: (1) sun-shielded/copy-gain-high/mutation-low; (2) sun-exposed/BRAF-NRAS-WT/mutation-high; (3) sun-exposed/BRAF-NRAS-mutant with frequent PTEN/CDKN2A losses [PMID:22842228](../papers/22842228.md)
- RAC1 P29S significantly more prevalent in males (12.8%) vs females (2.4%, P=0.01), consistent with greater UV exposure in men [PMID:22842228](../papers/22842228.md)
- [BAP1](../genes/BAP1.md) frameshift identified in 1 uveal melanoma case [PMID:22842228](../papers/22842228.md)

## Sources

- [PMID:22842228](../papers/22842228.md) — Krauthammer et al. Nat Genet 2012

*This page was processed by **entity-page-writer** on **2026-05-06**.*
