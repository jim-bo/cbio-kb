---
name: CPTAC Pancreatic Ductal Adenocarcinoma (Cell 2021)
studyId: paad_cptac_2021
institution: Clinical Proteomic Tumor Analysis Consortium (CPTAC)
size: 140
reference_genome: GRCh38
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
  - MRNA_EXPRESSION
  - PROTEIN_LEVEL
  - PHOSPHOPROTEIN
panels: []
tags:
  - pancreas
  - PAAD
  - PDAC
  - proteogenomics
  - CPTAC
  - glycoproteomics
  - multi-omic
processed_by: crosslinker
processed_at: 2026-05-16
---

# CPTAC Pancreatic Ductal Adenocarcinoma (Cell 2021)

## Overview

Integrated proteogenomic characterization of 140 treatment-naive pancreatic tumors (135 PDACs + 5 pancreatic adenosquamous carcinomas), 67 paired normal adjacent tissues (NATs), and 9 macrodissected normal pancreatic ductal tissues, collected prospectively by the Clinical Proteomic Tumor Analysis Consortium (CPTAC) from multiple international sites with controlled ischemia time. Eight omics layers were applied to the same tissue portion. Published in Cell 2021; available on cBioPortal as `paad_cptac_2021`. [PMID:34534465](../papers/34534465.md)

## Composition

- 140 treatment-naive pancreatic tumors (135 [PAAD](../cancer_types/PAAD.md) + 5 [PAASC](../cancer_types/PAASC.md)), 67 paired NATs, 9 normal pancreatic ductal tissues.
- 75% of resected tumors from pancreatic head; 59% Stage I–II, 9 Stage IV; 42% alive at data freeze.
- Risk-factor prevalence: smoking 37%, chronic pancreatitis 22%, obesity 11%, type II diabetes 28%.
- 105/140 samples passed neoplastic-purity QC ([KRAS](../genes/KRAS.md) VAF ≥ 0.075, equivalent to ≥15% neoplastic cellularity; 4 KRAS-WT tumors retained based on other SMG alterations). [PMID:34534465](../papers/34534465.md)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — somatic mutations, indels, CNA backbone.
- [whole-genome-seq](../methods/whole-genome-seq.md) — structural variants.
- [rna-seq](../methods/rna-seq.md) — 28,057 genes quantified.
- [mirna-seq](../methods/mirna-seq.md) — 2,416 miRNAs quantified.
- [dna-methylation-array](../methods/dna-methylation-array.md) — 850,000 CpG sites.
- [tmt-proteomics](../methods/tmt-proteomics.md) — 11,662 proteins (mean 8,781/sample).
- [tmt-phosphoproteomics](../methods/tmt-phosphoproteomics.md) — 51,469 phosphosites (mean 25,764/sample).
- N/O-linked glycoproteomics ([lc-ms-ms-proteomics](../methods/lc-ms-ms-proteomics.md)) — 34,024 glycopeptides (30,660 N-linked + 3,364 O-linked).
- [xcell](../methods/xcell.md) and DNA-methylation deconvolution — immune/stromal composition.
- [nmf-clustering](../methods/nmf-clustering.md) — proteogenomic subtyping (C1 classical, C2 basal-like).
- [gsea](../methods/gsea.md) — gene set enrichment.

## Papers using this cohort

- [PMID:34534465](../papers/34534465.md) — CPTAC proteogenomic characterization of PDAC; defined C1 (classical) and C2 (basal-like) proteogenomic subtypes with HR 3.4 vs Moffitt RNA-only HR 2.3; identified candidate early-detection secreted proteins and glycoproteins; implicated [PAK1](../genes/PAK1.md)/[PAK2](../genes/PAK2.md) as KRAS-downstream therapeutic targets; characterized an immune-cold subtype driven by endothelial remodeling and glycolysis. [PMID:34534465](../papers/34534465.md)

## Notable findings derived from this cohort

- [KRAS](../genes/KRAS.md) alterations in 97% of tumors (96% hotspot mutations + 1 amplification); G12D, G12V, and G12R dominant hotspots. [TP53](../genes/TP53.md) altered in 83%, [CDKN2A](../genes/CDKN2A.md) in 48%, [SMAD4](../genes/SMAD4.md) in 29%. [PMID:34534465](../papers/34534465.md)
- Two proteogenomic subtypes from NMF on CNV + mRNA + protein + phosphosite + glycosite: C1 (classical, pancreas beta-cell/bile-acid metabolism, KRAS-signaling suppression, SMAD4-enriched) and C2 (basal-like, EMT, DNA repair, glycolysis, hypoxia). Proteogenomic subtypes provided stronger prognostic separation than Moffitt RNA-only classification (CoxPH HR 3.4 vs 2.3). [PMID:34534465](../papers/34534465.md)
- 27 proteins consistently >2-fold upregulated in PDAC vs NAT after stromal/immune adjustment; 21 also elevated vs normal ductal tissue and in early-stage tumors; 12 are secreted (candidate early-detection biomarkers). [PMID:34534465](../papers/34534465.md)
- 75 N-linked glycoproteins upregulated >2-fold in tumors (48/75 DIA-validated); mucin-type O-linked glycoproteins [MUC1](../genes/MUC1.md), [MUC5AC](../genes/MUC5AC.md), [MUC13](../genes/MUC13.md) significantly upregulated including in early-stage tumors. [PMID:34534465](../papers/34534465.md)
- [CEACAM5](../genes/CEACAM5.md) and [CEACAM6](../genes/CEACAM6.md) upregulated specifically in KRAS G12D/G12V/Q61H tumors but not G12R; [CEACAM6](../genes/CEACAM6.md) overexpression linked to [gemcitabine](../drugs/gemcitabine.md) resistance. [PMID:34534465](../papers/34534465.md)
- [PAK1](../genes/PAK1.md) elevated in >70% and [PAK2](../genes/PAK2.md) in ~90% of tumors; both are downstream KRAS effectors via [RAC1](../genes/RAC1.md); concurrent upregulation with [MET](../genes/MET.md)/RAC1 observed. [PMID:34534465](../papers/34534465.md)
- Immune-cold tumors (majority) characterized by reduced endothelial-adhesion proteins, elevated VEGF and hypoxia pathway activity, and increased glycolysis; immune-hot tumors (~6% of cohort) enriched for CD8+ T cells, immune checkpoint molecules ([CTLA4](../genes/CTLA4.md), [PDCD1](../genes/PDCD1.md), [CD274](../genes/CD274.md), [IDO1](../genes/IDO1.md)), and endothelial cells. [PMID:34534465](../papers/34534465.md)
- Five kinase-substrate axes with FDA-approved or investigational inhibitors identified: [CDK7](../genes/CDK7.md)–[MCM2](../genes/MCM2.md), [AKT1](../genes/AKT1.md)–[FLNA](../genes/FLNA.md), [PAK1](../genes/PAK1.md)–[BAD](../genes/BAD.md) (S134), [PAK2](../genes/PAK2.md)–[MAPK6](../genes/MAPK6.md) (S189), [SRC](../genes/SRC.md)–[STAT3](../genes/STAT3.md). [PMID:34534465](../papers/34534465.md)

## Sources

- cBioPortal study: `paad_cptac_2021` (canonical, verified).
- Primary publication: [PMID:34534465](../papers/34534465.md).

*This page was processed by **crosslinker** on **2026-05-16**.*
