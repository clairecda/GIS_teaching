# Data Download Checklist

Use this checklist to confirm you have downloaded and staged the required datasets before each session. Store files in your course workspace (`intro-to-gis-course/`) following the folder structure outlined in `resources/docs/data-download-guide.md`.

## Week 1 — QGIS Orientation

- [ ] `data/raw/week01/natural-earth/ne_110m_admin_0_countries.*`
- [ ] `data/raw/week01/natural-earth/ne_10m_admin_1_states_provinces.*` (optional)

## Week 2 — Symbology & Layouts

- [ ] `data/raw/week02/renewable-energy/renewable-energy-data.csv` (rename downloaded CSV if needed)
- [ ] `data/raw/week02/world-cities/worldcities_basic.csv`

## Week 3 — Vector Analysis

- [ ] `data/raw/week03/asgs-sa2/` (or equivalent boundary shapefile)
- [ ] `data/processed/week03/seifa_sa2.csv` (or other indicator table)

## Week 4 — Raster & Terrain

- [ ] `data/raw/week04/elvis-dem/*.tif` (ELVIS download) **or** `data/raw/week04/srtm/*.hgt`
- [ ] `data/processed/week04/elvis_dem_clip.tif` (clipped/mosaicked output)

## Week 5 — Crime Case Study

- [ ] `data/raw/week05/nsw-crime/offences_by_lga.csv` (or local crime dataset)
- [ ] `data/processed/week05/nsw-crime.gpkg`

## Week 6 — Public Health & Accessibility

- [ ] `data/raw/week06/seifa/` or `data/raw/week06/aria/` (vulnerability index)
- [ ] `data/raw/week06/nhsd/health_services.csv`
- [ ] `data/raw/week06/osm/*.osm.pbf` (optional road network)
- [ ] `data/processed/week06/health_services_filtered.csv` (cleaned subset)

## Week 7 — Bridge to Python

- [ ] Confirm all required QGIS datasets above are organised under `data/`
- [ ] Verify managed environment access (dev container or conda)

## Week 8 — Python Vector Workflows

- [ ] `data/processed/week08/neighbourhoods.geojson`
- [ ] `data/processed/week08/incidents.geojson`
- [ ] `data/processed/week08/neighbourhoods_summary.gpkg`

## Week 9 — Raster & Remote Sensing in Python

- [ ] `data/processed/week09/sentinel_before.tif`
- [ ] `data/processed/week09/sentinel_after.tif`
- [ ] `data/processed/week09/aoi.geojson`
- [ ] `data/processed/week09/zones.geojson`

## Week 10 — Transport Networks

- [ ] `data/processed/week10/facilities.geojson`
- [ ] `data/processed/week10/population.geojson` (optional)
- [ ] `data/processed/week10/outputs/isochrones.gpkg`

## Week 11 — Design & Storytelling

- [ ] Latest project layers exported for layout critique (list filenames here)

## Week 12 — Capstone

- [ ] Final dataset inventory documented in `resources/docs/data-inventory.md`
- [ ] All project inputs/outputs stored under `data/` with clear names
