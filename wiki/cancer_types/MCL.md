---
name: Mantle Cell Lymphoma
oncotree_code: MCL
main_type: Mature B-Cell Neoplasms
parent: MBN
tags:
  - lymphoma
  - b-cell
  - ccnd1
  - atm
  - notch
processed_by: crosslinker
processed_at: 2026-05-09
---

# Mantle Cell Lymphoma (MCL)

## Overview

Mantle Cell Lymphoma (MCL) is a mature B-cell neoplasm within the Lymphoid tissue branch of OncoTree, sitting under the Mature B-Cell Neoplasms (MBN) parent node. It is defined by overexpression of cyclin D1 driven by the t(11;14)(q13;q32) translocation juxtaposing [CCND1](../genes/CCND1.md) with the IGH locus. MCL is biologically heterogeneous: SOX11-positive tumors with unmutated IGHV present an aggressive clinical course, while SOX11-negative / IGHV-mutated cases are typically more indolent.

## Cohorts in the corpus

- [mcl_idibips_2013](../datasets/mcl_idibips_2013.md) — WGS (n=4), WES (n=29 primaries + 6 cell lines), and targeted validation in 172 MCL patients; SNP 6.0 arrays and gene-expression profiling (HU133+2.0); deposited as EGA EGAS00001000510 and GEO GSE46969/GSE36000 [PMID:24145436](../papers/24145436.md).

## Recurrent alterations

- WES/WGS of 33 MCL tumors identified 25 significantly mutated genes; all 29 primary tumors harbored at least one; novel drivers include [NSD2](../genes/NSD2.md) (WHSC1), [KMT2D](../genes/KMT2D.md) (MLL2), [MEF2B](../genes/MEF2B.md) (chromatin modifiers), [BIRC3](../genes/BIRC3.md), [TLR2](../genes/TLR2.md), and [NOTCH2](../genes/NOTCH2.md) alongside known drivers [ATM](../genes/ATM.md), CCND1, and [TP53](../genes/TP53.md) [PMID:24145436](../papers/24145436.md).
- [ATM](../genes/ATM.md) — truncating/functional-domain mutations in 41% of WES cases; significantly enriched in SOX11-positive MCL (55% vs 0% in SOX11-negative); often biallelic via 11q deletion; an early/clonal event [PMID:24145436](../papers/24145436.md).
- [CCND1](../genes/CCND1.md) — exon-1 mutations in 35% of WES cases; enriched in SOX11-negative (86% vs 18%) and IGHV-mutated (58% vs 19%) tumors, consistent with germinal-center acquisition [PMID:24145436](../papers/24145436.md).
- [TP53](../genes/TP53.md) — mutations in 22% of the total cohort (42/192); associated with 17p allelic loss; independent [OS](../cancer_types/OS.md) risk factor (HR 2.4; 95% CI 1.4–4.2; P=0.003) [PMID:24145436](../papers/24145436.md).
- [NSD2](../genes/NSD2.md) (WHSC1/MMSET) — recurrent missense p.E1099K and p.T1150A in 10% (13/130) of MCL; restricted to SOX11-positive tumors; transcriptionally phenocopies t(4;14) plasma-cell myeloma [PMID:24145436](../papers/24145436.md).
- [NOTCH1](../genes/NOTCH1.md) / [NOTCH2](../genes/NOTCH2.md) — PEST-truncating mutations in 4.6% and 5.2% of MCL respectively; mutually exclusive in 15/16 mutated cases; combined NOTCH1/2 mutations mark an aggressive subset (3-y OS 24% vs 63%, P=3.4×10⁻⁴); NOTCH2 mutation is an independent OS risk factor (HR 3.5, P=0.017) [PMID:24145436](../papers/24145436.md).
- [BIRC3](../genes/BIRC3.md) — inactivating mutations in 6.4% (11/173); tightly co-occurs with 11q22.2 deletion; can be acquired post-treatment [PMID:24145436](../papers/24145436.md).
- [CDKN2A](../genes/CDKN2A.md) — only gene with recurrent homozygous deletions in MCL; no somatic point mutations detected [PMID:24145436](../papers/24145436.md).
- Mutational burden stratifies clinical course: indolent MCL (no treatment required) carries significantly fewer protein-coding mutations (mean 11 vs 25, P=3.4×10⁻⁵) and fewer CNAs (mean 2 vs 12, P=0.001) than treatment-requiring cases [PMID:24145436](../papers/24145436.md).

## Subtypes

- **SOX11-positive / IGHV-unmutated MCL** — aggressive subtype; enriched for ATM, NSD2, KMT2D, MEF2B mutations; higher CNA burden; typically treatment-requiring.
- **SOX11-negative / IGHV-mutated MCL** — indolent subtype; enriched for CCND1 exon-1 and TLR2 mutations; lower CNA burden; 5 patients in the WES cohort required no treatment over median 55-month follow-up [PMID:24145436](../papers/24145436.md).
- **Blastoid/pleomorphic MCL** — aggressive morphology enriched for NOTCH1/2 mutations; dismal 3-year OS of 0% for NOTCH2-mutant cases [PMID:24145436](../papers/24145436.md).

## Therapeutic landscape

- NOTCH pathway inhibition (e.g., γ-secretase inhibitors) is proposed as a strategy for the NOTCH1/2-mutated aggressive subset [PMID:24145436](../papers/24145436.md).
- Chemotherapy-driven clonal selection leads to emergence of new dominant subclones at relapse (including post-treatment BIRC3 mutation acquisition), supporting relapse-time genomic profiling to guide targeted therapy [PMID:24145436](../papers/24145436.md).

## Sources

- [PMID:24145436](../papers/24145436.md) — Beà et al. WGS/WES of 33 MCL tumors with targeted validation in 172 patients; identified 25 significantly mutated genes and characterized clonal evolution.

*This page was processed by **crosslinker** on **2026-05-09**.*
