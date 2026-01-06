# Week 6 Facilitator Notes: Health Accessibility Analysis

## Session Overview

### Duration
**Total: 3 hours**
- Lecture/discussion: 45 minutes
- Live demonstration: 30 minutes
- Hands-on lab work: 90 minutes
- Wrap-up & reflection: 15 minutes

### Learning Objectives
By the end of this session, students will be able to:
1. Prepare and validate health facility point data and road network data for analysis
2. Conduct network analysis using QNEAT3 to create drive-time isochrones
3. Calculate shortest path routes from population centers to health facilities
4. Overlay service areas with vulnerability indices to identify accessibility gaps
5. Interpret and communicate findings using equity-focused language
6. Document methodology in preparation for reproducible workflows in Python

### Materials Needed

**For facilitator:**
- Working QGIS project with sample health facility and road network data (pre-tested)
- Backup datasets in case students have download issues
- QNEAT3 plugin installed and tested (version compatibility confirmed)
- Example output: completed service area analysis for demonstration
- Printed reference card: QNEAT3 parameter quick guide
- Timer for activities

**For students:**
- QGIS 3.28 LTR or newer installed
- QNEAT3 plugin installed (send reminder 48 hours before class)
- Week 3 project with SEIFA/vulnerability data (remind students to bring)
- Health facility dataset downloaded
- OpenStreetMap road network downloaded
- Minimum 8GB RAM recommended (warn students with older machines)

**Datasets required:**
- Health facilities (points): hospitals, clinics, urgent care centers
- Road network (lines): OSM extract for study area
- SEIFA or vulnerability index (polygons): from Week 3
- Study area boundary (for clipping)
- Basemap access (QuickMapServices or XYZ tiles)

---

## Before Class Checklist

### 48 Hours Before
- [ ] Email students reminder to install QNEAT3 plugin
- [ ] Email reminder to download health facility and OSM road data
- [ ] Email reminder to bring Week 3 project file
- [ ] Test QNEAT3 on your machine with class datasets
- [ ] Prepare backup USB drive with all datasets
- [ ] Identify 2-3 "tech helper" students who can assist peers during lab

### 2 Hours Before
- [ ] Test classroom computer QGIS installation
- [ ] Verify projector display (check symbology colors are visible)
- [ ] Upload datasets to shared drive/LMS as backup
- [ ] Test network analysis end-to-end (15-20 minutes to ensure no surprises)
- [ ] Print QNEAT3 parameter guide (one per 2-3 students)
- [ ] Set up sample project file for demonstration
- [ ] Prepare breakout discussion groups (if using)

### Critical Pre-Test
**Run this test to avoid class-time disasters:**

1. Load sample health facilities (5-10 points)
2. Load road network clipped to small area
3. Verify both layers in same projected CRS
4. Run QNEAT3 Iso-Area with these parameters:
   - Network: road_network
   - Start points: facilities
   - Size: 900 seconds
   - Interval: 300 seconds
   - Cell size: 100 meters
   - Speed: 50 km/h
5. Confirm output completes in <3 minutes
6. Check output has 3 isochrone rings per facility

**If test fails:**
- Check network topology (run Fix Geometries)
- Verify network is connected (no isolated segments)
- Confirm CRS is projected, not geographic
- Update QNEAT3 plugin to latest version
- Consider smaller test area if memory issues

---

## Session Flow (with timing)

### 00:00-00:10 | Opening & Context Setting
**Objectives:** Frame health equity, activate prior knowledge, preview workflow

**Activities:**
- Quick poll: "Who has had to travel >30 minutes to see a doctor?" (show of hands)
- Brief news headline: Share recent story about rural hospital closure or healthcare desert
- Connect to Week 3: "You mapped where disadvantaged communities are. Today we ask: Can they reach healthcare?"
- Show striking before/after: Buffer-based access vs. network-based access map side-by-side
- Preview workflow: "Facilities → Network → Service areas → Gaps → Policy implications"

**Key talking points:**
- Access ≠ proximity (highways, rivers, public transit create barriers)
- Network analysis reveals *realistic* travel patterns
- This is the last QGIS-focused week—emphasize skill consolidation
- Next week: Python automation of these workflows

### 00:10-00:25 | Conceptual Foundation
**Objectives:** Build understanding of accessibility metrics, network analysis principles

**Content to cover:**
1. **Accessibility metrics comparison** (10 min)
   - Simple buffers: Fast but assumes "as crow flies"
   - Isochrones (service areas): Realistic travel patterns
   - Gravity models (2SFCA): Accounts for competition/capacity
   - When to use each + data requirements

2. **Network analysis fundamentals** (5 min)
   - Graph theory basics: nodes, edges, impedance
   - Time vs. distance as cost
   - One-way streets, speed limits, barriers
   - Why topology matters (connected network required)

**Teaching tip:** Use physical props—have students stand up, form a "road network" with arms as roads, demonstrate how breaks in network prevent travel

### 00:25-00:45 | Case Study & Discussion
**Objectives:** Apply concepts to real-world scenario, practice critical analysis

**Case study: Malaria Atlas Project** (or substitute local example)
- Show example accessibility maps
- Highlight data integration: facilities, roads, topography, population
- Discuss uncertainty visualization
- Policy impact: How findings influenced resource allocation

**Small group discussion (10 min):**
Prompt: "A government official says 'We have enough hospitals—everyone is within 20km.' Using what you've learned, how do you respond?"

Groups report out (5 min): Capture responses on board
- Expected themes: 20km by road vs. straight line, car ownership, public transit, vulnerable populations

**Bridge to lab:** "Now you'll generate the evidence to back up these arguments."

### 00:45-01:15 | Live Demonstration
**Objectives:** Model complete workflow, troubleshoot common issues proactively

**Demo script:** (See detailed script below)
1. Load and inspect health facility data (5 min)
2. Load and clean road network (5 min)
3. Verify CRS and network connectivity (3 min)
4. Configure and run QNEAT3 (7 min)
5. Style service areas (5 min)
6. Quick overlay with vulnerability data (5 min)

**Critical teaching moments:**
- **Data quality check:** Show students how to spot bad coordinates
- **CRS verification:** Emphasize projected vs. geographic
- **Parameter choices:** Explain why 50 km/h, why 300-second intervals
- **Interpretation:** "These gaps mean real people can't reach care"

**Narrate your thinking:** "I'm checking the CRS now because if it's in degrees, my analysis will be wrong. Let me show you what happens..." (briefly demonstrate wrong CRS → giant service areas)

### 01:15-02:45 | Hands-On Lab Work
**Objectives:** Students complete Activities 1-5, building skills through practice

**Facilitation strategy:**
- **First 15 minutes:** Circulate actively—catch setup issues early
- **Common checkpoints:**
  - 01:30 (15 min in): "Who has facilities loaded and cleaned? Thumbs up"
  - 01:50 (35 min in): "Who has road network ready? Raise hand if you need help"
  - 02:10 (55 min in): "Who is running or has finished isochrone analysis?"
  - 02:30 (75 min in): "Who has identified accessibility gaps?"

**Support triage:**
- Level 1 (Quick fixes): CRS mismatches, plugin not visible → Tech helpers or quick facilitator assist
- Level 2 (Moderate): Network topology errors, slow processing → Facilitator attention
- Level 3 (Showstoppers): Missing data, crashes → Switch to backup datasets or pair with classmate

**Stretch activities for fast finishers:**
- Create walking-access isochrones (5 km/h) and compare to driving
- Calculate shortest paths from SA2 centroids to nearest hospitals (Part 7 extension)
- Calculate population-weighted accessibility gaps
- Design inset map showing detail of worst-served area
- Research facility capacity data and discuss supply/demand

**Teaching tip:** Around 02:00 mark, do a "gallery walk"—ask 2-3 students to share screens showing their service areas. Peer learning + validates progress.

### 02:45-02:55 | Interpretation & Discussion
**Objectives:** Move from technical output to meaningful insight

**Facilitation prompts:**
1. "What surprised you about your accessibility gaps?" (open responses, 3-4 students)
2. "Who found areas that are both disadvantaged AND poorly served?" (show of hands, 1-2 examples)
3. "How would your findings change if you analyzed walking or transit access?" (think-pair-share, 2 min)

**Synthesize themes:**
- Urban vs. rural patterns
- Role of car ownership
- Interaction between socioeconomic status and access
- Limitations: Data quality, assumptions, real-world complexity

### 02:55-03:00 | Wrap-Up & Preview
**Objectives:** Consolidate learning, bridge to Python, assign deliverables

**Key messages:**
- "You've now completed 6 weeks of QGIS—you can do real spatial analysis"
- "Next week: Same analysis, but automated with Python code"
- "Documentation matters—your method notes will help you reproduce this in code"

**Deliverables reminder:**
- QGIS project file
- Service areas and gaps layers
- PDF map
- Method notes (emphasize this—it's scaffolding for Python)
- Reflection

**Exit ticket (optional):** "One thing you're confident about, one thing you're still fuzzy on" (sticky notes or online form)

---

## Key Concepts to Emphasize

### 1. Service Areas (Isochrones)
**Definition:** Polygons showing how far you can travel from a point in a given time or distance

**Emphasize:**
- Based on actual road network (not straight-line distance)
- Time-based (5, 10, 15 min) is more meaningful than distance for healthcare
- Reflects real-world barriers: rivers, highways, dead-end streets
- Overlapping zones = good coverage; gaps = underserved areas

**Common misconceptions:**
- "Bigger zones are always better" → No, depends on population distribution
- "Isochrones are perfectly accurate" → No, they assume average speed, no traffic, car ownership
- "If a zone touches an area, it's served" → Population distribution matters—use centroids or population-weighted analysis

**Visual aid:** Show buffer vs. isochrone side-by-side for same facility

### 2. Network Distance vs. Euclidean Distance
**Definition:**
- Euclidean: Straight-line "as the crow flies" distance
- Network: Actual travel distance along roads

**Emphasize:**
- Euclidean underestimates travel time (ignores roads, barriers)
- Network analysis requires connected road network (topology)
- Real-world factors: One-way streets, traffic, road quality (not always in data)

**Demonstration:** Show facility that's "close" by Euclidean distance but far by network distance (e.g., across river with limited bridge crossings)

**Teaching tip:** Have students estimate: "How far is your home from campus as the crow flies? How far do you actually travel?" Calculate ratio—often 1.3-1.8x

### 3. Accessibility Metrics (Continuum)
**Framework:** Different questions need different metrics

| Metric | Question | Data needed | When to use |
|--------|----------|-------------|-------------|
| **Simple buffer** | Is there a facility nearby? | Facility locations | Initial screening, data-scarce contexts |
| **Isochrone (network)** | Can people reach facilities? | Facilities + road network | Policy planning, resource allocation |
| **Gravity model (2SFCA)** | Is supply adequate for demand? | Facilities + network + population + capacity | Advanced planning, equity research |

**Emphasize:** Each adds complexity and realism, but requires more data and assumptions

**Class discussion:** "When might a simple buffer be *better* than network analysis?" (Answer: Walking/biking distances, rough regional screening, limited data quality)

### 4. Equity vs. Equality in Accessibility
**Definitions:**
- Equality: Everyone has same service area coverage
- Equity: Service meets needs—may require disproportionate resources for vulnerable populations

**Emphasize:**
- Accessibility gaps + vulnerability = priority areas
- Equal geographic coverage ≠ equitable health outcomes
- Transportation equity matters: Who has cars? Public transit?

**Discussion prompt:** "If you had funding for one new clinic, where would you put it? Justify using your analysis."

### 5. Data Quality and Assumptions
**Critical concept:** Analysis is only as good as the data

**Emphasize:**
- OSM completeness varies (better in urban areas)
- Facility data may be outdated (hospitals close)
- Speed assumptions are averages (traffic, weather vary)
- Car ownership is assumed (often invalid for disadvantaged populations)
- Opening hours, service capacity not captured

**Teaching strategy:** Have students list 3 assumptions in their analysis and 3 ways findings could be wrong—builds critical thinking

---

## Live Demo Script

### Part 1: Load and Inspect Health Facility Data (5 min)

**Narrate:**
"I'm starting with a CSV of hospital locations. First thing: Verify the data quality—bad coordinates will ruin our analysis."

**Steps:**
1. `Layer → Add Layer → Add Delimited Text Layer`
2. Select `health_facilities.csv`
3. Check "First record has field names"
4. Geometry: X field = `longitude`, Y field = `latitude`
5. CRS: EPSG:4326 (WGS84)
6. Add layer

**Inspect:**
7. Right-click → `Open Attribute Table`
8. "I'm checking for missing coordinates, duplicate names, facility status"
9. `Zoom to Layer` → "Do these points look reasonable?"
10. Add basemap (QuickMapServices → Google Satellite)
11. Click 2-3 facilities: "I'm spot-checking—does this hospital really exist here?"

**Clean:**
12. `Select → Select by Expression`
13. `"status" = 'Active' AND "type" IN ('Hospital', 'Clinic')`
14. Right-click → `Export → Save Selected Features As...`
15. Format: GeoPackage, CRS: **EPSG:XXXX (local projected CRS)**
16. Save to `data/processed/week06/health_facilities.gpkg`

**Emphasize:** "I reprojected to a local CRS because network analysis needs meters, not degrees."

### Part 2: Load and Clean Road Network (5 min)

**Narrate:**
"Network analysis needs a connected road network. I downloaded OpenStreetMap data, but it includes footpaths, cycleways—we only want drivable roads."

**Steps:**
1. `Layer → Add Vector Layer` → select `osm_roads.shp`
2. `Zoom to Layer` → "Look at this—millions of road segments"
3. Right-click → `Open Attribute Table` → "The 'highway' field tells us road type"

**Filter:**
4. `Select → Select by Expression`
5. ```
   "highway" IN ('motorway', 'trunk', 'primary', 'secondary', 'tertiary', 'residential')
   ```
6. "This keeps major roads only—reduces processing time"
7. `Right-click → Export → Save Selected Features As...`

**Clip:**
8. `Processing → Toolbox → Vector overlay → Clip`
9. Input: selected roads, Overlay: study area boundary
10. Save to `data/processed/week06/road_network.gpkg`

**Emphasize:** "Smaller network = faster processing. I clipped to my study area."

### Part 3: Verify CRS and Network Connectivity (3 min)

**CRS check:**
1. Right-click road_network → `Properties → Information`
2. "Confirm CRS is projected—should say 'meters' in the units"
3. Right-click facilities → `Properties → Information`
4. "Both layers MUST be in same CRS—QNEAT3 won't auto-reproject"

**Connectivity check:**
5. `Zoom in` to a section of road network
6. "I'm looking for gaps—roads should touch at intersections"
7. (If gaps exist): `Processing → Vector geometry → Fix geometries`
8. "If your network has major gaps, isochrones won't cross them—check your data"

**Emphasize:** "If your CRS is wrong or network is disconnected, you'll get empty output or errors. Check now, not after waiting 15 minutes for processing."

### Part 4: Configure and Run QNEAT3 (7 min)

**Narrate:**
"Now the network analysis. QNEAT3 calculates how far you can travel in a given time."

**Steps:**
1. `Processing → Toolbox` → search "iso-area"
2. Select **QNEAT3 → Iso-Area as Polygons (from Point)**
3. Configure parameters:

**Walk through each parameter:**
- **Network layer:** `road_network` → "This is our road network"
- **Start points:** `health_facilities` → "These are the hospitals"
- **Unique Point ID field:** `facility_name` → "Identifies each hospital in output"
- **Size of Iso-Area:** `900` → "15 minutes × 60 seconds = 900 seconds total"
- **Contour interval:** `300` → "Creates zones at 5, 10, 15 minutes"
- **Cell size:** `100` → "Resolution—smaller is more detailed but slower. 50-100m is good."
- **Direction field:** Leave blank → "Unless you have one-way street data"
- **Default speed:** `50` → "50 km/h for driving. Use 5 for walking."
- **Output:** `data/processed/week06/health_service_areas.gpkg`

**Before clicking Run:**
"This will take 5-10 minutes. If it takes longer than 15 minutes or QGIS freezes, stop it—your network might be too large. I tested with 5 facilities first to make sure it works."

4. Click **Run**
5. (While processing): "Let me show you what we expect to see..." (show pre-made example)

**Teaching tip:** If you have time, run a SMALL test (2-3 facilities, small area) live. For full demo, use pre-computed output to avoid waiting.

### Part 5: Style Service Areas (5 min)

**Narrate:**
"The output shows travel time zones. Let's make them visually intuitive—green for close, yellow/orange for farther."

**Steps:**
1. Right-click output layer → `Properties → Symbology`
2. Change from `Single Symbol` to `Categorized`
3. **Value:** Select the time field (often `cost_level` or `iso_value`)
4. Click `Classify`
5. Assign colors:
   - 300 (5 min): Dark green
   - 600 (10 min): Yellow
   - 900 (15 min): Orange
6. Click `OK`

**Transparency:**
7. Re-open `Properties → Transparency`
8. Set **Opacity** to 50%
9. "This lets us see overlapping zones and the basemap underneath"

**Checkpoint:**
10. `Zoom to Layer`
11. "You should see concentric rings around each facility. Close facilities have overlapping zones—that's good coverage. Look for gaps between orange zones—those are underserved areas."

**Emphasize:** "If zones are weirdly large (covering whole state) or tiny (just around point), check your CRS and speed setting."

### Part 6: Quick Overlay with Vulnerability Data (5 min)

**Narrate:**
"Accessibility gaps are most concerning where vulnerable populations live. Let's overlay SEIFA."

**Steps:**
1. Load SEIFA layer from Week 3 (or have it pre-loaded)
2. Move service_areas layer above SEIFA in Layers Panel
3. Move health_facilities to top

**Identify gaps:**
4. Visual scan: "Where are orange/yellow zones touching low SEIFA decile areas?"
5. `Processing → Toolbox → Vector overlay → Difference`
6. Input: SEIFA layer (filtered to deciles 1-2)
7. Overlay: service_areas (15-min zones only)
8. "This identifies disadvantaged areas NOT covered by 15-minute zones"
9. Output: `accessibility_gaps.gpkg`

**Style gaps:**
10. Red fill, high opacity—"These stand out as priority areas"

**Interpret:**
11. Click on a gap polygon → Show attributes
12. "This SA2 has 12,000 people in disadvantage decile 1, and no hospital within 15 minutes by car. If they don't have cars, it's even worse."

**Wrap demo:**
"That's the workflow. Now you'll do this with your own data. Remember: Check CRS first, start with small network, save your work before running QNEAT3."

---

### Part 7: Shortest Path Analysis (Optional Extension, 10 min)

**Purpose:** Calculate actual travel routes from population centers to nearest health facilities

**When to include:** If time permits and students want to explore beyond isochrones

**Narration:**
"Isochrones show catchment areas—but what if you want to know the actual route someone would take to reach a hospital? That's shortest path analysis."

**Steps:**

1. **Open Processing Toolbox:**
   - Search for "Shortest path"
   - Select **QNEAT3 → Shortest path (point to layer)**

2. **Configure parameters:**
   - **Network layer:** road_network
   - **Start point:** Click a point on the map (e.g., town center in a gap area)
   - **End points layer:** health_facilities
   - **Direction field:** Leave blank (undirected)
   - **Default speed:** 50 km/h
   - **Strategy:** Shortest (fastest if speed varies by road type)

3. **Run and interpret:**
   - Output shows the optimal route to nearest facility
   - Attribute table shows distance and travel time
   - "This resident in [area] would need to travel 23 km, taking 28 minutes to reach the nearest hospital"

4. **Teaching points:**
   - Shortest path = specific routes for specific origins
   - Different from isochrones (catchment areas)
   - Useful for: ambulance routing, patient journey mapping, community-specific analysis
   - Can run for multiple origins (e.g., SA2 centroids to nearest facility)

**Style the route:**
- Line symbology: red, 2mm stroke
- Add arrows to show direction (if using directed network)

**Discussion prompt:**
"If you ran shortest path from every SA2 centroid to the nearest hospital, what patterns might emerge? How might this inform ambulance station locations?"

**Note:** This activity demonstrates shortest path for health accessibility. For other applications like wildlife corridors or off-road movement, students would need cost-surface analysis (least-cost path)—which is beyond this week's scope but covered in external resources linked in the capstone examples guide.

---

## Discussion Prompts

### Health Equity and Social Determinants

**Prompt 1: Defining the Problem**
"We often hear 'healthcare deserts.' Based on what you've learned, how would you define that term using GIS concepts?"

*Expected responses:*
- Areas outside service catchments
- Gaps in network-based access
- High demand, low supply ratio

*Facilitator follow-up:*
"How does this differ from 'food deserts' or 'banking deserts'? What's similar?"

---

**Prompt 2: Beyond Geography**
"Your analysis shows a community is within 10 minutes of a hospital. Does that mean they have good healthcare access?"

*Expected responses:*
- No—may not have car
- May not have insurance
- Hospital may not have capacity/specialists
- Cultural/language barriers

*Facilitator synthesis:*
"Right—spatial access is necessary but not sufficient. GIS shows WHERE, but we need other data for WHY and HOW."

---

### Rural vs. Urban Access Patterns

**Prompt 3: Urban-Rural Divide**
"Compare your urban and rural service areas. What patterns do you notice? Why?"

*Expected responses:*
- Urban: Small zones, lots of overlap, high coverage
- Rural: Large zones, gaps between facilities, sparse coverage

*Facilitator probe:*
"Is the solution just 'build more rural hospitals'? What are the constraints?" (Cost, population density, workforce recruitment, sustainability)

---

**Prompt 4: Mode of Transport**
"In cities, many people don't drive—they walk, bike, or use transit. How would that change your analysis?"

*Expected responses:*
- Much smaller service areas for walking
- Need transit network, not road network
- Access gaps grow significantly

*Facilitator activity:*
"Calculate: If someone walks 5 km/h, how far can they go in 15 minutes?" (1.25 km vs. 12+ km driving)
"Who is most likely to depend on walking?" (Elderly, low-income, youth, disability)

---

### Policy Implications

**Prompt 5: Evidence for Action**
"You're presenting to a city council. They have budget for one new clinic. How do you use your GIS analysis to recommend a location?"

*Expected responses:*
- Largest accessibility gap
- Highest vulnerable population outside service areas
- Balance distance and population density

*Facilitator challenge:*
"Council member says 'But that neighborhood already has a community center—can't they just go there for healthcare?' How do you respond?" (Licensing, equipment, staffing, funding mechanisms)

---

**Prompt 6: Unintended Consequences**
"A hospital closes due to budget cuts. How would you use GIS to analyze the impact?"

*Expected responses:*
- Re-run isochrones without that facility
- Identify new gaps
- Calculate population affected

*Facilitator expansion:*
"What secondary impacts might occur that GIS can't easily show?" (Ambulance response times, ED crowding at remaining hospitals, economic impact on neighborhood)

---

### Critical Analysis & Limitations

**Prompt 7: Assumptions and Uncertainty**
"List 3 assumptions your analysis makes. How might real-world conditions differ?"

*Expected assumptions:*
- Everyone has a car
- Average speed is constant
- Roads are always passable
- Hospitals accept all patients
- Facilities are open 24/7

*Facilitator synthesis:*
"This doesn't invalidate your analysis—but you must communicate these limitations. How would you phrase a caveat in your map title or legend?"

---

**Prompt 8: Data Quality**
"OpenStreetMap is crowd-sourced. How might data quality vary geographically? How does that affect your confidence in results?"

*Expected responses:*
- Better data in urban areas, popular regions
- Rural/remote areas may have outdated or missing roads
- Developing countries may have gaps

*Facilitator discussion:*
"What's your responsibility as an analyst when presenting results based on incomplete data?" (Transparency, uncertainty quantification, local validation)

---

### Ethical Considerations

**Prompt 9: Language Matters**
"Look at your map. Does your title/legend use deficit language ('underserved,' 'lacking access') or strength-based language? How might affected communities prefer to be described?"

*Facilitator guidance:*
- Avoid: "Healthcare deserts," "inadequate," "deprived"
- Consider: "Priority areas for health investment," "communities with travel barriers," "areas requiring mobile clinics"
- Center solutions, not deficits

---

**Prompt 10: Who Benefits?**
"GIS accessibility analysis can be used for good (equity planning) or harm (hospital closures, insurance redlining). How do you ensure your work contributes to equity?"

*Expected responses:*
- Engage communities in interpretation
- Transparent methods
- Frame recommendations around justice
- Consider who commissioned the analysis

*Facilitator close:*
"You have power as analysts. Use it responsibly."

---

## Common Student Issues

### 1. Network Topology Errors

**Symptom:**
- Empty output from QNEAT3
- Error: "Network is not connected"
- Service areas only around some facilities, not others

**Diagnosis:**
- Road network has gaps (disconnected segments)
- Start points not snapped to network
- One-way streets blocking travel (if direction field set incorrectly)

**Solutions:**
1. **Fix geometries:**
   - `Processing → Vector geometry → Fix geometries`
   - Input: road_network
   - Run on network layer

2. **Check connectivity visually:**
   - Zoom to problem areas
   - Look for gaps at intersections
   - Use `Vector → Analysis Tools → Line Intersections` to find disconnections

3. **Snap points to network:**
   - `Processing → Vector geometry → Snap geometries to layer`
   - Input: health_facilities
   - Reference: road_network
   - Tolerance: 50-100 meters
   - Creates new layer with snapped points

4. **Simplify network:**
   - If OSM data is too complex, use only major roads
   - Filter to `"highway" IN ('motorway', 'primary', 'secondary', 'tertiary')`

**Prevention:**
- Download OSM data from reliable source (Geofabrik)
- Clip to reasonable study area
- Test with 2-3 facilities first before running all

---

### 2. Large Network Processing Time

**Symptom:**
- QNEAT3 runs for >20 minutes
- QGIS becomes unresponsive
- Progress bar stuck at 0% or 99%
- Computer fan runs loudly (memory/CPU overload)

**Diagnosis:**
- Network too large (e.g., entire country instead of city)
- Too many start points (e.g., 500+ facilities)
- Cell size too small (e.g., 10 meters)
- Insufficient RAM

**Solutions:**
1. **Reduce network size:**
   - Clip road network to smaller study area
   - Use `Processing → Vector overlay → Clip` with boundary polygon
   - Remove minor roads (keep only major road types)

2. **Process in batches:**
   - Select 10 facilities at a time
   - Run QNEAT3 on selection
   - Merge outputs afterward using `Vector → Data Management Tools → Merge Vector Layers`

3. **Increase cell size:**
   - Change from 50m to 100m or 150m
   - Reduces detail but speeds processing dramatically
   - 100m is usually sufficient for regional analysis

4. **Close other applications:**
   - Free RAM by closing browsers, other programs
   - Save work before running

5. **Use simpler analysis:**
   - If network analysis is too slow, fall back to buffers for initial screening
   - Note limitations in documentation

**Prevention:**
- Always test with small dataset first (5 facilities, small area)
- Monitor processing time on test—if >3 minutes, optimize before full run
- Check RAM availability: `Activity Monitor` (Mac) or `Task Manager` (Windows)

**Teaching tip:** Set expectation that network analysis is computationally intensive. Show students how to estimate: "If 5 facilities take 3 minutes, 50 will take ~30 minutes."

---

### 3. CRS Mismatch / Wrong Units

**Symptom:**
- Service areas are tiny (just around point) or gigantic (covering whole map)
- Error: "Layer CRS does not match project CRS"
- Distances/times seem unrealistic

**Diagnosis:**
- Network or facilities in geographic CRS (EPSG:4326, degrees) instead of projected (meters)
- Layers in different CRS
- Size parameter interpreted as degrees instead of meters

**Solutions:**
1. **Check CRS of all layers:**
   - Right-click each layer → `Properties → Information`
   - Look for "Units: degrees" (BAD) vs. "Units: meters" (GOOD)

2. **Reproject to local projected CRS:**
   - Right-click layer → `Export → Save Features As...`
   - CRS: Choose appropriate local projection:
     - Australia: GDA2020 MGA zones (EPSG:7850-7859)
     - USA: State Plane or UTM zones
     - UK: British National Grid (EPSG:27700)
   - Repeat for all layers

3. **Verify project CRS:**
   - Bottom-right corner of QGIS → Click CRS code
   - Set to same projected CRS as layers
   - Enable "On-the-fly CRS transformation" (should be default)

**Prevention:**
- Include CRS check as explicit step in demo
- Provide CRS quick reference card for students' region
- Build habit: "Check CRS first, before any analysis"

**Teaching tip:** Show dramatic example—run QNEAT3 with geographic CRS, show absurd result, then reproject and re-run to show correct output. Students remember visual mistakes.

---

### 4. QNEAT3 Plugin Not Visible/Working

**Symptom:**
- Plugin installed but doesn't appear in Processing Toolbox
- QNEAT3 tools grayed out
- Error: "Could not load QNEAT3"

**Diagnosis:**
- Plugin not activated after installation
- QGIS needs restart
- Processing plugin disabled
- Incompatible QGIS version

**Solutions:**
1. **Restart QGIS:**
   - Close and reopen QGIS completely
   - Check Processing Toolbox again

2. **Verify plugin is enabled:**
   - `Plugins → Manage and Install Plugins → Installed`
   - Check box next to QNEAT3 is checked
   - If not listed, reinstall: `All → search "QNEAT3" → Install Plugin`

3. **Enable Processing plugin:**
   - `Plugins → Manage and Install Plugins → Installed`
   - Ensure "Processing" is checked (core plugin)

4. **Check Processing Toolbox settings:**
   - `Processing → Options`
   - Under "Providers," ensure QNEAT3 is checked/activated

5. **Update QGIS:**
   - QNEAT3 requires QGIS 3.x (LTR 3.28+ recommended)
   - If using older version, update QGIS first

**Prevention:**
- Send installation instructions 48 hours before class
- Have students send screenshot of installed plugins
- Prepare backup: Students without plugin can pair with neighbor

**Emergency workaround:**
- Use built-in `Service Area (from layer)` tool (limited functionality)
- Or: Use buffer as rough approximation (15 min drive ≈ 12 km buffer at 50 km/h)

---

### 5. Service Areas Have Strange Shapes or Holes

**Symptom:**
- Isochrones have irregular holes inside
- Service areas don't expand smoothly
- Polygons have jagged edges or artifacts

**Diagnosis:**
- Network has disconnected segments (islands)
- One-way streets or barriers in data
- Cell size too large (low resolution)
- True geographic barriers (rivers, highways without crossings)

**Solutions:**
1. **Check if holes are real barriers:**
   - Overlay basemap
   - Are holes rivers, parks, gated communities?
   - If yes, this is CORRECT—those areas are truly unreachable

2. **If holes are artifacts:**
   - Decrease cell size from 100m to 50m (increases resolution)
   - Run `Fix geometries` on road network
   - Check for one-way streets: Filter `"oneway" = 'yes'` and review

3. **Smooth polygons (aesthetic only):**
   - `Processing → Vector geometry → Smooth`
   - Iterations: 2-3
   - Note: This is cosmetic—doesn't change analysis

**Prevention:**
- Emphasize to students: "Strange shapes might be real barriers—check the map!"
- Distinguish between data errors and genuine geographic constraints

**Teaching moment:** Show example of river with limited bridges—explain why isochrone has hole or narrow connector. Builds spatial thinking.

---

### 6. "Difference" Tool Produces Empty/Unexpected Result

**Symptom:**
- Overlay analysis (finding gaps) returns empty layer
- Or: Returns entire input layer unchanged

**Diagnosis:**
- No actual overlap between layers (service areas cover all vulnerable areas—good news!)
- CRS mismatch
- Invalid geometries
- Layer order reversed

**Solutions:**
1. **Visual check first:**
   - Load both layers
   - Do they visually overlap?
   - If no overlap, result will be empty

2. **CRS alignment:**
   - Both layers must be in same CRS
   - Reproject if needed

3. **Fix geometries:**
   - `Processing → Vector geometry → Fix geometries`
   - Run on BOTH input layers
   - Try Difference again

4. **Check layer order:**
   - Difference: Input A - Overlay B
   - Input = vulnerable areas (what you want to keep)
   - Overlay = service areas (what you want to subtract)
   - Reverse if wrong

5. **Alternative method:**
   - Use `Select by Location` instead
   - Select vulnerable areas that DON'T intersect service areas
   - Export selection

**Prevention:**
- Demo both successful overlap (gaps found) and full coverage (no gaps)
- Explain: Empty result might mean good coverage, not error

---

### 7. Students Can't Find Downloaded Data

**Symptom:**
- "I downloaded the data but I can't find it"
- Loading wrong file (e.g., metadata instead of shapefile)
- Can't remember which OSM extract to use

**Solutions:**
1. **Standardize folder structure:**
   - Provide template: `data/raw/week06/` and `data/processed/week06/`
   - Have students screenshot their folder structure

2. **Check Downloads folder:**
   - Often files are in Downloads, not organized
   - Move to proper project folder

3. **Identify correct file:**
   - OSM: Look for `.shp` file OR `.gpkg` file (not `.txt` or `.md`)
   - Health facilities: `.csv`, `.gpkg`, `.geojson`, or `.shp`
   - If multiple files, check dates (most recent)

4. **Re-download from shared drive:**
   - Have backup datasets on USB or shared drive
   - Distribute to students who are stuck

**Prevention:**
- Provide step-by-step download video/tutorial
- Include screenshot of "correct" file structure in lab instructions
- Do data download as Week 5 homework so issues surface before class

---

### 8. Analysis Completes But Results Don't Make Sense

**Symptom:**
- Service areas present but wrong scale/pattern
- Coverage seems too high or too low
- Isochrones cross obvious barriers

**Diagnosis:**
- Wrong speed parameter (e.g., 500 km/h instead of 50)
- Wrong size units (e.g., 900 km instead of 900 seconds)
- CRS in wrong units (degrees)
- Network includes ferries, air routes (if using full OSM)

**Solutions:**
1. **Verify parameters:**
   - Speed: 50 km/h driving, 5 km/h walking, 15-20 km/h biking
   - Size: 900 seconds = 15 minutes (NOT 900 meters or 900 km)
   - Cell size: 50-150 meters

2. **Sanity check:**
   - "In 15 minutes at 50 km/h, I can travel ~12.5 km"
   - Does the isochrone radius look approximately 12 km?
   - If not, re-check parameters

3. **Filter network:**
   - Remove ferries: `"highway" != 'ferry'`
   - Remove proposed/construction roads: `"status" = 'active'`

**Prevention:**
- Include "expected output" screenshots in lab manual
- Provide parameter checklist card
- Have students estimate before running: "How far should 15-min zone extend?"

---

## Wrap-Up & Preview

### Session Closing (5 minutes)

**Consolidate key learning:**
"Today you learned to measure healthcare access using network analysis—a skill used by planners, policymakers, and public health professionals worldwide. You can now:"

1. Set up network analysis with real-world data
2. Generate evidence-based accessibility maps
3. Identify underserved populations using spatial overlay
4. Think critically about assumptions and limitations

**Emphasize skill progression:**
"Six weeks ago, you were learning to load shapefiles. Today, you conducted advanced network analysis. That's significant growth."

**Validate effort:**
"Network analysis is challenging—if you struggled with topology or processing time, that's normal. These are professional-level skills."

---

### Bridge to Python (3 minutes)

**Frame transition:**
"This is your last QGIS-focused week. Next week, we shift to Python. You might be thinking: 'Why learn Python if I can do this in QGIS?' Here's why:"

**Python advantages:**
1. **Reproducibility:** Run same analysis on new data with one click
2. **Automation:** Process 100 cities instead of 1
3. **Customization:** Build tools QGIS doesn't have
4. **Integration:** Combine with statistics, machine learning, web apps

**Reassure students:**
"You won't lose QGIS skills—Python uses same concepts (layers, CRS, overlay). Think of it as learning to drive stick shift after learning automatic. Same destination, different tool."

**What to expect:**
- Week 7: Python basics, reading spatial data
- Week 8: Spatial analysis with GeoPandas (same tools, code-based)
- Week 9: Automation and iteration
- Week 10: Project work

**Action item:**
"Your method notes from today will help you translate QGIS workflows to Python. Keep them detailed!"

---

### Deliverables Reminder (2 minutes)

**Review checklist:**
Display on screen/board:

- [ ] QGIS project file: `projects/week06_health_accessibility.qgz`
- [ ] Service areas layer: `data/processed/week06/health_service_areas.gpkg`
- [ ] Accessibility gaps layer: `data/processed/week06/accessibility_gaps.gpkg`
- [ ] PDF map: `exports/week06_health_accessibility.pdf`
- [ ] Method documentation: `projects/week06_method_notes.txt`
- [ ] Reflection: Answer 5 reflection questions (see lab manual)
- [ ] Summary statistics: Include in reflection or separate file

**Due date:** [Specify—typically 1 week]

**Submission method:** [LMS upload, shared drive, etc.]

---

### Reflection Prompts (Highlight Key Questions)

**Point students to reflection questions in lab manual:**
1. Which areas had worst accessibility? Were you surprised?
2. How would findings change if you analyzed walking access?
3. What additional data would strengthen analysis?
4. Who are stakeholders? How might findings be used or misused?
5. How confident are you in results? Sources of uncertainty?

**Emphasize:**
"These questions push beyond technical skills to critical thinking. There's no single right answer—I want to see YOUR reasoning."

---

### Final Encouragement

**Acknowledge effort:**
"Network analysis is one of the most complex GIS workflows. If your computer crashed, if you're still troubleshooting, if you're not sure your results are right—that's all part of learning. Persistence matters more than perfection."

**Offer support:**
"Office hours: [Times]. I'm available to help debug, discuss results, or talk about what you're learning."

**Preview next week:**
"Next Tuesday: Install Python and Jupyter notebooks. Instructions posted on [LMS/website]. Start early so we can troubleshoot before class."

**End on impact:**
"The maps you're creating this week could inform real decisions about where to invest in health infrastructure. That's the power of GIS—and the responsibility you now hold."

---

### Optional: Exit Ticket

**Quick formative assessment** (digital form or index cards):

1. One thing you're confident about from today:
2. One thing you're still confused about:
3. One question you have about Python/upcoming weeks:

**Use responses to:**
- Identify concepts needing reinforcement next week
- Tailor Python intro to address concerns
- Follow up with struggling students

---

## Additional Notes for Facilitators

### Time Management Tips

**If running behind:**
- **Cut:** Malaria case study (assign as reading)
- **Shorten:** Small group discussions to 5 minutes
- **Streamline:** Demo Part 6 (overlay) quickly or show pre-made result

**If running ahead:**
- **Extend:** Hands-on lab time (students always need more)
- **Add:** Gallery walk—students present their service areas
- **Deepen:** Discussion prompt 10 (ethics)

**Critical time sinks to avoid:**
- Troubleshooting individual plugin issues during demo (delegate to tech helpers)
- Waiting for full network analysis during live demo (use pre-computed)
- Debugging student data downloads (have backups ready)

---

### Differentiation Strategies

**For struggling students:**
- Pair with stronger peer for lab work
- Provide simplified dataset (5 facilities, small area)
- Offer buffer-based analysis as alternative if network analysis fails
- Focus on interpretation over technical execution

**For advanced students:**
- Challenge: Walking vs. driving comparison
- Challenge: Population-weighted accessibility metrics
- Challenge: Research and implement 2SFCA (Two-Step Floating Catchment Area)
- Invite to help debug peers' issues (teaching deepens learning)

**For students with older/slower computers:**
- Provide pre-computed service areas—focus on interpretation and overlay
- Pair with student with better hardware for processing steps
- Emphasize method documentation (can run analysis later)

---

### Assessment Considerations

**What to grade:**
- **Process (40%):** Documented workflow, appropriate parameters, troubleshooting
- **Product (30%):** Service areas, gaps identified, map quality
- **Interpretation (30%):** Reflection depth, critical thinking, limitations acknowledged

**Common grading pitfalls to avoid:**
- Penalizing "weird" service areas that reflect real barriers (grade understanding, not aesthetics)
- Requiring perfect topology (acknowledge if student documented struggle)
- Expecting uniform map aesthetics (focus on clarity and completeness)

**Rubric emphasis:**
- Documentation: Can someone reproduce your analysis?
- Assumptions: Did you state what you assumed (car ownership, speed, etc.)?
- Limitations: Do you understand data quality constraints?
- Insight: Did you move beyond "here's a map" to "here's what it means"?

---

### Equity and Inclusion Considerations

**Content sensitivity:**
- Healthcare access is personal—students may have experienced barriers
- Frame deficit language carefully (avoid blaming communities)
- Acknowledge systemic causes (policy, investment, history)

**Examples and case studies:**
- Use local examples students can relate to
- Include diverse geographies (urban, rural, regional)
- If possible, incorporate Indigenous health access (Australia) or tribal lands (USA/Canada)

**Language:**
- Avoid: "Poor areas," "bad neighborhoods," "lacking"
- Use: "Under-resourced," "experiencing barriers," "priority for investment"
- Center agency: "Communities advocating for healthcare access" not "underserved populations"

---

### Follow-Up Actions

**Within 24 hours:**
- [ ] Email summary: Key concepts, deliverables, Python prep instructions
- [ ] Post demo project file to shared drive (for students who want reference)
- [ ] Review exit tickets and identify struggling students
- [ ] Respond to individual support requests

**Within 1 week:**
- [ ] Check midpoint: How many students have submitted?
- [ ] Send reminder to students who haven't started
- [ ] Prepare Python installation guide and test datasets
- [ ] Review this week's reflections—use insights to adjust future weeks

---

### Resources for Further Learning

**Share with students (optional enrichment):**
- QNEAT3 documentation: https://root676.github.io/
- OpenStreetMap road network guide: https://wiki.openstreetmap.org/
- Two-Step Floating Catchment Area (2SFCA): Academic papers
- Malaria Atlas Project: https://malariaatlas.org/
- CDC Social Vulnerability Index: https://www.atsdr.cdc.gov/placeandhealth/svi/

**For facilitators:**
- Network analysis theory: Rodrigue, J.-P., et al. "The Geography of Transport Systems"
- Health equity GIS: Cromley & McLafferty "GIS and Public Health"
- Accessibility metrics comparison: Neutens, T. (2015) on gravity models

---

## Conclusion

Week 6 is a pivotal session—students apply advanced GIS techniques to meaningful public health questions while building documentation habits that scaffold Python learning. Your role is to balance technical facilitation with critical discussion, ensuring students develop both skills and ethical awareness.

Remember: Struggles with topology and processing time are normal. Celebrate progress, validate effort, and emphasize that professional GIS analysts face these same challenges.

Good luck, and enjoy seeing students' "aha!" moments when their accessibility maps reveal hidden patterns!

---

**Document version:** 1.0
**Last updated:** 2025-12-23
**Contact:** [Facilitator coordinator email]
