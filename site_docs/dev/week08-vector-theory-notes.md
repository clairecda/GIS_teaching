# Week 8 Lecture · Vector Automation Concepts

## Objectives

- Map QGIS vector workflows to Python libraries (GeoPandas, Shapely, PyProj).
- Discuss data cleaning strategies (naming conventions, handling missing values).
- Highlight performance considerations and tooling for reproducible vector pipelines.

## Outline

1. **From GUI to code**  
   - Recap Week 3 joins and Week 5 analysis to show equivalent code snippets.  
   - Anatomy of a GeoPandas workflow (read → clean → spatial join → summarise → export).
2. **Data cleaning patterns**  
   - Column normalisation, dtype conversions, dealing with multi-part geometries.  
   - Using `assign`, `query`, `groupby`.
3. **Spatial joins & overlays**  
   - `sjoin`, `overlay`, `dissolve` and when to use each.  
   - Notes on projections and performance.
4. **Saving outputs**  
   - GeoPackage vs GeoJSON vs Parquet; storing metadata in filenames or README.  
   - Round-tripping data back into QGIS.

## Sample code to showcase

```python
neighbourhoods = gpd.read_file("data/processed/week08/neighbourhoods.geojson").to_crs(3857)
incidents = gpd.read_file("data/processed/week08/incidents.geojson").to_crs(3857)
joined = gpd.sjoin(incidents, neighbourhoods, predicate="within")
summary = (
    joined.groupby("neighbourhood_id")
    .size()
    .rename("incident_count")
    .to_frame()
    .join(neighbourhoods.set_index("neighbourhood_id"), how="right")
)
summary["rate_km2"] = summary["incident_count"] / (summary.geometry.area / 1e6)
summary.to_file("data/processed/week08/neighbourhoods_summary.gpkg", layer="summary")
```

## Discussion prompts

- What QA checks should you run after automating joins?  
- How do you balance code readability vs efficiency?  
- When would you still use QGIS manually instead of automation?

## Resources

- GeoPandas documentation: <https://geopandas.org/>  
- OSMnx for graph-based spatial operations: <https://osmnx.readthedocs.io/>  
- Pysal for spatial statistics: <https://pysal.org/>
