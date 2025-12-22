# Python for GIS

**Read before:** Week 7 | **Time:** 15 minutes

---

## Why Python?

You've spent 6 weeks clicking through QGIS menus. It works, but:

- **Repetitive:** Same clicks for every dataset
- **Hard to share:** Can you give someone your clicks?
- **Not reproducible:** Will you remember what you did in 6 months?

Python solves these problems. Write code once, run it on any dataset, share it with anyone, come back years later and know exactly what happened.

---

## What can Python do for GIS?

Everything you did in QGIS, plus more:

| Task | QGIS | Python |
|------|------|--------|
| Load data | Add Layer | `gpd.read_file()` |
| Filter rows | Select by Expression | `df[df['pop'] > 1000]` |
| Join tables | Join by field | `df.merge()` |
| Spatial join | Join by location | `gpd.sjoin()` |
| Calculate area | Field Calculator | `df['area'] = df.geometry.area` |
| Create map | Print Layout | `df.plot()` |
| Export | Save As | `df.to_file()` |

**Plus:**
- Process 100 files in a loop
- Pull data from web APIs
- Build interactive maps
- Create reproducible reports

---

## The Python GIS stack

You don't need to understand all of these yet — just know they exist:

### Core libraries

| Library | What it does |
|---------|--------------|
| **GeoPandas** | Vector data — the GIS equivalent of pandas |
| **Rasterio** | Raster data — read/write GeoTIFFs |
| **Shapely** | Geometry operations — buffers, intersections |
| **Pyproj** | Coordinate transformations |

### Visualisation

| Library | What it does |
|---------|--------------|
| **Matplotlib** | Static plots and maps |
| **Folium** | Interactive web maps |
| **Contextily** | Add basemaps to static maps |

### Analysis

| Library | What it does |
|---------|--------------|
| **OSMnx** | Download and analyse street networks |
| **NetworkX** | Graph/network analysis |
| **Rasterstats** | Zonal statistics on rasters |

---

## How Python code looks

Don't worry about understanding this yet. Just see the pattern:

```python
# Load a shapefile
import geopandas as gpd
suburbs = gpd.read_file("suburbs.shp")

# Filter to one state
nsw = suburbs[suburbs['state'] == 'NSW']

# Calculate area in square km
nsw['area_km2'] = nsw.geometry.area / 1_000_000

# Save the result
nsw.to_file("nsw_suburbs.gpkg")
```

**Four lines of code** = what might take 10 clicks in QGIS.

---

## Jupyter notebooks

You'll write Python in **Jupyter notebooks** — documents that mix:

- **Code cells:** Run Python code
- **Markdown cells:** Write notes and explanations
- **Output:** See results immediately below each cell

This makes your analysis:
- **Documented:** Explain what you're doing as you go
- **Reproducible:** Anyone can run the same notebook
- **Shareable:** Send the notebook, not just the results

---

## What you'll learn

| Week | Focus | Key skills |
|------|-------|------------|
| 7 | Setup | Install Anaconda, run Jupyter, load data |
| 8 | Vector | Filter, join, aggregate, export with GeoPandas |
| 9 | Raster | Load imagery, calculate NDVI, zonal stats |
| 10 | Networks | Download roads, calculate routes, isochrones |

By Week 10, you'll be able to automate the workflows you did manually in Weeks 1-6.

---

## Don't panic

Learning to code feels hard at first. Some reassurance:

- **Errors are normal.** Even experts see errors constantly.
- **You don't memorise syntax.** You look it up. Every time.
- **Start by copying.** Modify working examples before writing from scratch.
- **One step at a time.** Get one line working, then the next.

The goal isn't to become a programmer. It's to **automate your GIS work**.

---

## Key terms

| Term | Meaning |
|------|---------|
| **Library/package** | Pre-written code you import (like a QGIS plugin) |
| **DataFrame** | A table of data (rows and columns) |
| **GeoDataFrame** | A DataFrame with geometry (spatial data) |
| **Notebook** | A document mixing code, text, and output |
| **Environment** | An isolated set of installed packages |

---

## Preparation for Week 7

Before class:

1. Install Anaconda (see [Python Setup](../onboarding/04-python-setup.md))
2. Create the `intro-gis` environment
3. Test that Jupyter launches
4. Run `import geopandas` without errors

If you get stuck, bring your questions to class.

---

## Key takeaways

✅ **Python automates repetitive tasks** — write once, run many times

✅ **GeoPandas is like QGIS in code** — same concepts, different interface

✅ **Notebooks document your work** — code + explanation together

✅ **Errors are normal** — debugging is part of the process

✅ **You don't need to memorise** — copy, adapt, look things up
