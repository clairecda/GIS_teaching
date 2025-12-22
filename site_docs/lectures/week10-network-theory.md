# Week 10 Lecture · Transport Networks & Accessibility

## This week
We explore how spatial networks represent mobility systems and how graph theory helps measure accessibility. Learners work with OpenStreetMap data, compute isochrones, and apply network analysis to understand service coverage and transport equity.

## By the end of the week you will
- Explain fundamental graph concepts (nodes, edges, weights) and how they represent transport networks.
- Use OSMnx to download and analyze street networks from OpenStreetMap.
- Generate isochrones to measure accessibility and service catchment areas.
- Integrate network analysis with demographic data to evaluate transport equity and planning scenarios.

## Key vocabulary
Graph theory · nodes · edges · directed/undirected graphs · weighted networks · OSMnx · NetworkX · isochrones · accessibility · service area · betweenness centrality · catchment · GTFS · primal/dual graphs.

## What happens in class
- Introduce graph fundamentals: directed vs undirected networks, weighted edges (distance, time, elevation), and how they model different transport modes.
- Demonstrate OSMnx workflows: downloading street networks, visualizing road hierarchies, and computing basic network statistics.
- Generate isochrones showing areas reachable within 5/10/15 minutes by walking, cycling, or driving.
- Discuss accessibility metrics (betweenness centrality, coverage ratios, two-step floating catchment) and their applications in equity analysis.
- Review case studies linking accessibility to demographic data, connecting back to Week 3 boundaries and Week 6 health/equity themes.

## Prepare beforehand
- Install OSMnx and NetworkX libraries following the [Python setup guide](../reference/python-setup.md).
- Review graph theory basics in the [Week 10 pre-reading](../readings/week10-network-basics.md).
- Download or bookmark OpenStreetMap data for your study area using the [data download guide](../onboarding/data-downloads.md).

## Connected lab
The [Week 10 lab](../weeks/week10.md) guides learners through downloading networks with OSMnx, computing isochrones, and overlaying results with population data to assess service accessibility.

## Further Reading

**Essential:**
- [OSMnx Documentation](https://osmnx.readthedocs.io/en/stable/) - Official documentation for downloading, analyzing, and visualizing street networks from OpenStreetMap
- [NetworkX Tutorial](https://networkx.org/documentation/stable/tutorial.html) - Comprehensive guide to graph theory fundamentals and network analysis in Python
- [Introduction to Network Analysis - Geographic Data Science Book](https://geographicdata.science/book/notebooks/08_point_pattern_analysis.html) - Academic introduction to spatial network concepts with Python examples
- [OpenStreetMap Wiki: Routing](https://wiki.openstreetmap.org/wiki/Routing) - Guide to OSM data structure, tags, and routing considerations

**Optional but recommended:**
- [GTFS Static Overview - Google Transit](https://developers.google.com/transit/gtfs) - Specification for public transit data including stops, routes, and schedules
- [Urban Street Networks Analysis with OSMnx - Boeing 2017](https://journals.sagepub.com/doi/full/10.1177/2399808317715537) - Academic paper introducing OSMnx and its applications in urban analytics
- [Isochrone Maps with OSMnx + Python](https://geoffboeing.com/2017/08/isochrone-maps-osmnx-python/) - Tutorial by OSMnx creator on creating isochrone maps for accessibility analysis
- [Transport Geography - The Geography of Transport Systems](https://transportgeography.org/contents/chapter4/) - Conceptual overview of network structure and accessibility concepts

**Videos:**
- [OSMnx Street Network Tutorial](https://www.youtube.com/results?search_query=osmnx+python+tutorial+street+network+openstreetmap) - Search for tutorials on downloading and analyzing networks with OSMnx
- [NetworkX Graph Tutorial](https://www.youtube.com/results?search_query=networkx+python+tutorial+graph+analysis+beginner) - Search for introductions to graph theory and network analysis in Python
