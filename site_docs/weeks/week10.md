# Week 10 · Transport Networks & Accessibility

How far can someone walk to a grocery store in 10 minutes? Which neighborhoods have good bike access to parks? Who lives more than 30 minutes from a hospital? These questions matter for equity, health, and quality of life—and they require network analysis to answer properly. This week, you'll move beyond straight-line buffers to analyze real street networks using Python, calculating travel-time isochrones and identifying accessibility gaps. You'll automate workflows you learned in QGIS Week 6, making them reproducible and scalable for larger studies or policy analysis.

## What you'll learn

By the end of this week, you'll be able to:

1. Download and configure street network graphs using OSMnx from OpenStreetMap.
2. Calculate travel-time isochrones (service areas) for walking, cycling, or driving using network analysis algorithms.
3. Overlay isochrones with population or vulnerability data to identify underserved communities.
4. Compare Python network analysis to QGIS QNEAT3 workflows—understanding when automation adds value.

## Before you start

### 1. Get the notebook

📓 **Download the Week 10 notebook:** [week10_transport_networks.ipynb](../../resources/notebooks/week10_transport_networks.ipynb)

**Where to save it:** Save to your `intro-gis/notebooks/` folder

### 2. Confirm your environment works

- [ ] Activate your conda environment: `conda activate intro-gis`
- [ ] Check OSMnx imports: `python -c "import osmnx; print('✅ Ready!')"`
- [ ] If you see errors, OSMnx should have been installed in Week 7. Try: `conda install -c conda-forge osmnx`

### 3. Prepare your datasets

- [ ] Follow the [Downloading datasets](../onboarding/data-downloads.md) guide for Week 10
- [ ] You need: Facility points (hospitals, schools, parks, etc.)
- [ ] Save to `intro-gis/data/processed/week10/`
  - `facilities.geojson`
- [ ] Optional: Population data for accessibility analysis
  - `population.geojson`

**Note:** Street network data is downloaded automatically by OSMnx—you don't need to download it separately!

### 4. Choose your study area

- [ ] Pick a city or region to analyze (smaller areas process faster for testing)
- [ ] You'll specify the place name in the notebook (e.g., "Cambridge, Massachusetts, USA")

### 5. Review the lecture

- [ ] Read: [Week 10 · Network Theory for Mobility](../lectures/week10-network-theory.md)

!!! tip "OSMnx downloads data on the fly"
    Unlike other weeks, you don't need to download street network data manually. OSMnx fetches it from OpenStreetMap automatically when you run the notebook. Make sure you have a good internet connection!

## This week's activities

### Activity 1: Download a street network with OSMnx

You'll use OSMnx to download OpenStreetMap road networks directly into Python as a network graph.

**Steps:**

1. Open the Week 10 Jupyter notebook: `resources/notebooks/week10_transport_networks.ipynb`
2. Run the imports and configuration cell:
   ```python
   import osmnx as ox
   import networkx as nx
   import geopandas as gpd

   ox.settings.log_console = True
   ox.settings.use_cache = True
   ```
3. Download a network for your study area using a place name query:
   ```python
   PLACE = "Cambridge, Massachusetts, USA"  # Change to your area
   G = ox.graph_from_place(PLACE, network_type="walk")
   ```
4. Explore the network graph:
   - Print graph statistics: `print(nx.info(G))`
   - Check number of nodes (intersections): `len(G.nodes())`
   - Check number of edges (street segments): `len(G.edges())`
5. Convert the graph to GeoDataFrames for spatial analysis:
   ```python
   nodes, edges = ox.graph_to_gdfs(G)
   nodes.head()  # Inspect node attributes
   edges.head()  # Inspect edge attributes (length, highway type, etc.)
   ```

**What's happening?** OSMnx queries the OpenStreetMap Overpass API, downloads all roads/paths in your area, and builds a mathematical graph where intersections are "nodes" and street segments are "edges" with properties like length and speed limit.

!!! note "Network types"
    `network_type="walk"` includes footpaths and pedestrian infrastructure. Use `"bike"` for cycling networks or `"drive"` for car-accessible roads only. Choose based on your accessibility question.

**Troubleshooting:** If the API times out or returns an error, try:
- A smaller study area (one neighborhood instead of a whole city)
- Using a bounding box instead: `ox.graph_from_bbox(north, south, east, west, network_type="walk")`
- Checking OpenStreetMap coverage—some rural areas have incomplete data

### Activity 2: Network analysis basics

Before building isochrones, understand how graph algorithms work by calculating shortest paths and network centrality.

**Steps:**

1. Find the nearest network node to a specific location:
   ```python
   # Your facility coordinates (lat, lon)
   origin_lat, origin_lon = 42.3751, -71.1056  # Example: MIT
   origin_node = ox.distance.nearest_nodes(G, origin_lon, origin_lat)
   print(f"Nearest node ID: {origin_node}")
   ```
2. Calculate shortest path to another location:
   ```python
   dest_lat, dest_lon = 42.3601, -71.0942  # Example: Boston Common
   dest_node = ox.distance.nearest_nodes(G, dest_lon, dest_lat)
   route = nx.shortest_path(G, origin_node, dest_node, weight="length")
   print(f"Route has {len(route)} nodes")
   ```
3. Calculate the route length in meters:
   ```python
   route_length = sum(ox.utils_graph.get_route_edge_attributes(G, route, "length"))
   print(f"Route length: {route_length:.0f} meters")
   ```
4. Visualize the route (optional):
   ```python
   fig, ax = ox.plot_graph_route(G, route, route_linewidth=6,
                                   node_size=0, bgcolor='white')
   ```

**What's happening?** NetworkX uses Dijkstra's algorithm to find the shortest path by summing edge weights (distance in meters). This is the foundation of all network accessibility analysis.

!!! tip "Compare to QGIS"
    This is what QNEAT3 does behind the scenes when you calculate "Shortest Path" in QGIS. Python lets you script it, making it reproducible and batchable for hundreds of routes.

### Activity 3: Calculate isochrones (travel-time service areas)

Now you'll calculate how far someone can travel from a facility in a given time—creating isochrones just like Week 6, but scripted and automated.

**Steps:**

1. Load your facility locations:
   ```python
   facilities = gpd.read_file("../data/processed/week10/facilities.geojson")
   facilities = facilities.to_crs(4326)  # Ensure WGS84 for OSMnx
   print(f"Analyzing {len(facilities)} facilities")
   ```
2. Set travel parameters:
   ```python
   TRAVEL_TIMES = [5, 10, 15]  # minutes
   SPEED_KMPH = 4.8  # walking speed (adjust for bike: 15, car: 40)
   METERS_PER_MIN = SPEED_KMPH * 1000 / 60
   ```
3. Loop through each facility and calculate reachable nodes:
   ```python
   isochrones = []

   for idx, facility in facilities.iterrows():
       # Find nearest node
       center_node = ox.distance.nearest_nodes(G,
                                                facility.geometry.x,
                                                facility.geometry.y)

       # Calculate distances to all reachable nodes
       lengths = nx.single_source_dijkstra_path_length(
           G, center_node,
           cutoff=max(TRAVEL_TIMES) * METERS_PER_MIN,
           weight="length"
       )

       # Create isochrone for each time threshold
       for minutes in TRAVEL_TIMES:
           reachable_nodes = [node for node, length in lengths.items()
                               if length <= minutes * METERS_PER_MIN]
           subgraph = G.subgraph(reachable_nodes)
           polygon = ox.utils_graph.graph_area_polygon(subgraph)

           isochrones.append({
               "facility_id": facility.get("name", idx),
               "minutes": minutes,
               "geometry": polygon
           })

   isochrone_gdf = gpd.GeoDataFrame(isochrones, crs=edges.crs)
   ```
4. Inspect the results:
   ```python
   print(isochrone_gdf.head())
   print(f"Created {len(isochrone_gdf)} isochrones")
   ```

**What's happening?** For each facility, the algorithm finds all nodes reachable within the time threshold, extracts that subgraph, and converts it to a polygon boundary representing the service area.

!!! warning "Processing time"
    This can take several minutes for large networks or many facilities. Start with 1-2 facilities to test, then scale up. The `cutoff` parameter prevents checking the entire network unnecessarily.

### Activity 4: Analyze population coverage

Now overlay your isochrones with census data to quantify who has access and who doesn't.

**Steps:**

1. Load population or SA2 boundary data (from Week 3):
   ```python
   population = gpd.read_file("../data/processed/week03/sa2_with_seifa.gpkg")
   population = population.to_crs(isochrone_gdf.crs)
   ```
2. Identify which areas fall inside 15-minute service areas:
   ```python
   # Filter to 15-minute isochrones
   iso_15min = isochrone_gdf[isochrone_gdf["minutes"] == 15]

   # Spatial join: which SA2s intersect service areas?
   coverage = gpd.sjoin(population, iso_15min, how="left", predicate="intersects")

   # Mark covered vs. uncovered
   coverage["is_covered"] = coverage["facility_id"].notna()
   ```
3. Calculate summary statistics:
   ```python
   total_pop = coverage["population"].sum()
   covered_pop = coverage[coverage["is_covered"]]["population"].sum()
   coverage_pct = (covered_pop / total_pop) * 100

   print(f"Total population: {total_pop:,.0f}")
   print(f"Covered population: {covered_pop:,.0f} ({coverage_pct:.1f}%)")
   print(f"Uncovered population: {total_pop - covered_pop:,.0f}")
   ```
4. Export results for visualization in QGIS:
   ```python
   coverage.to_file("../data/processed/week10/outputs/coverage_analysis.gpkg",
                     layer="sa2_coverage", driver="GPKG")
   ```

**Interpret:** Are certain regions systematically underserved? What's the coverage rate?

### Activity 5: Equity analysis with vulnerability data

Go deeper by overlaying accessibility with socio-economic vulnerability to find the most critical gaps.

**Steps:**

1. Filter to high-disadvantage areas (SEIFA decile 1-2):
   ```python
   vulnerable = coverage[coverage["seifa_decile"] <= 2]
   print(f"High-disadvantage areas: {len(vulnerable)}")
   ```
2. Calculate vulnerability-specific coverage:
   ```python
   vuln_total = vulnerable["population"].sum()
   vuln_covered = vulnerable[vulnerable["is_covered"]]["population"].sum()
   vuln_coverage_pct = (vuln_covered / vuln_total) * 100

   print(f"Vulnerable population coverage: {vuln_coverage_pct:.1f}%")
   print(f"Overall population coverage: {coverage_pct:.1f}%")
   print(f"Equity gap: {coverage_pct - vuln_coverage_pct:.1f} percentage points")
   ```
3. Identify the most underserved vulnerable areas:
   ```python
   gaps = vulnerable[~vulnerable["is_covered"]].sort_values("population",
                                                              ascending=False)
   print("Top 5 underserved vulnerable areas:")
   print(gaps[["sa2_name", "population", "seifa_decile"]].head())
   ```
4. Export priority intervention areas:
   ```python
   gaps.to_file("../data/processed/week10/outputs/accessibility_gaps.gpkg",
                 layer="priority_areas", driver="GPKG")
   ```

**Why this matters:** This analysis provides evidence for where to locate new facilities or improve transit routes—prioritizing communities that face compounding barriers.

!!! tip "Compare modes"
    Repeat this analysis with `network_type="bike"` and `network_type="drive"` to see how accessibility varies by transportation mode. Non-drivers often face much larger gaps.

### Activity 6: Visualization and interpretation

Create clear visualizations and document your findings.

**Steps:**

1. Create a comparison plot showing service area sizes:
   ```python
   import matplotlib.pyplot as plt

   fig, ax = plt.subplots(1, 3, figsize=(15, 5))
   for i, minutes in enumerate([5, 10, 15]):
       iso_subset = isochrone_gdf[isochrone_gdf["minutes"] == minutes]
       iso_subset.plot(ax=ax[i], alpha=0.3, edgecolor="black")
       facilities.plot(ax=ax[i], color="red", markersize=50)
       ax[i].set_title(f"{minutes}-minute walk time")
       ax[i].axis("off")
   plt.tight_layout()
   plt.savefig("../data/processed/week10/outputs/isochrone_comparison.png", dpi=300)
   ```
2. Export isochrones for QGIS visualization:
   ```python
   isochrone_gdf.to_file("../data/processed/week10/outputs/isochrones.gpkg",
                          layer="isochrones", driver="GPKG")
   ```
3. Open the GeoPackage in QGIS (Week 11 prep):
   - Style isochrones with graduated colors by time
   - Add basemap and facility points
   - Create a layout for your design studio
4. Document your reflection prompts (see below)

**Compare to QGIS:** You've now automated what took multiple manual steps in QGIS Week 6. The Python workflow is reproducible—you can rerun it for different cities, time periods, or facility types with minimal changes.

## Support materials

- Slides: [Week 10 lecture deck](../../assets/slides/week10.html)
- Lecture notes: [Network Theory for Mobility](../lectures/week10-network-theory.md)
- Notebook: [week10_transport_networks.ipynb](../../resources/notebooks/week10_transport_networks.ipynb)
- OSMnx documentation: [https://osmnx.readthedocs.io/](https://osmnx.readthedocs.io/)
- NetworkX algorithms: [https://networkx.org/documentation/stable/reference/algorithms/](https://networkx.org/documentation/stable/reference/algorithms/)

## Reflect

Take 10-15 minutes to answer these questions in your [Week 10 reflection](../reference/reflections.md#week-10--transport-networks):

- What patterns did your accessibility analysis reveal? Which areas had the best/worst coverage?
- How did network-based isochrones differ from simple buffers (straight-line distance)? When does the difference matter most?
- How does this Python workflow compare to QGIS QNEAT3 (Week 6)? What are the advantages of scripting? What did you miss about QGIS's visual interface?
- If you compared walking vs. driving access, what equity issues emerged? Who benefits from each mode?
- What additional data would strengthen your analysis (transit schedules, elevation data, facility capacity)?
- How might policymakers use this analysis? What are the risks of oversimplifying accessibility?

!!! note "Reproducibility matters"
    One major advantage of the Python workflow is that you can share your notebook, and anyone with the same environment can reproduce your exact results. This is crucial for transparency in policy research and academic publication.

## What you'll submit

- [ ] Completed Jupyter notebook (`week10_transport_networks.ipynb`) with all cells run and outputs visible
- [ ] Exported isochrones GeoPackage: `outputs/isochrones.gpkg`
- [ ] Coverage analysis GeoPackage: `outputs/coverage_analysis.gpkg`
- [ ] Brief summary (2-3 paragraphs) interpreting your findings: overall coverage rate, equity gaps, policy implications
- [ ] At least one visualization (map or chart) showing accessibility patterns
- [ ] Your Week 10 reflection entry

## Coming up next week

Week 11 is the Design & Storytelling Studio. You'll bring together all the maps and analyses you've created (from QGIS and Python) and craft them into polished, narrative-driven layouts. You'll practice peer critique, run accessibility audits on your designs, and prepare materials for your capstone presentation. Start gathering your favorite outputs from Weeks 1-10—you'll be curating them into a portfolio-quality collection.
