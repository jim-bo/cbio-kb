# syntax=docker/dockerfile:1.6
#
# cbio-kb MCP server image
# ------------------------
# Published to Docker Hub on release (.github/workflows/publish-docker.yml).
# Runs the literature MCP server (ai_search/mcp.py) the same way the
# cBioPortal MCP images run: streamable HTTP at :8124/mcp plus GET /health,
# configured through CBIO_KB_MCP_* env vars (set CBIO_KB_MCP_SERVER_TRANSPORT=stdio
# and run with `docker run -i` for stdio clients).
#
# The passage index (data/paper_index, ~560 MB) is not in git. Mount it to
# enable search_hybrid / search_dense; without it the study, paper, entity
# and list tools still work:
#
#   docker build -t cbio-kb .
#   docker run --rm -p 8124:8124 \
#     -v "$PWD/data/paper_index:/app/data/paper_index:ro" cbio-kb

# ---------- Builder ----------
FROM python:3.13-slim-bookworm AS builder

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never

COPY --from=ghcr.io/astral-sh/uv:0.5.14 /uv /usr/local/bin/uv

WORKDIR /app
COPY pyproject.toml uv.lock README.md ./
COPY src/ src/
RUN uv sync --frozen --no-dev --extra chat --extra server --no-editable

# Bake the cross-encoder reranker weights in so search_hybrid never reaches
# HuggingFace at request time.
ENV HF_HOME=/app/hf-cache \
    CBIO_RERANKER_MODEL=cross-encoder/ms-marco-MiniLM-L-6-v2
RUN .venv/bin/python -c "import os; from sentence_transformers import CrossEncoder; CrossEncoder(os.environ['CBIO_RERANKER_MODEL'])"

# ---------- Runtime ----------
FROM python:3.13-slim-bookworm AS runtime

RUN groupadd --system --gid 1001 app \
    && useradd --system --uid 1001 --gid app --home /app app

WORKDIR /app
COPY --from=builder --chown=app:app /app/.venv /app/.venv
COPY --from=builder --chown=app:app /app/src /app/src
COPY --from=builder --chown=app:app /app/hf-cache /app/hf-cache

# Server code, the compiled wiki, and the small identifier tables it joins on.
COPY --chown=app:app ai_search/ /app/ai_search/
COPY --chown=app:app wiki/ /app/wiki/
COPY --chown=app:app data/seed/ /app/data/seed/
COPY --chown=app:app schema/ontology/studies.json schema/ontology/oncotree.json schema/ontology/sync_log.json /app/schema/ontology/

ENV PYTHONPATH=/app \
    PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    HF_HOME=/app/hf-cache \
    HF_HUB_OFFLINE=1 \
    CBIO_RERANKER_MODEL=cross-encoder/ms-marco-MiniLM-L-6-v2 \
    CBIO_KB_MCP_SERVER_TRANSPORT=http \
    CBIO_KB_MCP_BIND_HOST=0.0.0.0 \
    CBIO_KB_MCP_BIND_PORT=8124

USER app
EXPOSE 8124
HEALTHCHECK --interval=30s --timeout=5s --start-period=60s \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8124/health', timeout=4)" || exit 1

CMD ["python", "-m", "ai_search.mcp"]
