// API endpoint — local dev uses bundled FastAPI, production hits Cloud Run.
// Append ?cloud=1 to force the Cloud Run backend from localhost.
// Append ?port=N to override the local API port (default 8080).
const _params = new URLSearchParams(location.search);
const _forceCloud = _params.get('cloud') === '1';
const _port = _params.get('port') || '8080';
const _isLocal = !_forceCloud && (location.hostname === 'localhost' || location.hostname === '127.0.0.1');
const API_URL = _isLocal
    ? 'http://localhost:' + _port + '/api/chat'
    : 'https://cbio-kb-api-7vd2hab3va-uc.a.run.app/api/chat';

// Dev-only: ?delay=N holds the first event for N milliseconds so you can
// see the cold-start indicator without actually forcing a Cloud Run cold
// start. e.g. ?cloud=1&delay=3000 → 3 second fake cold start.
const COLD_START_FAKE_DELAY_MS = parseInt(_params.get('delay') || '0', 10);

// Accumulates the assistant's streamed text so we can re-parse it as markdown on every delta.
let assistantFullText = '';

let sessionId = null;
let sending = false;
let chatMode = 'agentic'; // 'agentic' | 'rag'

const form = document.getElementById('chat-form');
const input = document.getElementById('user-input');
const messages = document.getElementById('messages');
const contextFeed = document.getElementById('context-feed');
const contextTotal = document.getElementById('context-total');
const sendBtn = document.getElementById('send-btn');
const modeToggle = document.getElementById('mode-toggle');

let contextTokens = 0;
let pendingUserCard = null;
// Tracks the currently-growing assistant context block. A fresh one is
// created on the first text delta after each user/tool boundary, and
// finalized (nulled out) when a tool call or stream end interrupts.
let currentAssistantCard = null;
let currentAssistantText = '';
let currentAssistantPrevTokens = 0;
// The turn currently being built (received from server via turn_start).
let currentTurnIndex = 0;
// Length (in chars) of the pruning stub, used to adjust totals.
const STUB_TOKENS = 13; // "[previously retrieved …]" is ~51 chars → ~13 tok

// As the user types, show a "pending" user card at the bottom of the
// context stack. It previews what will be committed on Send — the
// first new block of the next turn's context.
input.addEventListener('input', function() {
    const text = input.value;
    if (!text.trim()) {
        if (pendingUserCard) {
            pendingUserCard.remove();
            pendingUserCard = null;
        }
        return;
    }
    if (!pendingUserCard) {
        removeEmptyState(contextFeed);
        pendingUserCard = document.createElement('div');
        pendingUserCard.className = 'context-card context-pending';
        contextFeed.appendChild(pendingUserCard);
    }
    const tokens = Math.max(1, Math.floor(text.length / 4));
    pendingUserCard.innerHTML =
        '<div class="context-card-header">' +
            '<span class="context-icon">\u270F\uFE0F</span>' +
            '<span class="context-kind">pending user message</span>' +
            '<span class="context-tokens">~' + tokens + ' tok</span>' +
        '</div>' +
        '<div class="context-body">' + escapeHtml(text) + '</div>';
    pendingUserCard.scrollIntoView({behavior: 'smooth', block: 'nearest'});
});

if (modeToggle) {
    modeToggle.addEventListener('change', function() {
        chatMode = modeToggle.value;
    });
}

form.addEventListener('submit', function(e) {
    e.preventDefault();
    const msg = input.value.trim();
    if (!msg || sending) return;
    sendMessage(msg);
});

// Static ASCII art for the cold-start DNA helix. CSS rotates it in 3D
// so it looks like a double helix spinning around its axis while we wait
// for the first SSE event from Cloud Run.
const DNA_HELIX_ART =
    " A━━━T\n" +
    " │   │\n" +
    " T━━━A\n" +
    " │   │\n" +
    " G━━━C\n" +
    " │   │\n" +
    " C━━━G\n" +
    " │   │\n" +
    " A━━━T\n" +
    " │   │\n" +
    " T━━━A";

function coldStartHTML() {
    return '<div class="cold-start">' +
               '<pre class="dna-helix">' + DNA_HELIX_ART + '</pre>' +
               '<p class="cold-start-label">waking up the agent…</p>' +
           '</div>';
}

// Tracks whether the first SSE event of the current turn has been seen.
// Used to hide the cold-start indicator on the first signal from the
// server (any event type) rather than waiting for text specifically.
let firstEventSeen = false;
// When ?delay=N is active we buffer every event until the fake delay
// expires, then drain them in order. Prevents streaming text from
// flashing into a bubble that still contains the DNA indicator.
let coldStartCleared = false;
let pendingEvents = [];

function sendMessage(msg) {
    sending = true;
    sendBtn.disabled = true;
    input.value = '';
    assistantFullText = '';
    firstEventSeen = false;
    coldStartCleared = false;
    pendingEvents = [];

    // Add user message
    const userDiv = document.createElement('div');
    userDiv.className = 'msg user';
    userDiv.textContent = msg;
    messages.appendChild(userDiv);

    // Create assistant message container, seeded with the cold-start
    // indicator. It's cleared on the first event of any kind.
    const assistantDiv = document.createElement('div');
    assistantDiv.className = 'msg assistant';
    assistantDiv.innerHTML = coldStartHTML();
    messages.appendChild(assistantDiv);
    messages.scrollTop = messages.scrollHeight;

    // Prior turn cards stay in place — the context accumulates across
    // turns to match what the model actually sees. Only clear the
    // transient pending-user preview card.
    if (pendingUserCard) {
        pendingUserCard.remove();
        pendingUserCard = null;
    }
    currentAssistantCard = null;
    currentAssistantText = '';

    // Stream response. Retry once on network errors (e.g. stale HTTP/2
    // socket after Cloud Run scale-to-zero).
    function doFetch(retries) {
        fetch(API_URL, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({message: msg, session_id: sessionId, mode: chatMode}),
        }).then(function(response) {
            if (!response.ok) {
                return response.text().then(function(body) {
                    throw new Error('HTTP ' + response.status + (body ? ': ' + body : ''));
                });
            }
            if (!response.body) {
                throw new Error('Streaming response body is unavailable');
            }
            var reader = response.body.getReader();
            var decoder = new TextDecoder();
            var buffer = '';

            var currentEvent = 'message';
            var currentData = '';

            function flushEvent() {
                if (currentData) {
                    handleEvent(currentEvent, currentData, assistantDiv);
                }
                currentEvent = 'message';
                currentData = '';
            }

            function processChunk(result) {
                if (result.done) {
                    flushEvent();
                    finishSending();
                    return;
                }
                buffer += decoder.decode(result.value, {stream: true});

                var lines = buffer.split('\n');
                buffer = lines.pop();

                for (var i = 0; i < lines.length; i++) {
                    var line = lines[i].replace(/\r$/, '');
                    if (line === '') {
                        flushEvent();
                    } else if (line.startsWith('event:')) {
                        currentEvent = line.slice(6).trim();
                    } else if (line.startsWith('data:')) {
                        // Per the SSE spec, multiple `data:` lines for
                        // a single event are joined with newlines.
                        // Trim only the conventional leading space, not
                        // payload content.
                        var piece = line.slice(5);
                        if (piece.startsWith(' ')) piece = piece.slice(1);
                        currentData = currentData ? (currentData + '\n' + piece) : piece;
                    }
                }

                messages.scrollTop = messages.scrollHeight;
                return reader.read().then(processChunk);
            }

            return reader.read().then(processChunk);
        }).catch(function(err) {
            if (retries > 0) {
                setTimeout(function() { doFetch(retries - 1); }, 500);
                return;
            }
            assistantDiv.textContent = 'Error: ' + err.message;
            finishSending();
        });
    }
    doFetch(1);
}

function handleEvent(eventType, data, assistantDiv) {
    if (!data) return;

    // First-event gating: handle the cold-start DNA indicator and the
    // optional ?delay=N fake cold start. When a delay is active we
    // buffer every event until the timer fires, then drain them in
    // order so real events never touch a bubble still showing the DNA.
    if (!firstEventSeen) {
        firstEventSeen = true;
        if (COLD_START_FAKE_DELAY_MS > 0) {
            pendingEvents.push({eventType: eventType, data: data});
            setTimeout(function() {
                coldStartCleared = true;
                const coldStart = assistantDiv.querySelector('.cold-start');
                if (coldStart) assistantDiv.innerHTML = '';
                const queue = pendingEvents;
                pendingEvents = [];
                for (const ev of queue) {
                    dispatchEvent(ev.eventType, ev.data, assistantDiv);
                }
            }, COLD_START_FAKE_DELAY_MS);
            return;
        }
        coldStartCleared = true;
        const coldStart = assistantDiv.querySelector('.cold-start');
        if (coldStart) assistantDiv.innerHTML = '';
    }

    // Still buffering during the fake delay?
    if (!coldStartCleared) {
        pendingEvents.push({eventType: eventType, data: data});
        return;
    }

    dispatchEvent(eventType, data, assistantDiv);
}

function dispatchEvent(eventType, data, assistantDiv) {
    try {
        const parsed = JSON.parse(data);

        if (eventType === 'text') {
            assistantFullText += parsed.delta;
            // Re-render the full markdown on each delta and append a
            // blinking cursor so the user can see the agent is still
            // producing text.
            assistantDiv.innerHTML =
                marked.parse(assistantFullText) +
                '<span class="streaming-cursor"></span>';
            appendAssistantDelta(parsed.delta);
        } else if (eventType === 'tool_use') {
            finalizeAssistantCard();
            addContextToolBlock(parsed);
            notifyGraphOfToolUse(parsed);
        } else if (eventType === 'context_system') {
            addContextSystemBlock(parsed);
        } else if (eventType === 'turn_start') {
            handleTurnStart(parsed);
            if (window.AskGraph && typeof parsed.turn_index === 'number') {
                window.AskGraph.startTurn(parsed.turn_index);
            }
        } else if (eventType === 'context_user') {
            addContextUserBlock(parsed);
        } else if (eventType === 'done') {
            finalizeAssistantCard();
            // Strip the streaming cursor now that the turn is complete.
            const cursor = assistantDiv.querySelector('.streaming-cursor');
            if (cursor) cursor.remove();
            sessionId = parsed.session_id;
        } else if (eventType === 'error') {
            assistantDiv.textContent += '\n[Error: ' + parsed.error + ']';
        }
    } catch (e) {
        // skip unparseable
    }
}

// Build a base context card. Every card is collapsed by default; the
// header has a caret toggle that expands the body on click.
// opts: {className, icon, kind, extraText?, summary?, tokens, bodyText, turnIndex?}
function buildCard(opts) {
    const card = document.createElement('div');
    card.className = 'context-card ' + opts.className;
    if (opts.turnIndex !== undefined) {
        card.dataset.turn = String(opts.turnIndex);
    }

    const header = document.createElement('div');
    header.className = 'context-card-header';

    const caret = document.createElement('span');
    caret.className = 'context-caret';
    caret.textContent = '+';
    header.appendChild(caret);

    const icon = document.createElement('span');
    icon.className = 'context-icon';
    icon.textContent = opts.icon;
    header.appendChild(icon);

    const kind = document.createElement('span');
    kind.className = 'context-kind';
    kind.textContent = opts.kind;
    header.appendChild(kind);

    if (opts.extraText) {
        const extra = document.createElement('span');
        extra.className = 'context-args';
        extra.textContent = opts.extraText;
        header.appendChild(extra);
    }

    if (opts.summary) {
        const summary = document.createElement('span');
        summary.className = 'context-summary';
        summary.textContent = opts.summary;
        header.appendChild(summary);
    }

    const tokens = document.createElement('span');
    tokens.className = 'context-tokens';
    tokens.textContent = opts.tokens + ' tok';
    header.appendChild(tokens);

    const body = document.createElement('div');
    body.className = 'context-body context-collapsed';
    body.textContent = opts.bodyText || '';

    header.addEventListener('click', function() {
        const collapsed = body.classList.toggle('context-collapsed');
        caret.textContent = collapsed ? '+' : '\u2212'; // + / −
    });

    card.appendChild(header);
    card.appendChild(body);
    return card;
}

function addContextSystemBlock(info) {
    removeEmptyState(contextFeed);
    const card = buildCard({
        className: 'context-system',
        icon: '\u{2699}\u{FE0F}',
        kind: 'system prompt',
        tokens: info.tokens,
        bodyText: info.content,
    });
    contextFeed.appendChild(card);
    contextTokens += info.tokens;
    updateContextTotal();
}

function addContextUserBlock(info) {
    // Replace the pending card (if any) with a committed user-message
    // block. Tokens contribute to the running total.
    removeEmptyState(contextFeed);
    if (pendingUserCard) {
        pendingUserCard.remove();
        pendingUserCard = null;
    }
    const card = buildCard({
        className: 'context-user',
        icon: '\u{1F464}',
        kind: 'user message',
        tokens: info.tokens,
        bodyText: info.content,
        turnIndex: info.turn_index,
    });
    contextFeed.appendChild(card);
    contextTokens += info.tokens;
    updateContextTotal();
    card.scrollIntoView({behavior: 'smooth', block: 'nearest'});
}

function appendAssistantDelta(delta) {
    if (!currentAssistantCard) {
        removeEmptyState(contextFeed);
        currentAssistantCard = buildCard({
            className: 'context-assistant',
            icon: '\u{1F916}',
            kind: 'assistant text',
            tokens: 0,
            bodyText: '',
            turnIndex: currentTurnIndex,
        });
        contextFeed.appendChild(currentAssistantCard);
        currentAssistantText = '';
        currentAssistantPrevTokens = 0;
    }
    currentAssistantText += delta;
    const body = currentAssistantCard.querySelector('.context-body');
    body.textContent = currentAssistantText;
    // Recompute tokens for just this card and update the running total
    // incrementally so we don't double-count.
    const newTokens = Math.max(1, Math.floor(currentAssistantText.length / 4));
    const diff = newTokens - currentAssistantPrevTokens;
    currentAssistantPrevTokens = newTokens;
    contextTokens += diff;
    const tokSpan = currentAssistantCard.querySelector('.context-tokens');
    tokSpan.textContent = newTokens + ' tok';
    updateContextTotal();
    currentAssistantCard.scrollIntoView({behavior: 'smooth', block: 'nearest'});
}

function finalizeAssistantCard() {
    // A new tool call or stream-end closes the current assistant round.
    currentAssistantCard = null;
    currentAssistantText = '';
    currentAssistantPrevTokens = 0;
}

function addContextToolBlock(info) {
    removeEmptyState(contextFeed);
    const card = buildCard({
        className: 'context-tool tool-' + info.name,
        icon: toolIcon(info.name),
        kind: info.name,
        extraText: formatArgs(info.args),
        summary: info.summary,
        tokens: info.tokens,
        bodyText: info.preview,
        turnIndex: info.turn_index,
    });
    // Remember the pre-prune token count so we can subtract accurately
    // if this card later gets marked as pruned.
    card.dataset.tokens = String(info.tokens);
    contextFeed.appendChild(card);
    contextTokens += info.tokens;
    updateContextTotal();
    card.scrollIntoView({behavior: 'smooth', block: 'nearest'});
}

function handleTurnStart(info) {
    currentTurnIndex = info.turn_index;
    const cutoff = info.turn_index - info.keep_recent;
    if (cutoff < 0) return; // nothing to prune yet

    // Walk every tool card whose turn_index is at or below the cutoff
    // and mark it pruned: show the stub text, drop its token weight,
    // apply the dimmed style.
    const cards = contextFeed.querySelectorAll('.context-card.context-tool');
    for (const card of cards) {
        if (card.classList.contains('context-pruned')) continue;
        const t = parseInt(card.dataset.turn || '0', 10);
        if (t <= cutoff) {
            const prev = parseInt(card.dataset.tokens || '0', 10);
            card.classList.add('context-pruned');
            const body = card.querySelector('.context-body');
            if (body) body.textContent = '[previously retrieved — re-run the tool if you need this again]';
            const tokSpan = card.querySelector('.context-tokens');
            if (tokSpan) tokSpan.textContent = '~' + STUB_TOKENS + ' tok (pruned)';
            contextTokens -= Math.max(0, prev - STUB_TOKENS);
        }
    }
    updateContextTotal();
}

function updateContextTotal() {
    if (contextTokens <= 0) {
        contextTotal.textContent = '';
    } else {
        contextTotal.textContent = '~' + formatTokens(contextTokens) + ' tok';
    }
    var badge = document.getElementById('drawer-badge');
    if (badge) badge.textContent = contextTotal.textContent;
}

function formatTokens(n) {
    if (n >= 1000) return (n / 1000).toFixed(1) + 'K';
    return String(n);
}

function removeEmptyState(container) {
    const empty = container.querySelector('.empty-state');
    if (empty) empty.remove();
}

function finishSending() {
    sending = false;
    sendBtn.disabled = false;
    input.focus();
}

function toolIcon(name) {
    var icons = {
        read_page: '\u{1F4C4}',
        read_section: '\u{1F4D1}',
        get_page_metadata: '\u{1F3F7}',
        list_pages: '\u{1F4C1}',
        search: '\u{1F50D}',
        follow_links: '\u{1F517}',
        find_references: '\u21A9',
        vector_search: '\u{1F9ED}'
    };
    return icons[name] || '\u{1F527}';
}

// Forward path-bearing tool calls to the graph viz so the agent's
// traversal of the wiki vault can be highlighted in the Graph tab.
// Only `read_page` / `read_section` / `get_page_metadata` / `follow_links`
// have a vault-relative `path` arg pointing at a known node; the other
// tools (`search`, `list_pages`, `find_references`) operate on
// folders/queries/entities, not on a specific page.
const PATH_BEARING_TOOLS = new Set([
    'read_page', 'read_section', 'get_page_metadata', 'follow_links',
]);

function notifyGraphOfToolUse(info) {
    if (!window.AskGraph || !info) return;
    const turn = typeof info.turn_index === 'number' ? info.turn_index : currentTurnIndex;
    const paths = Array.isArray(info.result_paths) ? info.result_paths : [];
    if (paths.length) {
        for (const p of paths) {
            if (typeof p !== 'string') continue;
            if (!p.endsWith('.md')) continue;
            if (p.startsWith('_') || p.startsWith('.')) continue;
            if (p.includes('://')) continue;
            window.AskGraph.markVisited(p, turn);
        }
        return;
    }
    if (!PATH_BEARING_TOOLS.has(info.name)) return;
    const path = info.args && info.args.path;
    if (typeof path !== 'string' || !path) return;
    window.AskGraph.markVisited(path, turn);
}

function formatArgs(args) {
    if (!args || typeof args !== 'object') return '';
    return Object.entries(args).map(function(kv) {
        return kv[0] + '=' + kv[1];
    }).join(', ');
}

function escapeHtml(s) {
    var div = document.createElement('div');
    div.textContent = s;
    return div.innerHTML;
}

// ─── Drawer tab switching ───────────────────────────────────────────
document.addEventListener('click', function(e) {
    var infoBtn = e.target.closest('.drawer-tab-info');
    if (infoBtn) {
        e.stopPropagation();
        var infoPaneId = infoBtn.dataset.infoFor;
        if (!infoPaneId) return;
        var panel = document.getElementById(infoPaneId.replace('-pane', '-info'));
        if (!panel) return;
        if (panel.hasAttribute('hidden')) {
            panel.removeAttribute('hidden');
            infoBtn.setAttribute('aria-expanded', 'true');
        } else {
            panel.setAttribute('hidden', '');
            infoBtn.setAttribute('aria-expanded', 'false');
        }
        return;
    }

    var tab = e.target.closest('.drawer-tab');
    if (!tab) return;
    var paneId = tab.dataset.drawerPane;
    if (!paneId) return;

    tab.closest('.drawer-tabs').querySelectorAll('.drawer-tab').forEach(function(t) {
        t.classList.remove('active');
        t.setAttribute('aria-selected', 'false');
    });
    document.querySelectorAll('.drawer-pane').forEach(function(p) {
        p.classList.remove('active');
    });

    tab.classList.add('active');
    tab.setAttribute('aria-selected', 'true');
    document.getElementById(paneId).classList.add('active');
});

document.addEventListener('keydown', function(e) {
    if (e.key !== 'Enter' && e.key !== ' ') return;
    var infoBtn = e.target.closest('.drawer-tab-info');
    if (!infoBtn) return;
    e.preventDefault();
    infoBtn.click();
});

// ─── Scroll to latest context card when drawer opens ────────────────
var sideDrawer = document.getElementById('side-drawer');
if (sideDrawer) {
    sideDrawer.addEventListener('shown.bs.offcanvas', function() {
        var last = contextFeed.lastElementChild;
        if (last) last.scrollIntoView({behavior: 'instant', block: 'end'});
    });
}

// ─── Drag-to-resize + snap + maximize on drawer ─────────────────────
(function() {
    var drawer = document.getElementById('side-drawer');
    if (!drawer) return;
    var handle = drawer.querySelector('.drawer-handle');
    var maxBtn = document.getElementById('drawer-maximize');
    if (!handle) return;

    // Snap points as fraction of viewport height.
    var SNAPS = { COLLAPSED: 0.25, MID: 0.6, MAX: 0.92 };
    // Drag below this height → dismiss drawer entirely.
    // Tuned so a single assertive swipe from MID (60vh) past the
    // COLLAPSED band closes the drawer, while a gentle drag lands
    // at COLLAPSED (25vh).
    var DISMISS_BELOW_VH = 0.20;

    var startY = null;
    var startHeight = 0;
    var dragging = false;
    var moved = false;
    var downTime = 0;
    var lastSnap = 'MID';

    // A pointerup that travelled < TAP_PX and took < TAP_MS is a tap,
    // not a drag — treat it as "close the drawer."
    var TAP_PX = 6;
    var TAP_MS = 300;

    function vhPx(ratio) { return window.innerHeight * ratio; }

    function applyHeight(px) {
        drawer.style.height = px + 'px';
        drawer.style.maxHeight = px + 'px';
    }

    function resetInline() {
        drawer.style.transition = '';
        drawer.style.transform = '';
        drawer.style.height = '';
        drawer.style.maxHeight = '';
    }

    function nearestSnap(pxHeight) {
        var keys = ['COLLAPSED', 'MID', 'MAX'];
        var best = keys[0], bestDiff = Math.abs(pxHeight - vhPx(SNAPS[keys[0]]));
        for (var i = 1; i < keys.length; i++) {
            var d = Math.abs(pxHeight - vhPx(SNAPS[keys[i]]));
            if (d < bestDiff) { best = keys[i]; bestDiff = d; }
        }
        return best;
    }

    function snapTo(name) {
        lastSnap = name;
        drawer.style.transition = 'height 0.2s ease-out, max-height 0.2s ease-out';
        applyHeight(vhPx(SNAPS[name]));
        setTimeout(function() { drawer.style.transition = ''; }, 220);
        updateMaxBtn();
    }

    function updateMaxBtn() {
        if (!maxBtn) return;
        var icon = maxBtn.querySelector('i');
        if (!icon) return;
        var maxed = lastSnap === 'MAX';
        icon.className = maxed ? 'bi bi-arrows-angle-contract' : 'bi bi-arrows-angle-expand';
        maxBtn.setAttribute('aria-label', maxed ? 'Collapse drawer' : 'Expand drawer');
    }

    function dismiss() {
        drawer.style.transition = 'transform 0.2s ease-out';
        drawer.style.transform = 'translateY(100%)';
        setTimeout(function() {
            var inst = bootstrap.Offcanvas.getInstance(drawer);
            if (inst) inst.hide(); else resetInline();
        }, 200);
    }

    // Whenever Bootstrap finishes hiding (any path: swipe, backdrop,
    // close button, Esc), reset inline styles so the next open starts
    // fresh at the CSS default (60vh / MID).
    drawer.addEventListener('hidden.bs.offcanvas', function() {
        resetInline();
        lastSnap = 'MID';
        updateMaxBtn();
    });

    // Also reset on show, defensively — catches any cross-cycle leak.
    drawer.addEventListener('show.bs.offcanvas', function() {
        drawer.style.transition = '';
        drawer.style.transform = '';
        // Keep CSS default 60vh on open by clearing inline height.
        drawer.style.height = '';
        drawer.style.maxHeight = '';
        startY = null;
        dragging = false;
        lastSnap = 'MID';
        updateMaxBtn();
    });

    function onDown(e) {
        if (!drawer.classList.contains('show')) return;
        startY = e.clientY;
        startHeight = drawer.getBoundingClientRect().height;
        dragging = true;
        moved = false;
        downTime = Date.now();
        drawer.style.transition = 'none';
        try { handle.setPointerCapture(e.pointerId); } catch (_) {}
        e.preventDefault();
    }

    function onMove(e) {
        if (!dragging) return;
        var deltaY = e.clientY - startY;
        if (Math.abs(deltaY) > TAP_PX) moved = true;
        // Drag DOWN (positive deltaY) shrinks; drag UP (negative) grows.
        var newH = Math.max(0, Math.min(window.innerHeight, startHeight - deltaY));
        applyHeight(newH);
    }

    function onUp(e) {
        if (!dragging) {
            // Defensive: always clear state even if onDown was missed.
            startY = null;
            return;
        }
        dragging = false;
        startY = null;
        try { handle.releasePointerCapture(e.pointerId); } catch (_) {}

        var elapsed = Date.now() - downTime;
        if (!moved && elapsed < TAP_MS) {
            // Tap (no drag) → dismiss.
            // Reset any transient height set during a sub-threshold move.
            drawer.style.height = '';
            drawer.style.maxHeight = '';
            dismiss();
            return;
        }

        var h = drawer.getBoundingClientRect().height;
        if (h < vhPx(DISMISS_BELOW_VH)) {
            dismiss();
        } else {
            snapTo(nearestSnap(h));
        }
    }

    handle.addEventListener('pointerdown', onDown);
    handle.addEventListener('pointermove', onMove);
    handle.addEventListener('pointerup', onUp);
    handle.addEventListener('pointercancel', onUp);
    // Fallback: if pointerup escapes the handle, window still catches it.
    window.addEventListener('pointerup', onUp);
    window.addEventListener('pointercancel', onUp);

    if (maxBtn) {
        maxBtn.addEventListener('click', function() {
            snapTo(lastSnap === 'MAX' ? 'MID' : 'MAX');
        });
    }
})();
