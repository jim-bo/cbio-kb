---
name: leuprolide
targets: [LHCGR]
drug_class: GnRH agonist / androgen-deprivation therapy
canonical_source: corpus
unverified: true
tags:
  - hormonal-therapy
  - adt
  - prostate-cancer
  - real-world-data
processed_by: wiki-cli
processed_at: 2026-05-16
---

# leuprolide

## Overview

Leuprolide (Lupron) is a synthetic GnRH (gonadotropin-releasing hormone) agonist that, on continuous administration, suppresses LH and FSH secretion from the pituitary, resulting in castrate levels of testosterone. It is a cornerstone of androgen-deprivation therapy (ADT) for prostate cancer and is also used in other hormone-sensitive conditions (endometriosis, precocious puberty).

## Evidence in the corpus

- Leuprolide was identified as one of the prior treatments extracted by the MSK-CHORD NLP pipeline from clinical notes across 3,211 prostate cancer ([PRAD](../cancer_types/PRAD.md)) patients in the MSK-CHORD dataset. It was captured as part of the treatment-annotation component used to define prior systemic therapy exposure for the multimodal survival modeling and post-treatment genomic enrichment analyses [PMID:39506116](../papers/39506116.md).
- OncoMark hallmark-survival analysis (TCGA logistic regression) associated leuprolide with the Evading Replicative Immortality (ERI) hallmark for overall survival, alongside anastrozole, nominating ERI-high tumors as candidate responders [PMID:35121966](../papers/35121966.md)

## Resistance mechanisms

- Not directly characterized in the corpus; androgen-receptor ([AR](../genes/AR.md)) alterations and [TP53](../genes/TP53.md) mutations are enriched in prostate cancer patients with prior systemic therapy (including ADT) in MSK-CHORD [PMID:39506116](../papers/39506116.md).

## Cancer types (linked)

- [PRAD](../cancer_types/PRAD.md) — prostate adenocarcinoma (ADT backbone; prior therapy annotation in MSK-CHORD)

## Sources

- [PMID:39506116](../papers/39506116.md) — Jee et al. 2024, *Nature*. MSK-CHORD real-world data integration; leuprolide as NLP-extracted prior treatment in the prostate cancer cohort.

*This page was processed by **crosslinker** on **2026-04-30**.*
- [PMID:35121966](../papers/35121966.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
