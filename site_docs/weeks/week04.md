# Week 4 · Raster & Terrain Analysis

Moving from crisp vector boundaries to continuous surfaces opens up new analytical possibilities. This week, you'll work with elevation data to understand the physical landscape, create terrain visualizations, and explore how topography intersects with the social and administrative boundaries you mapped in Week 3. Terrain analysis is fundamental to planning for floods, infrastructure, agriculture, and environmental conservation.

## What you'll learn

By the end of this week, you'll be able to:

1. Explain the difference between elevation rasters, derived surfaces, and spectral indices like NDVI.
2. Import DEM tiles (ELVIS or SRTM), clip them to an area of interest, and generate terrain products (hillshade, slope).
3. Calculate NDVI (vegetation index) from satellite imagery using the Raster Calculator.
4. Combine raster outputs with boundary data to support environmental resilience and planning questions.

## Before you start

- [ ] Download elevation data (ELVIS for Australia or SRTM tile) per [Downloading datasets](../onboarding/03-download-data.md) and tick off Week 4 in the [checklist](../reference/data-download-checklist.md)
- [ ] Download satellite imagery for NDVI (Sentinel-2 or Landsat) — see Activity 6 for sources
- [ ] Review [Raster Data Basics](../readings/week04-raster-basics.md) and the theory lecture on [Elevation & Surface Modelling](../lectures/week04-raster-theory.md)
- [ ] Ensure the Week 3 boundary and indicator layers load correctly—you'll clip rasters using these polygons
- [ ] Install optional plugins if advised (e.g., **Profile Tool**, **Raster terrain analysis**)

## This week's activities

### Activity 1: Load and inspect your DEM

Before you can analyze terrain, you need to understand what your elevation data represents and make sure it's in the right coordinate system.

**Steps:**

1. Load your DEM tile (ELVIS or SRTM) into QGIS using `Layer ▶ Add Layer ▶ Add Raster Layer...`
2. Inspect the layer properties:
   - Right-click layer → **Properties** → **Information** tab
   - Note the CRS (often WGS84/EPSG:4326 for SRTM)
   - Check resolution (pixel size) and vertical units (usually meters)
   - Verify the elevation range makes sense for your region
3. If you're working with multiple tiles, mosaic them first:
   - `Raster ▶ Miscellaneous ▶ Merge`
   - Select all your DEM tiles
   - Save output to `data/processed/week04/dem_mosaic.tif`

!!! tip "Understanding your data"
    SRTM typically has 30m or 90m resolution globally. ELVIS provides much higher resolution for Australia (often 5m). Higher resolution means more detail but larger file sizes and slower processing.

### Activity 2: Reproject to a suitable CRS

Most DEMs come in geographic coordinates (latitude/longitude), but terrain analysis works better in projected coordinates where distance measurements are accurate.

**Steps:**

1. Check your current CRS in the bottom-right corner of QGIS
2. Reproject your DEM to match your study area:
   - `Raster ▶ Projections ▶ Warp (Reproject)`
   - **Input layer:** your DEM
   - **Target CRS:** choose a projected CRS suitable for your region (e.g., EPSG:7856 for Australia, EPSG:32633 for Europe)
   - **Resampling method:** Bilinear (smooths elevation values)
   - **Output:** save to `data/processed/week04/dem_projected.tif`
3. Load the reprojected DEM and verify it looks correct

!!! note "Why reproject?"
    Geographic coordinates (degrees) don't represent equal distances across the map. A projected CRS uses meters or feet, making slope and distance calculations accurate.

### Activity 3: Clip to your area of interest

Working with full DEM tiles can be slow. You'll clip to just your study area using the boundary polygons from Week 3.

**Steps:**

1. Open your Week 3 project and identify your SA2 or LGA boundary layer
2. Clip the DEM using your boundary:
   - `Raster ▶ Extraction ▶ Clip Raster by Mask Layer`
   - **Input layer:** dem_projected.tif
   - **Mask layer:** your SA2 or LGA polygons from Week 3
   - **Match the extent of the clipped raster to the extent of the mask layer:** check this option
   - **Output:** save to `data/processed/week04/dem_clipped.tif`
3. Remove the full DEM layers and work with just the clipped version from now on
4. Style the clipped DEM using a terrain color ramp:
   - Layer Properties → **Symbology** → **Singleband pseudocolor**
   - Choose a green-to-brown-to-white palette that suggests elevation

**Document your work:** Update your `resources/docs/data-inventory.md` with DEM source, tile names, CRS, and processing steps.

### Activity 4: Generate a hillshade

Hillshade simulates how light and shadow would fall across terrain, making elevation patterns easier to see. It's essential for visualization and often used as a basemap.

**Steps:**

1. Generate the hillshade:
   - `Raster ▶ Analysis ▶ Hillshade`
   - **Elevation layer:** dem_clipped.tif
   - **Azimuth (horizontal angle):** 315 degrees (northwest, the default)
   - **Vertical angle:** 45 degrees (creates balanced shadows)
   - **Output:** save to `data/processed/week04/hillshade.tif`
2. Style the hillshade:
   - Layer Properties → **Symbology** → **Singleband gray**
   - Drag the white value slider slightly left to darken shadows
3. Layer it with your boundaries:
   - Move hillshade below your boundary layers in the Layers Panel
   - Set hillshade transparency to 0% (solid)
   - Set boundary layers to have transparent fills with visible outlines

!!! tip "Experiment with lighting"
    Try different azimuth values (0-360 degrees) to simulate light from different directions. Morning light (azimuth ~90) or evening light (azimuth ~270) can reveal different features. Some cartographers create multiple hillshades and blend them for more balanced terrain visualization.

### Activity 5: Calculate slope

Slope shows how steep the terrain is—critical for understanding flood risk, landslide potential, accessibility, and development suitability.

**Steps:**

1. Generate slope:
   - `Raster ▶ Terrain Analysis ▶ Slope`
   - **Elevation layer:** dem_clipped.tif
   - **Slope expressed as:** Percent (alternatively choose Degrees)
   - **Output:** save to `data/processed/week04/slope.tif`
2. Style the slope layer:
   - Layer Properties → **Symbology** → **Singleband pseudocolor**
   - Use a yellow-to-red color ramp (yellow = flat, red = steep)
   - **Min:** 0%, **Max:** adjust based on your terrain (30-50% is reasonable for many areas)
3. Adjust transparency (50-70%) and overlay with your boundary outlines
4. Identify the steepest areas—do they align with any particular boundaries or land uses?

**Optional:** Create contour lines (`Raster ▶ Extraction ▶ Contour`) with an interval appropriate for your study area (e.g., 10m for hilly terrain, 50m for mountainous areas).

### Activity 6: Calculate NDVI (vegetation index)

NDVI (Normalized Difference Vegetation Index) measures vegetation health using satellite imagery. Healthy plants absorb red light for photosynthesis but strongly reflect near-infrared (NIR) light. NDVI exploits this difference.

**The NDVI formula:**

```
NDVI = (NIR - Red) / (NIR + Red)
```

**Interpreting NDVI values:**

| NDVI Range | What it represents |
|------------|-------------------|
| 0.6 to 1.0 | Dense, healthy vegetation (forests, crops at peak) |
| 0.3 to 0.6 | Moderate vegetation (shrubs, grassland) |
| 0.1 to 0.3 | Sparse or stressed vegetation |
| -0.1 to 0.1 | Bare soil, rock, urban areas |
| -1.0 to -0.1 | Water, snow, clouds |

**Before you start:**

You need multispectral satellite imagery with separate Red and NIR bands. Options:

- **Sentinel-2**: Free from [Copernicus Open Access Hub](https://scihub.copernicus.eu/) — Band 4 = Red, Band 8 = NIR
- **Landsat 8/9**: Free from [USGS EarthExplorer](https://earthexplorer.usgs.gov/) — Band 4 = Red, Band 5 = NIR
- **Sample data**: Your instructor may provide pre-downloaded imagery

**Steps:**

1. Load your satellite imagery bands:
   - `Layer ▶ Add Layer ▶ Add Raster Layer...`
   - Add both the Red band and NIR band files
   - Note which band is which (check the filename or metadata)

2. Open the Raster Calculator:
   - `Raster ▶ Raster Calculator...`

3. Enter the NDVI formula:
   - In the **Raster Calculator Expression** box, type:
   ```
   ("NIR_band@1" - "Red_band@1") / ("NIR_band@1" + "Red_band@1")
   ```
   - Replace `NIR_band` and `Red_band` with your actual layer names
   - For Sentinel-2, this might look like:
   ```
   ("T55HBU_B08@1" - "T55HBU_B04@1") / ("T55HBU_B08@1" + "T55HBU_B04@1")
   ```

4. Set output options:
   - **Output layer:** save to `data/processed/week04/ndvi.tif`
   - **Output format:** GeoTIFF
   - Click **OK** to run

5. Style the NDVI layer:
   - Right-click the NDVI layer → **Properties** → **Symbology**
   - Change to **Singleband pseudocolor**
   - Set **Min:** -0.2, **Max:** 0.8 (or use **Min/Max Value Settings** → **Cumulative count cut**)
   - Choose the **RdYlGn** (Red-Yellow-Green) color ramp
   - Click **Classify** → **Apply** → **OK**

6. Interpret the result:
   - Green areas = healthy vegetation
   - Yellow areas = moderate/stressed vegetation
   - Red/brown areas = bare soil, urban, or water
   - Compare to satellite imagery—do the patterns make sense?

!!! tip "Common NDVI issues"
    - **All values near zero?** Check you're using the right bands (Red vs NIR)
    - **Values outside -1 to 1?** Your imagery may need atmospheric correction, or there are nodata values
    - **Striped patterns?** Could be sensor artifacts or cloud shadows

**Why this matters:**

NDVI is foundational for environmental analysis:

- **Agriculture:** Monitor crop health and predict yields
- **Urban planning:** Map green space and urban heat islands
- **Conservation:** Track deforestation and habitat change
- **Disaster response:** Assess vegetation damage from fires or floods

In Week 9, you'll automate this process in Python and compare NDVI across time to detect change.

### Activity 7: Combine terrain with boundaries

Now you'll bring together terrain analysis with the socio-economic data from Week 3 to tell a more complete story.

**Steps:**

1. Calculate zonal statistics to summarize terrain by boundary:
   - `Processing ▶ Toolbox ▶ Zonal Statistics`
   - **Raster layer:** slope.tif
   - **Vector layer:** your SA2 or LGA boundaries
   - **Statistics to calculate:** Mean, Maximum, Median
   - **Output column prefix:** "slope_"
   - Click Run
2. The boundary layer now has new fields showing average slope, max slope, etc.
3. Open the attribute table and sort by "slope_mean" to identify which areas have the steepest terrain
4. Create a map showing slope combined with SEIFA or another indicator from Week 3:
   - Are disadvantaged areas more likely to be on steep terrain?
   - How might terrain affect accessibility to services?
   - Which boundaries face combined challenges (steep terrain + low socio-economic status)?

**Optional:** Calculate zonal statistics for elevation to find mean height, elevation range, or lowest/highest points per boundary.

### Activity 8: Create a terrain visualization layout

Pull everything together into a professional map showing terrain context for your study area.

**Steps:**

1. Create a new Print Layout: `Project ▶ New Print Layout...` → name it "Terrain Analysis"
2. Add your main map showing:
   - Hillshade as the base
   - Slope or elevation as a semi-transparent overlay
   - Boundary outlines
   - Optional: contour lines if you created them
3. Add a second map frame showing zonal statistics (boundaries colored by mean slope)
4. Add map elements:
   - Title: "Terrain Analysis for [Your Region]"
   - Legend (simplify to show only essential layers)
   - Scale bar
   - North arrow
   - Data credits: "Elevation data: ELVIS/SRTM | Boundaries: ABS/[source] | Map: [Your Name], 2024"
5. Export to `exports/week04_terrain_analysis.pdf` and `exports/week04_terrain_analysis.png`

!!! note "Telling the terrain story"
    Your map should help viewers understand both the physical landscape (what the terrain looks like) and the analytical insight (how terrain relates to boundaries or vulnerability). Use annotations or text boxes to highlight key findings.

## Troubleshooting

### DEM appears as solid gray or black
- **Stretch symbology:** Right-click raster → **Properties** → **Symbology** → Set Min/Max to "Cumulative count cut" (2-98%)
- **NoData values:** Large NoData values (-9999) may skew the display. Set NoData color to transparent in Symbology
- **Single value:** Check raster statistics—the file may be corrupted or empty

### Hillshade is too dark or washed out
- **Adjust Z-factor:** For data in degrees (geographic CRS), use Z-factor of 0.00001. For meters, use 1
- **Change altitude:** Lower sun altitude (e.g., 35°) creates more dramatic shadows; higher (e.g., 60°) is softer
- **Blend modes:** In Layer Properties → Symbology, try "Multiply" blending with the DEM underneath

### Slope values seem wrong
- **CRS issue:** Slope calculation requires projected CRS (meters). Reproject the DEM first: `Raster ▶ Projections ▶ Warp (Reproject)`
- **Units:** QGIS outputs slope in degrees by default. For percent, check the tool options
- **Flat areas:** Very flat terrain (deltas, plains) will show near-zero slope everywhere—this may be correct

### Raster processing is extremely slow
- **File too large:** Clip to study area first: `Raster ▶ Extraction ▶ Clip Raster by Mask Layer`
- **High resolution:** Resample to lower resolution for testing: `Raster ▶ Projections ▶ Warp` with larger cell size
- **Close other apps:** Raster processing is memory-intensive

### "Clip Raster" produces empty or tiny output
- **CRS mismatch:** Clip layer and raster must be in the same CRS
- **Extent issue:** Make sure the mask layer actually overlaps the raster
- **NoData handling:** Check "Create output alpha band" if edges appear clipped incorrectly

### Raster doesn't align with vector boundaries
- **Different CRS:** Reproject one layer to match the other
- **On-the-fly projection:** QGIS may display them aligned, but they're not. Check actual CRS in layer properties
- **Datum shift:** Some older data uses different datums (e.g., AGD66 vs GDA94 in Australia)

### Zonal statistics returns NULL or wrong values
- **No overlap:** Vector polygons may not overlap the raster extent
- **CRS mismatch:** Both layers must be in the same CRS
- **NoData cells:** If polygons cover mostly NoData areas, statistics will be empty
- **Raster not loaded:** Make sure the raster is added to the project, not just referenced

### Export creates huge file
- **Compression:** When exporting, use "LZW" or "DEFLATE" compression in Advanced options
- **Reduce extent:** Clip to only the area you need
- **Lower resolution:** Resample to 30m or 90m if you don't need 10m detail

## Support materials

- Slides: [Week 04 – Raster & Terrain Analysis](../slides/index.md)
- Lecture notes: [Elevation & Surface Modelling](../lectures/week04-raster-theory.md)
- Reading: [Raster Data Basics](../readings/week04-raster-basics.md)
- Dataset checklist: [Week 4 items](../reference/data-download-checklist.md)

## Reflect

Take 10-15 minutes to answer these questions in your [Week 4 reflection](../reference/reflections.md#week-4--raster--terrain):

- How does DEM resolution influence the insights you can draw? When would you need higher-resolution LiDAR?
- What patterns did you discover when overlaying terrain with boundaries? Were there any surprising relationships between elevation/slope and socio-economic data?
- Which boundary level (SA2, LGA, suburbs) felt most appropriate when communicating terrain-related risk? Why?
- What did NDVI reveal about vegetation patterns in your study area? How might you use this for environmental monitoring?
- What challenges did you encounter working with raster data compared to vectors? What did you learn about managing file sizes and processing time?
- How will you document raster sources (DEM, satellite imagery) and processing steps for reproducibility?

## What you'll submit

- [ ] QGIS project file (`projects/week04_terrain_analysis.qgz`) with clipped DEM, hillshade, slope, and NDVI layers
- [ ] Derived rasters saved in `data/processed/week04/`:
  - Hillshade (`hillshade.tif`)
  - Slope (`slope.tif`)
  - NDVI (`ndvi.tif`)
- [ ] Exported map (PDF or PNG) combining terrain output with boundary annotations
- [ ] Your Week 4 reflection entry

## Coming up next week

Week 5 moves into crime hotspot mapping using kernel density estimation and ethical considerations for sensitive data. Think about how elevation or accessibility (steep terrain, distance from roads) might intersect with crime patterns in your region. The raster analysis skills you practiced this week will carry forward into density analysis next week.
