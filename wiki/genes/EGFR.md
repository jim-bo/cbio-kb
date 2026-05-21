---
symbol: EGFR
aliases:
  - ERBB1
  - HER1
cancer_types:
  - GBM
  - IHCH
  - EAC
tags: []
processed_by: crosslinker
processed_at: 2026-05-21
---

# EGFR

## Overview

EGFR (Epidermal Growth Factor Receptor, ERBB1) is a receptor tyrosine kinase and the founding member of the ERBB/HER family. Ligand binding or activating mutations trigger dimerization, autophosphorylation, and downstream activation of RAS/MAPK, PI3K/AKT, STAT, and PLCgamma pathways. EGFR amplification and structural variants (fusions, vIII deletion) are canonical events in glioblastoma, defining the classical subtype. EGFR also appears as a recurrent amplification in esophageal adenocarcinoma and intrahepatic cholangiocarcinoma at lower frequencies.

## Alterations observed in the corpus

- EGFR structural variants in 45/99 (45%) [GBM](../cancer_types/GBM.md) tumors ([gbm_cptac_2021](../datasets/gbm_cptac_2021.md)), all with concordant copy-number amplification (high SV-CNV concordance); EGFR mutation, SV, and amplification co-occurred (p < 0.01). Elevated RNA, protein, and Y1172 autophosphorylation in EGFR-altered tumors. EGFR phosphorylates [CTNNB1](../genes/CTNNB1.md) S33 (proteasomal-degradation site) and has trans effects on [PTPN11](../genes/PTPN11.md) Y62, [PLCG1](../genes/PLCG1.md) Y783, [GAB1](../genes/GAB1.md) Y657/Y689, [MAP3K1](../genes/MAP3K1.md) S1408, and [RB1](../genes/RB1.md) S795/Y805; strong cis effect at EGFR S1166 [PMID:33577785](../papers/33577785.md).
- EGFR amplification in 6 cases (rare, ~1.5%) of intrahepatic cholangiocarcinoma ([ihch_msk_2021](../datasets/ihch_msk_2021.md), n=412) [PMID:33765338](../papers/33765338.md).
- EGFR amplification is a recurrent driver at ≥5% in esophageal/GEJ adenocarcinoma ([egc_mskcc_2020](../datasets/egc_mskcc_2020.md), n=487); no independent [OS](../cancer_types/OS.md) association demonstrated in this cohort [PMID:33795256](../papers/33795256.md).
- EGFR P551L flagged as a single hotspot call requiring additional evidence in an 83-tumor [CSCC](../cancer_types/CSCC.md) meta-analysis; classified as 'possible false positive' [PMID:34272401](../papers/34272401.md)
- Recurrent oncogenic driver mutations and amplifications in [NSCLC](../cancer_types/NSCLC.md); EGFR mutations were enriched in cfDNA relative to tissue MSK-IMPACT in lung cancer in the MSK-ACCESS multi-cancer liquid biopsy study [PMID:34145282](../papers/34145282.md)
- Most frequently altered gene in [LUAD](../cancer_types/LUAD.md) (33% pN-negative / 31% pN-positive); no significant difference in alteration frequency by pathologic lymph node (pN) status in a 426-patient cohort [PMID:34290393](../papers/34290393.md)
- Protein significantly upregulated in LSCC and HNSCC but not [LUAD](../cancer_types/LUAD.md); EGFR amplification did not correlate with PROGENy EGFR pathway activity, which instead tracked mRNA abundance of five EGFR ligands; ligand abundance proposed as a better biomarker for response to cetuximab-class therapy in squamous lung tumors [PMID:34358469](../papers/34358469.md)
- Most frequently altered RTK-RAS gene in lung cancers from never smokers (LCINS; 30.6% overall, 51.4% in mezzo-forte SCNA subtype); mutations occur before clonal copy gain; MRCA appears ~8 yr before clinical diagnosis; independently associated with poor overall survival [PMID:34493867](../papers/34493867.md)
- EGFR alterations in 0.9% of metastatic and 1% of primary HER2+ breast tumors (n=733); low-frequency MAPK-pathway co-alteration context with [NF1](../genes/NF1.md), [KRAS](../genes/KRAS.md), [BRAF](../genes/BRAF.md), [MAP2K1](../genes/MAP2K1.md) [PMID:34795269](../papers/34795269.md)
- EGFR is a high-positive Δκ risk gene in [HGSOC](../cancer_types/HGSOC.md) ICI-treated patients, flagged as a putative network driver of ICI-modulated robustness alongside [EP300](../genes/EP300.md), [SMAD2](../genes/SMAD2.md), [PIK3R1](../genes/PIK3R1.md), [RB1](../genes/RB1.md), [ESR1](../genes/ESR1.md), [ATXN1](../genes/ATXN1.md) [PMID:34819508](../papers/34819508.md)
- Mutations enriched in LUAD patients with CNS/brain metastasis compared to primary tumors, supporting EGFR as a driver of brain-tropic metastatic spread in lung adenocarcinoma [PMID:35120664](../papers/35120664.md)
- EGFR and ERBB2/3/4 alterations together accounted for ~5% of CNS-tumor oncomap findings in the MAPPYACTS pediatric WES cohort (n=787); investigational ERBB-inhibitor matches were generated. [PMID:35292802](../papers/35292802.md)
- EGFR is referenced as an analogous oncogene-addicted system where compound on-target mutations and bypass signaling drive resistance to selective inhibitors, in the context of [selpercatinib](../drugs/selpercatinib.md) resistance mechanisms in RET-driven cancers. [PMID:35304457](../papers/35304457.md)
- Oncogenic EGFR mutations were identified in four never-smoker [SCLC](../cancer_types/SCLC.md) clinical samples, consistent with histologic transformation from EGFR-mutant LUAD; EGFR mutations also appeared in ~15% of PDX samples in an MSK [SCLC](../cancer_types/SCLC.md) biobank. [PMID:35440124](../papers/35440124.md)

## Cancer types (linked)

- **Glioblastoma ([GBM](../cancer_types/GBM.md)):** EGFR structural variants + amplification in 45% of tumors; classical subtype enriched; upregulates PHLDA1/PHLDA3, [SOX9](../genes/SOX9.md), [CTNND2](../genes/CTNND2.md), [CDK6](../genes/CDK6.md), and [CDKN2C](../genes/CDKN2C.md); converges on PTPN11/PLCG1 signaling hub; drug-connectivity analysis nominates broader kinase inhibitors beyond canonical EGFR inhibitors [PMID:33577785](../papers/33577785.md).
- **Intrahepatic cholangiocarcinoma ([IHCH](../cancer_types/IHCH.md)):** rare amplification (n=6); not prognostically significant in this cohort [PMID:33765338](../papers/33765338.md).
- **Esophageal/gastroesophageal junction adenocarcinoma ([EAC](../cancer_types/EAC.md)):** amplification at ≥5% frequency; co-occurs with [MYC](../genes/MYC.md), [VEGFA](../genes/VEGFA.md), [CDK6](../genes/CDK6.md), and [CCND3](../genes/CCND3.md) amplifications; no independent [OS](../cancer_types/OS.md) association [PMID:33795256](../papers/33795256.md).

## Co-occurrence and mutual exclusivity

- In GBM, EGFR alteration co-occurs with [PTPN11](../genes/PTPN11.md) Y62 phosphorylation, [PLCG1](../genes/PLCG1.md) Y783 phosphorylation, and [GAB1](../genes/GAB1.md) upregulation; EGFR-altered tumors show [GRB2](../genes/GRB2.md) downregulation [PMID:33577785](../papers/33577785.md).
- In [EAC](../cancer_types/EAC.md), EGFR amplification co-occurs with [MYC](../genes/MYC.md), [VEGFA](../genes/VEGFA.md), CDK6, and [CCND3](../genes/CCND3.md) amplifications as part of a broader amplification-driven recurrent driver landscape [PMID:33795256](../papers/33795256.md).

## Therapeutic relevance

- In GBM, phosphoproteomic drug-connectivity analysis (LINCS L1000 + P100) predicts that phosphoproteomic signatures of EGFR alteration are more strongly reversed by non-canonical kinase inhibitors than by approved EGFR inhibitors or HDAC inhibitors predicted from RNA alone [PMID:33577785](../papers/33577785.md).
- Convergent activation of PTPN11 and PLCG1 downstream of EGFR (and [PDGFRA](../genes/PDGFRA.md)) suggests these as alternative therapeutic targets in EGFR-altered GBM [PMID:33577785](../papers/33577785.md).

## Open questions

- Kinase-substrate relationships inferred from phospho-outlier analysis (e.g., EGFR → [CTNNB1](../genes/CTNNB1.md) S33) are not directly validated; functional confirmation required [PMID:33577785](../papers/33577785.md).
- Drug-connectivity predictions in GBM are signature-based with no preclinical or clinical confirmation reported in the corpus [PMID:33577785](../papers/33577785.md).

## Sources

- [PMID:33577785](../papers/33577785.md)
- [PMID:33765338](../papers/33765338.md)
- [PMID:33795256](../papers/33795256.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34272401](../papers/34272401.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34145282](../papers/34145282.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34290393](../papers/34290393.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34358469](../papers/34358469.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34493867](../papers/34493867.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34795269](../papers/34795269.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34819508](../papers/34819508.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35120664](../papers/35120664.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35292802](../papers/35292802.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35304457](../papers/35304457.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35440124](../papers/35440124.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
