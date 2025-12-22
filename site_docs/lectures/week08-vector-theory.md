# Week 8 Lecture · Python Vector Workflows

## This week
We translate QGIS workflows into reproducible Python code using GeoPandas. Learners explore GeoDataFrames, spatial joins, attribute operations, and choropleth mapping to automate the vector analysis techniques from earlier weeks.

## By the end of the week you will
- Explain how GeoPandas relates to pandas and why GeoDataFrames combine spatial and tabular operations.
- Perform spatial joins (sjoin) and overlays to replicate QGIS intersection and union workflows.
- Clean and transform spatial data using pandas methods (assign, query, groupby) and handle projection conversions.
- Generate choropleth maps with contextily basemaps and export publication-ready outputs.

## Key vocabulary
GeoPandas · GeoDataFrame · spatial join · sjoin · overlay · dissolve · CRS transformation · choropleth · attribute operation · groupby.

## What happens in class
- Recap Week 3 joins and Week 5 analysis, showing equivalent Python snippets for familiar workflows.
- Demonstrate reading spatial files, inspecting metadata, and converting CRS with to_crs().
- Walk through a spatial join example: counting incidents per neighbourhood and calculating density metrics.
- Show data cleaning patterns (column renaming, dtype fixes, handling null geometries) using assign and query.
- Produce a choropleth map and overlay a web basemap using contextily, then export to GeoPackage for QGIS review.

## Prepare beforehand
- Ensure Python environment is set up with GeoPandas, matplotlib, and contextily (see [Week 7 setup guide](../onboarding/python-setup.md)).
- Review the sample code in [Week 8 lecture slides](../assets/slides/week08.html) before class.
- Download the Week 8 datasets listed in the [data checklist](../reference/data-download-checklist.md).

## Connected lab
The [Week 8 lab](../weeks/week08.md) guides learners through automating vector workflows, performing spatial joins, and creating reproducible analysis scripts.

