---
name: TP53 Inactivation Classifier
slug: tp53-inactivation-classifier
kind: method
canonical_source: corpus
unverified: true
tags: [machine-learning, expression-classifier, biomarker, tp53, pancanatlas]
processed_by: crosslinker
processed_at: 2026-05-16
---

# TP53 Inactivation Classifier

## Overview

The [TP53](../genes/TP53.md) inactivation classifier is a pre-trained machine-learning model that uses bulk RNA-seq gene expression profiles to predict functional inactivation of the TP53 pathway, independent of TP53 mutation status. Developed as part of the TCGA PanCanAtlas project (Knijnenburg et al. 2018; Way et al. 2017/2018), the classifier assigns a continuous inactivation score: high scores indicate TP53-pathway-inactive tumors, including those with [MDM2](../genes/MDM2.md) amplification, [RB1](../genes/RB1.md) deletion, or other phenocopies that inactivate the p53 pathway without a direct TP53 mutation. The model was trained on TCGA adult tumor data and achieves AUROC ~0.89 when validated against genomically-confirmed TP53-altered samples.

## Used by

- Applied to 244 RNA-seq PPTC pediatric PDX models; achieved AUROC=0.89 distinguishing TP53-pathway-inactive from active models; TP53 classifier scores were significantly higher in TP53-altered (mean 0.790) vs. unaltered (mean 0.419) models (Wilcoxon p<2.2e-16); models with MDM2 and RB1 alterations also scored high; copy-number burden (R=0.51, p=1.8e-17) but not TMB correlated with classifier score [PMID:31693904](../papers/31693904.md).

## Notes

- Corpus-grown slug; no matching `genePanelId` in cBioPortal ontology.
- Trained on TCGA adult tumor data; prospective validation in pediatric PDX response studies still needed before clinical translation (AUROC for RAS classifier was only 0.55 in pediatric models, suggesting pediatric-specific biology).
- Authors propose using classifier scores — rather than gene-level TP53 mutation status alone — to nominate tumors for TP53-pathway-targeting therapy, as functionally inactive cases driven by MDM2, RB1, or gene fusions would be missed by mutation-only screening.
- See also: [NF1 inactivation classifier](../methods/nf1-inactivation-classifier.md).

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
