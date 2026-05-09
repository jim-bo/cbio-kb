---
name: "JHU Pancreatic Acinar Cell Carcinoma / Pancreatoblastoma WES 2014"
studyId: paac_jhu_2014
institution: "Johns Hopkins University / Memorial Sloan Kettering Cancer Center / University Medical Center Utrecht"
size: 23
reference_genome: hg18
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - fish
  - msi-pcr-pentaplex
  - qmsp
panels: []
tags:
  - pancreatic-cancer
  - acinar-cell-carcinoma
  - pancreatoblastoma
  - chromosomal-instability
  - microsatellite-instability
  - fanconi-anemia-pathway
processed_by: crosslinker
processed_at: 2026-05-09
---

# JHU Pancreatic Acinar Cell Carcinoma / Pancreatoblastoma WES 2014

## Overview

The paac_jhu_2014 cohort was assembled by Jiao, Wood, Hruban, Papadopoulos and colleagues at Johns Hopkins University, MSKCC, and University Medical Center Utrecht to perform the first whole-exome sequencing study of pancreatic neoplasms with acinar differentiation. The study profiled 23 tumors spanning pure and mixed acinar cell carcinoma subtypes plus pancreatoblastoma, establishing that these tumors are genomically distinct from pancreatic ductal adenocarcinoma (no [KRAS](../genes/KRAS.md) mutations), carry substantial chromosomal instability and mutation burden, and that over one-third harbor potentially targetable alterations in the Fanconi anemia/DNA-damage-response pathway or in BRAF/JAK1.

## Composition

- **Total samples:** 23 fresh-frozen, surgically resected tumors with matched normals
  - 17 pure acinar cell carcinomas ([PAAC](../cancer_types/PAAC.md))
  - 3 mixed acinar–ductal carcinomas ([PAAC](../cancer_types/PAAC.md))
  - 1 mixed acinar–neuroendocrine carcinoma ([PAAC](../cancer_types/PAAC.md))
  - 2 pancreatoblastomas ([PB](../cancer_types/PB.md))
- 16 men (70%), 7 women (30%); average age at resection 61 years; majority stage 1–2
- All samples macrodissected to >70% neoplastic cellularity
- Reference genome: hg18 (exome alignment); targeted prevalence calls on hg19

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md): Agilent SureSelect paired-end v4.0 capture + Illumina HiSeq; reads aligned to hg18 via Eland/CASAVA 1.6; mean depth 131×; 91% of targeted bases ≥10×
- [FISH](../methods/fish.md): proximal/distal probes against chromosomes 11, 15, and 22 on FFPE sections
- [MSI testing (pentaplex PCR)](../methods/msi-pcr-pentaplex.md): Promega MSI Analysis System (BAT-25, BAT-26, NR-21, NR-24, MONO-27) plus additional markers for outlier samples
- [Quantitative methylation-specific PCR (qMSP)](../methods/qmsp.md): after EZ bisulfite conversion; U/M primers for [BRCA1](../genes/BRCA1.md) and [MLH1](../genes/MLH1.md) promoters

## Papers using this cohort

- [PMID:24293293](../papers/24293293.md) — Jiao et al., J Pathol 2014: first WES of pancreatic acinar cell carcinomas and pancreatoblastomas

## Notable findings derived from this cohort

- 2,745 somatic mutations across 23 tumors (mean 119 non-synonymous per tumor; 64 excluding three outliers, range 12–189); mutation burden exceeds pancreatic ductal adenocarcinoma [PMID:24293293](../papers/24293293.md)
- Two tumors classified as MSI-H by pentaplex (ACINAR01: 701 non-synonymous; ACINAR03: 404); one additional MSI-Low case identified with extended markers [PMID:24293293](../papers/24293293.md)
- Fractional allelic loss (FAL) mean 0.27 (range 0–0.89), substantially higher than pancreatic ductal adenocarcinoma (mean 0.15); LOH of 11p in 52%, 17p in 39%, 18q in 57% [PMID:24293293](../papers/24293293.md)
- [KRAS](../genes/KRAS.md) was completely absent from all 23 tumors, confirming genomic distinction from PDAC [PMID:24293293](../papers/24293293.md)
- Most frequently mutated genes: [SMAD4](../genes/SMAD4.md) (26%), [JAK1](../genes/JAK1.md) (17%), [BRAF](../genes/BRAF.md) (13%), [RB1](../genes/RB1.md) (13%), [TP53](../genes/TP53.md) (13%); no single gene mutated in >30% of cases [PMID:24293293](../papers/24293293.md)
- >1/3 of carcinomas harbored potentially targetable alterations in Fanconi anemia/DDR pathway ([BRCA2](../genes/BRCA2.md), [PALB2](../genes/PALB2.md), [ATM](../genes/ATM.md), [BAP1](../genes/BAP1.md)) or in [BRAF](../genes/BRAF.md)/[JAK1](../genes/JAK1.md) [PMID:24293293](../papers/24293293.md)

## Sources

- [PMID:24293293](../papers/24293293.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
