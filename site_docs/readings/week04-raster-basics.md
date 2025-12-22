# Raster Data Basics

**Read before:** Week 4 | **Time:** 15 minutes

---

## What is raster data?

Raster data represents the world as a grid of cells (pixels). Each cell stores a single value — elevation, temperature, colour, or land cover type.

Think of it like a digital photo: millions of tiny squares, each with one colour. Zoom in far enough and you see the individual pixels.

---

## Raster vs vector

| Aspect | Raster | Vector |
|--------|--------|--------|
| Structure | Grid of cells | Points, lines, polygons |
| Best for | Continuous surfaces | Discrete features |
| Examples | Elevation, imagery, temperature | Roads, boundaries, buildings |
| File size | Large (one value per cell) | Smaller (just vertices) |
| Zoom | Gets pixelated | Stays sharp |

**Use raster for:** surfaces that vary continuously (elevation, rainfall, satellite images)

**Use vector for:** distinct features with boundaries (roads, suburbs, buildings)

---

## Common raster data types

### Elevation (DEM/DSM/DTM)

| Type | What it measures | Includes |
|------|------------------|----------|
| DEM | Digital Elevation Model | Bare ground only |
| DSM | Digital Surface Model | Ground + buildings + trees |
| DTM | Digital Terrain Model | Ground + natural features |

**Used for:** Flood modelling, slope analysis, viewsheds, 3D visualisation

### Satellite imagery

Multiple "bands" capture different wavelengths:
- **RGB (visible):** What we see — red, green, blue
- **NIR (near-infrared):** Vegetation reflects strongly here
- **SWIR (shortwave infrared):** Useful for geology, moisture

**Used for:** Land cover mapping, vegetation health (NDVI), change detection

### Derived surfaces

- **Slope:** Steepness of terrain (degrees or percent)
- **Aspect:** Direction a slope faces (N, S, E, W)
- **Hillshade:** Shaded relief for visualisation
- **Curvature:** Convex or concave terrain shapes

---

## Key raster concepts

### Resolution

How big is each cell?

| Resolution | Cell size | Detail level |
|------------|-----------|--------------|
| High | 1-10 metres | Individual buildings visible |
| Medium | 30 metres | Suburbs, fields visible |
| Low | 250+ metres | Regional patterns only |

**Trade-off:** Higher resolution = larger file = slower processing

### Bands

Satellite imagery has multiple bands (layers):
- Landsat: 11 bands
- Sentinel-2: 13 bands
- Drone imagery: Usually 3-5 bands

You can combine bands to see different things (true colour, false colour, vegetation indices).

### NoData

Cells with no valid value (clouds, ocean, outside boundary) are marked as "NoData" — typically -9999 or similar.

**Important:** NoData isn't zero! An elevation of 0 is sea level. NoData means "no measurement here."

---

## Raster formats

| Format | Extension | Notes |
|--------|-----------|-------|
| GeoTIFF | `.tif` | Most common, includes CRS info |
| JPEG2000 | `.jp2` | Compressed, good for imagery |
| ASCII Grid | `.asc` | Text-based, easy to read |
| NetCDF | `.nc` | Multi-dimensional (time series) |

**Recommendation:** Use GeoTIFF for most work — well-supported everywhere.

---

## Working with rasters in QGIS

### Load a raster
1. **Layer > Add Layer > Add Raster Layer**
2. Or drag `.tif` file into QGIS

### Check properties
Right-click layer > **Properties** > **Information**
- CRS, dimensions, cell size, bands, data type

### Style options
- **Singleband gray:** One band, grayscale
- **Singleband pseudocolor:** One band with colour ramp
- **Multiband color:** RGB composite from 3 bands

### Common operations
- **Clip:** Cut raster to boundary (Processing > Clip Raster)
- **Hillshade:** Create shaded relief (Raster > Analysis > Hillshade)
- **Slope:** Calculate steepness (Raster > Analysis > Slope)
- **Raster Calculator:** Math on cell values

---

## Week 4 preview

In Week 4, you'll:
1. Load elevation data (DEM)
2. Create hillshade for visualisation
3. Calculate slope
4. Clip to your study area
5. Combine with vector boundaries

---

## Key takeaways

✅ **Raster = grid of cells** with one value each

✅ **Resolution matters** — balance detail vs file size

✅ **DEM ≠ DSM ≠ DTM** — know what you're measuring

✅ **NoData ≠ zero** — it means "no measurement"

✅ **GeoTIFF** is the go-to format
