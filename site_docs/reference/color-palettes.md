# Color Palettes Reference

Consistent, accessible colors make your maps professional and readable. This guide covers creating palettes in QGIS and choosing colors for different map types.

## Course Color Palette

Use these colors as your baseline throughout the course:

| Color | Hex | RGB | Use for |
|-------|-----|-----|---------|
| ![#0d7377](https://via.placeholder.com/20/0d7377/0d7377.png) Deep Teal | `#0d7377` | 13, 115, 119 | Water, ocean, primary accent |
| ![#2e7d32](https://via.placeholder.com/20/2e7d32/2e7d32.png) Forest Green | `#2e7d32` | 46, 125, 50 | Vegetation, parks, forests |
| ![#e65100](https://via.placeholder.com/20/e65100/e65100.png) Warm Orange | `#e65100` | 230, 81, 0 | Points of interest, highlights |
| ![#455a64](https://via.placeholder.com/20/455a64/455a64.png) Slate Grey | `#455a64` | 69, 90, 100 | Urban areas, boundaries |
| ![#d4a574](https://via.placeholder.com/20/d4a574/d4a574.png) Sand | `#d4a574` | 212, 165, 116 | Desert, bare ground |
| ![#4fc3f7](https://via.placeholder.com/20/4fc3f7/4fc3f7.png) Light Blue | `#4fc3f7` | 79, 195, 247 | Rivers, streams |
| ![#8d6e63](https://via.placeholder.com/20/8d6e63/8d6e63.png) Brown | `#8d6e63` | 141, 110, 99 | Roads, built-up areas |
| ![#7cb342](https://via.placeholder.com/20/7cb342/7cb342.png) Lime Green | `#7cb342` | 124, 179, 66 | Agriculture, grassland |

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
