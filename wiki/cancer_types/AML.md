---
name: Acute Myeloid Leukemia
oncotree_code: AML
main_type: Leukemia
parent: MNM
tags: []
processed_by: crosslinker
processed_at: 2026-05-21
---

# Acute Myeloid Leukemia (AML)

## Overview

Acute Myeloid Leukemia (AML) is a hematologic malignancy arising from myeloid progenitor cells, classified under the Leukemia main type in OncoTree (parent node [MNM](../cancer_types/MNM.md)). Adult AML genomes are mutation-sparse (mean ~13 coding mutations per sample) yet nearly every tumor harbors at least one driver event across nine recognized functional gene categories: transcription-factor fusions, [NPM1](../genes/NPM1.md) mutations, tumor suppressors, DNA-methylation genes, activated signaling, chromatin modifiers, myeloid transcription factors, cohesin complex, and spliceosome genes.

## Cohorts in the corpus

- [laml_tcga_pub](../datasets/laml_tcga_pub.md) — 200 adult de novo AML cases (50 WGS, 150 WES) from Washington University tissue banking (Nov 2001–Mar 2010); complemented by RNA-seq, microRNA-seq, 450k methylation, and SNP arrays. [PMID:23634996](../papers/23634996.md)

## Recurrent alterations

- TCGA WGS/WES of 200 adult de novo AML cases identified 23 significantly mutated genes (FDR <0.05 by MuSiC); near-universal driver coverage: transcription-factor fusions (18%), [NPM1](../genes/NPM1.md) (27%), tumor suppressors (16%), DNA-methylation genes (44%), activated signaling (59%), chromatin modifiers (30%), myeloid transcription factors (22%), cohesin complex (13%), spliceosome (14%); a novel [NPM1](../genes/NPM1.md) + [DNMT3A](../genes/DNMT3A.md) + [FLT3](../genes/FLT3.md) co-occurring triplet defined a putative epigenetic AML subtype with distinct mRNA, miRNA, and CpG-sparse methylation signatures [PMID:23634996](../papers/23634996.md)
- In a Sanger sequencing screen of 1,345 hematologic cancers for [CALR](../genes/CALR.md) exon 9 mutations, AML cases showed no [CALR](../genes/CALR.md) mutations, confirming that [CALR](../genes/CALR.md) indels are restricted to the MPN/MDS disease spectrum and are absent from acute myeloid leukemia. [PMID:24325359](../papers/24325359.md)
- Papaemmanuil et al. 2016 sequenced 111 cancer genes in 1540 adults with AML (AMLSG trials), identifying 5234 driver mutations across 76 genes and 11 mutually exclusive genomic subgroups; three new categories (chromatin–spliceosome 18%, [TP53](../genes/TP53.md)–aneuploidy 13%, provisional [IDH2](../genes/IDH2.md) R172 1%) were defined, with the full genomic model achieving ~71% concordance for overall survival versus ~64% with ELN variables alone [PMID:27276561](../papers/27276561.md).
- Single-arm prospective trial (N=116, Washington University) of 10-day [decitabine](../drugs/decitabine.md) cycles: 100% blast clearance in TP53-mutant AML (21/21) vs 41% in [TP53](../genes/TP53.md) wild-type (P<0.001); unfavorable-risk karyotype predicted response (67% vs 34%, P<0.001); remissions were short-lived and mutation clearance never complete; median [OS](../cancer_types/OS.md) 12.7 months (TP53-mutant) vs 15.4 months ([TP53](../genes/TP53.md) wild-type, P=0.79) — substantially better than 4–6 months with conventional induction in TP53-mutant AML [PMID:27959731](../papers/27959731.md).
- PIPseq program (101 high-risk pediatric patients, Columbia University Medical Center) sequenced AML cases including [KIT](../genes/KIT.md) Asn655Lys, [IDH1](../genes/IDH1.md) R132C, [JAK3](../genes/JAK3.md) A573V, KMT2A-AFF1, NUP98-NSD1, [PTPN11](../genes/PTPN11.md) G503V, [CEBPA](../genes/CEBPA.md) biallelic frameshift, CBFB-MYH11 fusion, and [KMT2C](../genes/KMT2C.md) E704X mutations/fusions; actionable alterations identified in 47% of hematologic cases [PMID:28007021](../papers/28007021.md)
- Germline WES study of 372 pediatric cancer patients (Düsseldorf) included AML cases; hematologic neoplasms accounted for 57% of the cohort and LP/PVs in TP53, [CHEK2](../genes/CHEK2.md), and [ATM](../genes/ATM.md) were among the most common drivers [PMID:29489754](../papers/29489754.md)
- MC3 multi-center mutation calling project called somatic variants across 10,510 TCGA tumor/normal pairs including AML ([LAML](../cancer_types/LAML.md)); AML recovered only 44% of legacy AWG calls because tumor-in-normal contamination in [LAML](../cancer_types/LAML.md) skin 'normals' causes MC3's conservative filtering to misclassify somatic calls as germline [PMID:29596782](../papers/29596782.md)
- Pan-cancer aneuploidy analysis (10,522 TCGA tumors) found AML has one of the lowest aneuploidy scores (mean 1.6 arm-level alterations) across 33 cancer types, consistent with a predominantly mutation-driven rather than CNA-driven disease [PMID:29622463](../papers/29622463.md)
- AML resequencing on the Bionimbus Protected Data Cloud cited as exemplar of cloud-enabled somatic-variant discovery in adverse-risk primary AML ([CUX1](../genes/CUX1.md) haploinsufficiency study, Blood 2013); not a primary AML analysis [PMID:29902176](../papers/29902176.md)
- Beat AML profiled 672 primary tumor specimens from 562 AML patients using whole-exome sequencing, RNA-seq, and ex vivo drug-sensitivity assays against 122 compounds; integrating these layers identified novel mutational events and mapped drug-response patterns to single and combinatorial mutational events (e.g., FLT3-ITD/NPM1 co-mutation sensitizes to [ibrutinib](../drugs/ibrutinib.md) and [entospletinib](../drugs/entospletinib.md); BCOR/RUNX1 co-mutation sensitizes to JAK inhibitors); dataset deposited as [aml_ohsu_2018](../datasets/aml_ohsu_2018.md) [PMID:30333627](../papers/30333627.md)
- Pan-cancer CCLE profiling (1,072 cell lines) identified phospho-SHP2 (pY542) as a biomarker of [ponatinib](../drugs/ponatinib.md) sensitivity in AML lines; 4/5 previously untested AML lines with high pSHP2 were ponatinib-sensitive, including lines carrying [FLT3](../genes/FLT3.md), [KIT](../genes/KIT.md), and [FGFR1](../genes/FGFR1.md) alterations [PMID:31068700](../papers/31068700.md).
- AML (53% of hematologic malignancies in PM [NSGCT](../cancer_types/NSGCT.md) cohort, n=15), nearly half of which were [AMKL](../cancer_types/AMKL.md) M7, arose from a shared germ-cell precursor with the paired [GCT](../cancer_types/GCT.md); canonical AML drivers ([FLT3](../genes/FLT3.md), [DNMT3A](../genes/DNMT3A.md), [TET2](../genes/TET2.md), [NPM1](../genes/NPM1.md)) were absent; median survival was 6.3 months (95% CI 4.6–25.2). [PMID:32897884](../papers/32897884.md)
- In the MSK-IMPACT CH cohort (n=24,146), CH → therapy-related myeloid neoplasm (tMN/AML) progression was tracked in 35 paired pre-tMN/tMN samples; 19/32 (59%) already harbored leukemia-defining mutations at the CH stage; TP53-mutant tMNs co-occurred with complex karyotype in 12/13 evaluable cases. [PMID:33106634](../papers/33106634.md)
- Serial bone-marrow sequencing of 52 high-risk [NBL](../cancer_types/NBL.md) patients (HemePACT + FusionPlex Pan-Heme): AML was an endpoint for therapy-related myeloid neoplasm development after neuroblastoma therapy; 17 transformation cases included AML/MDS outcomes [PMID:35078859](../papers/35078859.md)
- AML was included in the MAPPYACTS pediatric precision-medicine trial (n=787); [IDH1](../genes/IDH1.md) R132L mutation (n=1) was identified as ready-for-routine-use in AML, targetable by [ivosidenib](../drugs/ivosidenib.md) [PMID:35292802](../papers/35292802.md)

## Subtypes

- **[POLE](../genes/POLE.md) ultramutated / FAB-based stratification.** RNA-seq NMF consensus clustering identified 7 mRNA groups and 5 miRNA groups mapping onto FAB subtypes (M1, M3, M4, M5). [PMID:23634996](../papers/23634996.md)
- **Transcription-factor fusion-driven (PML-RARA, RUNX1-RUNX1T1, MYH11-CBFB, [KMT2A](../genes/KMT2A.md) fusions):** favorable-risk; carry the fewest cooperating mutations (MLL-fused mean 2.09 vs. 5.24 overall, P=0.002). [PMID:23634996](../papers/23634996.md)
- **[NPM1](../genes/NPM1.md) + [DNMT3A](../genes/DNMT3A.md) + [FLT3](../genes/FLT3.md) triple-mutant:** putative novel intermediate-risk subtype with methylation loss in CpG-sparse regions and distinct miRNA signature (high miR-10a, low miR-424). [PMID:23634996](../papers/23634996.md)
- **TP53-mutant unfavorable-risk:** mean 7.00 tier-1 mutations; mutually exclusive of [FLT3](../genes/FLT3.md) and NPM1; associated with complex cytogenetics. [PMID:23634996](../papers/23634996.md)

## Therapeutic landscape

- No drug treatments were administered or evaluated in the TCGA AML study; the dataset ([laml_tcga_pub](../datasets/laml_tcga_pub.md)) was released as a public resource for risk-stratification and pathogenesis research. [PMID:23634996](../papers/23634996.md)
- Authors argue that [DNMT3A](../genes/DNMT3A.md), IDH1/IDH2, and [TET2](../genes/TET2.md) add prognostic value for intermediate-risk classification beyond the then-current markers ([FLT3](../genes/FLT3.md), NPM1, [CEBPA](../genes/CEBPA.md), [KIT](../genes/KIT.md)). [PMID:23634996](../papers/23634996.md)

## Sources

- [PMID:23634996](../papers/23634996.md) — TCGA Research Network. Genomic and epigenomic landscapes of adult de novo acute myeloid leukemia. *N Engl J Med* 2013.

- [PMID:24325359](../papers/24325359.md)

- [PMID:27276561](../papers/27276561.md) — Papaemmanuil et al. 2016, NEJM. Genomic classification and prognosis in AML; 1540 patients, 111-gene panel, 11 genomic subgroups.

- [PMID:27959731](../papers/27959731.md)

- [PMID:28007021](../papers/28007021.md)

- [PMID:29489754](../papers/29489754.md)

- [PMID:29596782](../papers/29596782.md)

- [PMID:29622463](../papers/29622463.md)

- [PMID:29902176](../papers/29902176.md)

- [PMID:30333627](../papers/30333627.md)

- [PMID:31068700](../papers/31068700.md) — Ghandi et al. CCLE multi-omic profiling (Nature 2019).


- [PMID:32897884](../papers/32897884.md)

- [PMID:33106634](../papers/33106634.md)

- [PMID:35078859](../papers/35078859.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35292802](../papers/35292802.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
