# Week 9 Lecture · Remote Sensing & Change Detection

## Objectives

- Introduce remote sensing fundamentals (spectral bands, temporal revisits, resolutions).
- Discuss common indices (NDVI, NDBI, NDWI) and when to use them.
- Explain workflows for change detection between pre- and post-event imagery.

## Outline

1. **Remote sensing basics**  
   - Platforms (Sentinel-2, Landsat 8/9, Planet).  
   - Spatial, temporal, spectral resolution trade-offs.  
   - Preprocessing considerations (cloud masking, atmospheric correction).
2. **Vegetation & built environment indices**  
   - NDVI formula: `(NIR - Red) / (NIR + Red)`; interpret scale.  
   - NDWI, NDBI, and other indices relevant to urban/environmental analysis.
3. **Change detection techniques**  
   - Simple differencing (NDVI_before - NDVI_after).  
   - Thresholding and classification.  
   - Limitations (seasonality, sensor differences).
4. **Zonal statistics & reporting**  
   - Summarise change by administrative boundaries (ties back to Week 3).  
   - Communicate uncertainty and limitations.

## Recommended readings

- ESA Sentinel-2 User Guide.  
- USGS remote sensing tutorials.  
- Articles on change detection best practices (e.g., NASA Earthdata).

## Classroom activities

- Compare two images (pre/post event) and identify potential false positives.  
- Debate whether change should be presented in raw index difference, percentage, or classification.

## Link to lab

- Prepares learners for the Week 9 notebook steps: clipping rasters, computing change arrays, and summarising by zones.
