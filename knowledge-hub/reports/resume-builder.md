# Graph Report - resume-builder  (2026-07-10)

## Corpus Check
- 123 files · ~113,702 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 703 nodes · 1197 edges · 126 communities (111 shown, 15 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 96 edges (avg confidence: 0.6)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c1367b65`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- jquery.min.js
- .trigger
- __init__.py
- .get
- xregexp.js
- jquery.js
- xregexp.min.js
- select2.full.js
- .on
- build_resume_pdf
- find
- RelatedObjectLookups.js
- Animation
- .extend
- .apply
- domManip
- actions.js
- Tags
- Resume Builder
- nodeName
- SingleSelection
- Dropdown
- theme.js
- MaximumSelectionLength
- ResumeConfig
- main
- urlify.js
- CloseOnSelect
- Translation
- build.sh
- 0001_initial.py
- 0002_notificationmodel.py
- asgi.py
- wsgi.py

## God Nodes (most connected - your core abstractions)
1. `Results()` - 18 edges
2. `build_resume_pdf()` - 15 edges
3. `AttachBody()` - 14 edges
4. `UserModel` - 12 edges
5. `ee()` - 12 edges
6. `$e()` - 12 edges
7. `SelectAdapter()` - 12 edges
8. `i()` - 12 edges
9. `re()` - 11 edges
10. `BaseSelection()` - 11 edges

## Surprising Connections (you probably didn't know these)
- `cacheAstral()` --indirect_call--> `l()`  [INFERRED]
  staticfiles/admin/js/vendor/xregexp/xregexp.min.js → staticfiles/admin/js/vendor/select2/select2.full.min.js
- `winnow()` --indirect_call--> `i()`  [INFERRED]
  staticfiles/admin/js/vendor/jquery/jquery.js → staticfiles/admin/js/vendor/select2/select2.full.min.js
- `buildParams()` --indirect_call--> `v()`  [INFERRED]
  staticfiles/admin/js/vendor/jquery/jquery.js → staticfiles/admin/js/vendor/select2/select2.full.min.js
- `XRegExp()` --indirect_call--> `G()`  [INFERRED]
  staticfiles/admin/js/vendor/xregexp/xregexp.min.js → staticfiles/admin/js/vendor/jquery/jquery.min.js
- `Tt()` --indirect_call--> `D()`  [INFERRED]
  staticfiles/admin/js/vendor/jquery/jquery.min.js → staticfiles/admin/js/vendor/select2/select2.full.min.js

## Import Cycles
- 1-file cycle: `resume/views.py -> resume/views.py`

## Communities (126 total, 15 thin omitted)

### Community 0 - "jquery.min.js"
Cohesion: 0.07
Nodes (55): Ae(), B(), Be(), c(), $e(), ee(), F(), fe() (+47 more)

### Community 1 - ".trigger"
Cohesion: 0.06
Nodes (7): AllowClear(), ArrayAdapter(), BaseAdapter(), InitSelection(), InputData(), Search(), SelectAdapter()

### Community 2 - "__init__.py"
Cohesion: 0.11
Nodes (33): Form, Model, api_csrf(), api_login(), api_logout(), api_register(), api_add_notification(), api_delete_notification() (+25 more)

### Community 3 - ".get"
Cohesion: 0.08
Nodes (7): AttachContainer(), HidePlaceholder(), InfiniteScroll(), MultipleSelection(), Placeholder(), Query(), Results()

### Community 4 - "xregexp.js"
Cohesion: 0.07
Nodes (29): _arrayLikeToArray(), augment(), buildAstral(), cacheAstral(), cacheInvertedBmp(), charCode(), clipDuplicates(), copyRegex() (+21 more)

### Community 5 - "jquery.js"
Cohesion: 0.06
Nodes (13): computeStyleTests(), dataAttr(), finalPropName(), getData(), Identity(), leverageNative(), NOTE: This can be skipped if there are no unmatched elements (i.e., `matchedCoun, TODO: Now that all calls to _data and _removeData have been replaced (+5 more)

### Community 6 - "xregexp.min.js"
Cohesion: 0.10
Nodes (14): G(), _arrayLikeToArray(), augment(), cacheAstral(), cacheInvertedBmp(), charCode(), clipDuplicates(), copyRegex() (+6 more)

### Community 7 - "select2.full.js"
Cohesion: 0.09
Nodes (14): callDep(), ContainerCSS(), countResults(), DropdownCSS(), handler(), hasProp(), makeNormalize(), makeRelParts() (+6 more)

### Community 9 - "build_resume_pdf"
Cohesion: 0.28
Nodes (16): build_resume_pdf(), _pic_path(), build_resume_pdf(user) — assembles all sections and writes the PDF to disk. Retu, build_education(), build_experience(), build_header(), build_personal_info(), build_projects() (+8 more)

### Community 10 - "find"
Cohesion: 0.17
Nodes (18): addCombinator(), assert(), compile(), condense(), createPositionalPseudo(), elementMatcher(), find(), markFunction() (+10 more)

### Community 11 - "RelatedObjectLookups.js"
Cohesion: 0.24
Nodes (10): addPopupIndex(), dismissAddRelatedObjectPopup(), dismissChangeRelatedObjectPopup(), dismissDeleteRelatedObjectPopup(), dismissRelatedLookupPopup(), removePopupIndex(), showAdminPopup(), showRelatedObjectLookupPopup() (+2 more)

### Community 12 - "Animation"
Cohesion: 0.15
Nodes (14): adoptValue(), ajaxConvert(), ajaxHandleResponses(), Animation(), camelCase(), createFxNow(), createTween(), defaultPrefilter() (+6 more)

### Community 13 - ".extend"
Cohesion: 0.19
Nodes (3): AjaxAdapter(), Defaults(), Options()

### Community 14 - ".apply"
Cohesion: 0.15
Nodes (6): DecoratedClass(), EventRelay(), makeRequire(), MaximumInputLength(), MinimumInputLength(), SelectOnClose()

### Community 16 - "domManip"
Cohesion: 0.20
Nodes (12): buildFragment(), buildParams(), cloneCopyEvent(), disableScript(), DOMEval(), domManip(), getAll(), isArrayLike() (+4 more)

### Community 17 - "actions.js"
Cohesion: 0.38
Nodes (8): checker(), clearAcross(), hide(), reset(), show(), showClear(), showQuestion(), updateCounter()

### Community 19 - "Resume Builder"
Cohesion: 0.29
Nodes (6): API Endpoints, Project Structure, Resume Builder, Running Locally, Tech Stack, What it does

### Community 20 - "nodeName"
Cohesion: 0.29
Nodes (7): boxModelAdjustment(), createButtonPseudo(), createInputPseudo(), curCSS(), getWidthOrHeight(), manipulationTarget(), nodeName()

### Community 24 - "theme.js"
Cohesion: 0.83
Nodes (3): cycleTheme(), initTheme(), setTheme()

## Knowledge Gaps
- **8 isolated node(s):** `build.sh script`, `Migration`, `Migration`, `What it does`, `Tech Stack` (+3 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **15 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `i()` connect `jquery.min.js` to `xregexp.min.js`?**
  _High betweenness centrality (0.043) - this node is a cross-community bridge._
- **Why does `winnow()` connect `jquery.min.js` to `jquery.js`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **Why does `o()` connect `jquery.min.js` to `xregexp.min.js`?**
  _High betweenness centrality (0.036) - this node is a cross-community bridge._
- **Are the 7 inferred relationships involving `ee()` (e.g. with `c()` and `p()`) actually correct?**
  _`ee()` has 7 INFERRED edges - model-reasoned connections that need verification._
- **What connects `ASGI config for ResumeBuilder project.  It exposes the ASGI callable as a module`, `WSGI config for ResumeBuilder project.  It exposes the WSGI callable as a module`, `build.sh script` to the rest of the system?**
  _20 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `jquery.min.js` be split into smaller, more focused modules?**
  _Cohesion score 0.0661189358372457 - nodes in this community are weakly interconnected._
- **Should `.trigger` be split into smaller, more focused modules?**
  _Cohesion score 0.05687645687645688 - nodes in this community are weakly interconnected._