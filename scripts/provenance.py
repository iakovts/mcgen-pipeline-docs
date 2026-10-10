"""Macros module for the Zensical build (loaded via the `macros` plugin).

Exposes the commit SHA and last-commit date of each staged source repo as Jinja
variables, so wrapper pages can stamp provenance:

    {{ mg_pipeline_sha }}   {{ mg_pipeline_date }}
    {{ hep_pipeline_env_sha }}   {{ hep_pipeline_env_date }}

Values come from sources/provenance.json, written by scripts/sync_sources.py.
Zensical's native `macros` plugin calls `define_env(env)` only.
"""

from __future__ import annotations

import json
from pathlib import Path

SITE_ROOT = Path(__file__).resolve().parents[1]
PROVENANCE = SITE_ROOT / "sources" / "provenance.json"

# source-repo name -> Jinja variable prefix
REPOS = {
    "mg-pipeline": "mg_pipeline",
    "hep-pipeline-env": "hep_pipeline_env",
}


def define_env(env) -> None:  # noqa: ANN001 - env type provided by Zensical
    data: dict[str, dict[str, str]] = {}
    if PROVENANCE.exists():
        try:
            data = json.loads(PROVENANCE.read_text())
        except json.JSONDecodeError:
            data = {}

    for repo, prefix in REPOS.items():
        info = data.get(repo, {})
        env.variables[f"{prefix}_sha"] = info.get("sha", "unknown")
        env.variables[f"{prefix}_date"] = info.get("date", "unknown")
