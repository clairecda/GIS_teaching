# Project Checklist

Use this checklist throughout your GIS projects. Print it out or keep it open as you work.

---

## Before You Start

### Planning
- [ ] Research question or objective is clearly defined
- [ ] Study area boundaries identified
- [ ] Required datasets listed with sources
- [ ] Appropriate CRS selected for your region
- [ ] Project timeline realistic for available time

### Workspace Setup
- [ ] Using the week-based folder structure:
  ```
  intro-gis/
  └── capstone/
      ├── data/
      │   ├── raw/        ← Original downloads (never edit!)
      │   └── processed/  ← Your cleaned/modified data
      ├── capstone.qgz    ← QGIS project file
      ├── notebooks/      ← Python analysis
      └── exports/        ← Your final maps
  ```
- [ ] Data sources bookmarked or documented
- [ ] Backup location identified (cloud/USB)

---

## Data Management

### Acquiring Data
- [ ] Downloaded from authoritative sources
- [ ] Checked licensing allows your intended use
- [ ] Recorded download date and version
- [ ] Saved to `data/raw/` folder (untouched originals)
- [ ] Created README noting source URLs

### Organizing Data
- [ ] File names are lowercase, no spaces (use underscores)
- [ ] File names include date or version where relevant
- [ ] Related files kept together (shapefile components)
- [ ] Processed data saved separately from raw data
- [ ] Large unused files removed to save space

### Data Quality
- [ ] Checked for missing values or NULL geometries
- [ ] Verified CRS matches project requirements
- [ ] Confirmed attribute fields contain expected values
- [ ] Checked for obvious errors (negative populations, etc.)
- [ ] Documented any cleaning steps performed

---

## QGIS Project

### Project Setup
- [ ] Saved as `.qgz` in your week or capstone folder
- [ ] "Save paths: Relative" enabled (Project → Properties → General)
- [ ] Project CRS set appropriately for study area
- [ ] Project title filled in (Project → Properties → General)

### Layer Management
- [ ] Layer names are clear and descriptive (renamed from defaults)
- [ ] Layers organized in logical groups
- [ ] Unused layers removed from project
- [ ] Layer order makes sense (points on top, polygons below)
- [ ] All layers display without errors

### Styling & Symbology
- [ ] Colors chosen with purpose (not random defaults)
- [ ] Color ramp appropriate for data type:
  - Sequential for ordered data (light→dark)
  - Diverging for data with meaningful middle
  - Qualitative for categories
- [ ] Classification method documented (equal interval, quantiles, etc.)
- [ ] Number of classes appropriate (usually 4-7)
- [ ] Tested with colorblind simulator

---

## Map Design

### Essential Elements
- [ ] **Title**: Specific, includes What + Where + When
- [ ] **Legend**: All symbols explained, units shown
- [ ] **Scale bar**: Appropriate units, reasonable size
- [ ] **North arrow**: Included if map orientation unclear
- [ ] **Data sources**: All datasets credited
- [ ] **Author & date**: Your name and creation date

### Visual Quality
- [ ] Clear visual hierarchy (title largest, important features prominent)
- [ ] Text readable at intended viewing size
- [ ] Consistent fonts (max 2 font families)
- [ ] White space used effectively
- [ ] No overlapping labels
- [ ] Borders and frames consistent

### Layout Polish
- [ ] All elements aligned properly
- [ ] Margins consistent around edges
- [ ] Legend doesn't obscure important map areas
- [ ] Inset/locator map included if helpful
- [ ] Color palette harmonious

---

## Accessibility

### Color & Contrast
- [ ] Text contrast ratio ≥4.5:1 (use [WebAIM checker](https://webaim.org/resources/contrastchecker/))
- [ ] Tested with [Color Oracle](https://colororacle.org/) for colorblind accessibility
- [ ] Categories distinguishable without relying solely on color
- [ ] Avoided red/green combinations for critical distinctions

### Typography
- [ ] Minimum 9pt for print, 12pt for digital display
- [ ] Sans-serif fonts for labels (Arial, Open Sans, etc.)
- [ ] Sufficient spacing between labels
- [ ] Text buffers/halos improve readability on busy backgrounds

### Digital Distribution
- [ ] Alt text prepared describing the map
- [ ] High contrast version available if needed
- [ ] PDF tagged for accessibility (if submitting PDF)

---

## Analysis Quality

### Methodology
- [ ] Methods appropriate for research question
- [ ] Analysis steps documented and reproducible
- [ ] Parameters and thresholds justified
- [ ] Intermediate outputs spot-checked for errors
- [ ] Results make logical sense

### Interpretation
- [ ] Key patterns identified and described
- [ ] Findings connected back to research question
- [ ] Limitations honestly acknowledged
- [ ] Alternative explanations considered
- [ ] Conclusions proportional to evidence

### Spatial Statistics (if applicable)
If your project involves regression or statistical analysis:

- [ ] Checked for spatial autocorrelation using Moran's I
- [ ] If Moran's I significant, used spatial regression instead of OLS
- [ ] Chose appropriate spatial model (lag vs error) with justification
- [ ] Checked residuals for remaining spatial autocorrelation
- [ ] Interpreted coefficients correctly (with uncertainty)
- [ ] Reported model diagnostics (R², AIC, p-values)

**Resources:** [Spatial Statistics reading](../readings/spatial-statistics.md) | [Spatial Statistics notebook](notebooks.md)

---

## Export & Submission

### File Preparation
- [ ] Exported at correct resolution:
  - Print: 300 DPI minimum
  - Web/presentation: 150 DPI or 1920×1080px
  - Social media: Platform-specific dimensions
- [ ] Correct format:
  - PDF for print/archival
  - PNG for web (supports transparency)
  - JPG for photos/smaller files
- [ ] File size reasonable for submission method
- [ ] Test-opened file to verify it looks correct

### Final Checks
- [ ] Opened project fresh to verify layers load
- [ ] Viewed export at 100% zoom—is everything readable?
- [ ] Spell-checked all text elements
- [ ] Verified all required components included
- [ ] File named according to submission guidelines

---

## Documentation

### For Your Records
- [ ] Research question clearly stated
- [ ] Data sources documented with URLs and dates
- [ ] Methods described step-by-step
- [ ] Key findings summarized (2-4 bullet points)
- [ ] Limitations noted
- [ ] Reflection completed

### For Reproducibility
- [ ] Someone else could recreate your analysis from notes
- [ ] All files organized with clear names
- [ ] README file explains folder contents
- [ ] Processing steps documented in order

---

## Common Mistakes to Avoid

| Mistake | How to Fix |
|---------|------------|
| Missing scale bar | Always include—Layout → Add Scale Bar |
| Legend doesn't match map | Regenerate legend after symbology changes |
| Unreadable text | Increase font size, add text buffer |
| No data sources | Credit every dataset in the map margin |
| Broken layer paths | Use relative paths, keep folder structure |
| Wrong file version | Include date/version in filename |
| Cluttered map | Simplify—remove unnecessary elements |
| Poor color choices | Use ColorBrewer, test for accessibility |
| CRS mismatch | Set project CRS, reproject layers if needed |
| Missing metadata | Document source, date, license for all data |

---

## Quick Reference: Keyboard Shortcuts

| Action | Windows/Linux | macOS |
|--------|--------------|-------|
| Save project | Ctrl+S | Cmd+S |
| Undo | Ctrl+Z | Cmd+Z |
| Pan map | Hold Space + drag | Hold Space + drag |
| Zoom in/out | Scroll wheel | Scroll wheel |
| Select features | Click or drag box | Click or drag box |
| Open attribute table | F6 | F6 |
| Identify features | Ctrl+Shift+I | Cmd+Shift+I |

---

## Submission Checklist

Final verification before you submit:

- [ ] All required files present
- [ ] Files named correctly per guidelines
- [ ] Project/maps open without errors
- [ ] Exports are readable and complete
- [ ] Documentation/reflection included
- [ ] Submitted to correct location
- [ ] Backup copy saved for yourself

**You're ready to submit!**
