# Week 10 Facilitator Notes: Transport Networks & Accessibility

## Session Overview

**Duration:** 2-hour session

**Learning Objectives:**
By the end of this session, students will be able to:

1. Download and configure street network graphs using OSMnx from OpenStreetMap
2. Calculate travel-time isochrones (service areas) for walking, cycling, or driving using network analysis algorithms
3. Overlay isochrones with population or vulnerability data to identify underserved communities
4. Compare Python network analysis to QGIS QNEAT3 workflows—understanding when automation adds value

**Materials Needed:**

- Student-facing content: `/site_docs/weeks/week10.md`
- Jupyter notebook: `/notebooks/week10_transport_networks.ipynb`
- Stable internet connection (CRITICAL - see backup plan if unavailable)
- Facility locations dataset (hospitals, schools, parks, etc.) saved as `facilities.geojson`
- Optional: Population/SEIFA data from Week 3 for equity analysis
- Google Colab accounts OR local Anaconda environment with OSMnx installed

**Software Environment:**

- Python packages: `osmnx`, `networkx`, `geopandas`, `matplotlib`
- Test installation before class: `python -c "import osmnx; print('Ready!')"`

---

## Before Class Checklist

**48 Hours Before:**

- [ ] Test OSMnx download with a SMALL suburb (e.g., "Carlton, Melbourne" or "Cambridge, Massachusetts")
- [ ] Time the download—it should take 10-30 seconds for a suburb
- [ ] Verify OpenStreetMap Overpass API is responding (check status: https://overpass-api.de/api/status)
- [ ] Prepare backup pre-downloaded network graph (save as `.graphml`) in case of API issues
- [ ] Test Colab notebook execution—run all cells to ensure no package conflicts
- [ ] Prepare 2-3 sample facility points relevant to your local context
- [ ] Check that students can access the GitHub repository and download the notebook

**1 Hour Before:**

- [ ] Open the Jupyter notebook and run imports cell
- [ ] Load the sample network graph for live demo
- [ ] Prepare slides/whiteboard for explaining graph theory concepts (nodes, edges, Dijkstra's algorithm)
- [ ] Queue up OpenStreetMap website in browser to show data source
- [ ] Have backup activity ready (manual network drawing exercise if internet fails)
- [ ] Print or display key troubleshooting tips (see Common Student Issues section)

**Internet Requirements:**

This session REQUIRES internet connectivity for:
- OSMnx downloading networks from OpenStreetMap Overpass API
- Students using Google Colab
- Accessing package documentation

**Critical:** Test downloads with student-typical suburb sizes. A whole city (e.g., "Melbourne, Australia") can take 5-15 minutes and may overwhelm beginners. Emphasize "suburb first, scale later."

---

## Session Flow (with Timing)

### Part 1: Introduction & Setup (20 minutes)

**0:00-0:10 | Opening & Context**

- Review accessibility questions from real-world planning: "How far is the nearest hospital?" "Which neighborhoods lack park access?" "Does our city meet the 15-minute city goal?"
- Connect to Week 6 (QGIS QNEAT3): "You've done this manually—today we automate it with code"
- Emphasize reproducibility: "This notebook can run on 100 cities with minimal changes"
- Show final output: isochrone map showing 5/10/15-minute walking zones

**0:10-0:15 | Conceptual Introduction to Network Graphs**

Use whiteboard or slides to explain:

- **Nodes** = intersections (where streets meet)
- **Edges** = street segments (the roads connecting intersections)
- **Weights** = attributes like length (meters), travel time, speed limit
- **Graph theory** = mathematical framework for analyzing connected systems

Draw a simple network:
```
    A ---100m--- B
    |             |
  150m          80m
    |             |
    C ---120m--- D
```

Ask: "What's the shortest path from A to D?" (walk through by hand: A→B→D = 180m vs A→C→D = 270m)

**0:15-0:20 | Environment Setup**

Guide students through:

1. Opening the notebook (Colab or local Jupyter)
2. Running the imports cell
3. Confirming no errors appear
4. Explaining `ox.settings.use_cache = True` (saves downloaded networks locally)

**Check-in:** "Everyone see 'Ready!' printed? Raise your hand if you see an error."

---

### Part 2: Live Demo - Downloading & Exploring Networks (30 minutes)

**0:20-0:30 | Demo: Download a Street Network**

**CRITICAL MESSAGING:** "We're starting with ONE SUBURB, not a whole city. This will take 10-30 seconds. If you try a whole state, it could take an hour and crash your notebook!"

Run this code together:

```python
PLACE = "Carlton, Victoria, Australia"  # Change to local suburb
G = ox.graph_from_place(PLACE, network_type="walk")
```

**While downloading (10-30 seconds):**

Explain what's happening:

1. "OSMnx is sending a request to OpenStreetMap's servers via the internet"
2. "OpenStreetMap is a crowdsourced map—volunteers worldwide add roads, paths, buildings"
3. "The Overpass API processes the request and returns all streets in Carlton"
4. "OSMnx converts this to a NetworkX graph object with nodes and edges"

**Show on screen:** OpenStreetMap website (https://www.openstreetmap.org), zoom to Carlton, point out footpaths, street names

**When download completes:**

```python
print(f"Nodes (intersections): {len(G.nodes)}")
print(f"Edges (street segments): {len(G.edges)}")
```

Typical suburb results: 300-800 nodes, 500-1200 edges

**0:30-0:40 | Explore the Graph Object**

Run:

```python
nodes, edges = ox.graph_to_gdfs(G)
nodes.head()
edges.head()
```

Point out columns:

- **Nodes:** `lat`, `lon`, `x`, `y`, `osmid` (OpenStreetMap ID)
- **Edges:** `length` (meters), `highway` (road type like "residential", "footway"), `name` (street name)

Ask: "What do you notice about the `highway` column? What types of streets are included?"

**0:40-0:50 | Visualize the Network**

```python
fig, ax = ox.plot_graph(G, figsize=(10, 10), node_size=0, edge_linewidth=0.3)
```

Discussion prompts:

- "Can you identify major streets vs side streets by density?"
- "Do you see any missing roads? Why might that happen?" (OSM data quality varies—some areas better mapped than others)
- "How would this network look different if we used `network_type='drive'` instead of 'walk'?" (no footpaths, fewer connections)

**Compare network types:** Show students the difference (prepare 3 versions ahead of time):

| Network Type | Includes | Use Case |
|--------------|----------|----------|
| `walk` | Footpaths, streets, trails | Pedestrian accessibility |
| `bike` | Bike paths, roads | Cycling infrastructure analysis |
| `drive` | Roads only (no footpaths) | Car-based accessibility |

---

### Part 3: Network Analysis Basics (25 minutes)

**0:50-1:00 | Shortest Path Calculation**

Pick two recognizable locations in your suburb (e.g., train station to library).

Explain: "We'll use Dijkstra's algorithm—the foundation of all network routing—to find the shortest walking path."

```python
# Find nearest nodes to two locations
origin_node = ox.distance.nearest_nodes(G, lon1, lat1)
dest_node = ox.distance.nearest_nodes(G, lon2, lat2)

# Calculate shortest path
route = nx.shortest_path(G, origin_node, dest_node, weight="length")
route_length = sum(ox.utils_graph.get_route_edge_attributes(G, route, "length"))
print(f"Route length: {route_length:.0f} meters")
```

Visualize:

```python
fig, ax = ox.plot_graph_route(G, route, route_linewidth=6, node_size=0, bgcolor='white')
```

**Discussion:**

- "How does this compare to a straight-line distance?" (usually 20-50% longer due to street layout)
- "What does this tell you about buffer analysis limitations?" (buffers assume as-the-crow-flies; networks account for street layout)

**1:00-1:15 | Load Facility Locations**

Students load their own facilities or use the sample (Royal Melbourne Hospital).

```python
facilities = gpd.read_file("../data/processed/week10/facilities.geojson").to_crs(4326)
```

**Emphasize CRS:** "Why EPSG:4326 (WGS84)? OSMnx expects lat/lon coordinates. If your facilities are in a projected CRS (like EPSG:28355), you'll get weird errors when finding nearest nodes."

Plot facilities on network:

```python
fig, ax = ox.plot_graph(G, node_size=0, edge_linewidth=0.3)
facilities.plot(ax=ax, color="red", markersize=100, zorder=5)
```

**Check understanding:** "Everyone see their facility points on the map? If not, check your CRS."

---

### Part 4: Isochrone Calculation (35 minutes)

**1:15-1:25 | Conceptual Introduction to Isochrones**

Draw on whiteboard:

1. Start at a point (hospital)
2. Walk along streets for 10 minutes at 4.8 km/h
3. Mark all intersections you can reach
4. Draw a boundary around those intersections
5. That's your 10-minute isochrone!

**Key parameters:**

- **Walking speed:** 4.8 km/h (average adult)
- **Distance in 10 minutes:** 4.8 km/h × 10 min / 60 = 0.8 km = 800 meters
- **Calculation:** For each time threshold, find all nodes ≤ (time × speed) meters from origin

**Compare to buffers:** "A 800m buffer is a circle. An isochrone follows actual streets—it's irregular, accounting for dead-ends, rivers, highways you can't cross."

**1:25-1:40 | Live Demo: Calculate Isochrones**

Walk through the code cell-by-cell:

```python
WALK_SPEED = 4.8  # km/h
METERS_PER_MIN = WALK_SPEED * 1000 / 60  # 80 m/min
TIMES = [5, 10, 15]  # minutes

isochrones = []

for _, fac in facilities.iterrows():
    node = ox.distance.nearest_nodes(G, fac.geometry.x, fac.geometry.y)

    for mins in TIMES:
        dist = mins * METERS_PER_MIN
        subgraph = nx.ego_graph(G, node, radius=dist, distance="length")
        nodes_gdf = ox.graph_to_gdfs(subgraph, edges=False)
        hull = nodes_gdf.unary_union.convex_hull

        isochrones.append({
            "facility": fac.get("name", "Unknown"),
            "minutes": mins,
            "geometry": hull
        })

iso_gdf = gpd.GeoDataFrame(isochrones, crs=G.graph["crs"])
```

**Explain each step:**

1. **`nearest_nodes()`** - Snaps facility to closest intersection (can't start mid-street)
2. **`mins * METERS_PER_MIN`** - Converts time to distance threshold
3. **`nx.ego_graph()`** - Extracts all nodes within distance along network edges
4. **`convex_hull`** - Draws boundary polygon around reachable nodes
5. **Appends to list** - Builds dataset of all isochrones for all facilities

**Common question:** "Why convex hull instead of exact polygon?" (Simplification—exact boundaries are jagged and slow to compute. Convex hull is good enough for most analyses.)

**1:40-1:50 | Visualize Isochrones**

```python
fig, ax = plt.subplots(figsize=(10, 10))

colors = {5: "green", 10: "yellow", 15: "orange"}

for mins in reversed(TIMES):
    iso_gdf[iso_gdf["minutes"] == mins].plot(
        ax=ax, color=colors[mins], alpha=0.4,
        edgecolor="black", label=f"{mins} min"
    )

facilities.plot(ax=ax, color="red", markersize=100, zorder=5)
ax.legend()
ax.set_title("Walking Time Isochrones")
ax.set_axis_off()
```

**Interpretation prompts:**

- "Which direction has the best accessibility from the facility? Why?" (look for street density, barriers)
- "Where do you see gaps? What might cause them?" (rivers, highways, parks, dead-end streets)
- "How does this compare to the QGIS isochrones from Week 6?" (same concept, automated workflow)

---

### Part 5: Guided Practice & Discussion (30 minutes)

**1:50-2:10 | Students Work Independently**

Students now work through the notebook on their own or in pairs:

1. Change `PLACE` to a suburb of their choice (remind: SUBURB, not city!)
2. Upload their own facilities file OR use the sample
3. Run all cells
4. Generate isochrone map

**Circulate and help with:**

- Download timing issues (emphasize small areas)
- CRS mismatches (facilities not appearing)
- Interpretation questions ("What does this mean for my area?")

**2:10-2:20 | Group Discussion: Equity & Policy Implications**

Bring class back together. Ask:

- "What did your analysis reveal about accessibility in your study area?"
- "Who benefits from good accessibility? Who is left out?"
- "If you could place one new facility, where would it go based on these isochrones?"

**Introduce equity lens:**

- "How might we overlay this with socio-economic data?" (Week 3 SEIFA data)
- "Would vulnerable populations have worse access?" (often yes—car dependency, transit deserts)
- "What's the 15-minute city concept?" (all essential services within 15-min walk/bike—see Paris, Melbourne plans)

**Connect to real-world applications:**

- Urban planning: siting new hospitals, schools, parks
- Emergency services: fire station coverage analysis
- Public health: food deserts (grocery store accessibility)
- Climate action: reducing car dependency through walkable neighborhoods

**2:20-2:30 | Wrap-up & Reflection Prompts**

Preview the written reflection questions (from student content):

- How did network-based isochrones differ from simple buffers? When does the difference matter most?
- How does this Python workflow compare to QGIS QNEAT3? Advantages of scripting vs visual interface?
- What additional data would strengthen your analysis? (transit schedules, elevation, facility capacity)
- How might policymakers use this? What are the risks of oversimplifying accessibility?

**Submission checklist:**

- Completed notebook with all cells run
- Exported isochrones GeoPackage
- Optional: Coverage analysis if they completed Activity 4-5
- 2-3 paragraph summary interpreting findings
- Reflection entry

**Preview Week 11:** "Next week is the Design Studio—bring all your best maps from Weeks 1-10. You'll craft them into polished, narrative-driven layouts for your capstone."

---

## Key Concepts to Emphasize

### 1. Network Graphs vs. Euclidean Buffers

**Critical distinction:**

- **Buffer (Week 2):** Circular zone based on straight-line distance. Fast to compute, but unrealistic.
- **Isochrone (Week 10):** Network-based zone following actual streets. Slower to compute, but accurate.

**When does it matter?**

- Dense urban grids: Minimal difference (streets form regular patterns)
- River cities, hilly terrain, highways: MAJOR difference (barriers create accessibility gaps)

**Example:** A hospital 500m away as the crow flies might be 1.2 km via streets if you have to cross a river at a bridge.

### 2. Graph Theory Fundamentals

Students may struggle with abstract graph concepts. Use concrete analogies:

- **Node** = Intersection, junction, place where paths meet
- **Edge** = Street segment, path, connection between nodes
- **Weight** = Attribute of edge (length in meters, travel time, elevation gain)
- **Path** = Sequence of edges from origin to destination
- **Shortest path** = Path with minimum total weight (Dijkstra's algorithm finds this)

**Analogy:** "Think of a metro map. Stations are nodes. Train lines between stations are edges. Travel time is the weight."

### 3. Walking Speed Assumptions

Default: **4.8 km/h** (80 meters/minute)

**Why this matters:**

- Average adult pace
- Slower for elderly, children, people with disabilities (3-4 km/h more realistic)
- Faster for fit young adults (5-6 km/h)
- Does NOT account for: hills, stoplights, weather, perceived safety

**Critical thinking:** "If we're analyzing accessibility for seniors, should we use 4.8 km/h?" (No—use 3.5-4 km/h for conservative estimate)

**Equity implication:** Accessibility is not universal—it depends on who's walking and under what conditions.

### 4. OpenStreetMap Data Source

**Strengths:**

- Free, open, global coverage
- Constantly updated by volunteers
- Includes footpaths, bike paths (not just roads)
- Rich attributes (street names, types, speed limits)

**Limitations:**

- Data quality varies by region (rich countries > developing countries; cities > rural)
- Volunteers may miss new construction or changes
- Not authoritative (government datasets may be more accurate but less accessible)
- Rural/remote areas often incomplete

**Teaching moment:** "Always validate OSM data against local knowledge. If a path looks suspicious, check on the ground or with official maps."

### 5. Reproducibility & Automation

**Why Python > QGIS for this task?**

| QGIS (Week 6) | Python (Week 10) |
|---------------|------------------|
| Visual, intuitive | Requires coding knowledge |
| Manual steps (click, export, repeat) | Automated (script runs 100 facilities instantly) |
| Hard to share exact process | Notebook = complete documentation |
| Good for exploration | Good for production analysis |

**Best practice:** Use QGIS for exploring, use Python for repeatable/large-scale analysis.

**Example:** "If a city planner asks you to analyze accessibility for 50 hospitals across 10 cities, would you rather click through QGIS 500 times or run one Python script?"

---

## Live Demo Script

### Demo 1: Downloading a Network (10 minutes)

**Setup:**

Open a fresh Jupyter notebook or Colab session. Share your screen.

**Script:**

"We're going to download the street network for Carlton, a suburb of Melbourne. This is a SMALL area—about 2 square kilometers. Never start with a whole city!"

Run:

```python
import osmnx as ox
PLACE = "Carlton, Victoria, Australia"
print(f"Downloading network for: {PLACE}")
G = ox.graph_from_place(PLACE, network_type="walk")
print(f"Nodes: {len(G.nodes)}, Edges: {len(G.edges)}")
```

**While running (talk through the wait):**

"Right now, OSMnx is:

1. Sending a request to OpenStreetMap's Overpass API
2. The API is searching its database for all streets in Carlton
3. It's packaging up the nodes (intersections) and edges (street segments)
4. OSMnx receives the data and builds a NetworkX graph object

This takes 10-30 seconds for a suburb. For a whole city, it could take 5-15 minutes. For a state? Don't try it—you'll crash your notebook!"

**When complete:**

"We now have 600 nodes and 900 edges. Each node has lat/lon coordinates. Each edge has a length in meters. Let's visualize it."

Run:

```python
fig, ax = ox.plot_graph(G, node_size=0, edge_linewidth=0.3)
```

**Point out:**

"See the dense grid? That's Carlton's Victorian-era street layout—very walkable. See the gaps? That's Carlton Gardens park—no through-streets. This is real data from OpenStreetMap volunteers."

### Demo 2: Explaining Network Structure (5 minutes)

**Convert to GeoDataFrame:**

```python
nodes, edges = ox.graph_to_gdfs(G)
print("NODES:")
print(nodes[['y', 'x', 'street_count']].head())
print("\nEDGES:")
print(edges[['name', 'length', 'highway']].head())
```

**Script:**

"The nodes table has 600 rows—one per intersection. Columns include:

- `y`, `x`: Latitude and longitude
- `street_count`: How many streets meet here (3-way, 4-way intersections)

The edges table has 900 rows—one per street segment. Columns include:

- `name`: Street name like 'Lygon Street' (some are None for unnamed paths)
- `length`: Distance in meters
- `highway`: Type like 'residential', 'footway', 'primary' (tells you if it's a main road or side street)

This is the raw data that powers our analysis."

### Demo 3: Creating Isochrones (10 minutes)

**Setup:**

Use a single facility (e.g., Royal Melbourne Hospital at 144.9556, -37.7990).

**Script:**

"We're going to calculate how far someone can walk from Royal Melbourne Hospital in 5, 10, and 15 minutes. The average person walks 4.8 km/h, which is 80 meters per minute."

Run:

```python
from shapely.geometry import Point
import geopandas as gpd
import networkx as nx

facility = Point(144.9556, -37.7990)
node = ox.distance.nearest_nodes(G, facility.x, facility.y)

WALK_SPEED = 4.8  # km/h
METERS_PER_MIN = 80
TIMES = [5, 10, 15]

isochrones = []

for mins in TIMES:
    dist = mins * METERS_PER_MIN
    subgraph = nx.ego_graph(G, node, radius=dist, distance="length")
    nodes_gdf = ox.graph_to_gdfs(subgraph, edges=False)
    hull = nodes_gdf.unary_union.convex_hull
    isochrones.append({"minutes": mins, "geometry": hull})

iso_gdf = gpd.GeoDataFrame(isochrones, crs=G.graph["crs"])
```

**Explain while running:**

"For the 5-minute walk:

- 5 minutes × 80 m/min = 400 meters
- We find all network nodes within 400m of the hospital (via streets, not straight-line)
- We draw a boundary around those nodes
- That's our 5-minute isochrone

We repeat for 10 minutes (800m) and 15 minutes (1200m)."

**Visualize:**

```python
fig, ax = plt.subplots(figsize=(10, 10))
iso_gdf[iso_gdf["minutes"] == 15].plot(ax=ax, color="orange", alpha=0.4, label="15 min")
iso_gdf[iso_gdf["minutes"] == 10].plot(ax=ax, color="yellow", alpha=0.4, label="10 min")
iso_gdf[iso_gdf["minutes"] == 5].plot(ax=ax, color="green", alpha=0.4, label="5 min")
gpd.GeoDataFrame([{"geometry": facility}], crs=4326).plot(ax=ax, color="red", markersize=100)
ax.legend()
ax.set_title("Walking Time from Royal Melbourne Hospital")
ax.set_axis_off()
```

**Interpretation:**

"Notice how the isochrones are NOT perfect circles. They follow the street grid. See how they extend further north-south than east-west? That's because Lygon Street is a major through-road running north-south, while east-west streets are more fragmented.

This is why network analysis beats simple buffers—it captures real-world street layout."

---

## Discussion Prompts

### 1. Accessibility Equity

**Prompt:** "Imagine two neighborhoods: one with dense street grids and one with cul-de-sac suburbs. If both have a hospital 1 km away, who has better walking accessibility?"

**Expected answers:**

- Dense grid: More direct routes, better accessibility
- Cul-de-sacs: Winding paths, worse accessibility even at same distance

**Follow-up:** "What does this mean for urban planning? Should new developments require connected street networks?"

### 2. The 15-Minute City Concept

**Prompt:** "Paris and Melbourne are implementing '15-minute city' plans—every resident should reach daily needs (grocery, school, park, pharmacy) within 15 minutes by foot or bike. How would you use this analysis to audit your city's progress?"

**Expected workflow:**

1. Map all essential facilities (groceries, schools, parks, etc.)
2. Create 15-minute walking/biking isochrones from each
3. Overlay with population data
4. Identify gaps: areas with <15-min access
5. Prioritize new facility locations or transit improvements

**Follow-up:** "What challenges might arise? What if 15 minutes is achievable but the route feels unsafe (highway underpass, poorly lit)? How do you measure perceived safety?"

### 3. Transport Mode Comparison

**Prompt:** "How would your analysis change if we compared walking vs driving accessibility? Who benefits from each mode?"

**Expected answers:**

- **Walking:** Benefits dense urban residents, excludes car-dependent suburbs
- **Driving:** Benefits suburban/rural residents, excludes non-drivers (elderly, low-income, children)

**Equity dimension:** "Who doesn't have a car in your city? How does car-centric planning affect them?"

**Extension:** "What about public transit? How would you incorporate bus schedules into this analysis?" (Advanced—requires GTFS data and time-aware routing)

### 4. Data Limitations & Assumptions

**Prompt:** "We assumed everyone walks at 4.8 km/h. Who does this assumption exclude or misrepresent?"

**Expected answers:**

- Elderly, people with disabilities (walk slower)
- Parents with strollers (walk slower, need ramps)
- Children (walk slower, may not travel alone)

**Follow-up:** "How could we make this analysis more inclusive?" (Use slower speeds like 3.5 km/h, account for elevation, model different populations separately)

**Critical thinking:** "Are we measuring true accessibility or just physical proximity? What else matters?" (Safety, lighting, weather, sidewalk quality, cultural factors)

### 5. Policy Implications & Risks

**Prompt:** "A city council sees your analysis showing a neighborhood has poor hospital accessibility. They propose building a new hospital. What questions should you ask before supporting this?"

**Expected considerations:**

- Is a new hospital the only solution? (Could improve transit routes, ambulance service)
- What's the cost-benefit? (Hospitals are expensive; might be cheaper to subsidize transport)
- Who lives in the underserved area? (If low-income, can they afford hospital care anyway?)
- Are there other barriers? (Insurance, language, cultural competency of staff)

**Teaching moment:** "Spatial analysis shows WHERE gaps exist, but not WHY they exist or HOW to fix them. Always combine GIS with qualitative research, community input, and policy expertise."

### 6. Comparison to QGIS Workflows

**Prompt:** "You've done isochrone analysis in QGIS (Week 6) and now in Python. When would you use each?"

**Create a table together:**

| Scenario | Best Tool | Why |
|----------|-----------|-----|
| Exploring a new dataset | QGIS | Visual, fast iteration |
| One-off map for a report | QGIS | Easier styling, layout tools |
| Analyzing 50 facilities | Python | Automation, scripting |
| Sharing analysis with a colleague | Python | Notebook = reproducible documentation |
| Presenting to a non-technical audience | QGIS | Prettier maps, less intimidating |
| Publishing in an academic journal | Python | Transparency, reproducibility required |

**Key insight:** "Use QGIS for exploration and communication. Use Python for production and reproducibility."

---

## Common Student Issues

### Issue 1: Slow Downloads / API Timeouts

**Symptom:** Student runs `ox.graph_from_place("Melbourne, Australia")` and waits 10+ minutes, or gets an error:

```
TimeoutError: Server did not respond within timeout
```

**Cause:** Downloaded area is too large (whole city or state).

**Solution:**

1. Emphasize in introduction: "Start with a SUBURB, not a city!"
2. Show size comparison on a map: Carlton (~2 km²) vs Melbourne (~10,000 km²)
3. If timeout occurs, suggest:
   - Smaller place name: "Carlton, Melbourne" instead of "Melbourne"
   - Bounding box: `ox.graph_from_bbox(north, south, east, west, network_type="walk")`
   - Increase timeout: `ox.settings.timeout = 300` (default is 180 seconds)

**Backup plan:** Provide pre-downloaded `.graphml` files for common suburbs. Students load with:

```python
G = ox.load_graphml("carlton_network.graphml")
```

### Issue 2: Network Topology Errors

**Symptom:** Error when calculating isochrones:

```
NetworkXError: Node X not in graph
```

**Cause:** The graph has disconnected components (e.g., isolated street segments not connected to main network).

**Solution:**

1. Extract the largest connected component:

```python
G = ox.utils_graph.get_largest_component(G, strongly=False)
```

2. Explain: "Some networks have isolated segments (islands, gated communities). We remove them to ensure every node is reachable."

### Issue 3: Facilities Not Appearing on Map

**Symptom:** Student runs plot but doesn't see their facility points.

**Cause:** CRS mismatch—facilities in projected CRS (e.g., EPSG:28355), graph in WGS84 (EPSG:4326).

**Solution:**

```python
facilities = facilities.to_crs(4326)  # Always convert to WGS84 for OSMnx
```

**Check:** "What CRS is your facilities file in? Check with `facilities.crs`."

### Issue 4: Understanding Graph Concepts

**Symptom:** "What's a node? What's an edge? I don't get it."

**Cause:** Graph theory is abstract for beginners.

**Solution:**

- Draw on whiteboard: simple network with 4 intersections, 5 streets
- Use physical analogy: "Imagine you're a GPS. You store intersections (nodes) and roads (edges) to calculate routes."
- Show `nodes.head()` and `edges.head()` tables—make it concrete

**Activity:** Print a simple network diagram, have students trace shortest path by hand before coding.

### Issue 5: Convex Hull vs. Exact Boundary

**Symptom:** "Why is my isochrone shape so smooth? Shouldn't it be jagged following exact streets?"

**Cause:** We use `convex_hull` for simplicity, not exact boundary.

**Explanation:** "The exact boundary is computationally expensive and jagged. Convex hull is good enough for most analyses—it shows the general reachable area."

**Advanced students:** Show how to use `concave_hull` or `alpha_shape` for more precise boundaries (requires `shapely` 2.0+ or `alphashape` package).

### Issue 6: Python Syntax Errors

**Symptom:** Student gets `SyntaxError` or `IndentationError`.

**Common mistakes:**

- Missing colon after `for` loop: `for _, fac in facilities.iterrows()` (forgot `:`)
- Wrong indentation (mixing tabs and spaces)
- Misspelled variable names: `isocrhones` instead of `isochrones`

**Solution:**

- Walk through slowly, emphasize syntax rules
- Show error message: "Read from bottom up—last line tells you what's wrong"
- Use Colab's autocomplete (Tab key)

### Issue 7: No Internet Connection

**Symptom:** `ox.graph_from_place()` fails immediately.

**Cause:** No internet or OpenStreetMap Overpass API is down.

**Check API status:** https://overpass-api.de/api/status

**Solution:** See Backup Plan below.

---

## Backup Plan (If OSM is Slow/Down)

### Scenario 1: OpenStreetMap Overpass API is Down

**Check:** Visit https://overpass-api.de/api/status. If it says "Service Unavailable" or "Too Many Requests," the API is overloaded.

**Backup Plan A: Use Pre-Downloaded Networks**

1. Before class, download 3-4 common suburbs/cities:

```python
G = ox.graph_from_place("Carlton, Melbourne", network_type="walk")
ox.save_graphml(G, "carlton_walk.graphml")
```

2. Share these `.graphml` files with students via cloud storage or USB
3. Students load instead of downloading:

```python
G = ox.load_graphml("carlton_walk.graphml")
```

**Backup Plan B: Manual Network Drawing Exercise**

If no networks are available:

1. Print a simple street map (5-10 intersections)
2. Students manually:
   - Label nodes (intersections A, B, C...)
   - Measure edge lengths with ruler
   - Calculate shortest path by hand
   - Draw 5-minute walking isochrone (400m radius along streets)

**Learning outcome:** Reinforces graph concepts without technology.

### Scenario 2: Downloads Are Extremely Slow (5+ minutes)

**Cause:** Overpass API is under load or student chose too large an area.

**Solutions:**

1. **Use cache:** If you downloaded a network earlier, OSMnx caches it. Delete and re-run:

```python
ox.settings.use_cache = True  # Enable cache
G = ox.graph_from_place("Carlton, Melbourne", network_type="walk")  # Loads from cache if exists
```

2. **Use a different OSM server:** Change the Overpass API endpoint:

```python
ox.settings.overpass_endpoint = "https://overpass.kumi.systems/api/interpreter"  # Alternative server
```

3. **Simplify the network:** Download "drive" network (fewer edges) instead of "walk":

```python
G = ox.graph_from_place("Carlton, Melbourne", network_type="drive")
```

### Scenario 3: No Internet at All

**Full offline session:**

1. Lecture on graph theory with whiteboard examples
2. Show pre-recorded video of OSMnx download (prepare ahead)
3. Students work with static maps and hand calculations
4. Homework: Complete notebook at home with internet

**Alternative activity:** Analyze a pre-generated isochrone shapefile in QGIS (review Week 6 skills).

---

## Wrap-up & Preview

### Session Wrap-up (5 minutes)

**Summarize key takeaways:**

1. "Network analysis is more accurate than buffers because it accounts for real street layout"
2. "OSMnx automates what you did manually in QGIS—reproducible and scalable"
3. "Accessibility is not just about distance—speed, mode, barriers, and user characteristics all matter"
4. "Always start with small study areas and scale up to avoid long download times"

**Check understanding:**

"Raise your hand if you can:

- Download a street network with OSMnx?" (hands up)
- Calculate walking time isochrones?" (hands up)
- Explain the difference between a node and an edge?" (hands up)

**Homework reminders:**

- Complete the notebook with your own study area
- Export isochrones as GeoPackage
- Write 2-3 paragraph summary interpreting findings
- Complete reflection prompts

**Due date:** [Insert your deadline]

### Preview Week 11: Design & Storytelling Studio

**Script:**

"Next week is special—no new technical skills. Instead, you'll bring ALL your favorite maps from Weeks 1-10 and turn them into polished, professional layouts.

Think of it as a portfolio curation session. You'll:

- Design multi-panel layouts combining maps, charts, and text
- Practice peer critique (giving and receiving feedback)
- Run accessibility audits (can colorblind people read my map?)
- Prepare materials for your final capstone presentation

**Action item:** This week, review your past work and identify 3-5 maps you're proud of. We'll polish them into portfolio-quality pieces.

**Example:** Maybe you combine:

- Week 3: SEIFA socio-economic map
- Week 6: QGIS network analysis
- Week 10: Python isochrones (today!)
- Week 8: Raster population density

...into a single narrative layout showing "Accessibility Equity in Melbourne."

Start thinking about your story!"

---

## Additional Facilitator Tips

### Time Management

**If running behind:**

- Skip Activity 2 (shortest path calculation)—it's conceptual, not critical for isochrones
- Pre-load facilities dataset (don't wait for students to upload)
- Use pre-downloaded network for demo instead of live download

**If running ahead:**

- Introduce Activity 4-5 (equity analysis with SEIFA data)
- Show advanced techniques: comparing network types (`walk` vs `drive` vs `bike`)
- Discuss elevation-aware routing (requires DEM data—preview for advanced students)

### Adapting for Different Skill Levels

**Beginner students (struggling with Python):**

- Provide more detailed comments in code cells
- Walk through line-by-line instead of cell-by-cell
- Pair strong coders with beginners for peer support

**Advanced students (finishing early):**

- Challenge: Analyze 5+ facilities instead of 1-2
- Challenge: Compare `walk` vs `bike` vs `drive` network types
- Challenge: Calculate population coverage (Activity 4) using Week 3 data
- Extension: Install `alphashape` and compute exact isochrone boundaries instead of convex hull

### Inclusive Teaching

**Accessibility considerations:**

- Ensure colorblind-friendly palettes (green/yellow/orange may be hard to distinguish—use ColorBrewer)
- Provide high-contrast visuals for low vision students
- Describe maps verbally: "The 5-minute zone extends 400m in all directions, but stops at the river to the east"

**Language support:**

- Define technical terms before using: "isochrone," "node," "edge," "graph"
- Provide glossary handout
- Encourage questions—graph theory is abstract!

**Different learning styles:**

- Visual learners: Emphasize maps and diagrams
- Kinesthetic learners: Have them trace routes on printed maps
- Auditory learners: Talk through concepts verbally before coding

### Building Connections Across Weeks

Link to prior knowledge:

| Week | Connection | How to Reference |
|------|------------|------------------|
| Week 2 | Buffers | "We used circular buffers—isochrones are network-aware versions" |
| Week 3 | Census data | "Overlay isochrones with SEIFA data to find equity gaps" |
| Week 6 | QGIS QNEAT3 | "You've done this manually—today we automate it" |
| Week 8 | Raster analysis | "Could combine with elevation rasters to model uphill walking speed" |
| Week 9 | Python intro | "Building on loops, GeoDataFrames, and plotting skills" |

### Real-World Context

Share case studies or news articles:

- **Paris 15-minute city plan:** https://www.paris.fr/pages/paris-ville-du-quart-d-heure-197
- **Melbourne 20-minute neighborhoods:** https://www.planning.vic.gov.au/policy-and-strategy/planning-for-melbourne/plan-melbourne/20-minute-neighbourhoods
- **Food deserts in the US:** USDA food access research atlas
- **Healthcare accessibility in rural Australia:** AIHW reports on GP shortages

**Discussion:** "How could our analysis inform these policies?"

### Student Motivation

**Why this matters:**

- Directly applicable to urban planning, public health, emergency services
- Builds portfolio piece for job applications
- Demonstrates Python/GIS skills employers value
- Addresses real equity issues in their own cities

**Career paths using these skills:**

- Transport planner
- Public health analyst
- Emergency services coordinator
- Accessibility consultant
- Smart cities data scientist

---

## FAQs from Students

**Q: Why does OSMnx sometimes download slightly different networks when I run the same code twice?**

A: OpenStreetMap is constantly updated. If a volunteer edits streets between your two downloads, you'll get different data. Use `ox.settings.use_cache = True` to load from cache for consistency.

**Q: Can I use this for public transit analysis?**

A: Not directly. This models walking/cycling/driving on streets. For transit, you need GTFS (General Transit Feed Specification) data and time-aware routing. See `r5py` package for transit analysis.

**Q: What if my city isn't well-mapped on OpenStreetMap?**

A: You have three options:

1. Contribute to OSM yourself (add missing streets)
2. Use official government road datasets (may require conversion to graph format)
3. Choose a different study area with better coverage

**Q: How do I account for hills or stairs?**

A: You'd need elevation data (DEM raster). Advanced workflow:

1. Download DEM for your area
2. Calculate slope for each street segment
3. Adjust walking speed based on slope (slower uphill, faster downhill)
4. Use adjusted speeds in isochrone calculation

This is beyond the scope of Week 10 but possible for capstone projects.

**Q: Can I use driving isochrones to model car accessibility?**

A: Yes, change `network_type="drive"` and adjust speed:

```python
DRIVE_SPEED = 40  # km/h (urban driving, accounting for traffic)
METERS_PER_MIN = DRIVE_SPEED * 1000 / 60
```

**Q: Why are my isochrones so much smaller than QGIS QNEAT3 results?**

A: Check your speed assumption. QGIS QNEAT3 defaults to 5 km/h; we use 4.8 km/h. Also check network type—did you use `walk` in Python but `drive` in QGIS?

**Q: How many facilities can I analyze before it gets too slow?**

A: Depends on network size. For a suburb-sized network:

- 1-10 facilities: Fast (<1 minute)
- 10-50 facilities: Medium (1-5 minutes)
- 50+ facilities: Slow (5-30 minutes)

Use the `cutoff` parameter to speed up:

```python
lengths = nx.single_source_dijkstra_path_length(G, node, cutoff=1500, weight="length")
```

---

## Reflection on Pedagogical Goals

This week marks a transition from "learning tools" to "applying tools for insight." By Week 10, students should:

- **Recognize patterns:** "Accessibility gaps correlate with low socio-economic status"
- **Ask critical questions:** "Who defined the 4.8 km/h walking speed? Who does that exclude?"
- **Propose solutions:** "We could improve accessibility by adding a bus route here"
- **Communicate findings:** "This neighborhood is underserved—here's the evidence"

**Encourage:**

- Questioning assumptions (speed, network type, data quality)
- Connecting to equity/justice frameworks
- Thinking beyond technical execution to policy impact

**Discourage:**

- Treating analysis as value-neutral ("the data says...")
- Over-simplifying complex social issues ("just build more hospitals")
- Ignoring data limitations ("OSM is perfect")

**Growth mindset:** "This analysis is a starting point for conversation, not a final answer."

---

## Post-Session Checklist

After class:

- [ ] Review student submissions—identify common errors for next year's prep
- [ ] Note which discussion prompts generated best engagement
- [ ] Check if download times matched expectations (adjust suburb recommendations)
- [ ] Gather feedback: "What was most confusing? What clicked?"
- [ ] Update facilitator notes with new insights

**For next time:**

- [ ] Pre-download 5 backup networks for common cities/suburbs
- [ ] Prepare printed network diagrams for manual shortest-path exercise
- [ ] Create video tutorial for OSMnx installation (for students setting up locally)
- [ ] Curate 2-3 news articles on 15-minute cities or accessibility equity

---

**End of Week 10 Facilitator Notes**

Remember: The goal is not perfect technical execution—it's building critical spatial thinkers who can use GIS to address real-world problems. Encourage exploration, celebrate mistakes as learning opportunities, and always connect code to context.
