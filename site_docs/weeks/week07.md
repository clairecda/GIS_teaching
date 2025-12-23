# Week 7 · Bridge to Python

You've spent six weeks mastering spatial analysis in QGIS—filtering data, creating hotspots, running network analysis. Now you'll learn how to automate these workflows with Python, making your analyses repeatable, shareable, and scalable. This week introduces Python for GIS using your first notebook—you can run it in the browser with Google Colab (no installation required) or set up a local environment if you prefer.

## What you'll learn

By the end of this week, you'll be able to:

1. Install Anaconda and set up a Python environment configured for spatial analysis.
2. Run verification scripts to confirm your environment includes essential packages (GeoPandas, Rasterio, OSMnx).
3. Launch Jupyter notebooks and run basic Python code for GIS.
4. Understand reproducibility principles: folder structures, relative paths, and documentation practices.
5. Map QGIS workflows to Python equivalents, recognizing when to use GUI tools versus scripts.

## Before you start

- [ ] Have a **Google account** (for Colab) OR **5 GB free disk space** (for local Anaconda)
- [ ] Review the lecture: [Week 7 · Reproducibility & Environments](../lectures/week07-reproducibility.md)

!!! tip "Two ways to run Python notebooks"
    **Google Colab (Recommended):** Run notebooks in your browser—no installation required. Great for getting started quickly.

    **Local (Anaconda):** Install Python on your computer for faster performance and offline access. Better for large datasets or the capstone project.

## This week's activities

### Activity 1: Set up your workspace folder

First, create an organized folder structure for your Python work.

**Steps:**

1. **Choose a location** for your course folder (e.g., `Desktop` or `Documents`)
2. **Create the folder structure:**

**On Mac/Linux (Terminal):**
```bash
cd ~/Desktop
mkdir -p intro-gis/notebooks
mkdir -p intro-gis/data
mkdir -p intro-gis/exports
cd intro-gis
```

**On Windows (Command Prompt):**
```cmd
cd %USERPROFILE%\Desktop
mkdir intro-gis\notebooks
mkdir intro-gis\data
mkdir intro-gis\exports
cd intro-gis
```

Your folder structure should look like:
```
intro-gis/
├── notebooks/       ← You'll download Week 8-10 notebooks here
├── data/            ← Downloaded datasets go here
└── exports/         ← Your outputs will be saved here
```

**Why this structure?**
- **Organized:** Everything related to Python work is in one place
- **Portable:** Relative paths work the same way on any computer
- **Professional:** Follows data science project conventions

### Activity 2: Install Anaconda and set up your environment

Now you'll install Anaconda and create a Python environment with all the spatial libraries you need.

**Follow the comprehensive guide:**

📘 **[Python Setup Guide](../onboarding/04-python-setup.md)** ← Click here for detailed instructions

The guide covers:
- Downloading and installing Anaconda (30-45 minutes)
- Creating the `intro-gis` environment with all required packages
- Verifying your installation works
- Launching Jupyter notebooks
- Troubleshooting common issues

!!! tip "Don't skip the setup guide!"
    The Python setup guide has step-by-step instructions for Windows, Mac, and Linux. Follow it carefully and you'll avoid most setup problems.

**Quick summary of what you'll do:**

1. Download Anaconda from [anaconda.com/download](https://www.anaconda.com/download)
2. Install it (10-15 minutes)
3. Create the environment: `conda env create -f environment.yml`
4. Activate the environment: `conda activate intro-gis`
5. Run verification script to confirm everything works

The [Python Setup Guide](../onboarding/04-python-setup.md) includes a verification script to confirm everything is working.

**You should see output like:**
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

If you see this, **you're ready to go!** ✅

If you see any errors, refer to the troubleshooting section in the [Python Setup Guide](../onboarding/04-python-setup.md).

### Activity 3: Run your first Python notebook

Now let's run the Week 7 starter notebook to verify everything works.

**Get the notebook:**

| Option | Link |
|--------|------|
| **Run in Colab** (Recommended) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/clairecda/GIS_teaching/blob/main/notebooks/week07_hello_gis.ipynb) |
| View on GitHub | [week07_hello_gis.ipynb](https://github.com/clairecda/GIS_teaching/blob/main/notebooks/week07_hello_gis.ipynb) |
| Download | [Right-click → Save As](https://raw.githubusercontent.com/clairecda/GIS_teaching/main/notebooks/week07_hello_gis.ipynb) |

=== "Google Colab"

    1. Click the **Open in Colab** button above
    2. Sign in with your Google account if prompted
    3. Run the first cell to install GIS packages:
       ```python
       !pip install geopandas rasterio rasterstats osmnx contextily folium -q
       ```
    4. Work through the notebook, running each cell with **Shift + Enter**
    5. Save your work: `File → Save a copy in Drive`

=== "Local (Anaconda)"

    1. Download the notebook and save to `intro-gis/notebooks/`
    2. Open Anaconda Prompt (Windows) or Terminal (Mac/Linux)
    3. Activate your environment: `conda activate intro-gis`
    4. Launch Jupyter: `jupyter lab`
    5. Open `week07_hello_gis.ipynb` and work through it
    6. Close when done: `File → Shut Down`

**If you completed the notebook, congratulations!** You're ready for Week 8.

### Activity 4: Understanding relative paths

Understanding relative paths is crucial for making your notebooks portable and reproducible.

**Key concept:** When you save a notebook in `intro-gis/notebooks/` and data in `intro-gis/data/`, you need to tell Python how to navigate from one folder to another.

**Folder structure reminder:**
```
intro-gis/
├── notebooks/          ← Your notebook is HERE
│   └── week08.ipynb
├── data/               ← Data is HERE
│   └── processed/
└── exports/
```

**To go from `notebooks/` to `data/`:**
- Go UP one level (`..`) to reach `intro-gis/`
- Go DOWN into `data/` folder

**In Python:**
```python
from pathlib import Path

# Relative path from notebooks/ to data/
data_path = Path("../data/processed/")
```

**Why this matters:**
- ✅ Works on any computer (Mac, Windows, Linux)
- ✅ Works when you share your notebook with classmates
- ✅ Works when you move your folder to different locations
- ❌ Absolute paths like `C:\Users\YourName\Desktop\GIS\data\` only work on YOUR computer

**Best practices:**
- Always use `Path()` from the `pathlib` module
- Use relative paths (`../data/`) not absolute paths
- Keep your folder structure organized

!!! tip "Windows path gotchas"
    Windows uses backslashes (`\`) but Python uses forward slashes (`/`). Always use forward slashes or `pathlib.Path()` which handles this automatically.

### Activity 5: QGIS to Python workflow mapping

You'll see how familiar QGIS operations translate to Python code.

**Comparison table:**

| QGIS Operation | QGIS Steps | Python Equivalent |
|----------------|-----------|-------------------|
| Load shapefile | `Layer ▶ Add Vector Layer` | `gpd.read_file("data.shp")` |
| Filter features | `Select by Expression ▶ Export` | `df[df['field'] > value]` |
| Spatial join | `Vector ▶ Data Management ▶ Join` | `gpd.sjoin(left, right, predicate='intersects')` |
| Calculate field | `Field Calculator ▶ Create` | `df['new_col'] = df['old_col'] * 2` |
| Count points in polygon | `Processing ▶ Count Points` | `gpd.sjoin(...).groupby('poly_id').size()` |
| Reproject layer | `Export ▶ Save As ▶ Set CRS` | `df.to_crs(epsg=4326)` |
| Dissolve by field | `Vector ▶ Geoprocessing ▶ Dissolve` | `df.dissolve(by='field')` |
| Create buffer | `Buffer` tool | `df.geometry.buffer(distance)` |

**Exercise:** Open a QGIS project from Week 3 or Week 5. Identify 3 operations you performed manually. For each one, find the Python equivalent in the table above or in the Week 8 notebook.

**Discussion:** When should you use QGIS vs. Python?

- **Use QGIS when:** Exploring unfamiliar data, creating one-off maps, presenting to non-technical audiences, debugging spatial issues visually
- **Use Python when:** Repeating the same workflow on multiple datasets, processing large datasets, automating monthly reports, documenting methods for publication, collaborating with data scientists

!!! note "You don't have to choose"
    Most professionals use both tools. QGIS for exploration and prototyping, Python for production workflows. You can even run Python scripts from inside QGIS using the PyQGIS console.

### Activity 6: Reproducibility reflection (optional)

Think about how you've been organizing your QGIS work over the past six weeks.

**Questions to consider:**

- Do your QGIS project files have descriptive names? (`week06_health_accessibility.qgz` ✓ vs. `project_final_v3_FINAL.qgz` ✗)
- Are your folders organized logically? (`data/processed/week06/` ✓ vs. everything in `Desktop/` ✗)
- Could someone else (or future you) recreate your Week 6 analysis if they needed to?
- What information would they need? (Data sources? Processing steps? Software versions?)

**Why this matters:** Python notebooks force you to document your analysis step-by-step. This is great for reproducibility! But the same principles apply to QGIS work.

**Optional exercise:** Write a brief summary (5-10 sentences) of your Week 6 project:
- What data you used and where you got it
- What tools you ran in QGIS
- What parameters you used
- What your final outputs were

Save this as `intro-gis/week07_notes.txt` for your own reference.

## Support materials

- 📘 **Essential:** [Python Setup Guide](../onboarding/04-python-setup.md) - Detailed installation instructions
- Slides: [Week 07 lecture deck](../slides/index.md)
- Lecture notes: [Reproducibility & Environments](../lectures/week07-reproducibility.md)
- Reference: [Understanding CRS](../readings/understanding-crs.md) - Important background for spatial analysis

## Reflect

Take 10-15 minutes to answer these questions:

- What was the most challenging part of Anaconda installation and environment setup? How did you resolve it?
- How do you feel about transitioning from QGIS (point-and-click) to Python (code-based) workflows?
- Which QGIS workflows are you most excited to automate with Python? Which do you think you'll keep doing in QGIS?
- What questions do you still have about Jupyter notebooks, relative paths, or folder structures?
- How confident do you feel about starting Python-based analysis next week (1-10 scale)? What would increase your confidence?

!!! note "Setup struggles are normal"
    Environment configuration can be frustrating—even experienced developers spend hours troubleshooting dependencies. If you encountered errors, document what you tried and how you solved them. This makes you a better troubleshooter and helps classmates facing similar issues.

## What you'll submit

- [ ] **Screenshot or text file** showing successful verification script output (confirming all packages are installed)
- [ ] **Screenshot of Jupyter Lab** showing the "Hello GIS" test working
- [ ] **Brief notes** (5-10 sentences) reflecting on the setup process and your readiness for Python

## Coming up next week

Week 8 launches into hands-on Python spatial analysis! You'll download the Week 8 notebook and learn to use GeoPandas for vector workflows—loading shapefiles, filtering data, performing spatial joins, and calculating densities.

**To prepare:**
1. Make sure your Anaconda environment is working (verification passed ✅)
2. Download the Week 8 notebook when it's posted
3. Download the Week 8 datasets following the data guide
4. Review the QGIS-to-Python comparison table from Activity 6

Come to Week 8 with questions from your setup experience!
