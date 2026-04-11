---
symbol: PIK3CA
aliases: []
cancer_types: [LUAD, LCH, ECD, OGCT, BLCA, UTUC, BRCA, NSCLC, EGC, CESC, UCEC, HCC, THAP, RMS, ERMS]
tags: [pi3k-pathway, actionable]
processed_by: crosslinker
processed_at: 2026-04-11
---

# PIK3CA

## Overview

PIK3CA encodes the catalytic p110-alpha subunit of PI3K. In the corpus it appears as a subclonal resistance driver in [NSCLC](../cancer_types/NSCLC.md) ctDNA, a lineage-conditioned actionable driver in histiocytosis vs germ cell tumors, and a metastasis-differentiating gene in [LUAD](../cancer_types/LUAD.md).

## Alterations observed in the corpus

- Enriched among ctDNA-only alterations (not detected by time-matched tissue) in advanced [NSCLC](../cancer_types/NSCLC.md); flagged as a subclonal resistance driver associated with short survival [PMID:36357680](../papers/36357680.md).
- Among ten genes differentially altered between ever- and never-metastatic [LUAD](../cancer_types/LUAD.md) primary tumors in the 2,532-specimen MSK organotropism cohort; altered less in metastases than primaries [PMID:37084736](../papers/37084736.md).
- Mutated in one histiocytosis patient and two ovarian GCT patients in the Make-an-IMPACT rare-cancer program [PMID:36862133](../papers/36862133.md).
- PIK3CA was the most frequent PI3K-pathway co-alteration in FGFR2/3-altered urothelial carcinoma (28%, 115/414), but did not predict response to [erdafitinib](../drugs/erdafitinib.md) in the MSK [bladder_msk_2023](../datasets/bladder_msk_2023.md) cohort [PMID:37682528](../papers/37682528.md).
- PIK3CA mutations (with [PIK3R1](../genes/PIK3R1.md) and [TP53](../genes/TP53.md), plus broad CNV load) were used to define "molecular grade-intermediate" in 1p19q codeleted IDH-mutant oligodendrogliomas [PMID:37910594](../papers/37910594.md).
- PIK3CA p.E545K was common in breast cancer CSF ctDNA samples; PIK3CA also appeared as an off-target resistance alteration in EGFR-mutant lung cancer CSF ctDNA in the [csf_msk_2024](../datasets/csf_msk_2024.md) cohort (1,007 CSF samples, 711 patients) [PMID:39289779](../papers/39289779.md).
- PIK3CA alterations identified as resistance mechanisms in escape lesions in HER2-positive metastatic esophagogastric cancer ([EGC](../cancer_types/EGC.md)) treated with [pembrolizumab](../drugs/pembrolizumab.md) + [trastuzumab](../drugs/trastuzumab.md) + chemotherapy [PMID:37406106](../papers/37406106.md).
- PIK3CA mutations/amplifications in 25% of cervical cancers (N=177); enriched in squamous subtype (38%) vs. gastric type (5%); most common OncoKB level 3B alteration in this cohort [PMID:37643132](../papers/37643132.md).
- PIK3CA mutation frequency similar between Black and White endometrial carcinoma patients but with distinct alteration mechanism (more amplification in Black patients) [PMID:37651310](../papers/37651310.md).
- PIK3CA oncogenic alterations present in >10% of early-onset esophagogastric cancer patients with no significant differential frequency vs. average-onset [PMID:37699004](../papers/37699004.md).
- PIK3CA oncogenic mutations in 5/17 FN-RMS (fusion-negative rhabdomyosarcoma) as part of the RAS/PIK3CA pathway alteration cluster [PMID:37730754](../papers/37730754.md).
- PIK3CA oncogenic alterations in 8% of advanced hepatocellular carcinoma ([HCC](../cancer_types/HCC.md)) cases by cfDNA profiling (MSK-ACCESS); actionable at OncoKB level 3b [PMID:37769223](../papers/37769223.md).
- PIK3CA co-occurs with [BRAF](../genes/BRAF.md) V600E in anaplastic thyroid carcinoma (FDR = 0.034); preferentially mutated in ATCs and co-differentiated thyroid cancers relative to PTC [PMID:38412093](../papers/38412093.md).
- PIK3CA mutated in 48% of dMMR/MSI-H gynecologic cancers treated with [nivolumab](../drugs/nivolumab.md); not associated with clinical benefit or resistance to PD-1 blockade [PMID:38653864](../papers/38653864.md).
- PIK3CA plasma detection associated with VTE risk (adjusted HR = 1.47, 95% CI: 1.01--2.13, N=254 patients) in pan-cancer ctDNA liquid biopsy cohort; in multivariate analysis, individual gene-level alterations including PIK3CA were not independently associated with VTE after controlling for ctDNA detection [PMID:39147831](../papers/39147831.md).

## Cancer types (linked)

- Non-small-cell lung cancer ([LUAD](../cancer_types/LUAD.md)) — ctDNA-only subclonal resistance driver [PMID:36357680](../papers/36357680.md); altered less in metastases than primaries [PMID:37084736](../papers/37084736.md).
- Histiocytosis ([LCH](../cancer_types/LCH.md), [ECD](../cancer_types/ECD.md)) — actionable with [alpelisib](../drugs/alpelisib.md) [PMID:36862133](../papers/36862133.md).
- Ovarian germ cell tumor ([OGCT](../cancer_types/OGCT.md)) — non-responsive to [alpelisib](../drugs/alpelisib.md) in this cohort [PMID:36862133](../papers/36862133.md).
- [BLCA](../cancer_types/BLCA.md) / [UTUC](../cancer_types/UTUC.md) — common co-alteration in FGFR3-altered tumors (28%), not predictive of [erdafitinib](../drugs/erdafitinib.md) response [PMID:37682528](../papers/37682528.md).
- [BRCA](../cancer_types/BRCA.md) — PIK3CA p.E545K frequently altered in breast cancer CSF ctDNA [PMID:39289779](../papers/39289779.md).
- [NSCLC](../cancer_types/NSCLC.md) — off-target resistance alteration in EGFR-mutant lung cancer CSF ctDNA [PMID:39289779](../papers/39289779.md).
- Esophagogastric cancer ([EGC](../cancer_types/EGC.md)) — resistance mechanism in HER2-positive EGC on pembrolizumab + trastuzumab [PMID:37406106](../papers/37406106.md).
- Cervical cancer ([CESC](../cancer_types/CESC.md)) — most common actionable alteration (25%), enriched in squamous histology [PMID:37643132](../papers/37643132.md).
- Endometrial carcinoma ([UCEC](../cancer_types/UCEC.md)) — similar frequency across racial groups; more amplification mechanism in Black patients [PMID:37651310](../papers/37651310.md); not predictive of nivolumab response in dMMR disease (48% mutation frequency) [PMID:38653864](../papers/38653864.md).
- Hepatocellular carcinoma ([HCC](../cancer_types/HCC.md)) — 8% by cfDNA; actionable at OncoKB level 3b [PMID:37769223](../papers/37769223.md).
- Anaplastic thyroid carcinoma ([THAP](../cancer_types/THAP.md)) — co-occurs with BRAF V600E (FDR = 0.034); enriched in ATC vs. PTC [PMID:38412093](../papers/38412093.md).
- Rhabdomyosarcoma ([RMS](../cancer_types/RMS.md) / [ERMS](../cancer_types/ERMS.md)) — RAS/PIK3CA pathway alterations in 5/17 FN-RMS [PMID:37730754](../papers/37730754.md).

## Co-occurrence and mutual exclusivity

- Appears in ctDNA-only alteration spectrum alongside [RICTOR](../genes/RICTOR.md) in [NSCLC](../cancer_types/NSCLC.md) [PMID:36357680](../papers/36357680.md).

## Therapeutic relevance

- One PIK3CA-mutant histiocytosis patient had a durable response to [alpelisib](../drugs/alpelisib.md); two PIK3CA-mutant ovarian GCT patients had no durable response, suggesting lineage-specific conditioning of PI3K inhibitor response [PMID:36862133](../papers/36862133.md).

## Open questions

- Whether ctDNA-only PIK3CA subclonal resistance alterations should directly alter [NSCLC](../cancer_types/NSCLC.md) treatment selection [PMID:36357680](../papers/36357680.md).
- Mechanism of lineage-specific [alpelisib](../drugs/alpelisib.md) response divergence [PMID:36862133](../papers/36862133.md).

## Sources

- [PMID:36357680](../papers/36357680.md)
- [PMID:36862133](../papers/36862133.md)
- [PMID:37084736](../papers/37084736.md)
- [PMID:37406106](../papers/37406106.md)
- [PMID:37643132](../papers/37643132.md)
- [PMID:37651310](../papers/37651310.md)
- [PMID:37682528](../papers/37682528.md)
- [PMID:37699004](../papers/37699004.md)
- [PMID:37730754](../papers/37730754.md)
- [PMID:37769223](../papers/37769223.md)
- [PMID:37910594](../papers/37910594.md)
- [PMID:38412093](../papers/38412093.md)
- [PMID:38653864](../papers/38653864.md)
- [PMID:39147831](../papers/39147831.md)
- [PMID:39289779](../papers/39289779.md)

*This page was processed by **crosslinker** on **2026-04-11**.*
