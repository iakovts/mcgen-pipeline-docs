# HEP Software Environment

This is **Step 1** of the quickstart: getting a working environment with
MadGraph, MadSpin, Pythia and Rivet. **If you already have one, skip to
[Step 2 — MG Pipeline](../mg-pipeline/guide.md).**

`hep-pipeline-env` gives you two ways to get an environment — pick the one that
matches where you work:

- **[Apptainer (HPC)](#apptainer-hpc)** — HPC clusters without Docker (e.g. AUTh's Aristotle).
- **[Docker](#docker)** — local Linux or WSL.

!!! info "Source"
    Pulled from [hep-pipeline-env](https://github.com/iakovts/hep-pipeline-env) at commit `{{ hep_pipeline_env_sha }}` ({{ hep_pipeline_env_date }}). Edit the source repo, not this page.

--8<-- "hep-pipeline-env/docs/index.md"

--8<-- "hep-pipeline-env/docs/apptainer.md"

--8<-- "hep-pipeline-env/docs/docker.md"

--8<-- "hep-pipeline-env/docs/running-the-pipeline.md"

--8<-- "hep-pipeline-env/docs/troubleshooting.md"
