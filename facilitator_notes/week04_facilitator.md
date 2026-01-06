# Week 4 Facilitator Notes · Raster Data & Terrain Analysis

## Session Overview

**Duration:** 2-3 hours (including lecture, demo, and lab work time)

**Learning Objectives:**
By the end of this session, students will be able to:
1. Explain the difference between raster and vector data models and when to use each
2. Distinguish between DEM, DSM, and DTM and select appropriate elevation products
3. Import, reproject, and clip digital elevation models to a study area
4. Generate terrain derivatives (hillshade, slope) and interpret their meaning
5. Calculate NDVI from multispectral imagery using Raster Calculator (optional)
6. Combine raster outputs with vector boundaries using zonal statistics
7. Communicate terrain-related insights through professional map layouts

**Materials Needed:**
- QGIS 3.x installed on all student machines
- Sample DEM tiles (ELVIS for Australian regions, SRTM globally) pre-downloaded
- Week 3 boundary layers (SA2/LGA) from previous session
- Projector for live demonstrations
- Backup USB drives with all datasets in case of download issues
- Example hillshade/slope outputs to show as reference

**Key Data:**
- DEM tiles (SRTM 30m or ELVIS 5m)
- SA2/LGA boundary shapefiles from Week 3
- Optional: SEIFA or other socio-economic indicators from Week 3
- Optional: Sentinel-2 or Landsat imagery for NDVI calculation (multispectral bands)

---

## Before Class Checklist

### Data Preparation
- [ ] Download DEM tiles for the study region(s) your students are using
- [ ] Test that DEM files open correctly in QGIS without corruption
- [ ] Verify DEM CRS and resolution match expectations (SRTM typically WGS84/EPSG:4326)
- [ ] Have boundary layers from Week 3 ready for clipping demonstrations
- [ ] Pre-process one complete workflow (DEM → hillshade → slope → zonal stats) as reference

### Technical Setup
- [ ] Test hillshade tool with default parameters (azimuth 315°, altitude 45°)
- [ ] Test slope calculation tool (verify output in degrees vs percent)
- [ ] Ensure Raster menu items are all available (no plugin dependencies)
- [ ] Check that Clip Raster by Mask Layer tool is accessible (Processing Toolbox)
- [ ] Verify zonal statistics tool works with sample data
- [ ] Test that large raster operations complete within reasonable time on lab computers

### Teaching Materials
- [ ] Load Week 4 lecture slides with DEM/DSM/DTM comparison diagrams
- [ ] Prepare visual examples showing raster grid structure
- [ ] Have real-world terrain analysis examples ready (flood maps, landslide risk, viewsheds)
- [ ] Create a simple diagram showing how slope is calculated from neighboring cells
- [ ] Prepare troubleshooting reference sheet with common CRS/NoData issues

### Classroom Environment
- [ ] Ensure all student computers have sufficient disk space (DEMs can be 500MB+)
- [ ] Test internet connectivity if students will download data during class
- [ ] Have backup workflow on USB in case of network issues
- [ ] Check that projector display shows QGIS interface clearly (especially layer panel)

---

## Session Flow

### 1. Introduction & Theory (20-25 minutes)

**Welcome & Context (5 min)**
- Recap Week 3: "Last week you mapped boundaries and joined socio-economic data. This week we add the physical landscape."
- Show compelling example: "Flood risk isn't just about proximity to water—elevation matters. Development suitability depends on slope. This week you'll analyze terrain."

**Raster vs Vector (10 min)**
- **Visual demonstration:** Open QGIS with both a vector boundary and a raster DEM
  - Zoom in progressively on the vector—stays crisp
  - Zoom in on the raster—see individual pixels appear

- **Explain the grid concept:**
  ```
  Vector (boundaries):          Raster (elevation):
  ┌─────────────┐              ░░░░░░░░░░░░░░░░
  │             │              ░░▓▓▓▓▓▓▓▓░░░░░░
  │   Polygon   │              ░░▓▓████▓▓░░░░░░
  │             │              ░░▓▓████▓▓▓▓░░░░
  └─────────────┘              ░░░░▓▓▓▓▓▓▓▓░░░░
  (precise boundaries)          (each cell = one value)
  ```

- **When to use each:**
  - Vector: Discrete features with clear boundaries (roads, parcels, admin areas)
  - Raster: Continuous surfaces (elevation, temperature, rainfall, satellite images)

**DEM/DSM/DTM Differences (5 min)**
- **DEM (Digital Elevation Model):** General term, often means bare earth
- **DTM (Digital Terrain Model):** Ground surface with natural features
- **DSM (Digital Surface Model):** Top of everything (buildings, trees, infrastructure)

**Visual analogy:** "Imagine flying over a city in winter after heavy snow. The DSM is what you see—snowy rooftops and tree canopies. The DTM is what you'd see if you removed all the snow and vegetation to show the natural ground."

**Real-world implications:**
- Flood modeling: Use DTM/DEM (water flows over ground, not rooftops)
- Viewshed analysis: Use DSM (buildings and trees block views)
- Landslide risk: Use DTM (natural terrain stability)

**Resolution & Trade-offs (5 min)**
- **Show examples:**
  - 5m ELVIS: See individual houses, driveways
  - 30m SRTM: See general terrain patterns, neighborhoods
  - 90m SRTM: Regional patterns only

- **Trade-off triangle:**
  ```
       Detail
         /\
        /  \
       /    \
      /______\
  Speed      File Size
  ```
  Higher resolution = more detail, slower processing, larger files

- **Emphasize:** "Choose resolution based on your question. Analyzing regional flood patterns? 30m is fine. Planning a bike path? You need 5m or better."

---

### 2. Live Demonstration (40-45 minutes)

**Setup (2 min)**
- Open QGIS with a new project
- Set project CRS to a relevant projected coordinate system (e.g., EPSG:7856 for Australia)
- "I'm starting fresh so you can see every step. In practice, you'd continue from your Week 3 project."

**Activity 1: Load and Inspect DEM (8 min)**

1. **Load the raster:**
   - `Layer > Add Layer > Add Raster Layer`
   - Navigate to DEM file (e.g., `srtm_tile_s38_e144.tif`)
   - Click Add

2. **Initial appearance issue:**
   - DEM likely appears as solid gray or washed out
   - **Teaching moment:** "This is normal! The symbology defaults don't know the elevation range."

3. **Fix symbology:**
   - Right-click layer → Properties → Symbology
   - Change to "Singleband pseudocolor"
   - Set Min/Max values: Choose "Cumulative count cut" (2%-98%)
   - Select color ramp: "RdYlGn" (reversed) or "Spectral"
   - Apply and OK
   - **Narrate:** "Now we see low elevations in green, high in brown/white. This makes sense for [your region]."

4. **Inspect metadata:**
   - Properties → Information tab
   - **Call out key details:**
     - CRS: "WGS 84, EPSG:4326—that's geographic coordinates, latitude/longitude"
     - Dimensions: "3601 x 3601 pixels"
     - Pixel Size: "0.000277... degrees" (explain this is roughly 30m at this latitude)
     - Data type: "Int16" or "Float32"
     - Bands: "1" (single-band elevation data)

5. **Check elevation values:**
   - Use Identify tool (i in toolbar) and click around
   - "Clicking here shows 245 meters. Clicking on the coast shows near 0. Does this match reality?"

**Activity 2: Reproject to Projected CRS (7 min)**

1. **Explain the why:**
   - "Geographic CRS (degrees) means distances aren't equal across the map"
   - "At the equator, 1° longitude ≈ 111km. At 60° latitude, it's only 55km"
   - "Slope calculation needs real distances in meters, not degrees"

2. **Reproject:**
   - `Raster > Projections > Warp (Reproject)`
   - Input layer: [your DEM]
   - Target CRS: EPSG:7856 (or appropriate projected CRS)
   - Resampling method: Bilinear
     - **Explain:** "Bilinear smooths values between pixels. Nearest neighbor preserves exact values but looks blocky."
   - Output file: Save to `data/processed/week04/dem_projected.tif`
   - Run

3. **Verify:**
   - Load the reprojected DEM
   - Check Properties → Information
   - Pixel size now shows meters (e.g., "30m x 30m")
   - "Now our pixel size is in real-world units we can measure."

**Activity 3: Clip to Study Area (8 min)**

1. **Load boundary layer:**
   - Add SA2 or LGA shapefile from Week 3
   - "We'll clip the DEM to just this region to speed up processing"

2. **Verify CRS match:**
   - **Important teaching moment:** "Before clipping, check both layers are in the same CRS"
   - Show layer CRS in Properties
   - "Both are EPSG:7856? Good. Mismatch here causes empty outputs."

3. **Clip the raster:**
   - Open Processing Toolbox (Gear icon or Ctrl+Alt+T)
   - Search for "Clip raster by mask layer"
   - Input layer: dem_projected.tif
   - Mask layer: SA2/LGA boundaries
   - Check "Match the extent of the clipped raster to the extent of the mask layer"
   - Assign NoData value: -9999
   - Output: `data/processed/week04/dem_clipped.tif`
   - Run

4. **Compare file sizes:**
   - Navigate to the output folder
   - "Full tile: 50MB. Clipped: 5MB. Much faster to work with."

5. **Style the clipped DEM:**
   - Apply terrain color ramp (green → yellow → brown → white)
   - Remove original DEM layers to avoid confusion

**Activity 4: Generate Hillshade (8 min)**

1. **Explain hillshade:**
   - "Hillshade simulates shadows as if the sun is shining from a specific angle"
   - "It doesn't change elevation data—purely for visualization"
   - "Makes terrain patterns jump out: valleys, ridges, slopes"

2. **Create hillshade:**
   - `Raster > Analysis > Hillshade`
   - Elevation layer: dem_clipped.tif
   - Z factor: 1 (we're in meters already)
   - Azimuth: 315° (northwest—the sun position)
   - Vertical angle: 45°
   - Output: `data/processed/week04/hillshade.tif`
   - Run

3. **Style and layer:**
   - Hillshade appears as grayscale
   - Layer Properties → Symbology → Singleband gray
   - Adjust contrast slightly if needed
   - Move hillshade below boundary layer in Layers Panel
   - Set boundary fill to transparent, outline visible
   - "See how the hillshade shows valleys and ridges? That's pure visualization—helps readers understand the landscape."

4. **Experiment (if time):**
   - Try azimuth 90° (east): "Morning light"
   - Try azimuth 270° (west): "Evening light"
   - "Different angles reveal different features. Cartographers sometimes blend multiple hillshades."

**Activity 5: Calculate Slope (10 min)**

1. **Explain slope:**
   - "Slope measures steepness—how much elevation changes over distance"
   - "Critical for flood risk (water flows downhill), landslides (steep = unstable), accessibility (wheelchairs, roads)"
   - "Output in degrees (0-90°) or percent (0-100%+ for very steep)"

2. **Calculate slope:**
   - `Raster > Terrain Analysis > Slope`
   - Input layer: dem_clipped.tif
   - Slope expressed as: Percent
     - **Explain:** "Percent is intuitive: 10% = 10m rise over 100m horizontal. Degrees are common in geomorphology."
   - Output: `data/processed/week04/slope.tif`
   - Run

3. **Style slope:**
   - Symbology → Singleband pseudocolor
   - Color ramp: YlOrRd (yellow-orange-red)
   - Mode: Equal Interval or Quantile
   - Classes: 5-7
   - Labels: "0-5% (flat)", "5-10% (gentle)", "10-20% (moderate)", "20-30% (steep)", ">30% (very steep)"
   - Apply

4. **Interpret:**
   - Use Identify tool to click on different areas
   - "This creek valley shows 15% slope—moderate. This ridgeline is 35%—very steep."
   - "Where would you build a road? Where might landslides occur?"

5. **Common issue check:**
   - If all values show near 0 or seem wrong:
     - "This happens if CRS is still geographic (degrees). Always reproject first!"

**Activity 6: Calculate NDVI (Optional, 10 min)**

**Note:** This activity requires multispectral satellite imagery (e.g., Sentinel-2 or Landsat). If students don't have this data, skip to Activity 7.

1. **Explain NDVI:**
   - "NDVI—Normalized Difference Vegetation Index—measures vegetation health"
   - "It uses red and near-infrared bands: healthy plants absorb red light for photosynthesis but reflect NIR light"
   - "Values range from -1 to +1: higher values = healthier vegetation"

2. **Formula:**
   - **NDVI = (NIR - Red) / (NIR + Red)**
   - For Sentinel-2: Red = Band 4, NIR = Band 8
   - For Landsat 8/9: Red = Band 4, NIR = Band 5

3. **Calculate NDVI using Raster Calculator:**
   - `Raster > Raster Calculator`
   - Expression (Sentinel-2):
     ```
     ("sentinel_B08@1" - "sentinel_B04@1") / ("sentinel_B08@1" + "sentinel_B04@1")
     ```
   - Output: `data/processed/week04/ndvi.tif`
   - Run

4. **Style NDVI:**
   - Symbology → Singleband pseudocolor
   - Color ramp: RdYlGn (red-yellow-green)
   - Min: -0.2, Max: 0.8 (adjust to your data range)
   - Classes/interpretation:
     - < 0: Water, bare soil, built-up areas
     - 0–0.2: Sparse vegetation, stressed plants
     - 0.2–0.5: Moderate vegetation (grasslands, crops)
     - 0.5–0.8: Dense, healthy vegetation (forests)
     - > 0.8: Very dense vegetation (tropical forests)

5. **Troubleshooting:**
   - All values near 0? Check you're using the correct band numbers for your sensor
   - Strange patterns? Verify image is not cloudy
   - Very high values (>1)? Division by zero—check for NoData values

**Teaching moment:**
"NDVI is the foundation for vegetation monitoring, crop health assessment, and change detection. Learning it in QGIS means you can later automate it in Python for time-series analysis."

**Activity 7: Zonal Statistics (8 min)**

1. **Explain the goal:**
   - "Zonal statistics summarizes raster values within vector boundaries"
   - "Example: What's the average slope in each SA2 area? Which LGA has the steepest terrain?"

2. **Run zonal statistics:**
   - Processing Toolbox → search "Zonal statistics"
   - Raster layer: slope.tif
   - Vector layer: SA2/LGA boundaries
   - Statistics to calculate: Check Mean, Median, Maximum, Minimum
   - Output column prefix: "slope_"
   - Run (creates modified vector layer)

3. **Examine results:**
   - Open attribute table of output layer
   - Sort by "slope_mean" (descending)
   - "This SA2 has mean slope of 25%—quite steep. This one is 2%—very flat."
   - "We can now map boundaries colored by their terrain characteristics."

4. **Symbolize by zonal stats:**
   - Layer Properties → Symbology → Graduated
   - Value: slope_mean
   - Color ramp: choose appropriate gradient
   - Mode: Natural Breaks (Jenks)
   - Classes: 5
   - Apply
   - "Now we see which administrative areas have the steepest terrain at a glance."

**Wrap Demo (2 min)**
- "You've now gone from raw elevation data to analytical products: hillshade for visualization, slope for analysis, zonal statistics for comparison."
- "Next you'll repeat this workflow with your own study area."

---

### 3. Guided Practice / Lab Work (60-75 minutes)

**Transition (2 min)**
- "Open your Week 3 project or start fresh with your study area"
- "Follow the Week 4 lab guide: load DEM, reproject, clip, create hillshade and slope"
- "Raise your hand if you get stuck—common issues are CRS mismatches and NoData handling"

**Circulate and Support:**
- Move between students, checking progress
- Watch for common issues (see "Common Student Issues" section below)
- Encourage students to compare their outputs: "What's the slope range in your area? Is it mostly flat or hilly?"

**Mid-way Check (after ~30 min):**
- Brief pause: "Who has successfully created a hillshade? Slope? Any surprises in your data?"
- Address recurring issues collectively

**Advanced Students:**
- "Try creating contour lines: `Raster > Extraction > Contour`"
- "Calculate aspect (direction slopes face): `Raster > Terrain Analysis > Aspect`"
- "Experiment with different hillshade angles and blend them"
- "Calculate zonal statistics for elevation (mean elevation by SA2)"

**Final Activity Reminder (last 15 min):**
- "Make sure to create a map layout combining your terrain outputs with boundaries"
- "Export to PDF—this is part of your submission"

---

### 4. Wrap-up & Discussion (15-20 minutes)

**Group Share (10 min)**
- Ask 2-3 students to briefly screen-share their outputs
- Prompt questions:
  - "What terrain patterns did you discover?"
  - "Were there any surprises when you overlaid slope with boundaries?"
  - "Which areas have the steepest terrain? What implications does that have?"

**Reflection Prompts (5 min)**
- Read aloud the reflection questions from the lab guide:
  - How does DEM resolution influence insights?
  - What patterns emerged when overlaying terrain with socio-economic data?
  - Which boundary level felt most appropriate for communicating terrain risk?
  - What challenges with raster data vs vectors?

- "Take 5 minutes now to start your Week 4 reflection. You can finish it after class."

**Preview Week 5 (3 min)**
- "Next week: kernel density estimation for crime hotspot mapping"
- "The raster skills you learned today carry forward—density surfaces are also rasters"
- "Think about how terrain might relate to crime patterns: steep areas = less accessible = less crime?"

**Housekeeping (2 min)**
- Submission checklist review
- Office hours availability
- Remind students to save their QGIS project files

---

## Key Concepts to Emphasize

### 1. Raster vs Vector Data Models

**Core Distinction:**
- **Vector:** Discrete features with precise boundaries (buildings, roads, admin areas)
- **Raster:** Continuous surfaces represented as a grid of cells (elevation, temperature, imagery)

**Teaching Analogy:**
"Vector is like a line drawing—precise outlines. Raster is like a digital photo—composed of pixels."

**Visual Explanation of Raster Grid:**
```
A raster is a matrix of cells (pixels), each storing one value:

    Column 1   Col 2   Col 3   Col 4   Col 5
Row 1  245      248     251     255     262   ← Elevation values
Row 2  243      246     250     258     270      (in meters)
Row 3  241      245     252     265     285
Row 4  240      244     255     275     295
Row 5  239      243     258     280     300

Each cell covers an area (e.g., 30m × 30m). The value represents
the measurement for that entire area.
```

**When to Use Each:**
| Task | Best Data Model | Why |
|------|-----------------|-----|
| Measure area of a suburb | Vector polygon | Precise boundaries |
| Find average elevation | Raster (DEM) | Continuous surface |
| Count buildings | Vector points/polygons | Discrete features |
| Analyze satellite imagery | Raster | Sensor data is grid-based |
| Map flooding extent | Both | Raster for elevation/flow, vector for boundaries |

**Important:** "You'll often use both together—vector boundaries with raster surfaces."

---

### 2. Resolution: The Detail-Speed-Size Trade-off

**Resolution = Cell Size**
- 1m resolution: Each cell is 1m × 1m (extremely detailed)
- 30m resolution: Each cell is 30m × 30m (regional analysis)
- 250m resolution: Each cell is 250m × 250m (continental patterns)

**Visual Example:**
```
5m Resolution (high detail):        30m Resolution (lower detail):
░░▓▓▓▓▓▓░░░░░░░░                   ░░░░▓▓▓▓░░░░
░░▓▓████▓▓░░░░░░                   ░░░░▓▓▓▓░░░░
░░▓▓████▓▓▓▓░░░░                   ░░░░▓▓▓▓░░░░
░░▓▓▓▓▓▓▓▓▓▓░░░░                   ░░░░░░░░░░░░
(Individual houses visible)         (General neighborhood patterns)
```

**Rule of Thumb:**
- Urban planning, site analysis: 1-10m
- Regional watershed analysis: 30m
- Continental climate modeling: 250m+

**The Trade-off:**
- Higher resolution → More detail, larger files, slower processing
- Lower resolution → Less detail, smaller files, faster processing

**Teaching Moment:** "Don't always grab the highest resolution. A 1m DEM of an entire country would be terabytes! Match resolution to your question."

---

### 3. CRS Importance for Raster Analysis

**Why CRS Matters Even More for Rasters:**

1. **Distance Calculations:**
   - Slope = rise / run (vertical change over horizontal distance)
   - If horizontal distance is in degrees (geographic CRS), slope calculation is meaningless
   - **Solution:** Always reproject to a projected CRS (meters) before terrain analysis

2. **Cell Size Interpretation:**
   - Geographic CRS: Cell size in degrees (varies across the map)
   - Projected CRS: Cell size in meters (consistent)

3. **Alignment Issues:**
   - Clipping a raster with a vector requires both to be in the same CRS
   - On-the-fly projection displays them aligned, but operations may fail

**Visual Demonstration:**
```
Geographic CRS (EPSG:4326):        Projected CRS (EPSG:7856):
Pixel size: 0.000277° × 0.000277°  Pixel size: 30m × 30m
(~30m at equator, ~21m at 45°N)    (exactly 30m everywhere in zone)
```

**Best Practice Workflow:**
1. Load DEM (often in WGS84)
2. Reproject to projected CRS matching your study area
3. Then run terrain analysis
4. Never skip reprojection!

**Common Error:**
- Student runs slope on geographic DEM → gets nonsensical values (slopes of 0.00001°)
- **Fix:** Reproject first

---

### 4. DEM/DSM/DTM Differences

**Definitions:**
- **DEM (Digital Elevation Model):** Broadly, any elevation surface. Often used interchangeably with DTM.
- **DTM (Digital Terrain Model):** Bare earth surface—vegetation and buildings removed.
- **DSM (Digital Surface Model):** Top surface—includes buildings, trees, infrastructure.

**Visual Representation:**
```
     Side View:

     DSM (top of everything):
       🌲    🏠    🌲
      ████  ████  ████
     ████████████████  ← DSM surface

     DTM (bare ground):
     ~~~~~~~~~~~~~~~~~~  ← DTM surface
     ╱╲               ╱╲
    ╱  ╲─────────────╱  ╲
```

**When to Use Each:**

| Application | Use | Reason |
|-------------|-----|--------|
| Flood modeling | DTM/DEM | Water flows over ground, not rooftops |
| Viewshed analysis | DSM | Trees and buildings block views |
| Landslide risk | DTM | Natural terrain stability |
| Urban 3D modeling | DSM | Need building heights |
| Archaeology | DTM | Looking for subtle ground features |

**Data Source Implications:**
- **SRTM:** Radar-based, mostly DSM (includes canopy)
- **ELVIS Australia (Geoscience Aus.):** Often DTM (ground-classified)
- **LiDAR:** Can produce both DSM and DTM (point cloud classification)

**Teaching Point:** "Always check your data source documentation. An SRTM 'DEM' of a dense forest might show canopy height, not ground elevation."

---

### 5. NoData Values

**What are NoData Values?**
- Cells where no valid measurement exists
- Commonly represented as -9999, -3.4e38, or defined in metadata
- **Not the same as zero!**

**Common Causes:**
- Ocean cells in land elevation data
- Clouds in satellite imagery
- Area outside the sensor's coverage
- Failed measurements

**Visual:**
```
Elevation Raster:
  150  155  160  NoData  NoData
  145  150  158  NoData  NoData  ← Ocean
  140  148  155  162     170
  138  145  152  160     175

NoData ≠ 0 meters elevation (sea level)
NoData = "No measurement here"
```

**Common Issues:**
1. **Display Problem:**
   - NoData values like -9999 included in symbology range
   - Makes entire raster appear black
   - **Fix:** Set NoData transparency in Symbology tab

2. **Analysis Problem:**
   - Statistics include NoData as real values
   - **Fix:** Ensure NoData value is properly set in raster properties

**Teaching Moment:** "If your DEM suddenly shows areas at -9999 meters below sea level, that's NoData being misinterpreted. Set it to transparent."

---

## Live Demo Script

This detailed script walks through the complete workflow. Use this as a reference; adapt timing and pacing to your class.

---

### **Part 1: Loading and Understanding the DEM (10 minutes)**

**[Open QGIS with blank project]**

**Facilitator:** "I'm starting with a fresh QGIS project. First thing—set the project CRS to something appropriate for our region."

**Action:**
- Bottom-right corner → Click current CRS
- Search "7856" (or your regional projected CRS)
- Select EPSG:7856 - GDA2020 / MGA zone 56
- Apply and OK

**Facilitator:** "Now let's load our elevation data. This is an SRTM tile covering [region]."

**Action:**
- `Layer > Add Layer > Add Raster Layer`
- Browse to `data/raw/week04/srtm_s38_e144.tif`
- Add

**[DEM appears as flat gray]**

**Facilitator:** "It loaded, but we can't see anything meaningful. This is completely normal—the default symbology doesn't know the elevation range. Let's fix it."

**Action:**
- Right-click DEM layer → Properties
- Symbology tab
- Change "Render type" from Singleband gray to **Singleband pseudocolor**
- Color ramp: Click dropdown → "Spectral" (or reverse RdYlGn)
- Min/Max Value Settings: "Cumulative count cut" 2%-98%
- Click "Apply"

**[DEM now shows colors]**

**Facilitator:** "Much better! Green shows lower elevations, brown and white show higher areas. Let's check the actual data."

**Action:**
- Still in Properties → **Information tab**
- Scroll through, point out key details

**Facilitator:** "Let me highlight a few things here:
- **CRS:** WGS 84, EPSG:4326—that's geographic coordinates, latitude/longitude
- **Dimensions:** 3601 by 3601 pixels—that's about 13 million cells
- **Pixel Size:** 0.000277 by 0.000277 degrees—roughly 30 meters at this latitude
- **Bands:** 1—just elevation, no color bands like a photo
- **Data Type:** Int16—whole numbers, saves space
- **No Data Value:** -32768—cells with no data"

**Facilitator:** "Now let's actually look at elevation values."

**Action:**
- Click "Identify Features" tool (i icon in toolbar)
- Click several points on the DEM

**Facilitator:** "Clicking here shows 245 meters elevation. Over here near the coast, 12 meters. Does this match what we expect for [region]? If you're seeing -32768, that's NoData—no measurement there."

**Facilitator:** "Key takeaway: always inspect your data before analysis. Check the CRS, resolution, and value range."

---

### **Part 2: Reprojecting to Projected CRS (8 minutes)**

**Facilitator:** "Our DEM is in a geographic CRS—EPSG:4326, latitude and longitude in degrees. This is a problem for terrain analysis. Let me show you why."

**[Draw or show diagram]**

**Facilitator:** "At the equator, 1 degree of longitude is about 111 kilometers. But at 60 degrees north, 1 degree of longitude is only 55 kilometers. Degrees don't represent equal distances across the Earth.

When we calculate slope—rise over run—we need run to be in real meters, not degrees. Otherwise slope values are meaningless.

Solution: reproject to a projected CRS where distances are in meters."

**Action:**
- `Raster > Projections > Warp (Reproject)`

**Facilitator:** "This tool reprojects rasters. Let's configure it."

**Action:**
- Input layer: [your DEM layer]
- Source CRS: Leave as is (auto-detected)
- Target CRS: Click globe icon → search "7856" → EPSG:7856

**Facilitator:** "EPSG:7856 is GDA2020 Map Grid of Australia zone 56—covers our study area with coordinates in meters."

**Action:**
- Resampling method to use: **Bilinear**

**Facilitator:** "Bilinear interpolation smooths values between pixels. Alternatives are:
- Nearest neighbor: Preserves exact values but looks blocky
- Cubic: Smoother but can create extreme values
For elevation, bilinear is standard."

**Action:**
- Output file: Click [...] → Save to `data/processed/week04/dem_projected.tif`
- Run

**[Processing runs, output loads]**

**Facilitator:** "Good. Now let's verify it worked."

**Action:**
- Right-click new layer → Properties → Information

**Facilitator:** "Look at **CRS:** now it's EPSG:7856. And **Pixel Size:** 30 by 30 meters—real-world units. Perfect. Now we can do terrain analysis."

**Action:**
- Remove original DEM layer (right-click → Remove Layer)

**Facilitator:** "I'm removing the old one to avoid confusion. Always work with the reprojected version from now on."

---

### **Part 3: Clipping to Study Area (10 minutes)**

**Facilitator:** "This DEM covers a huge area, but we only care about [specific LGA/SA2]. Processing the full tile is slow and wastes disk space. Let's clip it to just our study area."

**Action:**
- `Layer > Add Layer > Add Vector Layer`
- Browse to Week 3 SA2/LGA shapefile
- Add

**Facilitator:** "This is the boundary from last week. Before clipping, I need to check that both layers are in the same CRS. This is a common source of errors."

**Action:**
- Right-click DEM layer → Properties → Information → CRS: EPSG:7856 ✓
- Right-click boundary layer → Properties → Information → CRS: EPSG:7856 ✓

**Facilitator:** "Both are EPSG:7856—we're good. If they were different, the clip would fail or produce strange results. Now let's clip."

**Action:**
- Open **Processing Toolbox** (Ctrl+Alt+T or gear icon)
- Search "clip raster by mask"
- Double-click **Clip Raster by Mask Layer**

**Facilitator:** "This tool cuts the raster to the shape of a vector polygon."

**Action:**
- Input layer: dem_projected.tif
- Mask layer: [SA2/LGA boundary layer]
- Source CRS: Leave default
- Target CRS: Leave default
- Check **"Match the extent of the clipped raster to the extent of the mask layer"**

**Facilitator:** "That option makes sure the output is cropped tightly to the boundary."

**Action:**
- Assign a specified nodata value: -9999
- Output: Click [...] → `data/processed/week04/dem_clipped.tif`
- Run

**[Processing completes, clipped DEM loads]**

**Facilitator:** "Perfect. Let's compare."

**Action:**
- Zoom to full extent of original DEM (right-click → Zoom to Layer)
- Then zoom to clipped DEM

**Facilitator:** "Original covered the whole tile—50 megabytes. Clipped version covers just our study area—5 megabytes. Much faster to work with."

**Action:**
- Remove dem_projected layer
- Style dem_clipped with terrain colors (Properties → Symbology → Singleband pseudocolor → terrain color ramp)

**Facilitator:** "From now on, we work with this clipped version."

---

### **Part 4: Creating Hillshade (10 minutes)**

**Facilitator:** "Hillshade simulates sunlight and shadows across terrain. It doesn't change the elevation data—it's purely for visualization, to help us see ridges, valleys, and slopes."

**[Show example hillshade if available]**

**Facilitator:** "Think of it like shining a flashlight on a topographic model. Let's create one."

**Action:**
- `Raster > Analysis > Hillshade`

**Facilitator:** "This tool calculates how light would hit each cell based on sun angle."

**Action:**
- Elevation layer: dem_clipped
- Z factor: 1

**Facilitator:** "Z factor adjusts vertical exaggeration. Since we're already in meters, 1 is correct. If you were working in feet, you'd adjust this."

**Action:**
- Azimuth (horizontal angle): 315

**Facilitator:** "Azimuth is the sun's compass direction. 315 degrees is northwest—the traditional cartographic standard. It creates balanced shadows."

**[Draw compass diagram: N=0/360, E=90, S=180, W=270, NW=315]**

**Action:**
- Altitude (vertical angle): 45

**Facilitator:** "Altitude is how high the sun is above the horizon. 45 degrees is a good balance—low enough to create shadows but not overly dramatic."

**Action:**
- Output: `data/processed/week04/hillshade.tif`
- Run

**[Hillshade loads as grayscale]**

**Facilitator:** "There it is. See the light and shadow? Valleys appear dark, slopes facing northwest are bright. Let's style it nicely."

**Action:**
- Right-click hillshade → Properties → Symbology
- Render type: Singleband gray
- Enhance contrast: Adjust slightly if needed (or leave default)
- OK

**Facilitator:** "Now let's layer it with our boundary."

**Action:**
- Layers Panel: Drag hillshade below the boundary layer
- Double-click boundary layer → Symbology
  - Fill: Transparent
  - Stroke: Black, 0.5mm
  - OK

**Facilitator:** "Now we see the hillshade showing terrain, with the boundary outlined on top. This is a classic cartographic technique—hillshade as a basemap."

**Optional Experiment:**

**Facilitator:** "Let me show you how azimuth affects the result. I'll create another hillshade with eastern light."

**Action:**
- Raster > Analysis > Hillshade
- Azimuth: 90 (east)
- Output: hillshade_east.tif
- Run

**[Compare the two]**

**Facilitator:** "See the difference? Eastern light emphasizes different features. Some cartographers blend multiple hillshades for a more balanced effect. For now, stick with 315 degrees—it's the standard."

---

### **Part 5: Calculating Slope (12 minutes)**

**Facilitator:** "Slope measures steepness—how fast elevation changes across distance. It's critical for understanding flood risk, landslides, accessibility, and construction suitability."

**[Show slope examples if available]**

**Facilitator:** "Slope can be expressed in degrees (0-90°) or percent. Let's do percent—it's more intuitive for planning."

**Action:**
- `Raster > Terrain Analysis > Slope`

**Facilitator:** "This tool calculates slope by comparing each cell's elevation to its neighbors."

**[Draw simple 3x3 grid showing how slope is calculated from neighboring cells if time allows]**

**Action:**
- Input layer: dem_clipped
- Slope expressed as: **Percent**

**Facilitator:** "Percent means: a 10% slope rises 10 meters over 100 meters horizontal distance. A 100% slope rises 1 meter per 1 meter—that's 45 degrees."

**Action:**
- Output: `data/processed/week04/slope.tif`
- Run

**[Slope loads, likely as grayscale]**

**Facilitator:** "It's calculated, but the default gray symbology doesn't help us interpret it. Let's use color."

**Action:**
- Right-click slope layer → Properties → Symbology
- Render type: **Singleband pseudocolor**
- Color ramp: YlOrRd (Yellow-Orange-Red)

**Facilitator:** "Yellow represents flat areas, red represents steep. This is intuitive—red = warning, danger, difficulty."

**Action:**
- Mode: Equal Interval
- Classes: 6
- Click "Classify"
- Manually edit labels:
  - 0-5: "Flat (0-5%)"
  - 5-10: "Gentle (5-10%)"
  - 10-20: "Moderate (10-20%)"
  - 20-30: "Steep (20-30%)"
  - 30-50: "Very Steep (30-50%)"
  - >50: "Extreme (>50%)"
- Apply and OK

**[Slope now shows color-coded steepness]**

**Facilitator:** "Much better. Now we can visually identify steep areas."

**Action:**
- Use Identify tool (i icon)
- Click around the map

**Facilitator:** "Clicking in this valley: 8% slope—gentle. Up on this ridge: 35%—very steep. Along this creek: 18%—moderate.

Let me give you context:
- 0-5%: Flat, easy to build, accessible
- 5-10%: Gentle, suitable for most development
- 10-20%: Moderate, roads need careful design
- 20%+: Steep, expensive to build, erosion risk, poor accessibility
- 50%+: Very steep, landslide risk, not developable

Where would you build a school? A road? Where might floods concentrate?"

**Common Issue Check:**

**Facilitator:** "If your slope values all look near zero or seem wrong, the problem is usually CRS. Slope calculation assumes the DEM is in a projected CRS with meters. That's why we reprojected earlier."

---

### **Part 6: Zonal Statistics (10 minutes)**

**Facilitator:** "Now the powerful part: combining our raster analysis with vector boundaries. We'll calculate the average slope for each SA2 area using zonal statistics."

**[Draw simple diagram: polygon overlaying raster cells]**

**Facilitator:** "Zonal statistics takes a raster and a set of polygons, and calculates summary statistics for the raster cells within each polygon. Example: mean elevation, maximum slope, total rainfall."

**Action:**
- Open **Processing Toolbox**
- Search "zonal statistics"
- Double-click **Zonal Statistics**

**Action:**
- Raster layer: slope.tif
- Raster band: Band 1
- Vector layer containing zones: [SA2/LGA boundary layer]
- Output column prefix: "slope_"

**Facilitator:** "This prefix gets added to field names—slope_mean, slope_max, etc."

**Action:**
- Statistics to calculate:
  - Check **Mean**
  - Check **Median**
  - Check **Maximum**
  - Check **Minimum**
  - (Uncheck others for simplicity)
- Zonal Statistics: [Leave as Create new layer or Save to file...]
- Run

**[Output layer loads—same boundaries, now with slope statistics]**

**Facilitator:** "Done. The boundaries now have new fields showing slope statistics."

**Action:**
- Right-click output layer → Open Attribute Table

**Facilitator:** "See the new columns? slope_mean, slope_median, slope_max, slope_min. Let me sort by mean slope."

**Action:**
- Click column header "slope_mean" to sort descending

**Facilitator:** "This SA2 has a mean slope of 28%—very hilly. This one down here: 3%—quite flat. Now we can map this."

**Action:**
- Close attribute table
- Right-click layer → Properties → Symbology
- Change to **Graduated**
- Value: slope_mean
- Color ramp: YlOrRd
- Mode: Natural Breaks (Jenks)
- Classes: 5
- Classify
- Apply and OK

**Facilitator:** "Now we see at a glance which administrative areas have the steepest terrain. This is powerful for planning—imagine overlaying this with:
- Flood risk (steep slopes = faster runoff)
- Housing density (steep = less buildable land)
- Accessibility (steep = harder for elderly, wheelchairs)
- SEIFA from last week (does disadvantage correlate with steep terrain?)"

**Facilitator:** "That's the real power of GIS—combining datasets to answer complex questions."

---

### **Part 7: Wrap-Up (3 minutes)**

**Facilitator:** "Let me recap what we just did:
1. Loaded a raw DEM and inspected its metadata
2. Reprojected it to a projected CRS for accurate analysis
3. Clipped it to our study area to speed up processing
4. Created a hillshade for visualization
5. Calculated slope to analyze steepness
6. Used zonal statistics to summarize slope by administrative area

You now have the skills to analyze any terrain dataset. In your lab work, you'll repeat this workflow for your own study area."

**Action:**
- Save project: `File > Save As` → `projects/week04_terrain_demo.qgz`

**Facilitator:** "I'm saving this demo project so you can refer back to it. Now over to you—follow the lab guide and build your own terrain analysis."

---

## Discussion Prompts

Use these prompts to stimulate critical thinking and connect theory to real-world applications. Intersperse throughout the session or use during breaks.

---

### **1. Real-World Applications of Terrain Analysis**

**Prompt:** "Think about your local area. Where might slope or elevation data be critical for decision-making?"

**Possible Answers / Extensions:**
- **Flood risk:** Low-lying areas near rivers; steep slopes create flash flooding
- **Urban planning:** Flat land is easier/cheaper to develop; steep areas need retaining walls, different road designs
- **Agriculture:** Slope affects soil erosion, irrigation, crop selection
- **Transportation:** Roads on steep slopes require switchbacks, tunneling; accessibility issues
- **Emergency services:** Steep terrain affects ambulance response times, fire truck access
- **Renewable energy:** Wind turbines on ridges; solar panel orientation based on aspect
- **Recreation:** Hiking trail difficulty ratings based on slope; ski run classification

**Extension Question:** "How might terrain analysis differ between a coastal city and a mountainous region?"

---

### **2. Flood Risk and Terrain**

**Prompt:** "We've calculated slope across our study area. How does slope relate to flood risk? Is steeper always safer?"

**Discussion Points:**
- **Flat areas (low slope):**
  - Water pools and spreads slowly
  - High flood *duration* risk
  - Example: river deltas, floodplains

- **Steep slopes:**
  - Water runs off quickly
  - Lower *inundation* risk at the slope itself
  - BUT increases risk *downstream* (flash floods)
  - Erosion risk

- **Valleys/low elevation:**
  - Water collects here regardless of slope
  - Need both elevation *and* slope for full picture

**Extension:** "If you were advising on building permits, what elevation and slope thresholds would you set for flood-prone areas?"

---

### **3. Construction and Accessibility**

**Prompt:** "You're planning a new community center. The council has three potential sites with different slopes: Site A (2% slope), Site B (12% slope), Site C (25% slope). What are the pros and cons of each?"

**Guided Discussion:**

| Site | Slope | Construction | Accessibility | Cost |
|------|-------|--------------|---------------|------|
| A | 2% | Easy, minimal grading | Excellent wheelchair access | Low |
| B | 12% | Moderate, some grading needed | Ramps needed, manageable | Medium |
| C | 25% | Difficult, extensive earthworks | Very challenging, lifts needed | High |

**Additional Factors:**
- Drainage (flat sites need drainage design)
- Views (steep sites may have better views)
- Parking (flat areas easier to design parking lots)

**Extension:** "What if Site C is the only site in an underserved neighborhood? How do you balance accessibility against community need?"

---

### **4. Hiking and Recreation**

**Prompt:** "Imagine you're designing a hiking trail network. How would you use slope data to classify trails as Easy, Moderate, or Difficult?"

**Example Classification:**
- **Easy:** <10% slope, wide paths, suitable for families
- **Moderate:** 10-20% slope, some steep sections
- **Difficult:** >20% slope, sustained climbing, experienced hikers only

**Extension Activities:**
- Calculate average slope along proposed trail routes
- Identify viewpoints (high elevation areas)
- Assess accessibility (can people with mobility aids use the trail?)

**Real-World Example:** "National parks use exactly this kind of analysis. The Grand Canyon rates trails by elevation change and steepness."

---

### **5. DEM Resolution Trade-offs**

**Prompt:** "We used 30-meter SRTM data today. How would your analysis change with 5-meter LiDAR? What about 90-meter data?"

**Discussion Table:**

| Resolution | What You Gain | What You Lose | Use Case |
|------------|---------------|---------------|----------|
| 1-5m LiDAR | See individual buildings, trees, small gullies | Huge file sizes, slow processing | Urban planning, archaeology |
| 30m SRTM | Balanced detail, manageable files | Miss small features | Regional watershed, general planning |
| 90m SRTM | Fast, small files, global coverage | Very generalized | Continental analysis, broad patterns |

**Practical Example:** "If you're modeling a landslide on a specific hillside, 1m LiDAR shows every boulder and gully. If you're comparing slope across 50 municipalities, 30m is plenty."

**Extension:** "What resolution would you need to plan a bike path? A highway? A continental railway?"

---

### **6. Ethical Considerations**

**Prompt:** "You've just identified that low-income SA2 areas (low SEIFA) in your region are predominantly on steep terrain. What are the implications? What ethical responsibilities do you have as an analyst?"

**Discussion Points:**
- **Accessibility:** Steep areas harder for elderly, disabled residents
- **Service access:** Garbage collection, ambulances may be slower
- **Infrastructure costs:** Roads, utilities more expensive = less investment
- **Gentrification risk:** If you publish that flat areas are "better," does that drive up prices?
- **Communication:** How do you present findings without stigmatizing neighborhoods?

**Extension:** "Who should have access to this analysis? Just planners? Community groups? Developers?"

---

### **7. Climate Change and Terrain**

**Prompt:** "How might terrain analysis become more important as climate changes?"

**Discussion Points:**
- **Sea level rise:** Low-elevation areas at risk (combine DEM with projected inundation)
- **Extreme rainfall:** Steep slopes amplify flash flood risk
- **Landslides:** Increased rainfall + steep slopes = higher landslide frequency
- **Heatwaves:** Slope aspect (N-facing vs S-facing in southern hemisphere) affects heat exposure
- **Bushfire:** Slope affects fire spread (fire runs uphill faster)

**Extension:** "What new terrain datasets might we need? Higher resolution? More frequent updates?"

---

## Common Student Issues & Solutions

This section lists problems students frequently encounter during raster analysis, along with explanations and fixes.

---

### **1. CRS Errors with Slope Calculation**

**Symptom:**
- Slope values are extremely small (0.00001) or extremely large (10,000+)
- Slope output looks uniform/wrong

**Cause:**
- DEM is still in geographic CRS (degrees, e.g., EPSG:4326)
- Slope calculation interprets degrees as meters → wrong distance calculations

**Solution:**
- **Always reproject DEM to a projected CRS before running slope**
- `Raster > Projections > Warp (Reproject)` → Choose appropriate UTM or local projected CRS
- Re-run slope on the reprojected DEM

**Teaching Moment:**
"This is the most common mistake. QGIS will happily calculate slope on a geographic DEM—it doesn't throw an error. But the results are meaningless. Always check your CRS first."

**Prevention:**
- Add to checklist: "DEM is in projected CRS with units in meters? ✓"

---

### **2. Large File Performance Issues**

**Symptom:**
- QGIS freezes or takes 10+ minutes to process
- Computer fans spinning loudly
- Out of memory errors

**Cause:**
- Working with full DEM tiles (e.g., 50+ MB, millions of cells)
- High-resolution LiDAR (1m resolution over large area)

**Solutions:**

**A. Clip to study area first:**
- Don't run hillshade/slope on the full tile
- Clip to your SA2/LGA boundary first: `Raster > Extraction > Clip Raster by Mask Layer`

**B. Resample to lower resolution for testing:**
- `Raster > Projections > Warp (Reproject)`
- Set "Output file resolution in target georeferenced units" to 100m (instead of 30m)
- Test workflow, then re-run at full resolution

**C. Close other applications:**
- Raster processing is memory-intensive
- Close web browsers, Office apps

**D. Process in batches:**
- If multiple tiles, mosaic them last (not first)

**Teaching Moment:**
"Raster data can be huge. A 1-meter resolution DEM of a city is gigabytes. Always work on a clipped subset during testing, then scale up for final output."

---

### **3. NoData Values Causing Display Issues**

**Symptom:**
- DEM appears completely black or white
- Identify tool shows -9999 or -3.4e38 in some areas
- Slope calculation produces strange results at edges

**Cause:**
- NoData values (-9999) are being included in the symbology min/max range
- QGIS interprets -9999 as a real elevation value

**Solution:**

**A. Set NoData transparency:**
- Layer Properties → Symbology
- Scroll down to "No Data Value"
- Enter -9999 (or check raster metadata for the actual NoData value)
- Set "Additional no data value" if needed
- Under "Transparency" tab, add -9999 to transparent pixels

**B. Fix min/max values:**
- Symbology → Min/Max Value Settings
- Change from "Min/Max" to **"Cumulative count cut"** (2%-98%)
- This ignores extreme outliers

**C. Use Raster Calculator to remove NoData:**
- If NoData values are causing analysis problems
- `Raster > Raster Calculator`
- Expression: `("DEM@1" >= 0) * "DEM@1"`
- This sets negative values to 0 (only if appropriate for your data!)

**Teaching Moment:**
"NoData is not the same as zero elevation. Sea level is zero. NoData means 'no measurement here.' Always set NoData to transparent so it doesn't skew your visualization."

---

### **4. Clip Raster Produces Empty or Tiny Output**

**Symptom:**
- Clipped raster is blank, shows NoData everywhere
- Output file is tiny (few KB)
- Error message: "No data in output"

**Causes & Solutions:**

**A. CRS Mismatch:**
- **Check:** Are DEM and boundary layer in the same CRS?
- **Fix:** Reproject one to match the other
- Processing Toolbox has option to reproject on-the-fly, but safer to do it manually first

**B. No Overlap:**
- **Check:** Do the layers actually overlap?
- **Test:** Zoom to layer extents for both—do they cover the same geographic area?
- **Fix:** If no overlap, you've selected the wrong DEM tile or wrong boundary

**C. Boundary Layer is Empty/Corrupted:**
- **Check:** Open boundary attribute table—are there features?
- **Fix:** Reload boundary from source

**D. Wrong Mask Layer Selected:**
- **Check:** Did you select the actual polygon layer (not a point or line layer)?
- **Fix:** Ensure mask layer is polygon type

**Teaching Moment:**
"Always verify overlap before clipping. A quick zoom to both layers will show you if they're even in the same part of the world."

---

### **5. Raster Doesn't Align with Vector Boundaries**

**Symptom:**
- DEM and boundaries don't line up when zoomed in
- Offset by meters to kilometers
- Clipping fails or produces strange results

**Causes & Solutions:**

**A. Different CRS:**
- **Check:** Compare layer CRS in Properties → Information
- **Fix:** Reproject one to match the other

**B. On-the-Fly Projection Hiding the Problem:**
- **Check:** QGIS displays layers in the project CRS, which can hide misalignment
- **Test:** Turn off "On-the-fly CRS transformation" (old QGIS) or set project CRS to match one layer
- **Fix:** Don't rely on OTF—actually reproject layers to a common CRS

**C. Datum Shift:**
- **Check:** Are layers using different datums? (E.g., AGD66 vs GDA94 in Australia; NAD27 vs NAD83 in USA)
- **Fix:** Reproject with explicit datum transformation

**Teaching Moment:**
"QGIS is smart—it can display layers in different CRS together. But for analysis, they MUST be in the same CRS. On-the-fly projection is for viewing, not analysis."

---

### **6. Hillshade is Too Dark or Washed Out**

**Symptom:**
- Hillshade is all black or all white
- Shadows are too harsh or too subtle

**Solutions:**

**A. Adjust Z-Factor:**
- If hillshade is too flat (no shadows): Increase Z-factor to 2 or 3 (exaggerates relief)
- If hillshade is too dramatic: Decrease Z-factor to 0.5

**B. Change Altitude (Sun Angle):**
- Lower altitude (e.g., 30°): More dramatic shadows
- Higher altitude (e.g., 60°): Softer, less contrast

**C. Adjust Symbology Contrast:**
- Layer Properties → Symbology → Contrast enhancement
- Or manually adjust min/max grayscale values

**D. Blend Mode:**
- Layer Properties → Symbology → Layer Rendering → Blending mode
- Try "Multiply" blended over the DEM

**Teaching Moment:**
"Hillshade is art as much as science. Experiment with settings until it looks good for your purpose—print maps need different settings than screen displays."

---

### **7. Zonal Statistics Returns NULL or Wrong Values**

**Symptom:**
- New fields (slope_mean, etc.) are empty or show NULL
- Values seem incorrect or uniform

**Causes & Solutions:**

**A. No Overlap Between Layers:**
- **Check:** Do polygons actually overlap the raster?
- **Fix:** Verify both are in same CRS and same geographic area

**B. CRS Mismatch:**
- **Check:** Are raster and vector in the same CRS?
- **Fix:** Reproject one to match the other

**C. NoData Cells:**
- **Check:** Are polygons mostly covering NoData areas?
- **Fix:** Verify raster has valid data in the area of interest

**D. Raster Not Actually Loaded:**
- **Check:** Is the raster layer visible and loaded in the project?
- **Fix:** Re-add the raster layer

**E. Wrong Band Selected:**
- **Check:** If multi-band raster, did you select the correct band?
- **Fix:** Set "Raster band" to Band 1 (for DEMs)

**Teaching Moment:**
"Zonal statistics is powerful but picky. It requires perfect overlap and CRS match. Always check your inputs first."

---

### **8. Export Creates Huge File**

**Symptom:**
- Exported raster is 500MB+ (or multiple GB)
- Takes forever to save
- Crashes QGIS

**Solutions:**

**A. Use Compression:**
- When exporting (e.g., Warp, Clip, Slope tools):
- Expand "Advanced Parameters"
- Profile: "High compression"
- OR Additional command-line parameters: `compress=LZW` or `compress=DEFLATE`

**B. Reduce Extent:**
- Only export the area you need
- Clip to study area boundary first

**C. Lower Resolution:**
- If appropriate, resample to lower resolution
- E.g., 30m instead of 5m for regional analysis

**D. Change Data Type:**
- If slope values are 0-100, Int16 is sufficient (not Float64)
- Most tools have "Output data type" option

**Teaching Moment:**
"Always compress rasters when exporting. LZW compression can reduce file sizes by 50-80% with no quality loss."

---

### **9. Student Uses Geographic CRS for Analysis**

**Symptom:**
- Slope/aspect/hillshade values are nonsensical
- Tools run but produce garbage output

**Cause:**
- Student skipped reprojection step
- DEM still in EPSG:4326 or similar geographic CRS

**Solution:**
- **Stop and reproject first**
- Explain again why projected CRS is needed
- Have student verify pixel size is in meters, not degrees

**Prevention:**
- Add prominent warning in lab guide
- Include CRS check in demo
- Create checklist item: "DEM CRS is projected (meters)? ✓"

---

### **10. Student Confused by Percent vs Degree Slope**

**Symptom:**
- "My slope is 45, is that bad?"
- Misinterpreting slope units

**Solution:**

**Explain the difference:**
- **Degrees:** 0-90°, where 0° = flat, 45° = very steep, 90° = vertical cliff
- **Percent:** 0-∞%, where 0% = flat, 100% = 45°, 200% = 63°

**Conversion:**
- Percent = tan(degrees) × 100
- 10° ≈ 18%
- 20° ≈ 36%
- 45° = 100%

**Rule of Thumb:**
- <10% = walkable/drivable
- 10-20% = moderate slope
- >20% = steep, challenging

**Teaching Moment:**
"Use percent for communication with planners and public—it's more intuitive. Use degrees for scientific papers in geomorphology."

---

## Wrap-up & Preview

### **End-of-Session Summary (5 minutes)**

**Facilitator Script:**

"Let's recap what you've accomplished today:

**1. Conceptual Understanding:**
- You now understand the difference between raster and vector data models
- You can distinguish between DEM, DSM, and DTM
- You appreciate the trade-offs of resolution: detail vs speed vs file size

**2. Technical Skills:**
- Loading and inspecting raster metadata (CRS, resolution, extent)
- Reprojecting rasters to projected coordinate systems
- Clipping large datasets to study areas
- Generating terrain derivatives: hillshade for visualization, slope for analysis
- Combining raster and vector using zonal statistics

**3. Analytical Thinking:**
- You've connected terrain analysis to real-world questions: flood risk, accessibility, construction suitability
- You've seen how multiple data types (boundaries + terrain + socio-economic indicators) come together to answer complex questions

**What to Submit:**
- Your QGIS project file with clipped DEM, hillshade, and slope layers
- At least one derived raster saved to `data/processed/week04/`
- A map layout (PDF or PNG) combining terrain outputs with boundary annotations
- Your Week 4 reflection, answering the questions in the lab guide

**Submission deadline:** [State specific date/time]

**Getting Help:**
- Office hours: [times]
- Discussion forum: Post screenshots if you're stuck
- Don't struggle alone—CRS and NoData issues are common, we can help quickly"

---

### **Preview Week 5 (3 minutes)**

**Facilitator Script:**

"Next week, we shift focus to **kernel density estimation for crime hotspot mapping**. This is where we enter sensitive data territory—mapping crime locations to identify patterns.

**What's Coming:**
- Point density analysis (turning crime locations into continuous density surfaces)
- Ethical considerations: privacy, stigmatization, responsible communication
- The raster skills you learned today carry forward—density surfaces are rasters, just like elevation

**Connection to This Week:**
- Both elevation and density are continuous surfaces represented as rasters
- Both use similar visualization techniques (color ramps, transparency)
- You might even combine them: does crime cluster in flat areas? Near commercial zones? This is where multi-layer analysis gets powerful.

**Homework Thought:**
As you finish your Week 4 reflection, consider: how might terrain influence crime patterns in your study area? Are steep areas less accessible and therefore safer? Do certain crimes cluster near transportation hubs in valleys? Start thinking spatially across datasets.

**Data Prep for Next Week:**
- You'll need crime incident point data (we'll provide sources)
- Your SA2/LGA boundaries from Week 3 (again!)
- Start thinking about ethical considerations: how do you map crime without stigmatizing communities?

See you next week. Great work today."

---

### **Optional: Quick Feedback Check (2 minutes)**

**Facilitator:** "Before we finish, quick show of hands:

- Who successfully created a hillshade? [count hands]
- Who calculated slope? [count hands]
- Who ran zonal statistics? [count hands]
- Who encountered a problem they couldn't solve? [count hands—note for follow-up]

If you raised your hand for the last question, please stay for a minute or email me the issue. I want to make sure everyone is on track."

---

### **Post-Session Facilitator Tasks**

- [ ] Review common errors that came up—add to this document for next time
- [ ] Check discussion forum for posted questions
- [ ] Update troubleshooting guide if new issues emerged
- [ ] Prepare Week 5 crime data sources and ethical guidelines
- [ ] Follow up with students who struggled significantly

---

## Additional Teaching Resources

### **Visual Aids to Prepare**

**1. Raster Grid Diagram:**
```
How Rasters Store Data:

  [Elevation Raster - Each cell = one value]

     0    1    2    3    4   ← Column
  ┌─────────────────────────┐
0 │ 245  248  251  255  262 │ ← Row 0
1 │ 243  246  250  258  270 │
2 │ 241  245  252  265  285 │
3 │ 240  244  255  275  295 │
4 │ 239  243  258  280  300 │
  └─────────────────────────┘

  Cell (2,3) = 265 meters elevation
  Each cell covers 30m × 30m on the ground
```

**2. DEM vs DSM vs DTM Diagram:**
```
Side View of Landscape:

DSM (Digital Surface Model):
   🌲      🏠      🌲
  ████    ████    ████   ← Top of trees & buildings
  ─────────────────────

DEM/DTM (Bare Earth):
  ~~~~~~~~~~~~~~~~~~~~~   ← Ground surface only
  ╱╲               ╱╲
 ╱  ╲─────────────╱  ╲
```

**3. CRS Impact on Distance:**
```
Geographic CRS (degrees):
At equator: 1° longitude = 111 km
At 60°N:     1° longitude = 55 km
→ Distances vary across the map!

Projected CRS (meters):
Everywhere: 1000m = 1000m
→ Distances are consistent
```

**4. Slope Percent vs Degrees:**
```
Slope Comparison:

0%  = 0°   Flat ─────────
10% = 6°   Gentle  ╱
25% = 14°  Moderate ╱
50% = 27°  Steep    ╱
100% = 45° Very Steep ╱
```

---

### **Example Real-World Case Studies**

**1. Brisbane Floods (2011):**
- DEM used to model flood inundation
- Combined with building footprints to identify at-risk properties
- Slope analysis showed which areas would drain quickly vs pool water

**2. Christchurch Earthquake (2011):**
- LiDAR before/after showed ground deformation
- Slope analysis identified landslide-prone areas
- DTM vs DSM comparison showed building collapse

**3. Blue Mountains Bushfire Planning:**
- Slope + aspect analysis to predict fire spread direction and speed
- Steep slopes = fire travels uphill faster
- North-facing slopes (southern hemisphere) = hotter, drier, higher risk

---

### **Glossary for Students**

Provide this as a handout or reference:

- **Azimuth:** Compass direction (0-360°) where 0/360 = North, 90 = East, 180 = South, 270 = West
- **Band:** A layer in a raster dataset (elevation has 1 band, RGB imagery has 3)
- **Cell:** A single pixel in a raster grid
- **DEM:** Digital Elevation Model—elevation surface
- **DSM:** Digital Surface Model—top surface including buildings/trees
- **DTM:** Digital Terrain Model—bare earth surface
- **Hillshade:** Shaded relief map simulating sunlight and shadows
- **NoData:** Cells with no valid measurement (not zero!)
- **Resolution:** Cell size (e.g., 30m = each cell covers 30m × 30m)
- **Slope:** Steepness of terrain (degrees or percent)
- **Vertical Exaggeration (Z-factor):** Multiplier to amplify relief in visualizations
- **Zonal Statistics:** Summary statistics (mean, max, etc.) of raster values within vector polygons

---

## Final Notes for Facilitators

### **Pacing Tips**
- This is a content-heavy week—students encounter many new concepts
- Prioritize understanding over speed: better to master hillshade + slope than rush through all activities
- If time is tight, make contour lines and aspect optional

### **Common Stumbling Blocks**
1. **CRS confusion:** Reinforce repeatedly. Check CRS before every operation.
2. **File management:** Students lose track of original vs reprojected vs clipped DEMs. Emphasize naming conventions.
3. **NoData handling:** This is subtle but important. Take time to explain.

### **Differentiation**
- **Struggling students:** Focus on getting one complete workflow (DEM → hillshade → slope). Skip zonal stats if needed.
- **Advanced students:** Challenge them to create aspect maps, contour lines, 3D visualizations, or combine multiple hillshades.

### **Assessment Criteria** (if grading)
- Technical execution: Can they produce correct hillshade and slope outputs?
- Interpretation: Do they understand what the outputs mean?
- Integration: Did they successfully combine terrain with boundaries?
- Communication: Is their map layout clear and well-annotated?
- Reflection: Do they critically engage with resolution trade-offs and ethical considerations?

### **For Next Time**
- Note which troubleshooting issues came up most frequently
- Update this guide with new solutions
- Collect student work examples (with permission) to show future cohorts

---

**End of Facilitator Notes**

Good luck with the session! Remember: raster analysis is challenging for many students, but incredibly rewarding once they see terrain patterns emerge from raw elevation data.
