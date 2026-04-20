# RAG vs. Agentic: comparison harness

Compare two retrieval strategies on the same cBioPortal paper corpus:

- **Agentic** — PydanticAI agent in `ai_search/` walking the compiled `wiki/` vault via tools.
- **RAG** — pure vector retrieval over the 56 raw paper markdowns in `data/raw/papers/`, packed into a single-shot LLM call.

Both use **`claude-haiku-4-5`** as the answering model. **`claude-opus-4-6`** is the judge.

## Corpus

`corpus_pmids.txt` — 56 PMIDs present in both `wiki/papers/` and `data/raw/papers/`. Indexer and runners both restrict to this list so neither side gets free knowledge the other can't access.

## Layout

```
eval/
├── corpus_pmids.txt        # 56 PMIDs — shared corpus
├── questions/v1.yaml       # curated Q set with gold labels + splits
├── runners/
│   ├── agentic.py          # run Q through /api/chat agentic mode
│   └── rag.py              # run Q through RAG mode
├── judge.py                # opus rubric grader
├── run.py                  # end-to-end: Qs → runners → judge → results/
└── results/{YYYY-MM-DD-HHMM}/
    ├── runs.jsonl          # per-question per-mode record
    └── report.md           # aggregate summary
```

## Question set

`questions/v1.yaml` — 50 questions, categorized by type (`lookup`, `list`, `synthesis`, `definition`), split 30/10/10 `train`/`val`/`test`.

- **train** → prompt + retrieval tuning
- **val** → configuration selection
- **test** → final reported numbers (do not peek)

Each entry: `{id, question, category, split, gold_pmids, gold_entities}`.

## Metrics

Per query, both runners log: `input_tokens`, `output_tokens`, `llm_calls`, `wall_time_s`, `retrieved_sources`, `cited_pmids`, `answer`.

Judge scores (1–5) on: `accuracy`, `completeness`, `citation_correctness`.

Derived per mode: cost per query, citation recall vs. gold, aggregate quality score, per-category breakdown.

## Cost framing

Neither strategy is budget-matched against the other — each carries its
own cost shape (agentic spends tokens on graph-walk; RAG spends tokens on
packed passages). Per-run records include `input_tokens`,
`output_tokens`, `llm_calls`, and `wall_time_s` so the cost/quality
tradeoff is visible on the reports. See `plots/cost_quality.png`.

## Running

```bash
# Start the chat API on localhost:8080
.venv/bin/uvicorn ai_search.app:app --host 0.0.0.0 --port 8080

# Run a split, both modes (SSE-streams through /api/chat)
uv run python -m eval.run --split train --mode both
uv run python -m eval.run --split val --mode both
uv run python -m eval.run --split test --mode both

# Narrow to specific IDs (crosses splits)
uv run python -m eval.run --ids L01,LS04,S07 --mode both

# Build the wiki-embedded report from the latest run
uv run python -m eval.build_report

# Or combine train (primary) with val/test comparison tables
uv run python -m eval.build_report \
    --run-dir   eval/results/{train_ts} \
    --val-dir   eval/results/{val_ts} \
    --test-dir  eval/results/{test_ts}

# Regenerate per-question JSON for the traversal explorer
uv run python -m eval.build_explorer_data --run-dir eval/results/{train_ts}
```

## Artifacts written to the wiki

- `wiki/experiments/rag-vs-agentic.qmd` — headline table, per-category
  breakdown, per-question results, notable failures.
- `wiki/experiments/plots/*.png,*.html` — scatter (interactive),
  category bars, cost/quality, strategy strip (gantt + top-k).
- `wiki/experiments/explorer/*.json` — per-question payloads with
  tool timelines + retrieval, consumed by the traversal explorer page.

## Guardrails

- Agent runs are capped at 20 tool calls (`ai_search/app.py`,
  `UsageLimits(tool_calls_limit=20)`); exceeding cap sets
  `tool_limit_reached: true` on the record.
- Runner enforces a 180s wall-clock deadline on the SSE stream; exceeding
  it sets `timed_out: true`.
- Both flags are surfaced in the report's "Run guardrails" section.
