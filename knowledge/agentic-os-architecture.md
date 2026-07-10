# Agentic OS Architecture

The Agentic OS is a unified command center built around three layers:

## The Brain
An agentic knowledge base of markdown documents (this `knowledge/` folder). In the
full setup this is an Obsidian vault indexed by Graphify, which maps relationships
between notes and code so agents can query it as a local RAG source. The dashboard's
Knowledge tab searches these documents directly.

## The Build
The application layer: a zero-dependency Node.js server (`server.js`) serving a
mobile-first dashboard (`public/index.html`). Modules:

- **Metrics** — pulls channel analytics from the YouTube Data API v3.
- **Agent** — routes chat messages to a Hermes agent running on a VPS.
- **Knowledge** — full-text search over this folder.
- **Workflows** — a lightweight persisted task board for business processes.

## The Ship
Deployment on Railway. The server binds to `process.env.PORT`, has no native
dependencies, and every module degrades gracefully to demo mode when its
credentials are missing, so the app is deployable before any integration is wired.
