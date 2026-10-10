# MG Pipeline

This is **Step 2**: installing and running the pipeline driver. It assumes you
got an environment in [Step 1 — HEP Software Environment](../hep-software-environment/guide.md),
though mg-pipeline also runs standalone if MadGraph, MadSpin, Pythia and Rivet
are already on your system.

!!! info "Source"
    Pulled from [mg-pipeline](https://github.com/iakovts/mg-pipeline) at commit `{{ mg_pipeline_sha }}` ({{ mg_pipeline_date }}). Edit the source repo, not this page.

--8<-- "mg-pipeline/docs/index.md"

!!! tip "Already installed the tools? Skip the prerequisites"
    If you got MadGraph, MadSpin, Pythia and Rivet through one of the environment
    methods in [Step 1](../hep-software-environment/guide.md), the prerequisites
    below are already satisfied — **skip ahead to Usage**.

--8<-- "mg-pipeline/docs/prerequisites.md"

--8<-- "mg-pipeline/docs/usage.md"

--8<-- "mg-pipeline/docs/disclaimer.md"
