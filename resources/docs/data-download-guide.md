# Data Download Guide

Learners are responsible for fetching the open datasets used in weekly QGIS activities. This guide provides step-by-step instructions and folder conventions so everyone practices sourcing, unzipping, and staging spatial data before class. Use it alongside the checkbox tracker in `resources/docs/data-download-checklist.md` to confirm files are ready before each session.

> **Why boundaries matter:** Many datasets in this course are aggregated to administrative or statistical units (SA2, LGA, counties). Review `resources/docs/readings/week03-admin-boundaries.md` so you understand the context of each geography before downloading and joining data.

## General workflow

1. Create a folder for the week inside `~/Documents/intro-to-gis-course/data/raw/` (or your chosen workspace). Example: `data/raw/week01/`.
2. Download the dataset from the official source listed below.
3. If the download is a ZIP file, extract it inside the week folder. Keep the original ZIP for reference.
4. Copy or move only the files you need into `data/processed/<week>/` once you have cleaned or filtered them.
5. Update `resources/docs/data-inventory.md` with the dataset name, download date, and any processing notes.

## Week 1 — Natural Earth starter data

**Goal:** Load global boundaries to explore the QGIS interface.

1. Visit [Natural Earth Download](https://www.naturalearthdata.com/downloads/).
2. Under **Cultural** scroll to the **Admin 0 – Countries** section and click the **Download small scale data** link (1:110m). The file `ne_110m_admin_0_countries.zip` will download.
3. Optional: repeat for **Admin 1 – States/Provinces (1:110m)** to support subnational exercises.
4. Move the ZIP files to `data/raw/week01/natural-earth/`, then extract them so the folder contains the `.shp`, `.dbf`, `.shx`, `.prj`, and `.cpg` files.
5. In QGIS, add `ne_110m_admin_0_countries.shp` (Browser panel ▶ drag into canvas).
6. Log the dataset name, scale, and download date in `resources/docs/data-inventory.md`.

## Week 2 — Design practice datasets

**Goal:** Style thematic data and label cities.

### Renewable energy share (Our World in Data)

1. Visit [Our World in Data — Renewable Energy](https://ourworldindata.org/renewable-energy).
2. Find the **Data Explorer** panel (right-hand side) and click **Download data**.
3. Select **Download as CSV**. The file downloads as `renewable-energy-data.csv`.
4. Save the CSV to `data/raw/week02/renewable-energy/`. Do not alter column names.
5. Open the CSV in a spreadsheet tool, filter for the latest year you plan to visualise, and save the filtered version to `data/processed/week02/renewable-energy-latest.csv`.
6. When joining in QGIS, match `iso_code` from the CSV to the ISO country code field in Natural Earth.

### World cities (lite dataset)

1. Visit [SimpleMaps World Cities](https://simplemaps.com/data/world-cities).
2. Click **Download** under “World Cities Database Lite (free)”.
3. Provide an email address; SimpleMaps emails a download link. Download the `worldcities_basic.zip` file.
4. Save and extract the ZIP into `data/raw/week02/world-cities/` so `worldcities.csv` is accessible.
5. In QGIS choose `Layer ▶ Add Layer ▶ Add Delimited Text Layer…`, select `worldcities.csv`, set X field to `lng`, Y field to `lat`, CRS to `EPSG:4326`, then load the points.
6. Review the license requirements on the SimpleMaps page and note attribution language for use in layouts.

## Week 3 — Vector joins & demographics

**Goal:** Pair statistical indicators with boundary polygons for thematic mapping. Choose the example that matches your context.**

### Option A (Australia) — ASGS SA2 + SEIFA 2021

1. Open the ABS digital boundary files hub: https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files.
2. Under **Digital Boundaries**, click **“SA2 2021 Digital Boundaries in ESRI Shapefile Format”**. Save the ZIP (for example, `1270055001_sa2_2021_aust_shape.zip`) to `data/raw/week03/asgs-sa2/` and extract all files.
3. Download SEIFA 2021 indexes from https://www.abs.gov.au/statistics/people/people-and-communities/socio-economic-indexes-areas-seifa-australia/latest-release#data-downloads. In **Index data cubes**, grab **Statistical Area Level 2, Indexes, SEIFA 2021.xlsx** and save to `data/raw/week03/seifa/`.
4. Open the Excel file, keep the columns you need (e.g., `SA2_CODE_2021`, `IRSD_SCORE`, deciles), and export a cleaned CSV to `data/processed/week03/seifa_sa2.csv`.
5. Load the SA2 shapefile in QGIS and join the cleaned CSV using `SA2_CODE_2021`. Use the joined layer for choropleth practice.
6. Log download dates, version information, and cleaning steps in `resources/docs/data-inventory.md`.

### Option B (United States)

1. On https://data.census.gov/, search for table `B19013`. Use **Download**, choose geography, and export the CSV to `data/raw/week03/acs_income.zip`. Extract the contents.
2. Download boundaries from the TIGER/Line catalogue (https://www.census.gov/cgi-bin/geo/shapefiles/index.php), saving the shapefile to `data/raw/week03/tiger/` and extracting it.
3. Join the CSV to the shapefile on the GEOID/FIPS field and record all filters and projections in the inventory.

### Option C (Other regions)

- Use your national open data portal to download a boundary shapefile/GeoJSON and matching indicator table. Store both datasets under `data/raw/week03/<dataset>/` and follow the same join workflow.

## Week 4 — Raster & terrain

**Goal:** Bring in elevation data for surface analysis.**

### Option A (Australia) — ELVIS Digital Elevation Model

1. Visit Geoscience Australia's ELVIS portal: https://elevation.fsdf.org.au/.
2. Click **Get Data** ▶ **Guest Login** (or use your account).
3. Draw or upload your area of interest, then select **DEM (1 Second SRTM Derived)** or the resolution you need.
4. Add the dataset to your cart and download the generated ZIP to `data/raw/week04/elvis-dem/`. Extract the GeoTIFF(s).
5. Mosaic or clip the tiles in QGIS as required and save the output to `data/processed/week04/elvis_dem_clip.tif`.

### Option B (Global) — NASA SRTM

1. Ensure you have a NASA Earthdata login: https://urs.earthdata.nasa.gov/.
2. Browse the SRTMGL1.003 collection (https://e4ftl01.cr.usgs.gov/MEASURES/SRTMGL1.003/), download the tile covering your area (e.g., `S34E151.SRTMGL1.hgt.zip`), and save to `data/raw/week04/srtm/`.
3. Extract the `.hgt` file, convert it to GeoTIFF in QGIS (`Raster ▶ Conversion ▶ Translate`), and clip to your AOI. Note tile names and processing steps in the inventory.

## Week 5 — Crime case study

**Goal:** Pull incident-level crime data for hotspot analysis.**

### Option A (Australia) — NSW Recorded Crime (BOCSAR)

1. Go to the BOCSAR Open Datasets page: <https://bocsar.nsw.gov.au/statistics-dashboards/open-datasets/criminal-offences-data.html>.
2. Under **"Monthly counts of criminal incidents"**, find the row for **"Local Government Area"** and download the Excel file. Save to `data/raw/week05/nsw-crime/offences_by_lga.xlsx`.
3. Filter the data to the offences and time period you need (e.g., assault offences for 2022) in a spreadsheet, saving the result to `data/processed/week05/nsw-crime-filtered.csv`.
4. Download NSW LGA boundaries from the ABS ASGS shapefile and store under `data/raw/week05/nsw-lga/`.
5. Join the filtered CSV to the LGA layer in QGIS using the LGA code. Export to `data/processed/week05/nsw-crime.gpkg` and record filters in the inventory.

### Option B (Other regions)

- Follow the same process using your local open data portal (e.g., City of Chicago crime dataset, London Metropolitan Police data). Document offence filters and date ranges.

## Week 6 — Public health & accessibility

**Goal:** Combine vulnerability scores with health facility locations.**

### Option A (Australia)

1. **Vulnerability index:** Reuse the SEIFA SA2 CSV from Week 3 or download the Australian Remoteness Area (ARIA+) dataset from the ABS. Store under `data/raw/week06/seifa/` or `data/raw/week06/aria/`.
2. **Health services:** Download the National Health Services Directory (NHSD) public dataset from https://data.gov.au/dataset/ds-dga-4b10c443-4906-4d30-b3c6-a2ad99b04051/details. Save the CSV to `data/raw/week06/nhsd/health_services.csv`.
3. Filter the services to the categories you need (e.g., hospitals, GPs) and save the cleaned file to `data/processed/week06/health_services_filtered.csv`.
4. For road networks, download the relevant OpenStreetMap extract from https://download.geofabrik.de/ (e.g., `australia-oceania/australia-latest.osm.pbf`) and store under `data/raw/week06/osm/`.
5. Document filters, service categories, and any geocoding adjustments in `resources/docs/data-inventory.md`.

### Option B (Other regions)

- Use equivalent datasets (e.g., U.S. CDC SVI + HRSA clinics) and follow the same storage conventions.

## Weeks 7–12 — Bridge to Python & beyond

Use the datasets above plus any capstone-specific sources. For Python weeks, replicate the same structure inside `data/processed/week08/`, `week09/`, etc., so notebooks can load files with relative paths.

> **Tip:** Keep raw downloads intact. Perform cleaning steps in QGIS or Python, then save new layers into `data/processed/` with descriptive filenames. Document every transformation in the data inventory to support reproducibility.
