# Confounded results — archived 2026-06-07, kept as evidence (do NOT cite as findings)

These four runs were produced on 2026-06-06 **before** the full-corpus refresh, when the
eval was silently unfair: `rag`/`hybrid` retrieved from a frozen 56-paper FAISS/BM25 index
while `agentic` walked the live 377-paper wiki vault. The 3-way numbers therefore measure
corpus size as much as retrieval strategy. See `notes/EVAL_FULL_CORPUS_REFRESH.md`.

- `2026-06-06-130243/` — partial / early run
- `2026-06-06-133624/` — hybrid only, val (56-corpus)
- `2026-06-06-135213/` — agentic only, synthesis S10–S12 (377-vs-56 leak)
- `2026-06-06-140201/` — matched val, all 3 modes (**confounded**; the artifact that
  demonstrates the asymmetry)

The rag-vs-hybrid comparison within these is fair (identical 56-PMID index); only the
agentic column is compromised. Retained for provenance / the methods writeup. Fair 3-way
results live in the post-refresh `eval/results/{ts}/` dirs.
