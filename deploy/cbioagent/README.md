# cbio-kb on chat.cbioportal.org

Draft changes to
[knowledgesystems/knowledgesystems-k8s-deployment](https://github.com/knowledgesystems/knowledgesystems-k8s-deployment)
that run the cbio-kb literature MCP server next to cBioPortal's database and
navigator MCP servers and give the cBioPortalChat agent its tools. Nothing
here has been applied to that repo or the cluster. The patches were generated
against its `master` at `f08b829` and pass `git apply --check` there.

## The patches

Paths are relative to `argocd/aws/203403084713/clusters/cbioportal-prod/apps/`.

| Patch | File | Change |
|---|---|---|
| `1-cbio-kb-mcp.patch` | `cbioagent/cbio-kb-mcp.yaml` (new) | Deployment + ClusterIP Service `cbio-kb-mcp`, serving MCP at `/lit/mcp`. A copy of [`deploy/k8s/mcp.yaml`](../k8s/mcp.yaml). The `cbioagent` Argo app syncs the directory recursively, so the file deploys on merge. |
| `2-librechat-config-beta.patch` | `cbioagent-beta/librechat-config.yaml` | Adds `cbio-kb-mcp` to `mcpSettings.allowedDomains` and an MCP server `cbioportal-literature` at `http://cbio-kb-mcp:80/lit/mcp`. |
| `3-librechat-config-prod.patch` | `cbioagent/librechat-config.yaml` | The same for prod. |
| `4-mcp-ingress-lit.patch` | `cbioagent/mcp-ingress.yaml` | A `ratelimit-lit` Middleware and a `/lit` Ingress, making `https://mcp.cbioportal.org/lit/mcp` public. LibreChat doesn't need it. |

From the root of a knowledgesystems-k8s-deployment checkout:

```bash
git apply --check /path/to/cbio-kb/deploy/cbioagent/1-cbio-kb-mcp.patch
git apply /path/to/cbio-kb/deploy/cbioagent/1-cbio-kb-mcp.patch
```

If `master` has moved on and a patch no longer applies, the changes are
small enough to make by hand from the patch text.

Patch 1 must stay a copy of `deploy/k8s/mcp.yaml`. After editing the
manifest, regenerate the patch from the root of a knowledgesystems checkout:

```bash
f=argocd/aws/203403084713/clusters/cbioportal-prod/apps/cbioagent/cbio-kb-mcp.yaml
cp /path/to/cbio-kb/deploy/k8s/mcp.yaml "$f"
git diff --no-index /dev/null "$f" > /path/to/cbio-kb/deploy/cbioagent/1-cbio-kb-mcp.patch
rm "$f"
```

Choices in the LibreChat entry:

- **Server name `cbioportal-literature`**, the same on beta and prod.
  LibreChat stores agent tools as `<tool>_mcp_<server>`, so one name lets the
  prod agent reuse beta's tool list. Renaming the server later breaks the
  agents' tool references.
- **No trailing slash.** `/lit/mcp` is canonical; `/lit/mcp/` gets a 307,
  which LibreChat doesn't follow. This matches prod's `cbioportal-database`
  entry. Beta's `cbioportal-database` entry uses `/db/mcp/`, with a comment
  saying the slash avoids the 307; for cbio-kb the slash is what triggers it
  (checked locally).
- **`chatMenu: false`**, like the navigator. The tools stay available to
  agents that list them but don't show in the chat's MCP picker. Users reach
  them through cBioPortalChat, whose prompt says when to use literature
  tools rather than data tools. Merging the config therefore changes nothing
  users can see until the agent is updated.
- **User headers** (`x-user-id`, `x-user-email`) are copied from the other
  entries for consistency. cbio-kb ignores them and logs nothing per user;
  dropping them is fine.

## Before the first deploy (cbio-kb side)

As of 2026-09-16, neither of these is done:

1. **Publish a pullable image.** Push cbio-kb `main` so `mcp-server.yml`
   publishes `ghcr.io/jim-bo/cbio-kb-mcp:main`, then make the GHCR package
   public. A private package needs an imagePullSecret on the Deployment,
   which Keel also uses to poll.
2. **Bake in the passage index.** Build and package it
   (`scripts/package_index.sh`), upload the tarball (a GitHub Release asset
   works), set the `PAPER_INDEX_URL` and `PAPER_INDEX_SHA256` repository
   variables, then re-run `mcp-server.yml` from the Actions tab. Changing a
   variable doesn't trigger a build on its own. Without the index the pod
   still runs: the wiki tools work, the search tools report the missing
   index, and `/health` shows `"passage_index": false`.

## Rollout: beta first

1. **Deploy the server and wire up beta.** Merge patches 1 and 2. Argo syncs
   `cbioagent` automatically. `cbioagent-beta` has no automated sync policy,
   so sync it by hand. Reloader restarts beta LibreChat when its ConfigMap
   changes.
2. **Check the pod.**
   ```bash
   kubectl -n default rollout status deploy/cbio-kb-mcp
   kubectl -n default port-forward svc/cbio-kb-mcp 8124:80 &
   curl -s localhost:8124/health   # {"status":"ok",...,"passage_index":true}
   ```
3. **Give the beta agent the tools** (`cBioPortalChatBeta`,
   `agent_OHVSJI9Gd6gwsDnFSL-Xl`). This is manual, like other agent changes.
   Either open the agent in the Agent Builder as an ADMIN and add tools from
   the `cbioportal-literature` server (`chatMenu: false` hides it from the
   chat picker only, not from agents), or patch the agent document in
   MongoDB the way the root `CLAUDE.md` describes: add
   `<tool>_mcp_cbioportal-literature` entries to `tools` and
   `cbioportal-literature` to `mcpServerNames`. See
   [Tools](#which-tools-to-attach) for which tools, and
   [Agent prompt](#agent-prompt) for the prompt text.
4. **Test on beta.chat.cbioportal.org**, for example with the
   [starters below](#proposed-conversation-starters), plus a question that
   needs both data and literature ("How often is KRAS mutated in lung
   adenocarcinoma on cBioPortal, and what have published studies found about
   it?").
5. **Promote to prod.** Merge patch 3 first (on its own it changes nothing
   users can see), then copy the tool list and prompt change to the prod
   agent `agent_9ZXhcwLIsROBQX0u4JS5F`.
6. **Public endpoint (optional, independent).** Merge patch 4. Then:
   ```bash
   curl -si -X POST https://mcp.cbioportal.org/lit/mcp/ | grep -i location   # https://mcp.cbioportal.org/lit/mcp
   claude mcp add --transport http cbioportal-literature https://mcp.cbioportal.org/lit/mcp
   ```

### Which tools to attach

Every attached tool's schema is sent with each agent turn. All ten come to
about 9 KB of JSON (roughly 2,300 tokens).

| Tool | Attach? | |
|---|---|---|
| `get_study_papers` | yes | study ID -> the paper(s) behind it and the corpus papers that used its cohort |
| `get_paper` | yes | a paper's metadata, study IDs and selected sections |
| `list_papers` | yes | filter papers by gene, cancer type, drug, study, year |
| `get_entity` | yes | gene / cancer type / drug / method page and the papers citing it |
| `search_hybrid` | yes | passage search over the papers (needs the index) |
| `corpus_info` | yes | coverage and snapshot date, so the agent can say what's missing |
| `read_wiki_page` | optional | follow links from `get_entity` / `get_paper` output |
| `search_auto` | optional | router over `search_hybrid`; mostly useful to clients without their own planning |
| `search_dense`, `route_query` | no | covered by `search_hybrid` and by the agent's own planning |

`search_agentic` isn't registered, because the pod has no
`ANTHROPIC_API_KEY`.

### Agent prompt

cbio-kb publishes server instructions (about 2,600 characters: when to use
it rather than the database or navigator, shared identifiers, citation
rules). There are two ways to get them to the agent:

- add `serverInstructions: true` to the `cbioportal-literature` entry, so
  LibreChat appends the server's own text and it stays in step with cbio-kb
  releases; or
- add a paragraph like this to the agent's instructions in MongoDB:

  > **Literature (`cbioportal-literature` tools).** Use these for what
  > published studies found: the paper behind a cBioPortal study, how its
  > cohort was built, and what the literature says about a gene, drug, cancer
  > type or method. They take the same study IDs, HUGO symbols and OncoTree
  > codes as the database tools. Start from `get_study_papers` for a study,
  > `get_entity` for a gene/drug/cancer type, or `search_hybrid` for an open
  > question, then `get_paper` for detail. Cite every literature claim with
  > its PMID. Numbers from a paper describe its cohort at publication; never
  > present them as current cBioPortal counts, which come from the database
  > tools.

The patches do neither, so the agent's context is unchanged until you
choose.

### Proposed conversation starters

Not in the patches. Once the prod agent has the tools, a fourth category
under `conversationStarterCategories` in prod's `modelSpecs` could look like
this (the icon name follows prod's set; beta's icons are named differently):

```yaml
            - label: "Explore Literature"
              icon: "book-open"
              description: "Find what the publications behind cBioPortal studies reported."
              starters:
                - "What did the MSK-IMPACT 2017 paper report about the mutational landscape of metastatic cancer?"
                - "What have published cBioPortal studies found about KRAS mutations in lung adenocarcinoma?"
                - "Which papers studied BRAF fusions, and what did they find?"
```

All three are covered by the current corpus (407 papers).

## How updates roll out

- **Code and wiki content.** A push to cbio-kb `main` that touches the image
  (server code, wiki markdown, seed data, ontology) makes `mcp-server.yml`
  push new `:main` and `:sha-<short>` tags. Keel polls GHCR (about once a
  minute) and rolls the Deployment when the `:main` digest changes. New
  papers reach chat this way with no change to knowledgesystems-k8s-deployment.
- **Passage index.** It's baked into the image, so a new index means
  uploading a new tarball, updating the two repository variables, and
  re-running `mcp-server.yml`. Keel then rolls the pod as above. The
  commented initContainer in `cbio-kb-mcp.yaml` is the alternative: it
  fetches the index at pod start, and each index change becomes an edit to
  that file.
- **Tool changes.** Tool names and arguments are stable. LibreChat reads the
  tool list when it connects to the server, so a cbio-kb release that adds
  or renames a tool needs a LibreChat restart and an agent update.
- **Pinning or rollback.** Point the image at `:sha-<short>`. With
  `keel.sh/match-tag: "true"`, Keel only follows that tag, which never moves.
- **Surge.** With one replica, a roll starts the new pod before stopping the
  old one, so the node briefly needs room for two memory requests. If the
  `cbioagent` pool is still a single node (#452) and that doesn't fit, the
  new pod stays Pending while the old one keeps serving. Setting
  `strategy.rollingUpdate` to `maxSurge: 0, maxUnavailable: 1` trades that
  for a few seconds of downtime per roll.

## Resources

The requests and limits in `cbio-kb-mcp.yaml` come from a local run of the
ONNX Runtime image (no PyTorch) with 407 papers:

| | Memory |
|---|---|
| warm: BM25, wiki graph, FAISS index, both models, router question bank | ~1.3 GiB |
| after 8 concurrent `search_hybrid` calls | ~2.0-2.2 GiB |

| `search_hybrid` latency | 1 call | concurrent |
|---|---|---|
| no CPU limit, `CBIO_ONNX_THREADS=2` (as in the manifest) | ~1.3 s | 8 calls: ~3.2 s each at worst |
| capped at 1 CPU | ~2 s | 4 calls: ~14 s each at worst |

A container sees every core on the node, and ONNX Runtime starts a thread
per core. Under a CPU limit the server sizes its thread pool to the limit
itself (it reads cgroup `cpu.max`; without that, 1 CPU took ~32 s per
search). The manifest sets no CPU limit, so it pins `CBIO_ONNX_THREADS=2`
instead to stay polite to neighbouring pods. LibreChat's default MCP
timeout is 30 s. The 1.5 Gi request is still more than beta LibreChat's
512 Mi, so check it fits the `cbioagent` node.

## Open decisions for the cBioPortal team

1. **Is `/lit` public, and how is it gated?** Patch 4 applies a per-IP rate
   limit only, which is our recommendation: the tools are read-only over
   published literature, with no database behind them and no LLM spend, and
   the limit keeps one client from tying up the reranker's CPU. Gating it
   with Google OAuth like `/db` would need OAuth support added to cbio-kb and
   a separate `-auth` Deployment, as `/db` has; neither exists today.
   Leaving patch 4 out keeps the server in-cluster only. Your call.
2. **Beta-first rollout** as above: patches 1-2 and the beta agent, then
   patch 3 and the prod agent after a soak. There is one Deployment for both,
   so beta and prod always see the same cbio-kb build. Staging cbio-kb
   releases on beta would need a second Deployment on another tag, like
   `cbioportal-navigator-beta`.
3. **Image owner and registry.** Today it is `ghcr.io/jim-bo/cbio-kb-mcp`, a
   personal account. The options are to keep it (made public), to move the
   repo under the cBioPortal org (`ghcr.io/cbioportal/cbio-kb-mcp`), or to
   publish to Docker Hub next to `cbioportal/mcp`. `mcp-server.yml` already
   pushes to Docker Hub for `v*` tags when `DOCKER_USERNAME` and
   `DOCKER_PASSWORD` are set, but not for `main`. Any of these is a one-line
   image change in `cbio-kb-mcp.yaml`.
4. **Other LibreChat instances.** An instance outside this cluster, such as
   the MSK-side one, would have to use the public URL. All of its users
   would then share one source IP and one `ratelimit-lit` bucket.

## Verified, and not

Verified locally with the current image, the manifest's environment and the
real index:

- `GET /health` returns 200 at the pod root about a second after start, and
  stays fast while the indexes load; `/lit/health` and `/mcp` return 404;
- `POST /lit/mcp` (initialize, `tools/list`, tool calls) returns 200 and the
  server logs `transport 'http' (stateless)`;
- `POST /lit/mcp/` with `X-Forwarded-Proto: https` returns 307 to
  `https://mcp.cbioportal.org/lit/mcp`;
- all four patches pass `git apply --check` on `f08b829` and apply together;
  the resulting `cbio-kb-mcp.yaml` is byte-identical to `deploy/k8s/mcp.yaml`,
  and every edited file, including the embedded `librechat.yaml`, parses.

Not verified, because it needs the cluster: server-side validation of the
manifests (the Traefik Middleware also needs its CRD), scheduling on the
`cbioagent` node, Keel's GHCR polling, and LibreChat connecting to the
server.
