// MathJax configuration for pymdownx.arithmatex (generic mode).
// Official Zensical recipe: https://zensical.org/docs/authoring/math/
// House syntax: \( \) inline, \[ \] or $$ display.
// NOTE: the MathJax runtime is loaded from unpkg (temporary — see
// dev_notes/implementation-plan.md, Phase 4 item 13 for the self-hosting revisit).

window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

document$.subscribe(() => {
  MathJax.startup.output.clearCache()
  MathJax.typesetClear()
  MathJax.texReset()
  MathJax.typesetPromise()
})

component$.subscribe(({ ref }) => {
  if (ref.classList.contains("md-annotation"))
    MathJax.typesetPromise([ref])
})
