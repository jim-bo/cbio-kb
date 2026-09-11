# Hosting cbio-kb

This repo ships three pieces that are hosted independently, plus one data
artifact they share:

- **Website**: the Quarto site rendered from `wiki/`, including the `/ask`
  chat page.
- **Chat API**: the FastAPI service the `/ask` page talks to.
- **MCP server**: the literature MCP server that sits next to cBioPortal's
  own MCP servers.
- **Passage index**: the FAISS + BM25 search index (`data/paper_index/`).
  It is not in git and both containers can use it.

None of them needs Google Cloud. GCP only appears in one optional CI job
that deploys the chat API to Cloud Run for the original maintainer. Delete
that job and nothing else changes.

## At a glance

| | Website | Chat API | MCP server |
|---|---|---|---|
| **What** | Static HTML from `wiki/` (Quarto). `/ask` is a chat UI. | FastAPI app `ai_search/app.py`: `POST /api/chat`, streamed as SSE. Agentic, RAG and Hybrid modes. | FastMCP server `ai_search/mcp.py`: streamable HTTP at `/mcp`, `GET /health`. See [mcp.md](mcp.md). |
| **Needs at runtime** | Nothing but a web server. `/ask` needs a reachable chat API that allows the site's origin (CORS). | `ANTHROPIC_API_KEY`. The wiki is baked into the image. RAG and Hybrid also need the passage index. Sessions live in memory (one replica) or in Firestore. | Nothing required: wiki, study table and ontology are baked in. The search tools need the passage index. `ANTHROPIC_API_KEY` is optional and turns on `search_agentic`. |
| **Artifact** | `wiki/_site/`, uploaded as the `site` workflow artifact | `ghcr.io/<owner>/cbio-kb-chat` from [`docker/chat.Dockerfile`](../docker/chat.Dockerfile) | `ghcr.io/<owner>/cbio-kb-mcp` from [`docker/mcp.Dockerfile`](../docker/mcp.Dockerfile); also `<DOCKER_USERNAME>/cbio-kb` on Docker Hub for tags, if configured |
| **Built by** | [`website.yml`](../.github/workflows/website.yml) (`quarto render wiki`) | [`chat-api.yml`](../.github/workflows/chat-api.yml), `image` job | [`mcp-server.yml`](../.github/workflows/mcp-server.yml) |
| **Deployed today** | GitHub Pages (`gh-pages` branch) on every relevant push to `main` | Google Cloud Run: the `cloud-run` job in `chat-api.yml`, which uses Cloud Build, Artifact Registry, Secret Manager and Firestore | Not hosted by this repo; images only |
| **Config / secrets** | Variables `CHAT_API_URL`, `PUBLISH_GH_PAGES` | Runtime: `ANTHROPIC_API_KEY`, `CHAT_CORS_ORIGINS`, `SESSION_STORE`. CI (Cloud Run only): `GCP_*` variables and `GCP_SA_KEY` | Runtime: `CBIO_KB_MCP_*` ([mcp.md](mcp.md#configuration)). CI: optional `PAPER_INDEX_*`, `DOCKER_*` |
| **To self-host** | Keep Pages, or serve `wiki/_site/` from any static host. Set `CHAT_API_URL`. | Run the GHCR image ([`deploy/k8s/chat.yaml`](../deploy/k8s/chat.yaml), [`deploy/compose.yml`](../deploy/compose.yml)). Keep one replica. Delete the `cloud-run` job and `deploy/cloudrun/`. | Run the GHCR image ([`deploy/k8s/mcp.yaml`](../deploy/k8s/mcp.yaml), [`deploy/compose.yml`](../deploy/compose.yml)). Set `CBIO_KB_MCP_HTTP_PATH=/lit/mcp` behind a path-prefixed ingress. |

## Where things live

```
docker/mcp.Dockerfile        MCP server image
docker/chat.Dockerfile       chat API image
docker/fetch_paper_index.py  downloads + unpacks a packaged index (image build, k8s initContainer)
scripts/package_index.sh     data/paper_index/ -> dist/paper-index-YYYYMMDD.tar.gz (+ .sha256)
deploy/compose.yml           one host: MCP server, and the chat API with --profile chat
deploy/k8s/mcp.yaml          Deployment + Service + Ingress, MCP at /lit/mcp
deploy/k8s/chat.yaml         Deployment + Service + Ingress, chat at /api/chat
deploy/cloudrun/             Cloud Run only: Cloud Build config + manual deploy script
wiki/ask-config.js           the website's only deployment-specific value (chat API URL)
.github/workflows/           test.yml, website.yml, chat-api.yml, mcp-server.yml
```

## Workflows

| Workflow | Runs on | Does |
|---|---|---|
| `test.yml` | every push to `main`, every PR, manual | pytest, `cbio-kb lint --allow-orphans`, crosslink dry run. Deploys nothing. |
| `website.yml` | changes under `wiki/` or `schema/`, manual | Renders the site and uploads it as the `site` artifact. On `main`, publishes to GitHub Pages. |
| `mcp-server.yml` | changes to anything baked into the MCP image, `v*` tags, manual | PRs: build only. `main`: push `:main` and `:sha-<short>`. Tags: `:<version>`, `:<major>.<minor>`, `:latest`, plus Docker Hub if its secrets exist. |
| `chat-api.yml` | changes to anything baked into the chat image, `v*` tags, manual | `image` job: same tagging as the MCP image, to GHCR. `cloud-run` job: optional deploy (below). |

The path filters mean a code change (`ai_search/`, `src/`) rebuilds the two
images but not the site, and a change to the site's own files (`wiki/*.js`,
`*.css`, `*.qmd`, `_quarto.yml`) rebuilds only the site. Wiki content
(`wiki/**.md`, `wiki/graph.json`) rebuilds all three, because both images
bake in the wiki markdown.

Because of the path filters, only make `test` a required status check. A PR
that touches no image paths never reports an image check.

GHCR pushes use the workflow's own `GITHUB_TOKEN` (`packages: write`), so no
registry secret is needed. Check each new package's visibility after its
first push; it may start out private. Either make it public in the
package's settings, or give the cluster an image pull secret (a token with
`read:packages`).

### Repository variables and secrets

All optional unless noted. Set them under Settings > Secrets and variables >
Actions.

| Name | Kind | Used by | When unset |
|---|---|---|---|
| `CHAT_API_URL` | variable | website | The URL committed in `wiki/ask-config.js` ships |
| `PUBLISH_GH_PAGES` | variable | website | Publishes to Pages; `false` skips it |
| `PAPER_INDEX_URL` | variable | both images (and the Cloud Run build) | No index is baked in |
| `PAPER_INDEX_SHA256` | variable | same | The download isn't checksum-verified |
| `DOCKER_USERNAME`, `DOCKER_PASSWORD` | secrets | mcp-server, tags only | The Docker Hub push is skipped |
| `GCP_PROJECT_ID` | variable | chat-api `cloud-run` | The job is skipped. On `jim-bo/cbio-kb` only, it falls back to `cbioportal-python` |
| `GCP_REGION` | variable | `cloud-run` | `us-central1` |
| `CLOUD_RUN_SERVICE` | variable | `cloud-run` | `cbio-kb-api` |
| `GCP_ARTIFACT_REPO` | variable | `cloud-run` | `cbio-kb` |
| `GCP_ANTHROPIC_SECRET` | variable | `cloud-run` | `anthropic-api-key` (Secret Manager name) |
| `CHAT_CORS_ORIGINS` | variable (a secret also works) | `cloud-run` | `https://<owner>.github.io` plus `localhost:8080` |
| `GCP_SA_KEY` | secret | `cloud-run` | Required whenever that job runs |

## Passage index

`data/paper_index/` holds `faiss.index`, `meta.jsonl` and `index_config.json`
(from `cbio-kb index build-papers`), plus `bm25.pkl` (from `cbio-kb index
build-bm25`). It is about 0.5 GB and gitignored. Two things use it:

- the MCP server's `search_hybrid`, `search_dense` and `search_auto` tools;
- the chat API's RAG and Hybrid modes.

Without it, the MCP wiki tools still work and the search tools return an
error naming the missing index. The chat API's Agentic mode also still
works.

**Embedding model.** `index_config.json` records the Hugging Face model the
index was embedded with (`embed_model`). Both images download a model into
their Hugging Face cache at build time: the `EMBED_MODEL` build arg, set by
default in the Dockerfiles. They run with `HF_HUB_OFFLINE=1`, so the two
must match. When you rebuild the index with a different model, change
`EMBED_MODEL` in both Dockerfiles in the same commit. `CBIO_EMBED_MODEL`
overrides the model at runtime, but only with a model that is already in
the image's cache.

**Build and package it** on any machine with the raw papers:

```bash
uv run cbio-kb index build-papers   # see AGENTS.md for --papers-dir/--pmid-list/--incremental
uv run cbio-kb index build-bm25
scripts/package_index.sh            # -> dist/paper-index-YYYYMMDD.tar.gz + .sha256
```

The script prints the sha256 and the release commands to run. Host the
tarball wherever the image build or cluster can fetch it with a plain
unauthenticated HTTPS GET. A GitHub Release asset on a public repo works;
the limit is 2 GB per asset. So does an internal file server. Give each
index a new file name (the date stamp does this), so Docker's build cache
never serves an old one.

**Get it into a container.** Pick one:

| Option | How | Suits |
|---|---|---|
| Bind mount | `-v /path/to/paper_index:/app/data/paper_index:ro`; in compose, set `PAPER_INDEX_DIR` | One host, a laptop |
| Bake into the image | Set `PAPER_INDEX_URL` + `PAPER_INDEX_SHA256` repository variables, and CI images include it. Locally: `--build-arg PAPER_INDEX_URL=... --build-arg PAPER_INDEX_SHA256=...` | Kubernetes. Code, wiki and index become one immutable artifact; the image grows by ~0.5 GB |
| Fetch at pod start | The commented initContainer in `deploy/k8s/mcp.yaml`. It reuses the image's fetch script to download into an emptyDir | Kubernetes, when the index is updated separately from releases |
| PersistentVolume | Unpack into a PVC and mount it at `/app/data/paper_index` | Clusters with shared storage |

A mount hides whatever index the image baked in, so use one approach per
deployment.

## Running each piece

### Website

- **GitHub Pages** (today): `website.yml` publishes on `main`. The repo's
  Pages setting should be "Deploy from a branch: `gh-pages`".
- **Anywhere else**: download the `site` artifact from a workflow run, or
  run `quarto render wiki`. Serve `wiki/_site/` as static files (nginx, a
  bucket, an existing web server). Set `PUBLISH_GH_PAGES=false` if Pages
  isn't wanted.
- **Pointing `/ask` at a chat API**: set `CHAT_API_URL` to the full
  endpoint, e.g. `https://kb.example.org/api/chat`, or edit
  `wiki/ask-config.js`. If the site and the API share a host behind one
  ingress, `/api/chat` works and no CORS is involved. Otherwise the chat
  API's `CHAT_CORS_ORIGINS` must include the site's origin. On
  `localhost`, the page always uses `http://localhost:8080`.
- **Local preview**: see "Dev servers" in [AGENTS.md](../AGENTS.md).

### Chat API

```bash
docker run --rm -p 8080:8080 \
  -e ANTHROPIC_API_KEY \
  -e CHAT_CORS_ORIGINS=https://kb.example.org \
  -v "$PWD/data/paper_index:/app/data/paper_index:ro" \
  ghcr.io/<owner>/cbio-kb-chat:main
```

| Env | Default | |
|---|---|---|
| `ANTHROPIC_API_KEY` | none | Required. Every chat turn is billed to this key. |
| `CHAT_CORS_ORIGINS` | localhost dev origins and `https://jim-bo.github.io` | Comma-separated origins allowed to call the API. |
| `SESSION_STORE` | `memory` | `memory` keeps history in the process, so run one replica. `firestore` needs the `cloud` extra, `GOOGLE_CLOUD_PROJECT` and Google credentials. |
| `RAG_INDEX_DIR` | `/app/data/paper_index` | Passage index location. |
| `CBIO_MAX_TOOL_CALLS` | `20` | Per-turn tool-call cap in Agentic mode. |
| `PORT` | `8080` | Listen port. |

The service has no health route; probe the TCP port. On Kubernetes, start
from [`deploy/k8s/chat.yaml`](../deploy/k8s/chat.yaml).

**Cloud Run (original deploy).** The `cloud-run` job builds
`docker/chat.Dockerfile` with Cloud Build
(`deploy/cloudrun/cloudbuild-chat.yaml`), pushes it to Artifact Registry and
runs `gcloud run deploy` with `SESSION_STORE=firestore` and the Anthropic
key from Secret Manager. It needs an Artifact Registry repository, the
Secret Manager secret, a Firestore database and a service-account key
(`GCP_SA_KEY`) allowed to submit builds and deploy the service. The
one-time setup is in the header of
[`deploy/cloudrun/deploy-chat.sh`](../deploy/cloudrun/deploy-chat.sh),
which runs the same steps by hand. The GHCR image is built separately by the
`image` job, so Cloud Run and GHCR hold two builds of the same Dockerfile at
the same commit.

### MCP server

```bash
docker run --rm -p 8124:8124 \
  -v "$PWD/data/paper_index:/app/data/paper_index:ro" \
  ghcr.io/<owner>/cbio-kb-mcp:main
curl -s localhost:8124/health
```

Configuration and client setup are in [mcp.md](mcp.md). For Kubernetes,
[`deploy/k8s/mcp.yaml`](../deploy/k8s/mcp.yaml) serves it at
`https://<host>/lit/mcp` and does three things:

- sets `CBIO_KB_MCP_HTTP_PATH=/lit/mcp`, so the server answers on the
  prefixed path itself and the Ingress needs no rewrite. This is the same
  shape as `https://mcp.cbioportal.org/db/mcp`;
- sets `CBIO_KB_MCP_FORWARDED_ALLOW_IPS=*`, so redirects keep `https`
  behind the TLS-terminating ingress;
- sets `FASTMCP_STATELESS_HTTP=true`, so any replica can answer any
  request. Without it, FastMCP ties each client session to one pod.

`/health` stays at the pod root; the probes use it directly. Clients then
connect with, e.g.,
`claude mcp add --transport http cbio-kb https://<host>/lit/mcp`.

Neither service authenticates callers. The MCP tools are read-only, but
`search_agentic` (on when `ANTHROPIC_API_KEY` is set) and every chat turn
spend Anthropic tokens. If the endpoints are public, put authentication or
rate limiting at the ingress. cBioPortal's hosted MCP server uses Google
OAuth.

## Handover checklist (e.g. MSK, no Google Cloud)

1. **Move the repo** (transfer or fork). No workflow needs secrets to go
   green:
   - the `cloud-run` job skips itself outside `jim-bo/cbio-kb` until
     `GCP_PROJECT_ID` is set;
   - Docker Hub is skipped without its secrets;
   - GHCR images publish under the new owner on the next image build (a
     push to `main` that touches image paths, or Actions > Run workflow).
2. **Images.** After the first build, check the two GHCR packages
   (`cbio-kb-mcp`, `cbio-kb-chat`). Make them public, or create an image
   pull secret for the cluster. Pin deployments to `:sha-<short>` or a
   release tag (`git tag v1.0.0 && git push --tags` produces `:1.0.0`).
3. **Passage index.**
   1. Build it with `cbio-kb index build-papers` and `build-bm25`.
   2. Package it with `scripts/package_index.sh` and upload the tarball.
   3. To bake it into the images, set `PAPER_INDEX_URL` and
      `PAPER_INDEX_SHA256`, then re-run `mcp-server.yml` and `chat-api.yml`
      (Actions > Run workflow). Otherwise mount it (see
      [Passage index](#passage-index)).
   4. Make sure `EMBED_MODEL` in the Dockerfiles matches the index's
      `embed_model`.
4. **MCP server on Kubernetes.** Adapt `deploy/k8s/mcp.yaml` to your layout
   (e.g. knowledgesystems-k8s-deployment): the image, the host, the ingress
   class and TLS secret, and the `/lit/mcp` path next to `/db/mcp`. Leave
   `ANTHROPIC_API_KEY` unset unless you want `search_agentic`.
5. **Chat API** (only if you want the `/ask` page):
   1. Create a Secret holding the Anthropic key.
   2. Adapt `deploy/k8s/chat.yaml`; keep one replica.
   3. Set `CHAT_CORS_ORIGINS` to the site's origin.
6. **Website.** Either keep GitHub Pages and set `CHAT_API_URL`, or host
   `wiki/_site/` yourself: set `PUBLISH_GH_PAGES=false` and serve the `site`
   artifact or a local render. Without a chat API the rest of the site works
   and only `/ask` fails.
7. **Remove Google Cloud** if unused:
   - delete the `cloud-run` job from `chat-api.yml`, `deploy/cloudrun/`, and
     the `GCP_SA_KEY` / `CHAT_CORS_ORIGINS` secrets;
   - the Firestore session store (`ai_search/sessions.py`, the `cloud`
     extra) is harmless when unused, since `SESSION_STORE` defaults to
     `memory`.
8. **Replace the original maintainer's identifiers** (next section).
9. **Branch protection:** require the `test` check only.

## Values still tied to the original maintainer

Everything below is either overridable or cosmetic, and nothing breaks if
it stays. Change them after the handover.

| Where | Value | Effect | Change |
|---|---|---|---|
| `wiki/ask-config.js` | the Cloud Run URL `cbio-kb-api-7vd2hab3va-uc.a.run.app` | Where `/ask` posts unless `CHAT_API_URL` is set | Set `CHAT_API_URL` or edit the file |
| `.github/workflows/chat-api.yml` | `github.repository == 'jim-bo/cbio-kb'` fallback to `cbioportal-python`, `us-central1`, `cbio-kb-api` | Keeps the original deploy working with no variables set; inert elsewhere | Delete the fallback when that deploy is retired |
| `deploy/cloudrun/deploy-chat.sh` | `PROJECT_ID` and CORS defaults | Manual script only | Pass `PROJECT_ID=` / `CHAT_CORS_ORIGINS=` |
| `ai_search/app.py` | default `CHAT_CORS_ORIGINS` includes `https://jim-bo.github.io` | Only when the env var is unset | Set `CHAT_CORS_ORIGINS`, or edit the default |
| `ai_search/mcp.py` | `website_url="https://jim-bo.github.io/cbio-kb/"` | Link advertised to MCP clients | Edit |
| `wiki/_quarto.yml` | `repo-url: https://github.com/jim-bo/cbio-kb` | "Edit"/"source" links on every page | Edit |
| `schema/templates/index.md` (regenerates `wiki/index.md`), `wiki/experiments/rag-vs-agentic.qmd`, `eval/*.md`, `README.md` | links to `github.com/jim-bo/cbio-kb` and `jim-bo.github.io/cbio-kb` | Links | Search and replace; run `cbio-kb wiki build-index` |

## Known gaps

- **Image size.** On both amd64 and arm64, `torch` from PyPI pulls in the
  CUDA libraries (`nvidia-*` ~3 GB, `triton` ~0.7 GB), so each image is
  about 6.4 GB. Nothing here uses a GPU. Pointing `torch` at the CPU wheel
  index (`[tool.uv.sources]` in `pyproject.toml`) would cut roughly 4 GB.
  The image workflows free runner disk space before building because of
  this.
- **Chat sessions** can only be shared across replicas through Firestore.
  A Redis or Postgres `SessionStore` (see `ai_search/sessions.py`) would
  remove that last GCP-shaped dependency.
