# Knowledge Hub

A cross-project knowledge graph of all my repositories, built with
[Graphify](https://github.com/Graphify-Labs/graphify). Every function, class,
file, and dependency across every project lives in one queryable graph, so an
AI assistant (or you) can answer "where is X / what talks to Y / what breaks
if I change Z" without re-reading the source.

## What's in the graph

| Project | Nodes | What it is |
|---|---|---|
| career-command-center | 2,516 | Django + Angular job-hunt automation |
| resume-builder | 703 | JS/Python resume builder |
| f1-app | 588 | Java/JS F1 app |
| attendance-management-system | 158 | Python attendance system |
| Mail-Resume_Automation (SasarkSambhavam) | 26 | Flask mail/resume automation |

**Merged: 3,991 nodes · 7,086 edges · 329 communities.**
Every node carries a `repo` tag and a namespaced ID
(`career-command-center::backend_automation_service_app`), so cross-project
queries stay unambiguous.

Measured with `graphify benchmark`: **~58.6x fewer tokens per query** than
reading the corpus naively (~266k tokens naive vs ~4.5k per graph query).

## Files

- `graphs/all-projects-graph.json` — the merged graph (query this)
- `graphify-out/graph3d.html` — 3D interactive viewer (WebGL): orbit/zoom, search,
  project filters, click a node for its connections, animated link particles
- `graphify-out/graph.html` — the stock 2D visualization
- `graphify-out/GRAPH_REPORT.md` — merged-graph highlights
- `reports/*.md` — per-project graph reports
- `refresh.sh` — rebuild everything from the latest code

## Querying

Install the CLI once (`uv tool install graphifyy` or `pipx install graphifyy`), then:

```bash
# What is X and what touches it?
graphify explain "AutomationViewSet" --graph graphs/all-projects-graph.json

# Answer a question by graph traversal (budget-capped output)
graphify query "how does resume generation work" --graph graphs/all-projects-graph.json

# Shortest path between two things (works across repos)
graphify path "views.py" "ResumeBuilderComponent" --graph graphs/all-projects-graph.json

# What is impacted if I change X?
graphify affected "UserSerializer" --graph graphs/all-projects-graph.json
```

In Claude Code / Cursor / Codex, run `graphify install` once and then use
`/graphify` inside any of the projects.

## Refreshing

```bash
./refresh.sh            # clones/pulls all repos, rebuilds each graph, re-merges
```

The code pass is pure tree-sitter (local, deterministic, zero LLM tokens), so
refreshing is free and takes under a minute.
