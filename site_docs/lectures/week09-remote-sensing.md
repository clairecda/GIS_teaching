# Week 9 · Raster & Remote Sensing in Python

Working with satellite imagery opens up powerful possibilities for monitoring environmental change, tracking vegetation health, and detecting landscape transformations over time. This week, you'll move from QGIS-based raster analysis to Python workflows using rasterio and rioxarray. You'll learn to access multi-band satellite imagery, calculate vegetation indices like NDVI, detect change between time periods, and summarize patterns using zonal statistics tied to your administrative boundaries from Week 3.

## This week

You'll explore satellite imagery analysis in Python, working with Landsat and Sentinel data to calculate vegetation indices, detect change over time, and link raster patterns to vector boundaries using zonal statistics.

## By the end of the week you will

- Access and process multi-band satellite imagery (Landsat, Sentinel) using rasterio and rioxarray in Python
- Calculate spectral indices (NDVI, NDWI, NDBI) to measure vegetation health, water presence, and built environment
- Perform change detection by comparing imagery from different time periods and quantifying landscape transformations
- Apply zonal statistics to summarize raster values by administrative boundaries and communicate spatial patterns effectively

## Key vocabulary

Remote sensing · Spectral bands · Spatial resolution · Temporal resolution · NDVI (Normalized Difference Vegetation Index) · NIR (Near-Infrared) · Landsat · Sentinel-2 · Change detection · Rasterio · Rioxarray · Zonal statistics · Cloud masking · Atmospheric correction · Multispectral imagery · False color composite

## What happens in class

- Discuss remote sensing platforms and the trade-offs between spatial, temporal, and spectral resolution for different applications
- Compare pre- and post-event satellite imagery to identify landscape changes and discuss potential sources of false positives (seasonality, sensor differences, cloud shadows)
- Calculate NDVI from multi-band imagery and interpret the results in the context of vegetation health and land cover
- Apply zonal statistics to link raster-based change detection with administrative boundaries from Week 3
- Debate how to communicate change: raw index differences, percentage change, or categorical classification for different audiences

## Prepare beforehand

- Review Week 4 raster concepts (DEM, hillshade, clipping) to refresh your understanding of raster data structures
- Read the remote sensing foundations primer: [Understanding Spectral Bands & Resolution](../readings/week09-remote-sensing-basics.md) (if available)
- Install required Python packages: `rasterio`, `rioxarray`, `earthpy`, `geopandas` via your course environment
- Download sample Landsat or Sentinel-2 scenes for your study area via [Downloading datasets](../onboarding/data-downloads.md) and check Week 9 in the [data checklist](../reference/data-download-checklist.md)
- Bring a question about a landscape change event in your region (fire, flood, deforestation, urban expansion) that satellite imagery could help measure

## Connected lab

This week's lab notebook guides you through the full remote sensing workflow: loading multi-band imagery, clipping to your area of interest, computing NDVI and other indices, detecting change between two time periods, and using zonal statistics to report change by administrative boundaries.

## Further Reading

**Essential:**

- [Rasterio Documentation](https://rasterio.readthedocs.io/) - Official guide to reading, writing, and processing geospatial raster data in Python with comprehensive examples
- [Rioxarray User Guide](https://corteva.github.io/rioxarray/stable/) - Extends xarray with geospatial raster capabilities, ideal for working with multi-dimensional satellite imagery
- [USGS Landsat Missions](https://www.usgs.gov/landsat-missions) - Comprehensive resource on Landsat satellite missions, band descriptions, data access, and processing levels
- [ESA Sentinel-2 User Handbook](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-2-msi) - Official guide to Sentinel-2 spectral bands, resolution specifications, and data products

**Optional but recommended:**

- [EarthPy Documentation](https://earthpy.readthedocs.io/) - Python package for plotting and working with spatial raster and vector data, particularly useful for multi-band imagery visualization
- [Google Earth Engine Guides](https://developers.google.com/earth-engine/guides) - Cloud-based platform for planetary-scale geospatial analysis, useful for understanding large-scale remote sensing workflows even if not using GEE directly
- [NDVI: Foundation for Remote Sensing Phenology (USGS)](https://www.usgs.gov/special-topics/remote-sensing-phenology/science/ndvi-foundation-remote-sensing-phenology) - Explains the theory, applications, and interpretation of NDVI for vegetation monitoring

**Videos:**

- [Satellite Imagery Analysis in Python with Rasterio](https://www.youtube.com/results?search_query=rasterio+python+tutorial) (various tutorials, 15-30 min) - Search for recent tutorials demonstrating multi-band satellite imagery processing workflows
- [Introduction to Remote Sensing: Spectral Signatures](https://www.youtube.com/results?search_query=spectral+signatures+remote+sensing) (10-15 min) - Explains how different surfaces reflect electromagnetic radiation and how we use this to classify land cover
