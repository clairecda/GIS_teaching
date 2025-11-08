# Setting Up Your Python Environment with Anaconda

This guide will walk you through installing Anaconda and setting up the Python environment you'll need for Weeks 8-10 of this course. By the end, you'll have all the spatial analysis libraries (GeoPandas, Rasterio, OSMnx) ready to use in Jupyter notebooks.

**Time required:** 30-45 minutes (including download time)

## What is Anaconda?

Anaconda is a Python distribution that makes it easy to install scientific and data science packages. It includes:

- **Python** (the programming language)
- **Conda** (package manager that handles complex dependencies)
- **Jupyter** (interactive notebook environment)
- **Hundreds of pre-built packages** ready to install

For GIS work, conda is essential because spatial libraries like GeoPandas depend on compiled libraries (GDAL, GEOS, PROJ) that are difficult to install manually.

## Before you start

- [ ] **Check your disk space:** You need at least 5 GB free
- [ ] **Check your internet:** You'll download about 600 MB
- [ ] **Admin access:** You may need administrator privileges on your computer

## Step 1: Download Anaconda

### Option A: Full Anaconda (Recommended for beginners)

1. Go to [anaconda.com/download](https://www.anaconda.com/download)
2. Download the installer for your operating system:
   - **Windows:** `Anaconda3-...-Windows-x86_64.exe`
   - **Mac:** `Anaconda3-...-MacOSX-x86_64.pkg` (Intel) or `-arm64.pkg` (M1/M2/M3)
   - **Linux:** `Anaconda3-...-Linux-x86_64.sh`
3. Choose the latest version with **Python 3.11** or **Python 3.12**

### Option B: Miniforge (Lighter alternative)

If you have limited disk space or prefer a minimal installation:

1. Go to [github.com/conda-forge/miniforge](https://github.com/conda-forge/miniforge)
2. Download Miniforge3 for your platform
3. This is smaller (~400 MB) and uses conda-forge by default

!!! tip "Which should I choose?"
    - **Full Anaconda:** Includes Anaconda Navigator (graphical interface) and many pre-installed packages. Easier for beginners.
    - **Miniforge:** Command-line only, minimal installation. Better if you're comfortable with terminals and want to save space.

## Step 2: Install Anaconda

### On Windows:

1. **Run the installer** (double-click the `.exe` file)
2. Click **Next** through the welcome screens
3. **Accept the license agreement**
4. **Installation type:** Choose "Just Me" (recommended)
5. **Installation location:** Use the default path or choose a location with enough space
6. **Advanced options:**
   - ✅ **Check** "Add Anaconda to my PATH environment variable" (makes it easier to use)
   - ✅ **Check** "Register Anaconda as my default Python"
7. Click **Install** and wait 10-15 minutes
8. Click **Finish**

!!! warning "PATH option"
    The installer will warn you about adding Anaconda to PATH. For this course, we recommend checking this box despite the warning—it makes Anaconda easier to use from the command line.

### On Mac:

1. **Run the installer** (double-click the `.pkg` file)
2. Click **Continue** through the welcome screens
3. **Accept the license agreement**
4. **Installation type:** "Install for me only" is fine
5. Click **Install** and enter your password when prompted
6. Wait 10-15 minutes for installation to complete
7. Click **Close**

**Verify installation:**
1. Open **Terminal** (Applications → Utilities → Terminal)
2. Type: `conda --version`
3. You should see something like: `conda 23.7.4`

If you see `command not found`, the installation didn't add conda to your PATH. Run this command:
```bash
echo 'export PATH="$HOME/anaconda3/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### On Linux:

1. **Open Terminal**
2. **Navigate to Downloads:**
   ```bash
   cd ~/Downloads
   ```
3. **Run the installer:**
   ```bash
   bash Anaconda3-2024.02-1-Linux-x86_64.sh
   ```
   (Replace with your actual file name)
4. **Press Enter** to read the license
5. **Type `yes`** to accept
6. **Press Enter** to use default installation location (`~/anaconda3`)
7. **Type `yes`** when asked to initialize conda
8. **Close and reopen your terminal**

**Verify installation:**
```bash
conda --version
```

## Step 3: Update Conda (Important!)

Before creating your environment, update conda to the latest version:

**Open Anaconda Prompt (Windows) or Terminal (Mac/Linux) and run:**

```bash
conda update -n base -c conda-forge conda
```

Type `y` when prompted to proceed.

**Why?** Older conda versions may have bugs or missing features. This ensures you have the latest package solver.

## Step 4: Create the GIS Environment

Now you'll create a dedicated environment for this course with all the spatial libraries you need.

### Step 4a: Download the environment file

You need the `environment.yml` file from the course repository.

**Option 1: Download directly from GitHub**

1. Go to the course repository (your instructor will provide the URL)
2. Navigate to `resources/environment/environment.yml`
3. Click **Raw** button
4. Right-click → **Save As...** → Save to your **Downloads** folder

**Option 2: Copy the environment file**

Create a file called `environment.yml` in your Downloads folder and paste this content:

```yaml
name: intro-gis
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - geopandas
  - rasterio
  - rioxarray
  - xarray
  - osmnx
  - networkx
  - rasterstats
  - shapely
  - pyproj
  - fiona
  - matplotlib
  - seaborn
  - contextily
  - folium
  - jupyter
  - jupyterlab
  - notebook
  - ipykernel
  - pandas
  - numpy
  - scipy
  - pip
  - pip:
      - descartes
```

### Step 4b: Create the environment

1. **Open Anaconda Prompt** (Windows) or **Terminal** (Mac/Linux)

2. **Navigate to where you saved `environment.yml`:**
   ```bash
   cd Downloads
   ```

3. **Create the environment:**
   ```bash
   conda env create -f environment.yml
   ```

4. **Wait 10-20 minutes** while conda:
   - Solves dependencies
   - Downloads packages (~500 MB)
   - Installs everything

You'll see lots of output like:
```
Collecting package metadata...
Solving environment...
Downloading and Extracting Packages...
```

!!! tip "This is normal!"
    Don't worry if this step takes a while. Conda is downloading and compiling spatial libraries with complex dependencies. Grab a coffee!

**What if it fails?**

If you see errors like "conflicts" or "incompatible packages":

1. Make sure you updated conda in Step 3
2. Try creating the environment with Miniforge (uses conda-forge by default)
3. Try installing packages one at a time:
   ```bash
   conda create -n intro-gis python=3.11 -y
   conda activate intro-gis
   conda install -c conda-forge geopandas rasterio osmnx jupyter -y
   ```

## Step 5: Activate Your Environment

Every time you want to work on course notebooks, you need to **activate** the environment:

```bash
conda activate intro-gis
```

You'll see your prompt change to show `(intro-gis)` at the beginning:
```
(intro-gis) C:\Users\YourName>
```

or

```
(intro-gis) yourname@computer:~$
```

This tells you the environment is active!

**To deactivate later:**
```bash
conda deactivate
```

## Step 6: Verify Your Setup

Let's make sure everything installed correctly.

1. **Make sure your environment is activated:**
   ```bash
   conda activate intro-gis
   ```

2. **Download the verification script** from the course repository:
   - Go to `resources/environment/verify_setup.py`
   - Download it to your **Downloads** folder

   Or create a file called `verify_setup.py` with this content:

   ```python
   #!/usr/bin/env python3
   """Verify that the GIS environment is set up correctly."""

   import sys

   print("🔍 Checking your GIS environment setup...\n")

   # Required packages and their minimum versions
   packages = {
       'geopandas': '0.12.0',
       'shapely': '2.0.0',
       'pyproj': '3.4.0',
       'rasterio': '1.3.0',
       'rioxarray': '0.13.0',
       'osmnx': '1.5.0',
       'contextily': '1.3.0',
   }

   all_good = True

   for package, min_version in packages.items():
       try:
           module = __import__(package)
           version = getattr(module, '__version__', 'unknown')
           print(f"✅ {package:15s} {version}")
       except ImportError:
           print(f"❌ {package:15s} NOT INSTALLED")
           all_good = False

   print()

   if all_good:
       print("🎉 Success! All packages are installed correctly.")
       print("You're ready to start the Python weeks!")
   else:
       print("⚠️  Some packages are missing.")
       print("Try reinstalling the environment:")
       print("  conda env remove -n intro-gis")
       print("  conda env create -f environment.yml")
       sys.exit(1)
   ```

3. **Run the verification script:**
   ```bash
   python verify_setup.py
   ```

4. **You should see:**
   ```
   🔍 Checking your GIS environment setup...

   ✅ geopandas       0.14.1
   ✅ shapely         2.0.2
   ✅ pyproj          3.6.1
   ✅ rasterio        1.3.9
   ✅ rioxarray       0.15.0
   ✅ osmnx           1.8.1
   ✅ contextily      1.5.0

   🎉 Success! All packages are installed correctly.
   You're ready to start the Python weeks!
   ```

If you see this, **you're done!** ✅

## Step 7: Launch Jupyter

Now let's test that Jupyter works:

1. **Make sure your environment is activated:**
   ```bash
   conda activate intro-gis
   ```

2. **Launch Jupyter Lab:**
   ```bash
   jupyter lab
   ```

   Or use classic Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

3. **Your browser should open automatically** showing the Jupyter interface

4. **Create a new notebook:**
   - Click **New** → **Notebook** (or **Python 3** in classic Jupyter)
   - In the first cell, type:
     ```python
     import geopandas as gpd
     print("Hello GIS!")
     ```
   - Press **Shift + Enter** to run the cell
   - You should see: `Hello GIS!`

5. **Close Jupyter:**
   - In your browser: File → Shut Down
   - In terminal: Press `Ctrl+C` twice

## Organizing Your Workspace

Now that your environment is ready, create a folder structure for your course work:

```bash
# Navigate to where you want your course folder
cd ~/Desktop    # or ~/Documents, or wherever you prefer

# Create the folder structure
mkdir -p intro-gis/notebooks
mkdir -p intro-gis/data
mkdir -p intro-gis/exports

# Move into the course folder
cd intro-gis
```

Your folder structure should look like:
```
intro-gis/
├── notebooks/       ← Download Week 8-10 notebooks here
├── data/            ← Download datasets here
└── exports/         ← Your outputs will be saved here
```

## Common Issues and Solutions

### "conda: command not found"

**Problem:** Anaconda wasn't added to your PATH.

**Solution (Windows):**
1. Search for "Anaconda Prompt" in Start menu
2. Use that instead of Command Prompt

**Solution (Mac/Linux):**
```bash
export PATH="$HOME/anaconda3/bin:$PATH"
echo 'export PATH="$HOME/anaconda3/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### "PackagesNotFoundError" or "ResolvePackageNotFound"

**Problem:** Conda can't find packages or has conflicts.

**Solution:**
```bash
# Clear conda cache
conda clean --all

# Update conda
conda update -n base conda

# Try again with conda-forge explicitly
conda create -n intro-gis python=3.11 -c conda-forge -y
conda activate intro-gis
conda install -c conda-forge geopandas rasterio osmnx jupyter -y
```

### "ImportError: DLL load failed" (Windows)

**Problem:** Missing system dependencies for GDAL/GEOS.

**Solution:**
```bash
conda activate intro-gis
conda install -c conda-forge --force-reinstall gdal geos proj
```

### "ModuleNotFoundError: No module named 'geopandas'" in Jupyter

**Problem:** Jupyter is using the wrong Python environment.

**Solution:**
```bash
# Make sure environment is activated
conda activate intro-gis

# Register the environment as a Jupyter kernel
python -m ipykernel install --user --name=intro-gis --display-name="Python (intro-gis)"

# Launch Jupyter
jupyter lab

# In Jupyter, go to Kernel → Change Kernel → Python (intro-gis)
```

### Installation is too slow

**Problem:** Conda is taking forever to solve environment.

**Solution:** Use mamba (faster solver):
```bash
conda install -n base mamba -c conda-forge
mamba env create -f environment.yml
```

### Not enough disk space

**Problem:** Anaconda requires 5+ GB.

**Solution:**
1. Use Miniforge (smaller footprint)
2. Install to external drive
3. Use Google Colab as fallback (see week guides)

## Quick Reference

### Common commands you'll use:

```bash
# Activate environment (do this every time!)
conda activate intro-gis

# Launch Jupyter
jupyter lab

# List your environments
conda env list

# Update all packages
conda update --all

# Deactivate environment
conda deactivate

# Remove environment (if you need to start over)
conda env remove -n intro-gis
```

### Workflow for each Python week:

1. Open Anaconda Prompt (Windows) or Terminal (Mac/Linux)
2. Navigate to your course folder: `cd ~/Desktop/intro-gis`
3. Activate environment: `conda activate intro-gis`
4. Launch Jupyter: `jupyter lab`
5. Work on your notebook
6. Save your work
7. Shut down Jupyter (Ctrl+C in terminal)

## Getting Help

**Environment issues:**
- Check this troubleshooting section first
- Run `conda info` and `conda list` to see your setup
- Try the conda-forge approach above
- Ask your instructor or classmates

**Python/Jupyter issues:**
- Make sure environment is activated (you see `(intro-gis)` in prompt)
- Try restarting Jupyter kernel: Kernel → Restart
- Check Week 7 guide for more help

**Still stuck?**
- Post your error message (include full output)
- Share what you've tried
- Mention your operating system

---

**Next steps:**
- ✅ Environment set up? Great! Move on to Week 7 activities
- ✅ Download Week 8 notebook when you're ready to start Python analysis
- ✅ Download datasets following the week-by-week guides

You're now ready to start coding with Python! 🐍🗺️
