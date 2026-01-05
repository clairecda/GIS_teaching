# Week 9 Lecture · Raster & Remote Sensing in Python

## This week
You'll explore satellite imagery analysis in Python, working with Landsat and Sentinel data to calculate vegetation indices, detect change over time, and link raster patterns to vector boundaries using zonal statistics.

## By the end of the week you will
- Access and process multi-band satellite imagery (Landsat, Sentinel) using rasterio and rioxarray in Python.
- Calculate spectral indices (NDVI, NDWI, NDBI) to measure vegetation health, water presence, and built environment.
- Perform change detection by comparing imagery from different time periods and quantifying landscape transformations.
- Apply zonal statistics to summarize raster values by administrative boundaries and communicate spatial patterns effectively.

## Key vocabulary
Remote sensing · spectral bands · spatial resolution · temporal resolution · NDVI · NIR (near-infrared) · Landsat · Sentinel-2 · change detection · rasterio · rioxarray · zonal statistics · cloud masking · atmospheric correction · multispectral imagery · false color composite.

## Seeing from above

Satellite imagery offers a powerful perspective—but "seeing everything" doesn't mean understanding everything. Remote sensing carries its own assumptions about what matters, who's watching, and whose view counts.

**The view from nowhere?**

- Satellites orbit according to physics, but what they photograph reflects priorities. Commercial satellites offer higher resolution—for those who can pay
- Landsat and Sentinel are public goods, but their revisit cycles, band selections, and coverage gaps still embed choices
- The "god's eye view" flattens local knowledge. A pixel classified as "bare soil" might be fallow farmland, sacred ground, or recently cleared forest—the spectral signature doesn't distinguish

**Change detection and the question of change:**

- Algorithms detect spectral change, not meaning. A "loss of vegetation" could be deforestation, seasonal dormancy, or a controlled burn for land management
- Baseline matters: change from when? Colonial-era land cover? Pre-industrial? Last year?
- Whose definition of "degradation" or "improvement" is encoded in the classification scheme?

**Surveillance and consent:**

- The same imagery that monitors deforestation can track indigenous land use, refugee movements, or informal settlements
- Communities being observed rarely control how imagery of their land is collected, analyzed, or shared
- "Open data" in remote sensing means open to anyone with technical capacity—not equal access

**Questions to carry forward:**

- What would people on the ground say about how their landscape is being classified?
- Whose priorities determined what counts as "change" worth detecting?
- How do we acknowledge what satellites can't see—social relationships, tenure arrangements, sacred significance?

## What happens in class
- Discuss remote sensing platforms and the trade-offs between spatial, temporal, and spectral resolution for different applications.
- Compare pre- and post-event satellite imagery to identify landscape changes and discuss potential sources of false positives (seasonality, sensor differences, cloud shadows).
- Calculate NDVI from multi-band imagery and interpret the results in the context of vegetation health and land cover.
- Apply zonal statistics to link raster-based change detection with administrative boundaries from Week 3.
- Debate how to communicate change: raw index differences, percentage change, or categorical classification for different audiences.

## Prepare beforehand
- Review Week 4 raster concepts (DEM, hillshade, clipping) to refresh your understanding of raster data structures.
- Review the [Raster Data Basics](../readings/week04-raster-basics.md) reading from Week 4.
- Install required Python packages: `rasterio`, `rioxarray`, `earthpy`, `geopandas` via your course environment.
- Download sample Landsat or Sentinel-2 scenes for your study area via [Downloading datasets](../onboarding/03-download-data.md) and check Week 9 in the [data checklist](../reference/data-download-checklist.md).
- Bring a question about a landscape change event in your region (fire, flood, deforestation, urban expansion) that satellite imagery could help measure.

## Connected lab
This week's lab notebook guides you through the full remote sensing workflow: loading multi-band imagery, clipping to your area of interest, computing NDVI and other indices, detecting change between two time periods, and using zonal statistics to report change by administrative boundaries.

