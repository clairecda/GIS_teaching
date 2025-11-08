# Week 4 Lecture · Elevation & Surface Modelling

## Objectives

- Introduce digital elevation models (DEMs), hillshade, slope, and contour derivations.
- Compare data sources (ELVIS, SRTM, LiDAR) and discuss resolution implications.
- Explain how elevation intersects with planning contexts (flood, transport, habitat).

## Outline

1. **DEM fundamentals**  
   - Raster structure, resolution, vertical accuracy, common file formats.  
   - Differences between DEM, DSM, DTM.
2. **Data sources**  
   - Australia: ELVIS, state-based LiDAR portals.  
   - Global: SRTM, NASADEM, ASTER GDEM.  
   - Licensing and access considerations.
3. **Derived products**  
   - Hillshade, slope, aspect, contour, TPI.  
   - When to use each and styling considerations.
4. **Integrating with boundaries**  
   - Zonal statistics for risk assessment (e.g., elevation vs SEIFA).  
   - Communicating uncertainty (resolution, interpolation artefacts).

## Visual aids

- DEM vs hillshade comparison.  
- Resolution comparison (30 m vs 1 m).  
- Flowchart of raster processing pipeline (raw DEM → clip → hillshade/slope → overlay).

## Further reading

- Geoscience Australia: ELVIS documentation.  
- USGS: [SRTM Overview](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-digital-elevation-shuttle-radar-topography-mission-srtm).  
- Raster analysis chapters from QGIS training manual.

## Connection to lab

- Sets context for clipping DEMs, producing hillshade, and overlaying with SA2/LGA boundaries.  
- Prepares learners for Week 5 by thinking about terrain in situational analysis.
