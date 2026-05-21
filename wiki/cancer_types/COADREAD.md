---
name: Colorectal Adenocarcinoma
oncotree_code: COADREAD
main_type: Colorectal Cancer
parent: BOWEL
tags: []
processed_by: crosslinker
processed_at: 2026-05-21
mainType: Colorectal Cancer
---

# Colorectal Adenocarcinoma (COADREAD)

## Overview

OncoTree parent for colon adenocarcinoma ([COAD](COAD.md)) and rectal
adenocarcinoma. No paper in the current corpus targets COADREAD directly;
this stub exists so child pages can resolve their `parent:` link.

## Cohorts in the corpus

- [coadread_tcga](../datasets/coadread_tcga.md) — TCGA colorectal adenocarcinoma cohort.
- [msk_chord_2024](../datasets/msk_chord_2024.md) — 5,543 colorectal cancer patients at MSK in the MSK-CHORD clinicogenomic harmonized real-world dataset [PMID:39506116](../papers/39506116.md).

## Recurrent alterations

- Included in pan-cancer MSK-IMPACT pathway and metastasis analyses; [RB1](../genes/RB1.md) oncogenic alterations enriched in brain and liver metastases in the pan-cancer cohort [PMID:39506116](../papers/39506116.md).
- Heterogeneous acquired resistance to combined KRASG12C + [EGFR](../genes/EGFR.md) inhibition in KRASG12C-mutant colorectal cancer involves KRASG12C amplification (>20 copies) as a recurrent mechanism correlating with tumor markers and oncogene-induced senescence, with emergent alterations spanning RAS mutations (58.3%), RTK activation (75%), and MAPK pathway changes (58.3%) across 12 patients [PMID:36355783](../papers/36355783.md)
- [FBXO7](../genes/FBXO7.md) shallow deletions (heterozygous copy number loss) occur in 32.5% (169/526) of colorectal cancers (TCGA Pan-Cancer Atlas, n=526), associate with increased chromosome instability (aneuploidy score, tumor break load; q<0.0001), and correlate with significantly worse overall, progression-free, and disease-specific survival; [CHEK1](../genes/CHEK1.md) inhibition via Prexasertib shows synthetic lethality in FBXO7-deficient colonic cells (EC50 5.83 nM vs 9.03 nM in controls) [PMID:36334560](../papers/36334560.md)
- WES and WGS of 276 colorectal carcinomas (TCGA) identified 24 significantly mutated genes including [APC](../genes/APC.md) (81%), [TP53](../genes/TP53.md) (60%), [KRAS](../genes/KRAS.md) (43%), [PIK3CA](../genes/PIK3CA.md) (18%), [ARID1A](../genes/ARID1A.md), [SOX9](../genes/SOX9.md), and [AMER1](../genes/AMER1.md); 16% of tumors were hypermutated; [ERBB2](../genes/ERBB2.md) amplification (4%) identified as potentially targetable with [trastuzumab](../drugs/trastuzumab.md) [PMID:22810696](../papers/22810696.md)
- 74-tumor WES cohort (Genentech) characterised colorectal adenocarcinoma genomic landscape; RSPO2/RSPO3 fusions mutually exclusive with APC loss establish Wnt pathway as universal driver [PMID:22895193](../papers/22895193.md)
- Targeted NGS (MSK-IMPACT, 230 genes) of 69 matched primary/metastasis/normal trios from microsatellite-stable colorectal cancer showed 100% concordance for [KRAS](../genes/KRAS.md), [NRAS](../genes/NRAS.md), and [BRAF](../genes/BRAF.md) mutations and 93% overall concordance for recurrent driver alterations between primary and metastatic sites. [PMID:25164765](../papers/25164765.md)
- WES of 619 CRC tumour/normal pairs from NHS and HPFS cohorts ([coadread_dfci_2016](../datasets/coadread_dfci_2016.md)) identified 90 significantly mutated genes (73 novel); neoantigen load correlated with TILs (Spearman rho=0.36, p=2e-19) and improved CRC-specific survival (multivariate HR=0.57, p=0.03); HLA class I somatic mutations in 11% of cases were enriched in TIL-rich tumours, implicating antigen-presentation escape [PMID:27149842](../papers/27149842.md)
- Prospective MSK-IMPACT sequencing of 1,134 colorectal adenocarcinomas (979 metastatic + 120 early-stage patients) identified 47 recurrently mutated genes; WNT pathway alteration reached 96% when intronic APC and large [CTNNB1](../genes/CTNNB1.md) exon-3 deletions were included; right-sided MSS mCRC had shorter [OS](../cancer_types/OS.md) (5-year 45% vs 67%, p<0.001) and distinct oncogenic enrichment versus left-sided [PMID:29316426](../papers/29316426.md)
- MSI-high tumors in COADREAD over-express immune effectors [GZMA](../genes/GZMA.md), [PRF1](../genes/PRF1.md), [GZMK](../genes/GZMK.md), [GZMH](../genes/GZMH.md) (Kolmogorov-Smirnov P<0.01); TP53 and KRAS are mutually exclusive in COAD/READ but co-occur in [PAAD](../cancer_types/PAAD.md) [PMID:29625049](../papers/29625049.md)
- WGS pan-cancer reanalysis: 19% of colorectal tumors carry a mutation in ≥1 of 11 recurrent CTCF-binding-site (CBS) hotspots — the second-most-mutated functional element in GI cancers after TP53 (50% of GC); CBS hotspot mutations enriched in CIN-subtype tumors [PMID:29670109](../papers/29670109.md)
- Rectal cancer tumoroid biorepository (65 lines from 41 patients) confirmed APC, TP53, KRAS, [FBXW7](../genes/FBXW7.md) as top drivers in both tumoroids and 287-patient MSK cohort; 62% of tumoroids RAS-mutant; ex vivo 5-FU/FOLFOX AUC correlated with patient PFS (Spearman r=0.86, p=0.024) [PMID:31591597](../papers/31591597.md).
- In PCAWG, colorectal adenocarcinoma showed point mutation dominance over SVs (mean 7.4 ± 7.0 point mutations vs 2.4 ± 1.4 SVs, P = 4×10⁻¹⁰); [TP53](../genes/TP53.md) associated with chromothripsis (colorectal OR=25) [PMID:32025007](../papers/32025007.md).
- Mondaca et al. profiled 430 MSS unresectable metastatic [COADREAD](../cancer_types/COADREAD.md) patients (colon and rectal primaries) by MSK-IMPACT; APC mutation site (N- vs C-terminal at aa 1400) was independently prognostic for OS and PFS, while DDR pathway alterations were not associated with survival or oxaliplatin-chemotherapy response in this MSS cohort [PMID:32730818](../papers/32730818.md).
- [CGREF1](../genes/CGREF1.md) was overexpressed in 61.25% (49/80) of CRC tissues by IHC across a tissue microarray cohort; TCGA TIMER 2.0 / GEPIA2 analyses confirmed significant upregulation in both [COAD](../cancer_types/COAD.md) and [READ](../cancer_types/READ.md) subtypes; CGREF1 promoted liver metastasis via F-actin remodeling in orthotopic mouse models without affecting primary tumor growth [PMID:32888432](../papers/32888432.md).
- MSK-MET pan-cancer cohort (25,775 patients, 50 tumor types, MSK-IMPACT) characterizes primary vs. metastatic genomic differences; COADREAD is among tumor types analyzed for [FGA](../genes/FGA.md), TMB, WGD, and driver-alteration frequency shifts between primary and metastatic specimens [PMID:35120664](../papers/35120664.md)
- ARGO Nigerian colorectal cohort (380 patients): Nigerian patients younger (median 55.8 vs. 60.0y), more likely rectal (50.8% vs. 33.7%) and stage IV (53.8% vs. 36.2%); MSI-H rate 28.1% vs. 14.2% TCGA; MSS tumors had depleted APC and WNT signaling but enriched RAS-pathway [PMID:34819518](../papers/34819518.md)
- COLON MAP / HTAN multi-omic polyp atlas (142,065 cells, 62 participants): defines adenoma vs. serrated polyp cell-of-origin (stem vs. differentiated lineage); CRC molecular subtypes retain precursor transcriptomic signatures; MSI-H CRCs gain stemness on metaplastic background [PMID:34910928](../papers/34910928.md)
- MSK-IMPACT sequencing of 4,561 colorectal cancer patients identified 47 cases (1.03%) with dual RAS/BRAF V600E driver mutations; single-cell genotyping confirmed same-cell co-occurrence (14%–95% of tumor cells) in 4 cases [PMID:35235413](../papers/35235413.md)

## Therapeutic landscape

- NLP-augmented integrated survival-prediction models outperformed stage- or genomics-only models in colorectal cancer [PMID:39506116](../papers/39506116.md).

## Children

- [COAD](COAD.md) — Colon Adenocarcinoma

## Sources

- [PMID:39506116](../papers/39506116.md)

- [PMID:36355783](../papers/36355783.md)
- [PMID:36334560](../papers/36334560.md)

- [PMID:22810696](../papers/22810696.md)

- [PMID:22895193](../papers/22895193.md)

- [PMID:25164765](../papers/25164765.md)

- [PMID:27149842](../papers/27149842.md)

- [PMID:29316426](../papers/29316426.md)

- [PMID:29625049](../papers/29625049.md)

- [PMID:29670109](../papers/29670109.md)

- [PMID:31591597](../papers/31591597.md)

- [PMID:32025007](../papers/32025007.md)

- [PMID:32730818](../papers/32730818.md)

- [PMID:32888432](../papers/32888432.md)


- [PMID:35120664](../papers/35120664.md)

- [PMID:34819518](../papers/34819518.md)

- [PMID:34910928](../papers/34910928.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35235413](../papers/35235413.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
