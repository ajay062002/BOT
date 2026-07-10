# Agentic OS

A unified, mobile-optimized command center for a content business: live YouTube
metrics, a chat line to a Hermes agent on your VPS, searchable business
knowledge (the "Graphify brain"), and a workflow tracker — all in one
dashboard, deployable to Railway in minutes.

Built following the three-step framework: **the Brain** (a markdown knowledge
base in `knowledge/`), **the Build** (a zero-dependency Node.js app), and
**the Ship** (Railway deployment). The full SEED-style plan is in
[PLANNING.md](PLANNING.md).

## Quick start

```bash
npm start          # http://localhost:3000
npm test           # HTTP smoke tests
```

That's it — no `npm install` needed (zero dependencies, Node ≥ 18). Every
module runs in **demo mode** until you add credentials, so the dashboard works
immediately.

## Dashboard tabs

| Tab | What it does |
|---|---|
| **Overview** | Hero stats + which modules are connected vs in demo mode |
| **Metrics** | Channel subscribers/views/videos + a chart of recent video views |
| **Agent** | Chat with the Hermes agent running on your VPS |
| **Knowledge** | Search the markdown knowledge base in `knowledge/` |
| **Workflows** | Add and track business workflows (todo → active → done) |

## Going live

Copy `.env.example` to `.env` (locally) or set variables in Railway:

| Variable | Enables |
|---|---|
| `YOUTUBE_API_KEY` + `YOUTUBE_CHANNEL_ID` | Live metrics from the YouTube Data API v3 |
| `HERMES_URL` (+ optional `HERMES_TOKEN`) | Real agent chat via your VPS endpoint |

**YouTube key:** Google Cloud Console → enable *YouTube Data API v3* → create an
API key. Responses are cached 5 minutes to protect your quota.

**Hermes:** the dashboard POSTs `{"message": "..."}` to `HERMES_URL` and renders
the `reply` / `response` / `message` field of the JSON answer.

**Knowledge base:** drop markdown files into `knowledge/` — they're searchable
instantly. Export your Obsidian/Graphify vault there for a portable brain.

## Deploy on Railway

1. Push this repo to GitHub.
2. In [Railway](https://railway.com): *New Project → Deploy from GitHub repo*.
3. Add your environment variables under *Variables*.
4. Railway builds with Nixpacks and health-checks `/api/health` (see
   `railway.json`). Open the generated domain on your phone — the UI is
   mobile-first with a bottom tab bar.

> Note: `data/workflows.json` lives on the service filesystem. Attach a Railway
> volume at `/app/data` if you want workflows to survive redeploys.

## API

| Method | Path | Purpose |
|---|---|---|
| GET | `/api/health` | uptime + module connection status |
| GET | `/api/metrics/youtube` | channel stats + recent videos |
| POST | `/api/hermes/chat` | `{message}` → agent reply |
| GET | `/api/knowledge/docs` | list knowledge documents |
| GET | `/api/knowledge/search?q=` | ranked search with snippets |
| GET / POST | `/api/workflows` | list / create workflows |
| PATCH | `/api/workflows/:id` | update status (`todo`/`active`/`done`) |
