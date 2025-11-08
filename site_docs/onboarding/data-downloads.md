# Downloading Datasets

Learners are responsible for downloading the datasets used in weekly QGIS activities. Follow this guide alongside the checklist in [Reference ▸ Dataset inventory](../reference/data-inventory.md) and [Reference ▸ Data download checklist](../reference/data-download-checklist.md) to confirm files are ready before each session.

!!! note "Why boundaries matter"
    Many datasets in this course are aggregated to administrative or statistical units (SA2, LGA, counties). Review [Understanding administrative boundaries](../readings/week03-admin-boundaries.md) so you know the context of each geography before downloading and joining data.

## General workflow

Follow these exact steps for every dataset so your workspace stays organised:

1. **Create a weekly raw folder**  
   - Open Finder (macOS) or File Explorer (Windows) and navigate to your course workspace (e.g., `Documents/intro-to-gis-course/`).  
   - Inside `data/raw/`, create a new folder for the week (e.g., `data/raw/week01/`).
2. **Download the source file**  
   - Use the official link in this guide and save the file directly into that raw folder.
3. **Extract ZIP archives**  
   - If the download is a ZIP, right-click → “Extract”/“Open With Archive Utility” in the same folder.  
   - Keep both the ZIP and the extracted files (e.g., `.shp`, `.dbf`, `.tif`).
4. **Create processed copies when needed**  
   - After cleaning or filtering data (in QGIS, spreadsheets, or Python), save the output into a matching processed folder (e.g., `data/processed/week02/renewable-energy-latest.csv`).
5. **Record download & processing details**  
   - Update your copy of `resources/docs/data-inventory.md` (or a project log) with:  
     - Dataset name + URL  
     - Download date and version/vintage  
     - Local file paths (raw + processed)  
     - Filters/processing performed  
     - Licensing or usage notes  

Repeat these steps for every dataset so your project stays organised and reproducible.

Repeat these steps for every dataset so anyone (including your future self) can reproduce your work.

## Week 1 — Natural Earth starter data

**Goal:** Load global boundaries to explore the QGIS interface.

1. Visit [Natural Earth Downloads](https://www.naturalearthdata.com/downloads/).
2. Under **Cultural**, select **Admin 0 – Countries** → **Download small scale data** (1:110m). This downloads `ne_110m_admin_0_countries.zip`.
3. Optional: repeat for **Admin 1 – States/Provinces** (1:110m) for subnational exercises.
4. Move the ZIP files to `data/raw/week01/natural-earth/`, extract so the folder contains `.shp`, `.dbf`, `.shx`, `.prj`, and `.cpg`.
5. In QGIS, add `ne_110m_admin_0_countries.shp` via the Browser panel and confirm the data loads.

## Week 2 — Design practice datasets

**Goal:** Style thematic data and label cities.

### Renewable energy share (Our World in Data)

1. Visit [Our World in Data — Renewable Energy](https://ourworldindata.org/renewable-energy).
2. In the **Data Explorer**, click **Download data** → **Download as CSV** (`renewable-energy-data.csv`).
3. Save to `data/raw/week02/renewable-energy/` without renaming columns.
4. Filter for the latest year in a spreadsheet and save the filtered copy to `data/processed/week02/renewable-energy-latest.csv`.
5. Join `iso_code` to Natural Earth’s ISO field when styling choropleths.

### World cities (SimpleMaps)

1. Go to [SimpleMaps World Cities](https://simplemaps.com/data/world-cities) and click **Download** under “World Cities Database Lite (free)”.
2. Provide an email address to receive the download link. Save `worldcities_basic.zip` to `data/raw/week02/world-cities/` and extract.
3. In QGIS, choose `Layer ▶ Add Layer ▶ Add Delimited Text Layer…`, set X = `lng`, Y = `lat`, CRS = `EPSG:4326`, and load the points.
4. Note the attribution requirements on the SimpleMaps site.

## Week 3 — Vector joins & demographics

**Goal:** Pair statistical indicators with boundary polygons for thematic mapping.**

### Option A (Australia) — ASGS SA2 + SEIFA 2021

1. Download the SA2 shapefile from the ABS digital boundary files page: <https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files>.
   - Scroll to **Downloads for GDA2020 digital boundary files**.
   - Expand **Main Structure and Greater Capital City Statistical Areas**.
   - Click **Statistical Areas Level 2 – 2021 – Shapefile** to download `1270055001_sa2_2021_aust_shape.zip`.
   - Store the ZIP under `data/raw/week03/asgs-sa2/` and extract.
2. Download SEIFA 2021 indexes from <https://www.abs.gov.au/statistics/people/people-and-communities/socio-economic-indexes-areas-seifa-australia/latest-release#data-downloads>.
   - Scroll to **Data downloads** and expand **Index data cubes**.
   - Click **Statistical Area Level 2, Indexes, SEIFA 2021.xlsx**.
   - Save the Excel file to `data/raw/week03/seifa/` and extract/convert as needed.
3. Clean the CSV (retain `SA2_CODE_2021` and relevant index columns) and save to `data/processed/week03/seifa_sa2.csv`.
4. Join the CSV to the SA2 shapefile on `SA2_CODE_2021` inside QGIS.

### Option B (United States)

1. Export table `B19013` from [data.census.gov](https://data.census.gov/) to `data/raw/week03/acs_income.zip`, then extract.
2. Download matching boundaries (e.g., counties) from the [TIGER/Line catalogue](https://www.census.gov/cgi-bin/geo/shapefiles/index.php) and extract to `data/raw/week03/tiger/`.
3. Join the CSV to the shapefile using GEOID/FIPS fields.

### Option C (Other regions)

- Use your local open data portal to obtain boundary and indicator datasets, then follow the same join workflow.

## Week 4 — Raster & terrain

**Goal:** Bring in elevation data for surface analysis.**

### Option A (Australia) — ELVIS DEM

1. Visit <https://elevation.fsdf.org.au/>, log in as guest, and draw your area of interest.
2. Add **DEM (1 Second SRTM Derived)** to your cart and download the ZIP to `data/raw/week04/elvis-dem/`. Extract the GeoTIFF(s).
3. Mosaic or clip the tiles in QGIS, saving outputs to `data/processed/week04/elvis_dem_clip.tif`.

### Option B (Global) — NASA SRTM

1. Ensure you have a NASA Earthdata login (<https://urs.earthdata.nasa.gov/>).
2. Download the relevant tile from <https://e4ftl01.cr.usgs.gov/MEASURES/SRTMGL1.003/> (e.g., `S34E151.SRTMGL1.hgt.zip`) to `data/raw/week04/srtm/` and extract.
3. Convert to GeoTIFF and clip to your AOI as in the ELVIS workflow.

## Week 5 — Crime case study

**Goal:** Pull incident-level crime data for hotspot analysis.**

### Option A (Australia) — NSW Recorded Crime (BOCSAR)

1. Download the “Recorded Crime Offences by Local Government Area (CSV)” from <https://data.nsw.gov.au/data/dataset/nsw-recorded-crime-statistics> to `data/raw/week05/nsw-crime/offences_by_lga.csv`.
2. Filter to relevant offences/time periods, saving the cleaned file to `data/processed/week05/nsw-crime-filtered.csv`.
3. Download NSW LGA boundaries (same resource or ASGS LGA shapefile) to `data/raw/week05/nsw-lga/` and extract.
4. Join the CSV to the LGA layer in QGIS on the LGA code and export to `data/processed/week05/nsw-crime.gpkg`.

### Option B (Other regions)

- Follow the equivalent workflow on your local open data portal (e.g., City of Chicago crime dataset) and document any filters.

## Week 6 — Public health & accessibility

**Goal:** Combine vulnerability scores with health facility locations.**

1. Use SEIFA (from Week 3) or download ARIA+ (Australian remoteness index) from the ABS; store under `data/raw/week06/seifa/` or `data/raw/week06/aria/`.
2. Download the National Health Services Directory dataset from <https://data.gov.au/dataset/ds-dga-4b10c443-4906-4d30-b3c6-a2ad99b04051/details> to `data/raw/week06/nhsd/health_services.csv`.
3. Filter to relevant service categories and save to `data/processed/week06/health_services_filtered.csv`.
4. Optionally download an OpenStreetMap extract for your region from <https://download.geofabrik.de/> and store under `data/raw/week06/osm/` for network analysis.

## Weeks 7–12 — Bridge to Python & beyond

- Reuse the datasets above plus any capstone-specific sources.
- For notebooks, mirror the raw/processed structure so paths such as `../data/processed/week08/...` resolve correctly.
- Document every transformation (scripts, joins, clips) in the dataset inventory; this ensures your capstone is reproducible.

> Keep raw downloads intact. Save cleaned outputs with descriptive filenames (e.g., `seifa_sa2_2021_clean.csv`) and note all processing steps so you can revisit or share them later.
