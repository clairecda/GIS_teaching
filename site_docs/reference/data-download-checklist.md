# Data Download Checklist

Use this checklist during class as your facilitator guides you through each download. Tick off items as you complete them together.

!!! tip "In-class reference"
    Downloads happen during class time—no pre-class homework! See [Download Datasets](../onboarding/03-download-data.md) for step-by-step instructions.

---

## Folder structure

Each week has its own folder:

```
intro-gis/
├── week01/
│   └── data/
│       ├── raw/        ← Downloads go here (never edit)
│       └── processed/  ← Your modified files go here
├── week02/
└── ...
```

---

## Week 1 — QGIS Orientation

**Source:** [Natural Earth](https://www.naturalearthdata.com/downloads/)

- [ ] Downloaded `ne_110m_admin_0_countries.zip`
- [ ] Extracted ZIP file
- [ ] Files in `week01/data/raw/`:
    - [ ] `ne_110m_admin_0_countries.shp`
    - [ ] `ne_110m_admin_0_countries.dbf`
    - [ ] `ne_110m_admin_0_countries.shx`
    - [ ] `ne_110m_admin_0_countries.prj`

---

## Week 2 — Symbology & Layouts

**Sources:** [SimpleMaps](https://simplemaps.com/data/world-cities), [Our World in Data](https://ourworldindata.org/renewable-energy)

- [ ] Downloaded `worldcities.csv` from SimpleMaps
- [ ] Downloaded renewable energy CSV from Our World in Data
- [ ] Files in `week02/data/raw/`:
    - [ ] `worldcities.csv`
    - [ ] `renewable-energy-share.csv` (or similar name)

---

## Week 3 — Vector Analysis

**Sources:** [ABS Digital Boundaries](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files), [ABS SEIFA](https://www.abs.gov.au/statistics/people/people-and-communities/socio-economic-indexes-areas-seifa-australia/latest-release)

- [ ] Downloaded SA2 boundaries (shapefile)
- [ ] Extracted ZIP file
- [ ] Downloaded SEIFA data (Excel or CSV)
- [ ] Files in `week03/data/raw/`:
    - [ ] SA2 shapefile (`.shp`, `.dbf`, `.shx`, `.prj`)
    - [ ] SEIFA data file

---

## Week 4 — Flood Risk Assessment

**Sources:** [ELVIS](https://elevation.fsdf.org.au/) (Australia) or [USGS EarthExplorer](https://earthexplorer.usgs.gov/) (global)

**Study area:** Hawkesbury-Nepean floodplain (west of Sydney)

- Bounding box: approximately 150.6°E to 150.85°E, 33.65°S to 33.45°S
- Keep it small (~20km × 20km) for faster processing

- [ ] Identified study area on ELVIS map
- [ ] Downloaded DEM tiles for Hawkesbury-Nepean region
- [ ] Extracted any ZIP files
- [ ] Downloaded SA2 boundaries for study area (from Week 3 or ABS)
- [ ] Files in `week04/data/raw/`:
    - [ ] DEM raster file(s) (`.tif` or similar)
    - [ ] SA2 boundaries (for zonal statistics)

---

## Week 5 — Crime Case Study

**Sources:** [BOCSAR](https://www.bocsar.nsw.gov.au/) (NSW), [data.police.uk](https://data.police.uk/) (UK), or local open data portal

- [ ] Downloaded crime statistics (CSV)
- [ ] Downloaded LGA boundaries (shapefile)
- [ ] Extracted any ZIP files
- [ ] Files in `week05/data/raw/`:
    - [ ] Crime data CSV
    - [ ] LGA shapefile (`.shp`, `.dbf`, `.shx`, `.prj`)

---

## Week 6 — Public Health & Accessibility

**Sources:** State data portal (e.g., [data.nsw.gov.au](https://data.nsw.gov.au))

- [ ] Downloaded health facility locations
- [ ] Files in `week06/data/raw/`:
    - [ ] Health facilities (CSV, shapefile, or GeoJSON)
    - [ ] (Optional) Road network data

---

## Week 7 — Bridge to Python

**No data download required!**

- [ ] Python environment set up (see [Python Setup](../onboarding/04-python-setup.md))
- [ ] Created `week07/` folder with `data/raw/` and `data/processed/`
- [ ] Notebook downloads sample data automatically

---

## Week 8 — Python Vector Workflows

**No download needed!** The notebook automatically downloads NYC sample data.

- [ ] Run the notebook — it downloads NYC neighbourhoods + 311 complaints automatically

**Optional: Use your own data**

To use Australian data instead, export from QGIS and place in `week08/data/raw/`:
- [ ] `neighbourhoods.geojson` (from Week 3)
- [ ] `incidents.geojson` (from Week 5)

---

## Week 9 — Flood Risk (Python)

**No download needed!** The notebook fetches elevation data from Planetary Computer API.

- [ ] Run the notebook — it downloads Copernicus DEM automatically
- [ ] If API is unavailable, notebook falls back to synthetic terrain data

**What the notebook downloads automatically:**

- Copernicus DEM 30m for Hawkesbury-Nepean region
- SA2 boundaries (same study area as Week 4 QGIS)

**Optional: Use your own study area**

To analyze a different region, modify the bounding box in the notebook:
```python
bbox = [west, south, east, north]  # in decimal degrees
```

---

## Week 10 — Transport Networks

**No data download required!**

- [ ] Notebook downloads street network from OpenStreetMap automatically
- [ ] (Optional) Created `facilities.geojson` with custom locations

---

## Week 11 — Design & Storytelling

- [ ] Draft maps from previous weeks ready for critique

---

## Week 12 — Capstone

- [ ] All source datasets in `capstone/data/raw/`
- [ ] Analysis outputs in `capstone/data/processed/`
- [ ] Final maps in `capstone/exports/`

---

## Quick reference: File locations

| Week | Key files | Manual download? |
|------|-----------|------------------|
| 1 | `ne_110m_admin_0_countries.shp` | Yes |
| 2 | `worldcities.csv`, renewable energy CSV | Yes |
| 3 | SA2 shapefile, SEIFA data | Yes |
| 4 | DEM raster (Hawkesbury-Nepean), SA2 boundaries | Yes |
| 5 | Crime CSV, LGA shapefile | Yes |
| 6 | Health facilities | Yes |
| 7 | (none) | No — notebook creates data |
| 8 | (none) | No — notebook downloads NYC data |
| 9 | (none) | No — API fetches Copernicus DEM |
| 10 | (none) | No — OSMnx downloads from OpenStreetMap |
