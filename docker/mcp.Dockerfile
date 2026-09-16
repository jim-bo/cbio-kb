# syntax=docker/dockerfile:1.6
#
# cbio-kb MCP server image  ->  ghcr.io/<owner>/cbio-kb-mcp
# ---------------------------------------------------------
# Built by .github/workflows/mcp-server.yml (PRs build; main and v* tags
# publish to GHCR). Deployment: docs/hosting.md, deploy/compose.yml,
# deploy/k8s/mcp.yaml.
#
# Runs the literature MCP server (ai_search/mcp.py) the same way the
# cBioPortal MCP images run: streamable HTTP at :8124/mcp plus GET /health,
# configured through CBIO_KB_MCP_* env vars (set CBIO_KB_MCP_SERVER_TRANSPORT=stdio
# and run with `docker run -i` for stdio clients; set
# CBIO_KB_MCP_HTTP_PATH=/lit/mcp behind a path-prefixed ingress).
#
# The passage index (data/paper_index, FAISS + BM25, ~0.25 GB) is not in git.
# It powers search_hybrid / search_dense; without it the study, paper, entity
# and list tools still work and the search tools say the index is missing.
# Either mount it at runtime:
#
#   docker build -f docker/mcp.Dockerfile -t cbio-kb-mcp .
#   docker run --rm -p 8124:8124 \
#     -v "$PWD/data/paper_index:/app/data/paper_index:ro" cbio-kb-mcp
#
# or bake a tarball from scripts/package_index.sh into the image:
#
#   docker build -f docker/mcp.Dockerfile -t cbio-kb-mcp \
#     --build-arg PAPER_INDEX_URL=https://.../paper-index-YYYYMMDD.tar.gz \
#     --build-arg PAPER_INDEX_SHA256=<sha256> .

# ---------- Builder ----------
FROM python:3.13-slim-bookworm AS builder

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never

COPY --from=ghcr.io/astral-sh/uv:0.5.14 /uv /usr/local/bin/uv

WORKDIR /app
# Dependencies first, then model weights, then the project itself, so a
# source edit reuses the cached dependency and model layers.
COPY pyproject.toml uv.lock README.md ./
RUN uv sync --frozen --no-dev --extra mcp --no-install-project

# Bake the search models into HF_HOME so the server never reaches Hugging Face
# at request time (the runtime stage sets HF_HUB_OFFLINE=1). They run on ONNX
# Runtime, so the image has no PyTorch (src/cbio_kb/index/onnx_models.py):
#   - RERANK_MODEL, the cross-encoder that reranks search_hybrid results;
#   - EMBED_MODEL, which embeds queries for the dense leg. It must match
#     `embed_model` in the passage index's index_config.json (pass an empty
#     value to skip it).
# onnx_models.py is copied on its own so edits elsewhere in src/ reuse the
# cached model layer.
ARG EMBED_MODEL=Snowflake/snowflake-arctic-embed-m-v1.5
ARG RERANK_MODEL=cross-encoder/ms-marco-MiniLM-L-6-v2
ENV HF_HOME=/app/hf-cache
COPY src/cbio_kb/index/onnx_models.py /tmp/onnx_models.py
RUN .venv/bin/python /tmp/onnx_models.py --embed "$EMBED_MODEL" --rerank "$RERANK_MODEL"

COPY src/ src/
RUN uv sync --frozen --no-dev --extra mcp --no-editable

# ---------- Passage index (optional) ----------
# Empty unless PAPER_INDEX_URL is set, in which case the tarball is
# downloaded, checked against PAPER_INDEX_SHA256 (if given) and unpacked.
FROM python:3.13-slim-bookworm AS paper-index
COPY docker/fetch_paper_index.py /usr/local/bin/fetch_paper_index.py
ARG PAPER_INDEX_URL=""
ARG PAPER_INDEX_SHA256=""
RUN python /usr/local/bin/fetch_paper_index.py /out "$PAPER_INDEX_URL" "$PAPER_INDEX_SHA256"

# ---------- Runtime ----------
FROM python:3.13-slim-bookworm AS runtime

RUN groupadd --system --gid 1001 app \
    && useradd --system --uid 1001 --gid app --home /app app

WORKDIR /app
COPY --from=builder --chown=app:app /app/.venv /app/.venv
COPY --from=builder --chown=app:app /app/src /app/src
COPY --from=builder --chown=app:app /app/hf-cache /app/hf-cache
COPY --from=paper-index --chown=app:app /out/paper_index /app/data/paper_index

# Server code, the compiled wiki, and the small identifier tables it joins on.
COPY --chown=app:app ai_search/ /app/ai_search/
COPY --chown=app:app wiki/ /app/wiki/
COPY --chown=app:app data/seed/ /app/data/seed/
COPY --chown=app:app schema/ontology/studies.json schema/ontology/oncotree.json schema/ontology/sync_log.json /app/schema/ontology/
# The labeled eval questions: search_auto / route_query classify a question
# by its nearest neighbours here (without the file they fall back to keyword
# cues).
COPY --chown=app:app eval/questions/v1.yaml /app/eval/questions/v1.yaml
# Also shipped in the image so a Kubernetes initContainer can fetch the index
# at pod start instead of baking it in (see deploy/k8s/mcp.yaml).
COPY --chown=app:app docker/fetch_paper_index.py /app/docker/fetch_paper_index.py

ARG RERANK_MODEL=cross-encoder/ms-marco-MiniLM-L-6-v2
ENV PYTHONPATH=/app \
    PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    HF_HOME=/app/hf-cache \
    HF_HUB_OFFLINE=1 \
    CBIO_RERANKER_MODEL=$RERANK_MODEL \
    CBIO_ROUTER_CACHE=/tmp/router_qbank.npz \
    CBIO_KB_MCP_SERVER_TRANSPORT=http \
    CBIO_KB_MCP_BIND_HOST=0.0.0.0 \
    CBIO_KB_MCP_BIND_PORT=8124

USER app
EXPOSE 8124
HEALTHCHECK --interval=30s --timeout=5s --start-period=60s \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8124/health', timeout=4)" || exit 1

CMD ["python", "-m", "ai_search.mcp"]
