# PLANNING — Agentic OS

> SEED-style plan (project type: **Application**, rigor: deep). This document is
> the build contract; the phases below mirror the PAUL plan → apply → unify loop.

## 1. Vision
A unified, mobile-optimized dashboard — an "Agentic OS" — that acts as an
on-the-go command center for a content business: live channel metrics, a chat
line to an autonomous Hermes agent, searchable business knowledge, and a
workflow tracker.

## 2. Users & jobs
- **Owner (mobile):** glance at subscriber/view numbers, message the agent,
  check workflow state from a phone.
- **Agents (Hermes via MCP):** query the knowledge base, update workflows.

## 3. Scope
**In:** dashboard UI, YouTube metrics, Hermes chat proxy, knowledge search,
workflow CRUD, Railway deployment.
**Out (this phase):** auth, multi-user, payments, write-access for agents to the
knowledge base.

## 4. Architecture
- **Runtime:** Node.js ≥ 18, zero npm dependencies (`node:http`, global `fetch`).
- **Frontend:** single-file `public/index.html`, vanilla JS, mobile-first with a
  bottom tab bar, light/dark via `prefers-color-scheme`.
- **State:** workflows persisted to `data/workflows.json`; knowledge base is
  plain markdown in `knowledge/`.
- **Config:** everything via env vars; every module has a demo-mode fallback so
  the app runs with zero configuration.

## 5. Data model
- `Workflow { id, title, status: todo|active|done, createdAt }`
- `KnowledgeDoc { file, title, text }` (derived from `knowledge/*.md`)
- `Metrics { channel { title, subscribers, views, videos }, recentVideos[] }`

## 6. API surface
| Method | Path | Purpose |
|---|---|---|
| GET | `/api/health` | uptime + which modules are live vs demo |
| GET | `/api/metrics/youtube` | channel stats + recent video views (5-min cache) |
| POST | `/api/hermes/chat` | proxy `{message}` to the Hermes VPS endpoint |
| GET | `/api/knowledge/docs` | list knowledge documents |
| GET | `/api/knowledge/search?q=` | ranked full-text search with snippets |
| GET/POST | `/api/workflows` | list / create workflows |
| PATCH | `/api/workflows/:id` | update workflow status |

## 7. Build phases (PAUL loop)
- **Phase 1 — Foundation:** scaffold server, static shell, health endpoint. ✅
- **Phase 2 — Live metrics:** YouTube Data API v3 integration + chart. ✅
- **Phase 3 — Hermes link:** chat proxy with token auth + timeout. ✅
- **Phase 4 — Graphify search:** knowledge listing + ranked search. ✅
- **Phase 5 — Ship:** Railway config, env template, docs, smoke tests. ✅

## 8. Environment
| Var | Required | Purpose |
|---|---|---|
| `PORT` | no (3000) | server port; Railway injects it |
| `YOUTUBE_API_KEY` | no | enables live metrics |
| `YOUTUBE_CHANNEL_ID` | no | channel to report on |
| `HERMES_URL` | no | Hermes agent chat endpoint |
| `HERMES_TOKEN` | no | bearer token for Hermes |

## 9. Quality gates
- `npm test` runs the HTTP smoke tests (health, metrics shape, knowledge search,
  workflow create/update, static shell).
- No secrets in the repo; `.env` is gitignored and `.env.example` documents keys.

## 10. Risks & mitigations
- **YouTube quota:** 5-minute response cache; only 3 API calls per refresh.
- **Hermes downtime:** 30s timeout, error surfaced in chat instead of hanging.
- **Ephemeral disk on Railway:** `data/` is regenerated on boot; attach a volume
  at `/app/data` if workflow persistence across deploys matters.
