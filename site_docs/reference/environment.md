# Environment Verification & Options

This course provides a managed Python environment so everyone works with the same package versions. Choose the path that fits your hardware and follow the verification steps.

## Option 1 — VS Code Dev Container (recommended)

- Requirements: Docker Desktop (macOS/Windows) or Colima/Podman (Linux) plus VS Code with the **Dev Containers** extension.
- Workflow:
  1. Install Docker Desktop and ensure virtualization is enabled.
  2. Open this repository in VS Code.
  3. When prompted, click **Reopen in Container** or run **Dev Containers: Reopen in Container** from the command palette.
  4. The container builds using `.devcontainer/Dockerfile`, creating the `intro-gis` conda environment automatically.
  5. After the container starts, run the verification script below.
- Tips: Allocate sufficient disk space in Docker preferences (≥ 10 GB). If the build fails, run **Dev Containers: Rebuild without cache**.

## Option 2 — Local conda/mamba environment

- Requirements: Miniforge or Mambaforge (cross-platform).
- Workflow:
  1. Install Miniforge from <https://conda-forge.org/miniforge/>.
  2. In a terminal, run `mamba env create -f resources/environment/environment.yml`.
  3. Activate with `mamba activate intro-gis`.
  4. Launch JupyterLab via `jupyter lab` or `code .` to use VS Code with the environment interpreter.
  5. Run the verification script below.
- Tips: On Windows, run commands in **Anaconda Prompt** or **Windows Terminal** (not PowerShell) to ensure path variables load correctly.

## Option 3 — Google Colab (fallback)

- Use this for short demos or if you cannot install software.
- Upload datasets to Google Drive or host them in a public bucket.
- Add a setup cell in notebooks with `%pip install geopandas rasterio contextily osmnx pysal`.
- Remember to download/export results and sync them back to your local workspace; Colab sessions reset frequently.

## Verify your environment

After activating the environment (container or local), run:

```bash
python resources/environment/verify_setup.py
```

Expected output (versions may vary):

```
Python 3.11.x
✓ geopandas 0.14.x
✓ shapely 2.0.x
✓ pyproj 3.6.x
✓ rasterio 1.3.x
✓ rioxarray 0.15.x
✓ osmnx 1.5.x
✓ pysal 24.x
✓ contextily 1.4.x
Environment looks good.
```

If any library fails to import:

- In the dev container, rebuild (`Dev Containers: Rebuild Container`).
- In conda/mamba, run `mamba install <package>` to install the missing dependency.
- Ensure GDAL or PROJ path variables are set correctly (especially on Windows).

## Quick-start reminders

- To run notebooks in VS Code inside the container, select the `intro-gis` kernel when prompted.
- When using JupyterLab, access it at <http://localhost:8888> after running `jupyter lab`.
- Commit the `resources/environment/environment.yml` file if you add packages, so the team stays in sync.
