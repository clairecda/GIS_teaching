# Python Environment Strategy

To keep the transition from QGIS to Python smooth, the course ships with a managed environment that learners can access in three ways. This document outlines the recommended default and fallbacks so instructors can support diverse setups without fragmenting the tooling experience.

## Summary recommendation

1. **Primary:** Pre-configured VS Code Dev Container (Docker) published with the repo. Learners launch it via VS Code + Docker Desktop; everything (conda environment, extensions, data paths) is standardised.
2. **Secondary:** Local `mamba`/`conda` environment created from `resources/environment/environment.yml` for learners who cannot run Docker.
3. **Fallback / quick demo:** Google Colab notebooks for short exercises; use sparingly due to storage/network constraints.

## Option 1 — Dev Container (preferred)

- **Why:** Guarantees consistent package versions (GeoPandas, Rasterio, OSMnx, PySAL), isolates dependencies from host machines, and integrates with VS Code for an editor learners increasingly know.
- **Requirements:** Docker Desktop (macOS/Windows) or Colima/Podman on Linux, VS Code with Dev Containers extension.
- **Instructor work:** Maintain `.devcontainer/devcontainer.json` and Dockerfile; push container image to GitHub Container Registry for faster pulls.
- **Learner workflow:** Clone repo ▶ “Reopen in Container” ▶ start Jupyter server from VS Code or terminal (`jupyter lab`).
- **Support tips:** Provide video walkthrough, list common Docker fixes (e.g., enabling virtualization, increasing disk space).

## Option 2 — Local conda/mamba environment

- **Why:** Lighter footprint for learners without Docker or with limited hardware; still reproducible if they run `mamba env create -f resources/environment/environment.yml`.
- **Requirements:** Miniforge or Mambaforge installer; optional `make` script to automate environment activation.
- **Instructor work:** Keep `resources/environment/environment.yml` aligned with container packages; include post-creation script to verify installs.
- **Learner workflow:** Install Miniforge ▶ `mamba env create -f resources/environment/environment.yml` ▶ `mamba activate intro-gis` ▶ launch `jupyter lab`.
- **Support tips:** Provide OS-specific install screenshots, note how to resolve SSL issues on Windows, and include `resources/environment/verify_setup.py` to validate packages.

## Option 3 — Google Colab (fallback)

- **Why:** Zero-install path for short-form demos, especially when learners are on locked-down machines.
- **Limitations:** Resource caps, slower file I/O for large rasters, limited support for compiled libraries (e.g., `rasterio` wheels). Requires uploading datasets or linking to public Cloud storage.
- **Instructor work:** Provide lightweight starter notebooks with `%pip install` cells and pointers to sample data hosted in cloud buckets.
- **Learner workflow:** Open Colab link ▶ run setup cell ▶ mount Google Drive (if needed) ▶ work within session time limits.
- **Support tips:** Emphasise that Colab is for experimentation, not full projects; advise exporting finished notebooks and syncing back to repo.

## Home setup guidance

For learners who want to replicate the environment outside of the managed options:

1. Install Miniforge.
2. Run `mamba create -n intro-gis python=3.11 geopandas rasterio contextily osmnx pysal jupyterlab`.
3. Validate via `python verify_setup.py` (script to be added).
4. (Optional) Configure VS Code with the Python extension and point to the conda interpreter.

Clearly mark this pathway as “advanced / DIY” so expectations remain aligned.

## Action items

- [ ] Author `.devcontainer/` configuration and Dockerfile.
- [ ] Produce `resources/environment/environment.yml` and automated verification script.
- [ ] Draft Colab-compatible notebook templates with minimal dependency footprint.
- [ ] Record quick-start videos (dev container + local conda) for Week 7.

By agreeing on these tiers early, instructors can keep support focused and learners can choose the option that matches their hardware while still converging on a consistent toolchain.
