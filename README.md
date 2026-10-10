# mcgen-pipeline-docs

The lab's documentation site: tool instructions and the docs for
the HEP Software Environment and mg-pipeline tooling. Built with
[Zensical](https://zensical.org/); the output is a plain static `site/` folder —
interim hosting is GitHub Pages, the final home is the university's Plesk space.

## What happens here (content model)

Documentation is **owned by the thing it describes**:

- Each tool repo is **one big `README.md`** (short intro → table of contents →
  the full guide):
  [mg-pipeline](https://github.com/iakovts/mg-pipeline),
  [hep-pipeline-env](https://github.com/iakovts/hep-pipeline-env).
  That README is the single source of truth — GitHub shows it, and this site
  includes it. No copies, no generator, no hooks: **drift is impossible**.
- **This repo** is the site: theme, landing page, site-authored tool
  instructions (`docs/guides/`), and thin **wrapper pages**
  (`docs/hep-software-environment/`, `docs/mg-pipeline/`) that include the
  READMEs at build time and stamp where they came from.

To fix or extend tool documentation: edit the tool repo's `README.md`, re-run
the sync below, rebuild. Never edit a wrapper page's body.

### What `scripts/sync_sources.py` does

1. Looks for the two tool repos as **siblings** of this repo
   (`../mg-pipeline-main` or `../mg-pipeline`; `../hep-pipeline-env-main` or
   `../hep-pipeline-env`).
2. Copies each repo's `README.md` into `sources/<repo>/README.md` — `sources/`
   is gitignored: it is a build input, regenerated every time.
3. Records each repo's commit SHA and date in `sources/provenance.json`.

The site then includes README **sections** with `pymdownx.snippets`
(`--8<-- "<repo>/README.md:section"`). The sections are bracketed by invisible
HTML-comment markers (`<!-- --8<-- [start:x] -->`) in each README — that's how
the site can insert its own intro/notes between sections. Nothing under
`sources/` is served raw; only the pages that include it.

### What "provenance" means

Provenance = *where content came from, and which version it is*. The pulled
pages are copies of another repo's files, so every published page must say which
exact commit it reflects — otherwise the site can silently show yesterday's
truth. `sources/provenance.json` carries `git rev-parse --short HEAD` and the
last-commit date per repo; `scripts/provenance.py` (a small Zensical `macros`
module) exposes them as template variables (`{{ mg_pipeline_sha }}`,
`{{ hep_pipeline_env_sha }}`, …) that the wrapper pages render as a banner:
"Pulled from mg-pipeline at commit `e0ea57a` (2026-10-09)". If anyone says the
site disagrees with GitHub, that SHA tells you exactly which version it was
built from.

## Quickstart

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

python scripts/sync_sources.py      # pull tool docs/ into sources/ (run this
                                    # first, and again after editing a tool repo)
.venv/bin/zensical serve            # dev server with hot reload -> localhost:8000
.venv/bin/zensical build --strict   # static build -> ./site/
python3 -m http.server -d site      # optional preview of the built site
```

If a build ever produces stale output (pre-1.0 quirk), run a clean build:

```bash
.venv/bin/zensical build --clean --strict
```

## Layout

| Path | What |
|---|---|Site content: landing body, `guides/` (site-authored), wrapper pages in `hep-software-environment/` + `mg-pipeline/` |
| `scripts/sync_sources.py` | Stages tool-repo `docs/` into `sources/`; writes provenance |
| `scripts/provenance.py` | `macros` module: provenance JSON → template variables |
| `sources/` | Generated build input (gitignored) |
| `overrides/homepage.html` | Landing-page template (hero + quickstart text block) |
| `docs/stylesheets/extra.css` | Site CSS tweaks |
| `docs/javascripts/mathjax.js` | MathJax config (math is `\( \)` inline / `\[ \]` or `$$` display) |
| `.github/workflows/docs.yml` | Clones the tool repos, syncs, builds, deploys to Pages
| `docs/stylesheets/extra.css` | Site CSS tweaks |
| `docs/javascripts/mathjax.js` | MathJax config (math is `\( \)` inline / `\[ \]` or `$$` display) |
| `dev_notes/` | Internal plan + notes (not published) |

## Notes

- **Everything is built in**: search (Disco), Mermaid diagrams (native runtime —
  just use ` ```mermaid ` fences), Markdown extensions (bundled `pymdownx.*`).
  No third-party MkDocs/Zensical plugins are used.
- **Math** renders via MathJax. The runtime currently loads from unpkg — this is
  a temporary external reference; self-hosting is planned (see
  `dev_notes/implementation-plan.md`, Phase 4).
- **Language**: English only for now. A language dropdown example is commented in
  `zensical.toml` for the eventual EN/EL split (one build per language).
- `docs/smoke-test.md` is a test page — delete before public launch.

## Docs

See `dev_notes/HANDOFF.md` for context and `dev_notes/implementation-plan.md`
for the phased plan and verification checklists.
