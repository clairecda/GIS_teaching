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
