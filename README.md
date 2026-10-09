# mcgen-auth-docs

Lab documentation site (study guides, tool instructions, hep-pipeline and
mg-pipeline docs), built with [Zensical](https://zensical.org/). The build
output is a plain static `site/` folder — that is the deliverable for the
university's Plesk hosting.

## Quickstart

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

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
|---|---|
| `zensical.toml` | Site configuration (nav, theme, Markdown extensions) |
| `docs/` | All content (Markdown) |
| `overrides/homepage.html` | Landing-page template (topic cards) |
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
