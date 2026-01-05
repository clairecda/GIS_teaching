# Week 8 Facilitator Notes: Vector Workflows in Python

## Session Overview

**Duration:** 2 hours (120 minutes)

**Learning Objectives:**

By the end of this session, students will be able to:

1. Load vector datasets into GeoPandas GeoDataFrames and perform attribute cleaning and filtering programmatically
2. Execute spatial joins to link incidents to neighbourhoods and calculate density metrics (counts per area)
3. Create choropleth visualizations using Matplotlib and export cleaned outputs to GeoPackage for QGIS integration
4. Document reproducible workflows with explicit data paths and transparent processing steps

**Materials Needed:**

- [ ] Projector with **large font size** (minimum 16pt for code, 20pt preferred)
- [ ] Week 8 notebook open and tested in both Colab and Jupyter
- [ ] Sample datasets ready (`neighbourhoods.geojson`, `incidents.geojson`)
- [ ] QGIS open for side-by-side comparisons
- [ ] Backup: screenshots of expected outputs in case of live demo failures
- [ ] Student handout: Common error messages reference sheet
- [ ] Zoom breakout rooms configured (if virtual/hybrid)

**Key Transition:**

This is Week 8—students have completed Week 7's Python introduction and are now applying Python to replicate familiar QGIS workflows. Emphasize that this is about **translation, not replacement**: they're learning to speak GIS in a new language, not abandoning their QGIS skills.

---

## Before Class Checklist

### 1. Technical Setup (30 minutes before class)

- [ ] **Run the notebook from start to finish** in Google Colab
  - Clear all outputs, restart runtime, run all cells
  - Check for dependency issues (GeoPandas version conflicts, etc.)
  - Screenshot the final map for backup

- [ ] **Run the notebook locally** in Jupyter
  - Activate the conda environment: `conda activate intro-gis`
  - Test from the actual repository location
  - Verify file paths work with the `../data/processed/week08/` structure

- [ ] **Verify datasets are accessible**
  - Check that `neighbourhoods.geojson` and `incidents.geojson` are in the repository
  - Test file sizes (should be < 5 MB for smooth loading)
  - Open both files in QGIS to confirm validity and note key fields (neighbourhood_id, geometry types)

- [ ] **Prepare troubleshooting environment**
  - Have a second browser window with GeoPandas documentation open
  - Bookmark Stack Overflow searches for common errors
  - Have a terminal ready to check Python package versions: `conda list | grep geopandas`

### 2. Content Preparation

- [ ] **Review last week's content** (Week 7: Python Foundations)
  - What syntax did students learn? (variables, functions, imports)
  - What confusion points emerged? (indexing? data types?)

- [ ] **Identify the 3 hardest concepts** for this week:
  1. **File paths** (absolute vs. relative, `Path()` usage)
  2. **Spatial join logic** (which dataset goes first? what does `predicate="within"` mean?)
  3. **DataFrame vs. GeoDataFrame** (when does geometry matter?)

- [ ] **Prepare QGIS comparison examples**
  - Open QGIS with the same datasets loaded
  - Screenshare toggle ready to show: QGIS attribute table vs. `.head()`, QGIS Join by Location dialog vs. `sjoin()` code
  - Mark the QGIS toolbar locations you'll reference (Vector > Join by Location, Field Calculator)

### 3. Engagement Strategy

- [ ] **Plan 3 pause points** for questions (after loading data, after spatial join, after visualization)
- [ ] **Prepare 2 "Why Python?" stories**
  - Example: "I once had to update an analysis 10 times as data kept changing. In QGIS, I'd redo 20 clicks each time. In Python, I just re-ran the notebook in 5 seconds."
  - Example: "A colleague needed to replicate my workflow. In QGIS, I'd write a 10-page manual. With Python, I sent her the notebook—it was self-documenting."

- [ ] **Draft 2 live polls/questions** to check understanding:
  - "Raise hand if you've seen a `FileNotFoundError` before in any context"
  - "Type in chat: What's one step you've repeated 5+ times in QGIS that you'd love to automate?"

---

## Session Flow (with Timing)

### 0:00-0:10 | Introduction & Setup (10 min)

**What to do:**

- Start with a **relatable hook**: "Who has ever had to redo the same QGIS analysis because the data updated? [Wait for hands.] That's what we're solving today."
- Show the **big picture workflow diagram** on a slide:
  ```
  QGIS Process (Week 4-6):
  Add Layer > Open Attribute Table > Join by Location > Field Calculator > Symbology

  Python Process (Week 8):
  gpd.read_file() > .head() > sjoin() > column assignment > .plot()
  ```

- **Check environment readiness**:
  - "Everyone, open the Week 8 notebook. If you're using Colab, run the first cell with `!pip install geopandas...` **now**. This takes 30 seconds. While it installs, turn to a neighbor and share one thing you remember from Week 7."
  - Walk around (or monitor chat if virtual) to confirm students have the notebook open

**Live Coding Tips:**

- **Increase font size immediately**: In Jupyter, use `Cmd/Ctrl +` multiple times. In Colab, use View > Zoom In.
- **Narrate what you're doing**: "I'm clicking on the first cell. Now I'm pressing Shift + Enter to run it. See how the number in brackets changed from `[ ]` to `[1]`? That means it ran."

**Common Issues:**

- **Student says: "I don't see the install cell!"**
  - Response: "Are you looking at the correct notebook? It should be titled 'Week 8: Vector Workflows'. The install cell is at the very top, with a code fence starting `!pip install`."

- **Installation hangs in Colab**
  - Response: "If it's been more than 2 minutes, click Runtime > Restart runtime, then try again. Colab sometimes has slow package servers."

---

### 0:10-0:25 | Activity 1: Load and Inspect Data (15 min)

**Learning Goal:** Students understand that `gpd.read_file()` = "Add Vector Layer" in QGIS, and `.head()` = "Open Attribute Table."

**Live Demo Script:**

1. **Import libraries (cell: setup)**
   ```python
   import geopandas as gpd
   import pandas as pd
   import matplotlib.pyplot as plt
   from pathlib import Path
   ```
   - **Narrate**: "These imports are like opening QGIS and loading plugins. `geopandas` is the core library for vector data—it's like the entire Vector menu in QGIS, but in code."

2. **Set the data path (cell: load-header and load-data)**
   - **Stop and explain file paths carefully**:
     - Show the project folder structure on screen:
       ```
       intro-gis/
       ├── notebooks/
       │   └── week08_vector_workflows.ipynb  ← You are here
       ├── data/
       │   └── processed/
       │       └── week08/
       │           ├── neighbourhoods.geojson
       │           └── incidents.geojson
       ```
     - "We're in the `notebooks/` folder. To get to our data, we go **up one level** (that's `..`), then into `data/processed/week08/`. That's what `Path("../data/processed/week08")` does."

   - **Interactive moment**: "If you're using Colab and uploaded files directly, your path should be `Path("/content")` instead. Check the folder icon on the left—do you see your files there?"

3. **Load the data**
   ```python
   neighbourhoods = gpd.read_file(DATA / "neighbourhoods.geojson")
   incidents = gpd.read_file(DATA / "incidents.geojson")
   ```
   - **Narrate**: "This is **exactly** like QGIS's Layer > Add Vector Layer. We're loading two files: polygons (neighbourhoods) and points (incidents)."

4. **Inspect with `.head()`**
   ```python
   neighbourhoods.head()
   ```
   - **Narrate**: "This is like opening the attribute table. We see field names across the top—`neighbourhood_id`, `geometry`—and the first 5 rows."
   - **Point out the geometry column**: "See this `geometry` column? That's where the polygon shapes are stored. It looks like code, but it's actually coordinates."

5. **Check the CRS**
   ```python
   print(neighbourhoods.crs)
   ```
   - **Narrate**: "Just like in QGIS, we need to check the coordinate system. This shows us it's in EPSG:4326 (latitude/longitude)."

**Discussion Prompt:**

"Turn to your neighbor: What's the equivalent QGIS tool for each line of code we just ran?" (Give 1 minute, then ask for volunteers.)

**Answers:**
- `gpd.read_file()` → Layer > Add Vector Layer
- `.head()` → Open Attribute Table
- `.crs` → Right-click layer > Properties > Information > CRS

**Common Issues:**

- **`FileNotFoundError: [Errno 2] No such file or directory: '../data/processed/week08/neighbourhoods.geojson'`**
  - **Diagnosis**: The file doesn't exist at that path.
  - **Fix**: "Let's debug this together. First, check if the file exists. In a new cell, run `!ls ../data/processed/week08/`. Do you see `neighbourhoods.geojson` in the output? If not, the file isn't there—you need to download it or update your path."

- **Student sees: `ModuleNotFoundError: No module named 'geopandas'`**
  - **Diagnosis**: GeoPandas isn't installed.
  - **Fix (Colab)**: "Did you run the `!pip install` cell at the very top? Scroll up and run it, then try again."
  - **Fix (Local)**: "Your conda environment might not be activated. Close Jupyter, open a terminal, run `conda activate intro-gis`, then restart Jupyter from that terminal."

---

### 0:25-0:45 | Activity 2: Clean and Enrich Data (20 min)

**Learning Goal:** Students see that Python can standardize and calculate fields faster than repeated Field Calculator clicks.

**Live Demo Script:**

1. **Standardize column names (cell: clean-data)**
   ```python
   neighbourhoods = neighbourhoods.rename(columns=str.lower)
   incidents = incidents.rename(columns=str.lower)
   ```
   - **Narrate**: "Field names might be messy—`Neighbourhood_ID`, `NEIGHBOURHOOD_ID`, `neighbourhood_id`. Inconsistency causes join failures. This line forces everything to lowercase."
   - **Show before/after**:
     ```python
     # Before
     print(neighbourhoods.columns)
     # Run rename
     # After
     print(neighbourhoods.columns)
     ```

2. **Calculate area in km² (cell: clean-data continued)**
   ```python
   neighbourhoods["area_km2"] = neighbourhoods.to_crs(3857).area / 1e6
   ```
   - **Break this down step-by-step** (write on whiteboard if in-person):
     - `neighbourhoods.to_crs(3857)` → "Reproject to Web Mercator (EPSG:3857). We need a projected CRS for accurate area calculations. Just like QGIS warns you about measuring in a geographic CRS."
     - `.area` → "Calculate area in square meters (Web Mercator's unit)."
     - `/ 1e6` → "Divide by 1,000,000 to convert m² to km². (1 km = 1000 m, so 1 km² = 1,000,000 m²)."
     - `neighbourhoods["area_km2"] = ...` → "Create a new field called `area_km2` and store the result. Like Field Calculator's 'Create new field'."

3. **Inspect the result**
   ```python
   neighbourhoods[["neighbourhood_id", "area_km2"]].head()
   ```
   - **Narrate**: "Let's check our work. Do these areas look reasonable? Urban neighbourhoods are usually 1-50 km². If you see 0.0001 or 10,000,000, something's wrong."
   - **Ask students**: "What would cause weird area values?" (Answer: Wrong CRS, or forgot to convert units.)

**QGIS Comparison (screenshare toggle):**

Switch to QGIS window:
- "To do this in QGIS, I'd open Field Calculator, click 'Create new field', type `$area / 1000000`, and click OK. That's 5 clicks. In Python, it's one line of code—and it's documented in the notebook forever."

**Discussion Prompt:**

"Imagine you have 50 shapefiles of different cities, and you need to calculate area for all of them. In QGIS, you'd repeat those 5 clicks 50 times. In Python, you'd write one loop. Which would you prefer?"

**Common Issues:**

- **Student sees: `KeyError: 'neighbourhood_id'`**
  - **Diagnosis**: The field doesn't exist (maybe it's named differently, or the rename didn't run).
  - **Fix**: "Let's check what fields we actually have. Run `neighbourhoods.columns` and look at the list. Is the field name something different, like `neighb_id` or `NBHD_ID`? If so, update your code to match the actual field name."

- **Area values are tiny (e.g., 0.0001)**
  - **Diagnosis**: Forgot to reproject to a projected CRS before calculating area.
  - **Fix**: "You're calculating area in a geographic CRS (lat/lon degrees). Degrees aren't a real distance unit. Did you run the `.to_crs(3857)` part? That's crucial."

- **`AttributeError: 'GeoDataFrame' object has no attribute 'area'`**
  - **Diagnosis**: Typo (e.g., `neighbourhoods.Area` with capital A).
  - **Fix**: "Python is case-sensitive. It's `.area` (lowercase). Try again."

---

### 0:45-0:55 | Break (10 min)

**Facilitator Actions During Break:**

- Check chat/questions for recurring issues
- Test the spatial join cell on your own machine to ensure it's ready
- Prepare the QGIS "Join Attributes by Location" dialog to screenshare after break

---

### 0:55-1:20 | Activity 3: Spatial Join and Rate Calculation (25 min)

**Learning Goal:** Students understand that spatial joins in Python are conceptually identical to QGIS, but faster and more transparent.

**Live Demo Script:**

1. **Explain the goal (cell: join-header)**
   - **Narrate**: "We want to count how many incidents fall inside each neighbourhood. In QGIS, we'd use Vector > Join Attributes by Location. In Python, it's `gpd.sjoin()`."

2. **Perform the spatial join (cell: spatial-join)**
   ```python
   joined = gpd.sjoin(incidents, neighbourhoods, predicate="within", how="left")
   ```
   - **Break this down**:
     - `incidents` → "The points layer. We're starting with incidents."
     - `neighbourhoods` → "The polygons layer. We're adding neighbourhood info to each incident."
     - `predicate="within"` → "The spatial relationship. 'Within' means 'point is inside polygon'. Other options: `intersects`, `contains`, `touches`."
     - `how="left"` → "Keep all incidents, even if they don't fall in a neighbourhood (e.g., incidents in water or outside boundaries)."

   - **Show the result**:
     ```python
     joined.head()
     ```
     - "See how each incident now has a `neighbourhood_id` field? That's the join. Each point knows which neighbourhood it's in."

3. **QGIS Comparison (screenshare toggle):**
   - Switch to QGIS: Vector > Join Attributes by Location
   - Show the dialog: "Input layer = incidents, Join layer = neighbourhoods, Predicate = contains (QGIS's wording for 'within')."
   - "Same operation, different interface. Python's advantage: you can see exactly what parameters were used. In QGIS, if you forget what you clicked, you have to redo it."

4. **Count incidents per neighbourhood (cell: spatial-join continued)**
   ```python
   counts = joined.groupby("neighbourhood_id").size().rename("incident_count")
   ```
   - **Narrate**: "This is like QGIS's 'Statistics by Categories' plugin. We're grouping incidents by neighbourhood and counting how many in each group."
   - **Show the result**:
     ```python
     print(counts)
     ```
     - "This is a list: `neighbourhood_id` on the left, `incident_count` on the right. Some neighbourhoods have 0 incidents (they won't appear here yet—we'll fix that next)."

5. **Merge counts back to neighbourhoods (cell: spatial-join continued)**
   ```python
   neighbourhoods = neighbourhoods.merge(counts, on="neighbourhood_id", how="left")
   neighbourhoods["incident_count"] = neighbourhoods["incident_count"].fillna(0)
   ```
   - **Narrate**: "Now we're doing a **table join** (not a spatial join). We're matching `neighbourhood_id` in the neighbourhoods layer to `neighbourhood_id` in the counts table. This is like QGIS's 'Join Attributes by Field'."
   - **Explain `.fillna(0)`**: "Some neighbourhoods had zero incidents, so they don't appear in the counts table. The merge creates `NaN` (missing value) for them. We replace `NaN` with `0` to show 'zero incidents', not 'unknown'."

6. **Inspect the result**
   ```python
   neighbourhoods[["neighbourhood_id", "incident_count", "area_km2"]].head()
   ```
   - **Narrate**: "Now every neighbourhood has an `incident_count` field. Let's check—do you see any zeros? If not, it means every neighbourhood had at least one incident (or the `.fillna()` didn't work)."

7. **Calculate rate per km² (cell: calc-rate)**
   ```python
   neighbourhoods["rate_per_km2"] = neighbourhoods["incident_count"] / neighbourhoods["area_km2"]
   ```
   - **Narrate**: "This is density: incidents divided by area. High rates = hotspots. Just like Field Calculator in QGIS."
   - **Show top hotspots**:
     ```python
     neighbourhoods.sort_values("rate_per_km2", ascending=False).head()
     ```
     - "These are the neighbourhoods with the highest incident density. Does this match what you'd expect from the data?"

**Discussion Prompt:**

"What's the advantage of having this entire workflow in code versus clicking through QGIS menus?" (Give 2 minutes for pair discussion.)

**Sample Answers:**
- Reproducibility: Can re-run with new data instantly
- Transparency: Anyone reading the notebook knows exactly what was done
- Documentation: The code IS the method section of your report
- Error checking: If counts look wrong, you can inspect each step

**Common Issues:**

- **`KeyError: 'neighbourhood_id'` during merge**
  - **Diagnosis**: The join field name doesn't match between layers.
  - **Fix**: "Check the field names in both datasets. Run `neighbourhoods.columns` and `counts.index.name`. Do they match exactly? If one is `neighb_id` and the other is `neighbourhood_id`, you need to rename one before merging."

- **All incident counts are 1 (or way too low)**
  - **Diagnosis**: The groupby or join went wrong.
  - **Fix**: "Let's inspect the `joined` dataframe. Run `joined.groupby("neighbourhood_id").size()`. Do the counts look right? If not, check if the spatial join actually worked—run `joined.head()` and confirm each incident has a `neighbourhood_id`."

- **Getting `inf` (infinity) values in `rate_per_km2`**
  - **Diagnosis**: Dividing by zero (area is 0 for some neighbourhoods).
  - **Fix**: "Some neighbourhoods have zero area—probably data errors (e.g., invalid geometries). Filter them out: `neighbourhoods = neighbourhoods[neighbourhoods['area_km2'] > 0]` before calculating rate."

- **Spatial join returns empty dataframe (0 rows)**
  - **Diagnosis**: CRS mismatch between layers.
  - **Fix**: "Check if both layers are in the same CRS. Run `incidents.crs` and `neighbourhoods.crs`. If they're different, reproject one: `incidents = incidents.to_crs(neighbourhoods.crs)` before the spatial join."

---

### 1:20-1:35 | Activity 4: Visualize Results (15 min)

**Learning Goal:** Students create choropleth maps in Python and understand how parameters map to QGIS symbology settings.

**Live Demo Script:**

1. **Create the map (cell: plot-map)**
   ```python
   fig, ax = plt.subplots(figsize=(10, 8))

   neighbourhoods.plot(
       column="rate_per_km2",
       scheme="quantiles",
       k=5,
       cmap="YlOrRd",
       legend=True,
       ax=ax
   )

   ax.set_title("Incident Rate per km²")
   ax.set_axis_off()
   plt.show()
   ```

   - **Narrate each parameter**:
     - `column="rate_per_km2"` → "Which field to visualize. Like the 'Value' dropdown in QGIS Graduated Symbology."
     - `scheme="quantiles"` → "Classification method. Same options as QGIS: quantiles, equal interval, natural breaks (Jenks)."
     - `k=5` → "Number of classes. QGIS calls this 'Classes'."
     - `cmap="YlOrRd"` → "Color ramp. Yellow-Orange-Red. Same as ColorBrewer palettes in QGIS."
     - `legend=True` → "Show the legend. QGIS does this automatically."
     - `ax.set_axis_off()` → "Hide the axis numbers (lat/lon ticks). Makes it look cleaner."

2. **QGIS Comparison (screenshare toggle):**
   - Switch to QGIS: Right-click layer > Properties > Symbology > Graduated
   - Show side-by-side:
     ```
     QGIS Setting         | Python Parameter
     ---------------------|------------------
     Value: rate_per_km2  | column="rate_per_km2"
     Mode: Quantile       | scheme="quantiles"
     Classes: 5           | k=5
     Color ramp: YlOrRd   | cmap="YlOrRd"
     ```
   - "It's a direct translation. Once you know QGIS, you can learn Python syntax quickly."

3. **Experiment with parameters**
   - "Let's try different settings. Change `scheme="quantiles"` to `scheme="equalinterval"`. How does the map change?"
   - Run the cell again.
   - "Now try `cmap="Blues"` instead of `YlOrRd`. What if we do `cmap="RdYlGn_r"` (reversed diverging palette)?"
   - **Interactive moment**: "Everyone, pick a different color ramp from this list [share link to Matplotlib colormaps: https://matplotlib.org/stable/tutorials/colors/colormaps.html] and update your map. Share your favorite in the chat."

4. **Interpreting the map**
   - **Discussion prompt**: "Look at your map. Which neighbourhoods are the darkest red? What does that mean?"
   - Answer: Highest incident density (most incidents per km²).
   - "Is high density always 'bad'? What else could explain it?" (Answer: High population density, more nightlife, tourist areas, better reporting rates, etc.)

**Common Issues:**

- **`ValueError: 'quantiles' is not a valid scheme`**
  - **Diagnosis**: The `mapclassify` package isn't installed (required for classification schemes).
  - **Fix (Colab)**: "Add `mapclassify` to the pip install cell at the top: `!pip install geopandas contextily mapclassify -q`. Then restart the runtime and re-run."
  - **Fix (Local)**: "Run `conda install mapclassify` in your terminal, then restart Jupyter."

- **Map appears but is all one color**
  - **Diagnosis**: All values are the same (or NaN), so there's no variation to classify.
  - **Fix**: "Check your data. Run `neighbourhoods['rate_per_km2'].describe()`. Do you see variation (different min/max values)? If everything is 0 or NaN, the calculation step failed."

- **Legend shows weird numbers (e.g., 1e-05)**
  - **Diagnosis**: Scientific notation for very small numbers (normal behavior).
  - **Explanation**: "This is fine—it just means the values are very small. `1e-05` = 0.00001. If you want to avoid this, multiply your rate by 1000 to show 'incidents per 1000 km²' instead."

---

### 1:35-1:45 | Activity 5: Export and Verify in QGIS (10 min)

**Learning Goal:** Students complete the round-trip workflow: Python analysis → export → QGIS cartography.

**Live Demo Script:**

1. **Export to GeoPackage (cell: export)**
   ```python
   output_path = DATA / "neighbourhoods_summary.gpkg"
   neighbourhoods.to_file(output_path, driver="GPKG")
   print(f"Saved to {output_path}")
   ```
   - **Narrate**: "We're saving the results to a GeoPackage—a modern, efficient format that QGIS loves. The `driver="GPKG"` tells GeoPandas what format to use."
   - **Why GeoPackage?**: "Better than Shapefiles (no 10-character field name limit, no multiple files, can store multiple layers in one file). Same quality as GeoJSON but faster for large datasets."

2. **Verify the export**
   - "Let's make sure it worked. Run this in a new cell:"
     ```python
     !ls -lh ../data/processed/week08/*.gpkg
     ```
   - "You should see the file with a size (e.g., `52K` or `1.2M`). If it's `0K`, the export failed."

3. **Open in QGIS**
   - Switch to QGIS window (screenshare).
   - Layer > Add Vector Layer > navigate to `neighbourhoods_summary.gpkg` > Add.
   - Open attribute table: "See the fields we created? `incident_count`, `area_km2`, `rate_per_km2`. All there."
   - Apply graduated symbology to match the Python map: Right-click > Properties > Symbology > Graduated > Value: `rate_per_km2` > Mode: Quantile (5 classes) > Color ramp: YlOrRd > Apply.
   - "Now we have a polished QGIS map, but the analysis was done in Python. Best of both worlds."

**Discussion Prompt:**

"When would you want to do analysis in Python vs. QGIS?" (Give 1 minute, then share answers.)

**Sample Answers:**
- **Python**: Repeated workflows, large datasets, sharing methods, automation, complex calculations.
- **QGIS**: Final cartography, one-off quick looks, teaching/learning, working with stakeholders who don't code.

**Common Issues:**

- **`FileNotFoundError` when trying to save**
  - **Diagnosis**: Output directory doesn't exist.
  - **Fix**: "Create the directory first. Add this line before the export: `output_path.parent.mkdir(parents=True, exist_ok=True)`."

- **File exports but QGIS says it's corrupted**
  - **Diagnosis**: Invalid geometries in the GeoDataFrame.
  - **Fix**: "Run `neighbourhoods.is_valid.sum()` to count invalid geometries. If you see any, fix them: `neighbourhoods['geometry'] = neighbourhoods.buffer(0)` before exporting."

---

### 1:45-1:55 | Reflection and Q&A (10 min)

**Reflection Prompts:**

Project on screen:

1. **What felt easier in Python compared to QGIS? What felt harder?**
2. **Did you encounter any error messages? How did you troubleshoot them?**
3. **Where would automation be most valuable in projects you've worked on?**

**Facilitator Actions:**

- "Take 3 minutes to jot down answers to these questions. You don't need to share—this is for your own reflection. But if you want to share, we'll discuss in a moment."
- After 3 minutes: "Who wants to share one thing that felt easier in Python?" (Call on 2-3 volunteers.)
- "Who found something harder?" (Call on 2-3 volunteers.)
- Validate all responses: "That's a great observation. The syntax learning curve is real, but it gets easier with repetition."

**Open Q&A:**

- "Any questions about anything we covered today—file paths, spatial joins, visualization, exporting?"
- If no questions: "Let me ask you: What's one thing you'd like to try next week? Maybe calculating distances, or working with raster data?"

---

### 1:55-2:00 | Wrap-up and Preview (5 min)

**Wrap-up:**

- "Today you translated QGIS clicks into Python code. You can now:
  - Load and clean vector data programmatically
  - Perform spatial joins to answer 'which incidents fall in which neighbourhoods?'
  - Calculate density metrics and visualize them as choropleth maps
  - Export results back to QGIS for final polishing"

- "The hardest part is always the first time. Next time you run this notebook, it'll feel 50% easier. The time after that, 80% easier."

**Preview Week 9:**

- "Next week: **Raster Workflows in Python**. You'll work with satellite imagery, calculate NDVI (vegetation index), and perform change detection. Same reproducibility principles, but now with gridded data instead of vectors."
- "Homework: Complete this notebook (all cells should run without errors), export the GeoPackage, and submit your reflection. Due before next class."

**Final Question:**

- "On a scale of 1-5 (type in chat or raise fingers), how confident do you feel running this notebook on a different dataset?" (Gauge class sentiment—if most are 1-2, plan extra review next week.)

---

## Key Concepts to Emphasize

### 1. GeoPandas Fundamentals

**Core Idea:** GeoPandas is "QGIS in Python form." Every QGIS tool has a Python equivalent.

**Key Points:**

- **GeoDataFrame = Layer**: A GeoDataFrame is like a layer in QGIS—it has attributes (columns) and geometry (shapes).
- **Geometry column is special**: The `geometry` column stores spatial information. Without it, it's just a regular DataFrame.
- **CRS matters**: Always check the CRS with `.crs` and reproject with `.to_crs()` when needed (especially before spatial operations or area calculations).
- **File format agnostic**: `gpd.read_file()` reads any format—GeoJSON, Shapefile, GeoPackage, KML, etc. GeoPandas detects the format automatically.

**Teaching Tip:** Use the phrase "GeoPandas is a GeoDataFrame factory" to help students remember that most GeoPandas functions return GeoDataFrames.

### 2. Spatial Joins in Code

**Core Idea:** Spatial joins link features based on their geographic relationship (not a shared ID field).

**Key Points:**

- **Order matters**: `sjoin(incidents, neighbourhoods)` keeps incidents' attributes and adds neighbourhood info. Reversing it gives a different result.
- **Predicates define relationships**:
  - `"within"` → Point is inside polygon (most common for point-in-polygon joins)
  - `"intersects"` → Features touch or overlap (works for any geometry type)
  - `"contains"` → Polygon contains point (opposite direction of "within")
  - `"touches"` → Features share a boundary (for adjacency analysis)
- **`how` parameter controls output**:
  - `how="left"` → Keep all features from the left dataset (like LEFT JOIN in SQL)
  - `how="inner"` → Keep only features that match (default)
  - `how="right"` → Keep all features from the right dataset
- **CRS must match**: If layers are in different CRSs, the join will fail silently (no error, just no matches). Always check CRS before joining.

**Common Misconception:** Students think spatial joins are the same as attribute joins. Clarify: "Attribute joins match on a field (e.g., 'ID = 5'). Spatial joins match on geography (e.g., 'point is inside this polygon')."

### 3. QGIS-to-Python Translation Map

**Core Idea:** Every QGIS click has a Python equivalent. Learning Python is translation, not starting over.

**Master Table (share this as a handout):**

| **QGIS Tool** | **Python Code** | **Notes** |
|---------------|-----------------|-----------|
| Add Vector Layer | `gpd.read_file(path)` | Works with any format |
| Open Attribute Table | `.head()` or `.tail()` | Shows first/last N rows |
| View field names | `.columns` | Returns list of column names |
| Check CRS | `.crs` | Shows coordinate system |
| Reproject layer | `.to_crs(epsg)` | E.g., `.to_crs(3857)` |
| Field Calculator (new field) | `df["new_field"] = expression` | Direct assignment |
| Join Attributes by Location | `gpd.sjoin(df1, df2, predicate="...")` | Spatial join |
| Join Attributes by Field | `.merge(df2, on="field")` | Attribute join |
| Statistics by Categories | `.groupby("field").agg(...)` | Aggregation |
| Graduated Symbology | `.plot(column="field", scheme="quantiles", k=5, cmap="YlOrRd")` | Choropleth map |
| Export layer | `.to_file(path, driver="GPKG")` | Supports any format |

**Teaching Tip:** Keep this table on a slide and refer back to it frequently. Students should internalize these mappings.

### 4. Reproducibility Mindset

**Core Idea:** Code is self-documenting, repeatable, and shareable. QGIS clicks are ephemeral.

**Key Points:**

- **Notebooks are lab journals**: Every step is recorded. You can return 6 months later and know exactly what you did.
- **Automation potential**: Run the same analysis on 100 cities with a single loop. In QGIS, you'd click 100 times.
- **Error transparency**: If something goes wrong, you can inspect intermediate steps. In QGIS, you'd have to redo the entire workflow to debug.
- **Collaboration**: Send a notebook to a colleague, and they can reproduce your results exactly. No ambiguous instructions.

**Story to Share:** "I once analyzed crime data for 50 neighborhoods. The police department updated the data halfway through. In QGIS, I'd have to redo 50 layers manually. In Python, I just re-ran the notebook with the new data file. Took 10 seconds."

---

## Live Demo Best Practices

### Font Size and Visibility

- **Code**: Minimum 16pt, preferably 18-20pt. In Jupyter: `Cmd/Ctrl +` repeatedly until someone at the back confirms visibility.
- **Terminal output**: If showing terminal commands, increase terminal font size too (Preferences > Profiles > Text > Font).
- **Screen layout**: Use **dual screen** or **picture-in-picture** mode for Zoom to show code + your face simultaneously. Eye contact builds trust.

### Pacing and Pausing

- **Rule of thumb**: If you think you're going slow, go 20% slower.
- **Pause after running each cell**: Give 5 seconds for students to see the output before narrating. Silence is OK.
- **Explicit narration**: "I'm clicking on this cell. Now I'm pressing Shift + Enter. See the output? It says 'Loaded 25 neighborhoods'. That's what we expect."
- **Check for understanding every 10 minutes**: "Thumbs up if you got the same output as me. Thumbs sideways if you're confused. Thumbs down if you have an error."

### Handling Errors Gracefully

**When you make a mistake (you will):**

- **Model resilience**: "Oops, I got a `KeyError`. Let me read the error message... Ah, I misspelled the field name. This happens all the time. Let me fix it."
- **Show debugging process**: "First, I'll check what fields I actually have. `neighbourhoods.columns`. OK, so it's `neighbourhood_id`, not `neighb_id`. Let me correct that."
- **Normalize errors**: "Errors are learning opportunities. If you never get errors, you're not trying new things."

**When a student has an error:**

- **Don't take their keyboard**: Ask them to read the error message aloud. Guide them to the solution verbally.
- **Use diagnostic questions**: "What's the last line of the error say? OK, now look a few lines up—which line of code caused it? What do you think might be wrong?"
- **Celebrate fixes**: "Great job! You just debugged your first Python error. That's a real skill."

### Live Coding vs. Running Pre-Written Code

**Recommendation:** Mix both.

- **Cells 1-3**: Type live to model the process. Narrate as you type: "I'm importing geopandas... now I'll give it a nickname, `gpd`, so I don't have to type the full word every time."
- **Cells 4+**: Run pre-written code, but **pause to explain** each line. "This line calculates area. Let me break it down: `.to_crs(3857)` reprojects, `.area` calculates area, `/ 1e6` converts to km²."
- **Advantage of pre-written**: Prevents typos that derail the demo. Students can focus on concepts, not watching you type.

### Backup Plan for Failures

**If live demo breaks:**

- **Have screenshots**: Keep a PDF with screenshots of expected outputs. "My internet died, but here's what you should see when this cell runs."
- **Use a recorded screencast**: Pre-record the demo (10 minutes). If live coding fails, play the video and talk over it.
- **Share the working notebook**: "I'll upload my working notebook to the course site so you can compare outputs."

---

## Discussion Prompts

### 1. Comparing Python Workflow to QGIS Clicks

**Prompt:** "We just completed a full analysis—load, clean, join, calculate, visualize, export—in about 40 lines of code. How would you do this in QGIS? What would the steps be?"

**Facilitator Notes:**

- Give students 2 minutes to list the steps on paper or in a document.
- Call on volunteers to share.
- **Expected answer**:
  1. Add Vector Layer (neighbourhoods and incidents)
  2. Open attribute tables to inspect fields
  3. Rename fields manually (or use Refactor Fields tool)
  4. Reproject layers (Vector > Data Management Tools > Reproject)
  5. Calculate area (Open Field Calculator > create new field > `$area / 1000000`)
  6. Vector > Join Attributes by Location (incidents to neighbourhoods)
  7. Statistics by Categories plugin (or manual groupby in Field Calculator)
  8. Join counts back to neighbourhoods (Layer properties > Joins)
  9. Field Calculator to create `rate_per_km2`
  10. Graduated symbology to visualize
  11. Export layer

- **Follow-up**: "Which approach feels more transparent? Which is faster for a one-time task? Which is faster if you need to repeat this 10 times?"

### 2. When to Use Python vs. QGIS

**Prompt:** "Imagine three scenarios:
1. Your boss asks for a quick map of store locations for a meeting in 1 hour.
2. You need to analyze sales density for 200 store regions every month for a year.
3. You're presenting findings to stakeholders who don't use GIS.

Which tool (QGIS or Python) would you use for each scenario, and why?"

**Facilitator Notes:**

- Split into pairs or breakout rooms (3 minutes).
- Reconvene and share answers.
- **Expected answers**:
  1. **QGIS**: Quick task, one-off, need polished cartography fast.
  2. **Python**: Repeated workflow, automation saves hours, reproducibility critical.
  3. **QGIS** (or Python → QGIS round-trip): Stakeholders need visual clarity, not code. But Python could prepare the data, then polish in QGIS.

- **Key Insight**: "It's not Python OR QGIS—it's Python AND QGIS. Use the right tool for each stage of the workflow."

### 3. Reading Error Messages

**Prompt:** "Python gave you this error:
```
FileNotFoundError: [Errno 2] No such file or directory: '../data/processed/week08/neighbourhoods.geojson'
```
Turn to your neighbor: What does this error mean? How would you fix it?"

**Facilitator Notes:**

- This is a **low-stakes practice** for interpreting errors.
- After 1 minute, ask for answers.
- **Expected answer**: "The file doesn't exist at that path. Fix: Check if the file is downloaded, check if the path is correct, or update the path in the code."
- **Teaching moment**: "Error messages are your friend. They tell you exactly what's wrong. The more you read them, the less scary they become."

### 4. Visualizing Density vs. Count

**Prompt:** "We mapped `rate_per_km2` (density) instead of `incident_count` (raw count). Why does that matter? When would density be misleading?"

**Facilitator Notes:**

- This is a **critical thinking exercise** about normalization.
- Give 2 minutes for pair discussion.
- **Expected answers**:
  - **Why density matters**: Large neighbourhoods can have high raw counts just because they're big. Density normalizes by area.
  - **When density is misleading**: If you care about absolute numbers (e.g., allocating police resources, you might care about total incidents, not density). Also, tiny neighbourhoods can have very high densities from just a few incidents (small-number problem).

- **Follow-up**: "How would you decide whether to map density or count?" (Answer: Depends on the question. "Where is crime most concentrated?" → density. "Where do we need the most officers?" → count.)

---

## Common Student Issues

### 1. File Path Errors

**Symptom:** `FileNotFoundError: [Errno 2] No such file or directory`

**Causes:**

- File doesn't exist at the specified location
- Wrong relative path (e.g., using `../` when the file is in the same directory)
- Using backslashes on Windows (e.g., `data\processed\week08`) instead of forward slashes or `Path()`
- Notebook is running in a different working directory than expected

**Diagnosis Steps:**

1. **Check if file exists**: Run `!ls ../data/processed/week08/` (or `!dir` on Windows) to list files in the target directory.
2. **Check current working directory**: Run `!pwd` (or `!cd` on Windows) to see where the notebook is running.
3. **Inspect the full path**: Run `print((Path("../data/processed/week08") / "neighbourhoods.geojson").resolve())` to see the absolute path Python is looking for.

**Solutions:**

- **Fix the path**: Update the code to match the actual file location.
- **Use absolute paths**: Replace `Path("../data/processed/week08")` with the full path, e.g., `Path("/Users/yourname/Desktop/intro-gis/data/processed/week08")`.
- **Move the file**: Download the file and place it in the expected location.
- **Colab-specific**: If using Colab, change path to `Path("/content")` and upload files manually.

**Prevention:**

- Always run `!ls` or `!dir` to verify file locations before loading.
- Use `Path()` instead of raw strings to handle cross-platform path differences.

---

### 2. CRS Mismatch Issues

**Symptom:** Spatial join returns empty dataframe, or geometries don't align when plotted together.

**Causes:**

- The two layers are in different coordinate reference systems (e.g., one in EPSG:4326, one in EPSG:3857).
- GeoPandas can't automatically reproject during spatial joins (unlike QGIS, which does this behind the scenes).

**Diagnosis Steps:**

1. **Check CRS for both layers**:
   ```python
   print(f"Incidents CRS: {incidents.crs}")
   print(f"Neighbourhoods CRS: {neighbourhoods.crs}")
   ```
2. **Compare**: If they're different (e.g., `EPSG:4326` vs. `EPSG:3857`), that's the problem.

**Solutions:**

- **Reproject one layer to match the other**:
  ```python
  incidents = incidents.to_crs(neighbourhoods.crs)
  ```
- **Best practice**: Reproject the smaller dataset (usually points) to match the larger one (usually polygons) to save computation time.

**Prevention:**

- Always check CRS before spatial operations: "Trust but verify."
- Add a CRS check at the start of your notebook:
  ```python
  assert incidents.crs == neighbourhoods.crs, "CRS mismatch! Reprojecting..."
  incidents = incidents.to_crs(neighbourhoods.crs)
  ```

---

### 3. DataFrame vs. GeoDataFrame Confusion

**Symptom:** Student tries to use `.plot()` on a regular DataFrame and gets an error, or geometry column disappears after a merge.

**Causes:**

- Merged with a regular DataFrame (pandas `.merge()`), which drops the geometry column.
- Used pandas functions instead of GeoPandas functions.
- Selected columns without including `geometry`, converting GeoDataFrame to DataFrame.

**Diagnosis Steps:**

1. **Check the type**:
   ```python
   print(type(neighbourhoods))
   ```
   Should say `<class 'geopandas.geodataframe.GeoDataFrame'>`. If it says `<class 'pandas.core.frame.DataFrame'>`, the geometry was lost.

2. **Check for geometry column**:
   ```python
   print("geometry" in neighbourhoods.columns)
   ```
   Should be `True`.

**Solutions:**

- **Restore geometry**: If you have the original GeoDataFrame, reload it.
- **Explicitly keep geometry**: When selecting columns, include `geometry`:
  ```python
  neighbourhoods[["neighbourhood_id", "area_km2", "geometry"]]
  ```
- **Use GeoPandas merge**: Use `gdf.merge()` instead of `pd.merge()` to preserve geometry.

**Prevention:**

- **Teaching analogy**: "The geometry column is the spatial 'magic' that makes it a GeoDataFrame. If you lose it, you just have a regular table—like QGIS without the map view."

---

### 4. Module Import Errors

**Symptom:** `ModuleNotFoundError: No module named 'geopandas'` (or `contextily`, `mapclassify`, etc.)

**Causes:**

- Package not installed in the active environment.
- Using the wrong Python environment (e.g., base environment instead of `intro-gis`).
- In Colab: Didn't run the `!pip install` cell.

**Diagnosis Steps:**

1. **Check installed packages**:
   - Local: Run `conda list | grep geopandas` in terminal.
   - Colab: Run `!pip show geopandas` in a notebook cell.

2. **Check active environment** (local only):
   ```bash
   conda env list
   ```
   The active environment has an asterisk (*). Should be `intro-gis`, not `base`.

**Solutions:**

- **Colab**: Run the install cell at the top of the notebook:
  ```python
  !pip install geopandas contextily mapclassify -q
  ```
- **Local - wrong environment**: Activate the correct environment:
  ```bash
  conda activate intro-gis
  jupyter lab
  ```
- **Local - package missing**: Install the package:
  ```bash
  conda install geopandas
  ```

**Prevention:**

- Always activate the `intro-gis` environment before opening Jupyter.
- Add a validation cell at the start of the notebook:
  ```python
  import sys
  assert 'geopandas' in sys.modules, "GeoPandas not installed!"
  ```

---

### 5. NaN (Missing Value) Confusion

**Symptom:** Some neighbourhoods show `NaN` in `incident_count` or `rate_per_km2` fields.

**Causes:**

- Neighbourhoods with zero incidents don't appear in the grouped counts, so they get `NaN` after the merge.
- Division by zero (if `area_km2` is zero).

**Diagnosis Steps:**

1. **Check for NaN**:
   ```python
   print(neighbourhoods["incident_count"].isna().sum())
   ```
   If > 0, there are NaN values.

2. **Inspect NaN rows**:
   ```python
   neighbourhoods[neighbourhoods["incident_count"].isna()]
   ```
   Are these neighbourhoods with zero incidents, or is something else wrong?

**Solutions:**

- **Fill NaN with zero**:
  ```python
  neighbourhoods["incident_count"] = neighbourhoods["incident_count"].fillna(0)
  ```
- **Prevent NaN during merge**: Use `how="left"` in the merge to keep all neighbourhoods, then fill NaN.

**Teaching Moment:**

- "NaN means 'missing value'. It's not the same as zero. Zero means 'we counted and found nothing'. NaN means 'we didn't count this row'. In our case, we want zero, so we replace NaN with 0."

---

### 6. Spatial Join Direction Confusion

**Symptom:** Spatial join result has too many rows, or wrong attributes.

**Causes:**

- Student reversed the order: `sjoin(neighbourhoods, incidents)` instead of `sjoin(incidents, neighbourhoods)`.
- Misunderstood what the join returns: it keeps the geometry and attributes of the **first** dataset and adds attributes from the second.

**Diagnosis Steps:**

1. **Check row count**:
   ```python
   print(f"Incidents: {len(incidents)}, Neighbourhoods: {len(neighbourhoods)}, Joined: {len(joined)}")
   ```
   Expected: `len(joined)` should be close to `len(incidents)` (assuming most incidents fall in a neighbourhood).

2. **Inspect joined columns**:
   ```python
   print(joined.columns)
   ```
   Should include incident attributes AND neighbourhood attributes.

**Solutions:**

- **Correct order**: `sjoin(incidents, neighbourhoods)` to keep incidents' geometry and add neighbourhood info.
- **Explanation**: "The first dataset is the 'base'. The second dataset is the 'lookup'. We're asking: 'For each incident (base), which neighbourhood (lookup) does it fall in?'"

**Teaching Analogy:**

- "Think of it like a vlookup in Excel. The left table is your main data, the right table is the reference. Order matters."

---

## Code Troubleshooting Guide

### Quick Reference Table

| **Error Message** | **Likely Cause** | **Fix** |
|-------------------|------------------|---------|
| `FileNotFoundError: No such file or directory` | File doesn't exist at that path | Check file location with `!ls`, update path |
| `ModuleNotFoundError: No module named 'geopandas'` | GeoPandas not installed | Colab: run `!pip install geopandas -q`. Local: `conda install geopandas` |
| `KeyError: 'neighbourhood_id'` | Field name doesn't exist or misspelled | Run `df.columns` to check actual field names |
| `ValueError: Cannot transform naive geometries` | CRS not set | Set CRS: `gdf.set_crs(4326, inplace=True)` |
| `ValueError: 'quantiles' is not a valid scheme` | `mapclassify` package missing | Install: `!pip install mapclassify -q` or `conda install mapclassify` |
| `AttributeError: 'GeoDataFrame' object has no attribute 'area'` | Typo (e.g., `Area` instead of `area`) | Python is case-sensitive; use lowercase `area` |
| Empty result from `sjoin()` | CRS mismatch between layers | Check CRS with `.crs`, reproject with `.to_crs()` |
| `TypeError: cannot convert the series to <class 'float'>` | Trying to divide non-numeric columns | Check data type with `.dtypes`, convert with `.astype(float)` |
| `ZeroDivisionError: division by zero` | Area is zero for some polygons | Filter out zero-area polygons: `gdf = gdf[gdf['area_km2'] > 0]` |
| `inf` (infinity) values in calculated field | Division by zero (area = 0) | Same as above: filter or replace inf with NaN |

---

### Debugging Workflow (Teach This!)

**When students encounter an error, guide them through this process:**

1. **Read the error message (bottom-up)**
   - Last line: What type of error? (`FileNotFoundError`, `KeyError`, etc.)
   - Second-to-last line: What's the specific message?
   - Earlier lines: Which line of code caused it?

2. **Inspect the data**
   - Run `.head()` to see the first few rows.
   - Run `.columns` to see field names.
   - Run `.dtypes` to see data types.
   - Run `.crs` to see coordinate system.

3. **Test in small steps**
   - Break complex lines into smaller pieces.
   - Example: Instead of chaining `.to_crs(3857).area / 1e6`, do:
     ```python
     temp = neighbourhoods.to_crs(3857)  # Step 1
     areas = temp.area  # Step 2
     areas_km2 = areas / 1e6  # Step 3
     ```
   - Which step fails?

4. **Search the error**
   - Copy the error type (e.g., "GeoPandas KeyError neighbourhood_id") into Google or Stack Overflow.
   - Look for solutions from the last 2-3 years (old answers may reference outdated syntax).

5. **Ask for help effectively**
   - Share: (1) What you're trying to do, (2) The code you ran, (3) The full error message.
   - Don't just say "It doesn't work"—be specific.

---

### Common Gotchas (Share These as "Pro Tips")

1. **Python is case-sensitive**
   - `neighbourhood_id` ≠ `Neighbourhood_ID` ≠ `NEIGHBOURHOOD_ID`
   - Always standardize with `.rename(columns=str.lower)` early on.

2. **Indexing starts at 0**
   - First row is index 0, not 1.
   - `.head(5)` shows rows 0-4, not 1-5.

3. **Chaining operations can hide errors**
   - Long chains (`.rename().assign().merge()...`) are elegant but hard to debug.
   - If something fails, break the chain into separate lines.

4. **Geometry column is fragile**
   - Easy to lose (e.g., by selecting columns without including `geometry`).
   - Always check `type(gdf)` after merges or selections.

5. **Spatial operations are slow for large datasets**
   - A spatial join on 1 million points vs. 10,000 polygons can take minutes.
   - Consider spatial indexing (`gdf.sindex`) for large datasets (advanced topic).

6. **File paths on Windows**
   - Windows uses backslashes (`C:\Users\...`), but Python strings treat `\` as an escape character.
   - Solution: Use `Path()`, which handles cross-platform paths automatically.
   - Or use raw strings: `r"C:\Users\..."`

---

## Wrap-up and Preview

### Closing Summary (2 minutes)

**Key Achievements Today:**

- "You just completed a full GIS analysis workflow in Python—something that would have taken 20+ clicks in QGIS. You can now:
  - Load and clean messy vector data
  - Perform spatial joins to link points to polygons
  - Calculate rates and densities
  - Create choropleth maps
  - Export results for further use

- "The hardest part is the syntax learning curve. But the concepts? You already know them from QGIS. This is translation, not reinvention."

**Mindset Shift:**

- "Code might feel slower than clicking at first. That's normal. But once you have a working notebook, you can:
  - Rerun it with new data in seconds
  - Share it with colleagues who can reproduce your exact results
  - Adapt it for new projects (change file paths, tweak parameters)
  - Document your methodology transparently"

- "QGIS is for exploration and cartography. Python is for automation and reproducibility. Together, they're unstoppable."

### Preview Week 9 (2 minutes)

**What's Next:**

- "Next week: **Raster Workflows in Python**. You'll work with satellite imagery instead of vector features."

**Topics:**

- Loading raster data with Rasterio
- Calculating NDVI (Normalized Difference Vegetation Index) to measure greenness
- Performing change detection: comparing two dates to see what's changed
- Visualizing rasters with Matplotlib

**Connection:**

- "Same principles as this week—reproducible workflows, code-based analysis, round-trip with QGIS—but now with continuous data instead of discrete features."

**Preparation:**

- "Download the Week 9 datasets this week (satellite images). They're larger files (10-50 MB), so don't wait until 10 minutes before class."

### Homework Reminder (1 minute)

**Due before next class:**

- [ ] Complete `week08_vector_workflows.ipynb` (all cells should run without errors)
- [ ] Export `neighbourhoods_summary.gpkg` and verify it opens in QGIS
- [ ] Submit a screenshot or PNG of your choropleth map
- [ ] Write your Week 8 reflection (5 questions provided in the student guide)

**Submission Format:**

- Upload to [course platform]: Notebook file (.ipynb), GeoPackage (.gpkg), map image (.png), reflection (PDF or Markdown).

**Support:**

- "If you get stuck, post in the discussion forum. Include your error message and what you've tried. We're here to help."

### Final Encouragement (30 seconds)

- "Remember: Every expert coder was once exactly where you are now. The difference? They kept going. Errors are progress. Confusion is learning. You've got this."

- "See you next week for raster workflows. Enjoy your weekend, and happy coding!"

---

## Additional Facilitator Resources

### Pre-Class Email Template

**Subject:** Week 8 Prep: Python Vector Workflows - Action Items Before Class

Hi everyone,

This week we're diving into Python-based vector analysis—replicating QGIS workflows in code. To make the session smooth, please complete these steps **before class**:

**1. Download datasets**
- Get `neighbourhoods.geojson` and `incidents.geojson` from [link to data repository]
- Save to `intro-gis/data/processed/week08/`

**2. Test your environment**
- **Colab users**: Open the Week 8 notebook in Colab and run the first cell (`!pip install geopandas...`). Takes ~1 minute.
- **Local users**: Activate your conda environment (`conda activate intro-gis`) and run:
  ```bash
  python -c "import geopandas; print('Ready!')"
  ```
  If you see errors, review the [Python Setup Guide](link).

**3. Review Week 7**
- Refresh your memory on Python basics: variables, functions, imports.

**During class**, we'll code together—bring questions! If you get stuck during prep, post in the forum.

See you [day/time]!

[Your Name]

---

### Post-Class Follow-Up Email Template

**Subject:** Week 8 Recording + Resources + Homework Reminder

Hi everyone,

Great work today on Python vector workflows! Here are the resources:

**Recording & Materials:**
- Class recording: [link]
- Completed notebook (with outputs): [link]
- Slides: [link]

**Common Issues We Solved Today:**
1. **File path errors**: Remember to use `Path("../data/processed/week08")` or `Path("/content")` for Colab.
2. **CRS mismatches**: Always check `gdf.crs` before spatial joins.
3. **NaN values**: Fill with `.fillna(0)` for zero incidents.

**Homework (due [date]):**
- [ ] Complete `week08_vector_workflows.ipynb`
- [ ] Export `neighbourhoods_summary.gpkg` and verify in QGIS
- [ ] Screenshot your choropleth map
- [ ] Write your Week 8 reflection

**Next Week:**
Week 9: Raster workflows with satellite imagery. Download the datasets early (they're large files)!

Questions? Post in the forum or come to office hours [time].

Happy coding!

[Your Name]

---

### Office Hours Talking Points

**Common Questions to Prepare For:**

1. **"My notebook ran fine in class, but now it's broken. Why?"**
   - Likely cause: Ran cells out of order. Solution: Kernel > Restart & Run All.

2. **"How do I apply this to my own data?"**
   - Steps: (1) Replace file paths, (2) Check field names and update code, (3) Adjust parameters (e.g., color ramp, classification scheme).

3. **"Can I use this for my final project?"**
   - Yes! Encourage adaptation. Offer to review their modified notebook.

4. **"I want to learn more—what's next?"**
   - Recommend: GeoPandas documentation, Automating GIS Processes course (University of Helsinki, free online), "Python for Data Analysis" by Wes McKinney.

---

### Accessibility Considerations

- **Screen reader users**: Ensure all code cells have descriptive text in adjacent markdown cells.
- **Visual impairments**: Increase font size beyond minimum; use high-contrast color ramps (avoid red-green for colorblindness).
- **Motor impairments**: Offer pre-written code snippets for students who have difficulty typing.
- **Cognitive load**: Chunk the session into 15-minute blocks with clear transitions. Provide written summaries.

---

## Success Metrics (Self-Evaluation)

After class, reflect on:

- [ ] Did 80%+ of students successfully load the datasets?
- [ ] Did students complete the spatial join without major confusion?
- [ ] Did most students produce a choropleth map?
- [ ] Were error messages used as teaching moments (not frustration points)?
- [ ] Did I pause enough for students to process?
- [ ] Did I model debugging effectively when my own code failed?
- [ ] Did students ask questions (sign of engagement, not fear)?

**If fewer than 80% succeeded on any of these**, adjust for next time:
- More scaffolding? (E.g., pre-written code with fill-in-the-blanks)
- Slower pace? (Skip one activity to deepen the core concepts)
- Better pre-class prep? (More explicit setup instructions)

---

**End of Facilitator Notes**

Good luck with your session! Remember: your enthusiasm and patience are contagious. Students will mirror your energy. If you show that errors are learning opportunities, they'll embrace the struggle. You've got this.
