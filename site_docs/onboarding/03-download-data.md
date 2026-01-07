# 3. Download Datasets

This page gives you **exact steps** for each week's data downloads. Your facilitator will guide you through these during class—use this as a reference to follow along.

!!! tip "No pre-class downloads required"
    All data downloads happen during class time. Your facilitator will walk through the process step-by-step. This guide is for reference during class, not homework!

---

## Two rules

1. **Download to `raw/`** — never edit files in this folder
2. **Save your work to `processed/`** — your modified data goes here

```
intro-gis/
├── week01/
│   └── data/
│       ├── raw/        ← Download files here
│       └── processed/  ← Save your modified data here
├── week02/
│   └── (same structure)
└── ...
```

---

## How to extract ZIP files

Most spatial data downloads as ZIP files. You must extract them before use.

=== "Windows"
    1. Right-click the ZIP file
    2. Click **Extract All...**
    3. Choose the same folder (e.g., `raw/`)
    4. Click **Extract**
    5. You should now see the extracted files alongside the .zip

=== "Mac"
    1. Double-click the ZIP file
    2. It extracts automatically into the same folder
    3. Delete the .zip file to avoid confusion

!!! warning "Don't skip extraction!"
    QGIS cannot read files inside a ZIP. If you see a `.zip` file in your raw folder, extract it first.

---

## Week 1 — Natural Earth Countries

**What you need:** Global country boundaries (shapefile)

### Step-by-step

1. Go to [naturalearthdata.com/downloads](https://www.naturalearthdata.com/downloads/)
2. Under **Cultural**, click **Admin 0 – Countries**
3. Click the **Download countries** button for the **1:110m** scale (smallest file size, good for global maps)
4. Save the ZIP file to `week01/data/raw/`
5. **Extract the ZIP file** (see instructions above)

### What you should have

After extraction, your `raw/` folder should contain:

```
week01/data/raw/
├── ne_110m_admin_0_countries.shp    ← Open this in QGIS
├── ne_110m_admin_0_countries.dbf
├── ne_110m_admin_0_countries.shx
├── ne_110m_admin_0_countries.prj
└── (possibly other .cpg, .xml files)
```

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

## Week 2 — Cities and Energy Data

**What you need:** World cities (CSV) + Renewable energy statistics (CSV)

### Cities data

1. Go to [simplemaps.com/data/world-cities](https://simplemaps.com/data/world-cities)
2. Scroll down to **Download**
3. Click **Basic (Free)** to download `worldcities.csv`
4. Save to `week02/data/raw/`

### Renewable energy data

1. Go to [Our World in Data - Renewable Energy](https://ourworldindata.org/renewable-energy)
2. Scroll to any chart (e.g., "Share of electricity from renewables")
3. Click the **Download** tab below the chart
4. Click **Full data (CSV)**
5. Save to `week02/data/raw/`
6. Rename to something clear like `renewable-energy-share.csv`

### What you should have

```
week02/data/raw/
├── worldcities.csv
└── renewable-energy-share.csv
```

---

## Week 3 — Boundaries + Demographics

**What you need:** Statistical area boundaries + socioeconomic data

### For Australia: SA2 boundaries

1. Go to [ABS Digital Boundary Files](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files)
2. Scroll to **Statistical Area Level 2 (SA2)**
3. Download the **Shapefile** version
4. Save to `week03/data/raw/` and **extract**

### For Australia: SEIFA data

1. Go to [ABS SEIFA](https://www.abs.gov.au/statistics/people/people-and-communities/socio-economic-indexes-areas-seifa-australia/latest-release)
2. Click **Data downloads**
3. Download the **SA2** level data (Excel or CSV)
4. Save to `week03/data/raw/`

### For other countries

| Country | Boundaries | Demographics |
|---------|------------|--------------|
| USA | [Census TIGER/Line](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html) | [Census Reporter](https://censusreporter.org/) |
| UK | [ONS Geography](https://geoportal.statistics.gov.uk/) | [Nomis](https://www.nomisweb.co.uk/) |
| Global | [GADM](https://gadm.org/) | [World Bank](https://data.worldbank.org/) |

---

## Week 4 — Elevation Data (DEM)

**What you need:** Digital Elevation Model (raster)

### For Australia: ELVIS

1. Go to [ELVIS](https://elevation.fsdf.org.au/)
2. Click **Get Data**
3. Draw a rectangle over your study area (keep it small — 50km × 50km max)
4. Select **DEM** product
5. Click **Download**
6. Save to `week04/data/raw/` and **extract**

### For anywhere: SRTM via EarthExplorer

1. Go to [USGS EarthExplorer](https://earthexplorer.usgs.gov/)
2. Create a free account (required for downloads)
3. Under **Search Criteria**, enter your location or draw on the map
4. Under **Data Sets**, expand **Digital Elevation** > **SRTM**
5. Check **SRTM 1 Arc-Second Global**
6. Click **Results** and download the tile covering your area
7. Save to `week04/data/raw/`

!!! tip "DEM files are large"
    Start with a small area. A single SRTM tile is ~25MB compressed.

---

## Week 5 — Crime Data

**What you need:** Crime incident data (CSV or shapefile) + boundary data

### For NSW, Australia

1. Go to [BOCSAR Crime Statistics](https://www.bocsar.nsw.gov.au/Pages/bocsar_crime_stats/bocsar_crime_stats.aspx)
2. Click **Crime data download**
3. Select your area (LGA or suburb)
4. Download the CSV
5. Save to `week05/data/raw/`

You'll also need **LGA boundaries** from [ABS Digital Boundary Files](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files).

### For UK

1. Go to [data.police.uk](https://data.police.uk/data/)
2. Select a police force and date range
3. Click **Generate file**
4. Download and save to `week05/data/raw/`

### For US

Search for "[your city] open data crime" — most major cities publish crime data. Examples:
- [Chicago Crime Data](https://data.cityofchicago.org/)
- [Los Angeles Crime Data](https://data.lacity.org/)

---

## Week 6 — Health Facilities

**What you need:** Health facility locations (points) + optional road network

### Finding health facility data

| Region | Source |
|--------|--------|
| NSW | [data.nsw.gov.au](https://data.nsw.gov.au) — search "health facilities" |
| Victoria | [data.vic.gov.au](https://data.vic.gov.au) |
| Queensland | [data.qld.gov.au](https://data.qld.gov.au) |
| USA | [HIFLD Open Data](https://hifld-geoplatform.opendata.arcgis.com/) — search "hospitals" |
| Global | [Humanitarian Data Exchange](https://data.humdata.org/) |

### Road network (optional)

For accessibility analysis, you may need road data:
- [Geofabrik OpenStreetMap extracts](https://download.geofabrik.de/) — free, by region

---

## Weeks 7-10 — Python Weeks

The Python notebooks are designed to work **out of the box** with no manual data downloads. Each notebook includes sample data that loads automatically.

### Week 7 — Hello GIS

**No download needed.** The notebook:
- Creates sample Australian cities data programmatically
- Downloads Natural Earth boundaries from a URL automatically

Just run the cells!

---

### Week 8 — Vector Workflows

**No download needed.** The notebook automatically downloads:
- **NYC Neighbourhood Tabulation Areas** (polygon boundaries)
- **NYC 311 Service Requests** (point data — complaints/reports from residents)

This sample data demonstrates the same spatial join workflow you'd use with Australian data.

#### Want to use your own data instead?

Place these files in `week08/data/raw/` and the notebook will detect and use them:

| File | Description |
|------|-------------|
| `neighbourhoods.geojson` | Polygon boundaries (SA2s, suburbs, etc.) |
| `incidents.geojson` | Point locations (crimes, facilities, etc.) |

**To export from QGIS:**
1. Right-click the layer > **Export** > **Save Features As...**
2. Format: **GeoJSON**
3. CRS: **EPSG:4326** (WGS 84)
4. Save to `week08/data/raw/`

---

### Week 9 — Raster & Remote Sensing

**No download needed.** The notebook generates realistic synthetic satellite data that simulates:
- A "before" image with healthy vegetation
- An "after" image showing vegetation clearing
- Analysis zones for zonal statistics

This teaches NDVI calculation and change detection without downloading 800MB satellite files.

#### Want to use real satellite imagery?

Place these files in `week09/data/raw/` and the notebook will use them:

| File | Description |
|------|-------------|
| `sentinel_before.tif` | Multi-band satellite image (earlier date) |
| `sentinel_after.tif` | Multi-band satellite image (later date) |
| `aoi.geojson` | Your study area boundary (optional) |
| `zones.geojson` | Areas for zonal statistics (optional) |

**Downloading Sentinel-2 from Copernicus:**

This is a multi-step process. Only attempt this after completing the notebook with sample data.

**Step 1: Create a free account**

1. Go to [Copernicus Browser](https://browser.dataspace.copernicus.eu/)
2. Click **Login** → **Register**
3. Verify your email

**Step 2: Find your study area**

1. Navigate the map to your area of interest
2. Click the **Draw** tool (polygon icon) in the left panel
3. Draw a rectangle around your study area
4. **Keep it small** — 10km × 10km is plenty for learning

**Step 3: Filter images**

1. In the left panel, select **Sentinel-2** → **Sentinel-2 L2A** (atmospherically corrected)
2. Set **Time range** — you need TWO dates, 3-6 months apart
3. Set **Cloud cover** maximum to **10%**
4. Click **Search**

**Step 4: Preview and download**

1. Click results to preview — look for low clouds over your specific area
2. Click the **Download** icon on a good image
3. Choose **Full product** (downloads all bands)
4. Repeat for a second date

**Step 5: Extract and find the bands**

Downloaded files are large ZIPs (~800MB). Inside:

```
S2A_MSIL2A_.../
└── GRANULE/
    └── L2A_.../
        └── IMG_DATA/
            └── R10m/
                ├── *_B04_10m.jp2   ← Red band (you need this)
                └── *_B08_10m.jp2   ← NIR band (and this)
```

**Step 6: Create multi-band GeoTIFF in QGIS**

1. **Raster → Miscellaneous → Merge**
2. Add B04 and B08 as input layers
3. Check "Place each input file into a separate band"
4. Save as `sentinel_before.tif`
5. Repeat for the "after" date

!!! warning "Satellite imagery is complex"
    Real satellite data requires understanding of bands, resolutions, and atmospheric correction. Master the sample data workflow first before attempting real downloads.

---

### Week 10 — Transport Networks

**No download needed.** The notebook downloads street network data directly from OpenStreetMap using the OSMnx library.

Just specify a location (latitude/longitude) and radius, and the network downloads automatically.

#### Optional: Custom facility locations

To analyze accessibility from specific locations (hospitals, schools, etc.), create a `facilities.geojson` file with point geometries and place it in `week10/data/raw/`.

---

## Colab vs Local: Where do files go?

| If you're using... | Put files in... |
|--------------------|-----------------|
| **Google Colab** | Google Drive: `My Drive/intro-gis/week##/data/raw/` |
| **Local Jupyter** | Your computer: `intro-gis/week##/data/raw/` |

The notebooks detect which environment you're in and adjust paths automatically.

### Uploading to Google Drive (for Colab users)

1. Open [Google Drive](https://drive.google.com)
2. Navigate to `My Drive/intro-gis/week##/data/raw/`
3. Drag and drop your files, or click **+ New** > **File upload**

---

## Checklist

Use the [Data Download Checklist](../reference/data-download-checklist.md) to track your downloads week by week.

---

## Troubleshooting

### "File not found" errors in notebooks

1. Check the file is in the correct folder (`data/raw/`)
2. Check the filename matches exactly (case-sensitive!)
3. For Colab: Make sure you ran the "mount drive" cell first

### "Layer has no CRS" in QGIS

The data source didn't include coordinate system info. When prompted:
1. For Australian data: choose **EPSG:7844** (GDA2020) or **EPSG:4283** (GDA94)
2. For global data: choose **EPSG:4326** (WGS 84)

### Download links don't work

Data portals change URLs frequently. If a link is broken:
1. Go to the portal's homepage
2. Use the search function
3. Let us know so we can update the guide!

---

**Next step (Week 7+):** [4. Python setup](04-python-setup.md)
