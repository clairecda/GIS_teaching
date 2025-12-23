# Week 7 · Bridge to Python

You've spent six weeks mastering spatial analysis in QGIS—filtering data, creating hotspots, running network analysis. Now you'll learn how to automate these workflows with Python, making your analyses repeatable, shareable, and scalable. This week introduces Python for GIS using your first notebook—you can run it in the browser with Google Colab (no installation required) or set up a local environment if you prefer.

## What you'll learn

By the end of this week, you'll be able to:

1. Run Python notebooks using Google Colab (browser-based) or Jupyter (local).
2. Import and inspect spatial data using GeoPandas.
3. Understand reproducibility principles: folder structures, relative paths, and documentation practices.
4. Map QGIS workflows to Python equivalents, recognizing when to use GUI tools versus scripts.

## Before you start

- [ ] Have a **Google account** (for Colab) OR **5 GB free disk space** (for local Anaconda)
- [ ] Review the lecture: [Week 7 · Reproducibility & Environments](../lectures/week07-reproducibility.md)

!!! tip "Two ways to run Python notebooks"
    **Google Colab (Recommended):** Run notebooks in your browser—no installation required. Great for getting started quickly.

    **Local (Anaconda):** Install Python on your computer for faster performance and offline access. Better for large datasets or the capstone project.

## This week's activities

### Activity 1: Run your first Python notebook

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

### Activity 2: QGIS to Python workflow mapping

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

### Activity 3: Reproducibility reflection (optional)

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

- Slides: [Week 07 lecture deck](../slides/index.md)
- Lecture notes: [Reproducibility & Environments](../lectures/week07-reproducibility.md)
- Reference: [Understanding CRS](../readings/understanding-crs.md) - Important background for spatial analysis
- 📘 **Optional:** [Python Setup Guide](../onboarding/04-python-setup.md) - For local Anaconda installation

## Reflect

Take 10-15 minutes to answer these questions:

- How do you feel about transitioning from QGIS (point-and-click) to Python (code-based) workflows?
- Which QGIS workflows are you most excited to automate with Python? Which do you think you'll keep doing in QGIS?
- What questions do you still have about Jupyter notebooks, relative paths, or folder structures?
- How confident do you feel about starting Python-based analysis next week (1-10 scale)? What would increase your confidence?

!!! note "First time with Python?"
    Running code for the first time can feel unfamiliar. That's normal! The notebooks guide you step-by-step. Focus on understanding what each cell does rather than memorizing syntax.

## What you'll submit

- [ ] **Screenshot** of the completed "Hello GIS" notebook showing your first map
- [ ] **Brief notes** (5-10 sentences) reflecting on running your first Python notebook

## Coming up next week

Week 8 launches into hands-on Python spatial analysis! You'll use GeoPandas for vector workflows—loading shapefiles, filtering data, performing spatial joins, and calculating densities.

**To prepare:**

1. Make sure you can run the Week 7 notebook successfully
2. Review the QGIS-to-Python comparison table from Activity 2

Come to Week 8 ready to code!
