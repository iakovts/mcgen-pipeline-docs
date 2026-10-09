# mcgen-auth-docs — handoff

> Read this first, then `implementation-plan.md` (the working plan/tracklist).

## What this is

A **Zensical** (v0.0.69) static documentation site for the lab: study guides,
tool instructions, and docs for the hep-pipeline and mg-pipeline tools.
Math-heavy (physics). Output = plain static `site/` folder for the university's
Plesk hosting. Currently: scaffold + config + IA stubs only (no real content).

## How to run (plain Python venv — no Docker)

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

.venv/bin/zensical serve            # dev server (hot reload) -> localhost:8000
.venv/bin/zensical build --strict   # static build -> ./site/
python3 -m http.server -d site      # optional preview of the built site
```

If a build ever looks stale (pre-1.0 quirk): `zensical build --clean --strict`.
The **user runs all `zensical` commands**; the agent commits and verifies statically.

## Key facts

- Config lives in `zensical.toml` (native format; `mkdocs.yml` also accepted —
  that's the mechanical fallback to MkDocs Material if Zensical ever blocks).
- **Everything is built-in**: Disco search, native Mermaid runtime
  (`pymdownx.superfences.custom_fences` config only), bundled pymdown-extensions,
  theme navigation features. No third-party plugins, no vendored JS packages.
- Math: `pymdownx.arithmatex` + MathJax. House syntax `\( \)` inline,
  `\[ \]` or `$$` display. The MathJax runtime currently loads from unpkg —
  **temporary**; self-hosting/KaTeX is a planned revisit (plan item 13).
- Landing page: `docs/index.md` uses `template: "homepage.html"` (front matter) →
  `overrides/homepage.html` (MiniJinja, topic-card grid) + `docs/stylesheets/extra.css`.
- Language: English only (`theme.language = "en"`); commented `extra.alternate`
  dropdown example ready for the eventual EN/EL split (one build per language,
  Greek under `/el/`).
- `docs/smoke-test.md` is a test page — **delete before public launch**.

## Working agreements

- Agent commits in small one-line messages; user owns branches/merges/tags.
- User runs the site (`zensical serve`/`build`); agent provides run-checklists
  at phase boundaries (see the Verify items in `implementation-plan.md`).
- Pinned deps only (`zensical==0.0.69`); no packages added casually.

## Read next

1. `implementation-plan.md` — phases, steps, verification checklists, decisions.
2. `../auth-docu-site/dev_notes/ssg-comparison.md` — why Zensical over Docusaurus/MkDocs (context; update in Phase 4).
