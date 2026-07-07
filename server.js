/**
 * Agentic OS server — zero-dependency Node.js (18+).
 *
 * Modules (each degrades to demo mode when its env vars are unset):
 *   - YouTube metrics   GET  /api/metrics/youtube        (YOUTUBE_API_KEY, YOUTUBE_CHANNEL_ID)
 *   - Hermes agent chat POST /api/hermes/chat            (HERMES_URL, HERMES_TOKEN)
 *   - Knowledge search  GET  /api/knowledge/search?q=... (local knowledge/ markdown "brain")
 *   - Workflows         GET/POST/PATCH /api/workflows    (persisted to data/workflows.json)
 */

const http = require('node:http');
const fs = require('node:fs');
const fsp = require('node:fs/promises');
const path = require('node:path');
const crypto = require('node:crypto');

const PORT = Number(process.env.PORT) || 3000;
const ROOT = __dirname;
const PUBLIC_DIR = path.join(ROOT, 'public');
const KNOWLEDGE_DIR = path.join(ROOT, 'knowledge');
const DATA_DIR = path.join(ROOT, 'data');
const WORKFLOWS_FILE = path.join(DATA_DIR, 'workflows.json');

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.ico': 'image/x-icon',
  '.webmanifest': 'application/manifest+json',
};

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

function sendJson(res, status, body) {
  const payload = JSON.stringify(body);
  res.writeHead(status, {
    'Content-Type': 'application/json; charset=utf-8',
    'Cache-Control': 'no-store',
  });
  res.end(payload);
}

function readBody(req, limit = 64 * 1024) {
  return new Promise((resolve, reject) => {
    let size = 0;
    const chunks = [];
    req.on('data', (chunk) => {
      size += chunk.length;
      if (size > limit) {
        reject(new Error('payload too large'));
        req.destroy();
        return;
      }
      chunks.push(chunk);
    });
    req.on('end', () => resolve(Buffer.concat(chunks).toString('utf8')));
    req.on('error', reject);
  });
}

async function readJsonBody(req) {
  const raw = await readBody(req);
  if (!raw) return {};
  return JSON.parse(raw);
}

function compactNumber(n) {
  if (n >= 1e6) return (n / 1e6).toFixed(1).replace(/\.0$/, '') + 'M';
  if (n >= 1e3) return (n / 1e3).toFixed(1).replace(/\.0$/, '') + 'K';
  return String(n);
}

// ---------------------------------------------------------------------------
// Phase 2 — YouTube Data API v3 metrics
// ---------------------------------------------------------------------------

const YT_API = 'https://www.googleapis.com/youtube/v3';
let ytCache = { at: 0, payload: null };
const YT_CACHE_MS = 5 * 60 * 1000;

const DEMO_METRICS = {
  demo: true,
  channel: {
    title: 'Demo Channel',
    subscribers: 3200,
    views: 481250,
    videos: 42,
  },
  recentVideos: [
    { title: 'Build an Agentic OS in 2026', views: 18400, publishedAt: '2026-06-28' },
    { title: 'Claude Skills + Hermes Agent', views: 12100, publishedAt: '2026-06-20' },
    { title: 'SEED + PAUL Deep Dive', views: 9800, publishedAt: '2026-06-12' },
    { title: 'Claude Code + Graphify RAG', views: 15600, publishedAt: '2026-06-05' },
    { title: 'Railway Deploys for Agents', views: 7300, publishedAt: '2026-05-29' },
    { title: 'MCP Command Center Setup', views: 11250, publishedAt: '2026-05-21' },
  ],
};

async function fetchYouTubeMetrics() {
  const apiKey = process.env.YOUTUBE_API_KEY;
  const channelId = process.env.YOUTUBE_CHANNEL_ID;
  if (!apiKey || !channelId) return DEMO_METRICS;

  if (ytCache.payload && Date.now() - ytCache.at < YT_CACHE_MS) return ytCache.payload;

  const chanRes = await fetch(
    `${YT_API}/channels?part=snippet,statistics&id=${encodeURIComponent(channelId)}&key=${apiKey}`
  );
  if (!chanRes.ok) throw new Error(`YouTube channels API ${chanRes.status}`);
  const chanData = await chanRes.json();
  const channel = chanData.items && chanData.items[0];
  if (!channel) throw new Error('channel not found');

  const searchRes = await fetch(
    `${YT_API}/search?part=id&channelId=${encodeURIComponent(channelId)}&order=date&type=video&maxResults=6&key=${apiKey}`
  );
  if (!searchRes.ok) throw new Error(`YouTube search API ${searchRes.status}`);
  const searchData = await searchRes.json();
  const videoIds = (searchData.items || []).map((i) => i.id.videoId).filter(Boolean);

  let recentVideos = [];
  if (videoIds.length) {
    const vidsRes = await fetch(
      `${YT_API}/videos?part=snippet,statistics&id=${videoIds.join(',')}&key=${apiKey}`
    );
    if (!vidsRes.ok) throw new Error(`YouTube videos API ${vidsRes.status}`);
    const vidsData = await vidsRes.json();
    recentVideos = (vidsData.items || []).map((v) => ({
      title: v.snippet.title,
      views: Number(v.statistics.viewCount || 0),
      publishedAt: v.snippet.publishedAt.slice(0, 10),
    }));
  }

  const payload = {
    demo: false,
    channel: {
      title: channel.snippet.title,
      subscribers: Number(channel.statistics.subscriberCount || 0),
      views: Number(channel.statistics.viewCount || 0),
      videos: Number(channel.statistics.videoCount || 0),
    },
    recentVideos,
  };
  ytCache = { at: Date.now(), payload };
  return payload;
}

// ---------------------------------------------------------------------------
// Phase 3 — Hermes agent chat (VPS webhook proxy)
// ---------------------------------------------------------------------------

async function hermesChat(message) {
  const hermesUrl = process.env.HERMES_URL;
  if (!hermesUrl) {
    return {
      demo: true,
      reply:
        `Hermes (demo mode): I received “${message}”. ` +
        'Set HERMES_URL to your VPS agent endpoint to route messages to the live agent.',
    };
  }

  const headers = { 'Content-Type': 'application/json' };
  if (process.env.HERMES_TOKEN) headers.Authorization = `Bearer ${process.env.HERMES_TOKEN}`;

  const res = await fetch(hermesUrl, {
    method: 'POST',
    headers,
    body: JSON.stringify({ message }),
    signal: AbortSignal.timeout(30000),
  });
  if (!res.ok) throw new Error(`Hermes endpoint ${res.status}`);
  const data = await res.json().catch(() => ({}));
  return { demo: false, reply: data.reply || data.response || data.message || JSON.stringify(data) };
}

// ---------------------------------------------------------------------------
// Phase 4 — Graphify-style knowledge search over local markdown
// ---------------------------------------------------------------------------

async function listKnowledgeDocs() {
  let entries = [];
  try {
    entries = await fsp.readdir(KNOWLEDGE_DIR);
  } catch {
    return [];
  }
  const docs = [];
  for (const name of entries.filter((f) => f.endsWith('.md')).sort()) {
    const text = await fsp.readFile(path.join(KNOWLEDGE_DIR, name), 'utf8');
    const titleLine = text.split('\n').find((l) => l.startsWith('# '));
    docs.push({
      file: name,
      title: titleLine ? titleLine.slice(2).trim() : name.replace(/\.md$/, ''),
      text,
    });
  }
  return docs;
}

function snippetAround(text, index, radius = 140) {
  const start = Math.max(0, index - radius);
  const end = Math.min(text.length, index + radius);
  return (start > 0 ? '…' : '') + text.slice(start, end).replace(/\s+/g, ' ').trim() + (end < text.length ? '…' : '');
}

async function searchKnowledge(query) {
  const docs = await listKnowledgeDocs();
  const terms = query.toLowerCase().split(/\s+/).filter(Boolean);
  if (!terms.length) return [];

  const results = [];
  for (const doc of docs) {
    const lower = doc.text.toLowerCase();
    let score = 0;
    let firstHit = -1;
    for (const term of terms) {
      let idx = lower.indexOf(term);
      while (idx !== -1) {
        score += 1;
        if (firstHit === -1) firstHit = idx;
        idx = lower.indexOf(term, idx + term.length);
      }
      if (doc.title.toLowerCase().includes(term)) score += 5;
    }
    if (score > 0) {
      results.push({
        file: doc.file,
        title: doc.title,
        score,
        snippet: snippetAround(doc.text, Math.max(firstHit, 0)),
      });
    }
  }
  return results.sort((a, b) => b.score - a.score).slice(0, 10);
}

// ---------------------------------------------------------------------------
// Workflows — lightweight persisted task board
// ---------------------------------------------------------------------------

const WORKFLOW_STATUSES = ['todo', 'active', 'done'];

async function loadWorkflows() {
  try {
    const raw = await fsp.readFile(WORKFLOWS_FILE, 'utf8');
    const parsed = JSON.parse(raw);
    return Array.isArray(parsed) ? parsed : [];
  } catch {
    return [];
  }
}

async function saveWorkflows(workflows) {
  await fsp.mkdir(DATA_DIR, { recursive: true });
  await fsp.writeFile(WORKFLOWS_FILE, JSON.stringify(workflows, null, 2));
}

// ---------------------------------------------------------------------------
// Router
// ---------------------------------------------------------------------------

async function handleApi(req, res, url) {
  const route = `${req.method} ${url.pathname}`;

  if (route === 'GET /api/health') {
    return sendJson(res, 200, {
      ok: true,
      uptime: process.uptime(),
      modules: {
        youtube: Boolean(process.env.YOUTUBE_API_KEY && process.env.YOUTUBE_CHANNEL_ID),
        hermes: Boolean(process.env.HERMES_URL),
        knowledge: fs.existsSync(KNOWLEDGE_DIR),
      },
    });
  }

  if (route === 'GET /api/metrics/youtube') {
    try {
      return sendJson(res, 200, await fetchYouTubeMetrics());
    } catch (err) {
      return sendJson(res, 502, { error: `YouTube metrics failed: ${err.message}` });
    }
  }

  if (route === 'POST /api/hermes/chat') {
    let body;
    try {
      body = await readJsonBody(req);
    } catch {
      return sendJson(res, 400, { error: 'invalid JSON body' });
    }
    const message = typeof body.message === 'string' ? body.message.trim() : '';
    if (!message) return sendJson(res, 400, { error: 'message is required' });
    try {
      return sendJson(res, 200, await hermesChat(message));
    } catch (err) {
      return sendJson(res, 502, { error: `Hermes unreachable: ${err.message}` });
    }
  }

  if (route === 'GET /api/knowledge/docs') {
    const docs = await listKnowledgeDocs();
    return sendJson(res, 200, docs.map(({ file, title }) => ({ file, title })));
  }

  if (route === 'GET /api/knowledge/search') {
    const q = (url.searchParams.get('q') || '').trim();
    if (!q) return sendJson(res, 400, { error: 'q is required' });
    return sendJson(res, 200, { query: q, results: await searchKnowledge(q) });
  }

  if (route === 'GET /api/workflows') {
    return sendJson(res, 200, await loadWorkflows());
  }

  if (route === 'POST /api/workflows') {
    let body;
    try {
      body = await readJsonBody(req);
    } catch {
      return sendJson(res, 400, { error: 'invalid JSON body' });
    }
    const title = typeof body.title === 'string' ? body.title.trim() : '';
    if (!title) return sendJson(res, 400, { error: 'title is required' });
    const workflows = await loadWorkflows();
    const workflow = {
      id: crypto.randomUUID(),
      title: title.slice(0, 200),
      status: 'todo',
      createdAt: new Date().toISOString(),
    };
    workflows.push(workflow);
    await saveWorkflows(workflows);
    return sendJson(res, 201, workflow);
  }

  if (req.method === 'PATCH' && /^\/api\/workflows\/[\w-]+$/.test(url.pathname)) {
    const id = url.pathname.split('/').pop();
    let body;
    try {
      body = await readJsonBody(req);
    } catch {
      return sendJson(res, 400, { error: 'invalid JSON body' });
    }
    if (!WORKFLOW_STATUSES.includes(body.status)) {
      return sendJson(res, 400, { error: `status must be one of ${WORKFLOW_STATUSES.join(', ')}` });
    }
    const workflows = await loadWorkflows();
    const workflow = workflows.find((w) => w.id === id);
    if (!workflow) return sendJson(res, 404, { error: 'workflow not found' });
    workflow.status = body.status;
    await saveWorkflows(workflows);
    return sendJson(res, 200, workflow);
  }

  return sendJson(res, 404, { error: 'not found' });
}

function serveStatic(res, urlPath) {
  const safePath = path.normalize(urlPath).replace(/^(\.\.[/\\])+/, '');
  let filePath = path.join(PUBLIC_DIR, safePath === '/' || safePath === '.' ? 'index.html' : safePath);
  if (!filePath.startsWith(PUBLIC_DIR)) {
    res.writeHead(403);
    return res.end('forbidden');
  }
  fs.stat(filePath, (err, stat) => {
    if (!err && stat.isDirectory()) filePath = path.join(filePath, 'index.html');
    fs.readFile(filePath, (readErr, data) => {
      if (readErr) {
        // SPA-style fallback: unknown paths get the dashboard shell.
        return fs.readFile(path.join(PUBLIC_DIR, 'index.html'), (fbErr, fallback) => {
          if (fbErr) {
            res.writeHead(404);
            return res.end('not found');
          }
          res.writeHead(200, { 'Content-Type': MIME['.html'] });
          res.end(fallback);
        });
      }
      const ext = path.extname(filePath).toLowerCase();
      res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream' });
      res.end(data);
    });
  });
}

const server = http.createServer((req, res) => {
  const url = new URL(req.url, `http://${req.headers.host || 'localhost'}`);
  if (url.pathname.startsWith('/api/')) {
    handleApi(req, res, url).catch((err) => sendJson(res, 500, { error: err.message }));
  } else {
    serveStatic(res, decodeURIComponent(url.pathname));
  }
});

if (require.main === module) {
  server.listen(PORT, () => {
    console.log(`Agentic OS running on http://localhost:${PORT}`);
    console.log(
      `Modules — YouTube: ${process.env.YOUTUBE_API_KEY ? 'live' : 'demo'}, ` +
        `Hermes: ${process.env.HERMES_URL ? 'live' : 'demo'}, Knowledge: local`
    );
  });
}

module.exports = { server, searchKnowledge, compactNumber };
