# Data Download Checklist

Tick off each item as you download. See [Download Datasets](../onboarding/03-download-data.md) for step-by-step instructions.

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

## Week 4 — Raster & Terrain

**Sources:** [ELVIS](https://elevation.fsdf.org.au/) (Australia) or [USGS EarthExplorer](https://earthexplorer.usgs.gov/) (global)

- [ ] Identified study area (keep it small!)
- [ ] Downloaded DEM tiles
- [ ] Extracted any ZIP files
- [ ] Files in `week04/data/raw/`:
    - [ ] DEM raster file(s) (`.tif` or similar)

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

## Week 9 — Raster & Remote Sensing

**No download needed!** The notebook generates synthetic satellite data automatically.

- [ ] Run the notebook — it creates sample "before" and "after" imagery

**Optional: Use real Sentinel-2 imagery**

Only attempt this after completing the notebook with sample data:

1. [ ] Create free account at [Copernicus Browser](https://browser.dataspace.copernicus.eu/)
2. [ ] Draw study area (keep it small — 10km × 10km)
3. [ ] Select **Sentinel-2 L2A**, cloud cover <10%
4. [ ] Download TWO images (3-6 months apart)
5. [ ] Extract and find B04 (Red) and B08 (NIR) bands
6. [ ] Merge bands in QGIS: Raster → Miscellaneous → Merge
7. [ ] Save as `sentinel_before.tif` and `sentinel_after.tif`
8. [ ] Place in `week09/data/raw/`

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
| 4 | DEM raster | Yes |
| 5 | Crime CSV, LGA shapefile | Yes |
| 6 | Health facilities | Yes |
| 7 | (none) | No — notebook creates data |
| 8 | (none) | No — notebook downloads NYC data |
| 9 | (none) | No — notebook generates synthetic data |
| 10 | (none) | No — OSMnx downloads from OpenStreetMap |
