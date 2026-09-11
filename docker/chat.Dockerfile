# syntax=docker/dockerfile:1.6
#
# cbio-kb chat API image  ->  ghcr.io/<owner>/cbio-kb-chat
# --------------------------------------------------------
# The FastAPI app behind the website's /ask page (ai_search/app.py:
# POST /api/chat, streamed as SSE). Separate from the MCP-server image
# (docker/mcp.Dockerfile). Built by .github/workflows/chat-api.yml, which
# publishes it to GHCR and, optionally, builds the same file with Cloud
# Build for Cloud Run (deploy/cloudrun/). Deployment: docs/hosting.md.
#
#   docker build -f docker/chat.Dockerfile -t cbio-kb-chat .
#   docker run --rm -p 8080:8080 -e ANTHROPIC_API_KEY \
#     -e CHAT_CORS_ORIGINS=https://site.example.org \
#     -v "$PWD/data/paper_index:/app/data/paper_index:ro" cbio-kb-chat
#
# Runtime env: ANTHROPIC_API_KEY (required), CHAT_CORS_ORIGINS (the site's
# origin), SESSION_STORE (memory | firestore).
#
# Multi-stage:
#   1. `builder` installs the project + the `chat` and `cloud` extras into
#      a uv-managed .venv and bakes the model weights.
#   2. `paper-index` optionally downloads a packaged passage index.
#   3. `runtime` is a slim Python image that copies just the venv, weights,
#      index and application source (ai_search + src/cbio_kb + wiki) and
#      runs uvicorn.
#
# The wiki markdown files are COPY'd in because the agent reads them at
# runtime via src/cbio_kb/wiki/vault.py. Rendered HTML (wiki/_site) is
# NOT shipped — that is the separately hosted website.
#
# The RAG and Hybrid modes also need the passage index (data/paper_index,
# not in git). Mount it at /app/data/paper_index, or bake a tarball from
# scripts/package_index.sh in with --build-arg PAPER_INDEX_URL=... (and
# PAPER_INDEX_SHA256=...). Without it only the Agentic mode works.

# ---------- Builder ----------
FROM python:3.13-slim-bookworm AS builder

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never

# uv pinned for reproducibility
COPY --from=ghcr.io/astral-sh/uv:0.5.14 /uv /usr/local/bin/uv

WORKDIR /app

# Install deps first for better layer caching. pyproject.toml + uv.lock
# don't change often; application code changes far more. The project itself
# is installed after the model downloads below, so a source edit doesn't
# re-download model weights.
COPY pyproject.toml uv.lock README.md ./
RUN uv sync --frozen --no-dev --extra chat --extra cloud --no-install-project

# Pre-bake model weights into the image so retrieval never reaches out to
# HuggingFace at request time — that download would otherwise hit on the
# first query after a cold start (added latency + a network-failure mode in
# prod). HF_HOME points the cache at a copyable path; the runtime stage sets
# HF_HUB_OFFLINE so it's used as-is.
#   - the cross-encoder reranker (hybrid mode);
#   - the sentence-transformers model that embeds queries (rag/hybrid dense
#     leg). It must match `embed_model` in the passage index's
#     index_config.json (override with --build-arg EMBED_MODEL=...; pass an
#     empty value to skip it).
ENV HF_HOME=/app/hf-cache \
    CBIO_RERANKER_MODEL=cross-encoder/ms-marco-MiniLM-L-6-v2
RUN .venv/bin/python -c "import os; from sentence_transformers import CrossEncoder; CrossEncoder(os.environ['CBIO_RERANKER_MODEL'])"
ARG EMBED_MODEL=BAAI/bge-base-en-v1.5
RUN if [ -n "$EMBED_MODEL" ]; then \
      .venv/bin/python -c "import sys; from sentence_transformers import SentenceTransformer; SentenceTransformer(sys.argv[1])" "$EMBED_MODEL"; \
    fi

COPY src/ src/
RUN uv sync --frozen --no-dev --extra chat --extra cloud --no-editable

# ---------- Passage index (optional) ----------
# Empty unless PAPER_INDEX_URL is set (see docker/fetch_paper_index.py).
FROM python:3.13-slim-bookworm AS paper-index
COPY docker/fetch_paper_index.py /usr/local/bin/fetch_paper_index.py
ARG PAPER_INDEX_URL=""
ARG PAPER_INDEX_SHA256=""
RUN python /usr/local/bin/fetch_paper_index.py /out "$PAPER_INDEX_URL" "$PAPER_INDEX_SHA256"

# ---------- Runtime ----------
FROM python:3.13-slim-bookworm AS runtime

# Non-root runtime user (good practice; Cloud Run also respects USER)
RUN groupadd --system --gid 1001 app \
    && useradd --system --uid 1001 --gid app --home /app app

WORKDIR /app

# Copy the installed venv and the package tree from the builder.
COPY --from=builder --chown=app:app /app/.venv /app/.venv
COPY --from=builder --chown=app:app /app/src /app/src
# Pre-baked HuggingFace cache (reranker + query-embedding weights).
COPY --from=builder --chown=app:app /app/hf-cache /app/hf-cache
# Passage index: empty unless baked in above; a volume mount replaces it.
COPY --from=paper-index --chown=app:app /out/paper_index /app/data/paper_index

# Application code + raw wiki markdown (agent reads these at runtime).
COPY --chown=app:app ai_search/ /app/ai_search/
COPY --chown=app:app wiki/ /app/wiki/

# ai_search isn't pip-installed (only src/cbio_kb is in the wheel), so we
# put /app on PYTHONPATH so `import ai_search` resolves.
#
# SESSION_STORE=memory keeps chat history in the process, which is right for
# one replica. The Cloud Run deploy sets SESSION_STORE=firestore itself
# (Firestore via Application Default Credentials; see ai_search/sessions.py).
ENV PYTHONPATH=/app \
    PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    SESSION_STORE=memory \
    HF_HOME=/app/hf-cache \
    HF_HUB_OFFLINE=1 \
    CBIO_RERANKER_MODEL=cross-encoder/ms-marco-MiniLM-L-6-v2

USER app

# Cloud Run sets PORT; default to 8080 for local docker runs.
ENV PORT=8080
EXPOSE 8080

# Shell form so $PORT is expanded at start.
CMD exec uvicorn ai_search.app:app --host 0.0.0.0 --port ${PORT}
