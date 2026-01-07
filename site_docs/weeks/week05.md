# Week 5 · Crime Hotspot Analysis

## Research Question

> **"Where are crime hotspots located, and how do different mapping techniques and boundary choices shape the story we tell about safety?"**

Crime data is sensitive, powerful, and often misunderstood. This week, you'll learn how to map incident patterns responsibly using hotspot analysis techniques—while staying mindful of the ethical considerations that come with visualizing crime data. You'll work with real crime datasets to identify spatial patterns, compare different boundary systems, and practice framing your findings in ways that support communities rather than stigmatize them.

## What you'll learn

By the end of this week, you'll be able to:

1. Download, filter, and prepare crime incident data for spatial analysis.
2. Apply kernel density estimation (KDE) and hex binning techniques to identify hotspots in QGIS.
3. Compare how different administrative boundaries (LGA, police districts, suburbs) shape the story your analysis tells.
4. Frame crime analysis findings responsibly, considering context, community impact, and data limitations.

## Before you start

- [ ] Review the lecture: [Week 5 · Ethics of Crime Mapping](../lectures/week05-crime-ethics.md) — this is essential background
- [ ] Download crime incident datasets via [Downloading datasets](../onboarding/03-download-data.md) (e.g., NSW Recorded Crime, Chicago Crime Data, or local equivalent)
- [ ] Reopen your Week 3 project with boundary layers (SA2, LGA) — you'll use these for comparison
- [ ] Read about responsible crime mapping practices in the lecture notes
- [ ] Confirm Week 5 datasets are checked off in the [data download checklist](../reference/data-download-checklist.md)

## This week's activities

### Activity 1: Prepare your crime data

Before you can analyze patterns, you need clean, well-structured data. You'll filter by offense type, date range, and location quality.

**Steps:**

1. Download your chosen crime dataset (CSV or shapefile format)
2. Load the data into QGIS using `Layer ▶ Add Layer ▶ Add Delimited Text Layer…`
3. Inspect the attribute table to understand available fields (offense type, date, location quality)
4. Filter to a specific time period (e.g., 2023 incidents only) using `Select by Expression`
5. Optionally filter to specific offense types (e.g., property crime, assault) depending on your research question
6. Export the filtered subset to a GeoPackage: `Export ▶ Save Features As...` → save to `data/processed/week05/crime_filtered.gpkg`

!!! warning "Privacy & aggregation"
    Most public crime datasets are already anonymized and aggregated to protect privacy. Never map individual addresses or use crime data to identify specific people or households. Always work at the aggregate level.

### Activity 2: Create a kernel density heatmap

Kernel Density Estimation (KDE) helps you identify areas with unusually high concentrations of incidents—commonly called "hotspots."

**Steps:**

1. Open the Processing Toolbox: `Processing ▶ Toolbox` (or press `Ctrl+Alt+T`)
2. In the search box, type "Heatmap" and select **Heatmap (Kernel Density Estimation)**
3. Configure the tool parameters:
   - **Point layer:** your filtered crime incidents (`crime_filtered`)
   - **Radius:** 500 meters (you'll experiment with this later)
   - **Pixel size X/Y:** 50 meters (smaller = more detail but larger file)
   - **Kernel shape:** Quartic (default, works well for most cases)
   - **Output raster:** click `...` → Save to File → `data/processed/week05/crime_kde.tif`
4. Click **Run** and wait for processing (may take 1-2 minutes for large datasets)

**Style the heatmap:**

5. Right-click the new raster layer → **Properties** → **Symbology**
6. Change render type to **Singleband pseudocolor**
7. Set color ramp to **YlOrRd** (yellow-orange-red) or **Reds**
8. Set **Mode** to **Continuous** and click **Classify**
9. In the **Transparency** tab, set global opacity to 60-70%
10. Click **Apply** then **OK**

**Checkpoint:** You should see a smooth gradient with red areas showing highest density. The pattern should roughly match where you saw clusters when viewing the raw points.

**Experiment with bandwidth:**

| Radius | Effect | Best for |
|--------|--------|----------|
| 250m | Very localized hotspots, more "speckled" | Street-level analysis, dense urban areas |
| 500m | Balanced detail and smoothness | Neighborhood-level patterns |
| 1000m | Broad regional patterns, very smooth | City-wide comparisons, presentations |

Try all three and compare. Save each with a descriptive name (e.g., `crime_kde_250m.tif`).

!!! tip "Choosing the right bandwidth"
    A smaller radius shows localized hotspots but can be "noisy." A larger radius smooths patterns but might hide important detail. Consider: What scale are you analyzing? Street blocks? Neighborhoods? The whole city? Match your bandwidth to your question.

!!! warning "Edge effects"
    KDE values drop near the edges of your study area because there are fewer points to count. This is a known limitation—don't interpret low values near boundaries as "safe zones" without checking the raw data.

### Activity 3: Compare with hex bins

Hex bins are an alternative to KDE that group incidents into equal-area hexagons. This can make patterns easier to communicate to non-technical audiences.

**Step 1: Create a hexagonal grid**

1. Open Processing Toolbox: `Processing ▶ Toolbox`
2. Search for "Create grid" and select **Create grid**
3. Configure:
   - **Grid type:** Hexagon (H)
   - **Grid extent:** Click `...` → Calculate from Layer → select your LGA or study area boundary
   - **Horizontal spacing:** 500 meters
   - **Vertical spacing:** 500 meters
   - **Grid CRS:** Use the same CRS as your crime data (check layer properties if unsure)
   - **Output:** `data/processed/week05/hex_grid.gpkg`
4. Click **Run**

**Step 2: Count incidents per hexagon**

5. Search for "Count points in polygon" in Processing Toolbox
6. Configure:
   - **Polygons:** hex_grid (your new hexagon layer)
   - **Points:** crime_filtered
   - **Count field name:** `crime_count`
   - **Output:** `data/processed/week05/crime_hex_counts.gpkg`
7. Click **Run**

**Step 3: Style the hex bins**

8. Right-click crime_hex_counts → **Properties** → **Symbology**
9. Change from Single Symbol to **Graduated**
10. Set **Value** to `crime_count`
11. Set **Mode** to **Quantile (Equal Count)** and **Classes** to 5
12. Choose a sequential color ramp (e.g., YlOrRd)
13. Click **Classify** then **Apply**

**Checkpoint:** You should see a honeycomb pattern with darker hexagons where incidents cluster. Empty hexagons (0 incidents) should be in the lightest color or transparent.

**Compare KDE vs Hex bins:**

| Aspect | KDE Heatmap | Hex Bins |
|--------|-------------|----------|
| Output type | Continuous raster | Discrete polygons |
| Values | Density estimate | Actual counts |
| Best for | Smooth visualization | Exact counts, statistics |
| Communication | General audiences | Technical reports |

!!! tip "When to use which"
    Use KDE for visual storytelling and identifying general patterns. Use hex bins when you need to report specific counts or when your audience wants to query individual cells.

### Activity 4: Boundary comparison

The boundaries you choose dramatically affect how crime data is interpreted. You'll aggregate incidents by different administrative units and see how the narrative changes.

**Steps:**

1. Aggregate incidents by **LGA** (Local Government Area):
   - Use `Count Points in Polygon` with your LGA layer from Week 3
   - Calculate incident rate per 1,000 residents using Field Calculator: `"crime_count" / "population" * 1000`
   - Map using graduated symbology
2. Repeat for **SA2** or another boundary level
3. Repeat for **police districts** (if available in your region)
4. Create three maps side-by-side in a layout or export separately for comparison

**Discussion:** Which boundary level seems most appropriate for communicating with:
- Local residents?
- Police departments?
- Urban planners?

!!! note "Context matters"
    High crime counts don't always mean high crime rates—densely populated areas naturally have more incidents. Always normalize by population or area when comparing regions.

### Activity 5: Temporal patterns (optional)

If your dataset includes timestamps, explore how patterns change over time.

**Steps:**

1. Use `Select by Expression` to filter incidents by time period (e.g., `"date" >= '2023-01-01' AND "date" < '2023-04-01'` for Q1)
2. Run KDE separately for each quarter or month
3. Compare outputs by toggling layers on/off
4. Note any seasonal patterns or emerging hotspots

### Activity 6: Storytelling with context

Raw hotspot maps can be misleading without context. You'll add supporting layers that help explain patterns.

**Steps:**

1. Add contextual layers to your map:
   - Transit stops (from Week 6 prep or OSM)
   - SEIFA disadvantage index (from Week 3)
   - Land use zones (commercial, residential, parks)
   - Street lighting or pedestrian infrastructure (if available)
2. Identify correlations: Do hotspots align with transit hubs? Commercial zones? Areas of high disadvantage?
3. Draft 2-3 bullet points summarizing patterns you observe
4. Write a one-paragraph interpretation that acknowledges both the patterns AND the limitations of your analysis

!!! warning "Avoid stigmatization"
    When presenting findings, focus on environmental and systemic factors, not on labeling neighborhoods as "dangerous." Consider how your maps might be used—or misused—by media, police, or policymakers.

### Activity 7: What isn't mapped

Your crime hotspot map shows reported and recorded incidents. Now let's think critically about what it DOESN'T show—this is a professional skill that separates good analysts from great ones.

**The question:** Every dataset answers some questions well and makes others almost impossible to ask. What questions can't this data answer?

**Steps:**

1. **List what's missing:**
   Open a text file or your reflection document. Spend 5 minutes listing things that might matter for understanding "safety" or "crime" that your data doesn't include:

   - Unreported crimes (estimates suggest 40-60% of crimes go unreported)
   - Crimes that are reported but not recorded
   - White-collar and corporate crime (rarely mapped spatially)
   - Historical patterns—displacement, disinvestment, redlining
   - Perception of safety (fear vs. actual risk)
   - Community assets—mutual aid networks, neighborhood watch, community centers
   - Where offenders live vs. where offenses occur

2. **Identify what's hard to map:**
   Some things are genuinely difficult to represent spatially. Note at least three:

   - Trust in police (affects reporting patterns, but how do you map it?)
   - Informal justice and conflict resolution
   - The *causes* behind concentrations (poverty, lack of services, historical policy)
   - Time dimension—crime patterns shift by hour, season, year

3. **Reframe your findings:**
   Write two different one-sentence summaries of your hotspot map:

   **Version A (what your map shows):**
   > "This map shows reported [crime type] incidents per [unit], revealing concentrations in [areas]."

   **Version B (what your map doesn't show):**
   > "This map does NOT show unreported crimes, fear of crime, community safety resources, police patrol patterns, or the historical policies that shaped these patterns."

4. **Connect to professional practice:**
   If you were presenting this analysis to:
   - A police department
   - A community organization
   - A journalist

   What context would you add? What would you warn them NOT to conclude?

!!! note "Why this matters"
    "What isn't mapped" isn't an academic exercise—it's a professional skill. The best analysts know what their data CAN'T answer as well as what it can. This prevents overconfident conclusions and helps you seek complementary information.

**Reflection prompt:** What's one thing you wish you could map about safety or crime that current data can't capture? What would it take to create that data?

## Troubleshooting

### KDE produces a blank or all-zero raster
- **Check CRS:** Your points must be in a projected CRS (meters), not geographic (degrees). Reproject using `Vector ▶ Data Management Tools ▶ Reproject Layer` to a local CRS like EPSG:28356 (GDA2020 / MGA Zone 56 for eastern Australia)
- **Check radius units:** If your data is in degrees but you specified 500 meters, the tool may not work correctly
- **Check point count:** Very few points (<50) may not produce visible density

### Hex grid doesn't align with study area
- **CRS mismatch:** Ensure grid CRS matches your boundary layer
- **Extent issue:** Try using "Calculate from Layer" instead of drawing manually
- **Spacing too large:** For small areas, try 250m or 100m spacing

### Count Points in Polygon returns zeros
- **CRS mismatch:** Both layers must be in the same CRS
- **Points outside polygons:** Check if your points fall within the grid extent
- **Empty geometries:** Some polygons may have invalid geometry—run `Vector ▶ Geometry Tools ▶ Fix Geometries`

### Heatmap appears "blocky" or pixelated
- **Pixel size too large:** Reduce from 50m to 25m or 10m (warning: larger file size)
- **Radius too small:** Increase bandwidth for smoother appearance

### Performance issues with large datasets
- **Filter first:** Reduce to a subset (one year, one offense type) before running KDE
- **Increase pixel size:** 100m instead of 50m processes much faster
- **Clip to study area:** Don't process the entire state if you only need one city

## Your Research Findings

After completing this week's analysis, summarize your findings:

### Research Question
"Where are crime hotspots located, and how do different mapping techniques and boundary choices shape the story we tell about safety?"

### Key Findings
Complete these based on your analysis:

1. The primary hotspots are located in: _________________________________
2. The hotspot pattern correlates with: _________________________________ (transit hubs? commercial zones? specific land uses?)
3. Changing the KDE bandwidth from 250m to 1000m made the pattern: _________________________________
4. Aggregating by different boundaries (LGA vs SA2 vs hex bins) changed the story by: _________________________________

### Methodology
- **Data source:** _________________________________ (BOCSAR, data.police.uk, etc.)
- **Key parameters:** KDE bandwidth: _____m, Hex grid size: _____m
- **Tools used:** KDE Heatmap, Hex grid, Count Points in Polygon, Field Calculator

### Limitations
This analysis does NOT capture:

- [ ] Unreported crimes (estimated 40-60% go unreported)
- [ ] Reporting bias (some areas have more police presence → more reports)
- [ ] Changes over time (point-in-time snapshot only)
- [ ] Root causes of crime patterns
- [ ] Community assets and resilience factors

### Ethical considerations
How this analysis could be **misused:**

- _________________________________

How this analysis could **support communities:**

- _________________________________

### If this were your capstone
- What additional context layers would you add?
- How would you present findings to a community group vs. police department?
- What research question would you ask?

## Support materials

- Slides: [Week 05 lecture deck](../slides/index.md)
- Lecture notes: [Ethics of Crime Mapping](../lectures/week05-crime-ethics.md)
- Dataset checklist: [Week 5 items](../reference/data-download-checklist.md)

## Reflect

Take 10-15 minutes to answer these questions in your [Week 5 reflection](../reference/reflections.md#week-5--crime-mapping):

- What patterns did you discover? Were you surprised by any results?
- How did changing the bandwidth (KDE radius) or boundary system affect the story?
- What context layers helped explain the hotspots you identified?
- What are the ethical risks of publishing a map like this? Who might benefit? Who might be harmed?
- How would you present these findings to a community group versus a police department?

## What you'll submit

- [ ] QGIS project: `projects/week05_crime_hotspots.qgz`
- [ ] KDE heatmap raster: `data/processed/week05/crime_kde.tif`
- [ ] Hex bin counts layer: `data/processed/week05/crime_hex_counts.gpkg`
- [ ] Comparison layout (PDF or PNG): Three maps showing same data aggregated by LGA, SA2, and hex bins
- [ ] Written interpretation (1 paragraph): Describe patterns observed and at least 2 limitations of your analysis
- [ ] Your Week 5 reflection entry

!!! danger "Map submission requirements"
    Your exported maps **must** include: **Title**, **Legend**, **Scale bar**, and **North arrow**. Maps missing any of these elements will not be accepted. See [Map Design Principles](../reference/design-rubric.md).

## Coming up next week

Week 6 shifts from crime to public health and accessibility. You'll combine vulnerability indices (SEIFA, health risk data) with service locations to evaluate equity in healthcare access. Start thinking about how the network analysis concepts might apply to measuring access to hospitals, clinics, or other essential services.
