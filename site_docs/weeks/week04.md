# Week 4 · Flood Risk Assessment

## Research Question

> **"Which areas in the Hawkesbury-Nepean region are at elevated flood risk based on terrain characteristics?"**

This week, you'll conduct a terrain-based flood risk assessment—the same analysis you'll automate in Python during Week 9. By doing it manually first in QGIS, you'll understand exactly what each step accomplishes before writing code to replicate it.

The Hawkesbury-Nepean region west of Sydney experienced devastating floods in 2022. While professional flood modelling uses complex hydrological simulations, terrain analysis provides a first approximation of flood-prone areas based on elevation and slope.

## What you'll learn

By the end of this week, you'll be able to:

1. Download and prepare elevation data (DEM) for a specific study area.
2. Calculate terrain derivatives (slope, hillshade) that inform flood risk.
3. Use the Raster Calculator to classify areas by flood risk level.
4. Apply zonal statistics to summarize risk by administrative boundary.
5. Communicate findings with appropriate limitations and caveats.

## Before you start

- [ ] Review the lecture: [Elevation & Surface Modelling](../lectures/week04-raster-theory.md)
- [ ] Read: [Raster Data Basics](../readings/week04-raster-basics.md)

!!! note "Data downloads happen in class"
    We'll download elevation data from ELVIS together as Activity 1. Your facilitator will guide you through the process—this is one of the more complex downloads in the course!

## Study area

We'll focus on the **Hawkesbury-Nepean floodplain**, approximately:

- **Bounding box:** 150.6°E to 150.85°E, 33.65°S to 33.45°S
- **Why this area:** Real flood history (2022 floods), varied terrain, recognizable to Sydney students
- **Size:** Approximately 20km × 20km

!!! tip "For your capstone"
    You can adapt this workflow to any study area. The same approach works for bushfire risk (slope + aspect + vegetation), erosion risk, or accessibility analysis.

## This week's activities

### Activity 1: Download DEM from ELVIS

You'll download elevation data from ELVIS (Elevation Information System), Australia's national elevation data portal.

**Steps:**

1. Go to [ELVIS](https://elevation.fsdf.org.au/)
2. Click **Get Data** or **Order Data**
3. Navigate to the Hawkesbury-Nepean region (west of Sydney, around Richmond/Windsor)
4. Draw a rectangle covering your study area:
   - Keep it small (20km × 20km maximum) for faster processing
   - Include the river floodplain and surrounding hills
5. Select **DEM** as the product type
6. Choose the highest resolution available (typically 5m for NSW)
7. Download and save to `week04/data/raw/`
8. **Extract** the ZIP file

**What you should have:**

```
week04/data/raw/
├── dem_tile.tif (or similar name)
└── (possibly metadata files)
```

!!! note "Alternative: SRTM data"
    If ELVIS is unavailable, download SRTM 30m data from [USGS EarthExplorer](https://earthexplorer.usgs.gov/). It's lower resolution but covers the globe.

### Activity 2: Load and inspect the DEM

Before analysis, understand what your elevation data represents.

**Steps:**

1. Load your DEM into QGIS: `Layer ▶ Add Layer ▶ Add Raster Layer...`
2. Inspect layer properties:
   - Right-click layer → **Properties** → **Information** tab
   - Note the CRS (should be a projected CRS like EPSG:28356 for NSW)
   - Check pixel size (resolution) and elevation range
3. Style the DEM:
   - Layer Properties → **Symbology** → **Singleband pseudocolor**
   - Color ramp: **terrain** or **Spectral** (inverted)
   - Click **Classify** then **Apply**
4. Explore the terrain:
   - Where is the river? (lowest elevations)
   - Where are the hills? (highest elevations)
   - Can you identify the floodplain? (flat, low-lying areas near the river)

**Record these values:**

- Minimum elevation: _____ m
- Maximum elevation: _____ m
- Pixel size: _____ m

!!! warning "Check your CRS"
    If the DEM is in geographic coordinates (EPSG:4326), reproject it first:
    `Raster ▶ Projections ▶ Warp (Reproject)` → Target CRS: EPSG:28356 (GDA2020 / MGA Zone 56)

### Activity 3: Generate a hillshade

Hillshade helps visualize terrain and will serve as a basemap for your final output.

**Steps:**

1. Generate hillshade:
   - `Raster ▶ Analysis ▶ Hillshade`
   - **Elevation layer:** your DEM
   - **Azimuth:** 315° (northwest—standard cartographic convention)
   - **Altitude:** 45°
   - **Output:** `data/processed/week04/hillshade.tif`
2. Style the hillshade:
   - Layer Properties → **Symbology** → **Singleband gray**
   - This creates a shaded relief effect
3. Layer it under your DEM:
   - Move hillshade below the DEM in the Layers panel
   - Set DEM transparency to 50-60%
   - The combination shows elevation colors with 3D shading

**QGIS ↔ Python comparison:**

| QGIS | Python (Week 9) |
|------|-----------------|
| Raster > Analysis > Hillshade | Custom function with `np.gradient()` |

### Activity 4: Calculate slope

Slope tells us how steep the terrain is. **Flat areas accumulate water; steep areas drain quickly.**

**Steps:**

1. Calculate slope:
   - `Raster ▶ Analysis ▶ Slope`
   - **Elevation layer:** your DEM
   - **Slope expressed as:** Degrees
   - **Output:** `data/processed/week04/slope.tif`
2. Style the slope layer:
   - Layer Properties → **Symbology** → **Singleband pseudocolor**
   - Color ramp: **YlOrRd** (Yellow-Orange-Red)
   - **Min:** 0°, **Max:** 30° (adjust based on your terrain)
   - Click **Classify** then **Apply**
3. Interpret the result:
   - Yellow areas = flat (high flood accumulation risk)
   - Red areas = steep (water runs off quickly)

**Slope interpretation for flood risk:**

| Slope | Risk implication |
|-------|------------------|
| <2° | Very flat—water accumulates (HIGH RISK) |
| 2-5° | Gently sloping—some drainage |
| 5-15° | Moderate slopes—good drainage |
| >15° | Steep—rapid runoff (LOW RISK) |

**QGIS ↔ Python comparison:**

| QGIS | Python (Week 9) |
|------|-----------------|
| Raster > Analysis > Slope | `np.gradient()` + `np.arctan()` |

### Activity 5: Identify low-lying areas

Low elevation is the primary flood risk factor. We'll create a binary raster showing areas below a threshold elevation.

**Steps:**

1. Determine threshold:
   - Look at your DEM's elevation range
   - The floodplain is typically in the lowest 20-30% of elevations
   - For the Hawkesbury, areas below ~20-30m are historically flood-prone
2. Open Raster Calculator:
   - `Raster ▶ Raster Calculator...`
3. Enter expression to identify low areas:
   ```
   "dem@1" < 30
   ```
   - Replace `dem` with your actual layer name
   - Replace `30` with your chosen threshold
   - This creates a binary raster: 1 = low-lying, 0 = higher ground
4. Save as `data/processed/week04/low_lying.tif`
5. Style as categorized:
   - 0 = transparent or light gray
   - 1 = blue (flood-prone)

!!! tip "Choosing the threshold"
    The "right" threshold depends on local knowledge. For the Hawkesbury:
    - 1-in-100 year flood reaches ~15-20m in some areas
    - Major 2022 floods exceeded 20m at some gauges
    - Use 20-30m as a reasonable starting point

### Activity 6: Create flood risk classification

Now we combine elevation and slope into a composite risk score.

**Flood risk logic:**
- **Low elevation** = higher risk (water accumulates)
- **Flat slope** = higher risk (poor drainage)

**Steps:**

1. Open Raster Calculator: `Raster ▶ Raster Calculator...`

2. **Step A: Normalize elevation to 0-1 (inverted so low = high score)**
   ```
   1 - ("dem@1" - [MIN]) / ([MAX] - [MIN])
   ```
   Replace `[MIN]` and `[MAX]` with your DEM's actual range.

   Example for elevation range 0-200m:
   ```
   1 - ("dem@1" - 0) / (200 - 0)
   ```
   Save as `elevation_score.tif`

3. **Step B: Normalize slope to 0-1 (inverted so flat = high score)**
   ```
   1 - ("slope@1" / 15)
   ```
   This gives score of 1.0 for flat (0°) and 0.0 for slopes ≥15°
   Save as `slope_score.tif`

4. **Step C: Combine with weights**
   ```
   0.6 * "elevation_score@1" + 0.4 * "slope_score@1"
   ```
   - Elevation weighted 60% (most important factor)
   - Slope weighted 40%
   Save as `data/processed/week04/flood_risk_index.tif`

5. **Step D: Classify into risk zones**
   ```
   ("flood_risk_index@1" < 0.3) * 1 +
   ("flood_risk_index@1" >= 0.3 AND "flood_risk_index@1" < 0.5) * 2 +
   ("flood_risk_index@1" >= 0.5 AND "flood_risk_index@1" < 0.7) * 3 +
   ("flood_risk_index@1" >= 0.7) * 4
   ```
   Save as `data/processed/week04/flood_risk_classes.tif`

6. Style the classified output:
   - Layer Properties → **Symbology** → **Paletted/Unique values**
   - Assign colors:
     - 1 = Green (Low risk)
     - 2 = Yellow (Moderate risk)
     - 3 = Orange (High risk)
     - 4 = Red (Very high risk)

**QGIS ↔ Python comparison:**

| QGIS | Python (Week 9) |
|------|-----------------|
| Raster Calculator expressions | NumPy array operations |
| Multiple steps | Single code block |
| Manual classification | `np.where()` conditions |

### Activity 7: Zonal statistics by administrative boundary

To answer our research question, we need to summarize risk by area. "What percentage of each SA2 is at high flood risk?"

**Steps:**

1. Load SA2 boundaries for your study area (from Week 3 or ABS download)
2. Clip boundaries to study area if needed:
   - `Vector ▶ Geoprocessing Tools ▶ Clip`
3. Run zonal statistics:
   - `Processing ▶ Toolbox ▶ Zonal Statistics`
   - **Raster layer:** flood_risk_index.tif
   - **Vector layer:** SA2 boundaries
   - **Statistics to calculate:** Mean, Minimum, Maximum
   - **Output column prefix:** `risk_`
4. The SA2 layer now has new fields showing average risk per area

**Calculate percentage at high risk:**

5. Create a binary "high risk" raster (classes 3 or 4):
   ```
   "flood_risk_classes@1" >= 3
   ```
   Save as `high_risk_binary.tif`

6. Run zonal statistics again:
   - **Raster layer:** high_risk_binary.tif
   - **Statistics:** Mean
   - **Prefix:** `pct_high_`

   The mean of a binary raster (0/1) equals the proportion of 1s.
   Multiply by 100 to get percentage.

7. Style SA2 boundaries by `pct_high_risk_mean`:
   - Layer Properties → **Symbology** → **Graduated**
   - Color ramp: **Reds**
   - This shows which SA2s have the highest proportion of high-risk land

### Activity 8: Create your flood risk map

Compile your analysis into a professional map layout.

**Steps:**

1. Create a new Print Layout: `Project ▶ New Print Layout...` → name it "Flood Risk Assessment"
2. Add your main map showing:
   - Hillshade as the base (bottom layer)
   - Flood risk classes (semi-transparent)
   - SA2 boundaries (outlines only)
   - Rivers/waterways if available
3. Add a second map showing SA2s colored by % high risk
4. Add map elements:
   - **Title:** "Flood Risk Assessment: Hawkesbury-Nepean Region"
   - **Legend** with clear risk categories
   - **Scale bar**
   - **North arrow**
   - **Data sources:** "Elevation: ELVIS | Boundaries: ABS | Analysis: [Your Name], 2024"
   - **Methodology note:** "Risk based on elevation (60%) and slope (40%). Does not include hydrological modelling."
5. Export to `exports/week04_flood_risk.pdf` and `.png`

## Your Research Findings

After completing this analysis, summarize your findings:

### Research Question
"Which areas in the Hawkesbury-Nepean region are at elevated flood risk based on terrain characteristics?"

### Key Findings
Complete these based on your analysis:

1. The areas with highest flood risk are: _________________________________
2. Approximately ____% of the study area is classified as high or very high risk.
3. The SA2(s) with the greatest proportion of high-risk land: _________________________________

### Methodology
- **Data sources:** ELVIS DEM (___m resolution), ABS SA2 boundaries
- **Key parameters:** Elevation threshold: ___m, Slope threshold: ___°
- **Weights:** Elevation 60%, Slope 40%
- **Tools used:** QGIS Raster Calculator, Zonal Statistics

### Limitations
This analysis does NOT capture:

- [ ] Proximity to rivers and waterways
- [ ] Drainage infrastructure and stormwater systems
- [ ] Soil permeability and groundwater levels
- [ ] Historical flood extent data
- [ ] Hydrological flow modelling
- [ ] Climate change projections

### If this were your capstone
- How would you adapt this for your study area?
- What additional data would strengthen the analysis?
- What research question would you ask?

## Troubleshooting

### DEM appears blank or all one color
- **Stretch symbology:** Right-click raster → Properties → Symbology → Set Min/Max to "Cumulative count cut" (2-98%)
- **NoData values:** Large negative values (-9999) may skew the display

### Raster Calculator expression errors
- **Check layer names:** Use exact names as they appear in the Layers panel
- **Add @1:** Every raster reference needs `@1` suffix (e.g., `"dem@1"`)
- **Parentheses:** Ensure balanced parentheses in complex expressions

### Zonal statistics returns NULL
- **CRS mismatch:** Both layers must be in the same CRS
- **No overlap:** Check that boundaries actually cover the raster extent

### Processing is very slow
- **Clip first:** Reduce raster extent before analysis
- **Lower resolution:** Resample to 30m for testing, use full resolution for final output

## Support materials

- Slides: [Week 04 lecture deck](../slides/index.md)
- Lecture notes: [Elevation & Surface Modelling](../lectures/week04-raster-theory.md)
- Reading: [Raster Data Basics](../readings/week04-raster-basics.md)
- Dataset checklist: [Week 4 items](../reference/data-download-checklist.md)

## Reflect

Take 10-15 minutes to answer these questions in your [Week 4 reflection](../reference/reflections.md#week-4--raster--terrain):

- What terrain features correlate with flood risk in your study area?
- How did changing the elevation threshold affect your risk classification?
- Which SA2s would you prioritize for flood mitigation investment? Why?
- What are the biggest limitations of this terrain-only approach?
- How does this manual QGIS workflow compare to what you'll do in Python (Week 9)?

## What you'll submit

- [ ] QGIS project: `projects/week04_flood_risk.qgz`
- [ ] Derived rasters in `data/processed/week04/`:
  - `hillshade.tif`
  - `slope.tif`
  - `flood_risk_index.tif`
  - `flood_risk_classes.tif`
- [ ] Flood risk map (PDF): `exports/week04_flood_risk.pdf`
- [ ] Completed "Your Research Findings" section (in reflection or separate document)
- [ ] Your Week 4 reflection entry

!!! danger "Map submission requirements"
    Your exported map **must** include: **Title**, **Legend**, **Scale bar**, and **North arrow**. Maps missing any of these elements will not be accepted. See [Map Design Principles](../reference/design-rubric.md).

## Coming up next week

Week 5 applies similar spatial analysis thinking to crime data. You'll use kernel density estimation to identify hotspots and learn about the ethical considerations of mapping sensitive data. The "research question" approach continues—you'll ask "Where are crime hotspots and what factors correlate with them?"
