# Week 4 Lecture · Elevation & Surface Modelling

## This week
We move from vector-focused analysis to working with raster surfaces. Learners explore digital elevation models (DEMs), generate terrain derivatives, and understand how these layers interact with administrative boundaries for planning and resilience work.

## By the end of the week you will
- Describe what DEM/DSM/DTM products represent and when to use each.
- Compare common elevation data sources (ELVIS, SRTM, LiDAR) and discuss the trade-offs in resolution, accuracy, and coverage.
- Produce hillshade, slope, and other terrain derivatives and explain how they support decision-making.
- Integrate raster outputs with boundary data (SA2/LGA) to quantify risk or accessibility.

## Key vocabulary
DEM · DSM · DTM · resolution · vertical accuracy · hillshade · slope · aspect · contour · zonal statistics · resampling.

## What happens in class
- Review DEM fundamentals, highlighting raster structure, cell size, and metadata (vertical units, datum).
- Compare Australian (ELVIS, state LiDAR) and global (SRTM, NASADEM) elevation datasets, noting access restrictions and licensing.
- Demonstrate deriving hillshade, slope, and contours in QGIS; discuss styling tips to emphasise terrain.
- Show how to clip DEMs to an area of interest and run zonal statistics to summarise elevation against socio-economic boundaries.
- Discuss uncertainty: resolution limitations, interpolation artefacts, and how to communicate them in outputs.

## Prepare beforehand
- Download the ELVIS or SRTM tiles listed in the [data download guide](../onboarding/data-downloads.md) and tick off Week 4 in the checklist.
- Skim the [Week 04 lecture slides](../assets/slides/week04.html) and read relevant sections of the QGIS training manual on raster analysis.
- Ensure the boundary join outputs from Week 3 are available; they will be used to clip and summarise rasters.

## Connected lab
The [Week 4 lab](../weeks/week04.md) guides learners through clipping DEMs, creating hillshade/slope products, and overlaying results with SA2/LGA boundaries for interpretation.

## Further Reading

**Essential:**
- [QGIS Raster Analysis Tutorial](https://docs.qgis.org/3.34/en/docs/training_manual/rasters/index.html) - Official QGIS documentation on working with raster data, terrain analysis, and surface modelling
- [ELVIS - Elevation Information System](https://elevation.fsdf.org.au/) - Australian national elevation data portal with DEMs, DSMs, and LiDAR products
- [SRTM Data - USGS](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-digital-elevation-shuttle-radar-topography-mission-srtm-1) - Global elevation data at 30m and 90m resolution with documentation
- [Understanding DEMs - GIS Geography](https://gisgeography.com/dem-dsm-dtm-differences/) - Clear explanation of DEM vs DSM vs DTM and when to use each

**Optional but recommended:**
- [Terrain Analysis in QGIS](https://docs.qgis.org/3.34/en/docs/user_manual/processing_algs/qgis/rasterterrain.html) - Documentation on hillshade, slope, aspect, and other terrain derivatives
- [Zonal Statistics Tutorial](https://www.qgistutorials.com/en/docs/3/raster_zonal_stats.html) - Step-by-step guide to summarising raster values by polygon boundaries
- [LiDAR Data Basics - NOAA](https://coast.noaa.gov/digitalcoast/data/home.html) - Introduction to LiDAR technology and applications