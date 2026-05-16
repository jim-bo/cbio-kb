---
name: NF1 Inactivation Classifier
slug: nf1-inactivation-classifier
kind: method
canonical_source: corpus
unverified: true
tags: [machine-learning, expression-classifier, biomarker, nf1, pancanatlas]
processed_by: crosslinker
processed_at: 2026-05-16
---

# NF1 Inactivation Classifier

## Overview

The [NF1](../genes/NF1.md) inactivation classifier is a pre-trained machine-learning model that uses bulk RNA-seq gene expression profiles to predict functional inactivation of the NF1/RAS pathway, independent of NF1 mutation status. Developed as part of the TCGA PanCanAtlas project (Way et al. 2017/2018), the classifier assigns a continuous inactivation score that identifies NF1-pathway-inactive tumors including those driven by alterations in RAS effectors or other pathway phenocopies. It was trained on adult TCGA tumor data and achieves AUROC ~0.77 when validated against genomically-confirmed NF1-altered samples.

## Used by

- Applied to 244 RNA-seq PPTC pediatric PDX models; achieved AUROC=0.77 distinguishing NF1-pathway-inactive from active models; authors propose using the classifier — rather than NF1 mutation status alone — to nominate tumors for NF1-loss-directed agents and to identify functionally inactive cases not captured by WES alone [PMID:31693904](../papers/31693904.md).

## Notes

- Corpus-grown slug; no matching `genePanelId` in cBioPortal ontology.
- Underperforms relative to the [TP53](../genes/TP53.md) classifier (AUROC 0.77 vs. 0.89) and the RAS classifier achieved only AUROC 0.55 in pediatric models — likely reflecting pediatric-specific RAS biology distinct from adult TCGA training data.
- Requires prospective validation in PDX response studies before clinical translation.
- See also: [TP53 inactivation classifier](../methods/tp53-inactivation-classifier.md).

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
