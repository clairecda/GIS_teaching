# Accessibility Checklist

Use this checklist to audit your maps for accessibility compliance. Complete this for each map you create.

---

## Map Information

**Map title:** _______________________________________________

**Date audited:** _______________________________________________

**Auditor:** _______________________________________________

---

## 1. Color Contrast

Test all text-background combinations using [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/).

| Text Element | Foreground | Background | Ratio | Pass AA? |
|--------------|------------|------------|-------|----------|
| Title | | | | [ ] Yes [ ] No |
| Subtitle | | | | [ ] Yes [ ] No |
| Legend text | | | | [ ] Yes [ ] No |
| Scale bar text | | | | [ ] Yes [ ] No |
| Map labels (example 1) | | | | [ ] Yes [ ] No |
| Map labels (example 2) | | | | [ ] Yes [ ] No |
| Annotations | | | | [ ] Yes [ ] No |
| Data source text | | | | [ ] Yes [ ] No |

**WCAG Standards:**

- **AA (minimum):** 4.5:1 for normal text, 3:1 for large text (18pt+ or 14pt bold)
- **AAA (enhanced):** 7:1 for normal text, 4.5:1 for large text

**Notes on contrast issues found:**

_______________________________________________

---

## 2. Color Vision Deficiency Testing

Test your map using [Color Oracle](https://colororacle.org/) (desktop) or [Coblis](https://www.color-blindness.com/coblis-color-blindness-simulator/) (web).

| Simulation | All categories distinguishable? | Hierarchy preserved? | Notes |
|------------|--------------------------------|---------------------|-------|
| Deuteranopia (red-green, common) | [ ] Yes [ ] No | [ ] Yes [ ] No | |
| Protanopia (red-green) | [ ] Yes [ ] No | [ ] Yes [ ] No | |
| Tritanopia (blue-yellow, rare) | [ ] Yes [ ] No | [ ] Yes [ ] No | |

**If categories become indistinguishable, consider:**

- [ ] Adjust color ramp (use colorblind-safe palettes from ColorBrewer)
- [ ] Add patterns or textures to differentiate categories
- [ ] Increase value (lightness) differences between adjacent categories
- [ ] Add labels directly to features

---

## 3. Typography

| Requirement | Status | Notes |
|-------------|--------|-------|
| **Minimum size (print):** 9pt | [ ] Pass [ ] Fail | |
| **Minimum size (digital):** 12pt | [ ] Pass [ ] Fail | |
| **Font family:** Sans-serif for data labels | [ ] Yes [ ] No | Font used: ___________ |
| **No overlapping labels** | [ ] Pass [ ] Fail | |
| **Text buffers/halos used where needed** | [ ] Yes [ ] N/A | |
| **Consistent font hierarchy** (title > subtitle > labels) | [ ] Pass [ ] Fail | |

---

## 4. Map Elements

All four core elements are **required** on every map.

| Element | Present? | Accessible? | Notes |
|---------|----------|-------------|-------|
| Title | [ ] Yes [ ] No | [ ] Yes [ ] No | Clear and descriptive? |
| Legend | [ ] Yes [ ] No | [ ] Yes [ ] No | All categories explained? |
| Scale bar | [ ] Yes [ ] No | [ ] Yes [ ] No | Readable units? |
| North arrow | [ ] Yes [ ] No | [ ] Yes [ ] No | Visible and correctly oriented? |
| Data sources | [ ] Yes [ ] No | [ ] Yes [ ] No | All sources credited? |
| Date/author | [ ] Yes [ ] No | [ ] Yes [ ] No | Attribution present? |

---

## 5. Alt Text (for Digital Publication)

Write a 1-2 sentence description capturing the map's key message.

**Format:** [Map type] + [Topic] + [Key finding]

**Example:** "Choropleth map of healthcare accessibility in rural NSW showing 15-minute drive-time service areas, revealing significant gaps in western regions where 23% of high-need populations live beyond acceptable access thresholds."

**Your alt text:**

_______________________________________________

_______________________________________________

_______________________________________________

---

## 6. Overall Assessment

| Category | Score (1-4) |
|----------|-------------|
| Color contrast | |
| Colorblind safety | |
| Typography | |
| Map elements | |
| **Total** | **/16** |

**Scoring:**

- 4 = Fully accessible, no issues
- 3 = Minor issues, easily fixed
- 2 = Notable issues requiring attention
- 1 = Major barriers, significant revision needed

---

## Action Items

List specific changes needed to improve accessibility:

1. _______________________________________________

2. _______________________________________________

3. _______________________________________________

4. _______________________________________________

---

## Resources

- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Color Oracle](https://colororacle.org/) (desktop color blindness simulator)
- [Coblis](https://www.color-blindness.com/coblis-color-blindness-simulator/) (web-based simulator)
- [ColorBrewer](https://colorbrewer2.org/) (colorblind-safe palettes)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Accessible Maps Best Practices (W3C)](https://www.w3.org/WAI/tutorials/images/complex/)
