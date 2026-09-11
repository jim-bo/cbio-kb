# Embedding bake-off: replacing Vertex `gemini-embedding-001` with a local model

**Decision (2026-09-11):** the passage index now uses
`Snowflake/snowflake-arctic-embed-m-v1.5` (Apache-2.0, 110M parameters, 768-dim,
standard BERT architecture, no remote code), run locally with
sentence-transformers. Nothing in retrieval needs a cloud account any more.

## Setup

`eval/embed_bakeoff.py`, run over the 377-paper index's 37,733 chunks, so every
model embeds identical text. It scores the 80 labeled questions in
`eval/questions/v1.yaml` against their `gold_pmids`. There are no LLM calls. Gemini's
query vectors come from the router's cached bank, so the baseline needed no
Vertex call either.

- **dense R@8 / R@40**: share of gold papers among the papers of the top 8 / 40
  dense chunks.
- **dense MRR**: reciprocal rank of the first gold paper.
- **hybrid R@8**: the full `search_hybrid` pipeline (dense + BM25 + wiki graph,
  RRF, cross-encoder rerank, at most 2 passages per paper), the MCP default.
- **router acc**: leave-one-out kNN accuracy of the router's category vote.

## Results

See `2026-09-11.md` (table) and `.json` (per question).

| model | dense R@8 | dense R@40 | dense MRR | hybrid R@8 | router acc |
|---|---|---|---|---|---|
| gemini-embedding-001 (Vertex, 3072-d) | 0.714 | 0.824 | 0.812 | 0.724 | 0.55 |
| **arctic-embed-m-v1.5** | 0.735 | 0.827 | 0.776 | 0.712 | 0.76 |
| bge-base-en-v1.5 | 0.730 | 0.837 | 0.765 | 0.706 | 0.68 |
| e5-base-v2 | 0.678 | 0.798 | 0.689 | 0.696 | 0.86 |
| MedCPT (NCBI query/article encoders) | 0.678 | 0.806 | 0.638 | 0.726 | 0.41 |
| no dense leg (BM25 + graph only) | | | | 0.717 | |

Paired bootstrap (10k resamples) of the per-question difference from Gemini, with 95% CI:

| model | dense R@8 | dense MRR | hybrid R@8 |
|---|---|---|---|
| arctic-embed-m-v1.5 | +0.021 [-0.018, +0.054] | -0.035 [-0.094, +0.021] | -0.012 [-0.055, +0.023] |
| bge-base-en-v1.5 | +0.016 [-0.024, +0.052] | -0.047 [-0.107, +0.012] | -0.018 [-0.060, +0.015] |
| e5-base-v2 | -0.036 [-0.100, +0.021] | **-0.123 [-0.202, -0.048]** | -0.028 [-0.071, +0.004] |
| MedCPT | -0.036 [-0.097, +0.016] | **-0.174 [-0.246, -0.104]** | +0.002 [-0.033, +0.031] |
| no dense leg | | | -0.007 [-0.028, +0.013] |

## Reading it

- arctic and bge are statistically indistinguishable from Gemini on every metric.
  e5 and MedCPT rank the first gold paper significantly worse.
- Hybrid results barely depend on the dense model. Even with no dense leg they
  stay within noise, because BM25, the wiki-graph leg and the reranker do most
  of the work. The dense leg helps mostly on synthesis questions (hybrid R@8
  0.41 without it, 0.48 with arctic) and matters for `search_dense`.
- arctic beat bge on dense recall and router accuracy, and has a permissive
  license and no custom code. Query embedding on CPU takes about 15 ms, so no
  GPU is needed to serve.
- Qwen3-Embedding-0.6B was dropped: it's 5x larger to host, and with the small
  models already at parity it wasn't worth another GPU-hour.

## Caveats

- 80 questions, so differences under about 0.04 are noise, as the CIs show.
- Gold papers were curated against the 377-paper corpus.
- `list` questions score ~0.27 on hybrid R@8 for every model: eight passages
  can't enumerate a list. Those route to agentic, or the client walks
  `get_entity`.
- The Gemini index is kept locally as `data/paper_index_gemini_377` (gitignored)
  for re-running the comparison.
