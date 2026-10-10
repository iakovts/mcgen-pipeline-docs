# mcgen-pipeline-docs — handoff

> Read this first, then `implementation-plan.md` (the working plan/tracklist).

## What this is

A **Zensical** (v0.0.69) static documentation site for the lab: study guides,
tool instructions, and docs for the hep-pipeline and mg-pipeline tools.
Math-heavy (physics). Output = plain static `site/` folder — interim home is
GitHub Pages, final home is the university's Plesk hosting.

Tool docs are **not written here**: they are pulled from the two tool repos (see
"Content pipeline" below). This repo holds the site chrome, study guides, and
thin wrapper pages.

## How to run (plain Python venv — no Docker)

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

python scripts/sync_sources.py             # stage tool-repo docs/ -> sources/ (gitignored)
.venv/bin/zensical serve                   # dev server (hot reload) -> localhost:8000
.venv/bin/zensical build --clean --strict  # static build -> ./site/
python3 -m http.server -d site             # optional preview of the built site
```

The sync step needs the two tool repos checked out as **siblings** of this repo
(`../mg-pipeline-main`, `../hep-pipeline-env-main`; falling back to
`../mg-pipeline`, `../hep-pipeline-env`). Re-run it after editing a tool repo to
pick up the change.

If a build ever looks stale (pre-1.0 quirk): `zensical build --clean --strict`.
The **user runs all `zensical` commands**; the agent commits and verifies statically.

## Content pipeline (how tool docs get here)

Tool prose lives in **its own repo** (single source of truth); this repo only
holds the site chrome, study guides, and thin wrapper pages.

- Each tool repo is **one big `README.md`** (short intro → `## Contents` TOC →
  full guide): [mg-pipeline](https://github.com/iakovts/mg-pipeline),
  [hep-pipeline-env](https://github.com/iakovts/hep-pipeline-env).
  That README is the single source of truth — GitHub shows it; the site
  includes it. No copies, no generator, no hooks: **drift is impossible**.
- `scripts/sync_sources.py` copies each sibling repo's `README.md` into
  `sources/<repo>/README.md` (gitignored) and records the commit SHA/date in
  `sources/provenance.json`.
- Site pages under `docs/hep-software-environment/` and `docs/mg-pipeline/` are **wrapper pages**:
  a short "source" note (stamping `{{ mg_pipeline_sha }}` / `{{ hep_pipeline_env_sha }}`
  via the native `macros` plugin + `scripts/provenance.py`) followed by
  `--8<-- "<repo>/README.md:section"` (native `pymdownx.snippets`; sections are
  bracketed by invisible `<!-- --8<-- [start:x] -->` markers in each README).
- Only the included Markdown is rendered; `sources/` is never served raw.

**Swap point:** this is a **copy** today (the tool repos are local/unpushed, so
edits show up on a re-sync). The intended future change is git submodules under
`sources/`; only `scripts/sync_sources.py` and the CI checkout step change.

**CI** (`.github/workflows/docs.yml`): on push to `main` (or manual dispatch),
checks out this repo, `git clone`s the two tool repos into the sibling paths,
runs the sync, then `zensical build --clean` and deploys to GitHub Pages.

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
  `overrides/homepage.html` (MiniJinja; linear "Start here" path + topic cards)
  + `docs/stylesheets/extra.css`.
- Language: English only (`theme.language = "en"`); commented `extra.alternate`
  dropdown example ready for the eventual EN/EL split (one build per language,
  Greek under `/el/`).
- `docs/smoke-test.md` is a test page — **delete before public launch**.
- Content pipeline extras: `scripts/sync_sources.py`, `scripts/provenance.py`,
  `sources/` (gitignored), and `.github/workflows/docs.yml`.
- `site_url` is set to the GitHub Pages URL
  (`https://iakovts.github.io/mcgen-pipeline-docs/`); switch it to the Plesk
  origin later. `site_url` is required for instant navigation and a custom 404.

## Working agreements

- Agent commits in small one-line messages; user owns branches/merges/tags.
- User runs the site (`zensical serve`/`build`); agent provides run-checklists
  at phase boundaries (see the Verify items in `implementation-plan.md`).
- Pinned deps only (`zensical==0.0.69`); no packages added casually.

## Read next

1. `implementation-plan.md` — phases, steps, verification checklists, decisions.
2. `../auth-docu-site/dev_notes/ssg-comparison.md` — why Zensical over
   Docusaurus/MkDocs (context; update in Phase 4). *That path sits outside this
   workspace and may be absent; the reasoning is summarised in the plan's
   Decisions.*
