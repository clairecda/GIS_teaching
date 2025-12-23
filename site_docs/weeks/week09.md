# Week 9 · Raster & Remote Sensing in Python

Satellite imagery opens a window to environmental change at scales impossible to observe from the ground. This week, you'll process real satellite data using Python to detect changes in vegetation health, land use, or environmental disturbance. You'll move beyond QGIS's raster tools to write reproducible code that handles multispectral imagery, calculates vegetation indices like NDVI, and quantifies change across administrative boundaries. These techniques form the foundation of environmental monitoring, climate research, and disaster response workflows used by organizations worldwide.

## What you'll learn

By the end of this week, you'll be able to:

1. Load and inspect satellite imagery (Sentinel-2 or Landsat) using Rasterio and understand raster metadata (bands, resolution, CRS, nodata values).
2. Clip large rasters to your area of interest and perform band math to calculate spectral indices like NDVI (Normalized Difference Vegetation Index).
3. Detect environmental change by comparing before/after imagery and quantifying differences.
4. Calculate zonal statistics to summarize change metrics per administrative boundary (SA2, LGA, watershed) and export results for reporting.

## Before you start

### 1. Get the notebook

📓 **Download the Week 9 notebook:** [week09_raster_remote_sensing.ipynb](../../resources/notebooks/week09_raster_remote_sensing.ipynb)

**Where to save it:** Save to your `intro-gis/notebooks/` folder

### 2. Confirm your environment works

- [ ] Activate your conda environment: `conda activate intro-gis`
- [ ] Check Rasterio imports: `python -c "import rasterio; print('✅ Ready!')"`
- [ ] If you see errors, review [Week 7 setup](week07.md)

### 3. Download datasets

- [ ] Follow the [Downloading datasets](../onboarding/data-downloads.md) guide for Week 9
- [ ] You need:
  - Sentinel-2 or Landsat imagery (before/after images)
  - Area of interest boundary polygon
  - Zone boundaries for statistics (optional)
- [ ] Save to `intro-gis/data/processed/week09/`
  - `sentinel_before.tif`
  - `sentinel_after.tif`
  - `aoi.geojson`
  - `zones.geojson`

**Alternative:** If satellite data is too large, your instructor may provide pre-processed sample data.

### 4. Review the lecture

- [ ] Read: [Week 9 · Remote Sensing Change Detection](../lectures/week09-remote-sensing.md) for essential background on spectral bands and indices

!!! tip "Memory management heads up"
    Satellite imagery files can be large (100MB - several GB). You'll learn techniques to work efficiently with big rasters—clipping early, reading only needed bands, and using windowed reading. Don't try to load entire scenes into memory at once!

## This week's activities

### Activity 1: Understanding raster data in Python

Before processing imagery, you need to understand how rasters are structured differently from vector data you've worked with so far.

**Key concepts:**

- **Bands**: Rasters can have multiple layers (bands) representing different wavelengths of light. Sentinel-2 has 13 bands, Landsat has 11.
- **Resolution**: Pixel size (e.g., 10m means each pixel represents a 10m × 10m area on the ground)
- **Nodata values**: Pixels outside the imagery extent or obscured by clouds are marked as nodata (often -9999, 0, or NaN)
- **Affine transform**: Mathematical relationship between pixel coordinates (row, column) and real-world coordinates (X, Y)

**Steps:**

1. Open your Jupyter notebook and import core libraries:
   ```python
   from pathlib import Path
   import rasterio
   import numpy as np
   import geopandas as gpd
   import matplotlib.pyplot as plt
   ```

2. Load one of your satellite images and inspect its metadata:
   ```python
   with rasterio.open("data/processed/week09/sentinel_before.tif") as src:
       print(f"Bands: {src.count}")
       print(f"Width x Height: {src.width} x {src.height}")
       print(f"CRS: {src.crs}")
       print(f"Resolution: {src.res}")
       print(f"Bounds: {src.bounds}")
       print(f"Nodata value: {src.nodata}")
   ```

3. Read and visualize a single band:
   ```python
   with rasterio.open("data/processed/week09/sentinel_before.tif") as src:
       band4 = src.read(4)  # Red band for Sentinel-2

   plt.imshow(band4, cmap='gray')
   plt.colorbar(label='Digital Number')
   plt.title('Red band (Band 4)')
   plt.show()
   ```

**Compare to QGIS:**
In QGIS, you viewed raster properties through the Information panel and styled bands visually. In Python, you explicitly read metadata and array data. The benefit? You can programmatically process hundreds of rasters with the same code.

!!! note "Band numbering"
    Sentinel-2 bands: Band 4 = Red, Band 8 = NIR (Near-Infrared), Band 3 = Green, Band 2 = Blue
    Landsat 8/9 bands: Band 4 = Red, Band 5 = NIR, Band 3 = Green, Band 2 = Blue
    Check your dataset documentation—band numbers vary between sensors!

### Activity 2: Loading and clipping satellite imagery

Working with full satellite scenes is slow and memory-intensive. You'll clip rasters to your area of interest early in the workflow.

**Steps:**

1. Load your area of interest polygon (created in Week 3 or 8):
   ```python
   aoi = gpd.read_file("data/processed/week09/aoi.geojson")
   aoi = aoi.to_crs("EPSG:32756")  # Match raster CRS (example: UTM Zone 56S)
   ```

2. Verify CRS alignment between your raster and vector:
   ```python
   with rasterio.open("data/processed/week09/sentinel_before.tif") as src:
       print(f"Raster CRS: {src.crs}")
   print(f"Vector CRS: {aoi.crs}")
   # If they don't match, reproject the vector: aoi = aoi.to_crs(src.crs)
   ```

3. Clip the raster to your AOI using `rasterio.mask`:
   ```python
   from rasterio.mask import mask

   def clip_raster(raster_path, shapes):
       with rasterio.open(raster_path) as src:
           out_image, out_transform = mask(src, shapes.geometry, crop=True)
           out_meta = src.meta.copy()
           out_meta.update({
               "height": out_image.shape[1],
               "width": out_image.shape[2],
               "transform": out_transform
           })
       return out_image, out_meta

   before_clip, before_meta = clip_raster(
       "data/processed/week09/sentinel_before.tif",
       aoi
   )
   ```

4. Save the clipped raster for faster future access:
   ```python
   with rasterio.open("data/processed/week09/before_clipped.tif", "w", **before_meta) as dst:
       dst.write(before_clip)
   ```

5. Repeat for your "after" imagery

**Why clip early?**
A full Sentinel-2 tile is 10,980 × 10,980 pixels (120 million pixels). Clipping to a city reduces this to perhaps 1,000 × 1,000 (1 million pixels)—100x faster to process!

### Activity 3: Band math and NDVI calculation

NDVI (Normalized Difference Vegetation Index) measures vegetation health by comparing red and near-infrared reflectance. Healthy vegetation reflects strongly in NIR but absorbs red light.

**The NDVI formula:**
```
NDVI = (NIR - Red) / (NIR + Red)
```

NDVI values range from -1 to +1:
- **-1 to 0**: Water, bare soil, clouds
- **0 to 0.2**: Sparse vegetation, rock
- **0.2 to 0.4**: Shrubs, grassland
- **0.4 to 0.8**: Healthy vegetation, forests
- **0.8 to 1**: Very dense vegetation

**Steps:**

1. Extract Red and NIR bands from your clipped imagery:
   ```python
   # Sentinel-2: Band 4 = Red (index 3), Band 8 = NIR (index 7)
   red = before_clip[3].astype(float)  # Convert to float for division
   nir = before_clip[7].astype(float)
   ```

2. Handle nodata values (critical step!):
   ```python
   # Replace nodata with NaN to avoid calculation errors
   nodata_value = before_meta['nodata']
   if nodata_value is not None:
       red = np.where(red == nodata_value, np.nan, red)
       nir = np.where(nir == nodata_value, np.nan, nir)
   ```

3. Calculate NDVI:
   ```python
   # Add small epsilon to avoid division by zero
   ndvi_before = (nir - red) / (nir + red + 1e-8)

   # Clean up invalid values
   ndvi_before = np.where(np.isfinite(ndvi_before), ndvi_before, np.nan)
   ```

4. Visualize NDVI with appropriate color scheme:
   ```python
   plt.figure(figsize=(10, 8))
   plt.imshow(ndvi_before, cmap='RdYlGn', vmin=-0.2, vmax=0.8)
   plt.colorbar(label='NDVI', shrink=0.8)
   plt.title('NDVI - Before')
   plt.axis('off')
   plt.show()
   ```

5. Calculate summary statistics:
   ```python
   print(f"Mean NDVI: {np.nanmean(ndvi_before):.3f}")
   print(f"Median NDVI: {np.nanmedian(ndvi_before):.3f}")
   print(f"Std Dev: {np.nanstd(ndvi_before):.3f}")
   print(f"Min: {np.nanmin(ndvi_before):.3f}, Max: {np.nanmax(ndvi_before):.3f}")
   ```

6. Repeat for "after" imagery to create `ndvi_after`

!!! tip "Other useful indices"
    - **EVI** (Enhanced Vegetation Index): Improved version of NDVI, better for dense vegetation
    - **NDWI** (Normalized Difference Water Index): Detects water bodies
    - **NDBI** (Normalized Difference Built-up Index): Identifies urban areas
    - **NBR** (Normalized Burn Ratio): Assesses wildfire damage

    Each uses different band combinations. The band math workflow is the same!

### Activity 4: Change detection (before/after comparison)

Now you'll quantify how vegetation health changed between your two time periods.

**Steps:**

1. Calculate NDVI difference:
   ```python
   ndvi_change = ndvi_after - ndvi_before
   ```

2. Visualize the change:
   ```python
   plt.figure(figsize=(12, 9))

   # Use diverging colormap: red = loss, green = gain
   im = plt.imshow(ndvi_change, cmap='RdYlGn', vmin=-0.3, vmax=0.3)
   plt.colorbar(im, label='NDVI Change', shrink=0.8)
   plt.title('Vegetation Change (After - Before)')
   plt.axis('off')
   plt.show()
   ```

3. Classify change into categories:
   ```python
   # Create change categories
   change_categories = np.full(ndvi_change.shape, -9999, dtype=np.int8)
   change_categories[ndvi_change < -0.15] = 1  # Major loss
   change_categories[(ndvi_change >= -0.15) & (ndvi_change < -0.05)] = 2  # Moderate loss
   change_categories[(ndvi_change >= -0.05) & (ndvi_change <= 0.05)] = 3  # No change
   change_categories[(ndvi_change > 0.05) & (ndvi_change <= 0.15)] = 4  # Moderate gain
   change_categories[ndvi_change > 0.15] = 5  # Major gain
   change_categories[~np.isfinite(ndvi_change)] = -9999  # Nodata
   ```

4. Calculate area statistics:
   ```python
   pixel_area = before_meta['transform'][0] ** 2  # m² per pixel

   # Count pixels in each category
   major_loss_px = np.sum(change_categories == 1)
   moderate_loss_px = np.sum(change_categories == 2)
   no_change_px = np.sum(change_categories == 3)
   moderate_gain_px = np.sum(change_categories == 4)
   major_gain_px = np.sum(change_categories == 5)

   # Convert to hectares
   print(f"Major vegetation loss: {major_loss_px * pixel_area / 10000:.2f} ha")
   print(f"Moderate vegetation loss: {moderate_loss_px * pixel_area / 10000:.2f} ha")
   print(f"No significant change: {no_change_px * pixel_area / 10000:.2f} ha")
   print(f"Moderate vegetation gain: {moderate_gain_px * pixel_area / 10000:.2f} ha")
   print(f"Major vegetation gain: {major_gain_px * pixel_area / 10000:.2f} ha")
   ```

5. Create a side-by-side comparison:
   ```python
   fig, axes = plt.subplots(1, 3, figsize=(18, 6))

   axes[0].imshow(ndvi_before, cmap='RdYlGn', vmin=-0.2, vmax=0.8)
   axes[0].set_title('NDVI - Before')
   axes[0].axis('off')

   axes[1].imshow(ndvi_after, cmap='RdYlGn', vmin=-0.2, vmax=0.8)
   axes[1].set_title('NDVI - After')
   axes[1].axis('off')

   im = axes[2].imshow(ndvi_change, cmap='RdYlGn', vmin=-0.3, vmax=0.3)
   axes[2].set_title('NDVI Change')
   axes[2].axis('off')

   plt.colorbar(im, ax=axes[2], label='Change', shrink=0.8)
   plt.tight_layout()
   plt.savefig('exports/week09_ndvi_change_comparison.png', dpi=300, bbox_inches='tight')
   plt.show()
   ```

**Interpretation questions:**
- What areas show the most vegetation loss? Can you identify the cause (urbanization, fire, drought)?
- Are areas of gain clustered or scattered? (Might indicate reforestation or seasonal growth)
- Do edges of the study area show artifacts? (Common with imagery mosaics)

### Activity 5: Zonal statistics against boundaries

Aggregate your pixel-level change data to administrative boundaries to answer questions like "Which council area lost the most vegetation?" or "Which watershed is most affected?"

**Steps:**

1. Load your boundary polygons (SA2, LGA, watersheds, etc.):
   ```python
   zones = gpd.read_file("data/processed/week09/zones.geojson")
   zones = zones.to_crs(before_meta['crs'])  # Match raster CRS
   ```

2. Calculate zonal statistics using `rasterstats`:
   ```python
   from rasterstats import zonal_stats

   # Calculate stats for NDVI change
   stats = zonal_stats(
       zones,
       ndvi_change,
       affine=before_meta['transform'],
       stats=['mean', 'median', 'min', 'max', 'std', 'count'],
       nodata=np.nan
   )

   # Add results to GeoDataFrame
   zones_stats = zones.copy()
   for key in stats[0].keys():
       zones_stats[f'ndvi_{key}'] = [s[key] for s in stats]
   ```

3. Identify most affected areas:
   ```python
   # Sort by mean change
   zones_stats_sorted = zones_stats.sort_values('ndvi_mean')

   print("Top 5 areas with vegetation LOSS:")
   print(zones_stats_sorted[['name', 'ndvi_mean']].head())

   print("\nTop 5 areas with vegetation GAIN:")
   print(zones_stats_sorted[['name', 'ndvi_mean']].tail())
   ```

4. Visualize zonal summary on a map:
   ```python
   fig, ax = plt.subplots(1, 1, figsize=(12, 10))

   zones_stats.plot(
       column='ndvi_mean',
       cmap='RdYlGn',
       legend=True,
       ax=ax,
       edgecolor='black',
       linewidth=0.5,
       vmin=-0.2,
       vmax=0.2
   )

   ax.set_title('Mean NDVI Change by Zone', fontsize=16)
   ax.set_axis_off()
   plt.tight_layout()
   plt.savefig('exports/week09_zonal_change.png', dpi=300, bbox_inches='tight')
   plt.show()
   ```

5. Calculate additional metrics (optional):
   ```python
   # Percentage of zone area with significant loss (NDVI drop > 0.1)
   loss_threshold_stats = zonal_stats(
       zones,
       (ndvi_change < -0.1).astype(np.uint8),
       affine=before_meta['transform'],
       stats=['sum', 'count'],
       nodata=0
   )

   zones_stats['pct_significant_loss'] = [
       (s['sum'] / s['count'] * 100) if s['count'] > 0 else 0
       for s in loss_threshold_stats
   ]

   print("\nAreas with >20% significant vegetation loss:")
   print(zones_stats[zones_stats['pct_significant_loss'] > 20][['name', 'pct_significant_loss']])
   ```

!!! note "Statistical validity"
    Zonal statistics are only meaningful when you have enough pixels per zone. A zone with only 5 pixels won't produce reliable statistics. Filter out zones with low pixel counts (`zones_stats[zones_stats['ndvi_count'] > 100]`).

### Activity 6: Visualization and export

Create publication-ready visualizations and export your results for reporting or further analysis.

**Steps:**

1. Create a comprehensive figure with multiple subplots:
   ```python
   fig = plt.figure(figsize=(16, 12))

   # Raster change map
   ax1 = plt.subplot(2, 2, 1)
   im1 = ax1.imshow(ndvi_change, cmap='RdYlGn', vmin=-0.3, vmax=0.3)
   ax1.set_title('Pixel-level NDVI Change', fontsize=14)
   ax1.axis('off')
   plt.colorbar(im1, ax=ax1, shrink=0.8)

   # Zonal summary map
   ax2 = plt.subplot(2, 2, 2)
   zones_stats.plot(column='ndvi_mean', cmap='RdYlGn', ax=ax2,
                    legend=True, edgecolor='black', linewidth=0.5,
                    vmin=-0.2, vmax=0.2)
   ax2.set_title('Mean NDVI Change by Zone', fontsize=14)
   ax2.set_axis_off()

   # Histogram of change values
   ax3 = plt.subplot(2, 2, 3)
   ax3.hist(ndvi_change[np.isfinite(ndvi_change)].flatten(),
            bins=50, color='steelblue', edgecolor='black', alpha=0.7)
   ax3.axvline(0, color='red', linestyle='--', linewidth=2, label='No change')
   ax3.set_xlabel('NDVI Change', fontsize=12)
   ax3.set_ylabel('Pixel Count', fontsize=12)
   ax3.set_title('Distribution of NDVI Change', fontsize=14)
   ax3.legend()
   ax3.grid(alpha=0.3)

   # Top zones bar chart
   ax4 = plt.subplot(2, 2, 4)
   top_loss = zones_stats_sorted.head(5)
   top_gain = zones_stats_sorted.tail(5)
   combined = pd.concat([top_loss, top_gain])

   colors = ['red' if x < 0 else 'green' for x in combined['ndvi_mean']]
   ax4.barh(combined['name'], combined['ndvi_mean'], color=colors, alpha=0.7)
   ax4.axvline(0, color='black', linewidth=1)
   ax4.set_xlabel('Mean NDVI Change', fontsize=12)
   ax4.set_title('Top 5 Loss/Gain Zones', fontsize=14)
   ax4.grid(axis='x', alpha=0.3)

   plt.tight_layout()
   plt.savefig('exports/week09_comprehensive_analysis.png', dpi=300, bbox_inches='tight')
   plt.show()
   ```

2. Export the change raster as GeoTIFF:
   ```python
   change_meta = before_meta.copy()
   change_meta.update({
       'count': 1,
       'dtype': 'float32',
       'nodata': -9999
   })

   with rasterio.open('data/processed/week09/ndvi_change.tif', 'w', **change_meta) as dst:
       # Replace NaN with nodata value for export
       ndvi_change_export = np.where(np.isfinite(ndvi_change), ndvi_change, -9999)
       dst.write(ndvi_change_export.astype('float32'), 1)
   ```

3. Export zonal statistics to CSV and GeoPackage:
   ```python
   # CSV for spreadsheet analysis
   zones_stats[['name', 'ndvi_mean', 'ndvi_median', 'ndvi_std',
                'pct_significant_loss']].to_csv(
       'exports/week09_zonal_statistics.csv',
       index=False
   )

   # GeoPackage for use in QGIS or Week 10
   zones_stats.to_file(
       'data/processed/week09/zones_change.gpkg',
       driver='GPKG',
       layer='ndvi_change_zones'
   )
   ```

4. Create a metadata file documenting your analysis:
   ```python
   metadata = f"""
   NDVI Change Analysis Metadata
   ==============================

   Analysis Date: {pd.Timestamp.now().strftime('%Y-%m-%d')}
   Study Area: {aoi['name'].iloc[0] if 'name' in aoi.columns else 'Custom AOI'}

   Imagery Sources:
   - Before: [Source and date]
   - After: [Source and date]

   Raster Details:
   - CRS: {before_meta['crs']}
   - Resolution: {before_meta['transform'][0]}m
   - Extent: {before_meta['bounds']}

   NDVI Calculation:
   - Formula: (NIR - Red) / (NIR + Red)
   - Bands: Red = Band {4}, NIR = Band {8}  # Adjust for your sensor

   Summary Statistics:
   - Mean change: {np.nanmean(ndvi_change):.4f}
   - Median change: {np.nanmedian(ndvi_change):.4f}
   - Std deviation: {np.nanstd(ndvi_change):.4f}
   - Area analyzed: {np.sum(np.isfinite(ndvi_change)) * pixel_area / 10000:.2f} ha

   Zones Analyzed: {len(zones_stats)}
   Zones with significant loss (>10% area): {len(zones_stats[zones_stats['pct_significant_loss'] > 10])}

   Limitations:
   - Cloud cover: [Assess and note]
   - Seasonal effects: [Note if comparing different seasons]
   - Sensor differences: [Note if using different satellites]
   """

   with open('exports/week09_metadata.txt', 'w') as f:
       f.write(metadata)
   ```

!!! tip "Publishing your work"
    These visualizations are publication-ready for reports, presentations, or web articles. Consider adding:
    - North arrow and scale bar (use matplotlib's `annotate()` or cartopy)
    - Inset map showing study area location
    - Data source attribution in footer
    - Clear legend with units

**Compare to QGIS:**
In QGIS, you used the Raster Calculator for band math and Zonal Statistics tool for summaries. Python gives you more control over classification thresholds, batch processing multiple time periods, and creating complex multi-panel figures. For one-off analysis, QGIS is faster. For repeatable workflows or processing dozens of scenes, Python is essential.

## Support materials

- Slides: [Week 09 lecture deck](../slides/index.md)
- Lecture notes: [Remote Sensing Change Detection](../lectures/week09-remote-sensing.md)
- Jupyter notebook: `resources/notebooks/week09_raster_remote_sensing.ipynb`
- Rasterio documentation: [https://rasterio.readthedocs.io/](https://rasterio.readthedocs.io/)
- Sentinel-2 band information: [ESA User Guide](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-2-msi/resolutions/spatial)
- Landsat band information: [USGS Guide](https://www.usgs.gov/faqs/what-are-band-designations-landsat-satellites)
- Dataset checklist: [Week 9 items](../reference/data-download-checklist.md)

## Reflect

Take 10-15 minutes to answer these questions in your [Week 9 reflection](../reference/reflections.md#week-9--raster--remote-sensing):

- What patterns did your NDVI analysis reveal? Were you surprised by what you found?
- How did you decide on change thresholds (e.g., what counts as "significant" loss)? How might different thresholds change your conclusions?
- What challenges did you encounter with nodata values, memory management, or band selection?
- How confident are you in your results? What are potential sources of error (clouds, sensor calibration, seasonal differences)?
- What additional data or context would help interpret your findings (precipitation data, land use maps, historical imagery)?
- When would you use Python for raster analysis versus staying in QGIS?

!!! note "Real-world applications"
    The techniques you learned this week are used daily by:
    - Environmental agencies monitoring deforestation and wetland loss
    - Agricultural scientists tracking crop health and yield prediction
    - Climate researchers measuring glacier retreat and sea ice extent
    - Disaster response teams assessing wildfire damage or flood impacts
    - Urban planners analyzing green space changes over time

## What you'll submit

- [ ] Jupyter notebook (`week09_raster_remote_sensing.ipynb`) with all cells executed and outputs visible
- [ ] NDVI change raster: `data/processed/week09/ndvi_change.tif`
- [ ] Zonal statistics: `exports/week09_zonal_statistics.csv` and `data/processed/week09/zones_change.gpkg`
- [ ] Comprehensive analysis figure: `exports/week09_comprehensive_analysis.png`
- [ ] Metadata documentation: `exports/week09_metadata.txt`
- [ ] Your Week 9 reflection entry

## Coming up next week

Week 10 shifts to network analysis in Python—calculating optimal routes, service areas, and accessibility metrics using NetworkX and OSMnx. You'll bring together the zonal statistics from this week with network-based accessibility analysis to identify communities that lack both green space AND easy transport access. Make sure your Python environment is working smoothly and review your Week 6 QGIS network analysis to refresh the concepts.
