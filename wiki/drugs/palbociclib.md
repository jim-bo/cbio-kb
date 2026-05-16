---
name: palbociclib
targets:
  - CDK4
  - CDK6
drug_class: CDK4/6 inhibitor
canonical_source: corpus
unverified: true
tags:
  - targeted-therapy
  - cdk-inhibitor
processed_by: wiki-cli
processed_at: 2026-05-16
---

# palbociclib

## Overview

Palbociclib is an oral CDK4/6 inhibitor that blocks G1-to-S-phase cell-cycle progression. It is FDA-approved for hormone-receptor-positive, HER2-negative breast cancer. In sarcoma, CDK4/6 pathway activation (notably [CDK4](../genes/CDK4.md) amplification in liposarcoma) has motivated its inclusion in functional drug screens.

## Evidence in the corpus

- Palbociclib was included in the UCLA PDTO sarcoma drug-screening panel (>400 compounds); [CDK4](../genes/CDK4.md) amplification — prevalent in liposarcoma ([WDLS](../cancer_types/WDLS.md)/[DDCHS](../cancer_types/DDCHS.md)) — was cited as the genomic rationale for testing CDK4/6 inhibitors across sarcoma PDTOs (e.g., SARC0086_3 [PEComa](../cancer_types/PECOMA.md)). Response rates were not reported at the subtype level in the published data. [PMID:39305899](../papers/39305899.md)
- Pharmacologic CDK4/CDK6 inhibition with PD0332991 (palbociclib) induced G1 arrest in [DDLS](../cancer_types/DDLS.md) cell lines LPS141 and DDLS8817 following an shRNA screen of 385 genes on chromosome 12q that identified [CDK4](../genes/CDK4.md) as the top amplified dependency; [CDK4](../genes/CDK4.md) was the most overexpressed of 27 amplified anti-proliferative hits relative to normal fat. This constitutes one of the earliest functional genomic rationales for CDK4/6 inhibition in dedifferentiated liposarcoma [PMID:20601955](../papers/20601955.md).
- CDK4/6 inhibitor palbociclib under evaluation in RB1-intact [HCC](../cancer_types/HCC.md) as a rationale-driven trial target; [RB1](../genes/RB1.md) LOF occurs in 4% and homozygous deletion in 5% of HCCs [PMID:24798001](../papers/24798001.md)
- [CDKN2A](../genes/CDKN2A.md) loss (>36%), [CDK4](../genes/CDK4.md) amplification, and [CCND1](../genes/CCND1.md) amplification in pancreatic ductal adenocarcinoma (109 resected cases, WES) make PDA a high-prior candidate for CDK4/6 inhibition with palbociclib (PD-0332991); synergy with pathway-selective agents shown in PDA models [PMID:25855536](../papers/25855536.md)
- RB1 loss-of-function mutations occur in 5% of HR+/HER2- metastatic breast cancer (mBC) and may confer primary resistance to palbociclib, since RB1 protein is required for CDK4/6 inhibitor bioactivity; authors recommend RB1 testing on metastatic samples before initiating CDK4/6 inhibitors [PMID:28027327](../papers/28027327.md)
- p53/Rb-pathway-altered MIBC (CDKN2A loss with retained Rb) is being targeted with palbociclib (PD-0332991) in NCT02334527, motivated by the pervasive p53/cell-cycle pathway inactivation (89% of tumors) found in the TCGA MIBC cohort [PMID:28988769](../papers/28988769.md)
- CDK4/6 inhibitor used in 49/58 (84.5%) patients in the Wander et al. HR+/HER2- metastatic breast cancer cohort; eight resistance mechanisms were identified in 65.9% of resistant tumors, including RB1 loss, AKT1 activation, RAS mutations, AURKA amplification, CCNE2 amplification, ERBB2 alterations, FGFR2 alterations, and ER loss; in vitro overexpression/CRISPR validated palbociclib and abemaciclib resistance [PMID:32404308](../papers/32404308.md).
- In the CPTAC breast cancer proteogenomics cohort (n=122), Rb protein and median Rb phosphosite positively correlated with proliferation in HR+/ERBB2− tumors but negatively in TNBC (ρ = −0.54, p = 0.003 protein; ρ = −0.46, p = 0.015 phospho); GDSC cell-line data showed Rb protein level predicts palbociclib response in RB1-wild-type lines (ρ = −0.61, p = 0.022), arguing that protein-level Rb assessment adds predictive value beyond RB1 genotype alone. [PMID:33212010](../papers/33212010.md)
- In LUSC, universal CDK4/6-pathway dysregulation means every tumor loses CDKN2A or RB1 function; heterogeneous Rb protein and phospho-Rb in CCND1-amplified tumors may explain variable responses to palbociclib, and the authors argue RB1 protein + phospho-Rb status should guide patient selection over CDKN2A status alone [PMID:34358469](../papers/34358469.md)
- In CDK4/6i-resistant ER+ breast cancer, INK4-bound CDK6 selectively shrinks the palbociclib-binding pocket by 85% (computational modeling); CDK6-high (FAT1-null) cells have palbociclib IC50 252 nM vs 19 nM in parental MCF7. Palbociclib-based PROTACs (BSJ-05-017, BSJ-03-096) overcome INK4-locked CDK6 in xenograft models. [PMID:34544752](../papers/34544752.md)
- In NF1-null HER2+ breast cancer, palbociclib IC50 rises from 292 nM (control) to 857 nM (NF1-depleted cells), demonstrating CDK4/6 inhibitor resistance in MAPK-activated HER2+ disease where CDK2 supplants CDK4/6 as the dominant G1/S regulator. [PMID:34795269](../papers/34795269.md)

## Resistance mechanisms

- Not reported in corpus.

## Cancer types (linked)

- [WDLS](../cancer_types/WDLS.md), [DDCHS](../cancer_types/DDCHS.md), [PECOMA](../cancer_types/PECOMA.md), [DDLS](../cancer_types/DDLS.md)

## Sources

- [PMID:39305899](../papers/39305899.md) — Duminuco et al. 2024, UCLA PDTO sarcoma functional screen; CDK4/6 inhibitor testing context.
- [PMID:20601955](../papers/20601955.md) — Barretina et al. 2010, Nature Genetics; functional validation of [CDK4](../genes/CDK4.md) dependency in [DDLS](../cancer_types/DDLS.md); G1 arrest by palbociclib (PD0332991).

- [PMID:24798001](../papers/24798001.md)
- [PMID:25855536](../papers/25855536.md)
- [PMID:28027327](../papers/28027327.md) — Lefebvre et al. 2016, metastatic breast cancer WES; RB1 loss in 5% of HR+/HER2- mBC may confer primary palbociclib resistance.
- [PMID:28988769](../papers/28988769.md)
- [PMID:32404308](../papers/32404308.md)
- [PMID:33212010](../papers/33212010.md) — Krug et al. 2020, *Cell* (CPTAC BRCA proteogenomics). Rb protein/phosphosite levels refine CDK4/6 inhibitor sensitivity prediction beyond RB1 genotype; GDSC evidence ρ = −0.61 for Rb protein ~ palbociclib response in RB1-WT lines.

*This page was processed by **entity-page-writer** on **2026-05-16**.*

*This page was processed by **entity-page-writer** on **2026-05-16**.*
- [PMID:34358469](../papers/34358469.md)

*This page was processed by **entity-page-writer** on **2026-05-16**.*
- [PMID:34544752](../papers/34544752.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:34795269](../papers/34795269.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
