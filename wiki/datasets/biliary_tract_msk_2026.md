---
name: Hepatobiliary Cancer (MSK, 2026)
studyId: biliary_tract_msk_2026
institution: Memorial Sloan Kettering Cancer Center
size: 1291
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
panels:
  - IMPACT341
  - IMPACT410
  - IMPACT468
  - IMPACT505
tags:
  - biliary-tract-cancer
  - cholangiocarcinoma
  - gallbladder-cancer
  - msk-impact
  - actionability
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# Hepatobiliary Cancer (MSK, 2026)

## Overview

A prospective MSK clinical genomic profiling cohort (NCT01775072; MSK IRB 12-245) of 1,254 biliary tract cancer patients (1,285 tumor/plasma samples) sequenced with MSK-IMPACT between April 2014 and September 2022, used to track growth in clinically actionable alterations over time via serial OncoKB annotation (v1.8 vs v4.7). cBioPortal study record: 1,291 samples, hg19. [PMID:42360806](../papers/42360806.md)

## Composition

- Cancer types: [biliary tract cancer](../cancer_types/BILIARY_TRACT.md), comprising [intrahepatic cholangiocarcinoma (IHCH)](../cancer_types/IHCH.md) 767 (61.2%), [extrahepatic cholangiocarcinoma (EHCH)](../cancer_types/EHCH.md) 210 (16.8%) and [gallbladder cancer (GBC)](../cancer_types/GBC.md) 277 (22.1%); IHCH and EHCH both fall under [cholangiocarcinoma](../cancer_types/CHOL.md). [PMID:42360806](../papers/42360806.md)
- Demographics: median age 65 (range 21–89); 52% female / 48% male; 74.2% self-reported Caucasian, 10.2% Asian, 6.2% African American; 879 primary (70%) vs 375 metastatic (30%) samples sequenced. [PMID:42360806](../papers/42360806.md)
- Analysis subsets: potentially actionable cohort (OncoKB level 1/2/3A, or selected level 3B) n=514; clinically eligible cohort with outcome data n=413, of whom 176 (43%) received matched targeted therapy. [PMID:42360806](../papers/42360806.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) tumor/matched-normal hybridization-capture NGS across four panel versions: [IMPACT341](../methods/IMPACT341.md) (n=55), [IMPACT410](../methods/IMPACT410.md) (n=200), [IMPACT468](../methods/IMPACT468.md) (n=663), [IMPACT505](../methods/IMPACT505.md) (n=336); a subset also had cfDNA profiling with [MSK-ACCESS](../methods/msk-access.md). [PMID:42360806](../papers/42360806.md)
- [OncoKB](../methods/oncokb.md) annotation compared across the March 2017 (v1.8) and July 2023 (v4.7) releases. [PMID:42360806](../papers/42360806.md)

## Papers using this cohort

- [PMID:42360806](../papers/42360806.md) — Cowzer et al., *Clinical Cancer Research* (2026): source publication for this cohort.

## Notable findings derived from this cohort

## Sources

- cBioPortal study ID: biliary_tract_msk_2026 (name, institution, size, reference_genome from `schema/ontology/studies.json`).

*This page was processed by **entity-page-writer** on **2026-09-10**.*
