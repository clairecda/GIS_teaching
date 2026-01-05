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

## Automation and responsibility

Code-based workflows feel objective—the computer just executes instructions. But automation amplifies whatever logic we encode, including our assumptions and blind spots.

**Scale changes the stakes:**

- A manual QGIS analysis might process 50 neighborhoods. A Python script can process 50,000 in minutes
- Errors, biases, and questionable assumptions that might be caught manually now propagate across entire datasets
- "The algorithm did it" is not accountability—you wrote (or chose) the algorithm

**The objectivity trap:**

- Code can make arbitrary choices look inevitable. A spatial join with `how='left'` vs `how='inner'` changes which records survive—but the syntax doesn't signal that this is a judgment call
- Variable names like `calculate_risk()` or `identify_priority_areas()` embed interpretive frames as if they were neutral operations
- The same code applied to different communities produces "consistent" results—but consistency isn't the same as fairness

**Whose data, whose categories?**

When you automate vector workflows, ask:

- What records are being joined, and which are being dropped? (Check for NULL geometries, failed joins, edge cases)
- Whose categories are encoded in the attribute fields? Who created them, and for what purpose?
- Would the people being analyzed recognize themselves in these data structures?

**Professional practice:**

Automation is powerful precisely because it removes human judgment from each individual case. That makes it more important—not less—to exercise judgment about the system as a whole.

## What happens in class
- Recap Week 3 joins and Week 5 analysis, showing equivalent Python snippets for familiar workflows.
- Demonstrate reading spatial files, inspecting metadata, and converting CRS with to_crs().
- Walk through a spatial join example: counting incidents per neighbourhood and calculating density metrics.
- Show data cleaning patterns (column renaming, dtype fixes, handling null geometries) using assign and query.
- Produce a choropleth map and overlay a web basemap using contextily, then export to GeoPackage for QGIS review.

## Prepare beforehand
- Ensure Python environment is set up with GeoPandas, matplotlib, and contextily (see [Python Setup Guide](../onboarding/04-python-setup.md)).
- Review the sample code in [Week 8 lecture slides](../slides/week08.html) before class.
- Download the Week 8 datasets listed in the [data checklist](../reference/data-download-checklist.md).

## Connected lab
The [Week 8 lab](../weeks/week08.md) guides learners through automating vector workflows, performing spatial joins, and creating reproducible analysis scripts.

