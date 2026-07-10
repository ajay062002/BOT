# Graph Report - career-command-center  (2026-07-10)

## Corpus Check
- 140 files · ~138,099 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2516 nodes · 4760 edges · 174 communities (105 shown, 69 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 364 edges (avg confidence: 0.52)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c1367b65`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- UserSerializer
- index-CDWIGAMO.js
- SubmissionsComponent
- xt
- tn
- D
- app.js
- Xe
- Ni
- Ct
- ot
- claude_apply_bot.py
- He
- .clone
- .copy
- F1GameComponent
- Game
- gi
- ResumeVersionsComponent
- SpeechBubble
- DashboardService
- .constructor
- ControlPanel
- JobDiscoveryComponent
- .dispatchEvent
- RobotMascot
- web_server.py
- AuthService
- so
- Ys
- rt
- On
- cp
- nc
- devDependencies
- VpnService
- ChatBackend
- Claude Application Bot
- ResumePromptsComponent
- dependencies
- ChatWindow
- ResumeBuilderComponent
- .normalize
- Ne
- ._scene_back
- .paintEvent
- StudyComponent
- .setAttribute
- co
- main.py
- pl
- AppController
- .render
- BotEngine
- popup.js
- MainLayoutComponent
- JobService
- _i
- Ge
- .dot
- sn
- manifest.json
- AppComponent
- UserManagementComponent
- tc
- main
- reminders.component.ts
- LinkedInBot
- NvoidsBot
- ResumeService
- Fs
- matcher.py
- scraper.py
- options
- Job
- app.py
- history.py
- LinkedIn Jobs MCP Scraper
- ProfileComponent
- hp
- .remove
- jo
- wt
- 🚀 Key Features
- Career Command Center
- email_drafter.py
- generator.py
- production
- package.json
- RemindersComponent
- RtrDialogComponent
- development
- DashboardComponent
- Career Command Center — Feature Documentation
- career-command-center-frontend
- CareerCommandCenterFrontend
- ReminderDialogComponent
- .decompose
- phone.py
- fetch_nv_detail
- architect
- job.models.ts
- config.py
- engine.py
- ._load_assets
- config.py
- injected.js
- BilldocComponent
- Ui
- resume_service.py
- angular.json
- .closestPointToPoint
- .premultiply
- vercel.json
- assets
- ngsw-config.json
- .applyQuaternion
- Fa
- .w
- Ko
- CoreConfig
- login.py
- Cl
- df
- ic
- .getVertexPosition
- sc
- zp
- main
- @angular/compiler
- @angular/core
- @angular/forms
- @angular/platform-browser
- @angular/service-worker
- build.sh
- README.md
- run.sh script
- setup.sh
- web.sh
- export_to_new_repo.sh
- build.sh
- 0001_initial.py
- 0002_job_user_reminder_user_rtr_user_studysession_user_and_more.py
- 0003_scrapedjob.py
- 0004_remove_scrapedjob_description_and_more.py
- 0005_resumeprompt_resumeversion.py
- 0006_user_vpn_fields.py
- 0007_user_can_see_billdoc.py
- 0008_alter_user_can_see_billdoc.py
- asgi.py
- wsgi.py
- rxjs
- three
- karma-jasmine-html-reporter
- ec
- Fl
- Qo
- uf
- up
- wl
- environment.prod.ts

## God Nodes (most connected - your core abstractions)
1. `D` - 76 edges
2. `RobotMascot` - 65 edges
3. `Xe` - 55 edges
4. `ot` - 54 edges
5. `xt` - 47 edges
6. `Ct` - 47 edges
7. `rt` - 39 edges
8. `gi` - 38 edges
9. `He` - 38 edges
10. `Ni` - 35 edges

## Surprising Connections (you probably didn't know these)
- `ChatWindow` --uses--> `ChatBackend`  [INFERRED]
  backend/automation-service/bot_app/chat_window.py → backend/automation-service/bot_app/chat_backend.py
- `ChatBody` --uses--> `ChatBackend`  [INFERRED]
  backend/automation-service/bot_app/web_server.py → backend/automation-service/bot_app/chat_backend.py
- `LoginBody` --uses--> `ChatBackend`  [INFERRED]
  backend/automation-service/bot_app/web_server.py → backend/automation-service/bot_app/chat_backend.py
- `set_settings()` --calls--> `ChatBackend`  [INFERRED]
  backend/automation-service/bot_app/web_server.py → backend/automation-service/bot_app/chat_backend.py
- `SettingsBody` --uses--> `ChatBackend`  [INFERRED]
  backend/automation-service/bot_app/web_server.py → backend/automation-service/bot_app/chat_backend.py

## Import Cycles
- None detected.

## Communities (174 total, 69 thin omitted)

### Community 0 - "UserSerializer"
Cohesion: 0.05
Nodes (57): AbstractUser, Command, BaseCommand, Emergency admin creation + full data migration. Creates a guaranteed-access admi, Command, BaseCommand, Job, JobWorkflowStatus (+49 more)

### Community 1 - "index-CDWIGAMO.js"
Cohesion: 0.02
Nodes (55): Ad, ao, as, Ba, bi, bn, bp, cs (+47 more)

### Community 2 - "SubmissionsComponent"
Cohesion: 0.05
Nodes (17): RTR, RTRStatus, RtrVendorGroup, Submission, SubmissionStatus, VendorGroup, RtrService, Injectable (+9 more)

### Community 3 - "xt"
Cohesion: 0.05
Nodes (5): Bt, Ha, Xa, xt, Zn

### Community 4 - "tn"
Cohesion: 0.06
Nodes (6): kp(), lo(), Pt(), tn, vi(), Xp()

### Community 6 - "app.js"
Cohesion: 0.11
Nodes (47): adjustZoom(), annotEditor, applyMetadataToDoc(), applyZoom(), buildCustomFormHelp(), buildFormFields(), buildScannedSidebar(), checkAccessControl() (+39 more)

### Community 8 - "Ni"
Cohesion: 0.07
Nodes (8): ei, en, Hi, Ht, ln, Ni, Qn, wi

### Community 9 - "Ct"
Cohesion: 0.09
Nodes (6): Ct, Ft, Pd(), Ut, Ye(), Zo()

### Community 11 - "claude_apply_bot.py"
Cohesion: 0.11
Nodes (32): apply_to_job(), applying_card(), collect_job_urls(), error(), info(), login(), print_summary(), ╔══════════════════════════════════════╗ ║       Claude Application Bot        ║ (+24 more)

### Community 12 - "He"
Cohesion: 0.10
Nodes (8): Ds(), He, oi(), sl(), Tt, We, wf(), zs()

### Community 13 - ".clone"
Cohesion: 0.06
Nodes (5): ac, cc, ll, Vl, xl

### Community 14 - ".copy"
Cohesion: 0.09
Nodes (6): In, kt, pa, rl(), un, Ve

### Community 15 - "F1GameComponent"
Cohesion: 0.11
Nodes (6): F1GameComponent, F1Team, F1Track, Component, ViewChild, HostListener

### Community 16 - "Game"
Cohesion: 0.10
Nodes (8): AIController, buildCarMesh(), buildTrack(), CarPhysics, CIRCUITS, Game, ParticleSystem, TEAMS

### Community 18 - "ResumeVersionsComponent"
Cohesion: 0.10
Nodes (5): ResumeVersion, ResumeVersionService, Injectable, ResumeVersionsComponent, Component

### Community 19 - "SpeechBubble"
Cohesion: 0.10
Nodes (6): QWidget, Play this hero's signature celebration (goal, six, web-flip, thunder…)., scout found a job — play a signature move and show the contact., Trigger a signature move on demand (menu)., Remove the custom image and go back to the drawn cartoon., SpeechBubble

### Community 20 - "DashboardService"
Cohesion: 0.18
Nodes (9): DashboardSummary, JobStatusCount, RtrTimelineEntry, StudyTrend, VendorPerformance, DashboardService, Injectable, AnalyticsComponent (+1 more)

### Community 21 - ".constructor"
Cohesion: 0.09
Nodes (8): cn, dp(), hn, ip, nl(), pi(), $s, Xd()

### Community 22 - "ControlPanel"
Cohesion: 0.11
Nodes (11): ControlPanel, DropZone, QWidget, Control panel — dark-themed, floating window. Handles resume upload, template up, A labelled area that accepts file drops and has an 'Add' button., _section_label(), _sep(), QDragEnterEvent (+3 more)

### Community 23 - "JobDiscoveryComponent"
Cohesion: 0.13
Nodes (7): JobDiscoveryService, ScrapedJob, Injectable, JobDiscoveryComponent, JobInfoDialogComponent, Component, Inject

### Community 24 - ".dispatchEvent"
Cohesion: 0.10
Nodes (4): $a, Bs, qa, qp()

### Community 25 - "RobotMascot"
Cohesion: 0.10
Nodes (6): Capsule arms in blue sleeves holding the bat; pose per action., Boot-thruster flame: layered orange→yellow→white cones, flickering., Mjölnir: bevelled head, wrapped handle, leather strap., Open a one-time sign-in script (own console so you see the Enter prompt)., Iron Man roams the ENTIRE screen with a smooth wandering flight., RobotMascot

### Community 26 - "web_server.py"
Cohesion: 0.11
Nodes (14): chat(), ChatBody, login(), LoginBody, _on_applying(), _on_result(), BaseModel, Phone / web dashboard for the Claude Application Bot.  Runs a small FastAPI serv (+6 more)

### Community 27 - "AuthService"
Cohesion: 0.12
Nodes (9): authInterceptor(), AuthService, Injectable, User, LoginComponent, Component, RegisterComponent, Component (+1 more)

### Community 28 - "so"
Cohesion: 0.09
Nodes (7): da, Ii, Ns(), rn, so, Xi, zl

### Community 29 - "Ys"
Cohesion: 0.09
Nodes (6): Dn, ja, ml, qi, yl(), Ys()

### Community 32 - "cp"
Cohesion: 0.10
Nodes (22): af(), Bd(), bo(), cp(), ef(), ep(), Gd(), hl (+14 more)

### Community 33 - "nc"
Cohesion: 0.09
Nodes (13): al, Fd(), Jf(), mi, mn(), nc, Nd(), tl() (+5 more)

### Community 34 - "devDependencies"
Cohesion: 0.09
Nodes (23): @angular/cli, @angular/compiler-cli, @angular-devkit/build-angular, devDependencies, @angular/cli, @angular/compiler-cli, @angular-devkit/build-angular, jasmine-core (+15 more)

### Community 35 - "VpnService"
Cohesion: 0.13
Nodes (6): Injectable, VpnService, VpnStatus, Component, US_STATES, VpnComponent

### Community 36 - "ChatBackend"
Cohesion: 0.13
Nodes (11): ChatBackend, claude_cli_available(), Chat backend for Jarvis — the desktop job-search AI.  Primary:  NVIDIA NIM free, Chat router. prefer='nvidia' (free, no Claude tokens) or 'claude'., System prompt + live crew status so Jarvis knows what's running., Answer. If on_chunk is given and NVIDIA is used, stream partial text., _md(), QThread (+3 more)

### Community 37 - "Claude Application Bot"
Cohesion: 0.09
Nodes (20): Deploy on Fly.io (alternative), Deploy on Render (recommended — free tier, GitHub auto-deploy), Deploy the bot to an always-on cloud server, One-click deploy, Run the Docker image anywhere (VPS), Security notes, What works well in the cloud vs. what to know, Claude Application Bot (+12 more)

### Community 38 - "ResumePromptsComponent"
Cohesion: 0.16
Nodes (5): ResumePrompt, ResumePromptService, Injectable, ResumePromptsComponent, Component

### Community 39 - "dependencies"
Cohesion: 0.10
Nodes (21): @angular/animations, @angular/cdk, @angular/common, @angular/material, @angular/platform-browser-dynamic, @angular/router, chart.js, dependencies (+13 more)

### Community 40 - "ChatWindow"
Cohesion: 0.18
Nodes (5): ChatWindow, QWidget, Handle bot-control commands locally. Returns a reply, or None., One chat bubble: user → coral, right-aligned; Jarvis → dark card, left., Re-render the whole transcript as chat bubbles (plus a streaming reply).

### Community 44 - "._scene_back"
Cohesion: 0.14
Nodes (10): _ease_in(), _ease_out(), _lerp(), Desktop companion — a cartoon athlete that roams your screen, does random action, Sphere-shaded ball: radial gradient lit from top-left + specular dot., Fast start, gentle finish — how a struck ball actually decelerates., Slow start, fast finish — a bowler's run-up / wind-up., Goal drawn as a 3D box: near post tall, far post smaller and raised,         wit (+2 more)

### Community 45 - ".paintEvent"
Cohesion: 0.20
Nodes (7): Capsule arms with red sleeves; pose per action., A jagged lightning bolt between two points (+ soft glow)., Render a dropped image/GIF with bob + a celebration scale-pop., Shared pose params derived from the current action/frame., A limb drawn as an outlined capsule (round-cap stroke over an outline)., Shared face: shaded head, ear, brows, real eyes with pupils, nose, mouth., QPainter

### Community 46 - "StudyComponent"
Cohesion: 0.19
Nodes (5): StudySession, StudyService, Injectable, StudyComponent, Component

### Community 47 - ".setAttribute"
Cohesion: 0.15
Nodes (5): ci, el(), Ms, Mt, vp()

### Community 48 - "co"
Cohesion: 0.21
Nodes (4): co, ho(), ri(), uo()

### Community 49 - "main.py"
Cohesion: 0.14
Nodes (9): _arc_reactor_icon(), BotThread, LinkedInThread, NvoidsThread, QThread, Claude Application Bot — entry point.  One command:  python main.py First run  :, Draw the arc-reactor app icon (used for the panel + chat windows)., The scout's bot — scrape nvoids for jobs + recruiter contacts. (+1 more)

### Community 51 - "AppController"
Cohesion: 0.23
Nodes (3): AppController, main(), Jarvis 'status' command — what's running + last results.

### Community 52 - ".render"
Cohesion: 0.24
Nodes (5): ap(), eo, kl, _o, Pe()

### Community 53 - "BotEngine"
Cohesion: 0.24
Nodes (4): BotEngine, True if we appear to be on a Dice login/sign-in page (not authed)., Wait for the user to finish signing in (captcha/2FA included)., Save a debug screenshot so 'not applying' runs can be diagnosed.

### Community 54 - "popup.js"
Cohesion: 0.12
Nodes (13): btnIcon, btnLabel, citySelect, connectBtn, populateCities(), QUICK_STATES, quickGrid, stateSelect (+5 more)

### Community 55 - "MainLayoutComponent"
Cohesion: 0.13
Nodes (3): MainLayoutComponent, Component, ViewChild

### Community 56 - "JobService"
Cohesion: 0.15
Nodes (4): JobService, Injectable, JobFormComponent, Component

### Community 57 - "_i"
Cohesion: 0.12
Nodes (3): bl, _i, Ol

### Community 59 - ".dot"
Cohesion: 0.20
Nodes (3): es(), Gt, Ws

### Community 60 - "sn"
Cohesion: 0.13
Nodes (3): Ga, sn, Va

### Community 61 - "manifest.json"
Cohesion: 0.12
Nodes (15): action, default_popup, default_title, background, service_worker, content_scripts, description, host_permissions (+7 more)

### Community 62 - "AppComponent"
Cohesion: 0.17
Nodes (6): AppComponent, Component, appConfig, routes, AuthGuard, Injectable

### Community 63 - "UserManagementComponent"
Cohesion: 0.14
Nodes (4): ChangePasswordDialogComponent, Component, Inject, UserManagementComponent

### Community 65 - "main"
Cohesion: 0.21
Nodes (14): get_next_subfolder(), is_list_style(), main(), normalize_bullets(), Path, Find the next numeric subfolder under base, e.g., 1, 2, 3..., Main resume generation logic., Tighten line spacing and justify bullet paragraphs. (+6 more)

### Community 66 - "reminders.component.ts"
Cohesion: 0.24
Nodes (4): Reminder, ReminderType, ReminderService, Injectable

### Community 67 - "LinkedInBot"
Cohesion: 0.21
Nodes (6): _first_text(), LinkedInBot, LinkedIn job scout (runs under Kohli with nvoids).  Uses your DUMMY account's sa, Lazy-scroll the filtered search and return NEW job cards (list info)., Open each job, grab the full JD, filter, extract recruiter emails., One-time LinkedIn sign-in (use your DUMMY account).  Opens a real browser with y

### Community 68 - "NvoidsBot"
Cohesion: 0.21
Nodes (9): _decode_cfemail(), _emails_from(), _fetch_detail(), _get(), NvoidsBot, nvoids job-finder (Kohli's bot).  Scrapes nvoids.com for contract roles and pull, GET with small retries — nvoids occasionally drops a connection., Decode a Cloudflare-protected email (data-cfemail attribute). (+1 more)

### Community 71 - "matcher.py"
Cohesion: 0.29
Nodes (12): _extract(), _keyword_match(), _keyword_score(), _load_resumes(), match_resume(), _nvidia_match(), Path, Resume scorer — NVIDIA NIM (meta/llama-3.1-8b-instruct) with keyword fallback. (+4 more)

### Community 72 - "scraper.py"
Cohesion: 0.18
Nodes (11): _first_card_selector(), _first_text(), LinkedIn job-list scraper (Playwright).  Reuses the saved session from login.py,, scrape(), linkedin_status(), LinkedIn Jobs MCP server.  Exposes tools an MCP client (Claude Desktop / Claude, Scrape job listings from LinkedIn using your saved search filter.      Args:, Launch the interactive (headful) LinkedIn login so you can sign in and     clear (+3 more)

### Community 73 - "options"
Cohesion: 0.21
Nodes (13): options, browser, index, inlineStyleLanguage, outputPath, polyfills, scripts, styles (+5 more)

### Community 74 - "Job"
Cohesion: 0.23
Nodes (4): Job, JobsComponent, Component, ViewChild

### Community 75 - "app.py"
Cohesion: 0.27
Nodes (9): draft_email(), generate_resume_endpoint(), JDEmailRequest, BaseModel, ResumeRequest, build_gmail_url(), extract_email(), extract_job_title() (+1 more)

### Community 76 - "history.py"
Cohesion: 0.36
Nodes (10): company_applied(), domain_contacted(), link_seen(), _load(), mark_applied(), mark_emailed(), mark_seen(), Persistent "already contacted / applied" history, so repeated scheduled runs nev (+2 more)

### Community 77 - "LinkedIn Jobs MCP Scraper"
Cohesion: 0.18
Nodes (10): Claude Code CLI, Claude Desktop  (recommended), Connect to an MCP client, LinkedIn Jobs MCP Scraper, Log in once, Provide credentials + your filter URL, Setup, Tools exposed (+2 more)

### Community 80 - ".remove"
Cohesion: 0.18
Nodes (6): fp(), gl, mp(), _p(), wp(), Yp()

### Community 83 - "🚀 Key Features"
Cohesion: 0.18
Nodes (10): 1. Dashboard (The Nerve Center), 2. RTR Tracker (Ready To Represent), 3. Submissions Module, 4. Jobs, Study, & Reminders, Backend (Java Spring Boot), Career Command Center — Project Overview, 💡 Developer Notes, Frontend (Angular 18) (+2 more)

### Community 84 - "Career Command Center"
Cohesion: 0.18
Nodes (10): API Endpoints, Backend, Career Command Center, Environment Variables, Frontend, Project Structure, Running Locally, Source (+2 more)

### Community 85 - "email_drafter.py"
Cohesion: 0.31
Nodes (9): draft_for_job(), draft_for_jobs(), first_email(), _gmail_url(), load_template(), Email drafter — opens a pre-filled Gmail compose draft per recruiter.  Uses the, Open Gmail drafts for up to `limit` jobs, skipping vendors already contacted., Return (subject, cc, body) from email_template.txt or sensible defaults.      Fi (+1 more)

### Community 86 - "generator.py"
Cohesion: 0.29
Nodes (9): _client(), generate_resume(), Path, Resume generator — DeepSeek R1 via NVIDIA NIM free API. Called when no existing, DeepSeek R1 wraps its reasoning in <think>…</think> — remove it., Generate a tailored resume with DeepSeek R1 and save it to resumes/.     Returns, _save_docx(), _strip_think_tags() (+1 more)

### Community 87 - "production"
Cohesion: 0.20
Nodes (10): serve, production, budgets, buildTarget, fileReplacements, outputHashing, serviceWorker, builder (+2 more)

### Community 88 - "package.json"
Cohesion: 0.20
Nodes (9): name, private, scripts, build, ng, start, test, watch (+1 more)

### Community 90 - "RtrDialogComponent"
Cohesion: 0.24
Nodes (3): RtrDialogComponent, Component, Inject

### Community 91 - "development"
Cohesion: 0.22
Nodes (9): build, builder, configurations, defaultConfiguration, development, buildTarget, extractLicenses, optimization (+1 more)

### Community 93 - "Career Command Center — Feature Documentation"
Cohesion: 0.25
Nodes (7): 1. Automatic RTR-to-Submission Promotion 🔄, 2. Integrated Vendor Performance Analytics 📊, 3. Data Cleansing & Fresh Start 🧹, 4. Technical Enhancements 🛠️, Career Command Center — Feature Documentation, How it works:, Key Metrics Added:

### Community 94 - "career-command-center-frontend"
Cohesion: 0.25
Nodes (8): prefix, projectType, root, schematics, sourceRoot, career-command-center-frontend, style, @schematics/angular:component

### Community 95 - "CareerCommandCenterFrontend"
Cohesion: 0.25
Nodes (7): Build, CareerCommandCenterFrontend, Code scaffolding, Development server, Further help, Running end-to-end tests, Running unit tests

### Community 96 - "ReminderDialogComponent"
Cohesion: 0.29
Nodes (3): ReminderDialogComponent, Component, Inject

### Community 98 - "phone.py"
Cohesion: 0.48
Nodes (6): _arch(), download_cloudflared(), ensure_password(), find_cloudflared(), main(), One-tap phone access.  Starts the web dashboard AND a Cloudflare tunnel together

### Community 99 - "fetch_nv_detail"
Cohesion: 0.38
Nodes (6): extract_contacts(), fetch_nv_detail(), Deep search for email and phone numbers., Worker function for parallel detail scraping with keyword filtering., Turbo Scraper that excludes hotlists and in-person interviews., scrape_nvoids_jobs()

### Community 100 - "architect"
Cohesion: 0.29
Nodes (7): extract-i18n, test, architect, builder, options, buildTarget, builder

### Community 101 - "job.models.ts"
Cohesion: 0.57
Nodes (3): JobPage, JobStatus, WorkMode

### Community 102 - "config.py"
Cohesion: 0.40
Nodes (4): load(), _load_env_file(), Persistent config — saved to bot_config.json next to this file.  You can also se, Tolerant KEY=value parser for secrets.env. Returns config-key → value.

### Community 103 - "engine.py"
Cohesion: 0.33
Nodes (3): One-time Dice sign-in.  Opens a real browser, you sign in to Dice yourself (solv, Bot engine — Dice.com automation in a background thread. Fires callbacks so the, _read_template()

### Community 104 - "._load_assets"
Cohesion: 0.33
Nodes (3): Find mascots/<char>.<ext>; load as QMovie (gif) or QPixmap (static)., Pick an image/GIF and use it for the current character., QPixmap

### Community 105 - "config.py"
Cohesion: 0.40
Nodes (4): _from_file(), load(), Config for the LinkedIn MCP scraper. Precedence: environment variable → linkedin, Merge defaults < file < environment.

### Community 106 - "injected.js"
Cohesion: 0.47
Nodes (3): getCurrentPosition(), makeFakePosition(), watchPosition()

### Community 109 - "resume_service.py"
Cohesion: 0.70
Nodes (4): generate_resume(), reveal_in_explorer(), run_render_script(), update_resume_json()

### Community 110 - "angular.json"
Cohesion: 0.40
Nodes (4): newProjectRoot, projects, $schema, version

### Community 112 - ".closestPointToPoint"
Cohesion: 0.40
Nodes (4): Gs, Hs, jn, Ya

### Community 114 - "vercel.json"
Cohesion: 0.40
Nodes (4): buildCommand, framework, outputDirectory, rewrites

### Community 115 - "assets"
Cohesion: 0.50
Nodes (4): assets, src/assets, src/favicon.ico, src/manifest.webmanifest

### Community 116 - "ngsw-config.json"
Cohesion: 0.50
Nodes (3): assetGroups, index, $schema

## Knowledge Gaps
- **231 isolated node(s):** `build.sh script`, `run.sh script`, `setup.sh script`, `web.sh script`, `export_to_new_repo.sh script` (+226 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **69 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `D` connect `D` to `index-CDWIGAMO.js`, `.decompose`, `tn`, `Ct`, `.normalize`, `hp`, `.fromArray`, `.applyQuaternion`, `.slerp`, `Ge`, `.dot`, `Ys`?**
  _High betweenness centrality (0.020) - this node is a cross-community bridge._
- **Why does `gi` connect `gi` to `index-CDWIGAMO.js`, `tn`, `.normalize`, `.slerp`, `.w`, `Ge`, `so`?**
  _High betweenness centrality (0.020) - this node is a cross-community bridge._
- **Why does `xt` connect `xt` to `index-CDWIGAMO.js`, `nc`, `Ui`, `.clone`, `.remove`, `.constructor`, `.dispatchEvent`, `so`?**
  _High betweenness centrality (0.017) - this node is a cross-community bridge._
- **Are the 5 inferred relationships involving `RobotMascot` (e.g. with `AppController` and `BotThread`) actually correct?**
  _`RobotMascot` has 5 INFERRED edges - model-reasoned connections that need verification._
- **What connects `build.sh script`, `Chat backend for Jarvis — the desktop job-search AI.  Primary:  NVIDIA NIM free`, `Chat router. prefer='nvidia' (free, no Claude tokens) or 'claude'.` to the rest of the system?**
  _336 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `UserSerializer` be split into smaller, more focused modules?**
  _Cohesion score 0.05474315710536183 - nodes in this community are weakly interconnected._
- **Should `index-CDWIGAMO.js` be split into smaller, more focused modules?**
  _Cohesion score 0.024089635854341738 - nodes in this community are weakly interconnected._