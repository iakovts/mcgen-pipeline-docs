#!/usr/bin/env python3
"""Stage source-repo docs into ./sources/ for the Zensical build.

Copies each source repo's docs/ directory into sources/<repo>/docs/ so that
pymdownx.snippets can include it, and records each repo's commit SHA/date in
sources/provenance.json (read by scripts/provenance.py). Run before
`zensical serve` / `build`:

    python scripts/sync_sources.py

Iteration 1: copies from sibling checkouts (../mg-pipeline-main,
../hep-pipeline-env-main), falling back to ../mg-pipeline and
../hep-pipeline-env. The CI workflow clones the repos into those sibling paths.
(This layer is the swap point for git submodules later.)
"""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCES = REPO_ROOT / "sources"
PARENT = REPO_ROOT.parent

# dest name -> candidate sibling checkout dirs
REPOS = {
    "mg-pipeline": ["mg-pipeline-main", "mg-pipeline"],
    "hep-pipeline-env": ["hep-pipeline-env-main", "hep-pipeline-env"],
}


def _git(repo: Path, *args: str) -> str:
    try:
        out = subprocess.run(
            ["git", "-C", str(repo), *args],
            capture_output=True,
            text=True,
            check=True,
        )
        return out.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def main() -> None:
    SOURCES.mkdir(exist_ok=True)
    versions: dict[str, dict[str, str]] = {}
    for dest_name, candidates in REPOS.items():
        repo_dir = next(
            (PARENT / c for c in candidates if (PARENT / c / "docs").is_dir()), None
        )
        if repo_dir is None:
            print(f"!! no source docs found for {dest_name} (looked in: {', '.join(candidates)})")
            continue
        src = repo_dir / "docs"
        dest = SOURCES / dest_name / "docs"
        if dest.exists():
            shutil.rmtree(dest)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(src, dest)
        versions[dest_name] = {
            "sha": _git(repo_dir, "rev-parse", "--short", "HEAD"),
            "date": _git(repo_dir, "log", "-1", "--format=%cs"),
        }
        print(f"synced {src} -> {dest}")
    (SOURCES / "provenance.json").write_text(json.dumps(versions, indent=2) + "\n")
    print("wrote sources/provenance.json")


if __name__ == "__main__":
    main()
