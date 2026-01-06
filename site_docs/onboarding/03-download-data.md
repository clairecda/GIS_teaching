# 3. Download Datasets

Download the data you need before each week's lab.

---

## Folder structure reminder

Each week has its own folder with `raw/` and `processed/` inside:

```
intro-gis/
├── week01/
│   ├── data/
│   │   ├── raw/        ← Download files here
│   │   └── processed/  ← Save your modified data here
│   ├── week01.qgz
│   └── exports/
├── week02/
│   └── (same structure)
└── ...
```

**The rule:** Download to `raw/`, save your work to `processed/`.

---

## How to download and organise

1. **Create the week folder** (e.g., `intro-gis/week01/data/raw/`)
2. **Download** files into `raw/`
3. **Extract** any ZIP files (see below)
4. **Never edit** files in `raw/` — save changes to `processed/`

### How to extract ZIP files

=== "Windows"
    1. Right-click the ZIP file
    2. Click **Extract All...**
    3. Choose the same folder
    4. Click **Extract**

=== "Mac"
    1. Double-click the ZIP file
    2. It extracts automatically
    3. Delete the .zip file to avoid confusion

---

## Week 1 — Natural Earth

**What:** Global country boundaries

1. Go to [naturalearthdata.com/downloads](https://www.naturalearthdata.com/downloads/)
2. Click **Cultural** > **Admin 0 - Countries**
3. Download the **1:110m** scale
4. Save to `week01/data/raw/` and extract

!!! info "What are all these files?"
    A "shapefile" is actually 4+ files that work together:

    | File | What it contains |
    |------|------------------|
    | `.shp` | The shapes (geometry) |
    | `.dbf` | The data table (attributes) |
    | `.shx` | Index for fast access |
    | `.prj` | Coordinate system info |

    **Keep all files together!** In QGIS, open the `.shp` file.

---

## Week 2 — Cities and energy data

**Cities:**
1. Go to [simplemaps.com/data/world-cities](https://simplemaps.com/data/world-cities)
2. Download the free "Basic" version
3. Save to `week02/data/raw/`

**Renewable energy:**
1. Go to [ourworldindata.org/renewable-energy](https://ourworldindata.org/renewable-energy)
2. Click any chart > Download > CSV
3. Save to `week02/data/raw/`

---

## Week 3 — Boundaries + demographics

**Australia:**
- SA2 boundaries: [ABS Digital Boundary Files](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files)
- SEIFA indexes: [ABS SEIFA](https://www.abs.gov.au/statistics/people/people-and-communities/socio-economic-indexes-areas-seifa-australia/latest-release)

**Other regions:** Use your local census/statistics agency

Save to `week03/data/raw/`

---

## Week 4 — Elevation data

**Australia:** [ELVIS](https://elevation.fsdf.org.au/)

**Global:** [USGS EarthExplorer](https://earthexplorer.usgs.gov/) (free account required)

Save to `week04/data/raw/`

---

## Week 5 — Crime data

**Australia (NSW):** [BOCSAR Crime Statistics](https://www.bocsar.nsw.gov.au/Pages/bocsar_crime_stats/bocsar_crime_stats.aspx)

**UK:** [data.police.uk](https://data.police.uk/)

**US:** Search "[your city] open data crime"

Save to `week05/data/raw/`

---

## Week 6 — Health facilities

**Australia:** Search your state's data portal (e.g., data.nsw.gov.au)

**OpenStreetMap:** [Geofabrik downloads](https://download.geofabrik.de/) for road networks

Save to `week06/data/raw/`

---

## Week 7 — Python setup

No new datasets. Use Week 3 data to test your environment.

Your Week 7 folder will contain notebooks instead of QGIS projects:

```
week07/
├── data/
│   ├── raw/
│   └── processed/
├── week07.ipynb      ← Python notebook
└── exports/
```

---

## Week 8 — Vector workflows

Reuse data from Week 3 or Week 5.

**What you need:**
- Neighbourhood/SA2 polygons
- Point data (incidents, facilities)

!!! tip "Using Colab?"
    Notebooks include sample data URLs. No downloads needed!

---

## Week 9 — Raster & remote sensing

**Option A: Sample data (easiest)**
The notebook includes links to pre-processed imagery.

**Option B: Your own data**
1. Go to [Copernicus Browser](https://browser.dataspace.copernicus.eu/)
2. Create a free account
3. Download two images from different dates
4. Save to `week09/data/raw/`

---

## Week 10 — Transport networks

**Street networks:** Downloaded automatically by OSMnx — no manual download!

**Facilities:** Reuse from Week 6, or use sample data in notebook.

---

## Weeks 11-12 — Design & Capstone

Use outputs from previous weeks. No new datasets required.

---

## Checklist

Use the [Data Download Checklist](../reference/data-download-checklist.md) to track your downloads.

---

**Next step (Week 7+):** [4. Python setup](04-python-setup.md)
