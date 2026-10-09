# Smoke test

!!! danger "Delete before public launch"
    This page exists only to verify the toolchain: math, diagrams, admonitions,
    and search. It is not linked from the navigation.

## Inline math

Euler's identity: \( e^{i\pi} + 1 = 0 \), and the Gaussian integral
\( \int_{-\infty}^{\infty} e^{-x^2}\,\mathrm{d}x = \sqrt{\pi} \).

## Display math (bracket syntax)

\[
\cos x = \sum_{k=0}^{\infty} \frac{(-1)^k}{(2k)!} x^{2k}
\]

## Display math (dollar syntax)

$$
\frac{\partial \mathcal{L}}{\partial \theta}
= \sum_{i=1}^{N} \frac{\partial \mathcal{L}_i}{\partial \theta}
$$

## Mermaid diagram

```mermaid
graph LR
  A[Markdown] --> B[Zensical]
  B --> C[Static HTML]
  C --> D[Plesk]
```

## Admonition

!!! success "Admonitions work"
    If this renders as a styled call-out box, admonitions are configured correctly.

## Search check

Zebra xylophone quokka — unique words to look for in the search box. The search
should also find the heading "Search check".
