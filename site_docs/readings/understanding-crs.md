# Understanding Coordinate Reference Systems (CRS)

**Read before:** Week 1 (skim) / Week 3 (detail) | **Time:** 30 minutes

One of the most confusing aspects of GIS for beginners is the Coordinate Reference System (CRS). This guide explains what CRS is, why it matters, and how to work with it in your projects.

## What is a CRS and why does it matter?

Think back to maths class: you plotted points on a Cartesian grid using X and Y coordinates. The point (3, 4) meant "3 units right from the origin, 4 units up." Simple.

But that only works because everyone agrees on:

- **Where the origin (0, 0) is** — the corner of the grid
- **What the units are** — usually just "units" on the grid
- **Which direction is positive** — right for X, up for Y

Now imagine doing this on the Earth's surface. Where's (0, 0)? What's a "unit"—degrees? meters? feet? Which way is "up" when you're on a sphere?

A **Coordinate Reference System** (CRS) answers all these questions:

1. **Where is the origin?** (e.g., the intersection of the Equator and Prime Meridian)
2. **What units are used?** (degrees for lat/lon, meters for projected systems)
3. **How is the curved Earth flattened onto a flat map?** (the projection method)

Without a CRS, the coordinates `(151.2, -33.9)` are meaningless numbers. With the wrong CRS, your layers won't align—Sydney could end up in the Atlantic Ocean.

## The fundamental problem: Earth is round, maps are flat

You can't flatten a sphere perfectly. Try peeling an orange and flattening the peel—it tears or distorts.

Every map projection makes **trade-offs**:

- **Preserve area?** Shapes get distorted (e.g., Greenland looks huge on some projections)
- **Preserve shape?** Areas get distorted (e.g., things near poles look stretched)
- **Preserve distance?** Only from specific points, not everywhere
- **Preserve direction?** Useful for navigation, but distances might be wrong

**There is no perfect projection**—you choose based on your needs.

## Two main types of CRS

### 1. Geographic CRS (latitude/longitude)

**What it is:**
- Uses degrees of latitude (North-South) and longitude (East-West)
- Coordinates look like: `(51.5074, -0.1278)` or `(lat, lon)`
- Covers the whole globe
- Common example: **WGS 84 (EPSG:4326)**—used by GPS

**When to use it:**
- Global or multi-continent maps
- When you need to display data "as is" from GPS
- Initial data loading (before projecting)

**Limitations:**
- **Can't accurately measure distance or area** (a degree of longitude near the equator is wider than near the poles)
- Shapes appear distorted near poles
- Not good for analysis requiring measurements

**Example:**
```
Sydney Opera House: -33.8568°, 151.2153°
London Eye: 51.5033°, -0.1196°
```

### 2. Projected CRS (X/Y in meters or feet)

**What it is:**
- Uses flat X/Y coordinates in meters (or feet)
- Coordinates look like: `(500000, 6000000)` meters from an origin
- Designed for specific regions (e.g., Australia, Europe, a single state)
- Common examples:
  - **GDA2020 / MGA zones (Australia):** EPSG:7844-7860
  - **UTM zones (global, 6° wide strips):** EPSG:32601-32660 (Northern Hemisphere), 32701-32760 (Southern)
  - **Web Mercator (online maps):** EPSG:3857

**When to use it:**
- When you need accurate distance/area calculations
- Regional or local analysis
- Creating buffers (e.g., "500 meters around this point")
- Measuring perimeters, areas, or densities

**Limitations:**
- Only accurate within a limited area (don't use Australian projection for European data!)
- Coordinates aren't intuitive (what does "500000, 6000000" mean to a human?)

**Example (Sydney in GDA2020 MGA Zone 56):**
```
Sydney Opera House: ~334,000m East, ~6,251,000m North (from zone origin)
```

## Common CRS codes (EPSG codes)

EPSG codes are shorthand identifiers for CRS. Here are the most common:

| EPSG Code | Name | Type | Coverage | Use Case |
|-----------|------|------|----------|----------|
| **4326** | WGS 84 | Geographic | Global | GPS data, global maps |
| **3857** | Web Mercator | Projected | Global | Online maps (Google, OpenStreetMap) |
| **7844** | GDA2020 | Geographic | Australia | Australian lat/lon data |
| **7855-7860** | GDA2020 MGA zones | Projected | Australian zones | Accurate measurements in Australia |
| **32755** | WGS 84 / UTM zone 55S | Projected | Eastern Australia | Alternative to MGA |
| **4283** | GDA94 | Geographic | Australia | Older Australian standard (pre-2020) |
| **3577** | Australian Albers | Projected | Australia (all) | National-scale analysis, preserves area |

**How to read EPSG codes:**
- **4XXX:** Usually geographic (lat/lon in degrees)
- **3XXX, 7XXX, 32XXX:** Usually projected (X/Y in meters)

## How CRS affects your work

### Problem 1: Mismatched CRS breaks alignment

**Scenario:** You load a shapefile (CRS: EPSG:4326) and a GeoTIFF (CRS: EPSG:7856). They don't line up!

**Why:** QGIS tries to reproject one on-the-fly, but if it can't detect the CRS correctly, layers appear in wrong locations.

**Solution:**
1. Check each layer's CRS: Right-click layer → **Properties** → **Information** tab
2. Set project CRS: Click the CRS button in bottom-right corner
3. Reproject layers if needed: `Processing ▶ Vector geometry ▶ Reproject layer`

### Problem 2: Wrong CRS makes measurements meaningless

**Scenario:** You buffer a point by "500" in a geographic CRS (EPSG:4326).

**Result:** You get a buffer of 500 **degrees**, not 500 meters—which is enormous and distorted!

**Solution:** Always reproject to a projected CRS (in meters) before:
- Creating buffers
- Calculating areas or distances
- Measuring perimeters
- Doing density calculations

### Problem 3: Using the wrong regional projection

**Scenario:** You analyze Sydney data using a European projection (EPSG:3035).

**Result:** Distances and areas are completely wrong—you might get a park that's "10,000 square meters" when it's actually 15,000.

**Solution:** Use a projection designed for your region:
- **Australia:** GDA2020 MGA zones (EPSG:7855-7860) or Australian Albers (EPSG:3577)
- **USA:** State Plane or UTM zones
- **Europe:** ETRS89 / LAEA Europe (EPSG:3035)

## How to check and change CRS in QGIS

### Check a layer's CRS

1. Right-click the layer in the Layers Panel → **Properties**
2. Click the **Information** tab (or **Source** tab)
3. Look for "CRS" or "Coordinate Reference System"
4. You'll see something like: `EPSG:4326 - WGS 84`

### Set your project CRS

1. Click the CRS button in the **bottom-right corner** of QGIS
2. This shows/sets the project CRS (the CRS used to display all layers)
3. QGIS will try to reproject layers on-the-fly to match

!!! tip "Project CRS vs Layer CRS"
    - **Layer CRS:** The CRS the data is actually stored in
    - **Project CRS:** The CRS QGIS displays everything in
    - QGIS reprojects layers on-the-fly for display, but the original files aren't changed

### Reproject a layer (permanent change)

If you need to actually change a layer's CRS (not just display):

1. Right-click the layer → **Export** → **Save Features As...**
2. Set the **CRS** dropdown to your desired CRS
3. Save to a new file
4. The new file is now in the new CRS

**Or use Processing Toolbox:**
1. `Processing ▶ Toolbox`
2. Search: "Reproject layer"
3. Select `Vector geometry ▶ Reproject layer`
4. Choose target CRS and output location

## Common questions

### "Which CRS should I use?"

**For display/exploration:**
- Use whatever looks good for your region
- EPSG:4326 (WGS 84) is fine for global context

**For analysis (buffers, areas, distances):**
- Use a projected CRS in meters designed for your region:
  - **Australia:** EPSG:7855-7860 (MGA zones) or EPSG:3577 (national analysis)
  - **Global analysis:** UTM zone for your area (EPSG:32701-32760)
  - **Web maps:** EPSG:3857 (Web Mercator)

### "Why does my data have a weird CRS?"

Data publishers use different standards. Common reasons:
- **Government data:** Uses national standard (e.g., GDA2020 in Australia)
- **GPS data:** Usually WGS 84 (EPSG:4326)
- **Web-downloaded data:** Often Web Mercator (EPSG:3857)
- **Old data:** Might use outdated CRS (e.g., GDA94 instead of GDA2020)

### "What if my layer shows 'Unknown CRS' or 'No CRS'?"

This means QGIS couldn't detect the CRS from the file. You need to tell it:

1. Right-click layer → **Properties** → **Source** tab
2. Click **Select CRS**
3. Search for the correct CRS (check the data documentation!)
4. Click OK

!!! warning "Defining vs. Reprojecting"
    - **Set CRS/Define CRS:** Tells QGIS what CRS the data is *already* in (doesn't change coordinates)
    - **Reproject:** Actually transforms coordinates from one CRS to another

### "My layers don't align—what do I do?"

**Checklist:**

1. Check if all layers have a CRS defined (not "Unknown")
2. Check if project CRS is set (bottom-right corner)
3. Enable on-the-fly reprojection (should be default in QGIS 3+)
4. If still broken, reproject problem layers to match your project CRS

### "What's the difference between GDA94 and GDA2020?"

- **GDA94:** Old Australian standard
- **GDA2020:** New Australian standard (official since 2020)
- Difference is ~1.8 meters—matters for high-precision work

Use GDA2020 for new projects. If working with old data (GDA94), either:
- Leave it as-is if precision isn't critical
- Reproject to GDA2020 if combining with newer data

## Practical workflow

**Starting a new project:**

1. **Set your project CRS early** (bottom-right button)
   - Pick based on your analysis needs (projected for measurements, geographic for display)
2. **Check each layer's CRS as you load it**
   - Layer Properties → Information tab
3. **Reproject layers if you'll be doing analysis**
   - Saves time later and avoids errors
4. **Always use projected CRS (meters) for:**
   - Buffers
   - Area calculations
   - Distance measurements
   - Density calculations

**Working with mixed CRS data:**

1. Set project CRS to your preferred CRS
2. QGIS will reproject other layers on-the-fly for display
3. For analysis, explicitly reproject to match
4. Save your reprojected layers to avoid redoing work

## Resources

- **EPSG.io:** Search CRS codes and see their coverage: [epsg.io](https://epsg.io/)
- **QGIS Docs:** Official CRS documentation: [docs.qgis.org](https://docs.qgis.org/latest/en/docs/user_manual/working_with_projections/)
- **Projection Wizard:** Find best projection for your area: [projectionwizard.org](https://projectionwizard.org/)

## Key takeaways

✅ **Always check your CRS** when loading data
✅ **Use projected CRS (meters)** for analysis and measurements
✅ **Use geographic CRS (degrees)** for global display or GPS data
✅ **Match CRS to your region** (don't use Australian projection for European data!)
✅ **Set project CRS early** to avoid confusion
✅ **Reproject explicitly** for analysis (don't rely only on on-the-fly reprojection)

---

**Remember:** CRS confusion is normal for beginners. When in doubt:
1. Check the CRS (layer properties)
2. Set a project CRS
3. Reproject to match if doing analysis

You'll get more comfortable with practice!
