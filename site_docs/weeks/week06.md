# Week 6 · Public Health & Accessibility

Access to healthcare isn't just about having facilities nearby—it's about whether people can actually reach them. This week, you'll use network analysis to measure healthcare accessibility, combining vulnerability indices with travel-time analysis to identify communities that face barriers to essential services. You'll learn techniques that apply equally to hospitals, vaccination clinics, food banks, or any other critical infrastructure.

## What you'll learn

By the end of this week, you'll be able to:

1. Prepare and validate health facility point data (hospitals, clinics, pharmacies).
2. Set up network analysis in QGIS using road network data and calculate travel-time service areas (isochrones).
3. Overlay service areas with socio-economic vulnerability data (SEIFA, ARIA+, or local equivalents) to identify underserved populations.
4. Quantify and map accessibility gaps, creating evidence for planning interventions.

## Before you start

- [ ] Review the lecture: [Week 6 · Health Equity & Accessibility](../lectures/week06-health-theory.md)
- [ ] Download health facility locations (hospitals, clinics) via [Downloading datasets](../onboarding/03-download-data.md)
- [ ] Download or extract OpenStreetMap road network for your study area (see data guide)
- [ ] Install the **QNEAT3** plugin: `Plugins ▶ Manage and Install Plugins... ▶ search "QNEAT3" ▶ Install Plugin`
- [ ] Reopen your Week 3 project to access SEIFA or vulnerability layers
- [ ] Confirm Week 6 datasets are checked off in the [data download checklist](../reference/data-download-checklist.md)

!!! tip "Plugin troubleshooting"
    If QNEAT3 doesn't appear after installation, restart QGIS. If you encounter errors, check that your road network has proper line geometry and no gaps.

## This week's activities

### Activity 1: Prepare your health facility data

You'll work with point locations for healthcare facilities—hospitals, clinics, urgent care centers, or similar services depending on your region.

**Steps:**

1. Load your health facility dataset (CSV, shapefile, or GeoJSON)
2. Inspect the attribute table to verify:
   - Coordinates are accurate (cross-check a few against online maps)
   - Facility types are labeled (hospital, clinic, pharmacy, etc.)
   - Operating status (active vs. closed)
3. Filter to relevant facility types using `Select by Expression`
4. Clean the data:
   - Remove duplicate points (same name + coordinates)
   - Remove facilities with missing coordinates
   - Standardize naming conventions if needed
5. Save filtered facilities to `data/processed/week06/health_facilities.gpkg`
6. Add basemap imagery (QuickMapServices or XYZ Tiles) to visually verify locations

!!! note "Data quality matters"
    Incorrect coordinates can dramatically skew accessibility analysis. Spot-check at least 5-10 facilities by comparing their mapped location to satellite imagery or street maps.

### Activity 2: Prepare your road network

Network analysis requires a connected road network. You'll use OpenStreetMap data, which is free and covers most of the world.

**Steps:**

1. **Option A: Download OSM extract**
   - Visit [download.geofabrik.de](https://download.geofabrik.de/) or [BBBike](https://extract.bbbike.org/)
   - Download shapefile extract for your region
   - Load the `roads` or `lines` layer into QGIS

2. **Option B: Use QuickOSM plugin** (for smaller areas)
   - Install QuickOSM plugin if needed
   - `Vector ▶ QuickOSM ▶ Quick Query`
   - Key: `highway`, leave value blank to get all roads
   - Set extent to your study area
   - Click Run Query

3. **Clean the network:**
   - Keep major road types: `"highway" IN ('motorway', 'trunk', 'primary', 'secondary', 'tertiary', 'residential')`
   - Remove footpaths, cycleways, or paths unless you're analyzing walk/bike access
   - Clip to your study area boundary to reduce processing time
   - Save to `data/processed/week06/road_network.gpkg`

4. Verify the network visually—it should form a connected web with no major gaps

### Activity 3: Calculate service areas (isochrones)

Isochrones show how far you can travel from a location in a given time. You'll create 5, 10, and 15-minute drive-time zones around health facilities.

**Steps:**

1. Open Processing Toolbox and search for **"QNEAT3 - Iso-Area as Polygons from Point"**
2. Configure the tool:
   - **Vector layer representing network:** your road_network layer
   - **Start points:** health_facilities layer
   - **Unique Point ID field:** facility name or ID
   - **Size of iso-area (distance or time value):** enter `5` (for 5 minutes)
   - **Contour interval:** `5` (creates zones at 5, 10, 15 minutes)
   - **Path type to calculate:** Choose "Shortest" (time-based if you have speed data)
   - **Output:** save to `data/processed/week06/health_service_areas.gpkg`
3. Click Run (this may take several minutes)
4. Style the output with graduated colors (5min = dark green, 10min = medium, 15min = light)
5. Adjust transparency to see overlapping service areas

!!! warning "Processing time"
    Network analysis can be slow for large networks or many facilities. Start with a small study area (one city or region) and a subset of facilities to test your workflow. You can scale up once it's working.

**Interpret the results:**
- Where do service areas overlap? (Good coverage)
- Where are the gaps? (Underserved areas)
- Do service areas cross administrative boundaries?

### Activity 4: Overlay with vulnerability data

Now you'll identify which communities fall outside adequate healthcare access, focusing on vulnerable populations.

**Steps:**

1. Load your SEIFA disadvantage layer (or ARIA+, SVI, etc.) from Week 3
2. Identify highly disadvantaged areas:
   - Select SA2 polygons in the bottom 20% (deciles 1-2) using `Select by Expression`
   - Save selection to `data/processed/week06/high_disadvantage.gpkg`
3. Find underserved vulnerable areas:
   - Use `Processing ▶ Vector overlay ▶ Difference` to identify disadvantaged areas NOT covered by 15-minute service areas
   - Alternatively, use `Select by Location`: select high-disadvantage polygons that don't intersect with service areas
   - Save result to `data/processed/week06/accessibility_gaps.gpkg`
4. Calculate summary statistics:
   - How many SA2 areas are underserved?
   - What's the total population living outside 15-minute access?
   - Which LGAs have the worst coverage?

!!! tip "Drive time vs. reality"
    Drive-time analysis assumes car ownership. Consider creating separate isochrones for walking (15-minute walk ≈ 1km) or public transit if data is available. Accessibility gaps are often much larger for non-drivers.

### Activity 5: Visualize and communicate findings

Create a compelling map that tells the accessibility story.

**Steps:**

1. Create a new Print Layout for your accessibility map
2. Include these layers (experiment with order and styling):
   - Basemap (light gray or muted satellite)
   - SEIFA/vulnerability layer (choropleth showing disadvantage)
   - Health facility points (hospital icons or sized by capacity)
   - 15-minute service area polygons (green outline, high transparency)
   - Accessibility gap areas (highlighted in red or orange)
3. Add map elements:
   - Clear title: "Healthcare Accessibility Gaps in [Region]"
   - Legend explaining all layers
   - Text box with 2-3 key findings
   - Data sources and date
4. Export to `exports/week06_health_accessibility.pdf`

**Challenge:** Create an inset map zooming into one particularly underserved area to show local detail.

### Activity 6: Document your method (preparing for Python)

Next week you'll transition to Python. Start building good documentation habits now.

**Steps:**

1. Create a text file: `projects/week06_method_notes.txt`
2. Document:
   - Where you got your data (URLs, download dates)
   - Any cleaning or filtering steps you performed
   - QNEAT3 parameters you used (time values, contour intervals)
   - Assumptions you made (e.g., "assumes car ownership," "used 15-min threshold")
   - Limitations (e.g., "OSM data may be incomplete in rural areas")
3. This documentation will help you (and others) reproduce your analysis later

## Support materials

- Slides: [Week 06 lecture deck](../slides/index.md)
- Lecture notes: [Health Equity & Accessibility](../lectures/week06-health-theory.md)
- Plugin guide: [QNEAT3 documentation](https://root676.github.io/)
- Dataset checklist: [Week 6 items](../reference/data-download-checklist.md)
- Case study: [Malaria Atlas Project](https://malariaatlas.org/) — example of global health GIS

## Reflect

Take 10-15 minutes to answer these questions in your [Week 6 reflection](../reference/reflections.md#week-6--health-accessibility):

- Which areas had the worst accessibility? Were you surprised?
- How would your findings change if you analyzed walking access instead of driving?
- What additional data would strengthen this analysis (transit routes, facility capacity, wait times)?
- Who are the stakeholders for this type of analysis? How might different groups use (or misuse) these findings?
- How confident are you in your results? What are the biggest sources of uncertainty?

## What you'll submit

- [ ] QGIS project (`projects/week06_health_accessibility.qgz`) with service areas and gap analysis
- [ ] Accessibility map (PDF) showing vulnerable populations and service gaps
- [ ] Brief summary table: number of underserved areas, population affected, key findings
- [ ] Method documentation file
- [ ] Your Week 6 reflection entry

## Coming up next week

Week 7 is the bridge to Python. You'll install Anaconda, set up your Python environment, and see how the QGIS workflows you've mastered can be automated with code. Make sure you have disk space available (~5 GB) and review the [Python Setup Guide](../onboarding/04-python-setup.md) before next session.
