# Week 9 · Flood Risk Assessment in Python

## Research Question

> **"Which areas in the Hawkesbury-Nepean region are at elevated flood risk based on terrain characteristics?"**

This week, you'll automate the flood risk assessment you performed manually in QGIS during Week 4. By writing code to replicate the workflow, you'll understand how professionals process terrain data at scale and build reproducible analysis pipelines.

The Hawkesbury-Nepean region west of Sydney experienced devastating floods in 2022. While professional flood modelling uses complex hydrological simulations, terrain analysis provides a first approximation of flood-prone areas based on elevation and slope.

## What you'll learn

By the end of this week, you'll be able to:

1. Access cloud-hosted elevation data using the Planetary Computer STAC API—no manual downloads required.
2. Calculate terrain derivatives (slope, aspect, hillshade) using NumPy and rasterio.
3. Build a weighted flood risk index combining multiple terrain factors.
4. Apply zonal statistics to summarize risk by administrative boundary (SA2).
5. Create publication-ready visualizations and export analysis results.

## Before you start

### 1. Get the notebook

| Option | Link |
|--------|------|
| **Run in Colab** (Recommended) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/clairecda/GIS_teaching/blob/main/notebooks/week09_raster_remote_sensing.ipynb) |
| View on GitHub | [week09_raster_remote_sensing.ipynb](https://github.com/clairecda/GIS_teaching/blob/main/notebooks/week09_raster_remote_sensing.ipynb) |
| Download | [Right-click → Save As](https://raw.githubusercontent.com/clairecda/GIS_teaching/main/notebooks/week09_raster_remote_sensing.ipynb) |

**Using Colab?** Run this cell first to install GIS packages:
```python
!pip install geopandas rasterio rioxarray pystac-client planetary-computer rasterstats contextily folium -q
```

### 2. Confirm your environment works

=== "Google Colab"
    - Run the pip install cell above
    - If you see `Successfully installed...`, you're ready!

=== "Local (Anaconda)"
    - Activate your conda environment: `conda activate intro-gis`
    - Check imports: `python -c "import rioxarray; print('✅ Ready!')"`
    - If you see errors, review [Python Setup Guide](../onboarding/04-python-setup.md)

### 3. No manual download needed!

Unlike previous weeks, you don't need to download any data manually. The notebook:

- Fetches elevation data from [Planetary Computer's Copernicus DEM](https://planetarycomputer.microsoft.com/dataset/cop-dem-glo-30)
- Downloads SA2 boundaries from the ABS automatically
- Creates all derived layers programmatically

If the API is unavailable, the notebook falls back to synthetic terrain data so you can still complete the workflow.

### 4. Review the lecture

- [ ] Read: [Week 9 · Elevation & Surface Modelling](../lectures/week09-remote-sensing.md)
- [ ] Review: [Week 4 · QGIS Flood Risk Assessment](week04.md) (this week automates that workflow)

!!! tip "Week 4 ↔ Week 9 connection"
    In Week 4, you performed this analysis manually in QGIS. This week, you'll write code to do the same thing—but now you can process multiple study areas, adjust parameters programmatically, and create reproducible workflows.

## This week's activities

### Activity 1: Connect to cloud-hosted elevation data

Instead of downloading large DEM files, you'll access elevation data directly from the cloud using the Planetary Computer STAC API.

**Key concepts:**

- **STAC** (SpatioTemporal Asset Catalog): A standard for organizing geospatial data in the cloud
- **COG** (Cloud Optimized GeoTIFF): Rasters stored so you can read just the portion you need
- **rioxarray**: Library that combines rasterio with xarray for convenient raster manipulation

**Steps:**

1. Import libraries and connect to Planetary Computer:
   ```python
   import pystac_client
   import planetary_computer
   import rioxarray

   catalog = pystac_client.Client.open(
       "https://planetarycomputer.microsoft.com/api/stac/v1",
       modifier=planetary_computer.sign_inplace
   )
   ```

2. Define your study area (Hawkesbury-Nepean floodplain):
   ```python
   # Bounding box: [west, south, east, north]
   bbox = [150.65, -33.65, 150.85, -33.45]  # ~20km × 20km area
   ```

3. Search for Copernicus DEM tiles:
   ```python
   search = catalog.search(
       collections=["cop-dem-glo-30"],
       bbox=bbox
   )
   items = list(search.items())
   print(f"Found {len(items)} DEM tiles")
   ```

4. Read elevation data for your study area:
   ```python
   dem_url = items[0].assets["data"].href
   dem = rioxarray.open_rasterio(dem_url).squeeze()
   dem = dem.rio.clip_box(*bbox)
   ```

**QGIS ↔ Python comparison:**

| QGIS (Week 4) | Python (This week) |
|---------------|--------------------|
| Download from ELVIS portal | Fetch from Planetary Computer API |
| Manual file management | Programmatic access |
| One study area at a time | Script any bounding box |

!!! note "Why cloud-hosted data?"
    Traditional workflow: Download 500MB DEM → Extract → Load → Clip to study area.
    Cloud workflow: Read only the 5MB covering your study area directly from the server.
    For large-scale analysis (e.g., national flood mapping), this saves days of data preparation.

### Activity 2: Calculate terrain derivatives

Terrain derivatives like slope and aspect help identify flood-prone areas. You'll implement the same calculations QGIS performs internally.

**Steps:**

1. Calculate slope using NumPy gradient:
   ```python
   import numpy as np

   # Get elevation as numpy array
   elev = dem.values
   res = dem.rio.resolution()[0]  # Pixel size in meters

   # Calculate gradients
   dy, dx = np.gradient(elev, res)
   slope_rad = np.arctan(np.sqrt(dx**2 + dy**2))
   slope_deg = np.degrees(slope_rad)
   ```

2. Calculate aspect (direction of steepest descent):
   ```python
   aspect_rad = np.arctan2(-dx, dy)
   aspect_deg = np.degrees(aspect_rad) % 360
   ```

3. Calculate hillshade for visualization:
   ```python
   azimuth = np.radians(315)  # Light from northwest
   altitude = np.radians(45)  # Sun angle

   hillshade = (
       np.cos(altitude) * np.cos(slope_rad) +
       np.sin(altitude) * np.sin(slope_rad) *
       np.cos(azimuth - aspect_rad)
   )
   ```

4. Visualize your terrain analysis:
   ```python
   fig, axes = plt.subplots(2, 2, figsize=(14, 12))

   axes[0, 0].imshow(elev, cmap='terrain')
   axes[0, 0].set_title('Elevation (m)')

   axes[0, 1].imshow(slope_deg, cmap='YlOrRd', vmax=30)
   axes[0, 1].set_title('Slope (degrees)')

   axes[1, 0].imshow(aspect_deg, cmap='twilight')
   axes[1, 0].set_title('Aspect (degrees)')

   axes[1, 1].imshow(hillshade, cmap='gray')
   axes[1, 1].set_title('Hillshade')

   plt.tight_layout()
   plt.show()
   ```

**QGIS ↔ Python comparison:**

| QGIS (Week 4) | Python (This week) |
|---------------|--------------------|
| Raster > Analysis > Slope | `np.gradient()` + `np.arctan()` |
| Raster > Analysis > Hillshade | Custom formula with azimuth/altitude |
| Visual styling in Layer Properties | `matplotlib` colormaps |

### Activity 3: Build flood risk classification

Now you'll combine elevation and slope into a composite flood risk index—the same approach you used in Week 4's Raster Calculator.

**Flood risk logic:**

- **Low elevation** = higher risk (water accumulates)
- **Flat slope** = higher risk (poor drainage)

**Steps:**

1. Normalize elevation to 0-1 (inverted so low = high score):
   ```python
   elev_min, elev_max = np.nanmin(elev), np.nanmax(elev)
   elev_score = 1 - (elev - elev_min) / (elev_max - elev_min)
   ```

2. Normalize slope to 0-1 (inverted so flat = high score):
   ```python
   slope_score = 1 - np.clip(slope_deg / 15, 0, 1)
   ```

3. Combine with weights (elevation 60%, slope 40%):
   ```python
   risk_index = 0.6 * elev_score + 0.4 * slope_score
   ```

4. Classify into risk zones:
   ```python
   risk_classes = np.zeros_like(risk_index)
   risk_classes[risk_index < 0.3] = 1   # Low risk
   risk_classes[(risk_index >= 0.3) & (risk_index < 0.5)] = 2  # Moderate
   risk_classes[(risk_index >= 0.5) & (risk_index < 0.7)] = 3  # High
   risk_classes[risk_index >= 0.7] = 4  # Very high risk
   ```

5. Visualize risk classification:
   ```python
   from matplotlib.colors import ListedColormap

   colors = ['#2ecc71', '#f1c40f', '#e67e22', '#e74c3c']  # Green to Red
   cmap = ListedColormap(colors)

   plt.figure(figsize=(12, 10))
   plt.imshow(risk_classes, cmap=cmap, vmin=1, vmax=4)
   plt.colorbar(ticks=[1, 2, 3, 4], label='Risk Level')
   plt.title('Flood Risk Classification\nHawkesbury-Nepean Region')
   plt.show()
   ```

**QGIS ↔ Python comparison:**

| QGIS (Week 4) | Python (This week) |
|---------------|--------------------|
| Multiple Raster Calculator steps | Single code block |
| Manual formula entry | Parameterized functions |
| One-off analysis | Reproducible script |

### Activity 4: Zonal statistics by administrative boundary

To answer our research question, we need to summarize risk by area. "What percentage of each SA2 is at high flood risk?"

**Steps:**

1. Download SA2 boundaries:
   ```python
   import geopandas as gpd

   # NSW SA2 boundaries (simplified for this example)
   sa2_url = "https://www.abs.gov.au/..."  # See notebook for full URL
   sa2 = gpd.read_file(sa2_url)
   sa2 = sa2.to_crs(dem.rio.crs)

   # Clip to study area
   sa2_clip = sa2.cx[bbox[0]:bbox[2], bbox[1]:bbox[3]]
   ```

2. Calculate zonal statistics:
   ```python
   from rasterstats import zonal_stats

   stats = zonal_stats(
       sa2_clip,
       risk_index,
       affine=dem.rio.transform(),
       stats=['mean', 'median', 'min', 'max', 'count'],
       nodata=np.nan
   )

   sa2_clip['risk_mean'] = [s['mean'] for s in stats]
   ```

3. Calculate percentage at high risk:
   ```python
   high_risk_binary = (risk_classes >= 3).astype(float)

   high_risk_stats = zonal_stats(
       sa2_clip,
       high_risk_binary,
       affine=dem.rio.transform(),
       stats=['mean'],
       nodata=np.nan
   )

   # Mean of binary = proportion; multiply by 100 for percentage
   sa2_clip['pct_high_risk'] = [s['mean'] * 100 for s in high_risk_stats]
   ```

4. Identify highest-risk SA2s:
   ```python
   top_risk = sa2_clip.nlargest(5, 'pct_high_risk')
   print("SA2s with highest proportion of high-risk land:")
   print(top_risk[['SA2_NAME21', 'pct_high_risk']])
   ```

5. Create choropleth map:
   ```python
   fig, ax = plt.subplots(1, 1, figsize=(12, 10))

   sa2_clip.plot(
       column='pct_high_risk',
       cmap='Reds',
       legend=True,
       ax=ax,
       edgecolor='black',
       linewidth=0.5
   )

   ax.set_title('Percentage of SA2 at High/Very High Flood Risk')
   ax.set_axis_off()
   plt.show()
   ```

**QGIS ↔ Python comparison:**

| QGIS (Week 4) | Python (This week) |
|---------------|--------------------|
| Processing > Zonal Statistics | `rasterstats.zonal_stats()` |
| Style in Layer Properties | `geopandas.plot()` with colormap |
| Manual legend | Automatic with matplotlib |

### Activity 5: Create publication-ready outputs

Compile your analysis into professional visualizations and export results.

**Steps:**

1. Create multi-panel summary figure:
   ```python
   fig = plt.figure(figsize=(16, 12))

   # Panel 1: Risk raster with hillshade
   ax1 = plt.subplot(2, 2, 1)
   ax1.imshow(hillshade, cmap='gray', alpha=0.5)
   im1 = ax1.imshow(risk_classes, cmap=cmap, alpha=0.6, vmin=1, vmax=4)
   ax1.set_title('Flood Risk Classification')
   ax1.axis('off')

   # Panel 2: Choropleth by SA2
   ax2 = plt.subplot(2, 2, 2)
   sa2_clip.plot(column='pct_high_risk', cmap='Reds', ax=ax2,
                 legend=True, edgecolor='black', linewidth=0.5)
   ax2.set_title('% High Risk by SA2')
   ax2.axis('off')

   # Panel 3: Elevation profile
   ax3 = plt.subplot(2, 2, 3)
   ax3.hist(elev.flatten(), bins=50, color='steelblue', edgecolor='black')
   ax3.axvline(30, color='red', linestyle='--', label='Flood threshold')
   ax3.set_xlabel('Elevation (m)')
   ax3.set_ylabel('Pixel Count')
   ax3.set_title('Elevation Distribution')
   ax3.legend()

   # Panel 4: Risk area summary
   ax4 = plt.subplot(2, 2, 4)
   risk_labels = ['Low', 'Moderate', 'High', 'Very High']
   risk_areas = [(risk_classes == i+1).sum() for i in range(4)]
   ax4.bar(risk_labels, risk_areas, color=colors)
   ax4.set_ylabel('Number of Pixels')
   ax4.set_title('Area by Risk Category')

   plt.tight_layout()
   plt.savefig('exports/week09_flood_risk_analysis.png', dpi=300)
   plt.show()
   ```

2. Export raster results:
   ```python
   # Save flood risk classification as GeoTIFF
   risk_da = dem.copy(data=risk_classes)
   risk_da.rio.to_raster('data/processed/week09/flood_risk_classes.tif')
   ```

3. Export zonal statistics:
   ```python
   # CSV for reporting
   sa2_clip[['SA2_NAME21', 'risk_mean', 'pct_high_risk']].to_csv(
       'exports/week09_sa2_flood_risk.csv',
       index=False
   )

   # GeoPackage for GIS use
   sa2_clip.to_file('data/processed/week09/sa2_flood_risk.gpkg')
   ```

## Your Research Findings

After completing this analysis, summarize your findings:

### Research Question
"Which areas in the Hawkesbury-Nepean region are at elevated flood risk based on terrain characteristics?"

### Key Findings
Complete these based on your analysis:

1. The areas with highest flood risk are: _________________________________
2. Approximately ____% of the study area is classified as high or very high risk.
3. The SA2(s) with the greatest proportion of high-risk land: _________________________________
4. The elevation threshold where risk transitions from moderate to high: ____m

### Methodology
- **Data source:** Copernicus DEM 30m (via Planetary Computer API)
- **Key parameters:** Elevation weight: 60%, Slope weight: 40%, Slope threshold: 15°
- **Tools used:** Python (rioxarray, NumPy, rasterstats, geopandas)
- **Study area:** Hawkesbury-Nepean floodplain (~20km × 20km)

### Limitations
This analysis does NOT capture:

- [ ] Proximity to rivers and waterways
- [ ] Drainage infrastructure and stormwater systems
- [ ] Soil permeability and groundwater levels
- [ ] Historical flood extent data
- [ ] Hydrological flow modelling
- [ ] Climate change projections

### Week 4 ↔ Week 9 Comparison

| Aspect | QGIS (Week 4) | Python (Week 9) |
|--------|---------------|-----------------|
| Data access | Manual download from ELVIS | API fetch from Planetary Computer |
| Slope calculation | Raster > Analysis > Slope | `np.gradient()` + `np.arctan()` |
| Risk classification | Multiple Raster Calculator steps | Single code block |
| Zonal statistics | Processing toolbox | `rasterstats` library |
| Reproducibility | Project file, manual steps | Notebook, fully scripted |
| Scalability | One area at a time | Loop over multiple areas |

### If this were your capstone
- How would you adapt this for your study area?
- What additional data would strengthen the analysis?
- Could you combine this with Week 5 crime data or Week 6 accessibility analysis?

## Troubleshooting

### API returns no results
- **Check your bounding box:** Ensure coordinates are in [west, south, east, north] order
- **Try a different area:** Some regions may have missing tiles
- **Fallback:** The notebook includes synthetic data if the API is unavailable

### Memory errors with large areas
- **Reduce study area size:** Start with a 10km × 10km box
- **Use chunked processing:** Process in tiles and merge results

### CRS mismatch between raster and vector
- **Always reproject vectors to match raster CRS:**
  ```python
  sa2 = sa2.to_crs(dem.rio.crs)
  ```

### Zonal statistics returns NaN
- **Check overlap:** Ensure SA2 boundaries actually cover the raster extent
- **Check nodata:** Make sure nodata values are properly set

## Support materials

- Slides: [Week 09 lecture deck](../slides/index.md)
- Lecture notes: [Elevation & Surface Modelling](../lectures/week09-remote-sensing.md)
- QGIS workflow: [Week 4 · Flood Risk Assessment](week04.md)
- Planetary Computer: [https://planetarycomputer.microsoft.com/](https://planetarycomputer.microsoft.com/)
- rioxarray documentation: [https://corteva.github.io/rioxarray/](https://corteva.github.io/rioxarray/)
- Dataset checklist: [Week 9 items](../reference/data-download-checklist.md)

## Reflect

Take 10-15 minutes to answer these questions in your [Week 9 reflection](../reference/reflections.md#week-9--raster--remote-sensing):

- How did your Python results compare to your Week 4 QGIS analysis? Were the high-risk areas the same?
- What are the advantages of cloud-hosted data access vs. downloading files?
- How did changing the weighting (60/40 for elevation/slope) affect your results?
- What challenges did you encounter with the API, raster processing, or zonal statistics?
- How could you extend this analysis for a capstone project?

!!! note "Real-world applications"
    The techniques you learned this week are used daily by:

    - Emergency services for evacuation planning and resource allocation
    - Insurance companies for flood risk assessment and premium calculation
    - Urban planners for development restrictions in flood-prone areas
    - Climate scientists for modelling future flood scenarios

## What you'll submit

- [ ] Jupyter notebook (`week09_raster_remote_sensing.ipynb`) with all cells executed
- [ ] Flood risk raster: `data/processed/week09/flood_risk_classes.tif`
- [ ] SA2 analysis: `data/processed/week09/sa2_flood_risk.gpkg`
- [ ] Summary figure: `exports/week09_flood_risk_analysis.png`
- [ ] Zonal statistics: `exports/week09_sa2_flood_risk.csv`
- [ ] Completed "Your Research Findings" section
- [ ] Your Week 9 reflection entry

## Coming up next week

Week 10 shifts to network analysis in Python—calculating optimal routes, service areas, and accessibility metrics using NetworkX and OSMnx. You'll analyze which communities have poor access to emergency services, connecting the flood risk areas you identified this week with transport network analysis.
