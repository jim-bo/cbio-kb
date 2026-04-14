// Wiki traversal visualization for /ask. Renders a top-down hierarchical
// tree of the wiki vault (index → section → entity) and lights up nodes
// as the agent reads them via tool calls. Cross-link edges are revealed
// on hover so the structural tree stays readable at rest.
//
// Public API exposed on window.AskGraph:
//   markVisited(path, turnIndex)  — paint a node, draw a traversal arc
//                                   from the prior visit in the same turn
//   startTurn(turnIndex)          — demote the previous turn's "current" styling
//   reset()                       — clear visit state
//   fit()                         — restore the default zoom transform
//
// The graph manifest is fetched from `graph.json` (sibling file). Build
// it with: `uv run cbio-kb wiki build-graph`.

(function() {
    const PALETTE = ['#4c78a8', '#f58518', '#54a24b', '#e45756',
                     '#72b7b2', '#eeca3b', '#b279a2'];

    let graph = null;
    let svg = null, gView = null, gTree = null, gCross = null, gNodes = null;
    let zoom = null;
    let popupListenersInstalled = false;
    let canvasEl = null;
    const nodesByPath = new Map();
    const nodeElements = new Map();
    // Sections are collapsed by default; expansion is sticky for the
    // page-life session. A section expands automatically on the first
    // `markVisited` into one of its children, or when the user clicks
    // the section node directly.
    const expandedSections = new Set();

    // Visit state — accumulates across all turns of the page-life session.
    const visited = new Set();
    const visitCount = new Map();
    const lastVisitedByTurn = new Map();
    let currentTurn = 0;

    // Cross-edge adjacency — populated after fetch, used on hover.
    const outgoing = new Map();
    const incoming = new Map();
    const sectionColors = new Map();

    async function init() {
        const canvas = document.getElementById('graph-canvas');
        if (!canvas) return;

        // Wait briefly for d3 — on slow mobile connections it can land
        // after ask-graph.js even though it's in <head>. Fail loud if it
        // never shows up, rather than leaving the "Loading…" stub.
        try {
            await waitFor(function() { return typeof d3 !== 'undefined'; }, 5000);
        } catch (_err) {
            canvas.innerHTML = '<p class="empty-state">' +
                'Graph library (D3) failed to load. ' +
                'Check the network or ad/script blockers and reload.' +
                '</p>';
            console.error('[ask-graph] d3 unavailable after 5s');
            return;
        }

        try {
            const res = await fetch('graph.json', {cache: 'no-cache'});
            if (!res.ok) throw new Error('HTTP ' + res.status);
            graph = await res.json();
        } catch (err) {
            canvas.innerHTML = '<p class="empty-state">Failed to load graph: ' +
                               err.message + '</p>';
            console.error('[ask-graph] graph.json fetch failed', err);
            return;
        }

        try {
            indexGraph();
            render(canvas);
        } catch (err) {
            canvas.innerHTML = '<p class="empty-state">Graph render error: ' +
                               err.message + '</p>';
            console.error('[ask-graph] render failed', err);
        }
    }

    function waitFor(predicate, timeoutMs) {
        return new Promise(function(resolve, reject) {
            if (predicate()) { resolve(); return; }
            const started = Date.now();
            const iv = setInterval(function() {
                if (predicate()) { clearInterval(iv); resolve(); }
                else if (Date.now() - started > timeoutMs) {
                    clearInterval(iv); reject(new Error('timeout'));
                }
            }, 80);
        });
    }

    function indexGraph() {
        graph.sections.forEach(function(s, i) {
            sectionColors.set(s.id, PALETTE[i % PALETTE.length]);
        });
        for (const e of graph.cross_edges) {
            if (!outgoing.has(e.from)) outgoing.set(e.from, []);
            outgoing.get(e.from).push(e.to);
            if (!incoming.has(e.to)) incoming.set(e.to, []);
            incoming.get(e.to).push(e.from);
        }
    }

    function buildHierarchy() {
        const childrenBySection = new Map();
        for (const n of graph.nodes) {
            if (!childrenBySection.has(n.section)) {
                childrenBySection.set(n.section, []);
            }
            childrenBySection.get(n.section).push({
                id: n.id, label: n.label, title: n.title,
                section: n.section, kind: 'entity',
            });
        }
        return {
            id: graph.root.id, label: graph.root.label, kind: 'root',
            children: graph.sections.map(function(s) {
                const isExpanded = expandedSections.has(s.id);
                return {
                    id: s.id, label: s.label, count: s.count,
                    kind: 'section', section: s.id,
                    expanded: isExpanded,
                    children: isExpanded ? (childrenBySection.get(s.id) || []) : [],
                };
            }),
        };
    }

    function rerender() {
        if (!canvasEl) return;
        render(canvasEl);
        replayVisits();
    }

    function replayVisits() {
        // Re-apply node + tree-edge state after a re-layout (e.g. a
        // section collapse/expand). `paintNode` / `paintAncestor` /
        // `paintTreeEdge` are idempotent.
        for (const [path, cnt] of visitCount) {
            paintNode(path, cnt);
            const leaf = nodesByPath.get(path);
            if (!leaf) continue;
            let cursor = leaf;
            while (cursor.parent) {
                paintAncestor(cursor.parent.data.id);
                paintTreeEdge(cursor.parent.data.id, cursor.data.id, currentTurn);
                cursor = cursor.parent;
            }
        }
    }

    function toggleSection(sectionId) {
        if (expandedSections.has(sectionId)) expandedSections.delete(sectionId);
        else expandedSections.add(sectionId);
        rerender();
    }

    function expandSection(sectionId) {
        if (expandedSections.has(sectionId)) return false;
        expandedSections.add(sectionId);
        return true;
    }

    function render(canvas) {
        canvasEl = canvas;
        canvas.innerHTML = '';
        const root = d3.hierarchy(buildHierarchy());
        root.sort(function(a, b) {
            return d3.ascending(a.data.label, b.data.label);
        });

        // Horizontal (left→right) tree: the 305-leaf axis runs vertically
        // so the graph ends up taller than wide, matching the shape of the
        // glass-panel viewport.
        //   dx = leaf-to-leaf vertical spacing
        //   dy = level-to-level horizontal spacing
        // After layout, d3 exposes a node's position along the spread axis
        // as `d.x` and its depth as `d.y`; we plot `(d.y, d.x)` so depth
        // becomes the horizontal coordinate.
        const dx = 16;
        const dy = 200;
        d3.tree().nodeSize([dx, dy])(root);

        let xMin = Infinity, xMax = -Infinity;
        root.each(function(d) {
            if (d.x < xMin) xMin = d.x;
            if (d.x > xMax) xMax = d.x;
        });
        const leftPad = 160;   // room for root + section labels on the left
        const rightPad = 60;
        const yMax = root.height * dy;
        const width  = yMax + leftPad + rightPad;
        const height = (xMax - xMin) + 60;

        svg = d3.select(canvas).append('svg')
            .attr('class', 'graph-svg')
            .attr('width', '100%').attr('height', '100%')
            .attr('viewBox', [-leftPad, xMin - 30, width, height])
            .attr('preserveAspectRatio', 'xMidYMid meet');

        gView = svg.append('g').attr('class', 'graph-view');

        gTree   = gView.append('g').attr('class', 'tree-links');
        gCross  = gView.append('g').attr('class', 'cross-links');
        gNodes  = gView.append('g').attr('class', 'nodes');

        const linkGen = d3.linkHorizontal()
            .x(function(d) { return d.y; })
            .y(function(d) { return d.x; });
        gTree.selectAll('path')
            .data(root.links())
            .join('path')
            .attr('class', 'tree-link')
            .attr('data-from', function(d) { return d.source.data.id; })
            .attr('data-to', function(d) { return d.target.data.id; })
            .attr('d', linkGen);

        nodesByPath.clear();
        nodeElements.clear();
        root.descendants().forEach(function(d) {
            nodesByPath.set(d.data.id, d);
        });

        const nodeGroups = gNodes.selectAll('g.node')
            .data(root.descendants())
            .join('g')
            .attr('class', function(d) { return 'node node-' + d.data.kind; })
            .attr('data-id', function(d) { return d.data.id; })
            .attr('transform', function(d) {
                return 'translate(' + d.y + ',' + d.x + ')';
            });

        nodeGroups.append('circle')
            .attr('r', baseRadius)
            .attr('fill', function(d) {
                if (d.data.kind === 'root') return '#444';
                return sectionColors.get(d.data.section);
            });

        nodeGroups.append('title')
            .text(function(d) {
                if (d.data.kind === 'entity') {
                    return d.data.id + '\n' + (d.data.title || '');
                }
                if (d.data.kind === 'section') {
                    return d.data.label + ' (' + d.data.count + ')';
                }
                return d.data.label;
            });

        nodeGroups.filter(function(d) { return d.data.kind === 'section'; })
            .append('text')
            .attr('class', 'section-label')
            .attr('x', -10)
            .attr('dy', '0.32em')
            .attr('text-anchor', 'end')
            .text(function(d) {
                const chevron = d.data.expanded ? '▾' : '▸';
                return chevron + ' ' + d.data.label + ' (' + d.data.count + ')';
            });

        nodeGroups.filter(function(d) { return d.data.kind === 'root'; })
            .append('text')
            .attr('class', 'root-label')
            .attr('x', -14)
            .attr('dy', '0.32em')
            .attr('text-anchor', 'end')
            .text(function(d) { return d.data.label; });

        nodeGroups.filter(function(d) { return d.data.kind === 'entity'; })
            .on('mouseenter', function(_event, d) { showCrossEdges(d); })
            .on('mouseleave', function() { hideCrossEdges(); });

        nodeGroups.on('click', function(event, d) {
            event.stopPropagation();
            if (d.data.kind === 'section') {
                toggleSection(d.data.id);
                return;
            }
            showNodePopup(d, this);
        });

        nodeGroups.each(function(d) { nodeElements.set(d.data.id, this); });

        zoom = d3.zoom()
            .scaleExtent([0.2, 12])
            .on('zoom', function(ev) { gView.attr('transform', ev.transform); });
        svg.call(zoom);

        // Replay any visits that arrived before the graph finished loading.
        for (const path of visited) {
            paintNode(path, visitCount.get(path) || 1);
        }
    }

    function baseRadius(d) {
        if (d.data.kind === 'root')    return 9;
        if (d.data.kind === 'section') return 6;
        return 3;
    }

    function showCrossEdges(d) {
        const id = d.data.id;
        const out = outgoing.get(id) || [];
        const inn = incoming.get(id) || [];
        const edges = [];
        for (const t of out) edges.push({from: id, to: t});
        for (const s of inn) edges.push({from: s, to: id});
        const peerSet = new Set([id].concat(out, inn));

        const linkGen = d3.linkHorizontal().x(function(p) { return p.y; })
                                           .y(function(p) { return p.x; });
        gCross.selectAll('path')
            .data(edges)
            .join('path')
            .attr('class', 'cross-link')
            .attr('d', function(e) {
                const a = nodesByPath.get(e.from);
                const b = nodesByPath.get(e.to);
                if (!a || !b) return null;
                return linkGen({source: a, target: b});
            });

        gNodes.selectAll('g.node-entity')
            .classed('dim', function(n) { return !peerSet.has(n.data.id); });
        gNodes.selectAll('g.node-section')
            .classed('dim', function(n) {
                // Highlight only the hovered node's section + sections
                // containing any peer.
                if (n.data.section === d.data.section) return false;
                for (const p of peerSet) {
                    const peer = nodesByPath.get(p);
                    if (peer && peer.data.section === n.data.section) return false;
                }
                return true;
            });
    }

    function hideCrossEdges() {
        if (gCross) gCross.selectAll('path').remove();
        if (gNodes) {
            gNodes.selectAll('g.node-entity').classed('dim', false);
            gNodes.selectAll('g.node-section').classed('dim', false);
        }
    }

    function sectionSingular(section) {
        const map = {
            papers: 'paper', genes: 'gene', cancer_types: 'cancer type',
            datasets: 'dataset', drugs: 'drug', methods: 'method', themes: 'theme',
        };
        return map[section] || section;
    }

    function removePopup() {
        var canvas = document.getElementById('graph-canvas');
        if (!canvas) return;
        var existing = canvas.querySelector('.graph-popup');
        if (existing) existing.remove();
    }

    function showNodePopup(d, nodeEl) {
        var canvas = document.getElementById('graph-canvas');
        if (!canvas) return;

        // Remove any existing popup.
        removePopup();

        // Build popup element.
        var popup = document.createElement('div');
        popup.className = 'graph-popup';

        // Header row.
        var header = document.createElement('div');
        header.className = 'graph-popup-header';

        var labelEl = document.createElement('span');
        labelEl.className = 'graph-popup-label';
        labelEl.textContent = d.data.label || d.data.id;

        var closeBtn = document.createElement('button');
        closeBtn.className = 'graph-popup-close';
        closeBtn.setAttribute('aria-label', 'Close');
        closeBtn.textContent = '✕';
        closeBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            removePopup();
        });

        header.appendChild(labelEl);
        header.appendChild(closeBtn);
        popup.appendChild(header);

        // Meta line.
        var meta = document.createElement('div');
        meta.className = 'graph-popup-meta';
        if (d.data.kind === 'entity') {
            meta.textContent = sectionSingular(d.data.section);
        } else if (d.data.kind === 'section') {
            meta.textContent = (d.data.count || 0) + ' pages';
        } else {
            meta.textContent = 'Wiki index';
        }
        popup.appendChild(meta);

        // Title (entity only).
        if (d.data.kind === 'entity' && d.data.title) {
            var titleEl = document.createElement('p');
            titleEl.className = 'graph-popup-title';
            titleEl.textContent = d.data.title;
            popup.appendChild(titleEl);
        }

        // Action link.
        var href;
        if (d.data.kind === 'entity') {
            href = d.data.id.replace(/\.md$/, '.html');
        } else if (d.data.kind === 'section') {
            href = d.data.id + '/index.html';
        } else {
            href = 'index.html';
        }
        var link = document.createElement('a');
        link.className = 'graph-popup-link';
        link.href = href;
        link.target = '_blank';
        link.rel = 'noopener';
        link.textContent = 'Open page ↗';
        popup.appendChild(link);

        // Position the popup near the clicked node.
        var canvasRect = canvas.getBoundingClientRect();
        var nodeRect = nodeEl.getBoundingClientRect ? nodeEl.getBoundingClientRect() :
            (nodeEl.getBBox ? (function() {
                var b = nodeEl.getBBox();
                var ctm = nodeEl.getScreenCTM();
                return {
                    left: ctm.e + b.x,
                    top: ctm.f + b.y,
                    right: ctm.e + b.x + b.width,
                    bottom: ctm.f + b.y + b.height,
                    width: b.width,
                    height: b.height,
                };
            })() : canvasRect);

        var POPUP_W = 260;
        var POPUP_H = 160; // estimated
        var MARGIN = 8;

        // Horizontal: prefer right of node, fall back to left.
        var nodeRight = nodeRect.right - canvasRect.left;
        var nodeLeft = nodeRect.left - canvasRect.left;
        var left;
        if (nodeRight + POPUP_W + MARGIN <= canvasRect.width) {
            left = nodeRight + MARGIN;
        } else {
            left = nodeLeft - POPUP_W - MARGIN;
        }
        left = Math.max(MARGIN, left);

        // Vertical: center on node, clamp to canvas.
        var nodeMidY = (nodeRect.top + nodeRect.bottom) / 2 - canvasRect.top;
        var top = nodeMidY - POPUP_H / 2;
        top = Math.max(MARGIN, Math.min(top, canvasRect.height - POPUP_H - MARGIN));

        popup.style.left = left + 'px';
        popup.style.top = top + 'px';

        canvas.appendChild(popup);

        // Install global listeners once.
        if (!popupListenersInstalled) {
            popupListenersInstalled = true;

            document.addEventListener('click', function(ev) {
                var popupEl = document.querySelector('#graph-canvas .graph-popup');
                if (!popupEl) return;
                if (!popupEl.contains(ev.target) && !ev.target.closest('g.node')) {
                    removePopup();
                }
            });

            document.addEventListener('keydown', function(ev) {
                if (ev.key === 'Escape') removePopup();
            });
        }
    }

    function fit() {
        if (!svg || !zoom) return;
        svg.transition().duration(300)
           .call(zoom.transform, d3.zoomIdentity);
    }

    function markVisited(path, turnIndex) {
        if (typeof turnIndex === 'number') currentTurn = turnIndex;
        const cnt = (visitCount.get(path) || 0) + 1;
        visitCount.set(path, cnt);
        visited.add(path);
        lastVisitedByTurn.set(currentTurn, path);

        // Auto-expand the containing section so the visited leaf becomes
        // visible. The section is inferred from the vault-relative path
        // (first segment). `expandSection` re-renders if it flipped,
        // after which we fall through to paint the newly-rendered node.
        const section = typeof path === 'string' ? path.split('/')[0] : null;
        if (section && !expandedSections.has(section)) {
            // Only auto-expand if this section actually exists in the
            // graph; otherwise we'd trigger a pointless re-render.
            const known = graph && graph.sections && graph.sections.some(function(s) {
                return s.id === section;
            });
            if (known) {
                expandSection(section);
                rerender();
            }
        }

        paintNode(path, cnt);

        // Light up the ancestor chain: tool calls only name leaves, so
        // without this the Index + section nodes stay dark and the viz
        // looks like activity on disconnected leaves. Walk d3's parent
        // pointers and paint every ancestor + the tree edges that
        // connect them.
        const leaf = nodesByPath.get(path);
        if (leaf) {
            let cursor = leaf;
            while (cursor.parent) {
                const parentId = cursor.parent.data.id;
                const childId  = cursor.data.id;
                paintAncestor(parentId);
                paintTreeEdge(parentId, childId, currentTurn);
                cursor = cursor.parent;
            }
        }

        bumpVisitedBadge();
    }

    function paintAncestor(path) {
        const el = nodeElements.get(path);
        if (!el) return;
        const sel = d3.select(el);
        sel.classed('visited', true).classed('current-turn', true);
        sel.select('circle').transition().duration(150).attr('opacity', 0.5)
           .transition().duration(300).attr('opacity', 1);
    }

    function paintTreeEdge(fromId, toId, turn) {
        if (!gTree) return;
        const path = gTree.select(
            'path[data-from="' + cssEscape(fromId) + '"][data-to="' + cssEscape(toId) + '"]'
        );
        if (path.empty()) return;
        path.classed('traversed', true)
            .classed('turn-current', true)
            .classed('turn-past', false)
            .attr('data-turn', String(turn));
    }

    function cssEscape(s) {
        // CSS attribute-selector escaping for the forward slash in paths
        // like `papers/12345.md`. Backslash-escape anything non-alnum.
        return String(s).replace(/[^a-zA-Z0-9_\-]/g, function(ch) {
            return '\\' + ch;
        });
    }

    function paintNode(path, cnt) {
        const el = nodeElements.get(path);
        if (!el) return;
        const sel = d3.select(el);
        sel.classed('visited', true).classed('current-turn', true);
        const circle = sel.select('circle');
        circle.attr('r', 4 + Math.min(cnt, 4));
        circle.transition().duration(180).attr('opacity', 0.45)
              .transition().duration(360).attr('opacity', 1);
    }

    function startTurn(turnIndex) {
        currentTurn = turnIndex;
        if (gNodes) {
            gNodes.selectAll('g.node.current-turn').classed('current-turn', false);
        }
        if (gTree) {
            gTree.selectAll('path.traversed.turn-current')
                .classed('turn-current', false)
                .classed('turn-past', true);
        }
    }

    function reset() {
        visited.clear();
        visitCount.clear();
        lastVisitedByTurn.clear();
        currentTurn = 0;
        if (gNodes) {
            gNodes.selectAll('g.node')
                .classed('visited', false)
                .classed('current-turn', false);
            gNodes.selectAll('g.node circle').attr('r', baseRadius);
        }
        if (gTree) {
            gTree.selectAll('path.traversed')
                .classed('traversed', false)
                .classed('turn-current', false)
                .classed('turn-past', false);
        }
        bumpVisitedBadge();
    }

    function bumpVisitedBadge() {
        const badge = document.getElementById('graph-visited-count');
        if (badge) badge.textContent = visited.size ? String(visited.size) : '';
    }

    function attachToolbar() {
        const fitBtn = document.getElementById('graph-fit-btn');
        if (fitBtn) fitBtn.addEventListener('click', fit);
        const resetBtn = document.getElementById('graph-reset-btn');
        if (resetBtn) resetBtn.addEventListener('click', reset);
        // Re-fit when the Graph tab is activated, in case the pane was
        // hidden during initial render and the SVG measured at zero.
        document.addEventListener('click', function(e) {
            const tab = e.target.closest('.drawer-tab');
            if (tab && tab.dataset.drawerPane === 'graph-pane') {
                setTimeout(fit, 50);
            }
        });
    }

    window.AskGraph = {
        markVisited: markVisited,
        startTurn: startTurn,
        reset: reset,
        fit: fit,
    };

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            attachToolbar();
            init();
        });
    } else {
        attachToolbar();
        init();
    }
})();
