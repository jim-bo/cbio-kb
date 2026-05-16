---
name: Uveal Melanoma (TCGA)
oncotree_code: UVM
main_type: Melanoma
parent: UM
tags:
  - melanoma
  - uveal
  - ocular
  - tcga-cohort
  - low-mutation-burden
unverified: true
canonical_source: corpus
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Uveal Melanoma / UVM (TCGA)

## Overview

UVM is the TCGA cohort identifier for uveal melanoma. The corresponding OncoTree code is [UM](UM.md) (Uveal Melanoma). Uveal melanoma is biologically distinct from cutaneous melanoma: it is driven primarily by GNAQ/GNA11 mutations, has very low mutation burden (no UV signature), frequently metastasizes to the liver, and has an extremely poor prognosis upon metastasis. UVM has distinctive arm-level copy-number patterns including chromosome 3 monosomy and 8q amplification.

## Cohorts in the corpus

- TCGA UVM cohort: included as one of 33 cancer types in the MC3 pan-cancer mutation-calling project, the pan-cancer fusion landscape study, and the pan-cancer aneuploidy study; subset of the PanCancer Atlas ([uvm_tcga_pan_can_atlas_2018](../datasets/uvm_tcga_pan_can_atlas_2018.md)).

## Recurrent alterations

- MC3 pan-cancer mutation-calling project identified UVM as showing large sample-to-sample variability in mutations per sample alongside [KICH](../cancer_types/KICH.md), [PAAD](../cancer_types/PAAD.md), and [THYM](../cancer_types/THYM.md) [PMID:29596782](../papers/29596782.md).
- Pan-cancer fusion study (9,624 TCGA samples) found UVM has a median of 0 fusions per sample [PMID:29617662](../papers/29617662.md).
- Pan-cancer aneuploidy study found UVM is an exception to the positive aneuploidy–mutation-rate correlation (driven by its MSI/POLE-free but low-mutation character); UVM clusters in the neural-lineage arm-level group with [GBM](../cancer_types/GBM.md) and [LGG](../cancer_types/LGG.md) (melanoma subgroup); chromosome 3 monosomy and 8q gain are defining SCNA features [PMID:29622463](../papers/29622463.md).
- Included in TCGA PanCancer Atlas; UVM showed highest mutation rates with SKCM (UVB signature) in iCluster C15 [PMID:29625048](../papers/29625048.md)
- GNA11 and GNAQ activating mutations dominate uveal melanoma (UVM); drive calcium-signaling deregulation; GNA11/GNAQ exclusivity highlighted in pan-cancer driver co-occurrence/exclusivity network [PMID:29625049](../papers/29625049.md)
- UVM shows lowest actionable-alteration frequency at 2.5% pan-cancer; cell-cycle pathway rarely altered in UVM; included in pan-cancer pathway analysis of 9,125 TCGA tumors [PMID:29625050](../papers/29625050.md)
- Included in TCGA Pan-Cancer Clinical Data Resource (11,160 patients, 33 cancer types); UVM stage-III/IV vs stage-I/II Cox HR not significantly different by any survival endpoint [PMID:29625055](../papers/29625055.md)

## Subtypes

- **Monosomy 3 / BAP1-mutant:** high metastatic risk.
- **Disomy 3 / BAP1-wild-type:** lower metastatic risk.
- [GNAQ](../genes/GNAQ.md) and [GNA11](../genes/GNA11.md) Q209 hotspot mutations are nearly universal (~90% combined); [EIF1AX](../genes/EIF1AX.md), [SF3B1](../genes/SF3B1.md), and [BAP1](../genes/BAP1.md) mutations further stratify prognosis.

## Therapeutic landscape

*No drug-specific findings for UVM reported in the current corpus; MEK inhibitors and liver-directed therapies are investigational.*

## Sources

- [PMID:29596782](../papers/29596782.md) — MC3 multi-center mutation calling (Ellrott et al., 2018)
- [PMID:29617662](../papers/29617662.md) — Pan-cancer fusion landscape (Gao et al., 2018)
- [PMID:29622463](../papers/29622463.md) — Pan-cancer aneuploidy landscape (Taylor et al., 2018)

*This page was processed by **crosslinker** on **2026-05-15**.*
- [PMID:29625048](../papers/29625048.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29625050](../papers/29625050.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29625055](../papers/29625055.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
