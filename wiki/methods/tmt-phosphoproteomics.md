---
name: TMT phosphoproteomics
slug: tmt-phosphoproteomics
kind: method
canonical_source: corpus
unverified: true
tags:
  - proteomics
  - phosphoproteomics
  - mass-spectrometry
  - tandem-mass-tag
  - kinase-activity
  - multi-omics
processed_by: wiki-cli
processed_at: 2026-05-16
---

# TMT phosphoproteomics

## Overview

TMT phosphoproteomics combines isobaric tandem mass tag (TMT) labeling with phosphopeptide enrichment (typically by immobilized metal affinity chromatography, IMAC, or titanium dioxide) prior to LC-MS/MS analysis. This enables multiplexed, quantitative measurement of phosphosite abundance across tumor and normal samples. Phosphoproteomics data can be used to infer kinase activity, identify signaling pathway dysregulation, and detect post-translational modification changes that are invisible to genomic or transcriptomic approaches.

## Used by

- Applied to 96 CPTAC colon cancer tumor/NAT pairs ([coad_cptac_2019](../datasets/coad_cptac_2019.md)); quantified 7,295 phosphosites; 63 were upregulated >2-fold in tumors (mapping to 50 proteins); revealed [RB1](../genes/RB1.md) hyperphosphorylation at four E2F-regulating sites (T373, S807, S811, T826) as the principal Rb-pathway lesion (1.84-fold higher than NATs, p<2.2×10⁻¹⁶), with [CDK2](../genes/CDK2.md) predicted to be the dominant upstream kinase (r=0.47, p=1.8×10⁻⁶) [PMID:31031003](../papers/31031003.md)
- Performed with IMAC enrichment alongside global proteomics in the CPTAC endometrial carcinoma study (n=95 tumors); identified PLK1-T210 phosphorylation elevated in TP53-truncating mutant tumors and CHEK2-S163/TP53BP1-S1763 phosphorylation elevated in serous tumors [PMID:32059776](../papers/32059776.md).

## Notes

- In the CPTAC colon cohort, phosphoproteomics identified functional consequences of somatic mutations invisible to mRNA analysis: [APC](../genes/APC.md) truncating mutations reduced downstream APC-T2451 phosphorylation; [TGFBR2](../genes/TGFBR2.md) frameshifts reduced TGFBR2-S553 phosphorylation; TP53-R273 hotspot mutations caused >10-fold elevation of TP53-S315 phosphorylation.
- Phosphoproteomics also enabled kinase-activity inference, flagging CDK1/2/4/7, [MELK](../genes/MELK.md), [PFKFB3](../genes/PFKFB3.md), and [PI4KB](../genes/PI4KB.md) as elevated in colon tumors — most with available or in-development inhibitors.
- Not in cBioPortal gene-panels or molecular-profiles ontologies; corpus-grown slug.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
- [PMID:32059776](../papers/32059776.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
