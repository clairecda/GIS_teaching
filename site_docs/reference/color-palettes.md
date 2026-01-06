# Color Palettes Reference

Consistent, accessible colors make your maps professional and readable. This guide covers creating palettes in QGIS and choosing colors for different map types.

## Example Color Palette

Here's an **example** palette showing typical colors for common map features. You should choose colors appropriate to your specific map and data:

| Feature | Example Color | Hex | Notes |
|---------|---------------|-----|-------|
| Water (ocean, lakes) | Blue | `#4a90d9` | Use blues for water—this is a universal convention |
| Rivers, streams | Light Blue | `#4fc3f7` | Lighter blue for smaller water features |
| Vegetation, forests | Green | `#2e7d32` | Darker greens for dense vegetation |
| Parks, grassland | Light Green | `#7cb342` | Lighter greens for open land |
| Urban areas | Grey | `#455a64` | Neutral greys for built-up areas |
| Desert, bare ground | Sand/Tan | `#d4a574` | Warm earth tones |
| Roads | Brown/Grey | `#8d6e63` | Depending on map style |
| Points of interest | Orange/Red | `#e65100` | Warm colors draw attention |

!!! tip "These are suggestions, not rules"
    Choose colors that work for **your** map and data. The key principles are:

    - **Water should be blue** — this is a strong cartographic convention
    - **Vegetation should be green** — another universal expectation
    - **Use contrast** — ensure features are distinguishable
    - **Be consistent** — use the same color for the same feature type across your maps

## Setting Up Your Palette in QGIS

### Method 1: Settings → Options

1. Go to `Settings ▶ Options ▶ Colors`
2. Click the green **+** button
3. Enter hex code or use color picker
4. Double-click to name the color (e.g., "Course - Deep Teal")
5. Colors save automatically

### Method 2: From Any Color Selector

1. Click the dropdown arrow next to any color button
2. Select **Colors...** to open the palette manager
3. Add/edit colors as above

### Import/Export Palettes

**Export:**
```
Settings → Options → Colors → ... → Export Colors
Save as .gpl file
```

**Import:**
```
Settings → Options → Colors → ... → Import Colors
Select .gpl file
```

## Choosing Colors for Different Map Types

### Categorical Maps (Categorized Symbology)

For distinct categories (land use, continents, zones):

- Use **qualitative** color schemes with distinct hues
- Avoid implying order (light→dark suggests ranking)
- Maximum 7-8 distinct colors before confusion
- Consider using patterns/hatching for additional distinction

**Recommended:** ColorBrewer Set2, Set3, Paired

### Sequential Maps (Graduated Symbology)

For numeric data showing progression (population, income):

- Use **sequential** schemes: light→dark or single hue gradient
- Lighter = lower values, Darker = higher values
- 4-6 classes typically optimal

**Recommended:** ColorBrewer YlOrRd, Blues, Greens

### Diverging Maps

For data with meaningful midpoint (change, deviation from average):

- Use **diverging** schemes: two hues meeting at neutral middle
- Middle color = zero/average, extremes = positive/negative
- Ensure equal visual weight on both sides

**Recommended:** ColorBrewer RdBu, PiYG, BrBG

## Accessibility Considerations

### Color Vision Deficiency

~8% of males and ~0.5% of females have some form of color vision deficiency.

**Do:**

- Use ColorBrewer schemes (designed for accessibility)
- Add patterns/textures in addition to color
- Test with a [color blindness simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/)
- Ensure sufficient contrast between adjacent colors

**Don't:**

- Rely solely on red/green distinction
- Use rainbow color schemes for sequential data
- Assume everyone sees colors the same way

### Safe Color Combinations

| Good | Avoid |
|------|-------|
| Blue + Orange | Red + Green |
| Purple + Yellow | Blue + Purple (similar) |
| Teal + Coral | Green + Brown |
| Black + Yellow | Red + Brown |

## ColorBrewer Integration

[ColorBrewer](https://colorbrewer2.org/) provides research-backed color schemes.

### Using ColorBrewer in QGIS

1. Open Layer Properties → Symbology
2. Click the Color ramp dropdown
3. Select **All Color Ramps** → **ColorBrewer**
4. Choose from:
   - **Sequential:** Blues, Greens, YlOrRd, etc.
   - **Diverging:** RdBu, PiYG, PRGn, etc.
   - **Qualitative:** Set2, Paired, Dark2, etc.

### Creating Custom ColorBrewer Ramp

1. Visit [colorbrewer2.org](https://colorbrewer2.org/)
2. Select number of classes and scheme type
3. Copy hex codes
4. In QGIS: Color ramp → **Create New** → **Catalog: cpt-city**
5. Or manually create gradient using hex codes

## Quick Reference: Map Type → Color Scheme

| Map Type | Data | Scheme Type | Example Palettes |
|----------|------|-------------|------------------|
| Land use categories | Categorical | Qualitative | Set2, Paired |
| Population density | Numeric, sequential | Sequential | YlOrRd, Blues |
| Income levels | Numeric, sequential | Sequential | Greens, PuBu |
| Temperature change | Diverging from 0 | Diverging | RdBu, coolwarm |
| Election results | Two categories | Diverging | RdBu (red/blue) |
| Elevation/terrain | Continuous | Sequential | terrain, dem |
| NDVI (vegetation) | -1 to +1 | Diverging | RdYlGn |

## Saving Layer Styles

Once you've perfected a symbology:

1. Right-click layer → **Export** → **Save as QGIS Layer Style File**
2. Save as `.qml` file
3. Reapply anytime: Right-click → **Styles** → **Load Style**

This saves colors, classification, labels—everything.

## Resources

- [ColorBrewer 2.0](https://colorbrewer2.org/) - Research-backed color schemes
- [Coolors](https://coolors.co/) - Palette generator
- [Adobe Color](https://color.adobe.com/) - Color wheel and harmony rules
- [Color Oracle](https://colororacle.org/) - Color blindness simulator (desktop app)
- [Coblis](https://www.color-blindness.com/coblis-color-blindness-simulator/) - Online color blindness simulator
