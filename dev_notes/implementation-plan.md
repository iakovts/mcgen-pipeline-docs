# Implementation Plan — mcgen-auth-docs (Zensical)

> Renamed from `mg-docu-site` (2026-10-09, before first push). Display title: "MC Generation @ AUTH".

> Status: approved 2026-10-09. Companion to `HANDOFF.md`.
> This file is the working plan for building the site. Update it as phases complete.

**TL;DR:** Zensical v0.0.69 static docs site for the lab (study guides + tool instructions + hep-pipeline + mg-pipeline docs). Native `zensical.toml` config, new design theme, plain Python venv toolchain (no Docker). **Built-in features only** — Disco search, native Mermaid runtime, bundled pymdown-extensions, theme navigation features. Math via `pymdownx.arithmatex` + MathJax (unpkg for now — revisit, see Decisions). v1 = scaffold + config + IA stubs + smoke test. **No real content yet** (hep-pipeline/mg-pipeline repos not available; stubs = placeholders + TODO markers). `site/` build output = static deliverable for Plesk.

## Git / working agreements

- **The agent commits** in small one-line messages; the **user owns** branches, merges, tags, rebases and anything destructive.
- **The user runs all `zensical` commands** (`serve`, `build`, …). The agent verifies statically (files, config) and hands over run-checklists at phase boundaries.
- The repo may be relocated by the user (currently nested inside `auth-docu-site/`); all paths in this plan are **repo-relative**.
- Dependency pinning: `zensical==0.0.69` exactly in `requirements.txt`. `pymdown-extensions` arrives pinned as a Zensical dependency — nothing else is added.
- Phased work — stop at phase boundaries for user verification.

## Versions verified (2026-10-09, official sources)

- `zensical` **0.0.69** — latest GitHub release (published 2026-10-08); 0.1.0 + Studio launch announced for 2026-11-05.
- Zensical explicitly depends on **Python Markdown Extensions** ("automatically installed with a supported version") — all `pymdownx.*` config works with zero extra packages.
- **Mermaid is native** to Zensical: the `pymdownx.superfences.custom_fences` config is all that is needed; Zensical auto-initializes the JS runtime (works with instant navigation, follows theme fonts/colors, light+dark).
- Math: official recipes = **MathJax** (config JS + runtime via `extra_javascript`) or **KaTeX** (config JS + runtime "with additional effort, beyond the scope of Zensical").
- Not Zensical-supported (relevant later): `mkdocs-static-i18n` (translations = multi-build instead), `gen-files`.

## Progress log

- **2026-10-09** — Plan created. Phases 0–3 executed in the same session (scaffold, config, landing page, math config, IA stubs, smoke test). Awaiting user run-verification.
- **2026-10-09** — User run-verification passed (math + Mermaid render fine). Rendering checks added to `guides/study-guides/overview.md` and `pipeline/how-it-works.md`. Repo renamed `mg-docu-site` → **`mcgen-auth-docs`** (before first push; display title "MC Generation @ AUTH"). User handles remote/folder rename.

## Steps

### Phase 0 — Plan into the repo
- [x] 0. This plan + `HANDOFF.md` in `dev_notes/`. Commit: "docs: add implementation plan".

### Phase 1 — Repo hygiene & toolchain
- [x] 1. `.gitignore`: `.venv/`, `site/`, `.cache/`. Commit: "chore: add gitignore".
- [x] 2. `requirements.txt`: `zensical==0.0.69`. Commit: "chore: pin zensical dependency".
- [x] 3. `README.md`: quickstart — venv setup, `zensical serve`, `zensical build --strict`, `--clean` note (pre-1.0 stale-cache quirk), optional `python3 -m http.server -d site`, "site/ is the deliverable". Commit: "docs: add README quickstart".
- [x] **Verify (user):** `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`, then `zensical serve` starts on the skeleton.

### Phase 2 — Site config & features
- [x] 4. `zensical.toml`: `[project]` (site_name/site_url placeholder, `docs_dir`, `site_dir`, `use_directory_urls = true`, `nav` = Home | Guides | Pipeline | MG Pipeline), `[project.theme]` (`language = "en"`, `custom_dir = "overrides"`, features: `navigation.tabs`, `navigation.tabs.sticky`, `navigation.sections`, `navigation.indexes`, `navigation.top`, `toc.follow`, `search.suggest`, `search.highlight`; light/dark palette), `[project.extra]` (commented EN/EL `alternate` dropdown example), `[project.markdown_extensions]` (`admonition`, `attr_list`, `tables`, `toc` w/ permalink, `pymdownx.details`, `pymdownx.highlight`, `pymdownx.emoji` (bundled icon sets, to_svg), `pymdownx.superfences` + mermaid custom fence, `pymdownx.arithmatex.generic = true`). Commit: "feat: add zensical site config".
- [x] 5. Landing page: `overrides/homepage.html` (MiniJinja; hero + topic-card grid, selected via `template: "homepage.html"` front matter in `docs/index.md`) + `docs/stylesheets/extra.css` (cards, content width). Commit: "feat: add landing page with topic cards".
- [x] 6. Math: `docs/javascripts/mathjax.js` (official Zensical config: `\( \)`/`\[ \]` delimiters + `document$` re-typeset) wired via `extra_javascript` with the MathJax runtime from unpkg — **temporary external reference, revisit self-hosting/KaTeX** (see Decisions). Mermaid needs **no** assets (native). Commit: "feat: add mathjax math support".
- [x] **Verify (user):** `zensical serve` → landing cards render and link to topics; topic tabs + section indexes work; dark-mode toggle works; smoke-test math (`\( \)`, `\[ \]`) and Mermaid render.

### Phase 3 — IA stubs & smoke test
- [x] 7. `docs/index.md` hub text + `docs/guides/study-guides/overview.md` + `docs/guides/tool-instructions/overview.md`. Commit: "docs: add guides section stubs".
- [x] 8. `docs/pipeline/{overview,getting-started,configuration,how-it-works,running,troubleshooting}.md`. Commit: "docs: add pipeline section stubs".
- [x] 9. `docs/mg-pipeline/{overview,quickstart,card-formats,cli-reference,stage-reference,known-quirks,extending}.md`. Commit: "docs: add mg-pipeline section stubs".
- [x] 10. `docs/smoke-test.md`: `\( \)` inline + `\[ \]` display math, Mermaid flowchart, searchable headings, admonition. **Delete before public launch.** Commit: "test: add smoke test page".
- [ ] **Verify (user):** `zensical build --strict` → zero broken links; `zensical serve` → all stubs render, cards→tabs→sections navigate correctly, **Disco search finds smoke-test headings**; grep confirms no content copied from hep-pipeline/mg-pipeline repos.

### Phase 4 — Stabilization & verdict (FUTURE)
- [ ] 11. Subpath check: serve `site/` under a `/~username/guides/`-style prefix → CSS/assets/search resolve (validates Plesk subpath hosting).
- [ ] 12. After 2026-11-05: bump `zensical==0.1.0`, user re-runs the checklist; record verdict in `dev_notes/zensical-comparison.md`; update `auth-docu-site/dev_notes/ssg-comparison.md`. Commit: "chore: upgrade zensical to 0.1.0" + "docs: record zensical verdict".
- [ ] 13. Math revisit: replace the unpkg MathJax reference with a self-hosted runtime (KaTeX or MathJax) — keep `\( \)`/`\[ \]` syntax so the swap is syntax-compatible. Commit: "feat: self-host math runtime".
- [ ] 14. Real content from hep-pipeline-env / mg-pipeline (their repos arrive later) + deployment runbook (Plesk push of `site/`).

## Verification (user-run, full checklist)

1. `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt` works as README says.
2. `zensical serve` — hot reload works incl. `overrides/` changes.
3. `zensical build --strict` → `site/` with zero broken links; `python3 -m http.server -d site` serves the build.
4. Landing page: card grid renders, each card opens the right topic; topic tabs visible ≥1220px and sane on mobile; section index behavior works.
5. Smoke test: `\( \)` inline + `\[ \]` display math render; Mermaid flowchart renders in light **and** dark mode; dark-mode toggle restyles correctly.
6. Disco search returns hits for smoke-test headings.
7. Lean invariant: `requirements.txt` contains only `zensical`; no third-party plugins in `zensical.toml`.
8. Fresh-clone + fresh-venv README works as written.

## Decisions

- **Built-ins only (user, 2026-10-09): no added packages, no vendored JS.** Mermaid is native to Zensical (auto runtime). Math = `pymdownx.arithmatex` + MathJax per Zensical's official recipe, with the runtime on unpkg **temporarily** — the only external reference in the project; self-hosting or KaTeX is a Phase-4 revisit (user: math "might change later"). All math written as `\( \)` inline / `\[ \]` or `$$` display so any renderer swap is syntax-compatible.
- **Plain Python venv, no Docker** (user). The Docker-only rule applies to npm/Node projects only. `site/` static output is the deliverable; the user runs `zensical` themselves.
- **`zensical.toml` native config** + **new design theme** (the `classic` Material look is a one-line A/B). MkDocs fallback = mechanical `zensical.toml` → `mkdocs.yml` conversion + `mkdocs-material` in the same venv.
- **Search = built-in Disco** (no Pagefind, no custom search UI).
- **EN only for now** (`theme.language = "en"`) with a commented `extra.alternate` dropdown example. Eventual EN+Greek content: one build per language, Greek subtree under `/el/` (recommended), dropdown links the two.
- **No blog**; landing page with topic cards via per-page `template:` front matter + MiniJinja override.
- **No third-party plugins** — keeps the tree Zensical-native and the MkDocs fallback mechanical.
- Content policy: all prose lives in this site; pipeline repos' READMEs become pointers later. **No code↔doc sync tooling.**

## Supply-chain notes

- `zensical==0.0.69` pinned exactly; `pymdown-extensions` comes pinned via Zensical's own dependencies.
- One external reference (temporary): `https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js` in `extra_javascript`. No other CDN/external origin in the built site. Self-hosting is Phase 4 item 13.
- `zensical build --clean` documented for the pre-1.0 stale-cache quirk (their own docs advise it).

## Relevant files

- `zensical.toml` — single source of truth (nav, theme, extensions).
- `requirements.txt`, `README.md`, `.gitignore`.
- `overrides/homepage.html` — landing-page template (topic cards).
- `docs/index.md` — hub (uses `template: "homepage.html"`).
- `docs/stylesheets/extra.css`, `docs/javascripts/mathjax.js`.
- `docs/guides/`, `docs/pipeline/`, `docs/mg-pipeline/`, `docs/smoke-test.md` — stubs.
- `dev_notes/implementation-plan.md` (this file), `dev_notes/HANDOFF.md`.
