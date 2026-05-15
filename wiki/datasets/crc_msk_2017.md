---
name: MSK CRC IMPACT Cohort (2017)
studyId: crc_msk_2017
institution: Memorial Sloan Kettering Cancer Center
size: 1134
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - msk-impact-panel
panels:
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - metastatic-crc
  - colorectal-cancer
  - msi
  - sidedness
  - wnt-pathway
  - clinical-actionability
  - prospective-sequencing
processed_by: crosslinker
processed_at: 2026-05-15
---

# MSK CRC IMPACT Cohort (2017)

## Overview

Prospective targeted sequencing cohort of 1,134 colorectal adenocarcinomas assembled at Memorial Sloan Kettering Cancer Center using the [MSK-IMPACT](../methods/msk-impact-panel.md) panel. The cohort comprises 1,011 tumors from 979 patients with metastatic CRC plus 123 tumors from 120 patients with early-stage CRC. This is one of the largest prospectively sequenced CRC cohorts and defines the landscape of microsatellite-stable (MSS), MSI-H/hypermutated, and POLE-mutant colorectal cancer in a clinical setting. Data are publicly available on cBioPortal (`crc_msk_2017`) and at European Variation Archive accession PRJEB23844. [PMID:29316426](../papers/29316426.md)

## Composition

- **1,134 colorectal adenocarcinomas**: 1,011 tumors (478 primaries, 533 metastases) from 979 metastatic CRC patients, plus 123 tumors from 120 early-stage CRC patients. [PMID:29316426](../papers/29316426.md)
- **Cancer types:** [COADREAD](../cancer_types/COADREAD.md) ([COAD](../cancer_types/COAD.md) and [READ](../cancer_types/READ.md)). [PMID:29316426](../papers/29316426.md)
- **Molecular subtypes:** 1,027 MSS (90.6%), 99 MSI-H/hypermutated (8.7%), 8 POLE-mutant (0.7%); 4% of mCRC cases were MSI-H. [PMID:29316426](../papers/29316426.md)
- **Sidedness:** Cohort annotated for primary tumor laterality; right-sided vs. left-sided comparisons are a major analytical axis. [PMID:29316426](../papers/29316426.md)
- **Tissue/procedure:** 70% resection / 30% needle biopsy; 52% pre-treatment samples. Matched tumor/normal calling in a CLIA-certified lab. [PMID:29316426](../papers/29316426.md)
- **Median follow-up:** 23.7 months for MSS early-stage; 28.6 months for MSS mCRC. [PMID:29316426](../papers/29316426.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) hybridization capture NGS — panel expanded during study period:
  - [IMPACT341](../methods/IMPACT341.md): 214 cases
  - [IMPACT410](../methods/IMPACT410.md): 911 cases
  - [IMPACT468](../methods/IMPACT468.md): 9 cases
- Mean coverage 747x; MSI status assigned by [MSIsensor](../methods/msisensor.md) score ≥10 (98.6% concordance with MMR IHC). [PMID:29316426](../papers/29316426.md)

## Papers using this cohort

- [PMID:29316426](../papers/29316426.md) — Yaeger et al. 2018, *Cancer Cell* — "Clinical sequencing defines the genomic landscape of metastatic colorectal cancer"

## Notable findings derived from this cohort

- 47 significantly recurrently mutated genes in MSS CRC identified via [MutSig](../methods/mutsig.md) and [MuSiC](../methods/genome-music.md). Top frequencies: [APC](../genes/APC.md) 79%, [TP53](../genes/TP53.md) 78%, [KRAS](../genes/KRAS.md) 44%, [PIK3CA](../genes/PIK3CA.md) 18%, [SMAD4](../genes/SMAD4.md) 16%. [PMID:29316426](../papers/29316426.md)
- WNT pathway alterations reach 96% of CRCs when an intronic [APC](../genes/APC.md) splice-acceptor variant (chr5:112151184 A>G) and large [CTNNB1](../genes/CTNNB1.md) exon-3 in-frame deletions are included. [PMID:29316426](../papers/29316426.md)
- Right-sided MSS mCRC has shorter 5-year [OS](../cancer_types/OS.md) (45% vs. 67%, p<0.001), higher mutation burden, and enrichment of [KRAS](../genes/KRAS.md), [BRAF](../genes/BRAF.md), [PIK3CA](../genes/PIK3CA.md), [AKT1](../genes/AKT1.md), [RNF43](../genes/RNF43.md), and [SMAD4](../genes/SMAD4.md) vs. left-sided. [PMID:29316426](../papers/29316426.md)
- 37% of left-sided MSS mCRC have no detectable mitogenic-signaling alteration, with higher expression of RTK ligands (amphiregulin, epiregulin, neuregulin, [HGF](../genes/HGF.md)) suggesting ligand-driven activation. [PMID:29316426](../papers/29316426.md)
- Five genomic mitogenic-pathway subgroups (RTK-only, RAS-MAPK, PI3K, concurrent, none) were defined and largely explain the right-vs-left survival gap. [PMID:29316426](../papers/29316426.md)
- Multivariate survival: [APC](../genes/APC.md) alterations favorable (HR=0.57); [BRAF](../genes/BRAF.md) (HR=2.02), [KRAS](../genes/KRAS.md) (HR=1.40), and [NRAS](../genes/NRAS.md) (HR=2.59) unfavorable; primary tumor side not significant after genomic adjustment. [PMID:29316426](../papers/29316426.md)
- 86% of MSI-H/hypermutated vs. 37% of MSS mCRC harbored potentially actionable alterations per OncoKB. [PMID:29316426](../papers/29316426.md)

## Sources

- cBioPortal study: `crc_msk_2017`
- European Variation Archive: PRJEB23844
- DOI: [10.1016/j.ccell.2017.12.004](https://doi.org/10.1016/j.ccell.2017.12.004)

*This page was processed by **crosslinker** on **2026-05-15**.*
