---
name: Neurofibroma
oncotree_code: NFIB
main_type: Nerve Sheath Tumor
parent: NST
tags: []
canonical_source: oncotree
unverified: false
processed_by: crosslinker
processed_at: 2026-05-16
---

# Neurofibroma (NFIB)

## Overview

Neurofibroma (OncoTree: [NFIB](../genes/NFIB.md)) is a benign nerve sheath tumor arising from the peripheral nervous system, classified under the Nerve Sheath Tumor main type with parent node NST. It encompasses several subtypes — cutaneous neurofibroma (cNF), superficial diffuse infiltrating neurofibroma, and plexiform neurofibroma (pNF) — the last of which carries a risk of malignant transformation to malignant peripheral nerve sheath tumor ([MPNST](MPNST.md)). The majority of cases arise in the context of neurofibromatosis type 1 ([NF1](../genes/NF1.md)), driven by germline and somatic biallelic inactivation of [NF1](../genes/NF1.md).

## Cohorts in the corpus

- [nst_nfosi_ntap](../datasets/nst_nfosi_ntap.md) — JHU NF1 biospecimen repository (23 NF1 patients, 55 tumor samples total); includes cutaneous neurofibromas, plexiform neurofibromas, ANNUBP, and [MPNST](../cancer_types/MPNST.md) with matched germline + somatic WES and RNA-seq [PMID:32561749](../papers/32561749.md).

## Recurrent alterations

- [NF1](../genes/NF1.md) — germline driver in all NF1-associated neurofibromas; somatic biallelic inactivation is the canonical second hit; copy ratio at the NF1 locus preserved faithfully in derived cell lines and PDX models [PMID:32561749](../papers/32561749.md).
- [CDKN2A](../genes/CDKN2A.md) — commonly mutated gene panel tracked across histologies; loss enriched in malignant (MPNST) relative to benign neurofibroma contexts [PMID:32561749](../papers/32561749.md).
- [EED](../genes/EED.md) / [SUZ12](../genes/SUZ12.md) — PRC2-complex tumor suppressors; in the JHU first-release cohort, mutations were absent from benign and intermediate neurofibromas and restricted to the single MPNST sample, consistent with PRC2 inactivation being a malignant-transformation marker rather than a neurofibroma-intrinsic event [PMID:32561749](../papers/32561749.md).

## Subtypes

- **Cutaneous neurofibroma (cNF)** — superficial, dermal origin; typically non-progressive.
- **Plexiform neurofibroma (pNF)** — deeper, infiltrating; arises from peripheral nerve plexus; carries ~10–15% lifetime risk of malignant transformation to MPNST in NF1 patients.
- **Atypical neurofibromatous neoplasm of uncertain biologic potential (ANNUBP)** — intermediate histology between pNF and MPNST; characterized in the JHU biospecimen corpus alongside malignant cases.

## Therapeutic landscape

- No targeted therapies specific to neurofibroma are documented in the current corpus. Surgical resection remains standard for symptomatic lesions. The JHU NF1 biospecimen repository ([nst_nfosi_ntap](../datasets/nst_nfosi_ntap.md)) was released specifically to enable downstream preclinical drug studies, particularly for plexiform neurofibroma where surgery is the only established option [PMID:32561749](../papers/32561749.md).

## Sources

- [PMID:32561749](../papers/32561749.md) — Pollard et al. JHU NF1 biospecimen repository.

*This page was processed by **crosslinker** on **2026-05-16**.*
