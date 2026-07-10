# Graph Report - Mail-Resume_Automation-main  (2026-07-10)

## Corpus Check
- 4 files · ~2,747 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 26 nodes · 35 edges · 8 communities (4 shown, 4 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 1 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c1367b65`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- app.py
- get_next_subfolder
- main
- test_render.py
- is_list_style
- normalize_bullets
- tighten_list_paragraph

## God Nodes (most connected - your core abstractions)
1. `normalize_bullets()` - 7 edges
2. `main()` - 7 edges
3. `tighten_list_paragraph()` - 4 edges
4. `is_list_style()` - 4 edges
5. `get_next_subfolder()` - 4 edges
6. `JDEmailRequest` - 3 edges
7. `ResumeRequest` - 3 edges
8. `download_resume()` - 3 edges
9. `remove_paragraph()` - 3 edges
10. `draft_email()` - 2 edges

## Surprising Connections (you probably didn't know these)
- `main()` --calls--> `tighten_list_paragraph()`  [EXTRACTED]
  test_render.py → test_render.py  _Bridges community 7 → community 2_
- `normalize_bullets()` --calls--> `tighten_list_paragraph()`  [EXTRACTED]
  test_render.py → test_render.py  _Bridges community 7 → community 6_
- `main()` --calls--> `is_list_style()`  [EXTRACTED]
  test_render.py → test_render.py  _Bridges community 5 → community 2_
- `normalize_bullets()` --calls--> `is_list_style()`  [EXTRACTED]
  test_render.py → test_render.py  _Bridges community 5 → community 6_
- `normalize_bullets()` --calls--> `remove_paragraph()`  [EXTRACTED]
  test_render.py → test_render.py  _Bridges community 3 → community 6_

## Import Cycles
- None detected.

## Communities (8 total, 4 thin omitted)

### Community 0 - "app.py"
Cohesion: 0.43
Nodes (5): draft_email(), generate_resume(), JDEmailRequest, ResumeRequest, BaseModel

### Community 1 - "get_next_subfolder"
Cohesion: 0.40
Nodes (5): download_resume(), Serve a generated resume file for download., Path, get_next_subfolder(), Find the next numeric subfolder under base, e.g., 1, 2, 3...

### Community 2 - "main"
Cohesion: 0.67
Nodes (3): Document, main(), Main resume generation logic.

## Knowledge Gaps
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `get_next_subfolder()` connect `get_next_subfolder` to `main`, `test_render.py`?**
  _High betweenness centrality (0.473) - this node is a cross-community bridge._
- **Why does `download_resume()` connect `get_next_subfolder` to `app.py`?**
  _High betweenness centrality (0.423) - this node is a cross-community bridge._
- **Why does `main()` connect `main` to `get_next_subfolder`, `test_render.py`, `is_list_style`, `normalize_bullets`, `tighten_list_paragraph`?**
  _High betweenness centrality (0.246) - this node is a cross-community bridge._
- **What connects `Serve a generated resume file for download.`, `Tighten line spacing and justify bullet paragraphs.`, `Check if a paragraph uses a list-like style.` to the rest of the system?**
  _7 weakly-connected nodes found - possible documentation gaps or missing edges._