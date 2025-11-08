# Environment Strategy

Choose one of the following setups to run the Python portion of the course. The managed dev container is recommended, with conda/mamba as a fallback and Google Colab as a temporary solution.

## 1. VS Code Dev Container (preferred)

- **Why:** Guarantees consistent package versions (GeoPandas, Rasterio, OSMnx, PySAL) and isolates dependencies from your host machine.
- **Requirements:** Docker Desktop (macOS/Windows) or Colima/Podman (Linux), VS Code, **Dev Containers** extension.
- **Workflow:**
  1. Install Docker Desktop and ensure virtualization is enabled.
  2. Clone the repository and open it in VS Code.
  3. Command palette → **Dev Containers: Reopen in Container**.
  4. Wait for the image specified in `.devcontainer/Dockerfile` to build (uses `resources/environment/environment.yml`).
  5. Run `python resources/environment/verify_setup.py` to confirm dependencies.
- **Support tips:** Increase Docker disk space if builds fail; use “Rebuild without cache” for stubborn errors.

## 2. Local conda/mamba environment

- **Why:** Lighter footprint for learners who cannot run Docker; still reproducible with `environment.yml`.
- **Requirements:** Miniforge or Mambaforge.
- **Workflow:**
  1. Install Miniforge from <https://conda-forge.org/miniforge/>.
  2. Run `mamba env create -f resources/environment/environment.yml`.
  3. Activate with `mamba activate intro-gis`.
  4. Launch JupyterLab (`jupyter lab`) or VS Code (`code .`) and select the `intro-gis` interpreter.
  5. Run the verification script to confirm setup.
- **Support tips:** On Windows, use the Miniforge Prompt or Windows Terminal. Resolve SSL issues with `conda config --set ssl_verify true` if needed.

## 3. Google Colab (fallback)

- **Why:** Zero install; useful for quick demos or locked-down environments.
- **Workflow:**
  1. Upload required datasets to Google Drive or host them publicly.
  2. Start a Colab notebook and run a setup cell:
     ```python
     %pip install geopandas rasterio contextily osmnx pysal
     ```
  3. Mount Google Drive if needed and adjust file paths.
  4. Export results (notebooks, CSVs) back to your local workspace when finished.
- **Support tips:** Colab sessions time out; keep copies of outputs. Some compiled libraries may be slow to install each session.

## Verification script

Whichever option you choose, run:

```bash
python resources/environment/verify_setup.py
```

Check that all core libraries import successfully. Troubleshooting guidance is available in [Reference ▸ Environment verification](../reference/environment.md).

## Video walkthroughs & FAQs

- Record short screen captures (2–3 minutes) demonstrating the dev container build and conda setup.
- Maintain a troubleshooting FAQ: Docker disk space, GPU drivers, file permission issues, etc.
- Encourage learners to share environment issues in the designated support channel.
