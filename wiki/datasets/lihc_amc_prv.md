---
name: Hepatocellular Carcinoma — Asan Medical Center (AMC) Private Cohort
studyId: lihc_amc_prv
institution: Asan Medical Center, Seoul, Korea
size: 363
reference_genome: unknown
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - snp-array
panels: []
tags:
  - HCC
  - liver
  - hepatocellular-carcinoma
processed_by: entity-page-writer
processed_at: 2026-05-11
---

# Hepatocellular Carcinoma — Asan Medical Center (AMC) Private Cohort

## Overview

The lihc_amc_prv dataset is the Asan Medical Center (Seoul, Korea) hepatocellular carcinoma cohort, linked in the cBioPortal knowledge base. It is cited in a comprehensive molecular-landscape review of HCC by Llovet et al. (2018) that synthesises whole-exome sequencing data from 1,289 patients across multiple cohorts, including TCGA HCC (363 patients with all five molecular platforms), and SNP-array copy-number data from 704 patients.

## Composition

- Cancer types: [[cancer_types/HCC|HCC]] (hepatocellular carcinoma).
- Molecular profiling integrated in the 2018 review: WES (n = 1,289 pooled), SNP-array CNAs (n = 704 pooled).
- Largest single-institution genomic analysis cited: TCGA HCC (363 patients profiled across DNA copy number, methylation, mRNA, miRNA, RPPA platforms).

## Assays / panels (linked)

- Whole-exome sequencing
- SNP-array copy-number profiling

## Papers using this cohort

- [PMID:24798001](../papers/24798001.md) — Llovet et al., *Nature Reviews Clinical Oncology* 2018. Molecular therapies and precision medicine for hepatocellular carcinoma.

## Notable findings derived from this cohort

- [[genes/TERT|TERT]] promoter mutations are the single most frequent somatic alteration in HCC (54%, range 44–59% across 1,289 WES patients); [[genes/CTNNB1|CTNNB1]] activating mutations in 29%, [[genes/TP53|TP53]] LOF in 28% [PMID:24798001](../papers/24798001.md).
- High-level focal amplifications: [[genes/MYC|MYC]] 12%, [[genes/CCND1|CCND1]] 7%, [[genes/FGF19|FGF19]] 6%, [[genes/VEGFA|VEGFA]] 5% (n = 704 SNP-array patients) [PMID:24798001](../papers/24798001.md).
- Only ~25% of HCCs harbour potentially targetable driver alterations; the majority of trunk mutations (TERT promoter, CTNNB1, TP53, AXIN1, ARID1A, ARID1B) are not currently actionable [PMID:24798001](../papers/24798001.md).
- Two principal molecular subclasses identified: a *proliferation class* (~50%, enriched for TP53 inactivation, FGF19/CCND1 amplification, HBV aetiology, poor prognosis) and a *non-proliferation class* (~50%, canonical WNT via CTNNB1, higher TERT promoter mutation, HCV/alcohol aetiology, better prognosis) [PMID:24798001](../papers/24798001.md).
- Immune classification identifies ~30% of HCCs as an "immune class" with high [[genes/CD274|CD274]]/[[genes/PDCD1|PDCD1]] expression; ~25% as an "immune-excluded" class characterised by [[genes/CTNNB1|CTNNB1]] mutations and low T-cell infiltrate [PMID:24798001](../papers/24798001.md).

## Sources

- cBioPortal studyId: `lihc_amc_prv`
- Llovet JM et al. Molecular therapies and precision medicine for hepatocellular carcinoma. *Nat Rev Clin Oncol*. 2018. [PMID:24798001](../papers/24798001.md).

*This page was processed by **entity-page-writer** on **2026-05-11**.*
