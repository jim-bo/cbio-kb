---
name: "JHU Intrahepatic Cholangiocarcinoma / Gallbladder Carcinoma WES 2013"
studyId: chol_jhu_2013
institution: "Johns Hopkins University / MSKCC / Mayo Clinic / Fundeni Clinical Institute / University Hospital Trust of Verona"
size: 80
reference_genome: hg18/hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - targeted-dna-seq
  - sanger-sequencing
panels: []
tags:
  - cholangiocarcinoma
  - gallbladder-carcinoma
  - chromatin-remodeling
  - swi-snf
  - idh-mutation
processed_by: crosslinker
processed_at: 2026-05-09
---

# JHU Intrahepatic Cholangiocarcinoma / Gallbladder Carcinoma WES 2013

## Overview

The chol_jhu_2013 cohort was assembled by Jiao, Pawlik, Wood and colleagues at Johns Hopkins University and collaborating institutions to define the mutational landscape of intrahepatic cholangiocarcinoma ([IHCH](../cancer_types/IHCH.md)) and gallbladder carcinoma ([GBC](../cancer_types/GBC.md)) by whole-exome sequencing. The study was the first large-scale genomic profiling effort in these biliary cancers and led to the discovery of recurrent inactivating mutations in the chromatin-remodeling genes [BAP1](../genes/BAP1.md), [ARID1A](../genes/ARID1A.md), and [PBRM1](../genes/PBRM1.md) as dominant drivers of IHCH, distinct from the TP53-dominated landscape of GBC.

## Composition

- **Total samples:** 80 (64 IHCH + 16 GBC across discovery and prevalence screens)
- **Discovery screen:** 32 [IHCH](../cancer_types/IHCH.md) + 9 [GBC](../cancer_types/GBC.md) (one GBC excluded — hypermutator), tumor + matched normal
- **Prevalence screen:** 32 additional [IHCH](../cancer_types/IHCH.md) + 8 additional [GBC](../cancer_types/GBC.md)
- **Key clinical fields:** primary surgical resection specimens; IRB-approved collections at Johns Hopkins, MSKCC, Mayo Clinic, Fundeni Clinical Institute (Romania), and University Hospital Trust of Verona (Italy)
- Reference genome: hg18 (exome discovery); hg19 (targeted prevalence screen)

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md): Agilent SureSelect Paired-End v2.0 Human Exome + Illumina HiSeq 2000; mean coverage 130×; >90% of targeted bases ≥10× (discovery screen)
- [Targeted DNA sequencing](../methods/targeted-dna-seq.md): custom Ion AmpliSeq panel (17 candidate driver genes) on Ion Torrent PGM 318 chip; mean depth 1,276×; 88.9% of target bases ≥100× (prevalence screen)
- [Sanger sequencing](../methods/sanger-sequencing.md): orthogonal validation of 50 mutations; 100% confirmed

## Papers using this cohort

- [PMID:24185509](../papers/24185509.md) — Jiao et al., Nature Genetics 2013: discovery of BAP1/ARID1A/PBRM1 as recurrent IHCH drivers

## Notable findings derived from this cohort

- [BAP1](../genes/BAP1.md) inactivating mutations in 13/64 (20%) IHCH; first report of BAP1 alteration in a gastrointestinal cancer [PMID:24185509](../papers/24185509.md)
- [ARID1A](../genes/ARID1A.md) mutated in 9/64 (14%) IHCH; [PBRM1](../genes/PBRM1.md) in 8/64 (13%) IHCH and 4/16 (25%) GBC; at least one SWI/SNF chromatin-remodeling gene altered in 41% of combined IHCH cohort [PMID:24185509](../papers/24185509.md)
- [IDH1](../genes/IDH1.md)/[IDH2](../genes/IDH2.md) hotspot mutations in 20% of IHCH; associated with significantly worse survival (3-year [OS](../cancer_types/OS.md) 33% vs 81%, log-rank P=0.0034; Cox HR 7.37 after stage/age/sex adjustment) [PMID:24185509](../papers/24185509.md)
- [FGFR2](../genes/FGFR2.md) point mutations in 4/32 (13%) discovery-screen IHCH, complementing known [FGFR2](../genes/FGFR2.md) gene fusions in cholangiocarcinoma [PMID:24185509](../papers/24185509.md)
- [TP53](../genes/TP53.md) was the dominant GBC alteration (5/8, 63% discovery screen; 44% combined GBC cohort), supporting genomically distinct biology between IHCH and GBC [PMID:24185509](../papers/24185509.md)

## Sources

- [PMID:24185509](../papers/24185509.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
