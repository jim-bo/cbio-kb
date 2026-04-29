// Reusable tree-graph widget for the RAG-vs-agentic traversal explorer.
// Each call to `createExplorerGraph(container, graphData, options)` returns
// an independent instance with its own D3 selections, zoom, and paint
// state — unlike ask-graph.js which is a page-wide singleton. The
// instance exposes two paint modes:
//
//   • traversal — `markVisited(path, orderIdx)` lights up nodes in call
//     order and draws a dashed arc between successive visits, matching
//     the style of the /ask sidebar.
//   • intensity — `markIntensity(path, score, count)` sizes and tints a
//     node proportional to retrieval strength (color scale 0..maxScore,
//     radius scale 0..maxCount). Use `setIntensityRange(maxScore,
//     maxCount)` before issuing marks so paints are comparable across
//     the set.
//
// This module does not fetch graph.json; callers pass the parsed object
// in (the explorer page fetches it once and shares across both instances).

(function() {
    const PALETTE = ['#4c78a8', '#f58518', '#54a24b', '#e45756',
                     '#72b7b2', '#eeca3b', '#b279a2'];

    function createExplorerGraph(container, graphData, options) {
        options = options || {};
        const initialExpanded = new Set(options.initialExpanded || ['papers']);
        const mode = options.mode || 'traversal'; // 'traversal' | 'intensity'
        const accentColor = options.accentColor || '#e45756';

        // Per-instance state ----------------------------------------------
        let svg = null, gView = null, gTree = null, gNodes = null;
        let zoom = null;
        const nodesByPath = new Map();
        const nodeElements = new Map();
        const expandedSections = new Set(initialExpanded);
        const sectionColors = new Map();
        const visitOrder = []; // [{path, idx}]
        const visitedSet = new Set();
        let intensityMaxScore = 1;
        let intensityMaxCount = 1;
        const intensityByPath = new Map(); // path -> {score, count}

        // Index section colors ------------------------------------------
        graphData.sections.forEach(function(s, i) {
            sectionColors.set(s.id, PALETTE[i % PALETTE.length]);
        });

        function buildHierarchy() {
            const childrenBySection = new Map();
            for (const n of graphData.nodes) {
                if (!childrenBySection.has(n.section)) {
                    childrenBySection.set(n.section, []);
                }
                childrenBySection.get(n.section).push({
                    id: n.id, label: n.label, title: n.title,
                    section: n.section, kind: 'entity',
                });
            }
            return {
                id: graphData.root.id, label: graphData.root.label, kind: 'root',
                children: graphData.sections.map(function(s) {
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

        function render() {
            container.innerHTML = '';
            const root = d3.hierarchy(buildHierarchy());
            root.sort(function(a, b) { return d3.ascending(a.data.label, b.data.label); });

            const dx = 14;
            const dy = 180;
            d3.tree().nodeSize([dx, dy])(root);

            let xMin = Infinity, xMax = -Infinity;
            root.each(function(d) {
                if (d.x < xMin) xMin = d.x;
                if (d.x > xMax) xMax = d.x;
            });
            const leftPad = 150, rightPad = 40;
            const yMax = root.height * dy;
            const width = yMax + leftPad + rightPad;
            const height = (xMax - xMin) + 50;

            svg = d3.select(container).append('svg')
                .attr('class', 'ex-graph-svg')
                .attr('width', '100%').attr('height', '100%')
                .attr('viewBox', [-leftPad, xMin - 25, width, height])
                .attr('preserveAspectRatio', 'xMidYMid meet');

            gView = svg.append('g').attr('class', 'ex-view');
            gTree = gView.append('g').attr('class', 'ex-tree-links');
            gNodes = gView.append('g').attr('class', 'ex-nodes');

            const linkGen = d3.linkHorizontal()
                .x(function(d) { return d.y; })
                .y(function(d) { return d.x; });
            gTree.selectAll('path')
                .data(root.links())
                .join('path')
                .attr('class', 'ex-tree-link')
                .attr('data-from', function(d) { return d.source.data.id; })
                .attr('data-to', function(d) { return d.target.data.id; })
                .attr('d', linkGen);

            nodesByPath.clear();
            nodeElements.clear();
            root.descendants().forEach(function(d) {
                nodesByPath.set(d.data.id, d);
            });

            const nodeGroups = gNodes.selectAll('g.ex-node')
                .data(root.descendants())
                .join('g')
                .attr('class', function(d) { return 'ex-node ex-node-' + d.data.kind; })
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
                .attr('class', 'ex-section-label')
                .attr('x', -10).attr('dy', '0.32em')
                .attr('text-anchor', 'end')
                .text(function(d) { return d.data.label + ' (' + d.data.count + ')'; });

            nodeGroups.filter(function(d) { return d.data.kind === 'root'; })
                .append('text')
                .attr('class', 'ex-root-label')
                .attr('x', -12).attr('dy', '0.32em')
                .attr('text-anchor', 'end')
                .text(function(d) { return d.data.label; });

            nodeGroups.each(function(d) { nodeElements.set(d.data.id, this); });

            zoom = d3.zoom()
                .scaleExtent([0.2, 12])
                .on('zoom', function(ev) { gView.attr('transform', ev.transform); });
            svg.call(zoom);

            // Replay any paints issued before render ---------------
            if (mode === 'traversal') {
                for (let i = 0; i < visitOrder.length; i++) {
                    const v = visitOrder[i];
                    paintVisited(v.path, v.idx);
                }
            } else if (mode === 'intensity') {
                for (const [path, info] of intensityByPath) {
                    paintIntensity(path, info.score, info.count);
                }
            }
        }

        function baseRadius(d) {
            if (d.data.kind === 'root')    return 8;
            if (d.data.kind === 'section') return 5;
            return 3;
        }

        // --- Traversal mode ---------------------------------------
        function paintVisited(path, idx) {
            const el = nodeElements.get(path);
            if (!el) return;
            const sel = d3.select(el);
            sel.classed('ex-visited', true);
            const circle = sel.select('circle');
            circle.attr('r', 5)
                  .attr('stroke', accentColor)
                  .attr('stroke-width', 2);
            if (idx !== undefined && idx !== null) {
                // Overlay a tiny order-index badge
                let label = sel.select('text.ex-order');
                if (label.empty()) {
                    label = sel.append('text')
                        .attr('class', 'ex-order')
                        .attr('x', 8).attr('dy', '-0.4em')
                        .attr('font-size', 9)
                        .attr('fill', '#222');
                }
                label.text(String(idx + 1));
            }

            // Light up the ancestor chain --------------------------
            const leaf = nodesByPath.get(path);
            if (leaf) {
                let cursor = leaf;
                while (cursor.parent) {
                    const p = cursor.parent.data.id;
                    const c = cursor.data.id;
                    const parentEl = nodeElements.get(p);
                    if (parentEl) {
                        d3.select(parentEl).classed('ex-visited-ancestor', true);
                    }
                    paintTreeEdge(p, c);
                    cursor = cursor.parent;
                }
            }
        }

        function paintTreeEdge(fromId, toId) {
            if (!gTree) return;
            gTree.select(
                'path[data-from="' + cssEscape(fromId) + '"][data-to="' + cssEscape(toId) + '"]'
            ).classed('ex-traversed', true);
        }

        function markVisited(path, idx) {
            visitOrder.push({path: path, idx: idx});
            visitedSet.add(path);
            // Auto-expand containing section before paint
            const section = typeof path === 'string' ? path.split('/')[0] : null;
            if (section && !expandedSections.has(section)) {
                const known = graphData.sections.some(function(s) { return s.id === section; });
                if (known) {
                    expandedSections.add(section);
                    render();
                    return; // render replays the paint
                }
            }
            paintVisited(path, idx);
        }

        // --- Intensity mode ---------------------------------------
        function setIntensityRange(maxScore, maxCount) {
            intensityMaxScore = Math.max(1e-6, maxScore || 1);
            intensityMaxCount = Math.max(1, maxCount || 1);
        }

        function paintIntensity(path, score, count) {
            const el = nodeElements.get(path);
            if (!el) return;
            const sel = d3.select(el);
            sel.classed('ex-intense', true);
            const circle = sel.select('circle');
            // Radius: 3 (base) → 12 (max count)
            const r = 3 + 9 * Math.min(1, count / intensityMaxCount);
            // Opacity of accent halo proportional to score fraction
            const frac = Math.max(0, Math.min(1, score / intensityMaxScore));
            circle.attr('r', r)
                  .attr('stroke', accentColor)
                  .attr('stroke-width', 2)
                  .attr('stroke-opacity', 0.4 + 0.6 * frac)
                  .attr('fill-opacity', 0.6 + 0.4 * frac);

            // Annotate with chunk count
            let label = sel.select('text.ex-count');
            if (label.empty()) {
                label = sel.append('text')
                    .attr('class', 'ex-count')
                    .attr('x', 10).attr('dy', '0.32em')
                    .attr('font-size', 9)
                    .attr('fill', '#333');
            }
            label.text('×' + count);

            // Ancestors get a subtle highlight so the active section
            // chain remains visible.
            const leaf = nodesByPath.get(path);
            if (leaf) {
                let cursor = leaf;
                while (cursor.parent) {
                    const parentEl = nodeElements.get(cursor.parent.data.id);
                    if (parentEl) {
                        d3.select(parentEl).classed('ex-intense-ancestor', true);
                    }
                    cursor = cursor.parent;
                }
            }
        }

        function markIntensity(path, score, count) {
            intensityByPath.set(path, {score: score, count: count});
            const section = typeof path === 'string' ? path.split('/')[0] : null;
            if (section && !expandedSections.has(section)) {
                const known = graphData.sections.some(function(s) { return s.id === section; });
                if (known) {
                    expandedSections.add(section);
                    render();
                    return;
                }
            }
            paintIntensity(path, score, count);
        }

        // --- Utility ----------------------------------------------
        function cssEscape(s) {
            return String(s).replace(/[^a-zA-Z0-9_\-]/g, function(ch) { return '\\' + ch; });
        }

        function reset() {
            visitOrder.length = 0;
            visitedSet.clear();
            intensityByPath.clear();
            render();
        }

        function fit() {
            if (!svg || !zoom) return;
            svg.transition().duration(300).call(zoom.transform, d3.zoomIdentity);
        }

        // Initial render
        render();

        return {
            markVisited: markVisited,
            markIntensity: markIntensity,
            setIntensityRange: setIntensityRange,
            reset: reset,
            fit: fit,
            rerender: render,
        };
    }

    window.createExplorerGraph = createExplorerGraph;
})();
