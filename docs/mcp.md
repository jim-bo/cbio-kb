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
| `search_hybrid(query, top_k, max_per_paper)` | Dense + BM25 + wiki-graph passages, RRF-fused and reranked. Runs as BM25 + graph (flagged `degraded`) without Vertex credentials. | passage index |
| `search_dense(query, top_k)` | Dense-only passages. | passage index + `GCP_PROJECT` |
| `route_query(query)` / `search_auto(query)` | The eval-trained router: lookup/definition → hybrid, list/synthesis → agentic (or hybrid plus a walk hint when agentic is off). | passage index |
| `search_agentic(query)` | Server-side graph-walking agent that returns a cited answer. Only registered when `ANTHROPIC_API_KEY` is set (or `CBIO_KB_MCP_ENABLE_AGENTIC=1`), because it spends tokens on the server's account. | `ANTHROPIC_API_KEY` |

Resources: `cbio-kb://guide`, `cbio-kb://paper/{pmid}`, `cbio-kb://study/{study_id}`.

The server doesn't load `.env`. Dense retrieval (Vertex embeddings) and the
agentic tool both bill the server operator, so they're only on when you export
`GCP_PROJECT` / `ANTHROPIC_API_KEY` yourself.

## Run it

```bash
uv sync --extra chat --extra server
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

```bash
docker build -t cbio-kb .
docker run --rm -p 8124:8124 \
  -v "$PWD/data/paper_index:/app/data/paper_index:ro" cbio-kb
```

For stdio clients run it with `-i -e CBIO_KB_MCP_SERVER_TRANSPORT=stdio`.

### With the cbioportal-mcp-qa agent harness

[cbioportal-mcp-qa](https://github.com/cBioPortal/cbioportal-mcp-qa) drives
servers through a generic agent container pointed at `MCP_SERVER_URL`. Add
cbio-kb to its `agents/docker-compose.yml` the same way the navigator is wired:

```yaml
  cbio-kb:
    image: cbio-kb:latest
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
| `GCP_PROJECT` | unset | Enables the dense leg (Vertex `gemini-embedding-001`, needs ADC). |
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
