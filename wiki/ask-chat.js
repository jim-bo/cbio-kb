// API endpoint — local dev uses bundled FastAPI, production hits Cloud Run.
const API_URL = (location.hostname === 'localhost' || location.hostname === '127.0.0.1')
    ? 'http://localhost:8080/api/chat'
    : 'https://cbio-kb-api.run.app/api/chat';

// Accumulates the assistant's streamed text so we can re-parse it as markdown on every delta.
let assistantFullText = '';

let sessionId = null;
let sending = false;

const form = document.getElementById('chat-form');
const input = document.getElementById('user-input');
const messages = document.getElementById('messages');
const contextFeed = document.getElementById('context-feed');
const contextTotal = document.getElementById('context-total');
const sendBtn = document.getElementById('send-btn');

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

form.addEventListener('submit', function(e) {
    e.preventDefault();
    const msg = input.value.trim();
    if (!msg || sending) return;
    sendMessage(msg);
});

function sendMessage(msg) {
    sending = true;
    sendBtn.disabled = true;
    input.value = '';
    assistantFullText = '';

    // Add user message
    const userDiv = document.createElement('div');
    userDiv.className = 'msg user';
    userDiv.textContent = msg;
    messages.appendChild(userDiv);

    // Create assistant message container
    const assistantDiv = document.createElement('div');
    assistantDiv.className = 'msg assistant';
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

    // Stream response
    fetch(API_URL, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message: msg, session_id: sessionId}),
    }).then(function(response) {
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let buffer = '';

        let currentEvent = 'message';
        let currentData = '';

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

            // Line-by-line parse: accumulate event/data until an empty line.
            const lines = buffer.split('\n');
            buffer = lines.pop(); // last (possibly incomplete) line

            for (const rawLine of lines) {
                const line = rawLine.replace(/\r$/, '');
                if (line === '') {
                    flushEvent();
                } else if (line.startsWith('event:')) {
                    currentEvent = line.slice(6).trim();
                } else if (line.startsWith('data:')) {
                    currentData = line.slice(5).trim();
                } else if (line.startsWith(':')) {
                    // comment / ping — ignore
                }
            }

            messages.scrollTop = messages.scrollHeight;
            return reader.read().then(processChunk);
        }

        return reader.read().then(processChunk);
    }).catch(function(err) {
        assistantDiv.textContent = 'Error: ' + err.message;
        finishSending();
    });
}

function handleEvent(eventType, data, assistantDiv) {
    if (!data) return;
    try {
        const parsed = JSON.parse(data);

        if (eventType === 'text') {
            assistantFullText += parsed.delta;
            assistantDiv.innerHTML = marked.parse(assistantFullText);
            appendAssistantDelta(parsed.delta);
        } else if (eventType === 'tool_use') {
            finalizeAssistantCard();
            addContextToolBlock(parsed);
        } else if (eventType === 'context_system') {
            addContextSystemBlock(parsed);
        } else if (eventType === 'turn_start') {
            handleTurnStart(parsed);
        } else if (eventType === 'context_user') {
            addContextUserBlock(parsed);
        } else if (eventType === 'done') {
            finalizeAssistantCard();
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
        find_references: '\u21A9'
    };
    return icons[name] || '\u{1F527}';
}

function formatArgs(args) {
    return Object.entries(args).map(function(kv) {
        return kv[0] + '=' + kv[1];
    }).join(', ');
}

function escapeHtml(s) {
    var div = document.createElement('div');
    div.textContent = s;
    return div.innerHTML;
}
