# Data Inventory

Working list of candidate datasets for weekly case studies. Capture licensing notes, download links, update cadence, and preprocessing steps as you validate each source. Prefer open, well-documented datasets with permissive licenses.

| Theme | Dataset | Source | License / Access | Notes |
| ----- | ------- | ------ | ---------------- | ----- |
| Orientation | Natural Earth Admin 0/1 boundaries | https://www.naturalearthdata.com/ | Public domain | Lightweight shapefiles for quick plotting demos. |
| Orientation | Sample learner hometowns | Instructor-generated CSV | Permission from participants | Optional icebreaker data; anonymise before sharing publicly. |
| Symbology & design | Our World in Data — Renewable energy share | https://ourworldindata.org/renewable-energy | CC BY 4.0 | Download CSV for latest year and join to Natural Earth in Week 2. |
| Symbology & design | World cities with pop estimates | https://simplemaps.com/data/world-cities | Commercial/free tier | Use Lite version for labelling practice; verify licensing before redistribution. |
| Vector analysis | ABS ASGS Edition 3 SA2 boundaries | https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files | CC BY 4.0 (ABS) | Statewide/national shapefiles for Week 3 joins. |
| Vector analysis | ABS SEIFA 2021 (SA2 indexes) | https://www.abs.gov.au/statistics/people/people-and-communities/socio-economic-indexes-areas-seifa-australia/latest-release#data-downloads | CC BY 4.0 (ABS) | Provides socio-economic scores for joins; note index and revision. |
| Crime analytics | City of Chicago Crime | https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2 | Open Data Commons | Daily updates; filter by year to reduce size. |
| Crime analytics | NYC NYPD Complaint Data | https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Map/ | Open Data Commons | Use for comparative analysis or network hotspot mapping. |
| Crime analytics | UK Police street-level crime | https://data.police.uk/data/ | Open Government Licence | Small CSV extracts suitable for in-class practice. |
| Crime analytics | NSW Recorded Crime Offences by LGA | https://bocsar.nsw.gov.au/statistics-dashboards/open-datasets/criminal-offences-data.html | CC BY 4.0 | Download "Local Government Area" Excel under Monthly counts; pair with ASGS LGA boundaries. |
| Public health | CDC Social Vulnerability Index | https://www.atsdr.cdc.gov/place-health/php/svi/ | Public domain | Includes tract-level indices; pair with health facility locations. |
| Public health | Health Resources & Services Admin (HRSA) Health Center data | https://data.hrsa.gov | Public domain | Point locations + services metadata; useful for catchment analysis. |
| Public health | OpenStreetMap healthcare amenities | https://download.geofabrik.de/ | ODbL | Extract hospitals/clinics from OSM; or use state health data portals. |
| Environmental resilience | FEMA National Flood Hazard Layer | https://www.fema.gov/flood-maps | Public domain | Download subsets via FEMA GeoPlatform; requires preprocessing. |
| Environmental resilience | NOAA Sea Level Rise Raster | https://coast.noaa.gov/slrdata/ | Public domain | GeoTIFF rasters for sea-level scenarios; large files, clip to AOI. |
| Environmental resilience | NASA SRTM 30m DEM | https://earthexplorer.usgs.gov/ | Public domain | Search "SRTM 1 Arc-Second Global" for terrain analysis in Week 4. |
| Environmental resilience | Geoscience Australia ELVIS DEM | https://elevation.fsdf.org.au/ | CC BY 4.0 | Provides 1-second SRTM-derived DEM tiles across Australia. |
| Transport mobility | GTFS feeds (e.g., MBTA, WMATA) | https://mobilitydatabase.org/ | Varies | Document license per agency; convert to network for accessibility metrics. |
| Transport mobility | OpenStreetMap extracts | https://download.geofabrik.de/ | ODbL | Use for street networks, micromobility infrastructure. |
| Transport mobility | US DOT National Transit Map | https://data.transportation.gov/Transit/National-Transit-Map-NTM-Spring-2023/dxav-78z2 | Public domain | Alternate source for stop locations; useful when GTFS access is limited. |
| Spatial statistics | American Community Survey (ACS) 5-year estimates | https://www.census.gov/data/developers/data-sets/acs-5year.html | Public domain | Access via Census API; document year and variables used. |
| Spatial statistics | LA Times neighborhood boundaries | https://github.com/datadesk/california-neighborhoods | CC BY 4.0 | Use for polygon boundaries in vector join labs (Week 3 & Week 8). |
| Remote sensing | Landsat 8/9 Collection 2 | https://earthexplorer.usgs.gov/ | Public domain | Search for Landsat Collection 2; also available via AWS Open Data. |
| Remote sensing | Sentinel-2 Level-2A | https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR | Copernicus | Accessible via Earth Engine; log scripts for reproducibility. |
| Remote sensing | NOAA VIIRS Nighttime Lights | https://eogdata.mines.edu/products/vnl/#annual_v20 | Public domain | Useful for change detection storylines in Week 9. |
| Map design | ColorBrewer palettes | https://colorbrewer2.org/ | Public domain | Reference for accessible colour schemes in design week. |
| Map design | UN OCHA humanitarian icons | https://github.com/UN-OCHA/hid-graphics | CC BY 4.0 | Incorporate pictograms in Week 11 layouts; credit per license. |
| Cross-cutting | OpenStreetMap geocoding (Nominatim) | https://nominatim.org/ | ODbL | Use responsibly with rate limits; consider cached lookups. |
| Cross-cutting | Esri Living Atlas (selected datasets) | https://livingatlas.arcgis.com/ | Mixed | Curate downloadable items with permissive licenses; document any restrictions. |

## Tracking template

Record additional details in the table below as datasets are adopted.

| Dataset | Date acquired | Version / vintage | Local path | Processing steps | QA status | Maintainer |
| ------- | ------------- | ----------------- | ---------- | ---------------- | --------- | ---------- |

> Tip: keep processed files small and reproducible; document scripts in `notebooks/util/` or `scripts/`.
