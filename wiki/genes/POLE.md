---
symbol: POLE
aliases: []
cancer_types: [UCEC, PRAD, COAD]
tags: [dna-polymerase, ultramutator, immunotherapy-biomarker, tmb]
processed_by: wiki-cli
processed_at: 2026-05-11
canonical_source: cbioportal
unverified: false
---

# POLE

## Overview

POLE encodes the catalytic and proofreading subunit of DNA polymerase epsilon. Hotspot mutations in the exonuclease domain (e.g., P286R, V411M, F367S) abrogate proofreading activity and produce an ultramutator phenotype with extremely high TMB (often >100 mut/Mb). POLE-mutant tumors are exquisitely sensitive to immune checkpoint blockade and carry a favorable prognosis in endometrial cancer.

## Alterations observed in the corpus

- POLE exonuclease domain hotspot mutations rare in Black endometrial cancer patients (1.2% vs. 5.8% in White patients); this favorable-prognosis subtype is substantially underrepresented in the Black EC population, contributing to disparities in access to immunotherapy-eligible molecularly favorable tumors [PMID:37651310](../papers/37651310.md).
- One POLE exonuclease domain hotspot mutation (p.F367S) identified in an MSS gynecologic cancer patient; this patient had the highest TMB in the cohort and was MSS, confirming POLE mutation as an independent route to hypermutation [PMID:38653864](../papers/38653864.md).
- Three prostate cancer patients harbored oncogenic POLE mutations (P286R ×2, V411M ×1; TMBs of 183, 34, and 169 mut/Mb), all with microsatellite-stable tumors; none of the ICB-treated patients in this cohort had POLE mutations [PMID:38949888](../papers/38949888.md).
- POLE exonuclease-domain mutations (e.g. V411L) explain discordant MiMSI MSI calls in pan-cancer NGS data: two MiMSI false-negatives had POLE-deficient mutational signatures plus high TMB; one false-positive (Sample_54409, colon adenocarcinoma) attributed 72% of mutations to POLE deficiency. MiMSI can flag MMR phenotype even when co-occurring with POLE-driven hypermutation. [PMID:39746944](../papers/39746944.md)
- p.E830G missense mutation in a myoepithelial carcinoma patient (Patient 2) [PMID:36577525](../papers/36577525.md)
- POLE assessed in metastatic UC (UC-GENOME cohort) in the context of tumor mutational burden and DNA repair pathway analysis [PMID:36333289](../papers/36333289.md)
- Somatic mutations in the ultramutated subset of colorectal tumors lacking MSI-H; defines a distinct hypermutation mechanism in the 276-tumor TCGA CRC cohort [PMID:22810696](../papers/22810696.md)
- Exonuclease-domain hotspots Pro286Arg and Val411Leu define the ultramutated endometrial cancer subgroup (Q=4.2×10⁻²³); associated with C→A transversion-rich mutational spectrum and improved progression-free survival [PMID:23636398](../papers/23636398.md)
- No somatic mutations identified across 23 pancreatic acinar cell carcinomas and pancreatoblastomas; wild-type status documented alongside [POLD1](../genes/POLD1.md) in this exome sequencing cohort [PMID:24293293](../papers/24293293.md)
- POLE inactivating mutation in one hypermutator gastric cancer case consistent with prior TCGA findings in CRC/endometrial [PMID:25079317](../papers/25079317.md)

## Cancer types (linked)

- Endometrial carcinoma ([UCEC](../cancer_types/UCEC.md)) — POLE exonuclease domain mutations define the ultramutator subtype with favorable prognosis; underrepresented in Black patients (1.2% vs. 5.8%) [PMID:37651310](../papers/37651310.md).
- Gynecologic cancers ([UCEC](../cancer_types/UCEC.md) / [OVT](../cancer_types/OVT.md)) — POLE p.F367S generates extreme TMB in the MSS background, representing a distinct hypermutation mechanism [PMID:38653864](../papers/38653864.md).
- Prostate cancer ([PRAD](../cancer_types/PRAD.md)) — POLE mutations (P286R, V411M) produce TMB-H/MSS phenotype; not clearly associated with ICB benefit in this small series [PMID:38949888](../papers/38949888.md).
- Pan-cancer (MSK-IMPACT) — POLE deficiency co-occurs with dMMR in rare cases; MiMSI detects the MMR component even when POLE ultramutation dominates the mutational landscape. Colon adenocarcinoma exemplar had 72% POLE-attributed mutations alongside [MSH2](../genes/MSH2.md) E580* truncation. [PMID:39746944](../papers/39746944.md)

## Co-occurrence and mutual exclusivity

- POLE ultramutator mutations are typically mutually exclusive with MSI-H/dMMR; they produce TMB-H/MSS tumors with a distinct mutational signature.
- In prostate cancer, POLE mutations were absent from the ICB-treated patient cohort, limiting conclusions about response [PMID:38949888](../papers/38949888.md).

## Therapeutic relevance

- POLE ultramutator endometrial cancers have favorable prognosis and excellent response to immune checkpoint blockade regardless of MSI status; POLE mutation is an FDA-recognized tumor-agnostic biomarker for [pembrolizumab](../drugs/pembrolizumab.md).
- The underrepresentation of POLE-mutant ECs in Black patients reduces immunotherapy eligibility in this population [PMID:37651310](../papers/37651310.md).
- In prostate cancer, the clinical significance of POLE mutations for ICB response is uncertain; TMB-H/MSS prostate cancer does not appear to respond as well to ICB as MSI-H/dMMR disease [PMID:38949888](../papers/38949888.md).

## Open questions

- The mechanistic basis for the lower occurrence of POLE ultramutator ECs in Black patients remains unknown [PMID:37651310](../papers/37651310.md).
- Whether POLE-mutant prostate cancers are a subset of TMB-H/MSS that respond better to ICB requires evaluation in larger cohorts [PMID:38949888](../papers/38949888.md).

## Sources

- [PMID:37651310](../papers/37651310.md)
- [PMID:38653864](../papers/38653864.md)
- [PMID:38949888](../papers/38949888.md)
- [PMID:39746944](../papers/39746944.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:36577525](../papers/36577525.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:36333289](../papers/36333289.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:22810696](../papers/22810696.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:23636398](../papers/23636398.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24293293](../papers/24293293.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:25079317](../papers/25079317.md)

*This page was processed by **wiki-cli** on **2026-05-11**.*
