# Week 9 Facilitator Notes: Raster & Remote Sensing in Python

## Session Overview

**Duration:** 3 hours (2-hour workshop + 1-hour guided practice)

**Learning Objectives:**
By the end of this session, students will be able to:

1. Load and inspect satellite imagery using Rasterio, understanding raster metadata (bands, resolution, CRS, nodata values)
2. Clip large rasters to areas of interest and perform band math to calculate spectral indices like NDVI
3. Detect environmental change by comparing before/after imagery and quantifying differences
4. Calculate zonal statistics to summarize change metrics per administrative boundary and export results for reporting

**Materials Needed:**

- [ ] Pre-processed satellite imagery datasets (Sentinel-2 or Landsat) for all students
  - Before imagery (e.g., 2019 or pre-event)
  - After imagery (e.g., 2024 or post-event)
  - Ideally showing clear change (deforestation, urban growth, fire recovery, etc.)
- [ ] Area of interest boundary polygons (GeoJSON format)
- [ ] Zone boundaries for statistics (SA2, LGA, or watersheds - GeoJSON/GeoPackage)
- [ ] Week 9 Jupyter notebook distributed to students
- [ ] Backup Colab notebook link (for students with local environment issues)
- [ ] Example change detection results to show at session start
- [ ] Slide deck covering remote sensing fundamentals

**Pre-requisites:**
Students should have completed Weeks 1-8, particularly:
- Week 2: Python basics and NumPy array operations
- Week 3: Vector analysis with GeoPandas
- Week 5-6: QGIS raster analysis (for conceptual foundation)

---

## Before Class Checklist

### Data Preparation (Complete 1 week before)

- [ ] **Source satellite imagery** for your study region:
  - **Option 1 (Recommended):** Use Google Earth Engine to export pre-processed Sentinel-2 imagery
  - **Option 2:** Download from [Copernicus Open Access Hub](https://scihub.copernicus.eu/)
  - **Option 3:** Use USGS EarthExplorer for Landsat data
  - Choose dates with <10% cloud cover
  - Select imagery showing clear environmental change (fire scars, urban expansion, seasonal vegetation change)

- [ ] **Pre-process imagery** to manageable size:
  - Clip to a reasonable study area (10km x 10km to 50km x 50km)
  - Export as GeoTIFF with 4-8 essential bands (RGB, NIR minimum)
  - Test file size: should be 10-100MB per file (not multi-GB)
  - Ensure both before/after images have identical CRS, resolution, and extent

- [ ] **Prepare boundary files:**
  - Area of interest polygon covering the study region
  - Zonal boundaries (5-20 zones ideal for demonstration)
  - Ensure all files are in same CRS as satellite imagery

- [ ] **Upload to shared location:**
  - Create Google Drive folder or institutional file share
  - Test download speeds
  - Provide clear file naming: `sentinel_before_20190315.tif`, `sentinel_after_20240408.tif`

### Technical Testing (Complete 3 days before)

- [ ] **Test all environments:**
  ```python
  import rasterio
  import rasterstats
  import geopandas as gpd
  import numpy as np
  import matplotlib.pyplot as plt

  print("Rasterio version:", rasterio.__version__)
  print("All imports successful!")
  ```

- [ ] **Verify Colab compatibility:**
  - Run through entire notebook in Colab
  - Confirm `pip install` cell works without errors
  - Test file upload process
  - Note: Colab sessions timeout after 90 minutes of inactivity

- [ ] **Run complete workflow** with your prepared data:
  - Load and clip rasters (time this step - should be <2 minutes)
  - Calculate NDVI for both dates
  - Create change detection maps
  - Run zonal statistics
  - Document any unexpected behavior

- [ ] **Prepare backup datasets:** If primary data has issues (cloud cover discovered, file corruption), have alternative ready

### Student Communications (Send 2-3 days before)

Email students with:

- [ ] Data download links and file checklist
- [ ] Reminder to test their Python environment: `conda activate intro-gis` and `import rasterio`
- [ ] Colab backup option for those with installation issues
- [ ] Optional reading: Week 9 lecture notes on remote sensing fundamentals
- [ ] Reminder about file sizes: "Satellite imagery files are large. Start downloads early and ensure you have 500MB+ free disk space."

---

## Session Flow

### Opening (0:00 - 0:15, 15 minutes)

**Welcome & Context Setting**

1. **Hook with real-world example (5 min):**
   - Show compelling before/after satellite imagery:
     - Amazon deforestation (clear-cut patches appearing)
     - Australian bushfire scars (2019-2020 Black Summer)
     - Urban expansion (agricultural land → suburbs)
     - Glacier retreat or wetland loss
   - "These images are from publicly available satellites that pass overhead every few days. Today you'll learn to quantify these changes programmatically."

2. **Learning objectives overview (3 min):**
   - Walk through the 4 main objectives
   - Emphasize: "By end of session, you'll have a complete change detection workflow you can adapt to any region or environmental question"

3. **Session roadmap (2 min):**
   - "We'll move from loading individual rasters → clipping → band math → change detection → spatial statistics"
   - Show the final visualization students will create

4. **Data check (5 min):**
   - "Quick hands up: who has downloaded all data files?"
   - "Who is using Google Colab vs local Jupyter?"
   - Address any immediate technical issues
   - Share screen showing folder structure: `data/processed/week09/` with all required files

**Key Teaching Point:**
Emphasize that satellite analysis requires computational thinking: "Unlike clicking through QGIS, you'll write code that can process hundreds of images automatically. Initial setup takes longer, but the reproducibility is invaluable."

---

### Part 1: Understanding Raster Data in Python (0:15 - 0:45, 30 minutes)

**Activity 1: Raster fundamentals (15 min live demo)**

**Concept introduction (5 min):**
- "Rasters are fundamentally different from the vector data (points, lines, polygons) we've worked with. They're grids of pixels, each storing one or more values."
- Draw on board/slide:
  ```
  Vector: geometries with attributes
  Raster: arrays with spatial reference
  ```
- "In Python, we use Rasterio to read rasters and NumPy to manipulate the pixel arrays."

**Live Demo Script:**

```python
# 1. Open and inspect metadata
import rasterio

with rasterio.open("data/processed/week09/sentinel_before.tif") as src:
    print(f"Number of bands: {src.count}")
    print(f"Dimensions: {src.width} x {src.height} pixels")
    print(f"CRS: {src.crs}")
    print(f"Resolution: {src.res[0]} meters")
    print(f"Nodata value: {src.nodata}")
    print(f"Bounds: {src.bounds}")
```

**Pause for explanation:**
- "Note the context manager (`with` statement) - it automatically closes the file"
- "Resolution is 10m for Sentinel-2 bands 2,3,4,8 (the ones we'll use)"
- "`src.count` tells us how many bands - Sentinel-2 has 13, but we may have exported fewer"

```python
# 2. Read a single band as NumPy array
with rasterio.open("data/processed/week09/sentinel_before.tif") as src:
    red_band = src.read(4)  # Band 4 = Red for Sentinel-2

print(f"Data type: {red_band.dtype}")
print(f"Shape: {red_band.shape}")
print(f"Value range: {red_band.min()} to {red_band.max()}")
```

**Pause for explanation:**
- "`.read(4)` returns a 2D NumPy array - just like the arrays we learned in Week 2"
- "Each cell value is a 'digital number' representing reflected light intensity"
- "Values typically range from 0-10000 for Sentinel-2 (stored as uint16)"

```python
# 3. Visualize the band
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
plt.imshow(red_band, cmap='gray')
plt.colorbar(label='Digital Number')
plt.title('Sentinel-2 Band 4 (Red)')
plt.axis('off')
plt.show()
```

**Pause for explanation:**
- "This is raw data - not yet a pretty RGB composite, just one band"
- "Dark areas = low reflectance (water, shadows), bright = high reflectance (bare soil, buildings)"

**Common student questions to anticipate:**
- **Q:** "Why does it look grainy/pixelated?"
  - **A:** "Each pixel is 10m x 10m. Zoom matters! This looks coarse at city scale but fine for regional analysis."
- **Q:** "What's the difference between raster bands and RGB image layers?"
  - **A:** "Satellite bands capture specific wavelengths beyond visible light. We have red, green, blue BUT also near-infrared, shortwave infrared, etc. RGB images combine 3 bands for display; satellites have 10+ bands for analysis."
- **Q:** "Can I just use `plt.imread()` instead of Rasterio?"
  - **A:** "No! `imread()` loses spatial reference (CRS, coordinates). Rasterio preserves georeferencing."

**Activity: Students explore metadata (10 min hands-on)**

"Now open your own `sentinel_before.tif` and answer these questions in your notebook:"

1. How many bands does your imagery have?
2. What is the pixel resolution?
3. What CRS is it in? (Is it geographic lat/lon or projected like UTM?)
4. Read and display band 8 (NIR) - how does it differ from the red band visually?

**Circulate and help:**
- Watch for students who can't find their data files (path issues)
- Check that Colab users have uploaded files correctly
- Verify students are using correct band numbers for their sensor (Sentinel vs Landsat)

**Debrief (5 min):**
- "What did you notice about the NIR band vs Red band?"
- Expected answer: "NIR is brighter over vegetation, darker over water"
- "Exactly! Healthy plants reflect NIR strongly. This difference is the basis for vegetation indices like NDVI."

---

### Part 2: Clipping Rasters to AOI (0:45 - 1:05, 20 minutes)

**Why clip? (3 min discussion)**

Ask students: "Why not just work with the full satellite scene?"

Collect responses, then emphasize:
- **Memory:** Full Sentinel-2 tile = 10,980 x 10,980 x 13 bands = 1.6 billion values. Your laptop has limits!
- **Speed:** Processing time scales with pixel count. Clipping 100x can mean 100x faster.
- **Focus:** Removes irrelevant areas, makes visualization clearer.

**Live Demo: Clipping workflow (12 min)**

```python
# 1. Load area of interest
import geopandas as gpd

aoi = gpd.read_file("data/processed/week09/aoi.geojson")
print(f"AOI CRS: {aoi.crs}")
aoi.plot(facecolor='none', edgecolor='red', linewidth=2)
plt.title('Area of Interest')
plt.show()
```

**Critical teaching moment - CRS alignment:**

```python
# 2. Check CRS match
with rasterio.open("data/processed/week09/sentinel_before.tif") as src:
    print(f"Raster CRS: {src.crs}")
    print(f"Vector CRS: {aoi.crs}")

# If they don't match:
if aoi.crs != src.crs:
    print("⚠️ CRS mismatch! Reprojecting vector to match raster...")
    aoi = aoi.to_crs(src.crs)
```

**Emphasize:** "ALWAYS reproject the vector to match the raster, not vice versa. Reprojecting rasters is slow and can degrade data quality. Vectors are fast to reproject."

```python
# 3. Perform the clip
from rasterio.mask import mask

def clip_raster(raster_path, shapes):
    """Clip raster to polygon boundary"""
    with rasterio.open(raster_path) as src:
        # mask() returns clipped array and updated transform
        out_image, out_transform = mask(src, shapes.geometry, crop=True)

        # Update metadata for the clipped raster
        out_meta = src.meta.copy()
        out_meta.update({
            "height": out_image.shape[1],
            "width": out_image.shape[2],
            "transform": out_transform
        })

    return out_image, out_meta

# Clip both images
before_clipped, before_meta = clip_raster(
    "data/processed/week09/sentinel_before.tif",
    aoi
)

after_clipped, after_meta = clip_raster(
    "data/processed/week09/sentinel_after.tif",
    aoi
)

print(f"Original size: ~11000 x 11000")
print(f"Clipped size: {before_clipped.shape[1]} x {before_clipped.shape[2]}")
```

**Pause for explanation:**
- "The `mask()` function does the heavy lifting: it sets pixels outside your polygon to nodata"
- "`crop=True` means 'trim the array to just the bounding box' - saves even more memory"
- "We get back TWO things: the clipped array AND a new transform (updated coordinates)"

```python
# 4. Optional: Save clipped raster for faster future access
with rasterio.open("data/processed/week09/before_clipped.tif", "w", **before_meta) as dst:
    dst.write(before_clipped)

print("✅ Saved clipped raster")
```

**Student practice (5 min):**
- "Clip your own before and after images to your AOI"
- "Compare file sizes: check the shape before and after clipping"
- "Save your clipped versions"

**Common issues to watch for:**
- **CRS mismatch errors:** Students forget to reproject AOI
- **"geometry" error:** AOI GeoDataFrame is empty or has invalid geometries
- **Memory errors:** Original file too large even to open - suggest using `.read(1, window=...)` for partial reads first

---

### Break (1:05 - 1:15, 10 minutes)

"Take a break! When we return, we'll calculate NDVI and detect change."

---

### Part 3: NDVI Calculation & Band Math (1:15 - 1:45, 30 minutes)

**Concept introduction: Why NDVI? (5 min)**

Show diagram/slide:
```
Healthy vegetation:
- Absorbs RED light (for photosynthesis)
- Reflects NIR strongly (plant cell structure)

NDVI = (NIR - RED) / (NIR + RED)

Result ranges from -1 to +1:
  -1 to 0   : Water, clouds, snow
   0 to 0.2 : Bare soil, rock, urban
   0.2 to 0.4: Grassland, sparse vegetation
   0.4 to 0.8: Healthy vegetation, crops, forests
   0.8 to 1  : Very dense/healthy vegetation
```

**Real-world examples:**
- "Farmers use NDVI to identify stressed crops before visible symptoms appear"
- "Ecologists track forest health and regrowth after fire"
- "Urban planners measure green space accessibility"

**Live Demo: NDVI calculation (15 min)**

```python
# 1. Extract Red and NIR bands
# Sentinel-2: Band 4 = Red (index 3), Band 8 = NIR (index 7)
# Note: Python uses 0-indexing!

red_before = before_clipped[3].astype(float)
nir_before = before_clipped[7].astype(float)

print(f"Red band shape: {red_before.shape}")
print(f"NIR band shape: {nir_before.shape}")
```

**Critical step - handling nodata:**

```python
# 2. Replace nodata values with NaN
nodata_val = before_meta['nodata']

if nodata_val is not None:
    red_before = np.where(red_before == nodata_val, np.nan, red_before)
    nir_before = np.where(nir_before == nodata_val, np.nan, nir_before)

print(f"NaN pixels: {np.sum(np.isnan(red_before))}")
```

**Emphasize:** "This step is CRUCIAL. If you don't handle nodata, you'll get weird artifacts in your calculations. Nodata values like -9999 or 0 would contaminate the math."

```python
# 3. Calculate NDVI
# Add tiny epsilon to denominator to avoid division by zero
ndvi_before = (nir_before - red_before) / (nir_before + red_before + 1e-8)

# Clean up any remaining invalid values
ndvi_before = np.where(np.isfinite(ndvi_before), ndvi_before, np.nan)

print(f"NDVI range: {np.nanmin(ndvi_before):.3f} to {np.nanmax(ndvi_before):.3f}")
print(f"Mean NDVI: {np.nanmean(ndvi_before):.3f}")
```

**Explanation:**
- "The formula is simple algebra, but the data cleaning (nodata handling) is where bugs happen"
- "`np.isfinite()` catches any remaining NaN, inf, or -inf values"
- "Mean NDVI around 0.3-0.5 suggests moderate vegetation; 0.6-0.8 indicates dense forest"

```python
# 4. Visualize with appropriate colormap
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Red band (for comparison)
axes[0].imshow(red_before, cmap='gray')
axes[0].set_title('Red Band (Before)')
axes[0].axis('off')

# NDVI with green color scheme
im = axes[1].imshow(ndvi_before, cmap='RdYlGn', vmin=-0.2, vmax=0.8)
axes[1].set_title('NDVI (Before)')
axes[1].axis('off')

plt.colorbar(im, ax=axes[1], label='NDVI', shrink=0.8)
plt.tight_layout()
plt.show()
```

**Pause for interpretation:**
- "What do you see in the NDVI map?"
- Point out features: "Green areas = vegetation, yellow/red = urban or bare soil, brown/red = water"
- "Notice how NDVI makes vegetation patterns much clearer than the raw red band"

**Student practice (10 min):**
"Now calculate NDVI for your AFTER image:"

1. Extract Red and NIR bands from `after_clipped`
2. Handle nodata values
3. Calculate `ndvi_after`
4. Create a side-by-side visualization of `ndvi_before` and `ndvi_after`
5. Calculate summary statistics for both

**Circulate and troubleshoot:**
- Watch for students using wrong band indices (Landsat vs Sentinel confusion)
- Check for students who skip nodata handling - their maps will have artifacts
- Help interpret results: "Is there obvious change? Which areas?"

---

### Part 4: Change Detection (1:45 - 2:15, 30 minutes)

**Concept: Quantifying change (3 min)**

"Visual comparison is great, but we need numbers. How much vegetation was lost? Where are the hotspots?"

"Change detection is simply: `after - before`"
- Positive values = increase (greening, regrowth)
- Negative values = decrease (deforestation, drought)
- Values near zero = stable

**Live Demo: Change detection workflow (20 min)**

```python
# 1. Calculate difference
ndvi_change = ndvi_after - ndvi_before

print(f"Mean change: {np.nanmean(ndvi_change):.4f}")
print(f"Std deviation: {np.nanstd(ndvi_change):.4f}")
print(f"Min: {np.nanmin(ndvi_change):.4f}, Max: {np.nanmax(ndvi_change):.4f}")
```

**Interpretation moment:**
- "Mean change of -0.05 would suggest overall vegetation loss"
- "Mean change of +0.02 would suggest slight greening"
- "High std deviation means spatially variable change - some areas gain, some lose"

```python
# 2. Visualize with diverging colormap
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

axes[0].imshow(ndvi_before, cmap='RdYlGn', vmin=-0.2, vmax=0.8)
axes[0].set_title('NDVI Before', fontsize=14)
axes[0].axis('off')

axes[1].imshow(ndvi_after, cmap='RdYlGn', vmin=-0.2, vmax=0.8)
axes[1].set_title('NDVI After', fontsize=14)
axes[1].axis('off')

# KEY: Use symmetric vmin/vmax for change maps
im = axes[2].imshow(ndvi_change, cmap='RdYlGn', vmin=-0.3, vmax=0.3)
axes[2].set_title('NDVI Change (After - Before)', fontsize=14)
axes[2].axis('off')

plt.colorbar(im, ax=axes[2], label='NDVI Change', shrink=0.8)
plt.tight_layout()
plt.show()
```

**Teaching point - colormap choice:**
- "For change maps, ALWAYS use a diverging colormap (red-yellow-green or red-white-blue)"
- "ALWAYS center on zero with symmetric bounds (`vmin=-0.3, vmax=0.3`)"
- "This ensures red = loss, green = gain, yellow/white = no change"

```python
# 3. Classify change into categories
change_classes = np.full(ndvi_change.shape, -9999, dtype=np.int8)

change_classes[ndvi_change < -0.15] = 1         # Major loss
change_classes[(ndvi_change >= -0.15) & (ndvi_change < -0.05)] = 2  # Moderate loss
change_classes[(ndvi_change >= -0.05) & (ndvi_change <= 0.05)] = 3  # No change
change_classes[(ndvi_change > 0.05) & (ndvi_change <= 0.15)] = 4    # Moderate gain
change_classes[ndvi_change > 0.15] = 5          # Major gain
change_classes[~np.isfinite(ndvi_change)] = -9999  # Nodata

# Count pixels in each class
labels = ['Major loss', 'Moderate loss', 'No change', 'Moderate gain', 'Major gain']
counts = [(change_classes == i).sum() for i in range(1, 6)]

for label, count in zip(labels, counts):
    print(f"{label}: {count:,} pixels")
```

**Emphasize thresholds:**
- "I chose ±0.05 and ±0.15 as thresholds, but these are somewhat arbitrary"
- "Domain knowledge matters: what NDVI change is ecologically significant in your region?"
- "Seasonal variation might be ±0.1 normally, so use ±0.15 for 'real' change"

```python
# 4. Calculate area statistics
pixel_size = before_meta['transform'][0]  # meters
pixel_area_m2 = pixel_size ** 2
pixel_area_ha = pixel_area_m2 / 10000  # convert to hectares

for i, label in enumerate(labels, start=1):
    pixel_count = (change_classes == i).sum()
    area_ha = pixel_count * pixel_area_ha
    print(f"{label}: {area_ha:.2f} hectares")
```

**Real-world context:**
- "1 hectare = 100m x 100m = size of a large sports field"
- "If you found 500 ha of major vegetation loss, that's equivalent to 700 soccer fields"

```python
# 5. Create histogram to show distribution
plt.figure(figsize=(10, 6))
plt.hist(ndvi_change[np.isfinite(ndvi_change)].flatten(),
         bins=50, color='steelblue', edgecolor='black', alpha=0.7)
plt.axvline(0, color='red', linestyle='--', linewidth=2, label='No change')
plt.axvline(np.nanmean(ndvi_change), color='orange', linestyle='--',
            linewidth=2, label=f'Mean = {np.nanmean(ndvi_change):.3f}')
plt.xlabel('NDVI Change', fontsize=12)
plt.ylabel('Pixel Count', fontsize=12)
plt.title('Distribution of NDVI Change', fontsize=14)
plt.legend()
plt.grid(alpha=0.3)
plt.show()
```

**Interpretation:**
- "A bell curve centered near zero suggests mostly stable vegetation with some change"
- "A skewed distribution (long tail to left) suggests widespread loss events"
- "Bimodal distribution might indicate two distinct processes (e.g., urban growth AND agricultural expansion)"

**Student practice (7 min):**
"Calculate change statistics for your own data:"
1. Compute `ndvi_change`
2. Create the 3-panel before/after/change visualization
3. Calculate area statistics by change class
4. Create a histogram

"Discuss with your neighbor: What's driving the change you observe?"

---

### Part 5: Zonal Statistics (2:15 - 2:45, 30 minutes)

**Why zonal stats? (3 min)**

"Pixel-level analysis is powerful, but decision-makers often want summaries by administrative units:"
- "Which suburb lost the most tree cover?"
- "Which watershed needs restoration priority?"
- "Which council area has the best vegetation trend?"

"Zonal statistics aggregate raster values within vector polygons."

**Live Demo: Zonal statistics workflow (20 min)**

```python
# 1. Load zone boundaries
zones = gpd.read_file("data/processed/week09/zones.geojson")

print(f"Number of zones: {len(zones)}")
print(f"Zone CRS: {zones.crs}")

# Reproject if needed
if zones.crs != before_meta['crs']:
    zones = zones.to_crs(before_meta['crs'])

# Preview
zones.plot(facecolor='none', edgecolor='black')
plt.title('Analysis Zones')
plt.show()
```

```python
# 2. Calculate zonal statistics
from rasterstats import zonal_stats

stats = zonal_stats(
    zones,
    ndvi_change,
    affine=before_meta['transform'],
    stats=['mean', 'median', 'min', 'max', 'std', 'count'],
    nodata=np.nan
)

# Preview results
print("Example stats for first zone:")
print(stats[0])
```

**Explanation:**
- "`affine` parameter tells rasterstats how to georeference the array"
- "`stats` list defines which summaries to calculate"
- "`nodata=np.nan` tells it to ignore NaN pixels"
- "Returns list of dictionaries, one per zone"

```python
# 3. Add results to GeoDataFrame
zones_analysis = zones.copy()

# Extract each statistic into a column
for stat in ['mean', 'median', 'min', 'max', 'std', 'count']:
    zones_analysis[f'ndvi_{stat}'] = [s[stat] for s in stats]

# Preview
zones_analysis[['name', 'ndvi_mean', 'ndvi_count']].head()
```

```python
# 4. Filter out zones with insufficient data
# Rule of thumb: need at least 100 pixels for reliable statistics
zones_valid = zones_analysis[zones_analysis['ndvi_count'] > 100].copy()

print(f"Zones with sufficient data: {len(zones_valid)} / {len(zones_analysis)}")
```

**Teaching point:**
- "Small zones or zones mostly outside your raster extent will have low pixel counts"
- "Stats from 5 pixels aren't meaningful - filter them out"

```python
# 5. Identify hotspots
zones_sorted = zones_valid.sort_values('ndvi_mean')

print("Top 5 zones with VEGETATION LOSS:")
print(zones_sorted[['name', 'ndvi_mean', 'ndvi_std']].head())

print("\nTop 5 zones with VEGETATION GAIN:")
print(zones_sorted[['name', 'ndvi_mean', 'ndvi_std']].tail())
```

```python
# 6. Visualize on map
fig, ax = plt.subplots(1, 1, figsize=(12, 10))

zones_valid.plot(
    column='ndvi_mean',
    cmap='RdYlGn',
    legend=True,
    ax=ax,
    edgecolor='black',
    linewidth=0.5,
    vmin=-0.2,
    vmax=0.2,
    legend_kwds={'label': 'Mean NDVI Change', 'shrink': 0.8}
)

ax.set_title('Mean NDVI Change by Zone', fontsize=16)
ax.set_axis_off()
plt.tight_layout()
plt.show()
```

**Interpretation activity:**
- "Look at the map - are loss areas clustered or scattered?"
- "Does the pattern match known development or events?"
- "Which zones would you prioritize for further investigation?"

```python
# 7. Create summary bar chart
fig, ax = plt.subplots(figsize=(10, 8))

# Combine top 5 loss and top 5 gain
top_loss = zones_sorted.head(5)
top_gain = zones_sorted.tail(5)
combined = pd.concat([top_loss, top_gain])

# Color bars by direction of change
colors = ['red' if x < 0 else 'green' for x in combined['ndvi_mean']]

ax.barh(combined['name'], combined['ndvi_mean'], color=colors, alpha=0.7)
ax.axvline(0, color='black', linewidth=1)
ax.set_xlabel('Mean NDVI Change', fontsize=12)
ax.set_title('Top 5 Loss and Gain Zones', fontsize=14)
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.show()
```

**Student practice (7 min):**
"Run zonal statistics on your own data:"
1. Load your zone boundaries
2. Calculate zonal stats for `ndvi_change`
3. Filter to zones with >100 pixels
4. Create the choropleth map
5. Identify the top 3 loss and gain zones

---

### Part 6: Export & Wrap-up (2:45 - 3:00, 15 minutes)

**Exporting results (8 min live demo)**

```python
# 1. Export change raster
change_meta = before_meta.copy()
change_meta.update({
    'count': 1,
    'dtype': 'float32',
    'nodata': -9999
})

# Replace NaN with nodata value for export
ndvi_change_export = np.where(np.isfinite(ndvi_change), ndvi_change, -9999)

with rasterio.open('data/processed/week09/ndvi_change.tif', 'w', **change_meta) as dst:
    dst.write(ndvi_change_export.astype('float32'), 1)

print("✅ Exported: ndvi_change.tif")
```

```python
# 2. Export zonal statistics
# CSV for spreadsheet analysis
zones_valid[['name', 'ndvi_mean', 'ndvi_median', 'ndvi_std', 'ndvi_count']].to_csv(
    'exports/week09_zonal_statistics.csv',
    index=False
)

# GeoPackage for GIS software
zones_valid.to_file(
    'data/processed/week09/zones_change.gpkg',
    driver='GPKG',
    layer='ndvi_change'
)

print("✅ Exported: zonal_statistics.csv and zones_change.gpkg")
```

```python
# 3. Export comprehensive figure
fig = plt.figure(figsize=(16, 10))

ax1 = plt.subplot(2, 2, 1)
ax1.imshow(ndvi_before, cmap='RdYlGn', vmin=-0.2, vmax=0.8)
ax1.set_title('NDVI Before', fontsize=14)
ax1.axis('off')

ax2 = plt.subplot(2, 2, 2)
ax2.imshow(ndvi_after, cmap='RdYlGn', vmin=-0.2, vmax=0.8)
ax2.set_title('NDVI After', fontsize=14)
ax2.axis('off')

ax3 = plt.subplot(2, 2, 3)
im = ax3.imshow(ndvi_change, cmap='RdYlGn', vmin=-0.3, vmax=0.3)
ax3.set_title('NDVI Change', fontsize=14)
ax3.axis('off')
plt.colorbar(im, ax=ax3, shrink=0.8)

ax4 = plt.subplot(2, 2, 4)
zones_valid.plot(column='ndvi_mean', cmap='RdYlGn', ax=ax4,
                 legend=True, edgecolor='black', linewidth=0.5,
                 vmin=-0.2, vmax=0.2)
ax4.set_title('Zonal Mean Change', fontsize=14)
ax4.set_axis_off()

plt.suptitle('NDVI Change Detection Analysis', fontsize=18, y=0.98)
plt.tight_layout()
plt.savefig('exports/week09_comprehensive_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

print("✅ Exported: week09_comprehensive_analysis.png")
```

**Session debrief (5 min)**

Ask students:
- "What was the most challenging part today?"
- "What was most surprising about your results?"
- "How would you explain your findings to a non-technical audience?"

**Key takeaways to emphasize:**
1. "Rasterio + NumPy gives you full control over satellite data processing"
2. "Data cleaning (nodata handling, CRS alignment) is 50% of the work"
3. "Zonal statistics bridge raster analysis and vector decision-making"
4. "This workflow is fully reproducible - you can rerun it on any region or time period"

**Preview Week 10 (2 min):**
- "Next week: Network analysis in Python (optimal routing, service areas)"
- "We'll combine your zonal stats from today with accessibility metrics"
- "Question: Which suburbs have poor vegetation AND poor transport access?"

---

## Key Concepts to Emphasize

### 1. Raster vs Vector Thinking

**Vector (previous weeks):**
- Discrete objects (points, lines, polygons)
- Attributes attached to geometries
- Topology matters (intersections, adjacency)

**Raster (this week):**
- Continuous grids of pixels
- Each cell has numeric value(s)
- Spatial relationships through array operations

**Key message:** "Rasters are excellent for continuous phenomena (temperature, elevation, reflectance). Vectors are better for discrete features (roads, buildings, boundaries). You often combine both: raster analysis with vector summaries."

---

### 2. The Nodata Problem

**Why it matters:**
- Satellite imagery has gaps: clouds, shadows, sensor issues, scene edges
- Nodata pixels coded as special values: -9999, 0, 65535, or NaN
- If not handled, nodata contaminates calculations

**Best practices:**
1. Check metadata for nodata value: `src.nodata`
2. Replace with NaN before calculations: `np.where(array == nodata, np.nan, array)`
3. Use NaN-aware functions: `np.nanmean()`, `np.nanstd()`, `np.isfinite()`
4. Convert back to nodata value for export

**Common student mistake:** Forgetting nodata handling, then seeing strange artifacts (extreme values, weird colors)

---

### 3. Band Math Fundamentals

**Core concept:**
- Satellite bands are just arrays of numbers
- Band math = algebraic operations on arrays
- Different band combinations reveal different information

**Examples beyond NDVI:**

| Index | Formula | Purpose |
|-------|---------|---------|
| NDVI | (NIR - Red) / (NIR + Red) | Vegetation health |
| NDWI | (Green - NIR) / (Green + NIR) | Water detection |
| NDBI | (SWIR - NIR) / (SWIR + NIR) | Urban/built-up areas |
| NBR | (NIR - SWIR) / (NIR + SWIR) | Burn severity |

**Key message:** "Once you understand the workflow for NDVI, you can calculate ANY spectral index by changing the band combination."

---

### 4. Change Detection Logic

**Simple but powerful:**
- `Change = After - Before`
- Positive = increase
- Negative = decrease
- Magnitude = size of change

**Critical decisions:**
1. **Threshold selection:** What change is "significant"?
   - Statistical: ±2 standard deviations
   - Domain-based: ±0.1 NDVI is typical for real vegetation change
   - Context-specific: Seasonality, climate, ecosystem type

2. **Time period:**
   - Same season across years (e.g., summer 2019 vs summer 2024)
   - Avoids phenological variation (seasonal greening/browning)

3. **Validation:**
   - Ground truth data
   - Visual comparison with high-res imagery (Google Earth)
   - Cross-reference with known events (fires, logging permits)

**Key message:** "Change detection is easy to calculate but hard to interpret correctly. Context is everything."

---

### 5. Zonal Statistics as Bridge to Decision-Making

**Why it matters:**
- Pixel-level data is overwhelming (millions of values)
- Decision-makers think in jurisdictional units (suburbs, councils, watersheds)
- Zonal stats provide actionable summaries

**Best practices:**
1. **Filter low-pixel zones:** Need sufficient sample size for statistics
2. **Choose appropriate statistic:**
   - Mean: Overall trend
   - Median: Robust to outliers
   - Std: Variability within zone
   - Min/Max: Identify hotspots
3. **Report uncertainty:** Include pixel count and std deviation
4. **Combine with other attributes:** Zone population, area, land use

**Key message:** "Zonal statistics turn scientific analysis into policy-relevant information."

---

## Live Demo Script Summary

**Complete workflow (for reference):**

```python
# ===== SETUP =====
import rasterio
from rasterio.mask import mask
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
from rasterstats import zonal_stats
from pathlib import Path

DATA = Path("data/processed/week09")

# ===== 1. LOAD & INSPECT =====
with rasterio.open(DATA / "sentinel_before.tif") as src:
    print(f"Bands: {src.count}, Size: {src.width}x{src.height}")
    print(f"CRS: {src.crs}, Resolution: {src.res}")

# ===== 2. CLIP TO AOI =====
aoi = gpd.read_file(DATA / "aoi.geojson")

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

before, before_meta = clip_raster(DATA / "sentinel_before.tif", aoi)
after, after_meta = clip_raster(DATA / "sentinel_after.tif", aoi)

# ===== 3. CALCULATE NDVI =====
def calculate_ndvi(clipped_array, nodata_value):
    red = clipped_array[3].astype(float)  # Sentinel-2 Band 4
    nir = clipped_array[7].astype(float)  # Sentinel-2 Band 8

    # Handle nodata
    red = np.where(red == nodata_value, np.nan, red)
    nir = np.where(nir == nodata_value, np.nan, nir)

    # Calculate
    ndvi = (nir - red) / (nir + red + 1e-8)
    ndvi = np.where(np.isfinite(ndvi), ndvi, np.nan)

    return ndvi

ndvi_before = calculate_ndvi(before, before_meta['nodata'])
ndvi_after = calculate_ndvi(after, after_meta['nodata'])

# ===== 4. DETECT CHANGE =====
ndvi_change = ndvi_after - ndvi_before

print(f"Mean change: {np.nanmean(ndvi_change):.4f}")

# ===== 5. VISUALIZE =====
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
axes[0].imshow(ndvi_before, cmap='RdYlGn', vmin=-0.2, vmax=0.8)
axes[0].set_title('Before')
axes[1].imshow(ndvi_after, cmap='RdYlGn', vmin=-0.2, vmax=0.8)
axes[1].set_title('After')
axes[2].imshow(ndvi_change, cmap='RdYlGn', vmin=-0.3, vmax=0.3)
axes[2].set_title('Change')
plt.show()

# ===== 6. ZONAL STATISTICS =====
zones = gpd.read_file(DATA / "zones.geojson").to_crs(before_meta['crs'])

stats = zonal_stats(zones, ndvi_change, affine=before_meta['transform'],
                    stats=['mean', 'count'], nodata=np.nan)

zones['ndvi_mean'] = [s['mean'] for s in stats]
zones['ndvi_count'] = [s['count'] for s in stats]

zones_valid = zones[zones['ndvi_count'] > 100]
zones_valid.plot(column='ndvi_mean', cmap='RdYlGn', legend=True)
plt.show()

# ===== 7. EXPORT =====
zones_valid.to_file(DATA / "zones_change.gpkg", driver='GPKG')
print("✅ Analysis complete!")
```

---

## Discussion Prompts

Use these throughout the session to deepen understanding:

### After Raster Basics (Part 1):
- **Q:** "What are the tradeoffs between high-resolution (1m) and moderate-resolution (10m) imagery?"
  - **Expected answers:** Resolution vs coverage, file size, processing time, cost
  - **Follow-up:** "Planet Labs offers daily 3m imagery - but files are huge. Sentinel-2 is free but 10-30m. Which would you choose for monitoring a 50km² forest?"

### After NDVI Calculation (Part 3):
- **Q:** "Why might NDVI be misleading? What factors could give you a false 'vegetation loss' signal?"
  - **Expected answers:** Seasonal differences, cloud shadows, wet vs dry season, sensor calibration
  - **Key point:** "This is why same-season comparisons matter! Comparing summer to winter would show 'loss' even with no actual change."

### After Change Detection (Part 4):
- **Q:** "If you found 200 hectares of vegetation loss, what additional information would you need to determine if this is a problem?"
  - **Expected answers:** Land use context (e.g., planned clearing for housing vs illegal logging), environmental regulations, replacement planting, ecosystem type
  - **Key point:** "Technical analysis answers 'what changed' and 'how much'. Human judgment answers 'is this good or bad'."

### After Zonal Statistics (Part 5):
- **Q:** "You find that Zone A has mean change of -0.08 (loss) and Zone B has -0.12 (worse loss). But Zone B has high std deviation (0.15) while Zone A has low (0.03). What might explain this?"
  - **Expected answers:** Zone B might have mixed change (some areas gain, some lose heavily), Zone A has uniform loss
  - **Key point:** "Always look at variability, not just mean. High variability suggests localized processes."

---

## Real-World Remote Sensing Applications

Share these examples to inspire students:

### 1. Amazon Rainforest Monitoring
- **Organization:** INPE (Brazilian Space Agency)
- **Method:** Landsat + Sentinel-2 time series
- **Impact:** DETER system provides alerts of deforestation within 1-2 weeks
- **Data:** Public dashboards showing annual deforestation rates
- **Link students to:** Global Forest Watch (globalforestwatch.org)

### 2. Australian Bushfire Assessment
- **Event:** 2019-2020 Black Summer fires
- **Method:** NBR (Normalized Burn Ratio) from Sentinel-2
- **Output:** Burn severity maps showing 10+ million hectares affected
- **Application:** Recovery prioritization, insurance claims, ecological research
- **Real example:** Geoscience Australia's burn mapping

### 3. Urban Heat Island Monitoring
- **Cities:** Los Angeles, Phoenix, Singapore
- **Data:** Landsat thermal bands (30m resolution)
- **Method:** Land Surface Temperature + NDVI correlation
- **Finding:** Areas with <20% tree cover are 4-7°C hotter
- **Application:** Urban planning for climate adaptation, tree planting programs

### 4. Agricultural Drought Monitoring
- **Scale:** Continental (Australia, US)
- **Data:** MODIS NDVI time series (250m, daily)
- **Method:** Compare current NDVI to 20-year average
- **Users:** Farmers for irrigation decisions, governments for disaster declarations
- **Example:** USDA's Crop Condition and Soil Moisture Analytics

### 5. Wetland Change Detection
- **Example:** Kakadu National Park, Australia
- **Method:** NDWI (water index) + NDVI
- **Time scale:** 1990-2024 (30+ years)
- **Findings:** Saltwater intrusion, changing flood patterns
- **Impact:** Informed management of Ramsar-listed wetlands

### 6. Disaster Response
- **Event:** 2023 Turkey-Syria earthquake
- **Data:** Synthetic Aperture Radar (SAR) from Sentinel-1
- **Speed:** Damage maps within 12 hours
- **Users:** UN, Red Cross for rescue prioritization
- **Technique:** Change detection pre/post event

### 7. Glacier Retreat Monitoring
- **Location:** Himalayan glaciers, Antarctic ice shelves
- **Data:** Landsat archive (1970s-present)
- **Method:** Edge detection + NDSI (snow index)
- **Impact:** Climate change evidence, water security assessments

**Facilitate discussion:**
- "Which of these applications resonates with your interests?"
- "What environmental changes in YOUR community could be monitored with these techniques?"
- "What are the ethical considerations of satellite surveillance?"

---

## Common Student Issues & Solutions

### Issue 1: "I can't load my raster - FileNotFoundError"

**Causes:**
- Incorrect file path (relative vs absolute)
- File not uploaded (Colab users)
- Typo in filename

**Debugging steps:**
```python
# 1. Check current working directory
from pathlib import Path
print(Path.cwd())

# 2. List files in data directory
print(list(Path("data/processed/week09").glob("*.tif")))

# 3. Use absolute path
raster_path = Path("/Users/username/intro-gis/data/processed/week09/sentinel_before.tif")
```

**Prevention:** Teach students to use `Path` objects consistently and check paths before proceeding.

---

### Issue 2: "MemoryError when loading raster"

**Causes:**
- Raster file too large (multi-GB scenes)
- Student loaded all bands at once
- Not enough RAM (common on older laptops)

**Solutions:**

**Option A: Read specific bands only**
```python
with rasterio.open(raster_path) as src:
    # Don't read all bands
    red = src.read(4)
    nir = src.read(8)
    # Not: all_bands = src.read()  # Memory hog!
```

**Option B: Use windowed reading**
```python
from rasterio.windows import Window

# Read a subset
window = Window(0, 0, 1000, 1000)  # Read first 1000x1000 pixels
with rasterio.open(raster_path) as src:
    subset = src.read(4, window=window)
```

**Option C: Clip FIRST, then analyze**
- Emphasize: "Always clip to AOI before doing anything else"

**Prevention:** Provide pre-clipped data for students, or demonstrate windowed reading early.

---

### Issue 3: "My NDVI values are all 0 or NaN"

**Causes:**
- Wrong band indices (using 1-indexing instead of 0-indexing)
- Nodata values not handled
- Integer division instead of float

**Diagnosis:**
```python
print(f"Red min/max: {red.min()} / {red.max()}")
print(f"NIR min/max: {nir.min()} / {nir.max()}")
print(f"Red dtype: {red.dtype}")
print(f"Number of NaN: {np.isnan(red).sum()}")
```

**Solutions:**
- Check band numbers match sensor (Sentinel-2 vs Landsat)
- Convert to float BEFORE division: `.astype(float)`
- Verify nodata handling

---

### Issue 4: "CRS mismatch error when clipping"

**Error message:** `ValueError: Input shapes do not overlap raster`

**Cause:** Vector and raster in different CRS

**Solution:**
```python
# Check CRS
with rasterio.open(raster_path) as src:
    print(f"Raster CRS: {src.crs}")
print(f"Vector CRS: {aoi.crs}")

# Reproject vector to match raster
aoi_reprojected = aoi.to_crs(src.crs)
```

**Teaching point:** "ALWAYS reproject vector to raster, not raster to vector. Raster reprojection is slow and lossy."

---

### Issue 5: "My change map shows weird artifacts/stripes"

**Causes:**
- Nodata values (e.g., -9999) not masked
- Before/after images not aligned (different extents/resolutions)
- Sensor differences (Sentinel-2A vs 2B have slight calibration differences)

**Diagnosis:**
```python
# Check for extreme values
print(f"Change min/max: {np.nanmin(ndvi_change)} / {np.nanmax(ndvi_change)}")

# Check alignment
print(f"Before shape: {ndvi_before.shape}")
print(f"After shape: {ndvi_after.shape}")
```

**Solutions:**
- Mask nodata: `ndvi_change = np.where(np.isfinite(ndvi_change), ndvi_change, np.nan)`
- Verify before/after rasters have identical metadata
- Use Coregister if needed (advanced: rasterio.warp.reproject)

---

### Issue 6: "Colormap looks wrong - all one color"

**Causes:**
- vmin/vmax set incorrectly
- Using sequential colormap (e.g., 'viridis') for diverging data
- Data range doesn't match colormap bounds

**Solution:**
```python
# Check data range
print(f"NDVI range: {np.nanmin(ndvi_change)} to {np.nanmax(ndvi_change)}")

# Use appropriate colormap and bounds
plt.imshow(ndvi_change, cmap='RdYlGn', vmin=-0.3, vmax=0.3)

# For change maps: ALWAYS symmetric bounds centered on zero
```

**Teaching point:** "Colormap choice is NOT just aesthetic - it affects interpretation. Diverging colormaps for change, sequential for single-time data."

---

### Issue 7: "Zonal statistics returns None or empty results"

**Causes:**
- Zones don't overlap raster (CRS mismatch or extent mismatch)
- `affine` parameter incorrect
- All raster values are nodata within zones

**Diagnosis:**
```python
# Check overlap
print(f"Raster bounds: {before_meta['bounds']}")
print(f"Zones bounds: {zones.total_bounds}")

# Visualize together
fig, ax = plt.subplots()
plt.imshow(ndvi_change)
zones.plot(ax=ax, facecolor='none', edgecolor='red')
plt.show()
```

**Solutions:**
- Reproject zones to raster CRS
- Verify `affine=before_meta['transform']` (not 'affine')
- Check if zones actually contain valid pixels

---

### Issue 8: "Code is extremely slow"

**Causes:**
- Working with full-resolution scenes (10,000+ x 10,000+ pixels)
- Not clipping to AOI first
- Inefficient loops instead of vectorized operations

**Solutions:**
```python
# BAD: Looping over pixels
for i in range(ndvi_before.shape[0]):
    for j in range(ndvi_before.shape[1]):
        ndvi_change[i, j] = ndvi_after[i, j] - ndvi_before[i, j]  # Slow!

# GOOD: Vectorized operation
ndvi_change = ndvi_after - ndvi_before  # Fast!
```

**Prevention:** Emphasize clipping workflow and NumPy vectorization from Week 2.

---

### Issue 9: "I don't understand what my results mean"

**Cause:** Student calculated numbers correctly but lacks interpretation context

**Solution - Ask guiding questions:**
- "What NDVI values do you expect for forests vs cities?"
- "Is the change positive or negative? What does that mean?"
- "Look at a satellite image of the area in Google Earth - what do you see?"
- "What events might have caused this change?"

**Teaching strategy:** Always link numbers back to real-world phenomena. Show examples of NDVI values for different land covers.

---

## Troubleshooting Quick Reference

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| FileNotFoundError | Wrong path | Check `Path.cwd()`, use absolute paths |
| MemoryError | File too large | Clip first, read specific bands only |
| All NaN values | Nodata not handled | `np.where(arr == nodata, np.nan, arr)` |
| CRS error | Vector/raster mismatch | Reproject vector: `aoi.to_crs(src.crs)` |
| Weird artifacts | Nodata contamination | Mask with `np.isfinite()` |
| Wrong colors | Bad colormap choice | Use 'RdYlGn' for change, symmetric vmin/vmax |
| Empty zonal stats | CRS/extent mismatch | Reproject zones, check overlap |
| Extremely slow | Not vectorized | Use NumPy operations, not loops |

---

## Wrap-up & Preview

### Session Summary (2 min)

"Today you learned the complete satellite change detection workflow:"
1. Load and inspect raster metadata
2. Clip to area of interest
3. Calculate spectral indices (NDVI)
4. Detect change through simple subtraction
5. Aggregate with zonal statistics
6. Export results for reporting

"This is a professional workflow used by environmental agencies worldwide. You can now apply it to any region, any timeframe, any environmental question."

### Assignment Expectations

Students should submit:
- [ ] Jupyter notebook with all cells executed
- [ ] NDVI change raster (GeoTIFF)
- [ ] Zonal statistics (CSV + GeoPackage)
- [ ] Comprehensive analysis figure (PNG)
- [ ] Metadata file documenting their analysis
- [ ] Reflection (250-300 words)

**Grading criteria:**
- Code runs without errors (30%)
- Nodata handled correctly (15%)
- Appropriate visualizations (20%)
- Zonal statistics calculated (15%)
- Interpretation demonstrates understanding (20%)

### Preview: Week 10 - Network Analysis

"Next week shifts to network analysis in Python:"
- "Calculating optimal routes with NetworkX"
- "Service area analysis (isochrones)"
- "Accessibility metrics"

"We'll combine your vegetation analysis from today with transport networks:"
- "Which neighborhoods have poor green space AND poor transit access?"
- "This is environmental justice analysis - identifying disadvantaged communities"

**What to prepare:**
- Review Week 6 QGIS network analysis concepts
- Think about accessibility questions for your city
- No new data downloads required - we'll use OSM

---

## Additional Resources for Facilitators

### Recommended Pre-Session Reading

- [Rasterio Documentation](https://rasterio.readthedocs.io/) - Focus on "Reading datasets" and "Masking"
- [ESA Sentinel-2 User Guide](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-2-msi) - Band descriptions
- [USGS Landsat Band Designations](https://www.usgs.gov/faqs/what-are-band-designations-landsat-satellites)

### Example Datasets

**Good study areas for change detection:**

1. **Urban expansion:**
   - Dubai, UAE (dramatic growth)
   - Phoenix, Arizona (sprawl into desert)
   - Lagos, Nigeria (rapid development)

2. **Deforestation:**
   - Amazon (Rondônia, Brazil)
   - Borneo, Indonesia (palm oil plantations)
   - Tasmania, Australia (forestry)

3. **Natural disasters:**
   - California fires (2018, 2020, 2021)
   - Australian Black Summer fires (2019-2020)
   - Hurricane damage (e.g., Puerto Rico 2017)

4. **Seasonal change (for testing):**
   - Agricultural areas (planting/harvest cycles)
   - Deciduous forests (summer vs winter)

### Data Sources

| Source | Satellites | Resolution | Access |
|--------|-----------|------------|--------|
| [Copernicus Open Access Hub](https://scihub.copernicus.eu/) | Sentinel-1, 2, 3 | 10-60m | Free, registration required |
| [USGS EarthExplorer](https://earthexplorer.usgs.gov/) | Landsat 5, 7, 8, 9 | 15-30m | Free, registration required |
| [Google Earth Engine](https://earthengine.google.com/) | All major satellites | Varies | Free, script-based |
| [AWS Open Data](https://registry.opendata.aws/sentinel-2/) | Sentinel-2 | 10-60m | Free, requires AWS account |

### Troubleshooting Support

**Common installation issues:**

**Rasterio won't install:**
```bash
# Option 1: Use conda (recommended)
conda install -c conda-forge rasterio

# Option 2: Use pip with binary wheels
pip install rasterio --find-links=https://girder.github.io/large_image_wheels
```

**GDAL errors:**
- Rasterio depends on GDAL (Geospatial Data Abstraction Library)
- GDAL installation can be tricky - conda usually handles it better than pip
- Colab has GDAL pre-installed

**Rasterstats issues:**
```bash
pip install rasterstats
# If shapely/fiona errors occur:
conda install -c conda-forge rasterstats
```

---

## Timing Flexibility Guide

**If running ahead of schedule (+15-20 min):**
- Add optional activity: Calculate EVI or NDWI
- Demonstrate creating RGB composite from satellite bands
- Show advanced visualization (basemap overlay with contextily)
- Discuss sensor differences (Sentinel-2 vs Landsat comparison)

**If running behind schedule (-15-20 min):**
- Skip detailed metadata inspection (just show briefly)
- Provide pre-clipped rasters (skip clipping demo)
- Skip histogram visualization
- Reduce student practice time (5 min instead of 10 min)
- Combine export demos (show but don't execute)

**Critical sections (cannot skip):**
- Nodata handling explanation (Part 1)
- NDVI calculation walkthrough (Part 3)
- Change detection workflow (Part 4)
- Zonal statistics concept (Part 5)

---

## Accessibility Considerations

- **Visual impairments:** Ensure colorblind-friendly palettes (avoid red-green for colorblind students - use viridis alternatives)
- **Screen readers:** Describe visualizations verbally ("The map shows green areas indicating vegetation gain in the northeast, red areas showing loss in the southwest")
- **Motor impairments:** Allow extra time for coding, provide code snippets to copy-paste
- **Learning disabilities:** Provide written summary of key steps, allow note-taking

---

## Engagement Strategies

### For quiet/shy students:
- Use polls: "Hands up if you've used NDVI before"
- Pair programming: "Work with your neighbor for the next 10 minutes"
- Anonymous questions: "Type questions in the chat"

### For advanced students:
- Challenge questions: "Try calculating EVI instead of NDVI"
- Extensions: "Can you automate this for multiple time periods?"
- Discussion facilitator: "Explain to your neighbor why we use NIR-Red"

### For struggling students:
- Frequent check-ins: "Let me know if you're stuck - raise hand or message me"
- Peer support: "If you finish early, help someone nearby"
- Simplified data: Provide smaller, pre-processed datasets

---

**End of Facilitator Notes**

*Remember: The goal is not just technical proficiency, but environmental insight. Help students see the story in the data.*
