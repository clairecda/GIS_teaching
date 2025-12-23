# 3. Download Datasets

Download the data you need before each week's lab. Start with Week 1.

---

## How to organise downloads

1. **Create a week folder** in `data/raw/` (e.g., `data/raw/week01/`)
2. **Download** files into that folder
3. **Extract** ZIP files in place
4. **Keep originals** — work from copies in `data/processed/` when editing

---

## Week 1 — Natural Earth

**What:** Global country boundaries to explore QGIS

1. Go to [naturalearthdata.com/downloads](https://www.naturalearthdata.com/downloads/)
2. Click **Cultural** > **Admin 0 - Countries**
3. Download the **1:110m** scale (small file, good for learning)
4. Save to `data/raw/week01/` and extract the ZIP
5. You should see files ending in `.shp`, `.dbf`, `.shx`, `.prj`

---

## Week 2 — Cities and energy data

**Cities (for labelling practice):**

1. Go to [simplemaps.com/data/world-cities](https://simplemaps.com/data/world-cities)
2. Download the free "Basic" version
3. Save to `data/raw/week02/` and extract

**Renewable energy (for choropleth):**

1. Go to [ourworldindata.org/renewable-energy](https://ourworldindata.org/renewable-energy)
2. Click any chart > Download > CSV
3. Save to `data/raw/week02/`

---

## Week 3 — Boundaries + demographics

**Australia option:**

- SA2 boundaries: [ABS Digital Boundary Files](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files)
- SEIFA indexes: [ABS SEIFA](https://www.abs.gov.au/statistics/people/people-and-communities/socio-economic-indexes-areas-seifa-australia/latest-release)

**Other regions:** Use your local census/statistics agency

---

## Week 4 — Elevation data

**Australia:** [ELVIS](https://elevation.fsdf.org.au/) — free DEM tiles

**Global:** [USGS EarthExplorer](https://earthexplorer.usgs.gov/) — SRTM data (requires free account)

---

## Week 5 — Crime data

**Australia (NSW):** [BOCSAR Crime Statistics](https://www.bocsar.nsw.gov.au/Pages/bocsar_crime_stats/bocsar_crime_stats.aspx)

**UK:** [data.police.uk](https://data.police.uk/)

**US:** Search "[your city] open data crime"

---

## Week 6 — Health facilities

**Australia:** Search your state's data portal (e.g., data.nsw.gov.au)

**OpenStreetMap:** [Geofabrik downloads](https://download.geofabrik.de/) for road networks

---

## Week 7 — Python setup

No new datasets needed. Use Week 3 data to test your environment.

---

## Week 8 — Vector workflows

Reuse your Week 3 or Week 5 data, or use the sample data included in the notebook.

**What you need:**

- Neighbourhood/SA2 polygons (from Week 3)
- Point data (incidents, facilities, etc.)

!!! tip "Using Colab?"
    The notebook includes sample data URLs you can load directly. No downloads needed!

---

## Week 9 — Raster & remote sensing

**Option A: Sample data (easiest)**

The notebook includes links to pre-processed Sentinel-2 imagery.

**Option B: Download your own**

1. Go to [Copernicus Browser](https://browser.dataspace.copernicus.eu/)
2. Create a free account
3. Draw a small area of interest
4. Download two images from different dates (before/after)
5. Save to `data/raw/week09/`

---

## Week 10 — Transport networks

**Street networks:** Downloaded automatically by OSMnx — no manual download needed!

**Facilities:** Reuse health facilities from Week 6, or use sample data in the notebook.

---

## Weeks 11-12 — Design & Capstone

Use outputs from all previous weeks. No new datasets required.

---

## Checklist

Use the [Data Download Checklist](../reference/data-download-checklist.md) to track what you've downloaded.

---

**Next step (Week 7+):** [4. Python setup](04-python-setup.md)
