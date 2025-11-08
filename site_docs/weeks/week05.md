# Week 5 · Crime Hotspots & Ethical Mapping

Crime data is sensitive, powerful, and often misunderstood. This week, you'll learn how to map incident patterns responsibly using hotspot analysis techniques—while staying mindful of the ethical considerations that come with visualizing crime data. You'll work with real crime datasets to identify spatial patterns, compare different boundary systems, and practice framing your findings in ways that support communities rather than stigmatize them.

## What you'll learn

By the end of this week, you'll be able to:

1. Download, filter, and prepare crime incident data for spatial analysis.
2. Apply kernel density estimation (KDE) and hex binning techniques to identify hotspots in QGIS.
3. Compare how different administrative boundaries (LGA, police districts, suburbs) shape the story your analysis tells.
4. Frame crime analysis findings responsibly, considering context, community impact, and data limitations.

## Before you start

- [ ] Review the lecture: [Week 5 · Ethics of Crime Mapping](../lectures/week05-crime-ethics.md) — this is essential background
- [ ] Download crime incident datasets via [Downloading datasets](../onboarding/data-downloads.md) (e.g., NSW Recorded Crime, Chicago Crime Data, or local equivalent)
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

1. Open the Processing Toolbox (`Processing ▶ Toolbox`)
2. Search for "Heatmap (Kernel Density Estimation)"
3. Configure the tool:
   - **Point layer:** your filtered crime incidents
   - **Radius:** start with 500 meters (you'll experiment with this)
   - **Pixel size:** 50 meters (smaller = more detail, larger file)
   - **Output:** save to `data/processed/week05/crime_kde.tif`
4. Click Run and wait for the raster to generate
5. Style the output using a warm color ramp (yellow → orange → red)
6. Adjust raster transparency (50-70%) so you can see boundary layers underneath

**Experiment:** Try different radius values (250m, 500m, 1000m). How does the bandwidth setting change what patterns emerge?

!!! tip "Understanding bandwidth"
    A smaller radius shows very localized hotspots but can be "noisy." A larger radius smooths the pattern but might hide important detail. There's no single "right" answer—it depends on your research question and the scale you're working at.

### Activity 3: Compare with hex bins

Hex bins are an alternative to KDE that group incidents into equal-area hexagons. This can make patterns easier to communicate to non-technical audiences.

**Steps:**

1. Create a hexagonal grid over your study area:
   - `Processing ▶ Toolbox ▶ Create Grid`
   - **Grid type:** Hexagon
   - **Horizontal/Vertical spacing:** 500 meters
   - **Grid extent:** use your boundary layer or draw a custom extent
   - Save to `data/processed/week05/hex_grid.gpkg`
2. Count incidents per hexagon:
   - `Processing ▶ Toolbox ▶ Count Points in Polygon`
   - **Polygons:** hex_grid
   - **Points:** crime_filtered
   - Save output to `data/processed/week05/crime_hex_counts.gpkg`
3. Style using graduated symbology (quantile classification, 5 classes)
4. Compare the hex bin map to your KDE output—which tells a clearer story?

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

## Support materials

- Slides: [Week 05 lecture deck](../../assets/slides/week05.html)
- Lecture notes: [Ethics of Crime Mapping](../lectures/week05-crime-ethics.md)
- Dataset checklist: [Week 5 items](../reference/data-download-checklist.md)
- Optional reading: Responsible crime mapping guidelines (link in lecture notes)

## Reflect

Take 10-15 minutes to answer these questions in your [Week 5 reflection](../reference/reflections.md#week-5--crime-mapping):

- What patterns did you discover? Were you surprised by any results?
- How did changing the bandwidth (KDE radius) or boundary system affect the story?
- What context layers helped explain the hotspots you identified?
- What are the ethical risks of publishing a map like this? Who might benefit? Who might be harmed?
- How would you present these findings to a community group versus a police department?

## What you'll submit

- [ ] QGIS project (`projects/week05_crime_hotspots.qgz`) with KDE raster and hex bins
- [ ] At least two comparison maps showing different boundary aggregations or methods
- [ ] Brief written interpretation (1 paragraph) explaining patterns and limitations
- [ ] Your Week 5 reflection entry

## Coming up next week

Week 6 shifts from crime to public health and accessibility. You'll combine vulnerability indices (SEIFA, health risk data) with service locations to evaluate equity in healthcare access. Start thinking about how the network analysis concepts might apply to measuring access to hospitals, clinics, or other essential services.
