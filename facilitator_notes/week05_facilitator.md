# Week 5 Facilitator Notes: Crime Mapping & Ethical Analysis

**Course:** Introduction to GIS
**Week:** 5 of 12
**Topic:** Crime Hotspots & Ethical Analysis
**Prepared for:** Lecturers/Facilitators

---

## Session Overview

### Duration
- **Lecture:** 60-75 minutes (including ethical discussion)
- **Lab/Tutorial:** 90-120 minutes
- **Total contact time:** 2.5-3 hours

### Learning Objectives

By the end of this session, students will be able to:

1. Download, filter, and prepare crime incident data for spatial analysis
2. Apply kernel density estimation (KDE) and hex binning techniques to identify hotspots in QGIS
3. Compare how different administrative boundaries (LGA, police districts, suburbs) shape the narrative
4. Frame crime analysis findings responsibly, considering context, community impact, and data limitations
5. Critically evaluate ethical implications of crime mapping including privacy, bias, and community stigma

### Materials Needed

**Before Class:**
- [ ] Crime dataset downloaded and tested (NSW Recorded Crime, Chicago Crime Data, or local equivalent)
- [ ] Sample KDE outputs prepared at 250m, 500m, and 1000m bandwidths
- [ ] Boundary layers from Week 3 (LGA, SA2) available
- [ ] QGIS project with base layers pre-loaded for demo
- [ ] Example "good" and "bad" crime maps for discussion (see resources below)
- [ ] Ethics discussion prompts printed or ready to display
- [ ] Population data for normalization calculations

**Student Requirements:**
- Completed Week 3 boundary work (SA2, LGA layers)
- QGIS installed and functional
- Crime dataset downloaded (check Week 5 data checklist)
- Ethics reading completed: `/site_docs/readings/week05-ethics-in-mapping.md`

---

## Before Class Checklist

### Data Preparation (1-2 hours before class)

1. **Test crime dataset:**
   - Download the specific dataset students will use
   - Load into QGIS and verify all points display correctly
   - Check attribute table for key fields: date, offense_type, location_quality
   - Note any data quality issues (missing coordinates, invalid dates)
   - Prepare filtered subset if dataset is very large (>100,000 records)

2. **Pre-run KDE analysis:**
   - Create heatmaps at 250m, 500m, and 1000m radius
   - Save as separate `.tif` files for quick comparison during demo
   - Style each with YlOrRd color ramp, 60% opacity
   - Note processing times to set student expectations

3. **Test hex bin workflow:**
   - Create hex grid (500m spacing)
   - Run "Count Points in Polygon"
   - Verify counts look reasonable
   - Style using graduated symbology

4. **Prepare boundary comparison:**
   - Load LGA and SA2 layers
   - Run count aggregation for both
   - Calculate crime rates using population data
   - Export as styled maps for demonstration

5. **Prepare ethical discussion materials:**
   - Curate 2-3 example crime maps from media (screenshots)
   - Identify problematic language, missing context, stigmatizing framing
   - Prepare counter-examples showing responsible approaches

### Technical Setup

- **Test QGIS Processing Toolbox:** Ensure "Heatmap (KDE)" and "Count Points in Polygon" tools appear in search
- **Check projections:** Verify crime data and boundaries are in compatible CRS (preferably projected, not geographic)
- **Prepare backup data:** Have USB or shared drive with datasets in case students have download issues
- **Screen sharing ready:** If teaching remotely, test screen resolution for QGIS visibility

---

## Session Flow

### Part 1: Introduction & Ethical Framing (20 minutes)

**[0:00-0:05] Welcome & Week Overview**

- **Opening statement:** "This week we're working with sensitive data—crime incidents. Before we touch any software, we need to talk about responsibility."
- Review learning objectives
- Acknowledge discomfort: "Some of you may have personal experiences with crime or policing. Today's discussion may bring up strong feelings. That's valid."

**[0:05-0:20] Ethical Discussion: The Power of Crime Maps**

**Facilitation approach:** This is NOT a lecture—facilitate discussion, don't monologue.

**Opening question (pose to class):**
> "Who has seen a crime map in the media or online? Where did you see it, and what was your reaction?"

*Wait for responses. Write key themes on board.*

**Follow-up prompts:**
- "Did the map make you feel more or less safe?"
- "Did it change how you thought about a neighborhood?"
- "What information was missing?"

**Key points to surface (draw from student responses):**

1. **Maps are persuasive:** People trust maps more than text
2. **Data reflects systems, not reality:** Crime data = policing activity, not all crime
3. **Privacy matters:** Even aggregated data can identify communities or individuals
4. **Context is essential:** Raw counts vs rates, temporal trends, data limitations
5. **Unintended consequences:** Your map might be used to justify over-policing or disinvestment

**Show example maps (2-3 minutes each):**

- **Bad example:** "Crime-ridden neighborhoods" headline, no context, stigmatizing language
  - *Ask:* "What's wrong with this map?"
  - *Expected responses:* No rates, loaded language, missing temporal context, no limitations noted

- **Good example:** "Reported property crime incidents per 1,000 residents, 2023" with disclaimer
  - *Ask:* "What makes this better?"
  - *Expected responses:* Neutral language, normalized data, clear time frame, acknowledges limitations

**Transition statement:**
> "Today you'll learn powerful techniques—KDE, hex bins, hotspot analysis. But technique without ethics is dangerous. As you work through the lab, keep asking: 'Who might this map harm? How can I present this responsibly?'"

---

### Part 2: Technical Concepts (15 minutes)

**[0:20-0:30] Kernel Density Estimation (KDE) Explained**

**Facilitation tip:** Use visual analogy before diving into parameters.

**Analogy for KDE:**
> "Imagine each crime incident as a pebble dropped in water. The ripples overlap, and where many ripples meet, the water is most disturbed. That's density. KDE creates a smooth surface showing where incidents cluster."

**Key concepts to emphasize:**

1. **What KDE does:**
   - Takes point data and creates a smooth continuous surface
   - Each point contributes to surrounding area based on distance
   - Output is a raster with density values (incidents per unit area)

2. **Bandwidth (search radius):**
   - Controls how far each point's influence spreads
   - **Small radius (250m):** Very localized, shows street-level detail, can be "noisy"
   - **Medium radius (500m):** Balanced, good for neighborhood patterns
   - **Large radius (1000m+):** Broad trends, very smooth, hides local variation

   **Analogy:** "Bandwidth is like zoom level—close-up vs wide-angle view"

3. **When to use which:**
   - Street-level intervention planning → 250m
   - Community safety assessment → 500m
   - City-wide policy comparison → 1000m

4. **Limitations to acknowledge:**
   - **Edge effects:** Density drops at study area boundaries (fewer neighbors to count)
   - **Sensitivity to parameters:** Different bandwidths tell different stories
   - **Not a prediction:** Shows past patterns, not future risk

**[0:30-0:35] Hex Bins vs KDE**

**Quick comparison (use table on slides):**

| Aspect | KDE Heatmap | Hex Bins |
|--------|-------------|----------|
| Output type | Continuous raster | Discrete polygons |
| Values | Density estimate | Exact counts |
| Best for | Smooth visualization | Reporting specific numbers |
| Communication | General audiences (emotional impact) | Technical reports (precise data) |

**When students should use each:**
- "Use KDE when you want to show WHERE patterns emerge visually"
- "Use hex bins when you need to report HOW MANY incidents per area"
- "Often you'll create both for different audiences"

---

### Part 3: Live Demonstration (25 minutes)

**[0:35-1:00] QGIS Workflow Demonstration**

**Facilitation approach:**
- **Go slow:** Students will follow along during lab time
- **Narrate every click:** "Now I'm clicking Processing > Toolbox..."
- **Pause for questions:** "Before I run this, any questions about the parameters?"

**Demo Script:**

**Step 1: Load and filter crime data (5 minutes)**

1. Open QGIS with base layers visible (LGA boundaries, OSM basemap)
2. `Layer > Add Layer > Add Delimited Text Layer`
3. Navigate to crime CSV file
4. Configure:
   - Geometry: Point coordinates
   - X field: longitude/easting
   - Y field: latitude/northing
   - Geometry CRS: EPSG:4326 (or relevant CRS)
5. Click "Add" and verify points appear

**Narrate:**
> "I can see [X] points loaded. Let me check the attribute table... I see fields for offense_type, date, location_quality. I want to filter to just 2023 property crime."

6. Open attribute table
7. Click "Select features using an expression"
8. Build expression: `"date" >= '2023-01-01' AND "date" < '2024-01-01' AND "offense_type" = 'Property'`
9. Run selection (show count: "X features selected")
10. Right-click layer > Export > Save Selected Features As...
11. Save to GeoPackage: `crime_filtered_2023_property.gpkg`

**Emphasize:**
> "Filtering first makes processing faster and focuses our analysis. We're asking a specific question: Where were property crimes concentrated in 2023?"

**Step 2: Create KDE heatmap (8 minutes)**

12. Open Processing Toolbox: `Processing > Toolbox` (or Ctrl+Alt+T)
13. Search "heatmap" and select **Heatmap (Kernel Density Estimation)**

**Pause and explain parameters BEFORE entering them:**

> "Radius is our bandwidth—how far each point's influence spreads. I'll start with 500 meters for neighborhood-scale patterns."

> "Pixel size controls resolution. Smaller = more detail but larger files. 50m is a good starting point."

14. Configure:
    - Point layer: `crime_filtered_2023_property`
    - Radius: 500 meters
    - Pixel size: 50m
    - Kernel shape: Quartic (default)
    - Output: `crime_kde_500m.tif`
15. Click Run

**While processing:**
> "This may take 30 seconds to 2 minutes depending on point count. For very large datasets—100,000+ points—you might filter to a smaller area or increase pixel size."

16. Once complete, style the output:
    - Right-click layer > Properties > Symbology
    - Render type: Singleband pseudocolor
    - Color ramp: YlOrRd
    - Mode: Continuous
    - Click Classify
    - Navigate to Transparency tab
    - Global opacity: 60%
    - Click Apply, then OK

**Narrate:**
> "Yellow-orange-red is intuitive—red = high density. Transparency lets us see the basemap underneath for geographic context."

**Step 3: Compare bandwidths (5 minutes)**

17. Repeat KDE process with 250m radius (save as `crime_kde_250m.tif`)
18. Repeat with 1000m radius (save as `crime_kde_1000m.tif`)
19. Toggle layers on/off to compare

**Facilitate observation:**
> "Look at the 250m version—very detailed, almost speckled. Now the 1000m—very smooth, broad regions. The 500m strikes a balance. Which is 'right'? Depends on your question and audience."

**Step 4: Create hex bins (7 minutes)**

20. Processing Toolbox > Search "Create grid"
21. Configure:
    - Grid type: Hexagon
    - Grid extent: Calculate from Layer > [select LGA boundary]
    - Horizontal spacing: 500m
    - Vertical spacing: 500m
    - CRS: [match crime data CRS]
    - Output: `hex_grid_500m.gpkg`
22. Run

23. Processing Toolbox > Search "Count points in polygon"
24. Configure:
    - Polygons: `hex_grid_500m`
    - Points: `crime_filtered_2023_property`
    - Count field name: `crime_count`
    - Output: `crime_hex_counts.gpkg`
25. Run

26. Style hex bins:
    - Right-click > Properties > Symbology
    - Change to Graduated
    - Value: `crime_count`
    - Mode: Quantile
    - Classes: 5
    - Color ramp: YlOrRd
    - Classify > Apply

**Show comparison:**
> "The hex bins give us exact counts—this hexagon has 23 incidents. The KDE gives us a smooth density estimate. Both are useful for different purposes."

**Demo wrap-up:**
> "In the lab, you'll recreate this workflow with your own filtered data, experiment with parameters, and aggregate by different boundaries. Remember: every choice you make—bandwidth, bin size, color ramp, title—shapes the story."

---

### Part 4: Ethical Discussion Deep Dive (15 minutes)

**[1:00-1:15] Structured Ethical Discussion**

**Facilitation approach:**
- Use think-pair-share for engagement
- Validate all perspectives
- Redirect victim-blaming or stigmatizing comments gently but firmly

**Discussion 1: Data Provenance (5 minutes)**

**Question for class:**
> "We're using 'crime data.' What are we actually mapping?"

*Allow responses, then clarify:*

**Key teaching point:**
> "This data shows REPORTED and RECORDED incidents. It reflects:
> - Where police patrol (more patrols = more arrests)
> - Who reports crime (some communities have lower trust in police)
> - What gets recorded (not all calls result in reports)
> - System capacity (under-resourced areas may under-record)
>
> It does NOT show all crime that occurred. We're mapping the criminal justice system's activity, not crime itself."

**Follow-up question:**
> "How does this affect our interpretation? What might we miss?"

*Expected responses: Unreported domestic violence, white-collar crime, crimes in low-trust communities*

**Discussion 2: Unintended Consequences (5 minutes)**

**Present scenario:**
> "You've created a beautiful heatmap showing property crime hotspots. A local newspaper wants to publish it with the headline 'City's Most Dangerous Neighborhoods Revealed.' What do you do?"

**Think-pair-share:**
1. Think (1 min): Individual reflection
2. Pair (2 min): Discuss with neighbor
3. Share (2 min): Volunteers share with class

**Facilitate toward these insights:**
- **Stigmatization risk:** Labels neighborhoods, affects property values, discourages investment
- **Self-fulfilling prophecy:** Increased police presence → more arrests → confirms "dangerous" label
- **Missing context:** Are these high-traffic commercial areas? Entertainment districts? What about population density?
- **Alternatives:** Suggest reframing ("Areas with high incident reports"), adding context (rates, temporal trends), including disclaimers

**Teaching point:**
> "You can't control how others use your work, but you CAN:
> 1. Add clear limitations and disclaimers
> 2. Refuse to provide data without context
> 3. Advocate for responsible framing
> 4. Ask: 'Would I want this published if I lived there?'"

**Discussion 3: Privacy & Aggregation (5 minutes)**

**Question:**
> "Why do we aggregate to hex bins or KDE instead of showing individual points?"

*Expected responses: Privacy, anonymization, patterns easier to see*

**Expand with scenario:**
> "Imagine a dataset with 'assault at residential address' and exact coordinates. What could go wrong?"

*Expected responses: Identify victims, target witnesses, stigmatize specific households*

**Key teaching point:**
> "Even aggregated data can be problematic:
> - A hex bin with 1 incident in a low-population area might still identify a victim
> - Temporal filters (e.g., 'assaults on December 25') could narrow to specific events
> - Always check data publisher guidelines and ethics approval requirements"

**Best practices to emphasize:**
- Use broader temporal windows (annual, not daily)
- Aggregate to sufficient area size (min. population threshold)
- Avoid combining multiple rare categories
- Apply coordinate jittering if showing points (randomize location within area)

---

## Part 5: Lab Introduction & Setup (5 minutes)

**[1:15-1:20] Transition to Hands-On Work**

**Briefly outline lab activities:**

1. **Activity 1:** Prepare and filter crime data (15 min)
2. **Activity 2:** Create KDE heatmap, experiment with bandwidths (25 min)
3. **Activity 3:** Create hex bins and count incidents (20 min)
4. **Activity 4:** Boundary comparison—aggregate by LGA, SA2, calculate rates (25 min)
5. **Activity 5 (optional):** Temporal patterns (15 min)
6. **Activity 6:** Add contextual layers and draft responsible interpretation (20 min)

**Set expectations:**
- "This is a multi-step workflow. Don't rush—focus on understanding WHY we make each choice."
- "If you finish early, help a neighbor or explore the optional temporal analysis."
- "Expect to spend 90-120 minutes. Use the troubleshooting section in the lab guide if stuck."

**Remind about ethical framing:**
> "As you work, think about your final deliverable. You'll write a 1-paragraph interpretation that includes patterns AND limitations. Practice neutral language. Avoid words like 'dangerous,' 'crime-ridden,' 'bad neighborhoods.' Focus on patterns and context."

**Check for questions, then release to lab work.**

---

## Key Concepts to Emphasize

### Technical Concepts

**1. Kernel Density Estimation (KDE)**
- **What it is:** Smoothing technique that estimates density of point patterns across space
- **How it works:** Each point contributes to surrounding area; contributions overlap and sum
- **Output:** Continuous raster surface showing relative density
- **Key parameter:** Bandwidth/search radius controls smoothness vs detail

**Teaching tip:** Use the "pebble in water" analogy. Emphasize that KDE doesn't predict future crime—it describes past patterns.

**2. Bandwidth Selection**
- **No single "correct" bandwidth:** Choice depends on research question and scale
- **Trade-off:** Detail vs smoothness, local vs regional patterns
- **Rule of thumb:** Start with 500m for urban neighborhood analysis, adjust based on results
- **Documentation:** Always report bandwidth used (e.g., "500m search radius")

**Common student question:** "Which bandwidth should I use?"
**Answer:** "What scale are you analyzing? Individual streets (250m), neighborhoods (500m), or city-wide trends (1000m+)? Match bandwidth to your question."

**3. Normalization**
- **Counts vs rates:** High counts may just reflect high population
- **Always normalize for spatial comparisons:** Incidents per 1,000 residents, per square km
- **Formula:** `(crime_count / population) * 1000`
- **When NOT to normalize:** If your question is about absolute resource needs (e.g., "Where should we add police patrols?")

**Teaching tip:** Show side-by-side comparison: raw counts vs rates. Same data, different story.

**4. Edge Effects**
- **What they are:** KDE values drop near study area boundaries
- **Why:** Fewer neighboring points to contribute to density estimate
- **Implication:** Don't interpret low density at edges as "safe zones"
- **Mitigation:** Use a buffer zone outside study area when processing, then clip to actual boundary

**Common mistake:** Students assume edges are low-crime areas. Remind them to check raw point data.

### Ethical Concepts

**1. Data Provenance & Bias**
- **Crime data ≠ crime:** It's a record of criminal justice system activity
- **Systemic bias:** Over-policing in certain neighborhoods inflates their "crime" counts
- **Questions to ask:**
  - Who collected this data and for what purpose?
  - What incidents are included/excluded?
  - Does reporting vary by community trust in police?

**Teaching tip:** Ask students, "If two neighborhoods have equal crime but one is policed twice as heavily, what will the data show?" (Answer: The heavily-policed area appears more dangerous.)

**2. Privacy & Aggregation**
- **Principle:** Individual-level data should never be published without consent
- **Aggregation levels:** Points → hex bins → administrative areas
- **Minimum population threshold:** Avoid cells with <5 incidents or <100 residents
- **Coordinate jittering:** Random offset for point data (±100m)

**3. Narrative Framing**
- **Language matters:** "High incident reports" vs "dangerous area"
- **Context is essential:** Include rates, temporal trends, data limitations
- **Disclaimers:** Always note what data doesn't show (unreported crime, system bias)
- **Audience awareness:** Community groups vs police vs media require different framing

**4. Unintended Consequences**
- **Maps have life beyond creator's control:** Consider downstream uses
- **Potential harms:**
  - Stigmatization of communities
  - Justification for over-policing
  - Property value impacts
  - Insurance or lending discrimination
- **Mitigation:** Clear limitations, responsible titles, restricted distribution if necessary

**Teaching approach:** Frame as professional responsibility, not just academic exercise. Students are future practitioners—these skills have real-world impact.

---

## Live Demo Script (Detailed)

**Pre-demo setup (5 minutes before class):**
- Open QGIS with clean project
- Load basemap (OSM or equivalent)
- Load LGA boundary layer (styled with outline, no fill)
- Have crime CSV file path ready to copy-paste
- Open Processing Toolbox in sidebar
- Have this script open on second monitor or printed

---

**Demo Part 1: Loading Crime Data (5 minutes)**

**[Show desktop, open QGIS]**

**Say:** "I'm starting with a clean QGIS project. I've already added a basemap and LGA boundaries for context. Now I'll load the crime dataset."

**Do:**
1. `Layer > Add Layer > Add Delimited Text Layer`
2. Click `...` to browse, navigate to crime CSV
3. **Say:** "This is the NSW Bureau of Crime Statistics and Research dataset—publicly available reported crime incidents for 2023."

4. In the dialog:
   - File format: CSV
   - **Say:** "QGIS auto-detected the delimiter—comma in this case."
   - Geometry definition: Point coordinates
   - X field: `longitude` (or `easting`)
   - Y field: `latitude` (or `northing`)
   - **Say:** "These field names vary by dataset. Look for lat/long or x/y coordinates."
   - Geometry CRS: EPSG:4326 (WGS84)
   - **Say:** "The metadata says this uses WGS84 geographic coordinates. We'll reproject to a local CRS in a moment for accurate distance calculations."

5. Click `Add`
6. **Say:** "It's loading... [wait for points to appear] ...there we go. I can see points across Sydney. Let me check the attribute table to understand what's here."

7. Right-click layer > Open Attribute Table
8. **Say while scrolling:** "I can see fields for offense_type, date, LGA_name, location_quality. There are [check row count] 45,782 incidents. That's too many for efficient processing, so I'll filter to just property crime in 2023."

---

**Demo Part 2: Filtering Data (5 minutes)**

**Do:**
9. In attribute table, click `Select features using an expression` (yellow icon with ε)
10. **Say:** "I'll build a filter expression. Think of this like Excel's filtering but more powerful."

11. In Expression dialog, type (narrating as you type):
   ```
   "date" >= '2023-01-01' AND "date" < '2024-01-01' AND "offense_type" = 'Theft'
   ```
   **Say:** "I'm filtering to theft offenses in 2023. Notice the date format—YYYY-MM-DD in quotes."

12. Click `Select Features`
13. **Say:** "[Check status bar] 8,234 features selected. Much more manageable."

14. Close attribute table
15. **Say:** "Now I'll export just the selected features."

16. Right-click crime layer > Export > Save Selected Features As...
17. Configure:
    - Format: GeoPackage
    - File name: `crime_filtered_2023_theft.gpkg`
    - CRS: EPSG:7856 (GDA2020 / MGA Zone 56)
    - **Say:** "I'm reprojecting to a local projected CRS—MGA Zone 56 for Sydney. This uses meters, which is essential for KDE bandwidth calculations."

18. Click OK
19. **Say:** "A new layer appears—just my filtered, reprojected data. I can remove the original layer now."

20. Right-click original layer > Remove Layer

---

**Demo Part 3: Creating KDE Heatmap (8 minutes)**

**Do:**
21. Open Processing Toolbox (Ctrl+Alt+T or `Processing > Toolbox`)
22. **Say:** "The Processing Toolbox contains hundreds of algorithms. I'll search for the KDE tool."

23. Type "heatmap" in search box
24. Double-click **Heatmap (Kernel Density Estimation)**

25. **Say (BEFORE filling parameters):** "Let me explain each parameter before we run this."

26. **Point to each field and explain:**
   - **Point layer:** "Our filtered crime data"
   - **Radius:** "This is bandwidth—how far each point's influence spreads. I'll use 500 meters for neighborhood-scale patterns."
   - **Pixel size:** "Resolution of output raster. 50m means each pixel is 50×50 meters. Smaller = more detail but larger file."
   - **Kernel shape:** "Quartic is the default and works well. Other options (Gaussian, Triangular) produce slightly different smoothing."
   - **Output value scaling:** "None—we want raw density values."

27. **Now fill in parameters:**
   - Point layer: `crime_filtered_2023_theft`
   - Radius: 500 meters
   - Pixel size X: 50 meters
   - Pixel size Y: 50 meters
   - Kernel shape: Quartic
   - Output: Click `...` > Save to File > `crime_kde_500m.tif`

28. Click `Run`
29. **Say while processing:** "This may take 30 seconds to a minute. For large datasets—50,000+ points—expect 2-3 minutes. If it's too slow, increase pixel size to 100m or filter to a smaller area."

30. **When complete:** "Done! A gray raster appeared. It's not styled yet—let me fix that."

---

**Demo Part 4: Styling the Heatmap (5 minutes)**

**Do:**
31. Right-click `crime_kde_500m` layer > Properties
32. Navigate to Symbology tab
33. **Say:** "By default, rasters display as grayscale. We'll use a color ramp that's intuitive for density—yellow to red."

34. Change Render type to: **Singleband pseudocolor**
35. Color ramp: Click dropdown > Select `YlOrRd` (or Reds)
36. **Say:** "Mode determines how values are classified. I'll use Continuous for a smooth gradient."
37. Mode: Continuous
38. Click `Classify`
39. **Say:** "QGIS calculated the min and max density values and assigned colors. Let me add transparency so we can see the basemap underneath."

40. Navigate to Transparency tab
41. Global opacity: 60%
42. **Say:** "60% transparency strikes a balance—you can see the pattern but also geographic context."

43. Click `Apply` then `OK`

44. **Say:** "Now we have a smooth heatmap. Red areas show highest theft density. Notice the clusters in the CBD and around commercial areas—that makes sense for property crime."

---

**Demo Part 5: Comparing Bandwidths (5 minutes)**

**Do:**
45. **Say:** "Let me show you how bandwidth affects the result. I'll create two more heatmaps—one with 250m radius, one with 1000m."

46. Reopen Processing Toolbox > Heatmap tool (click the circular arrow to reopen last-used tool)
47. Change Radius to: 250 meters
48. Change Output to: `crime_kde_250m.tif`
49. Click `Run`

50. **While processing, say:** "The 250m version will show more localized hotspots—almost street-level detail. It might look speckled or noisy."

51. When complete, style the same way (YlOrRd, 60% transparency)

52. Repeat for 1000m radius:
    - Radius: 1000 meters
    - Output: `crime_kde_1000m.tif`
    - Run and style

53. **Compare all three:**
    - **Say:** "Let me toggle these on and off so you can see the difference."
    - Turn on only `crime_kde_250m`
    - **Say:** "Very detailed—you can see individual street clusters. Good for micro-scale interventions like adding lighting."
    - Turn on only `crime_kde_500m`
    - **Say:** "More balanced—neighborhood-level patterns. This is my go-to starting point."
    - Turn on only `crime_kde_1000m`
    - **Say:** "Very smooth—broad regional trends. Good for city-wide comparisons, less useful for local planning."

54. **Teaching point:** "There's no single 'correct' bandwidth. It depends on your question: Are you analyzing streets, neighborhoods, or regions? Match your bandwidth to your scale."

---

**Demo Part 6: Hex Bins (7 minutes)**

**Do:**
55. **Say:** "KDE gives us a smooth visual, but sometimes we need exact counts—that's where hex bins come in."

56. Processing Toolbox > Search "create grid" > Double-click **Create grid**

57. Configure:
   - Grid type: Hexagon
   - **Say:** "Hexagons are better than squares for spatial analysis—they have uniform distance to all neighbors."
   - Grid extent: Click `...` > Calculate from Layer > Select LGA boundary
   - **Say:** "This sets the grid to cover our study area."
   - Horizontal spacing: 500 meters
   - Vertical spacing: 500 meters
   - Grid CRS: EPSG:7856 (same as crime data)
   - Output: `hex_grid_500m.gpkg`

58. Click `Run`
59. **Say:** "Now we have a honeycomb grid. Next, we'll count how many incidents fall in each hexagon."

60. Processing Toolbox > Search "count points" > Double-click **Count points in polygon**

61. Configure:
    - Polygons: `hex_grid_500m`
    - Points: `crime_filtered_2023_theft`
    - Count field name: `crime_count`
    - **Say:** "This creates a new field called crime_count with the number of points in each hex."
    - Output: `crime_hex_counts.gpkg`

62. Click `Run`

63. **Say:** "Done. Now to visualize the counts with graduated symbology."

64. Right-click `crime_hex_counts` > Properties > Symbology
65. Change from Single Symbol to: **Graduated**
66. Value: `crime_count`
67. Color ramp: YlOrRd
68. Mode: Quantile (Equal Count)
69. Classes: 5
70. Click `Classify`
71. **Say:** "Quantile divides the data into 5 equal groups—each color represents 20% of hexagons. This highlights relative differences."

72. Click `Apply` then `OK`

73. **Compare KDE and hex bins:**
    - Turn on KDE layer and hex bin layer together
    - **Say:** "Notice how they show similar patterns but with different styles. KDE is smooth and visual—great for presentations. Hex bins give exact counts—better for reporting specific numbers or statistical analysis."

---

**Demo Wrap-Up (2 minutes)**

**Say:** "In the lab, you'll recreate this entire workflow with your own data. You'll also:
- Aggregate by different boundaries (LGA, SA2) to see how the story changes
- Calculate crime rates (normalizing by population)
- Add contextual layers like SEIFA or transit stops to explain patterns
- Write a responsible interpretation that acknowledges limitations

Remember: Every technical choice—bandwidth, bin size, color ramp—shapes the narrative. And every narrative has ethical implications. Think critically about how your maps might be used or misused."

---

## Discussion Prompts

Use these to facilitate ethical discussions during lecture or at transition points in lab.

### Opening Discussion: Personal Experience with Crime Maps

**Prompt:**
> "Before we start, let's talk about crime maps you've encountered. Where have you seen them? News articles? Real estate websites? Police reports? What was your reaction?"

**Facilitation tips:**
- Write responses on board/whiteboard
- Group into themes: media, policy, personal safety
- Validate all responses—no "wrong" answers at this stage
- Listen for stigmatizing language students may have absorbed; gently reframe

**Transition:** "Maps are powerful because they're persuasive. Today we'll learn to create them responsibly."

---

### Mid-Lecture Discussion: What Are We Actually Mapping?

**Prompt:**
> "We call this 'crime data,' but what does it actually measure? If I show you a map of 'high crime areas,' what am I really showing you?"

**Expected responses:**
- Reported crime (not all crime)
- Police activity (patrols, arrests)
- System capacity (under-resourced areas under-report)
- Community trust (low trust = low reporting)

**Follow-up question:**
> "How might policing patterns affect what we see on the map?"

**Key teaching point to surface:**
- **Over-policing creates self-fulfilling prophecies:** More patrols → more arrests → labeled "high crime" → more patrols
- **Under-policing hides problems:** Low reports ≠ low crime

**Facilitation tip:** If students blame communities ("they commit more crime there"), redirect to systemic factors: "Let's think about what creates that pattern—historical disinvestment, lack of services, biased enforcement?"

---

### Post-Demo Discussion: Bandwidth and Narrative

**Prompt (after showing 250m, 500m, 1000m KDE outputs):**
> "I just showed you three heatmaps of the exact same data. Which one is 'true'? Which should we publish?"

**Expected responses:**
- "All are true—just different scales"
- "Depends on the audience"
- "Depends on the question"

**Follow-up:**
> "Imagine you're a journalist choosing a map for your article. You want to make people care about crime. Which bandwidth do you choose? Why?"

**Key teaching point:**
- **250m looks scarier:** More red blobs, fragmented, emphasizes danger
- **1000m looks calmer:** Smooth gradients, diffuse, downplays concern
- **500m is balanced but still a choice**

**Ethical implication:** "Even 'objective' technical decisions shape emotional response. This is why we document parameters and acknowledge that different choices tell different stories."

---

### Lab Transition Discussion: Privacy and Aggregation

**Prompt:**
> "We're aggregating points to hex bins and KDE surfaces. Why not just show individual crime locations?"

**Expected responses:**
- Privacy concerns
- Identify victims
- Patterns easier to see

**Scenario follow-up:**
> "Your dataset has a field called 'assault at residential address' with exact coordinates. What could go wrong if you mapped those points publicly?"

**Facilitation tips:**
- Emphasize: Even de-identified data can re-identify individuals through spatial proximity
- Discuss: What if there's only one house at that location? What if combining time + place narrows to a specific event?
- Introduce concept of **k-anonymity:** Minimum threshold of incidents before displaying (e.g., don't show cells with <5 incidents)

**Transition:** "This is why aggregation isn't just about visualization—it's about protecting people."

---

### End-of-Lab Discussion: Responsible Framing

**Prompt (after students complete analysis):**
> "You've created a hotspot map. A local newspaper wants to publish it with the headline: 'City's Most Dangerous Neighborhoods Revealed.' How do you respond?"

**Think-pair-share format:**
1. **Think (1 min):** Individual reflection
2. **Pair (2 min):** Discuss with neighbor—what would you say to the journalist?
3. **Share (5 min):** Volunteers present to class

**Expected responses:**
- Request headline change
- Demand context be added
- Refuse permission
- Provide alternative framing

**Facilitate toward best practices:**
- **Alternative headline:** "Reported Theft Incidents Per 1,000 Residents, 2023"
- **Required context:**
  - These are reported incidents (doesn't include unreported crime)
  - High counts may reflect high foot traffic (commercial areas)
  - Temporal trends (compared to last year)
  - Data limitations (system bias, incomplete reporting)

**Key question:**
> "Would you want this map published if you lived in a 'red zone'? If not, what would make it acceptable?"

**Teaching point:** "Your professional reputation depends on how your work is used. Advocate for responsible framing, or withhold permission."

---

### Closing Reflection: Unintended Consequences

**Prompt:**
> "Imagine your hotspot map leads to increased police patrols in the identified areas. Six months later, you run the analysis again. What might you see? Why?"

**Expected response:**
- Even more incidents in those areas (more patrols = more arrests)
- Confirms the "hotspot" label
- Self-fulfilling prophecy

**Follow-up:**
> "How do you prevent your work from contributing to over-policing?"

**Strategies to surface:**
- Frame as "areas needing resources" (lighting, services) not "dangerous areas"
- Recommend community-based interventions, not just enforcement
- Acknowledge data bias in limitations section
- Advocate for root-cause analysis (poverty, lack of services) alongside crime analysis

**Closing statement:**
> "GIS gives you power to shape narratives. Use it responsibly. The communities you map are real places with real people who deserve dignity, not stigma."

---

### Historical Context: Mapping and Redlining

**If time permits (10 minutes), add this discussion to deepen students' understanding of how crime mapping fits into a longer history.**

**Setup:**
> "Crime mapping has a history we should acknowledge. Let me share something that might reframe how you think about what we're doing today."

**Brief historical context:**
> "In the 1930s-1960s, US cities used 'security maps' to rate neighborhoods by risk for mortgage lending. These maps were color-coded—green for 'best,' red for 'hazardous.' The maps were presented as objective assessments of property values and loan risk.
>
> In practice, they systematically marked Black and immigrant neighborhoods as red zones, regardless of actual economic conditions. This justified denying mortgages, insurance, and investment to those communities for decades. The term 'redlining' comes from these maps.
>
> The results? Decades of disinvestment that created the very conditions the maps claimed to measure. Infrastructure deteriorated. Property values fell. Poverty concentrated. Crime rose. A self-fulfilling prophecy, drawn on a map."

**Connection to today's work:**
> "Now look at your hotspot map. What neighborhoods appear in red? What's the demographic history of those areas? Are we potentially repeating a pattern where maps justify policies that reinforce existing inequalities?"

**This isn't about guilt—it's about awareness:**
> "I'm not saying your analysis is racist or that you shouldn't create crime maps. I'm saying: know the history. The communities we map often have good reasons to distrust 'objective' spatial analysis. Our job is to be worthy of trust—by acknowledging limitations, adding context, and centering systemic causes rather than neighborhood labels."

**Key takeaway:**
> "Our maps inherit this history whether we acknowledge it or not. Adding context, acknowledging limitations, and centering systemic causes are concrete practices that break the pattern."

**Optional resources to share:**
- "Mapping Inequality" project (redlining maps digitized): [https://dsl.richmond.edu/panorama/redlining/](https://dsl.richmond.edu/panorama/redlining/)
- NPR's "A 'Forgotten History' Of How The U.S. Government Segregated America"

---

## Ethical Discussion Guide

This section provides structured facilitation for the 15-minute ethical discussion mid-lecture.

### Setup (Before Class)

**Materials needed:**
- Example "bad" crime map (stigmatizing headline, no context, raw counts)
- Example "good" crime map (neutral framing, rates, limitations noted)
- Projector/screen for displaying examples
- Whiteboard/flipchart for capturing student responses

**Room arrangement:**
- If possible, arrange seats in semi-circle for discussion (not lecture rows)
- Ensure all students can see examples

---

### Facilitation Structure

**Phase 1: Establishing Norms (2 minutes)**

**Say:**
> "We're about to discuss sensitive topics—crime, policing, community impacts. Here are our discussion norms:
> 1. **Assume good intent:** We're all learning.
> 2. **Speak from 'I' perspective:** Share your own experiences and reactions, not generalizations.
> 3. **Listen actively:** Don't interrupt; build on others' ideas.
> 4. **Challenge ideas, not people:** Critique the map, not the mapmaker.
> 5. **It's okay to be uncomfortable:** Growth happens at the edge of our comfort zone.
>
> Does anyone need to add a norm?"

**Facilitation tip:** Write norms on board. Reference them if discussion gets heated.

---

**Phase 2: Example Analysis (5 minutes)**

**Show "bad" example crime map** (e.g., news article with "Crime-Ridden Neighborhoods" headline, no rates, stigmatizing language)

**Ask:** "What do you notice about this map? What's problematic?"

**Capture responses on board. Listen for:**
- Loaded language ("crime-ridden," "dangerous," "sketchy")
- Missing context (no rates, no temporal comparison, no data source)
- Lack of limitations (no disclaimer about reporting bias)
- Color choices that amplify fear (red = danger)

**Probing questions if discussion stalls:**
- "How might residents of a 'red zone' feel seeing this?"
- "What information is missing?"
- "Who benefits from this framing? Who is harmed?"

**Show "good" example crime map** (e.g., "Reported Property Crime Incidents Per 1,000 Residents, 2023" with disclaimer)

**Ask:** "How is this different? What makes it more responsible?"

**Expected responses:**
- Neutral language
- Normalized data (rates, not counts)
- Clear temporal scope
- Disclaimer about data limitations

**Transition:** "Now let's dig deeper into specific ethical issues."

---

**Phase 3: Structured Scenario Discussion (6 minutes)**

**Scenario 1: Data Bias (2 minutes)**

**Present:**
> "Two neighborhoods: Neighborhood A has heavy police presence (foot patrols, traffic stops). Neighborhood B has minimal patrols. Your crime data shows 3× more incidents in A. What's going on?"

**Expected response:** More policing = more recorded crime (not necessarily more actual crime)

**Follow-up:** "How do you communicate this in your map?"

**Key teaching point:**
> "Include disclaimer: 'This data reflects reported and recorded incidents, which are influenced by policing patterns and community reporting practices. It does not represent all crime that occurred.'"

---

**Scenario 2: Unintended Use (2 minutes)**

**Present:**
> "You create a hotspot map for a university assignment. A real estate company finds it online and uses it to label neighborhoods as 'high crime' on their listings. Property values drop. Residents are upset. Are you responsible?"

**Facilitate discussion:**
- **Legally:** Probably not (public data, fair use)
- **Ethically:** Partially (didn't anticipate downstream use)

**Ask:** "How could you have prevented this?"

**Strategies to surface:**
- Add license/usage terms
- Include prominent disclaimer
- Password-protect sensitive outputs
- Don't publish online—submit only to instructor
- Advocate with the company to remove/contextualize

**Key teaching point:** "Once your map is public, you lose control. Think carefully about distribution."

---

**Scenario 3: Privacy Edge Case (2 minutes)**

**Present:**
> "You're mapping domestic violence incidents. You aggregate to SA2 regions to protect privacy. But one SA2 has only 3 households and 1 reported incident. Have you protected privacy?"

**Expected response:** No—neighbors could identify the household

**Ask:** "What's your solution?"

**Strategies:**
- Set minimum threshold (don't display cells with <5 incidents or <100 residents)
- Aggregate to larger areas in low-population zones
- Apply coordinate jittering (random offset)
- Consult ethics board or data custodian

**Key teaching point:** "Aggregation alone isn't enough. Consider context—population density, incident rarity, sensitivity."

---

**Phase 4: Closing Reflection (2 minutes)**

**Ask:**
> "What's one ethical principle you'll take into your lab work today?"

**Go around room quickly (popcorn style, not forced).**

**Close with:**
> "Ethics isn't a checkbox—it's ongoing critical reflection. As you work through the lab, keep asking:
> - Who might this map harm?
> - What context am I missing?
> - How can I present this responsibly?
>
> If you're unsure, ask me. I'd rather you pause and think than rush ahead."

---

### Facilitation Tips for Sensitive Discussions

**1. Handling Victim-Blaming or Stigmatizing Comments**

**If a student says:** "Well, those neighborhoods ARE dangerous—the data proves it."

**Redirect gently:**
> "I hear that the data shows high incident counts. Let's unpack that—what does 'dangerous' mean? Are we measuring actual risk, or police activity? How might other factors like poverty or lack of services contribute? Let's focus on patterns, not labeling places or people."

**2. Validating Personal Experiences**

**If a student shares:** "I grew up in a neighborhood labeled 'high crime.' It felt stigmatizing."

**Validate and invite others:**
> "Thank you for sharing that. It's important we hear from people who've been on the receiving end of these maps. Does your experience change how you think about crime mapping? What would responsible mapping look like from your perspective?"

**3. Managing Dominant Voices**

**If one student monopolizes discussion:**
> "Thanks, [Name]. I want to make sure we hear from others too. Who hasn't spoken yet? What's your take?"

**4. Handling Silence**

**If no one responds to a question:**
- Wait 10 seconds (feels long; count in your head)
- Rephrase: "Let me ask differently..."
- Use think-pair-share: "Take 30 seconds to jot down a thought, then share with a neighbor."
- Volunteer an answer: "Here's what I think... do you agree or disagree?"

**5. Dealing with Disagreement**

**If students disagree on ethical stance:**
> "This is exactly the kind of tension practitioners face. There's not always one right answer. Let's explore both perspectives—what are the trade-offs of each approach?"

**6. Time Management**

**If discussion runs long:**
> "This is a rich conversation—I wish we had more time. Let's continue this in the lab or during office hours. Here's the key takeaway for now: [summarize main point]."

**If discussion stalls early:**
> "Great—we've covered the key issues quickly. Let me add one more scenario to consider... [introduce additional example]."

---

### Sample Script for Ethical Discussion

**[0:00] Opening**

"Alright, we're going to shift gears for the next 15 minutes to talk about the ethics of crime mapping. [Display discussion norms on screen.] Here are our norms for this conversation. [Read aloud.] Anything to add? [Wait.] Great.

I'm going to show you two crime maps. As I do, I want you to think about: What story does this map tell? Who does it help? Who does it harm?"

---

**[0:02] Bad Example Analysis**

[Display bad example: "City's Most Dangerous Neighborhoods" with raw counts, no context]

"What do you notice? What's problematic about this map?"

[Wait for responses. Capture on board: loaded language, missing context, no disclaimer, stigmatizing]

"Exactly. Now imagine you live in one of those red zones. How does this map affect you?"

[Responses: property values drop, harder to get insurance, stigma, over-policing]

"Right. This map, intended to 'inform the public,' actually harms communities. Let's look at a better approach."

---

**[0:05] Good Example Analysis**

[Display good example: "Reported Property Crime Per 1,000 Residents, 2023" with disclaimer]

"How is this different?"

[Responses: neutral language, rates not counts, time period clear, disclaimer present]

"Yes—same data, more responsible framing. It acknowledges limitations and avoids stigmatizing language. This is the standard we'll hold ourselves to."

---

**[0:07] Scenario 1: Data Bias**

"Quick scenario: Two neighborhoods. A has heavy police patrols. B has minimal patrols. Your data shows A has 3× more crime. What's really going on?"

[Response: More policing = more recorded crime]

"Exactly. We're not mapping crime—we're mapping police activity. How do you communicate that?"

[Response: Add disclaimer]

"Right. Include language like: 'This data reflects reported incidents, which are influenced by policing patterns.' Always name the bias."

---

**[0:09] Scenario 2: Unintended Use**

"Next scenario: You make a hotspot map for this class. A real estate company finds it online and uses it to label neighborhoods. Property values drop. Residents are angry. Are you responsible?"

[Responses vary: yes/no/partially]

"Ethically, I'd say partially. You didn't intend harm, but you also didn't anticipate how it could be misused. What could you have done differently?"

[Responses: disclaimer, password-protect, don't publish publicly]

"Exactly. Think about distribution carefully. Once it's online, you lose control."

---

**[0:11] Scenario 3: Privacy**

"Last one: You're mapping domestic violence, aggregated to SA2 regions. But one SA2 has only 3 households and 1 incident. Privacy protected?"

[Response: No—neighbors could identify the household]

"Right. Aggregation alone isn't enough in low-population areas. What's your fix?"

[Responses: minimum threshold, larger areas, jittering]

"Yes. Set thresholds—don't display cells with <5 incidents or <100 residents. Always consider context."

---

**[0:13] Closing**

"Alright, let's bring this home. What's one ethical principle you'll carry into the lab today?"

[Popcorn responses: add context, check privacy, neutral language, acknowledge bias]

"Perfect. Remember: ethics isn't a checkbox. It's constant critical thinking. As you work through the lab, ask yourself: Who might this harm? What am I missing? How can I do this responsibly?

And if you're unsure—ask me. I'd rather you pause and think than rush ahead. Okay, let's move into the technical demo."

---

## Common Student Issues & Solutions

### Technical Issues

**Issue 1: KDE produces blank or all-zero raster**

**Symptoms:**
- Output raster loads but displays as uniform gray or all zeros
- No visible pattern when styled

**Common causes:**
1. **CRS mismatch—data in geographic (degrees) but radius in meters**
   - **Solution:** Reproject point data to projected CRS before running KDE
   - **How to identify:** Check layer CRS in Properties > Information
   - **Fix:** `Vector > Data Management Tools > Reproject Layer` to local projected CRS (e.g., EPSG:7856 for Sydney)

2. **Radius units mismatch**
   - **Solution:** Ensure radius matches CRS units (meters for projected, degrees for geographic—but always use projected for KDE!)
   - **Check:** If your data is in EPSG:4326 (WGS84), reproject first

3. **Very few points (<50)**
   - **Solution:** Use smaller radius (100m) or filter less aggressively
   - **Explanation:** KDE needs sufficient points to estimate density

**Student dialogue:**
> **Student:** "My heatmap is just gray—nothing shows up."
> **You:** "Let me check your CRS. [Open layer properties > Information] I see your points are in EPSG:4326—that's geographic coordinates in degrees. But you set radius to 500 meters. QGIS can't mix degrees and meters. Let's reproject your data to EPSG:7856, then re-run the KDE."

---

**Issue 2: Heatmap appears blocky or pixelated**

**Symptoms:**
- Output looks like Minecraft blocks instead of smooth gradient
- Hard edges between pixels visible

**Causes:**
1. **Pixel size too large**
   - **Solution:** Reduce pixel size from 50m to 25m or 10m
   - **Trade-off:** Larger file size, longer processing time

2. **Radius too small relative to pixel size**
   - **Solution:** If using 10m pixels, ensure radius is at least 100m
   - **Rule of thumb:** Radius should be ≥10× pixel size for smooth output

**Student dialogue:**
> **Student:** "My heatmap looks blocky."
> **You:** "What pixel size did you use? [Student says 100m] That's quite large—each pixel is 100×100 meters. Try reducing to 25m for smoother output. It'll take longer to process but will look much better."

---

**Issue 3: Edge effects—low density at study area boundaries**

**Symptoms:**
- Density drops dramatically at edges of study area
- Students interpret edges as "safe zones"

**Cause:**
- KDE has fewer neighboring points to count near boundaries (mathematical artifact)

**Solution:**
1. **Explain it's expected:** "This is called edge effect—KDE has fewer points to count at boundaries. Don't interpret low values at edges as low crime."
2. **Advanced fix:** Buffer study area by radius distance, run KDE on buffered area, then clip to original boundary
   - **Demo if time permits:** `Vector > Geoprocessing Tools > Buffer` → 500m buffer → Run KDE → Clip output

**Student dialogue:**
> **Student:** "Why is there low crime all around the edge of the city?"
> **You:** "That's edge effect—an artifact of how KDE works, not real crime patterns. The algorithm has fewer points to count near boundaries. If you want accurate edge values, you'd need to include neighboring areas in your analysis. For this exercise, just note it as a limitation."

---

**Issue 4: Count Points in Polygon returns all zeros**

**Symptoms:**
- Hex bins or polygons show `crime_count = 0` for all features

**Causes:**
1. **CRS mismatch between points and polygons**
   - **Solution:** Ensure both layers use same CRS
   - **Check:** Layer Properties > Information > CRS
   - **Fix:** Reproject one layer to match the other

2. **Points fall outside polygon extent**
   - **Solution:** Visually check overlap—toggle layers on/off
   - **Fix:** Recreate grid using "Calculate from Layer" for extent

3. **Invalid geometries in polygon layer**
   - **Solution:** Run `Vector > Geometry Tools > Fix Geometries` on polygon layer

**Student dialogue:**
> **Student:** "All my hex bins say zero but I can see points on the map."
> **You:** "Let's check CRS. [Open properties for both layers] Your hexagons are in EPSG:7856 but points are still in EPSG:4326. QGIS can display them together but can't count correctly. Reproject your points to EPSG:7856 and re-run Count Points in Polygon."

---

**Issue 5: Hex grid doesn't align with study area**

**Symptoms:**
- Grid extends far beyond boundary
- Grid doesn't cover entire study area
- Grid is rotated or misaligned

**Causes:**
1. **CRS mismatch**
   - **Solution:** Grid CRS must match boundary layer CRS

2. **Manually drawn extent instead of calculated**
   - **Solution:** Use `Calculate from Layer` option for Grid Extent parameter

3. **Spacing too large**
   - **Solution:** For small study areas (e.g., single suburb), use 100m or 250m spacing instead of 500m

**Student dialogue:**
> **Student:** "My hex grid is way too big—it covers the whole state."
> **You:** "Did you use 'Calculate from Layer' for the extent? [Student says no] Let's redo it. In the Grid Extent parameter, click the three dots, then 'Calculate from Layer,' and select your LGA boundary. That'll constrain the grid to just your study area."

---

### Conceptual Issues

**Issue 6: Confusing density values with counts**

**Symptom:**
- Student says "this area has 487 crimes" based on KDE pixel value

**Clarification:**
> "KDE values are density estimates—incidents per square kilometer—not actual counts. If you need exact counts, use hex bins instead. The KDE value 487 means approximately 487 incidents per km² in that area, based on the smoothing algorithm."

**Teaching moment:**
- Show attribute table of KDE raster—students can see decimal values like 15.37 (obviously not a count of incidents)
- Compare to hex bins which show integers (1, 5, 23)

---

**Issue 7: Not understanding bandwidth/radius choice**

**Symptom:**
- Student asks "Which bandwidth is correct?"
- Student uses 1000m for street-level analysis or 100m for city-wide comparison

**Teaching response:**
> "There's no single 'correct' bandwidth—it depends on your question and scale. Are you analyzing:
> - Individual street blocks? → 100-250m
> - Neighborhoods? → 500m
> - City-wide regions? → 1000m+
>
> What question are you trying to answer? [Student responds.] Okay, for neighborhood-level safety assessment, 500m makes sense. For identifying specific intersections for lighting upgrades, try 250m."

**Rule of thumb to share:**
- Start with 500m for urban analysis
- Adjust based on whether output looks too detailed (reduce bandwidth) or too smooth (increase bandwidth)
- Always report the bandwidth you used

---

**Issue 8: Not normalizing—comparing raw counts across different-sized areas**

**Symptom:**
- Student concludes "LGA A has more crime than LGA B" based on raw counts
- Doesn't account for population differences

**Teaching response:**
> "LGA A has 500 incidents and LGA B has 200—but LGA A has 200,000 residents and LGA B has 50,000. Which has a higher crime rate? [Wait for student to calculate.] Right—LGA B has 4 per 1,000 residents vs LGA A's 2.5 per 1,000. Always normalize by population or area when comparing regions."

**Formula to provide:**
```
Crime rate = (crime_count / population) × 1000
```

**QGIS Field Calculator:**
```
"crime_count" / "population" * 1000
```

---

**Issue 9: Interpreting patterns without context**

**Symptom:**
- Student says "this neighborhood is dangerous because it's red on the map"
- Doesn't consider contributing factors

**Teaching response:**
> "You've identified a hotspot—good. Now let's ask why. Turn on the SEIFA layer. [Toggle layer.] I see this hotspot overlaps with areas of high disadvantage. Turn on land use. [Toggle.] It's also a commercial district with high foot traffic. So is this a 'dangerous neighborhood' or a place with more activity, fewer resources, and more policing? How does that change your interpretation?"

**Encourage questions:**
- What type of crime is this? (Property crime in commercial areas vs violent crime in residential)
- What time period? (Has it changed over time?)
- What's the context? (Transit hubs, nightlife districts, poverty, lack of services)

---

**Issue 10: Ethical discomfort or resistance**

**Symptom:**
- Student says "This ethics stuff is too political—I just want to learn GIS"
- Student dismisses bias concerns as "overthinking"

**Teaching response (validating but firm):**
> "I hear that you want to focus on technique. But GIS is never just technical—it has real-world impacts. The maps you create will influence decisions about policing, funding, insurance, real estate. Ignoring ethics doesn't make you neutral—it makes you complicit if your work harms communities. Part of being a GIS professional is thinking critically about consequences. That's not political—it's professional responsibility."

**Alternative approach (if student seems defensive):**
> "Think of ethics like quality control. You wouldn't submit a map with wrong projections or unlabeled axes, right? Ethical analysis is the same—checking that your work is accurate, contextual, and won't mislead. It's part of doing good GIS."

---

### Performance Issues

**Issue 11: KDE processing takes >5 minutes or crashes**

**Causes:**
- Very large dataset (>100,000 points)
- Very small pixel size (5m or 10m)
- Insufficient RAM

**Solutions:**

1. **Filter data first:**
   - Select subset (e.g., one year, one crime type, one region)
   - Export selection and work with smaller dataset

2. **Increase pixel size:**
   - Use 100m instead of 50m (processes 4× faster)
   - Reduce to 50m or 25m for final output if needed

3. **Clip to study area:**
   - Don't process entire state if you only need one city
   - Use `Clip` tool to extract points within your boundary first

4. **Close other programs:**
   - Free up RAM—close browser tabs, other applications

**Student dialogue:**
> **Student:** "QGIS has been processing for 10 minutes and nothing's happening."
> **You:** "How many points are you processing? [Student checks: 250,000] That's a lot. Let's filter to just 2023 first. [Filter and export.] Now how many? [25,000] Much better. Re-run the KDE—should take 1-2 minutes max."

---

**Issue 12: File sizes too large (>500MB rasters)**

**Cause:**
- Small pixel size (5m) with large extent

**Solutions:**
1. Increase pixel size to 50m or 100m
2. Clip raster to smaller extent after processing
3. Reduce bit depth (use 32-bit float instead of 64-bit if option available)

**When to worry:**
- >1GB files can cause display lag
- Prioritize usability over marginal quality gains

---

## Wrap-up & Preview

### Final 5 Minutes of Lab Session

**Gather attention:**
> "Alright everyone, let's wrap up for today. Save your work—you'll submit the final project next week but I want to leave you with a few thoughts."

---

### Key Takeaways (2 minutes)

**Ask students:**
> "What's one technical thing you learned today?"

[Responses: KDE, bandwidth selection, hex bins, normalization]

> "And what's one ethical consideration you'll take forward?"

[Responses: context matters, avoid stigmatizing language, acknowledge limitations]

**Reinforce:**
> "You now have powerful tools—KDE, hex bins, boundary aggregation. But technique without ethics is dangerous. Every choice you made today—bandwidth, bin size, color ramp, boundary system—shaped the narrative. Always ask: Who does this map help? Who might it harm? How can I present this responsibly?"

---

### Common Pitfalls to Avoid (1 minute)

**Quickly review:**
1. **Don't compare raw counts across different-sized areas** → Always normalize by population or area
2. **Don't ignore edge effects** → Note as limitation; don't interpret edges as "safe zones"
3. **Don't use stigmatizing language** → "Reported incidents" not "dangerous areas"
4. **Don't skip context** → Include rates, time periods, data limitations
5. **Don't forget your CRS** → Reproject to projected CRS before KDE

---

### Submission Reminders (1 minute)

**Due [specify date]:**
- [ ] QGIS project file: `week05_crime_hotspots.qgz`
- [ ] KDE heatmap raster: `crime_kde.tif`
- [ ] Hex bin counts layer: `crime_hex_counts.gpkg`
- [ ] Comparison layout: Three maps (LGA, SA2, hex bins) as PDF
- [ ] Written interpretation: 1 paragraph describing patterns AND limitations
- [ ] Week 5 reflection responses

**Emphasis:**
> "Your written interpretation is critical—this is where you demonstrate ethical thinking. I'm looking for:
> - Description of patterns (e.g., 'Property crime clusters in commercial districts and near transit hubs')
> - Contextual explanation (e.g., 'This aligns with high foot traffic and SEIFA disadvantage indices')
> - At least 2 limitations (e.g., 'Data reflects reported incidents only, influenced by policing patterns. Edge effects may underestimate density at study area boundaries.')
>
> Don't just describe—interpret and acknowledge uncertainty."

---

### Preview of Week 6 (1 minute)

**Transition:**
> "Next week we shift from crime to public health and accessibility. You'll combine vulnerability indices—SEIFA, health risk data—with service locations to evaluate equity in healthcare access. Think of it as: Who lives where, and how far are they from essential services like hospitals or clinics?
>
> We'll introduce network analysis—measuring travel distance along roads, not straight-line 'as the crow flies.' This is crucial for understanding real-world accessibility."

**Preparation for next week:**
- Download Week 6 datasets (hospital locations, health indices)
- Reopen Week 3 SEIFA work—you'll build on it
- Read Week 6 lecture notes on accessibility analysis

**Optional teaser:**
> "If you're interested in seeing how crime and health intersect, there's a great optional reading on the connection between disadvantage, policing, and health outcomes. Link is on the course site."

---

### Office Hours & Support (30 seconds)

> "I'll be in [location/Zoom link] for office hours on [days/times]. Bring questions, troubleshooting issues, or your draft maps for feedback.
>
> If you're stuck before then, post in the discussion forum—I and your classmates can help. Don't struggle in silence."

---

### Closing Statement (30 seconds)

> "Today you learned to map sensitive data responsibly. That's a skill you'll use throughout your GIS career—whether mapping health, environment, demographics, or infrastructure. The questions we asked today—Who does this help? Who might it harm? What am I missing?—those questions never go away.
>
> You're building both technical skills and ethical judgment. Keep practicing both. See you next week."

---

### Post-Session Tasks for Facilitator

**After class (10 minutes):**
- [ ] Note common issues that arose (add to next year's notes)
- [ ] Upload demo project file to shared drive for student reference
- [ ] Post FAQ based on student questions to discussion forum
- [ ] Review any flagged ethical concerns from student work
- [ ] Prepare feedback template for Week 5 submissions

**Before next class:**
- [ ] Download Week 6 datasets and test network analysis tools
- [ ] Review Week 5 submissions for common misconceptions to address in Week 6 opening

---

## Additional Resources for Facilitators

### Example Crime Maps for Discussion

**"Bad" Examples (stigmatizing, lacking context):**
- Search Google Images: "most dangerous neighborhoods" + [your city]
- Typical issues: Loaded language, no rates, no temporal context, no limitations

**"Good" Examples:**
- Australian Bureau of Statistics crime statistics reports (neutral framing, rates, disclaimers)
- Academic journal articles on spatial crime analysis (documented methods, acknowledged limitations)
- Police department transparency reports (context-rich, time-series comparisons)

### Recommended Readings for Deeper Prep

**For facilitators new to crime mapping ethics:**
- Chainey, S., & Ratcliffe, J. (2005). *GIS and Crime Mapping*. Wiley. (Chapter 1: Crime Mapping Ethics)
- Crampton, J., & Krygier, J. (2006). "An Introduction to Critical Cartography." *ACME: An International E-Journal for Critical Geographies*.
- Harries, K. (1999). *Mapping Crime: Principle and Practice*. NIJ Research Report.

**On KDE technical details:**
- O'Sullivan, D., & Unwin, D. (2010). *Geographic Information Analysis* (2nd ed.). Wiley. (Chapter 5: Point Pattern Analysis)

### Sample Grading Rubric for Week 5 Submissions

**KDE Heatmap (20 points):**
- [ ] Correctly loaded and filtered crime data (5 pts)
- [ ] Applied KDE with appropriate bandwidth documented (5 pts)
- [ ] Styled with appropriate color ramp and transparency (5 pts)
- [ ] Saved as properly georeferenced TIF (5 pts)

**Hex Bin Analysis (15 points):**
- [ ] Created hex grid with appropriate spacing (5 pts)
- [ ] Counted points correctly (5 pts)
- [ ] Styled using graduated symbology (5 pts)

**Boundary Comparison (20 points):**
- [ ] Aggregated by LGA and SA2 (10 pts)
- [ ] Calculated crime rates (normalized by population) (5 pts)
- [ ] Created comparison layout with 3 maps (5 pts)

**Written Interpretation (25 points):**
- [ ] Described spatial patterns observed (5 pts)
- [ ] Provided contextual explanation (5 pts)
- [ ] Acknowledged at least 2 limitations (data bias, edge effects, etc.) (10 pts)
- [ ] Used neutral, non-stigmatizing language (5 pts)

**Reflection (10 points):**
- [ ] Answered all 5 reflection questions (5 pts)
- [ ] Demonstrated critical ethical thinking (5 pts)

**Technical Quality (10 points):**
- [ ] Proper CRS used throughout (3 pts)
- [ ] Files organized and named correctly (3 pts)
- [ ] No major errors or artifacts (4 pts)

**Total: 100 points**

---

### Troubleshooting: Difficult Conversations

**Scenario 1: Student challenges the premise of data bias**

**Student says:** "But the data is objective—it's just numbers. You're inserting politics."

**Response:**
> "I appreciate that concern—let's think about how data is created. Crime data comes from police reports. Police patrol certain areas more heavily based on policy decisions. Those decisions are made by people, influenced by budgets, political pressure, historical patterns. So the data reflects those choices, not just 'objective crime.' Acknowledging that isn't political—it's accurate methodology. Does that make sense?"

**If student persists:**
> "This is a foundational concept in data science: all data has context and limitations. If you're skeptical, I encourage you to read [cite specific reading]. Let's continue this in office hours if you'd like to discuss further."

---

**Scenario 2: Student shares harmful stereotypes**

**Student says:** "Well, certain neighborhoods just have more crime because of [demographic characteristic]."

**Response (firm but educational):**
> "Let's pause there. We're analyzing spatial patterns, not making claims about communities or people. Crime is influenced by systemic factors—poverty, lack of services, historical disinvestment, policing patterns—not by the characteristics of residents. Our role as GIS professionals is to map patterns responsibly, not reinforce stereotypes. Let's refocus on the data and its limitations."

**Follow up privately after class if needed.**

---

**Scenario 3: Student feels overwhelmed by ethical considerations**

**Student says:** "This is too much—how can I ever make a map if I have to worry about all these ethical issues?"

**Response (validating, then reframing):**
> "I hear you—it can feel overwhelming at first. But think of it like this: you already apply quality control to your technical work (correct CRS, labeled axes, accurate data). Ethical analysis is just another layer of quality control. Over time, these questions become automatic: 'Did I normalize? Did I add context? Could this mislead?'
>
> Start with a few key practices:
> 1. Normalize data when comparing areas
> 2. Include a disclaimer about limitations
> 3. Use neutral language
>
> You don't need to solve every ethical dilemma—just practice responsible defaults. It gets easier with experience."

---

## Facilitator Self-Reflection

After delivering this session, consider:

1. **What ethical discussions resonated most with students?** (Note for emphasis next time)
2. **What technical issues arose repeatedly?** (Add to troubleshooting guide)
3. **Did any students seem disengaged during ethics discussion?** (Consider alternative engagement strategies)
4. **How can I better integrate ethics throughout the course, not just this week?** (Long-term pedagogical planning)
5. **Did I create a safe space for difficult conversations?** (Reflect on facilitation approach)

**Continuous improvement:** Update these notes each year based on what worked and what didn't.

---

## Quick Reference: Key Commands & Parameters

**Loading CSV Points:**
- `Layer > Add Layer > Add Delimited Text Layer`
- Geometry: Point coordinates
- CRS: Check metadata; often EPSG:4326 (WGS84)

**Reprojecting to Projected CRS:**
- `Vector > Data Management Tools > Reproject Layer`
- Target CRS: Local projected system (e.g., EPSG:7856 for Sydney)

**Filtering Data:**
- Open Attribute Table > Select by Expression
- Example: `"date" >= '2023-01-01' AND "offense_type" = 'Theft'`

**Creating KDE Heatmap:**
- `Processing > Toolbox > Search "Heatmap"`
- **Radius:** 500m (adjust based on scale)
- **Pixel size:** 50m (smaller = more detail)
- **Kernel shape:** Quartic (default)

**Styling KDE:**
- Layer Properties > Symbology
- Render type: Singleband pseudocolor
- Color ramp: YlOrRd
- Mode: Continuous
- Transparency: 60%

**Creating Hex Grid:**
- `Processing > Toolbox > Create Grid`
- Grid type: Hexagon
- Extent: Calculate from Layer
- Spacing: 500m

**Counting Points in Polygons:**
- `Processing > Toolbox > Count Points in Polygon`
- Polygons: hex_grid
- Points: crime_filtered
- Count field: crime_count

**Calculating Crime Rate:**
- Open attribute table > Field Calculator
- Formula: `"crime_count" / "population" * 1000`

---

**End of Facilitator Notes**

*These notes are a living document. Update annually based on student feedback, emerging ethical issues, and software changes. Good luck with your session!*
