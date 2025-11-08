# Spatial Data Models

Vector and raster data are the two foundational structures used in GIS. Understanding how they differ helps you choose the right model for each analysis.

## Vector data

- Represents discrete features (points, lines, polygons).
- Stores geometry + attribute tables.
- Ideal for boundaries, roads, facilities, and other distinct objects.
- Common formats: Shapefile, GeoPackage, GeoJSON.

### Strengths

- Precise geometry for measurements and topology.
- Easier to link with tabular data (joins, queries).
- Smaller file sizes for sparse data.

### Limitations

- Less efficient for continuous surfaces (temperature, elevation).
- Complex topology management when editing.

## Raster data

- Represents continuous surfaces via grid cells (pixels) with numeric values.
- Ideal for imagery, elevation, density, and model outputs.
- Common formats: GeoTIFF, IMG, NetCDF.

### Strengths

- Handles continuous phenomena and cell-based operations (map algebra).
- Integrates well with remote sensing and surface analysis.

### Limitations

- File sizes grow quickly with resolution and extent.
- Attribute storage limited to cell values; categorical rasters may need look-up tables.

## Metadata to capture

| Field | Vector | Raster |
| ----- | ------ | ------ |
| CRS | e.g., `EPSG:4283` | e.g., `EPSG:3577` |
| Geometry/resolution | Point, Line, Polygon | Cell size (e.g., 30 m) |
| Extent | Bounding box | Bounding box |
| Population threshold | Often defined for statistical areas | Not applicable |
| Data vintage | Census year | Acquisition date |

## Course connections

- **Week 2:** Compare vector (Natural Earth) and raster (hillshade) styling.
- **Week 3:** Join vector boundaries with socio-economic tables.
- **Week 4:** Clip DEM rasters and derive slope/hillshade.
- **Week 9:** Use raster processing tools in Python for change detection.

Keep this cheat sheet handy when deciding whether to work with vectors, rasters, or both.
