# Integrations

How each external system connects to the Agentic OS.

## YouTube Data API v3
Set `YOUTUBE_API_KEY` and `YOUTUBE_CHANNEL_ID`. Get a key from the Google Cloud
Console (enable "YouTube Data API v3", create an API key). The server caches
responses for 5 minutes to stay inside the free quota (10,000 units/day).

## Hermes agent
Set `HERMES_URL` to the chat endpoint of the Hermes agent on your VPS (for
example `https://your-vps.example.com/chat`) and optionally `HERMES_TOKEN` for a
bearer token. The dashboard POSTs `{"message": "..."}` and expects a JSON reply
containing a `reply`, `response`, or `message` field.

## Graphify / Obsidian
Drop markdown exports of your vault into `knowledge/`. The search endpoint scores
documents by term frequency with a title boost. For a full graph-aware RAG,
point Graphify at this folder and expose it to Hermes via MCP.

## Railway
Connect the GitHub repo in Railway, and it deploys on every push. No build step
is needed; `npm start` runs the server on the assigned `PORT`.
