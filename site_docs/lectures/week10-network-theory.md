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

## Whose mobility counts?

Network analysis models movement through infrastructure—but infrastructure itself reflects historical investment patterns, and the networks we can analyze depend on what's been mapped and measured.

**Networks model what exists, not what should exist:**

- An isochrone shows where you can reach in 15 minutes—assuming the roads, sidewalks, or transit lines exist
- Areas with sparse infrastructure appear "inaccessible" in analysis, but this describes underinvestment, not inherent geography
- Network analysis can naturalize inequality: "these areas have poor access" versus "these areas have been denied infrastructure"

**Whose movement is modeled?**

- Walking networks assume pedestrian infrastructure. What about wheelchair users, parents with strollers, or people with mobility aids?
- Driving isochrones assume car ownership. Transit analysis assumes published schedules—but many communities rely on informal transport (shared rides, unlicensed taxis) that doesn't appear in GTFS feeds
- Cycling networks assume bike infrastructure and cultural acceptance of cycling—neither universal

**The edge weights encode assumptions:**

- Travel time calculations assume average speeds, free-flow conditions, and consistent network quality
- Perception of safety, lighting, social factors, and historical trauma affect real-world route choice but rarely appear in network models
- A technically "accessible" route may be practically inaccessible due to factors the model doesn't capture

**Questions to carry forward:**

- Who is the implied traveler in this network model? What would change if we centered a different person?
- What infrastructure investments would change these isochrones? Who decides whether those investments happen?
- How do we communicate that "accessibility" in a network model is not the same as lived experience of access?

## What happens in class
- Introduce graph fundamentals: directed vs undirected networks, weighted edges (distance, time, elevation), and how they model different transport modes.
- Demonstrate OSMnx workflows: downloading street networks, visualizing road hierarchies, and computing basic network statistics.
- Generate isochrones showing areas reachable within 5/10/15 minutes by walking, cycling, or driving.
- Discuss accessibility metrics (betweenness centrality, coverage ratios, two-step floating catchment) and their applications in equity analysis.
- Review case studies linking accessibility to demographic data, connecting back to Week 3 boundaries and Week 6 health/equity themes.

## Prepare beforehand
- Install OSMnx and NetworkX libraries following the [Python Setup Guide](../onboarding/04-python-setup.md).
- Review Week 6 and Week 7 materials on network analysis concepts.
- Download or bookmark OpenStreetMap data for your study area using the [data download guide](../onboarding/03-download-data.md).

## Connected lab
The [Week 10 lab](../weeks/week10.md) guides learners through downloading networks with OSMnx, computing isochrones, and overlaying results with population data to assess service accessibility.

