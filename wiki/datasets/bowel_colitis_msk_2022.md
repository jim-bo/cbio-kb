---
name: Colitis-Associated Cancer MSK 2022
studyId: bowel_colitis_msk_2022
institution: Memorial Sloan Kettering Cancer Center
size: 174
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - IMPACT468
  - whole-exome-sequencing
  - rna-sequencing
panels:
  - IMPACT468
tags:
  - colitis-associated-cancer
  - inflammatory-bowel-disease
  - colon-cancer
  - wnt-signaling
processed_by: crosslinker
processed_at: 2026-05-03
---

# Colitis-Associated Cancer MSK 2022

## Overview

The bowel_colitis_msk_2022 dataset is the largest annotated clinical and genomic series of colitis-associated cancers (CAC) assembled to date, comprising 174 patients with inflammatory bowel disease (IBD)-associated bowel cancers at Memorial Sloan Kettering Cancer Center (MSKCC). Additionally, 29 synchronous or isolated dysplasia samples were sequenced. The dataset was reported by Chatila et al. (Nature Communications, 2023) [PMID:36611031](../papers/36611031.md) and establishes the molecular landscape distinguishing CAC from sporadic colorectal cancer ([[[COAD](../cancer_types/COAD.md)]]).

## Composition

- **174 patients** with colitis-associated cancers ([[COAD]]); 144 in the clinical cohort, 161 in the genomic cohort, 166 CAC tumors sequenced. [PMID:36611031](../papers/36611031.md)
- IBD subtype: 56% ulcerative colitis (n = 93), 44% Crohn's disease (n = 73). 84.9% had ≥10 years of IBD at CAC diagnosis. [PMID:36611031](../papers/36611031.md)
- Primary tumor sites: small intestine 10.3%, right colon 27.1%, left colon 29.5%, rectum 31.3%, fistula tract 1.8%. [PMID:36611031](../papers/36611031.md)
- 29 dysplasia samples (synchronous or isolated) included for genomic analysis; 9 profiled by MSK-IMPACT, 20 by whole-exome sequencing (WES). [PMID:36611031](../papers/36611031.md)
- Germline panel data available for 73/161 patients via MSK-IMPACT germline pipeline. [PMID:36611031](../papers/36611031.md)
- **Cancer types:** [[COAD]] (colitis-associated colorectal cancer). [PMID:36611031](../papers/36611031.md)
- **Key clinical fields:** IBD subtype (UC vs. CD), years of IBD at diagnosis, tumor site, colonoscopy history, IBD disease activity, overall survival, bone/pelvic metastases. [PMID:36611031](../papers/36611031.md)

## Assays / panels (linked)

- [[[IMPACT468](../methods/IMPACT468.md)]] targeted exon sequencing on 166 CAC + 9 dysplasia samples; FoundationOne used in some cases. [PMID:36611031](../papers/36611031.md)
- [[[whole-exome-sequencing](../methods/whole-exome-sequencing.md)]] at 150× depth on 13 CAC + 20 dysplasia samples paired with adjacent normal mucosa. [PMID:36611031](../papers/36611031.md)
- [[[rna-sequencing](../methods/rna-sequencing.md)]] on a subset (5 CAC, 6 sporadic CRC) for Wnt ssGSEA scoring; also performed on PDX models. [PMID:36611031](../papers/36611031.md)
- Copy-number analysis by [[[facets](../methods/facets.md)]] and [[[cnapp](../methods/cnapp.md)]]; functional models: AOM/DSS mouse model, patient-derived organoids (PDOs), and patient-derived xenografts (PDXs). [PMID:36611031](../papers/36611031.md)

## Papers using this cohort

- [PMID:36611031](../papers/36611031.md) — Chatila et al. "Integrated clinical and genomic analysis identifies driver events and molecular evolution of colitis-associated cancers." Nature Communications (2023).

## Notable findings derived from this cohort

- [[[TP53](../genes/TP53.md)]] is altered in 90% of CAC and ~50% of dysplasia samples; alterations are predominantly clonal and frequently arise via convergent evolution across independent multifocal lesions. [PMID:36611031](../papers/36611031.md)
- [[[APC](../genes/APC.md)]] is mutated in only 20% of CAC (vs. dominant frequency in sporadic CRC), and Wnt pathway alterations are globally infrequent; CAC organoids grow without exogenous Wnt supplementation, indicating transcriptional rewiring away from Wnt. [PMID:36611031](../papers/36611031.md)
- Other recurrent drivers: [[[KRAS](../genes/KRAS.md)]] 31%, [[[MYC](../genes/MYC.md)]] 20% (focal amplifications enriched vs. sporadic CRC), [[[SMAD4](../genes/SMAD4.md)]] 13%, [[[PIK3CA](../genes/PIK3CA.md)]] and [[[IDH1](../genes/IDH1.md)]] enriched in Crohn's disease vs. UC. [PMID:36611031](../papers/36611031.md)
- Multiple primary or synchronous lesions arise as genetically independent events — no shared alterations detected across six patients with multifocal tumors — arguing against a genomic field defect. [PMID:36611031](../papers/36611031.md)
- Germline pathogenic alterations identified in 10/73 patients (14%): [[APC]] I1307K (3 cases, Ashkenazi Jewish low-penetrance variant), [[[PMS2](../genes/PMS2.md)]], [[[ATM](../genes/ATM.md)]], [[[RAD51B](../genes/RAD51B.md)]], [[[DICER1](../genes/DICER1.md)]], [[[FANCA](../genes/FANCA.md)]], [FANCC](../genes/FANCC.md). [PMID:36611031](../papers/36611031.md)
- [[IDH1]] R132 mutant CAC exhibited high global methylation and 2-HG production; selective IDH1 and [[[FGFR2](../genes/FGFR2.md)|FGFR]] inhibitors suppressed tumor growth in PDX models. [PMID:36611031](../papers/36611031.md)
- Bone and pelvic metastases are significantly enriched in CAC vs. sporadic CRC. [PMID:36611031](../papers/36611031.md)

## Sources

- Chatila WK et al. "Integrated clinical and genomic analysis identifies driver events and molecular evolution of colitis-associated cancers." Nature Communications (2023). [PMID:36611031](../papers/36611031.md)

*This page was processed by **crosslinker** on **2026-05-03**.*
