# cbio-kb MCP server

`ai_search/mcp.py` serves the cBioPortal literature knowledge base over the
[Model Context Protocol](https://modelcontextprotocol.io). It is built to sit
next to the published cBioPortal servers, not replace them:

| Server | Answers | Transport |
|---|---|---|
| [cbioportal-mcp](https://github.com/cBioPortal/cbioportal-mcp) | Data: counts, mutation frequencies, clinical attributes (SQL over ClickHouse). Hosted at `https://mcp.cbioportal.org/db/mcp` (Google OAuth). | stdio / http / sse |
| [cbioportal-navigator](https://github.com/cBioPortal/cbioportal-navigator) | Portal URLs for study, patient, results, and comparison views. | stdio / http |
| **cbio-kb** (this repo) | Literature: what the publication behind each cBioPortal study found, and what the corpus says about a gene, drug, cancer type, or method. | stdio / http / sse |

All three use the same identifiers, so answers compose: a study ID from
`list_studies` on cbioportal-mcp goes straight into `get_study_papers` here, and
every `study_ids` value returned here works with `get_study_guide` there or
`navigate_to_study_view` on the navigator. Genes are HUGO symbols and cancer
types are OncoTree codes throughout.

It follows the same conventions as cbioportal-mcp: stdio by default,
streamable HTTP at `/mcp`, `GET /health`, env-var configuration, a server-level
`instructions` prompt that tells the client how to route between the three
servers, and `{"error_message": ...}` on failure. Its tool names don't overlap
with either server's.

## Tools

| Tool | What it does | Needs |
|---|---|---|
| `get_study_papers(study_id)` | The paper(s) behind a cBioPortal study, plus the corpus papers that analyzed its cohort. Says so explicitly when the study's paper isn't open access. | wiki |
| `get_paper(pmid, sections)` | Metadata, the cBioPortal studies the paper backs (`study_ids`), the cohorts it analyzed (`datasets_used`), and selected sections. | wiki |
| `list_papers(search, study_id, gene, cancer_type, drug, year_from, year_to, limit)` | Metadata filters plus keyword ranking. Fallback when there's no passage index. | wiki |
| `get_entity(kind, id, section)` | Gene / cancer_type / dataset / drug / method / theme page and the papers citing it. Accepts gene aliases and OncoTree names. | wiki |
| `read_wiki_page(path, heading)` | Any page or section; relative links from page content are accepted as-is. | wiki |
| `corpus_info()` | Coverage (how many cBioPortal publications are in the corpus), snapshot date, which retrieval tools are live. | wiki |
| `search_hybrid(query, top_k, max_per_paper)` | Dense + BM25 + wiki-graph passages, RRF-fused and reranked. | passage index |
| `search_dense(query, top_k)` | Dense-only passages. | passage index |
| `route_query(query)` / `search_auto(query)` | The eval-trained router: lookup/definition → hybrid, list/synthesis → agentic (or hybrid plus a walk hint when agentic is off). | passage index |
| `get_passage(pmid, chunk_id \| anchor, context)` | A passage of the paper's full text, verbatim, with its neighbours: the exact wording behind a search result. Search results and `verify_quote` give each passage a paragraph anchor such as `§Results ¶4`. | passage index (`meta.jsonl`) |
| `verify_quote(pmid, quote)` | Checks a quotation against the paper's full text before it's presented as one. A match returns the paper's own wording and a PMC link that opens at that sentence; no match returns the closest sentences and any other papers containing the text. | passage index (`meta.jsonl`) |
| `search_agentic(query)` | Server-side graph-walking agent that returns a cited answer. Only registered when `ANTHROPIC_API_KEY` is set (or `CBIO_KB_MCP_ENABLE_AGENTIC=1`), because it spends tokens on the server's account. | `ANTHROPIC_API_KEY` |

Resources: `cbio-kb://guide`, `cbio-kb://paper/{pmid}`, `cbio-kb://study/{study_id}`.

Every result with text says which kind in `text_source`: verbatim paper text
(search tools, `get_passage`, `verify_quote`), or a wiki summary written by an
LLM from the papers (`get_paper`, `get_entity`, `read_wiki_page`). The server
instructions tell clients to quote only verified paper text and to take numbers
from paper text; see `notes/GROUNDING.md` for why.

Queries are embedded locally with the model that built the passage index
(recorded in `data/paper_index/index_config.json`), so search needs no cloud
account. The server doesn't load `.env`: the agentic tool bills the server
operator, so it's only on when you export `ANTHROPIC_API_KEY` yourself. (An
index built with `gemini-embedding-001` also needs `GCP_PROJECT`; without it,
`search_hybrid` runs as BM25 + graph and says so under `degraded`.)

## Run it

```bash
uv sync --extra mcp                                   # server only (no PyTorch)
uv run cbio-kb serve                                  # stdio
uv run cbio-kb serve --transport http --port 8124     # http://127.0.0.1:8124/mcp
curl -s http://127.0.0.1:8124/health
```

`search_hybrid` needs `data/paper_index/` (FAISS + BM25, built with
`cbio-kb index build-papers` and `cbio-kb index build-bm25`). Everything else
only needs `wiki/`, `data/seed/`, and `schema/ontology/`.

## Connect a client

Claude Code, alongside the official database server:

```bash
claude mcp add --transport http cbioportal https://mcp.cbioportal.org/db/mcp
claude mcp add cbio-kb -- uv run --directory /path/to/cbio-vec cbio-kb serve
# or, against a running HTTP server / container:
claude mcp add --transport http cbio-kb http://127.0.0.1:8124/mcp
```

Claude Desktop (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "cbio-kb": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/cbio-vec", "cbio-kb", "serve"]
    }
  }
}
```

## Docker

The `MCP server image` workflow publishes `ghcr.io/<owner>/cbio-kb-mcp`
(`:main` from the default branch, `:<version>` from `v*` tags). To build it
locally:

```bash
docker build -f docker/mcp.Dockerfile -t cbio-kb-mcp .
docker run --rm -p 8124:8124 \
  -v "$PWD/data/paper_index:/app/data/paper_index:ro" cbio-kb-mcp
```

For stdio clients run it with `-i -e CBIO_KB_MCP_SERVER_TRANSPORT=stdio`.

[hosting.md](hosting.md) has the rest of the deployment story: getting the
passage index into the container without a local checkout (bake it in or
fetch it at start), `deploy/compose.yml`, and a Kubernetes example that
serves the server at `/lit/mcp` behind an ingress, next to cBioPortal's
`/db/mcp`.

### With the cbioportal-mcp-qa agent harness

[cbioportal-mcp-qa](https://github.com/cBioPortal/cbioportal-mcp-qa) drives
servers through a generic agent container pointed at `MCP_SERVER_URL`. Add
cbio-kb to its `agents/docker-compose.yml` the same way the navigator is wired:

```yaml
  cbio-kb:
    image: cbio-kb-mcp:latest
    environment:
      - CBIO_KB_MCP_SERVER_TRANSPORT=http
      - CBIO_KB_MCP_BIND_HOST=0.0.0.0
      - CBIO_KB_MCP_BIND_PORT=8124
    volumes:
      - /path/to/cbio-vec/data/paper_index:/app/data/paper_index:ro
    ports:
      - "8124:8124"

  cbio-kb-agent:
    image: inodb/mcp-agent-base:bedrock
    env_file: [.env]
    environment:
      - MCP_SERVER_URL=http://cbio-kb:8124/mcp
    ports:
      - "8083:5000"
    depends_on: [cbio-kb]
```

The harness's current question set is about portal data (counts and
frequencies), which is cbioportal-mcp's job; cbio-kb is for literature
questions.

## Configuration

| Variable | Default | |
|---|---|---|
| `CBIO_KB_MCP_SERVER_TRANSPORT` | `stdio` | `stdio`, `http`, or `sse`. `--host`/`--port` without `--transport` implies `http`. |
| `CBIO_KB_MCP_BIND_HOST` | `127.0.0.1` | |
| `CBIO_KB_MCP_BIND_PORT` | `8124` | |
| `CBIO_KB_MCP_HTTP_PATH` | `/mcp` | Set when reverse-proxied under a prefix, e.g. `/lit/mcp`. |
| `CBIO_KB_MCP_FORWARDED_ALLOW_IPS` | unset | Trust `X-Forwarded-*` from these IPs (TLS-terminating proxy). |
| `CBIO_KB_MCP_WARM` | `1` | Pre-load BM25, the wiki graph, and the reranker at startup (~30 s otherwise paid by the first search). |
| `CBIO_KB_MCP_ENABLE_AGENTIC` | auto | Force `search_agentic` on/off; default follows `ANTHROPIC_API_KEY`. |
| `CBIO_EMBED_MODEL` | built-in local model | Embedding model for new index builds and the router (a Hugging Face id, run locally). Queries always use the model recorded in the index. |
| `CBIO_EMBED_BACKEND` | `auto` | `onnx` or `torch` for the embedding model and reranker; `auto` uses PyTorch when sentence-transformers is installed, else ONNX Runtime. Same results either way. |
| `CBIO_ONNX_THREADS` | the container's CPU limit, else all cores | ONNX Runtime threads per inference. Set it when the pod has no CPU limit but shares a node (every core would otherwise be claimed per search). |
| `GCP_PROJECT` | unset | Only for an index built with `gemini-embedding-001` (Vertex AI, needs ADC). |
| `CBIO_WIKI_DIR`, `CBIO_KB_SEED_CSV`, `CBIO_KB_ONTOLOGY_DIR`, `RAG_INDEX_DIR` | repo paths | Data locations. |
| `CBIOPORTAL_BASE_URL` | `https://www.cbioportal.org` | Base for returned study URLs (same variable as the navigator). |

## Keeping the corpus current

```bash
uv run cbio-kb ingest seed        # live cBioPortal studies -> data/seed/cbioportal_study_pmids.csv
uv run cbio-kb ingest resolve     # PMID -> PMCID (data/pmid_to_pmcid.csv)
uv run cbio-kb ingest pdfs        # open-access PDFs (Europe PMC first)
uv run cbio-kb ingest extract     # PDFs -> data/raw/papers/{pmid}.md
uv run cbio-kb ingest bioc        # papers with no PDF -> NCBI BioC full text
uv run cbio-kb ontology sync      # refresh schema/ontology snapshot
```

Then compile the new raw papers into the wiki as described in `AGENTS.md`, and
rebuild the passage index. `corpus_info()` reports how many cBioPortal
publications are covered.
