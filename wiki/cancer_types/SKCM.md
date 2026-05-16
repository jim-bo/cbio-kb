---
name: Cutaneous Melanoma
oncotree_code: SKCM
main_type: Melanoma
parent: MEL
tags:
  - melanoma
  - skin-cancer
  - UV-mutagenesis
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# Cutaneous Melanoma (SKCM)

## Overview

SKCM is the OncoTree code for cutaneous (skin) melanoma. SKCM is a high-TMB malignancy driven primarily by UV-induced mutagenesis, with characteristic C>T transitions at dipyrimidines (SBS7 signature) and frequent activating mutations in [BRAF](../genes/BRAF.md), [NRAS](../genes/NRAS.md), and [NF1](../genes/NF1.md).

## Cohorts in the corpus

- [normal_skin_melanocytes_2024](../datasets/normal_skin_melanocytes_2024.md) — single-cell genotyping atlas of phenotypically normal skin melanocytes adjacent to a SKCM patient, profiling LowMut neural-crest-like vs HighMut UV-driven cell-of-origin programs. [PMID:39975212](../papers/39975212.md)

## Recurrent alterations

- [BRAF](../genes/BRAF.md), [NRAS](../genes/NRAS.md), [NF1](../genes/NF1.md), [TP53](../genes/TP53.md), [PTEN](../genes/PTEN.md), [CDKN2A](../genes/CDKN2A.md), [TERT](../genes/TERT.md) promoter mutations are canonical SKCM drivers.
- The [PMID:39975212](../papers/39975212.md) atlas characterizes precursor melanocyte transcriptomic states ([MITF](../genes/MITF.md), [MLANA](../genes/MLANA.md), [PMEL](../genes/PMEL.md), [TYRP1](../genes/TYRP1.md), [AXL](../genes/AXL.md)) that may seed SKCM cell-of-origin hypotheses.
- WGS of 25 cutaneous melanoma tumors identified [PREX2](../genes/PREX2.md) as a recurrently mutated gene and confirmed [KIT](../genes/KIT.md) and [BRAF](../genes/BRAF.md) alterations [PMID:22622578](../papers/22622578.md)
- WES of 121 cutaneous melanomas (Broad) identified [RAC1](../genes/RAC1.md) P29S (3.9%), [PPP6C](../genes/PPP6C.md) (9%), and [MAP2K1](../genes/MAP2K1.md) as novel recurrently mutated genes; 83% of tumors harbored [BRAF](../genes/BRAF.md) or [NRAS](../genes/NRAS.md) hotspot mutations (mutually exclusive, p=3e-14) [PMID:22817889](../papers/22817889.md)
- WES of 147 melanomas (Yale) found [RAC1](../genes/RAC1.md) P29S in 9.2% of sun-exposed cutaneous melanomas, [PPP6C](../genes/PPP6C.md) mutations in 12.4%, and [NF1](../genes/NF1.md) inactivation in 30% of BRAF/NRAS-WT tumors; [vemurafenib](../drugs/vemurafenib.md) and [dabrafenib](../drugs/dabrafenib.md) cited as established BRAF-targeted therapies [PMID:22842228](../papers/22842228.md)
- Whole-exome sequencing of 45 [BRAF](../genes/BRAF.md) V600 metastatic cutaneous melanoma patients treated with [vemurafenib](../drugs/vemurafenib.md) or [dabrafenib](../drugs/dabrafenib.md) identified resistance alterations in 51% of cases; MAPK-pathway alterations ([NRAS](../genes/NRAS.md), [BRAF](../genes/BRAF.md) amplification, [MAP2K1](../genes/MAP2K1.md), [MAP2K2](../genes/MAP2K2.md), [MITF](../genes/MITF.md), [NF1](../genes/NF1.md)) accounted for 44% of patients. Novel resistance genes [MAP2K2](../genes/MAP2K2.md) (MEK2; 4 mutations) and [MITF](../genes/MITF.md) amplification were discovered and experimentally validated. Pre-treatment [RAC1](../genes/RAC1.md) P29S was enriched in early-resistance patients (3/14 vs 0 responders; P=0.026). [PMID:24265153](../papers/24265153.md)
- Whole-exome sequencing of 64 metastatic SKCM patients treated with anti-CTLA-4 (ipilimumab/tremelimumab) showed high tumor mutational load was significantly associated with long-term clinical benefit (discovery P=0.01, validation P=0.009); a shared tetrapeptide neoepitope signature in responders predicted overall survival (P<0.001 log-rank in both cohorts) [PMID:25409260](../papers/25409260.md).
- TCGA integrative multi-platform profiling of 333 primary/metastatic SKCM (dataset: [skcm_tcga_pub_2015](../datasets/skcm_tcga_pub_2015.md)) defined four genomic subtypes: BRAF-mutant (52%), RAS-mutant (28% [NRAS](../genes/NRAS.md)), NF1-mutant (14%), and Triple-WT (14%); mean 16.8 mut/Mb — highest of any TCGA type; transcriptomic Immune subclass (51%) associated with significantly improved survival in regional metastases (log-rank P=0.003); bivariate LScore + [LCK](../genes/LCK.md) model proposed as a clinical-grade prognostic tool (HR=5.5, P=7.9e-5) [PMID:26091043](../papers/26091043.md)
- Comprehensive genomic analysis of cutaneous melanoma revealed mutational landscape dominated by UV-signature mutations with recurrent alterations in [BRAF](../genes/BRAF.md), [NRAS](../genes/NRAS.md), and [NF1](../genes/NF1.md) [PMID:26359337](../papers/26359337.md)
- 38 pretreatment metastatic SKCM biopsies profiled by WES and RNA-seq to identify genomic and transcriptomic correlates of anti-PD-1 response; the IPRES mesenchymal/angiogenic transcriptional program defined innate resistance in 9/13 non-responders vs 1/15 responders, and BRCA2 LOF mutations were enriched in responders (28% vs 6%, Fisher P=0.002, OR=6.2) [PMID:26997480](../papers/26997480.md)
- Cutaneous melanoma (SKCM) used as comparator to acral melanoma (ACRM): SKCM harbours canonical UV-signature BRAF/NRAS/NF1 drivers and higher mutation burden, contrasting with ACRM's structural-variant dominance and UV-signature absence [PMID:28373299](../papers/28373299.md)
- Riaz et al. profiled paired pre- and on-therapy biopsies from 68 advanced melanoma patients on anti-PD-1 (nivolumab, CA209-038 trial), demonstrating that pre-therapy TMB predicts OS in ipilimumab-naive but not ipilimumab-progressed patients, and that genomic contraction (selective depletion of neoantigenic clones on-therapy) in responders provides evidence of immunoediting under PD-1 blockade [PMID:29033130](../papers/29033130.md)
- MC3 pan-cancer mutation-calling project (10,510 TCGA pairs) included SKCM; concordance with the legacy PanCan12 MAF exceeded 90%; SKCM had the largest median SNVs per sample along with LUSC and LUAD, consistent with UV-mutagen exposure [PMID:29596782](../papers/29596782.md)
- Pan-cancer fusion study (9,624 TCGA samples) included SKCM; SKCM (melanoma) clustered in the neural-lineage arm-level group with GBM and LGG in the aneuploidy analysis; druggable fusions annotated across 29 cancer types including SKCM [PMID:29617662](../papers/29617662.md)
- Included in TCGA PanCancer Atlas; SKCM/UVM showed highest mutation rates (UVB signature) in iCluster C15; 361/9,125 TCGA PanCanAtlas samples are metastatic (all from SKCM) [PMID:29625048](../papers/29625048.md)
- BRAF-mutant SKCM tumors in C3 immune subtype have higher CD8 T-cell fraction than NRAS-mutant tumors (ANOVA P<2e-5); a CD8-CD274(PD-L1)-PDCD1(PD-1) signaling loop recovered, suggesting BRAF+PD-L1 co-targeting may be synergistic [PMID:29625049](../papers/29625049.md)
- SKCM leads in OncoKB Level 1/2A actionable alteration frequency at 46% (driven by BRAF hotspots at 51%); RTK-RAS alteration rate 95% in SKCM; PI3K+RAF combination actionable in 12% [PMID:29625050](../papers/29625050.md)
- Included in TCGA Pan-Cancer Clinical Data Resource (11,160 patients, 33 cancer types); SKCM TCGA cohort is predominantly metastatic (296 regional lymph-node, 68 distant metastases vs 103 primary); survival correlations should use only the 103 primary tumors [PMID:29625055](../papers/29625055.md)
- Largest cancer type (N=151) in pooled WES ICB cohort of 249 MSS tumors; dominant UV mutational signature (S7) is a stronger correlate of response to immune checkpoint blockade than TMB alone; TMB ceases to predict response after adjusting for dominant signature [PMID:30150660](../papers/30150660.md)
- SKCM (cutaneous melanoma, combined with MEL n=321) was the second-largest histology in the ICI-treated MSK-IMPACT cohort; TMB-high SKCM patients had improved overall survival with ICI and PFS/clinical-benefit associations with TMB were specifically reported. [PMID:30643254](../papers/30643254.md)
- CCLE multi-omic profiling demonstrated that SOX10 promoter hypomethylation and expression are restricted to melanoma (SKCM) cell lines and selectively predict SOX10 knockdown sensitivity, establishing a lineage-specific synthetic lethality mechanism [PMID:31068700](../papers/31068700.md).
- Cutaneous melanoma (SKCM, n=105, 72.9% of cohort) was the dominant subtype in a 144-patient anti-PD1 ICB study; TMB was higher in cutaneous/occult (median 297.5 nonsynonymous mutations) versus acral/mucosal (58; P=1.1e-6); MHC-II HLA expression, TAP2 and MHC-I HLA amplification identified as response predictors; BRAF 39%, NRAS 30%, NF1 17% mutation frequencies [PMID:31792460](../papers/31792460.md)
- Cutaneous/skin melanoma was among TRK fusion-positive tumor types in the MSK prospective cohort (n=5, 6.6%); one melanoma with GON4L-NTRK1 + NRAS Q61R co-mutation was the only TRK fusion-positive case with a co-occurring canonical MAPK driver and showed progressive disease on larotrectinib [PMID:31871300](../papers/31871300.md)

## Subtypes

- SKCM — cutaneous melanoma (this page).
- See [MEL](MEL.md) for the umbrella melanoma OncoTree code spanning cutaneous, acral, mucosal, and uveal subtypes.

## Therapeutic landscape

- Immune checkpoint blockade: [pembrolizumab](../drugs/pembrolizumab.md), [nivolumab](../drugs/nivolumab.md).
- Targeted therapy: BRAF/MEK inhibition ([trametinib](../drugs/trametinib.md), and [BRAF](../genes/BRAF.md) inhibitors).

## Sources

- [PMID:39975212](../papers/39975212.md) — normal skin melanocyte single-cell atlas (Tandukar et al.).

---

*Page last touched by entity-page-writer on 2026-05-01.*

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22622578](../papers/22622578.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22817889](../papers/22817889.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22842228](../papers/22842228.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24265153](../papers/24265153.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25409260](../papers/25409260.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26091043](../papers/26091043.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26359337](../papers/26359337.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26997480](../papers/26997480.md)

- [PMID:28373299](../papers/28373299.md) — Liang et al. 2017; ACRM integrated genomics; SKCM used as comparator for UV-mutation-burden and BRAF/NRAS/NF1 driver landscape.

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29033130](../papers/29033130.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29596782](../papers/29596782.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29617662](../papers/29617662.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29625048](../papers/29625048.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29625050](../papers/29625050.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29625055](../papers/29625055.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30150660](../papers/30150660.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30643254](../papers/30643254.md)

- [PMID:31068700](../papers/31068700.md) — Ghandi et al. CCLE multi-omic profiling (Nature 2019).

*This page was processed by **entity-page-writer** on **2026-05-16**.*

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:31792460](../papers/31792460.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:31871300](../papers/31871300.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
