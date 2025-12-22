# Image Audit

Images needed for the course, organised by section.

---

## Getting Ready (Onboarding)

### 01-install-qgis.md
- [ ] QGIS download page screenshot (showing LTR option)
- [ ] QGIS splash screen (showing version number)
- [ ] QGIS interface with Browser, Layers, Processing panels enabled
- [ ] Mac Gatekeeper warning dialog

### 02-workspace-setup.md
- [ ] Folder structure diagram (intro-gis with subfolders)
- [ ] QGIS Browser panel showing Favorites
- [ ] "Add a Directory" dialog
- [ ] Project Properties showing "Save paths: relative"

### 03-download-data.md
- [ ] Natural Earth download page screenshot
- [ ] Example of extracted shapefile files (.shp, .dbf, etc.)
- [ ] QGIS with Natural Earth layer loaded

### 04-python-setup.md
- [ ] Anaconda download page
- [ ] Anaconda Prompt / Terminal with (intro-gis) environment active
- [ ] Jupyter Lab interface
- [ ] Successful import test output

---

## Background Reading

### week01-what-is-gis.md
- [ ] Vector vs raster comparison diagram
- [ ] Points, lines, polygons examples
- [ ] Raster grid/cells illustration
- [ ] GIS layers stacking concept

### week01-capstone-introduction.md
- [ ] Capstone timeline visual (12 weeks)
- [ ] Example capstone folder structure
- [ ] Example finished capstone map

### understanding-crs.md
- [ ] Orange peel projection analogy
- [ ] Geographic vs projected CRS comparison
- [ ] Mercator distortion (Greenland vs Africa)
- [ ] QGIS CRS selector dialog
- [ ] Layers misaligned example
- [ ] Layers aligned correctly example
- [ ] Project CRS button location (bottom-right)

### week03-admin-boundaries.md
- [ ] Boundary hierarchy diagram (ADM0 → ADM1 → ADM2)
- [ ] Australian ASGS hierarchy (SA4 → SA3 → SA2 → SA1)
- [ ] MAUP example (same data, different boundaries, different results)
- [ ] Successful join vs failed join attribute table

### week04-raster-basics.md
- [ ] Raster cells/pixels diagram
- [ ] DEM vs DSM vs DTM comparison
- [ ] Satellite imagery RGB vs false colour
- [ ] Resolution comparison (1m vs 30m vs 250m)
- [ ] Hillshade example
- [ ] Slope map example

### week05-ethics-in-mapping.md
- [ ] Point data vs aggregated data privacy comparison
- [ ] Crime hotspot map example (ethical framing)
- [ ] Choropleth with vs without context

### week07-python-for-gis.md
- [ ] Jupyter notebook interface annotated
- [ ] Code cell vs Markdown cell
- [ ] GeoPandas plot output example

---

## Weekly Labs

### Week 1
- [ ] QGIS interface overview (annotated)
- [ ] Adding a vector layer
- [ ] Attribute table open
- [ ] Identify tool in use
- [ ] Saving a project

### Week 2
- [ ] Layer Properties → Symbology panel
- [ ] Categorized symbology example
- [ ] Graduated symbology example
- [ ] Color ramp selector
- [ ] Label settings panel
- [ ] Print Layout interface
- [ ] Adding map, legend, scale bar, north arrow

### Week 3
- [ ] Join dialog in Layer Properties
- [ ] Attribute table showing joined fields
- [ ] Field Calculator dialog
- [ ] Successful join result map

### Week 4
- [ ] Raster layer loaded in QGIS
- [ ] Raster → Analysis → Hillshade menu
- [ ] Hillshade settings dialog
- [ ] Slope output styled
- [ ] Clip raster by extent dialog

### Week 5
- [ ] Heatmap/KDE settings dialog
- [ ] KDE output map
- [ ] Bandwidth comparison (small vs large)
- [ ] Hotspot map with appropriate styling

### Week 6
- [ ] QNEAT3 plugin installation
- [ ] Isochrone settings
- [ ] Service area output
- [ ] Overlay with vulnerability data

### Week 7
- [ ] Jupyter Lab file browser
- [ ] Running a code cell
- [ ] GeoPandas DataFrame output
- [ ] Simple plot from GeoPandas

### Week 8
- [ ] GeoPandas sjoin output
- [ ] Choropleth from GeoPandas
- [ ] GeoPackage export confirmation

### Week 9
- [ ] Multi-band raster loaded
- [ ] NDVI output
- [ ] Before/after change detection
- [ ] Zonal statistics output

### Week 10
- [ ] OSMnx network visualization
- [ ] Isochrone from Python
- [ ] Network centrality visualization

### Week 11
- [ ] Good vs bad map design comparison
- [ ] Color blindness simulation
- [ ] Visual hierarchy example
- [ ] Before/after design improvements

### Week 12
- [ ] Example capstone presentation slide
- [ ] Portfolio layout example

---

## Slides

Each slide deck needs:
- [ ] Title slide graphic/background (already has contour pattern)
- [ ] Concept diagrams matching lecture content
- [ ] Example outputs from that week's techniques

---

## Summary by Priority

### High Priority (needed for basic understanding)
1. QGIS interface annotated screenshot
2. Vector vs raster diagram
3. CRS/projection explanation diagram
4. Folder structure diagram
5. Boundary hierarchy diagram
6. Jupyter notebook interface

### Medium Priority (helpful but not blocking)
1. Step-by-step QGIS operation screenshots
2. Example map outputs for each week
3. Good vs bad design comparisons
4. DEM/DSM/DTM comparison

### Lower Priority (nice to have)
1. Slide deck graphics
2. Multiple examples of each concept
3. Animated GIFs for complex operations

---

## Suggested image folder structure

```
site_docs/
├── images/
│   ├── onboarding/
│   │   ├── qgis-interface.png
│   │   ├── folder-structure.png
│   │   └── ...
│   ├── concepts/
│   │   ├── vector-vs-raster.png
│   │   ├── crs-projection.png
│   │   └── ...
│   ├── qgis-screenshots/
│   │   ├── add-layer.png
│   │   ├── symbology-panel.png
│   │   └── ...
│   └── examples/
│       ├── choropleth-example.png
│       ├── hotspot-map.png
│       └── ...
```

---

## Total count

- **Onboarding:** ~15 images
- **Background Reading:** ~25 images
- **Weekly Labs:** ~40 images
- **Slides:** ~12+ images

**Estimated total: 90-100 images**

Focus on high-priority conceptual diagrams first, then add screenshots as you teach each week.
