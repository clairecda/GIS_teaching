# Week 10 Lecture · Network Theory for Mobility

## Objectives

- Explain fundamental graph concepts used in transport analysis (nodes, edges, weights).
- Introduce accessibility metrics (isochrones, betweenness, coverage, catchment ratios).
- Discuss data sources (OpenStreetMap, GTFS) and preprocessing considerations.

## Outline

1. **Graph fundamentals**  
   - Directed vs undirected graphs, weighted edges (distance, time).  
   - Simplification levels (primal vs dual graphs) and implications for analysis.
2. **Accessibility measures**  
   - Isochrones (reach in X minutes) and coverage metrics (population within catchment).  
   - Betweenness/closeness centrality for identifying critical links.  
   - Two-step floating catchment for transit/health service overlap.
3. **Data integration**  
   - Working with OpenStreetMap (coverage, tagging quirks).  
   - GTFS feed components (stops, trips, stop_times) and conversion to networks.  
   - Handling coordinate reference systems and projections for network calculations.
4. **Equity & policy context**  
   - Using demographic overlays to interpret accessibility, aligning with Week 6 themes.  
   - Presenting limitations (schedule granularity, assumed speeds).

## Activities

- Visualise a simple network diagram and compute sample metrics manually.  
- Review case studies (e.g., Melbourne tram accessibility, Sydney bus coverage).

## Resources

- OSMnx documentation: <https://osmnx.readthedocs.io/>  
- Transitland / GTFS resources.  
- Academic references on accessibility modelling.

## Lab connection

- Supports Week 10 notebook tasks (downloading network graphs, computing isochrones, intersecting with population polygons).
