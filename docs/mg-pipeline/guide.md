# MG Pipeline

This is **Step 2**: installing and running the pipeline driver. It assumes you
got an environment in [Step 1 — HEP Software Environment](../hep-software-environment/guide.md),
though mg-pipeline also runs standalone if MadGraph, MadSpin, Pythia and Rivet
are already on your system.

!!! info "Source"
    Pulled from [mg-pipeline](https://github.com/iakovts/mg-pipeline) at commit `{{ mg_pipeline_sha }}` ({{ mg_pipeline_date }}). Edit the source repo, not this page.

--8<-- "mg-pipeline/docs/index.md"

<!-- Include the '## Prerequisites' heading alone, then the note, then the body,
     so the note sits directly under the heading. If prerequisites.md gains lines
     before the heading, adjust these line numbers. -->
--8<-- "mg-pipeline/docs/prerequisites.md:1:1"

!!! tip "Already installed the tools? Skip the prerequisites"
    If you got MadGraph, MadSpin, Pythia and Rivet through one of the environment
    methods in [Step 1](../hep-software-environment/guide.md), the prerequisites
    are already satisfied — **skip ahead to Usage**. Your layout will look
    **similar but not exactly** like the example below: the tool directories
    carry version numbers (e.g. `MG5_aMC_v3_5_13`) and mg-pipeline auto-detects
    them at runtime, so you don't have to match the tree precisely.

--8<-- "mg-pipeline/docs/prerequisites.md:2"

--8<-- "mg-pipeline/docs/usage.md"

--8<-- "mg-pipeline/docs/disclaimer.md"
