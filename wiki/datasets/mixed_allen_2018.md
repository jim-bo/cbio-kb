---
name: MSS Mixed Solid Tumors (Broad/Dana-Farber, Nat Genet 2018)
studyId: mixed_allen_2018
institution: Broad Institute / Dana-Farber Cancer Institute
size: 249
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
panels: []
tags:
  - pan-cancer
  - mixed
  - immune-checkpoint-blockade
  - microsatellite-stable
  - tumor-mutational-burden
  - van-allen-lab
  - icb-response
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSS Mixed Solid Tumors (Broad/Dana-Farber, Nat Genet 2018)

## Overview

A pan-cancer whole-exome sequencing cohort of 249 microsatellite-stable (MSS) tumors with matched germline samples and corresponding immune checkpoint blockade (ICB) clinical outcomes, assembled by Miao, Margolis, Vokes, and colleagues (Van Allen lab, Dana-Farber/Broad Institute). The cohort pools WES data from seven previously published ICB trial cohorts plus 78 newly sequenced Dana-Farber samples, all uniformly re-analyzed against RECIST 1.1 response. It covers melanoma, non-small cell lung cancer, bladder cancer, head and neck squamous cell carcinoma, anal cancer, and sarcoma. Published in Nature Genetics 2018.

## Composition

- 249 tumors after QC (314 starting samples); distribution by cancer type:
  - [SKCM](../cancer_types/SKCM.md) melanoma — N=151 (61%)
  - [NSCLC](../cancer_types/NSCLC.md) — N=57 (23%)
  - [BLCA](../cancer_types/BLCA.md) bladder cancer — N=27 (11%)
  - [HNSC](../cancer_types/HNSC.md) head and neck SCC — N=12 (5%)
  - [ANSC](../cancer_types/ANSC.md) anal cancer — N=1
  - [SARCNOS](../cancer_types/SARCNOS.md) sarcoma — N=1
- Treatment classes: anti-PD-1 N=74, anti-PD-L1 N=20, anti-CTLA-4 N=145, combination N=10, other N=7.
- Mean tumor WES coverage: 150× tumor / 119× germline; mean tumor purity 58% (range 10–97%).
- Raw BAMs deposited at dbGaP: phs000694.v3.p2, phs000980.v1.p1, phs001041.v1.p1, phs000452.v2.p1, phs001075.v1.p1, phs001565.v1.p1.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — tumor/normal WES; uniform reprocessing pipeline across all cohorts.
- [mutect](../methods/mutect.md) — SNV calling.
- [strelka](../methods/strelka.md) — indel calling.
- [oncotator](../methods/oncotator.md) — variant annotation.
- [absolute](../methods/absolute.md) — clonality, purity, and ploidy estimation.
- [polysolver](../methods/polysolver.md) — HLA typing from WES.
- [netmhcpan](../methods/netmhcpan.md) v3.0 — neoantigen prediction.
- [mutational-signatures](../methods/mutational-signatures.md) — NMF deconvolution against COSMIC signatures.

## Papers using this cohort

- [PMID:30150660](../papers/30150660.md) — Miao et al. Nature Genetics 2018: "Genomic correlates of response to immune checkpoint blockade in microsatellite-stable solid tumors."

## Notable findings derived from this cohort

- Clonal TMB was a stronger predictor of CR/PR vs. PD than total TMB; patients with >50% subclonal mutations (high intratumoral heterogeneity) were enriched for PD (p=0.0014) [PMID:30150660](../papers/30150660.md).
- Clonal driver mutations in [PIK3CA](../genes/PIK3CA.md), [KRAS](../genes/KRAS.md), and [PBRM1](../genes/PBRM1.md) were enriched in CR/PR; clonal [EGFR](../genes/EGFR.md) hotspot mutations were enriched in PD across cancer types [PMID:30150660](../papers/30150660.md).
- Biallelic [PTEN](../genes/PTEN.md) homozygous deletion occurred exclusively in PD patients (N=4); loss of intact interferon-γ signaling via CNAs (deletions of IFN genes or amplifications of SOCS1/SOCS3/PIAS1/PIAS4) also enriched in PD (p=0.019) [PMID:30150660](../papers/30150660.md).
- Focal amplifications on 11q ([PAK1](../genes/PAK1.md), [YAP1](../genes/YAP1.md), [CCND1](../genes/CCND1.md)) and 12q ([MDM2](../genes/MDM2.md), [CDK4](../genes/CDK4.md)) were predominantly observed in PD patients [PMID:30150660](../papers/30150660.md).
- In melanoma, dominant mutational signature (UV S7) was a stronger correlate of ICB response than TMB; TMB ceased to predict response after adjusting for signature — suggesting TMB is partly a proxy for UV-driven biology [PMID:30150660](../papers/30150660.md).
- [EGFR](../genes/EGFR.md)-hotspot [NSCLC](../cancer_types/NSCLC.md) tumors were subclonal-skewed, low-TMB, enriched in never-smokers, and showed poor ICB response; [KRAS](../genes/KRAS.md)-mutant smoker-signature NSCLC had favorable response profile [PMID:30150660](../papers/30150660.md).
- Power analysis established that detection of a common (~10% prevalence) response-associated driver variant requires ~300 samples under Bonferroni correction [PMID:30150660](../papers/30150660.md).

## Sources

- cBioPortal study: `mixed_allen_2018`
- Citation: Miao et al. Nature Genetics 2018; DOI: 10.1038/s41588-018-0200-2

*This page was processed by **crosslinker** on **2026-05-16**.*
