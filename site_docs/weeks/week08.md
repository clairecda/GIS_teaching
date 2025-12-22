# Week 8 · Python Vector Workflows

You've spent weeks mastering QGIS operations—filtering data, joining attributes, calculating densities, styling maps. This week, you'll replicate those same workflows using Python and GeoPandas, unlocking the power of automation and reproducibility. Instead of clicking through menus, you'll write code that documents every step, can be run repeatedly with new data, and can be shared with colleagues who need to reproduce your analysis. If Week 7 was your bridge to Python, this week you'll cross it.

## What you'll learn

By the end of this week, you'll be able to:

1. Load vector datasets into GeoPandas GeoDataFrames and perform attribute cleaning and filtering programmatically.
2. Execute spatial joins to link incidents to neighbourhoods and calculate density metrics (counts per area).
3. Create choropleth visualizations using Matplotlib and export cleaned outputs to GeoPackage for QGIS integration.
4. Document reproducible workflows with explicit data paths and transparent processing steps.

## Before you start

### 1. Get the notebook

📓 **Download the Week 8 notebook:** [week08_vector_workflows.ipynb](../../resources/notebooks/week08_vector_workflows.ipynb)

**Where to save it:** Save to your `intro-gis/notebooks/` folder (the one you created in Week 7)

### 2. Confirm your environment works

- [ ] Activate your conda environment: `conda activate intro-gis`
- [ ] Check packages import: `python -c "import geopandas; print('✅ Ready!')"`
- [ ] If you see errors, review [Week 7 setup](week07.md)

### 3. Download datasets

- [ ] Follow the [Downloading datasets](../onboarding/data-downloads.md) guide for Week 8
- [ ] You need: neighbourhood polygons and incident points
- [ ] Save to `intro-gis/data/processed/week08/`
  - `neighbourhoods.geojson`
  - `incidents.geojson`

### 4. Review the lecture

- [ ] Read: [Week 8 · Vector Automation Concepts](../lectures/week08-vector-theory.md)

!!! tip "First-time Python users"
    If the notebook environment feels unfamiliar, spend 5 minutes exploring: Shift+Enter runs a cell, Tab autocompletes, and `?function_name` shows documentation. You'll get the hang of it quickly.

## This week's activities

### Activity 1: Validate your environment

Before diving into spatial analysis, confirm that all required packages are available and functioning correctly.

**Follow the notebook:**

1. Open `week08_vector_workflows.ipynb` in Jupyter Lab or VS Code
2. Run the first code cell (Section 1: Environment validation)
3. You should see green checkmarks confirming each package imports successfully

**Expected output:**

```
Python 3.11.x
✓ geopandas 0.14.x
✓ pyproj 3.6.x
✓ shapely 2.0.x
✓ matplotlib 3.8.x
✓ contextily 1.5.x
```

**Troubleshooting:**

- If you see `ModuleNotFoundError`, make sure your conda environment is activated: `conda activate intro-gis`
- If package versions differ slightly, that's usually fine—major version mismatches (e.g., GeoPandas 0.12 vs 0.14) may require updating
- Still stuck? Check the [Anaconda Setup Guide](../onboarding/anaconda-setup.md) troubleshooting section

### Activity 2: Load and inspect datasets

You'll load neighbourhood polygons and incident points using `gpd.read_file()`, the GeoPandas equivalent of adding a layer in QGIS.

**Follow the notebook:**

1. Update the file paths in Section 2 if your data is located somewhere other than `data/processed/week08/`
2. Run the cell to load both datasets
3. Examine the output of `neighbourhoods.head()` and `incidents.head()`

**What you're learning:**

- **`gpd.read_file()`** reads any vector format (GeoJSON, Shapefile, GeoPackage)—just like QGIS's Add Vector Layer tool
- **`.head()`** shows the first 5 rows, similar to opening the attribute table in QGIS
- The `geometry` column stores spatial information (polygons for neighbourhoods, points for incidents)

**Comparison to QGIS:**

| **QGIS action** | **Python equivalent** |
|-----------------|----------------------|
| Add Vector Layer | `gpd.read_file(path)` |
| Open Attribute Table | `.head()` or `.info()` |
| View field names | `df.columns` |
| Check CRS | `df.crs` |

!!! note "Common error: FileNotFoundError"
    If you see `FileNotFoundError: Provide neighbourhood polygons at...`, it means the data file doesn't exist at the expected path. Double-check that you've downloaded the Week 8 datasets and placed them in `data/processed/week08/` (or update the path in the notebook to match your file location).

### Activity 3: Clean and enrich attribute data

Before analysis, you'll standardize column names and calculate area in square kilometers—essential for computing densities later.

**Follow the notebook:**

1. Run Section 3: Cleaning & enrichment
2. The code performs three operations:
   - **`.rename(columns=str.lower)`** converts field names to lowercase (standardization)
   - **`.to_crs(3857)`** projects to Web Mercator for accurate area calculation
   - **`.area / 1e6`** converts square meters to square kilometers

**What's happening behind the scenes:**

```python
neighbourhoods_clean = (
    neighbourhoods.rename(columns=str.lower)
    .assign(area_km2=neighbourhoods.geometry.to_crs(3857).area / 1e6)
)
```

This single chain of operations replaces several QGIS steps:
- Opening field calculator
- Creating a new field called `area_km2`
- Using `$area / 1000000` expression

**Why lowercase names?** Consistency prevents errors. `neighbourhood_id` vs `Neighbourhood_ID` vs `NEIGHBOURHOOD_ID` can cause join failures. Standardizing avoids headaches later.

**Check your work:**

- Run `neighbourhoods_clean.columns` to see cleaned field names
- Run `neighbourhoods_clean[['neighbourhood_id', 'area_km2']].head()` to inspect area values
- Do the areas look reasonable? (Urban neighbourhoods typically 1-50 km²)

### Activity 4: Perform a spatial join

This is where GIS magic happens: you'll link each incident point to the neighbourhood polygon it falls within—exactly like QGIS's "Join attributes by location" tool.

**Follow the notebook:**

1. Run Section 4: Spatial join example
2. The code performs several steps:

**Step-by-step breakdown:**

```python
# Join incidents to neighbourhoods (like QGIS "Join by Location")
joined = gpd.sjoin(incidents_clean, neighbourhoods_clean, predicate="within", how="left")

# Count incidents per neighbourhood (like "Statistics by Categories" in QGIS)
incident_counts = joined.groupby("neighbourhood_id").size().rename("incident_count")

# Merge counts back to neighbourhood polygons (like table join in QGIS)
neighbourhoods_summary = neighbourhoods_clean.merge(
    incident_counts, left_on="neighbourhood_id", right_index=True, how="left"
).fillna({"incident_count": 0})

# Calculate rate per km² (like Field Calculator)
neighbourhoods_summary["rate_per_km2"] = (
    neighbourhoods_summary["incident_count"] / neighbourhoods_summary["area_km2"]
)
```

**QGIS workflow comparison:**

| **QGIS tool** | **Python equivalent** |
|---------------|----------------------|
| Join attributes by location | `gpd.sjoin(predicate="within")` |
| Statistics by categories | `.groupby().size()` |
| Join attributes by field | `.merge()` |
| Field Calculator | Direct column assignment |

**Understanding spatial predicates:**

- `predicate="within"` means "point is inside polygon"
- Other options: `"intersects"`, `"contains"`, `"touches"` (choose based on your spatial relationship)

**Inspect the results:**

- Run `neighbourhoods_summary.head()` to see the new fields
- Check for neighbourhoods with zero incidents (should be filled with 0, not NaN)
- Look at the `rate_per_km2` values—do hotspots emerge?

!!! warning "Join direction matters"
    The order in `sjoin(incidents, neighbourhoods)` matters: it keeps the incidents' attributes and adds neighbourhood info. Reversing it would keep neighbourhood attributes and add incident info—usually not what you want for point-in-polygon joins.

### Activity 5: Visualize incident density

Now you'll create a choropleth map showing incident density per neighbourhood—the Python equivalent of graduated symbology in QGIS.

**Follow the notebook:**

1. Run Section 5: Visualise results
2. A map appears showing neighbourhoods colored by `rate_per_km2`

**Understanding the visualization code:**

```python
ax = neighbourhoods_summary.plot(
    column="rate_per_km2",        # Field to visualize (like "Value" in QGIS)
    scheme="Quantiles",            # Classification method
    k=5,                           # Number of classes
    cmap="YlOrRd",                 # Color ramp (Yellow-Orange-Red)
    legend=True,                   # Show legend
    figsize=(10, 6),               # Map size
)
ax.set_title("Incident density per neighbourhood")
ax.set_axis_off()
```

**QGIS symbology comparison:**

| **QGIS setting** | **Python parameter** |
|------------------|---------------------|
| Graduated symbology | `scheme="Quantiles"` |
| Value field | `column="rate_per_km2"` |
| Classes | `k=5` |
| Color ramp | `cmap="YlOrRd"` |
| Mode: Quantile | `scheme="Quantiles"` |

**Experiment:**

Try modifying the visualization parameters:

- Change `scheme` to `"EqualInterval"` or `"NaturalBreaks"` (same options as QGIS)
- Try different color ramps: `"Blues"`, `"Reds"`, `"RdYlGn"` (reversed for diverging)
- Change `k=5` to `k=7` for more classes

!!! tip "Choosing color ramps"
    Use sequential palettes (single hue, e.g., YlOrRd) for continuous data like density. Use diverging palettes (two hues, e.g., RdYlGn) for data with a meaningful midpoint (above/below average). Matplotlib supports all ColorBrewer palettes.

### Activity 6: Export processed data

You'll save the cleaned neighbourhood summary layer so you can reopen it in QGIS or use it in future notebooks.

**Follow the notebook:**

1. Run Section 6: Export outputs
2. The code saves your analysis to a GeoPackage file

**What's happening:**

```python
OUTPUT_DIR = Path("..") / "data" / "processed" / "week08"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

out_path = OUTPUT_DIR / "neighbourhoods_summary.gpkg"
neighbourhoods_summary.to_file(out_path, layer="neighbourhoods_summary", driver="GPKG")
```

**Understanding the export:**

- **`Path()`** handles file paths in a cross-platform way (works on Mac, Windows, Linux)
- **`mkdir(parents=True, exist_ok=True)`** creates the output folder if it doesn't exist (avoids errors)
- **`to_file()`** exports to any format: GeoPackage (`.gpkg`), GeoJSON (`.geojson`), Shapefile (`.shp`)
- **`layer="neighbourhoods_summary"`** names the layer inside the GeoPackage (GeoPackages can hold multiple layers)

**Verify the export:**

1. Open QGIS
2. Navigate to `data/processed/week08/neighbourhoods_summary.gpkg`
3. Drag it onto the canvas
4. Open the attribute table—you should see `incident_count`, `area_km2`, and `rate_per_km2` fields
5. Style it using graduated symbology to match your Python visualization

!!! note "Round-trip workflow"
    This is the power of reproducibility: you can process data in Python (fast, documented, repeatable) and refine cartography in QGIS (precise control, layout tools). The best workflows combine both tools' strengths.

### Activity 7: Reflect on the workflow

The notebook includes reflection prompts to help you process what you've learned.

**Follow the notebook:**

1. Run Section 7: Reflection
2. Answer the prompts either in a markdown cell below or in your reflection document

**Reflection questions:**

- **Automation win:** Which step felt faster or more reproducible in Python compared to QGIS? (Likely: cleaning field names, calculating rates, repeating analysis with new data)
- **QGIS alignment:** How will you integrate these Python outputs back into QGIS layouts? (Answer: import the GeoPackage and apply final cartographic styling)
- **Questions:** List any open questions for instructors or topics you want to explore further

**Additional questions for your Week 8 reflection:**

- What was the steepest learning curve—understanding spatial joins, mastering syntax, or interpreting outputs?
- How does seeing the entire workflow in code (load → clean → join → visualize → export) change your understanding of what you were doing in QGIS?
- Where would automation provide the biggest benefit in your own work or research?

## Support materials

- Slides: [Week 08 lecture deck](../../assets/slides/week08.html)
- Lecture notes: [Week 8 · Vector Automation Concepts](../lectures/week08-vector-theory.md)
- GeoPandas documentation: [geopandas.org/en/stable](https://geopandas.org/en/stable/)
- Dataset checklist: [Week 8 items](../reference/data-download-checklist.md)
- Spatial joins guide: [GeoPandas merging data tutorial](https://geopandas.org/en/stable/docs/user_guide/mergingdata.html)

## Reflect

Take 15-20 minutes to answer these questions in your [Week 8 reflection](../reference/reflections.md#week-8--python-vector-workflows):

- What was one thing that felt easier in Python compared to QGIS? What felt harder?
- How does writing code change the way you think about spatial analysis workflows?
- Did you encounter any error messages? How did you troubleshoot them?
- Where would automation be most valuable in projects you've worked on (or can imagine working on)?
- How confident do you feel adapting this notebook for a different dataset (different cities, different incident types)?

!!! tip "Troubleshooting mindset"
    Python errors can feel intimidating at first, but they're actually helpful—they tell you exactly what went wrong and which line caused the issue. Start reading error messages from the bottom up: the last line usually describes the problem, and the lines above show where it occurred.

## What you'll submit

- [ ] Completed Jupyter notebook: `week08_vector_workflows.ipynb` with all cells run and outputs visible
- [ ] Exported GeoPackage: `data/processed/week08/neighbourhoods_summary.gpkg`
- [ ] Screenshot or exported PNG of your choropleth map (from the notebook)
- [ ] Your Week 8 reflection entry

## Coming up next week

Week 9 shifts focus from vector to raster: you'll work with elevation data, satellite imagery, and other continuous surfaces. You'll learn Python tools for raster analysis (Rasterio), terrain modeling (slope, aspect, hillshade), and zonal statistics. The same reproducibility principles apply, but the data structure changes from discrete features to continuous grids. Make sure your environment is still working smoothly—Week 9 builds directly on this week's foundation.
