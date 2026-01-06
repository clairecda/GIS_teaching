# Week 6 · Public Health & Accessibility

Access to healthcare isn't just about having facilities nearby—it's about whether people can actually reach them. This week, you'll use network analysis to measure healthcare accessibility, combining vulnerability indices with travel-time analysis to identify communities that face barriers to essential services. You'll learn techniques that apply equally to hospitals, vaccination clinics, food banks, or any other critical infrastructure.

## What you'll learn

By the end of this week, you'll be able to:

1. Prepare and validate health facility point data (hospitals, clinics, pharmacies).
2. Set up network analysis in QGIS using road network data and calculate travel-time service areas (isochrones).
3. Calculate shortest paths to identify travel times from communities to facilities.
4. Overlay service areas with socio-economic vulnerability data (SEIFA, ARIA+, or local equivalents) to identify underserved populations.
5. Quantify and map accessibility gaps, creating evidence for planning interventions.

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

**Step 1: Verify your network is ready**

Before running QNEAT3, check your road network:

1. Right-click road_network → **Properties** → **Information**
2. Confirm geometry type is `LineString` or `MultiLineString`
3. Verify CRS is projected (meters), not geographic (degrees)
4. Check the layer has an ID field (or create one with Field Calculator: `$id`)

**Step 2: Run the isochrone analysis**

1. Open Processing Toolbox: `Processing ▶ Toolbox`
2. Search for "Iso-Area" and select **QNEAT3 → Iso-Area as Polygons (from Point)**
3. Configure parameters:

| Parameter | Value | Explanation |
|-----------|-------|-------------|
| **Network layer** | road_network | Your prepared road layer |
| **Start points** | health_facilities | Facility locations |
| **Unique Point ID field** | Select your facility name or ID field | Identifies each service area |
| **Size of Iso-Area** | `900` | 15 minutes × 60 seconds = 900 seconds |
| **Contour interval** | `300` | Creates zones at 5min (300s), 10min (600s), 15min (900s) |
| **Cell size** | `50` | Resolution in meters (smaller = more detail, slower) |
| **Direction field** | Leave blank | Unless you have one-way street data |
| **Default speed** | `50` | km/h for driving (use 5 for walking) |
| **Output** | `data/processed/week06/health_service_areas.gpkg` | |

4. Click **Run** — this may take 5-15 minutes depending on network size

**Step 3: Style the service areas**

5. Right-click the output layer → **Properties** → **Symbology**
6. Change to **Categorized** symbology
7. Set **Value** to the time/cost field (often `cost` or `iso_value`)
8. Choose a sequential color ramp: dark green (5min) → yellow (10min) → orange (15min)
9. Set layer transparency to 50% in the **Transparency** tab

**Checkpoint:** You should see concentric polygons around each facility. The 5-minute zones should be smallest (closest to facilities), expanding outward to 15-minute zones. Zones from nearby facilities will overlap—this indicates good coverage.

**Expected output characteristics:**

| Zone | Approximate size (driving) | Approximate size (walking) |
|------|---------------------------|----------------------------|
| 5 minutes | 2-4 km radius | 400-500m radius |
| 10 minutes | 5-8 km radius | 800-1000m radius |
| 15 minutes | 8-12 km radius | 1.2-1.5 km radius |

If your zones are much larger or smaller, check your speed setting and CRS.

!!! warning "Processing time and memory"
    Network analysis is computationally intensive. If QGIS freezes or runs out of memory:
    - Reduce the number of facilities (test with 5-10 first)
    - Clip your road network to a smaller area
    - Increase cell size from 50 to 100 meters
    - Close other applications to free memory

**Interpret the results:**

- **Overlapping zones:** Good coverage—residents can reach multiple facilities
- **Gaps between zones:** Underserved areas needing attention
- **Irregular shapes:** Reflect road network constraints (rivers, highways, terrain)

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

### Activity 4.5: Invisible barriers

Your service area analysis calculates travel time along roads. But real-world access involves barriers that don't appear in road network data. This activity builds the critical thinking that distinguishes good analysis from great analysis.

**The question:** What barriers to healthcare access are invisible to our analysis?

**Steps:**

1. **List invisible barriers:**
   Your isochrone analysis assumes someone can drive a car at average speed. List at least five barriers that would prevent someone from reaching a facility even if they're "within 15 minutes":

   - No car access or can't drive
   - Can't afford fuel, parking, or time off work
   - Disability limiting mobility
   - No childcare during appointment time
   - Language barriers at the facility
   - Cultural barriers (gender of provider, past discrimination, distrust)
   - Operating hours conflict with work schedule
   - Fear of immigration enforcement
   - Facility doesn't accept their insurance or Medicare
   - Long wait times after arrival

2. **Map what you can:**
   Some barriers have proxy data. If available, try adding one of these layers:

   - Car ownership rates by SA2 (census data)
   - Public transit routes (OpenStreetMap or local transport authority)
   - Languages spoken at home (census)
   - SEIFA disadvantage (already loaded from Week 3)

   How does adding this layer change your interpretation of "accessibility gaps"?

3. **Acknowledge limitations in your output:**
   Add a text box to your layout (or include in your method notes):

   > "This analysis measures drive-time accessibility only. It does not account for car ownership, public transit access, appointment availability, insurance acceptance, language services, or other factors affecting real-world access."

4. **Reframe from deficit to action:**
   Instead of labeling areas as "underserved" or "lacking access" (deficit framing), reframe your findings in action-oriented language:

   - **Deficit:** "These communities lack adequate healthcare access"
   - **Action:** "These communities would benefit from mobile clinic services, extended hours, or transit partnerships"

   Both describe the same gap, but one stigmatizes communities and the other points toward solutions.

!!! tip "Why language matters"
    Deficit framing puts the problem *in* communities. Action framing puts the problem *in* systems. As a GIS analyst, you have power over how gaps are described—use that power thoughtfully.

**Reflection prompt:** If you could add one "invisible barrier" to your analysis, which would most change your conclusions? What data would you need to map it?

### Activity 5: Calculate shortest paths (routes to facilities)

Beyond service areas, you can calculate the actual route someone would take to reach a facility. This is useful for understanding travel patterns, emergency response times, and identifying communities with poor road connections.

**Steps:**

1. Open Processing Toolbox: `Processing ▶ Toolbox`
2. Search for "Shortest path" and select **QNEAT3 → Shortest Path (Point to Point)**
3. Configure parameters:

| Parameter | Value |
|-----------|-------|
| **Network layer** | road_network |
| **Start point** | Click "..." and select a location (e.g., a community center) |
| **End point** | Click "..." and select a hospital |
| **Direction field** | Leave blank unless you have one-way data |
| **Default speed** | 50 (km/h for driving) or 5 (km/h for walking) |
| **Output** | shortest_path.gpkg |

4. Click **Run** — the output is a line showing the optimal route
5. Open the attribute table to see the total travel time and distance

**Batch routes from multiple locations:**

1. Search for **QNEAT3 → Shortest Path (Layer to Point)**
2. Set **Start points** to a layer of community locations or population centers
3. Set **End point** to your main hospital
4. Run — this creates routes from every origin to the hospital
5. Style routes by travel time (graduated colors) to identify which communities have the longest trips

**Interpret the results:**

- Long travel times may indicate need for closer facilities or better transport links
- Compare drive routes vs. walk routes — the gap reveals car dependency
- Routes that cross barriers (rivers, highways) may be longer than straight-line distance suggests

**Compare to Python:**

In Week 10, you'll automate route calculations with NetworkX in Python. The QGIS workflow is ideal for exploring individual routes; Python scales to hundreds of origin-destination pairs.

### Activity 6: Visualize and communicate findings

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

### Activity 7: Document your method (preparing for Python)

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

## Troubleshooting

### QNEAT3 plugin not visible
- **Restart QGIS** after installing the plugin
- Check `Plugins ▶ Manage and Install Plugins... ▶ Installed` to confirm QNEAT3 is checked
- Some QGIS versions have compatibility issues—try updating QGIS to latest LTR

### "No valid network" or empty output
- **CRS mismatch:** Network and start points must be in the same projected CRS
- **Network not connected:** Check for gaps in your road network using `Vector ▶ Analysis Tools ▶ Line Intersections` to find disconnected segments
- **Start points not on network:** Facilities must be close to road segments. Use `Processing ▶ Vector geometry ▶ Snap geometries to layer` to snap points to the nearest road

### Isochrones are unexpectedly large or small
- **Speed setting:** Default 50 km/h is for driving. Use 5 km/h for walking, 15-20 km/h for cycling
- **Size units:** The "Size of Iso-Area" is in the network's cost units. For time-based analysis, use seconds (900 = 15 minutes)
- **CRS in degrees:** If your CRS is geographic (EPSG:4326), distances are calculated incorrectly. Reproject to a local projected CRS

### QGIS crashes or freezes during processing
- **Too many points:** Start with 5-10 facilities to test
- **Network too large:** Clip to a smaller study area
- **Memory issue:** Increase cell size from 50 to 100 or 200 meters
- **Save your work** before running long processes

### Service areas have strange shapes or holes
- **Network topology issues:** Run `Vector ▶ Geometry Tools ▶ Fix Geometries` on your road layer
- **Disconnected network:** Some areas may be truly unreachable by road (islands, gated communities)
- **One-way streets:** If your data has one-way restrictions, check the direction field parameter

### "Difference" tool produces empty result
- **No overlap:** Your service areas may already cover all disadvantaged areas (good news!)
- **CRS mismatch:** Both layers must be in the same CRS
- **Invalid geometries:** Run Fix Geometries on both layers first

## Support materials

- Slides: [Week 06 lecture deck](../slides/index.md)
- Lecture notes: [Health Equity & Accessibility](../lectures/week06-health-theory.md)
- Plugin guide: [QNEAT3 documentation](https://root676.github.io/)
- Dataset checklist: [Week 6 items](../reference/data-download-checklist.md)

## Reflect

Take 10-15 minutes to answer these questions in your [Week 6 reflection](../reference/reflections.md#week-6--health-accessibility):

- Which areas had the worst accessibility? Were you surprised?
- How would your findings change if you analyzed walking access instead of driving?
- What did the shortest path routes reveal that isochrones didn't show? When is each approach more useful?
- What additional data would strengthen this analysis (transit routes, facility capacity, wait times)?
- Who are the stakeholders for this type of analysis? How might different groups use (or misuse) these findings?
- How confident are you in your results? What are the biggest sources of uncertainty?

## What you'll submit

- [ ] QGIS project: `projects/week06_health_accessibility.qgz`
- [ ] Service areas layer: `data/processed/week06/health_service_areas.gpkg`
- [ ] Gap analysis layer: `data/processed/week06/accessibility_gaps.gpkg`
- [ ] Accessibility map (PDF): `exports/week06_health_accessibility.pdf`
- [ ] Summary statistics (include in your reflection or as a separate file):
  - Number of facilities analyzed
  - Number of SA2s/areas within 15-minute access
  - Number of high-disadvantage areas outside 15-minute access
  - Estimated population in accessibility gaps (if data available)
- [ ] Method documentation: `projects/week06_method_notes.txt`
- [ ] Your Week 6 reflection entry

## Coming up next week

Week 7 is the bridge to Python. You'll run your first Python notebook and see how the QGIS workflows you've mastered can be automated with code. No installation required—you can use Google Colab in your browser!
