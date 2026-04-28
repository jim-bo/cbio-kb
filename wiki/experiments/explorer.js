// Page driver for the traversal explorer.
//   1. Loads the wiki graph once + the explorer index
//   2. Populates the question dropdown
//   3. On select, fetches the per-question JSON and repaints both
//      graph panels (agentic = traversal mode, RAG = intensity mode)

(function() {
    let graphData = null;
    let indexData = null;
    let agenticGraph = null;
    let ragGraph = null;
    let currentQid = null;

    async function init() {
        const shell = document.querySelector('.explorer-shell');
        if (!shell) return;

        try {
            await waitFor(function() { return typeof d3 !== 'undefined'; }, 5000);
        } catch (_err) {
            shell.innerHTML = '<p>D3 failed to load — check network/adblock and reload.</p>';
            return;
        }

        try {
            const [gRes, iRes] = await Promise.all([
                fetch('../graph.json', {cache: 'no-cache'}),
                fetch('explorer/index.json', {cache: 'no-cache'}),
            ]);
            if (!gRes.ok) throw new Error('graph.json: HTTP ' + gRes.status);
            if (!iRes.ok) throw new Error('explorer/index.json: HTTP ' + iRes.status);
            graphData = await gRes.json();
            indexData = await iRes.json();
        } catch (err) {
            shell.innerHTML = '<p>Failed to load explorer data: ' + err.message + '</p>';
            console.error(err);
            return;
        }

        buildDropdown(indexData.questions);
        updateRunMeta();

        if (indexData.questions.length > 0) {
            const first = indexData.questions[0].id;
            await selectQuestion(first);
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

    function buildDropdown(questions) {
        const select = document.getElementById('explorer-question-select');
        if (!select) return;
        select.innerHTML = '';
        questions.forEach(function(q) {
            const opt = document.createElement('option');
            opt.value = q.id;
            const qtxt = q.question.length > 110 ? q.question.slice(0, 107) + '…' : q.question;
            opt.textContent = '[' + q.id + ' · ' + q.category + ']  ' + qtxt;
            select.appendChild(opt);
        });
        select.addEventListener('change', function() {
            selectQuestion(select.value);
        });
    }

    function updateRunMeta() {
        const meta = document.getElementById('explorer-run-meta');
        if (meta && indexData) {
            meta.textContent = 'run ' + indexData.run_id + ' · ' +
                               indexData.questions.length + ' questions';
        }
    }

    async function selectQuestion(qid) {
        currentQid = qid;
        const requestedQid = qid;
        const select = document.getElementById('explorer-question-select');
        if (select) select.value = qid;

        let payload = null;
        try {
            const res = await fetch('explorer/' + qid + '.json', {cache: 'no-cache'});
            if (!res.ok) throw new Error('HTTP ' + res.status);
            payload = await res.json();
        } catch (err) {
            if (currentQid !== requestedQid) return;
            setPanelEmpty('agentic-graph', 'Failed to load: ' + err.message);
            setPanelEmpty('rag-graph', 'Failed to load: ' + err.message);
            return;
        }

        if (currentQid !== requestedQid) return;
        renderQuestionCard(payload);
        renderAgentic(payload);
        renderRag(payload);
    }

    function renderQuestionCard(payload) {
        const card = document.getElementById('explorer-question-card');
        if (!card) return;
        const gold = (payload.gold_pmids || []).map(function(p) {
            return '<code>' + escapeHtml(String(p)) + '</code>';
        }).join(' ');
        card.innerHTML =
            '<span class="explorer-q-id">' + escapeHtml(payload.id) + '</span>' +
            escapeHtml(payload.question) +
            '<span class="explorer-q-category">' + escapeHtml(payload.category) + '</span>' +
            (gold ? '<div class="explorer-q-gold">gold: ' + gold + '</div>' : '');
    }

    function renderAgentic(payload) {
        const container = document.getElementById('agentic-graph');
        const scoreEl = document.getElementById('agentic-score');
        const answerEl = document.getElementById('agentic-answer');
        if (!container) return;
        container.innerHTML = '';

        const rec = payload.agentic;
        if (!rec) {
            setPanelEmpty('agentic-graph', 'No agentic record.');
            if (scoreEl) scoreEl.textContent = '';
            if (answerEl) answerEl.textContent = '';
            return;
        }

        if (scoreEl) scoreEl.textContent = formatScore(rec);
        if (answerEl) answerEl.innerHTML = '<p>' + escapeHtml(rec.answer || '(empty)') + '</p>';

        agenticGraph = window.createExplorerGraph(container, graphData, {
            mode: 'traversal',
            accentColor: '#e45756',
            initialExpanded: ['papers', 'datasets'],
        });

        // Issue visits in timeline order. The tool call's `args.path` (or
        // `args.entity`/`args.folder`) is the node identity.
        const events = rec.timeline || [];
        events.forEach(function(ev, i) {
            const path = resolveEventPath(ev);
            if (path) agenticGraph.markVisited(path, i);
        });
    }

    function resolveEventPath(ev) {
        const args = ev.args || {};
        if (args.path) return args.path;
        if (args.folder) return args.folder;  // section-level node
        if (args.entity) {
            // find_references — entity stem, e.g. 'EGFR' or '25730765'.
            // Guess the section by scanning the graph.
            const bare = args.entity;
            if (graphData && graphData.nodes) {
                const hit = graphData.nodes.find(function(n) {
                    return n.id.endsWith('/' + bare + '.md') ||
                           n.id.endsWith('/' + bare);
                });
                if (hit) return hit.id;
            }
            return null;
        }
        return null;
    }

    function renderRag(payload) {
        const container = document.getElementById('rag-graph');
        const scoreEl = document.getElementById('rag-score');
        const answerEl = document.getElementById('rag-answer');
        if (!container) return;
        container.innerHTML = '';

        const rec = payload.rag;
        if (!rec) {
            setPanelEmpty('rag-graph', 'No RAG record.');
            if (scoreEl) scoreEl.textContent = '';
            if (answerEl) answerEl.textContent = '';
            return;
        }

        if (scoreEl) scoreEl.textContent = formatScore(rec);
        if (answerEl) answerEl.innerHTML = '<p>' + escapeHtml(rec.answer || '(empty)') + '</p>';

        ragGraph = window.createExplorerGraph(container, graphData, {
            mode: 'intensity',
            accentColor: '#4c78a8',
            initialExpanded: ['papers'],
        });

        // Aggregate retrieval rows by paper path.
        const byPath = new Map();
        (rec.retrieval || []).forEach(function(r) {
            const path = r.path || ('papers/' + r.pmid + '.md');
            const cur = byPath.get(path) || {maxScore: 0, count: 0};
            cur.count += 1;
            if (r.score > cur.maxScore) cur.maxScore = r.score;
            byPath.set(path, cur);
        });

        let maxScore = 0, maxCount = 0;
        for (const v of byPath.values()) {
            if (v.maxScore > maxScore) maxScore = v.maxScore;
            if (v.count > maxCount) maxCount = v.count;
        }
        ragGraph.setIntensityRange(maxScore || 1, maxCount || 1);
        for (const [path, info] of byPath) {
            ragGraph.markIntensity(path, info.maxScore, info.count);
        }
    }

    function setPanelEmpty(canvasId, msg) {
        const el = document.getElementById(canvasId);
        if (el) el.innerHTML = '<div class="empty-state">' + escapeHtml(msg) + '</div>';
    }

    function formatScore(rec) {
        const s = rec.scores || {};
        if (!('accuracy' in s)) return '';
        return 'acc=' + s.accuracy + ' comp=' + s.completeness +
               ' cite=' + s.citation_correctness +
               (rec.wall_time_s ? '  ·  ' + rec.wall_time_s.toFixed(1) + 's' : '');
    }

    function escapeHtml(s) {
        return String(s == null ? '' : s)
            .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
