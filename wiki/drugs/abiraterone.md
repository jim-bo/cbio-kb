---
name: abiraterone
targets: [CYP17A1]
drug_class: androgen biosynthesis inhibitor (CYP17A1 inhibitor)
canonical_source: corpus
unverified: true
tags: [targeted-therapy, hormone-therapy, prostate-cancer]
processed_by: crosslinker
processed_at: 2026-05-21
---

# abiraterone

## Overview

Abiraterone acetate is a selective, irreversible inhibitor of CYP17A1 (17α-hydroxylase/C17,20-lyase), blocking androgen biosynthesis in the testes, adrenal glands, and tumor tissue. It is used in combination with [prednisone](../drugs/prednisone.md) for metastatic castration-resistant and castration-sensitive prostate cancer. In the MSK-CHORD dataset it appears as a recorded systemic therapy for prostate cancer patients.

## Evidence in the corpus

- Abiraterone is listed as a tracked systemic therapy drug in the MSK-CHORD ([msk_chord_2024](../datasets/msk_chord_2024.md)) dataset covering 3,211 [PRAD](../cancer_types/PRAD.md) patients. NLP-based annotation of prior treatment history (using transformer models) was used to identify patients who had received abiraterone, enabling post-treatment alteration enrichment analyses including [AR](../genes/AR.md) and [TP53](../genes/TP53.md) enrichment after prior systemic therapy in prostate cancer. [PMID:39506116](../papers/39506116.md)
- Abiraterone pre-treatment context: AR-V7 splice variant was detectable at low ratios in most pre-abiraterone/enzalutamide mCRPC cases; recurrent [AR](../genes/AR.md) hotspots (T878A, W742C, L702H) that confer agonism predict differential responses to ADT including abiraterone [PMID:26000489](../papers/26000489.md)
- Variable [AR](../genes/AR.md) transcriptional output across [PRAD](../cancer_types/PRAD.md) subtypes implies subtype-stratified responses to AR-directed therapies; abiraterone named alongside [enzalutamide](../drugs/enzalutamide.md) as relevant for SPOP/FOXA1-mutant primary tumors with highest [AR](../genes/AR.md) output [PMID:26544944](../papers/26544944.md)
- A patient (WCMC161) whose CRPC-NE liver metastasis arose while on abiraterone therapy provided clonal phylogenetic evidence for divergent evolution from a CRPC-Adeno precursor; CRPC-NE tumors with high NEPC classifier scores are predicted unlikely to respond to further abiraterone or [enzalutamide](../drugs/enzalutamide.md) [PMID:26855148](../papers/26855148.md)
- Only 3 of 63 mCRPC men in the [prad_fhcrc](../datasets/prad_fhcrc.md) rapid-autopsy cohort had received abiraterone; the authors note that the small n prevented assessment of whether this potent [AR](../genes/AR.md) antagonist induces divergent inter-metastasis resistance mechanisms (AR amplification, AR ligand-binding-domain mutation, AR splice variants). [PMID:26928463](../papers/26928463.md)
- In the mCRPC cohort (n=128 first-line ARSI, [prad_su2c_2019](../datasets/prad_su2c_2019.md)), AR alteration was associated with shorter time on first-line abiraterone (P=0.005, CPE=0.651), while [RB1](../genes/RB1.md) alteration (multivariate RR 6.56) was the dominant predictor of ARSI failure; abiraterone and [enzalutamide](../drugs/enzalutamide.md) were pooled as androgen-receptor signaling inhibitors (ARSIs) in the analysis. [PMID:31061129](../papers/31061129.md)
- AR alterations predict androgen-axis treatment failure in mCSPC; abiraterone (with enzalutamide and [apalutamide](../drugs/apalutamide.md)) is a next-generation AR-pathway therapy for which NOTCH-pathway status, [CDK12](../genes/CDK12.md) biallelic inactivation, and AR alteration profiles may stratify benefit [PMID:32220891](../papers/32220891.md)
- Time on first-line abiraterone or enzalutamide in castration-resistant prostate cancer was not significantly different between CDK12-altered and CDK12-WT patients (median 9.7 vs 8.7 months; aHR 1.08, 95% CI 0.57–1.51; p=0.8) [PMID:32317181](../papers/32317181.md)
- In prostate cancer brain metastases (PCBM), 11/42 (26%) of ADT-treated patients had received abiraterone and/or enzalutamide (next-generation ARSi), establishing clinical context for HRR-targeted therapy evaluation in the PCBM setting [PMID:35504881](../papers/35504881.md)
- CRPC-SCL subtype (stem cell-like, YAP/TAZ/AP-1-driven) had significantly shorter time on next-generation ARSi including abiraterone among 56 SU2C CRPC patients, suggesting CRPC-SCL classification could deprioritize abiraterone escalation (Cox log-rank) [PMID:35617398](../papers/35617398.md)
- In mCRPC, the IPATential150 trial (NCT03072238) tested [ipatasertib](../drugs/ipatasertib.md) + abiraterone/prednisone and showed improved radiographic PFS only in PTEN-loss patients (HR 0.77, 95% CI 0.61–0.98); PIK3R1-altered patients were not formally analyzed despite mechanistic rationale for AKT-inhibitor benefit [PMID:35670774](../papers/35670774.md).

## Resistance mechanisms

- [AR](../genes/AR.md) and [TP53](../genes/TP53.md) alterations are enriched in [PRAD](../cancer_types/PRAD.md) patients with prior systemic therapy (annotated by NLP from clinical notes), consistent with the endocrine-resistance signature seen after androgen deprivation and androgen-receptor–targeted agents including abiraterone. [PMID:39506116](../papers/39506116.md)
- CRPC-NE, which lacks [AR](../genes/AR.md) amplification and activating mutations, is the dominant resistance phenotype emerging on abiraterone; the 70-gene NEPC classifier identifies tumors transitioning toward this AR-independent state that are unlikely to benefit from continued abiraterone [PMID:26855148](../papers/26855148.md)

## Cancer types (linked)

- [PRAD](../cancer_types/PRAD.md) — metastatic castration-resistant prostate cancer (mCRPC); CRPC-NE subtype emerges as an abiraterone-resistant state [PMID:26855148](../papers/26855148.md)

## Sources

- [PMID:39506116](../papers/39506116.md)
- [PMID:26000489](../papers/26000489.md)
- [PMID:26544944](../papers/26544944.md)
- [PMID:26855148](../papers/26855148.md)
- [PMID:26928463](../papers/26928463.md)
- [PMID:31061129](../papers/31061129.md)
- [PMID:32220891](../papers/32220891.md)
- [PMID:32317181](../papers/32317181.md)
- [PMID:35504881](../papers/35504881.md)
- [PMID:35617398](../papers/35617398.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35670774](../papers/35670774.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
