# What is GIS?

**Read before:** Week 1 | **Time:** 15 minutes

---

## The short answer

A **Geographic Information System (GIS)** connects data to locations. It lets you ask questions like:

- Where are the hospitals closest to this neighbourhood?
- Which areas have the highest crime rates?
- How has land use changed over the past 20 years?

GIS combines maps, data, and analysis tools to answer spatial questions that spreadsheets can't.

---

## Why location matters

Most data has a location attached to it — addresses, postcodes, coordinates, place names. But in a spreadsheet, that location is just text. You can't see patterns, measure distances, or find what's nearby.

GIS turns location into something you can analyse:

| Spreadsheet | GIS |
|-------------|-----|
| "123 Main St, Sydney" | A point on a map you can click |
| "NSW" | A polygon boundary you can measure |
| "5km from CBD" | A buffer zone you can visualise |

---

## Two types of spatial data

### Vector data
Points, lines, and polygons that represent discrete features:

- **Points:** Cities, hospitals, crime incidents, survey locations
- **Lines:** Roads, rivers, power lines, bus routes
- **Polygons:** Countries, suburbs, parks, flood zones

Vector data has an **attribute table** — each feature has a row with information (name, population, date, etc.).

### Raster data
Grids of cells (pixels) that represent continuous surfaces:

- Satellite imagery
- Elevation models (DEMs)
- Temperature maps
- Land cover classifications

Each cell has a single value (elevation in metres, temperature in degrees, etc.).

---

## What can you do with GIS?

**Mapping:** Create thematic maps that show patterns in data

**Analysis:** Buffer zones, density calculations, route finding, change detection

**Joins:** Connect data tables to map boundaries (e.g., census data to suburbs)

**Overlay:** Combine layers to answer questions (e.g., which schools are in flood zones?)

---

## GIS in everyday life

You already use GIS without realising it:

- **Google Maps** — routing, traffic, place search
- **Weather apps** — spatial forecasts, radar imagery
- **Real estate sites** — property maps, neighbourhood data
- **Delivery tracking** — location updates, route planning

This course teaches you to build these kinds of analyses yourself.

---

## Key terms to know

| Term | Meaning |
|------|---------|
| Layer | A single dataset on the map (e.g., roads, boundaries) |
| Attribute | A property of a feature (e.g., name, population) |
| CRS | Coordinate Reference System — how locations are defined |
| Shapefile | A common vector data format (.shp) |
| GeoTIFF | A common raster data format (.tif) |

---

## Reflection questions

Before Week 1, think about:

1. What spatial questions do you encounter in your work or life?
2. Where have you seen maps used to communicate data?
3. What would you like to be able to map by the end of this course?

Bring these thoughts to the Week 1 discussion.
