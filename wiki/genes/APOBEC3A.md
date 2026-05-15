---
symbol: APOBEC3A
aliases: []
cancer_types:
  - BLCA
tags:
  - mutational-signature
  - cytidine-deaminase
  - apobec
  - chemotherapy-resistance
processed_by: wiki-cli
processed_at: 2026-05-15
---

# APOBEC3A

## Overview

APOBEC3A (Apolipoprotein B mRNA Editing Catalytic Polypeptide-Like 3A) is a member of the APOBEC family of cytidine deaminases. It converts cytosine to uracil in single-stranded DNA, generating C-to-T (and C-to-G) mutations predominantly at TC motifs (YTCA context). APOBEC3A is recognized as a major source of mutational signatures 2 and 13 (COSMIC) in multiple cancer types, including urothelial carcinoma (UC), breast cancer, and lung adenocarcinoma. Its expression and enzymatic activity can be upregulated by DNA damage and viral infection, and it has been implicated as an endogenous mutagen that shapes cancer evolution — particularly under genotoxic stress such as platinum-based chemotherapy.

## Alterations observed in the corpus

- APOBEC3A YTCA mutagenesis significantly enriched in post-chemotherapy urothelial carcinoma tumors (P=1×10⁻⁵, Fisher's exact test); APOBEC3A identified as the dominant cytidine deaminase shaping the post-chemotherapy UC mutational landscape, with clonal APOBEC-induced mutations rising after treatment [PMID:27749842](../papers/27749842.md).
- APOBEC-induced mutations enriched in ABC-transporter (OR=2.7, P=0.038) and homologous-recombination DNA-repair (OR=3.8, P=0.033) pathways in post-chemotherapy tumors [PMID:27749842](../papers/27749842.md).
- APOBEC3A mutational signature modestly enriched at the NOL10 locus in CPGEA and TCGA PRAD vs. genome-wide background, suggesting ectopic APOBEC mutagenesis as a complementary somatic contributor to NOL10 deregulation in prostate cancer [PMID:28927585](../papers/28927585.md)

## Cancer types (linked)

- [BLCA](../cancer_types/BLCA.md): Dominant post-chemotherapy mutational editor in a 32-patient WES cohort (16 matched pre/post-chemotherapy pairs); APOBEC3A YTCA-context mutagenesis significantly higher in post-treatment tumors vs pre-treatment [PMID:27749842](../papers/27749842.md).

## Co-occurrence and mutual exclusivity

- Co-occurs with [APOBEC3B](../genes/APOBEC3B.md) activity in post-chemotherapy UC; both YTCA (APOBEC3A) and RTCA ([APOBEC3B](../genes/APOBEC3B.md)) context mutagenesis enriched after platinum treatment, while APOBEC3G CCC-motif mutagenesis decreased [PMID:27749842](../papers/27749842.md).

## Therapeutic relevance

- Platinum-based chemotherapy (cisplatin/gemcitabine) appears to amplify APOBEC3A-driven mutagenesis, hypothesized to occur via increased availability of single-stranded DNA during double-strand-break repair of platin-DNA adducts. This iatrogenic mutational editing may contribute to chemotherapy resistance evolution [PMID:27749842](../papers/27749842.md).
- No direct APOBEC3A inhibitor in clinical use; mechanistic link between APOBEC3A activity and resistance pathways (HR repair, ABC transporters) may represent indirect therapeutic opportunities.

## Open questions

- The mechanism linking platinum-based chemotherapy to APOBEC3A/3B mutagenesis (proposed: increased ssDNA from HR repair of platin-DNA adducts) is hypothesized rather than experimentally demonstrated [PMID:27749842](../papers/27749842.md).
- Whether APOBEC3A-driven mutations in post-chemotherapy tumors are functionally driver events or passenger bystanders remains unresolved.

## Sources

- [PMID:27749842](../papers/27749842.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:28927585](../papers/28927585.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
