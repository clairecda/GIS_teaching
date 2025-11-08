# Licensing

This course uses a dual-licensing approach to make materials as useful and reusable as possible. Understanding how these licenses work will help you properly attribute course materials and license your own work.

## Overview: Two Licenses for Different Components

This course repository contains two types of materials, each with its own license:

### Code: MIT License

All Jupyter notebooks, Python scripts, utility functions, and code examples are released under the **MIT License**. This is a permissive open-source license that lets you use, modify, and redistribute the code with very few restrictions.

**What's covered:**
- Jupyter notebooks (`.ipynb` files)
- Python scripts (`.py` files)
- Code snippets and examples
- Analysis workflows and automation scripts

**Full license text:** See `LICENSE` in the repository root

**Link:** <https://opensource.org/license/mit/>

### Content: Creative Commons Attribution 4.0 (CC BY 4.0)

All course content—including lecture notes, lab guides, slides, written documentation, images, maps, and other teaching materials—are released under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

**What's covered:**
- Lecture notes and lab guides
- Slide decks and presentations
- Written documentation and tutorials
- Maps, charts, and visualizations
- Images and diagrams (created by the course authors)
- Video transcripts and captions

**Full license text:** See `CONTENT_LICENSE.md` in the repository root

**Link:** <https://creativecommons.org/licenses/by/4.0/>

### Data: Various Licenses

The course uses third-party datasets from multiple sources, each with its own license. Most are openly licensed (CC BY 4.0, public domain, or Open Data Commons), but always check before redistributing.

**Where to find license information:**
- See the [Data Inventory](data-inventory.md) for a complete list of datasets, sources, and licenses
- Each dataset entry includes licensing details and usage notes
- Always verify current license terms when downloading data

## How to Attribute Course Materials

If you use materials from this course, here's how to give proper attribution:

### For Students: Using Materials in Your Projects

**If you adapt code from the course:**

```
Code adapted from Introduction to GIS course notebooks
© 2025 Claire Boulange
Licensed under MIT License
https://github.com/[repository-url]
```

You can also use a shorter version in comments:

```python
# Adapted from intro-to-gis course (MIT License)
# Original: https://github.com/[repository-url]
```

**If you include maps or visualizations from the course:**

Include attribution in the map footer, caption, or figure notes:

```
Map design based on Introduction to GIS course materials
© 2025 Claire Boulange, CC BY 4.0
Data: [list your data sources with their licenses]
```

**If you quote or adapt written content:**

```
Content adapted from Introduction to GIS course materials
© 2025 Claire Boulange, licensed under CC BY 4.0
Available at: https://github.com/[repository-url]
```

### For Instructors: Adapting the Course

**If you teach a course based on these materials:**

You're welcome to use and adapt these materials! Here's how to attribute:

**In your syllabus or course website:**

```
This course is based on Introduction to GIS course materials by Claire Boulange,
licensed under CC BY 4.0. Materials have been adapted for [your institution/context].
Original course: https://github.com/[repository-url]
```

**In slide decks:**

Include an attribution slide at the beginning or end:

```
Course Materials Attribution
─────────────────────────────
Based on: Introduction to GIS course materials
Author: Claire Boulange
License: CC BY 4.0 (content), MIT License (code)
Adaptations: [describe your changes]
Available at: https://github.com/[repository-url]
```

**If you significantly remix the materials:**

You can note your adaptations while still attributing the original:

```
Adapted from Introduction to GIS course materials © 2025 Claire Boulange (CC BY 4.0)
by [Your Name], [Year]
Available at: [your repository URL]
```

### For Researchers: Citing in Publications

If you reference these materials in academic work:

```
Boulange, C. (2025). Introduction to GIS [Course materials].
GitHub repository. https://github.com/[repository-url]
```

## Attribution Examples by Material Type

### Example 1: Student Lab Report with Course Map

**Map footer text:**
```
Data: ABS ASGS 2021, SEIFA 2021 (CC BY 4.0)
Map design adapted from Introduction to GIS course materials
© 2025 Claire Boulange, CC BY 4.0
```

### Example 2: Code Notebook Adapted from Course

**First markdown cell:**
```markdown
# Spatial Analysis Workflow

This notebook adapts code from the Introduction to GIS course
(© 2025 Claire Boulange, MIT License).

Original materials: https://github.com/[repository-url]
Adaptations: [describe your changes]
```

### Example 3: Presentation Using Course Slides

**Attribution slide:**
```
Materials Attribution
─────────────────────
Slides 3-8 adapted from Introduction to GIS course materials
© 2025 Claire Boulange, CC BY 4.0

Data sources:
• ABS SEIFA 2021 (CC BY 4.0)
• NSW Recorded Crime Statistics (CC BY 4.0)
• Natural Earth (public domain)
```

### Example 4: Blog Post Using Course Concepts

**Footer or attribution section:**
```
This tutorial is based on concepts from the Introduction to GIS course
by Claire Boulange (CC BY 4.0). Code examples have been adapted for
web mapping applications.
```

## How to License Your Own Work

When creating your own GIS projects, you'll need to choose licenses too. Here are some guidelines:

### If You Create Original Maps or Analyses

**Recommended approach:**
- License your code under MIT (or another permissive license)
- License your written content and visualizations under CC BY 4.0
- Document all data sources with their licenses

**Example attribution for your work:**
```
Melbourne Bike Infrastructure Analysis
© 2025 [Your Name], CC BY 4.0

Code: MIT License
Data: City of Melbourne Open Data (CC BY 4.0)
      OpenStreetMap (ODbL)
```

### If You Combine Course Materials with Your Own Work

You can create derivative works that combine course materials with your additions:

```
Urban Heat Island Analysis for Sydney
Based on Introduction to GIS course materials © 2025 Claire Boulange (CC BY 4.0)
Extended analysis and additional data © 2025 [Your Name] (CC BY 4.0)

Data sources:
• NASA SRTM DEM (public domain)
• ABS ASGS boundaries (CC BY 4.0)
• [Your additional data sources]
```

### What About Data You Use?

**Key principle:** Data licenses are independent of code and content licenses.

- Always preserve the original data license
- Include proper attribution for all datasets
- Document data sources in your README and map outputs
- See the [Data Inventory](data-inventory.md) for examples of how to document data sources

**Example data attribution in README:**
```markdown
## Data Sources

| Dataset | Source | License | Access Date |
|---------|--------|---------|-------------|
| ABS SA2 Boundaries | Australian Bureau of Statistics | CC BY 4.0 | 2025-01-15 |
| SEIFA 2021 | Australian Bureau of Statistics | CC BY 4.0 | 2025-01-15 |
| Natural Earth Admin Boundaries | Natural Earth | Public domain | 2025-01-10 |
```

## Understanding License Requirements

### MIT License Summary

**You CAN:**
- Use the code commercially
- Modify the code
- Distribute copies
- Sublicense the code
- Use it privately

**You MUST:**
- Include the original MIT license text
- Include the copyright notice

**You CANNOT:**
- Hold the author liable

### CC BY 4.0 Summary

**You CAN:**
- Share (copy and redistribute)
- Adapt (remix, transform, build upon)
- Use commercially

**You MUST:**
- Give appropriate credit (attribution)
- Link to the license
- Indicate if you made changes
- Not suggest the licensor endorses you

**You CANNOT:**
- Apply additional restrictions
- Use technological measures to prevent others from doing what the license allows

## Frequently Asked Questions

### Can I use course materials for my capstone project?

Yes! You can use code, adapt examples, and build on concepts from the course. Make sure to:
- Attribute any code you adapt (MIT License)
- Attribute any maps or written content you reuse (CC BY 4.0)
- Add your own analysis and insights
- Document your data sources separately

### Do I need permission to use course materials?

No permission needed! Both licenses are permissive. Just provide proper attribution as described above.

### Can I use course materials in a commercial project?

Yes, both MIT and CC BY 4.0 allow commercial use. Just maintain proper attribution.

### What if I only use a small snippet of code?

Even small snippets should include a brief attribution comment. For example:

```python
# Buffer function adapted from intro-to-gis course (MIT License)
def create_buffer(gdf, distance):
    return gdf.buffer(distance)
```

### Can I translate the course materials?

Yes! CC BY 4.0 explicitly allows for translation. Include attribution and note that you created the translation:

```
Introduction to GIS course materials
© 2025 Claire Boulange, CC BY 4.0
Translated to [language] by [Your Name], [Year]
```

### What if I find an error and fix it?

Please contribute back! You can:
- Submit a pull request to the original repository
- Or document your fixes with attribution if you're maintaining a fork

### How do I attribute multiple data sources?

List each source separately with its license. For example:

**In a map footer:**
```
Data: ABS ASGS 2021 (CC BY 4.0) | Natural Earth (public domain) |
OpenStreetMap (ODbL) | Map design © 2025 [Your Name]
```

**In a README:**
```markdown
## Data Attribution

- ABS ASGS Edition 3 SA2 boundaries © Australian Bureau of Statistics, CC BY 4.0
- ABS SEIFA 2021 © Australian Bureau of Statistics, CC BY 4.0
- Natural Earth Admin Boundaries (public domain)
- OpenStreetMap data © OpenStreetMap contributors, ODbL
```

### Can I remove the attribution from my maps?

No—both CC BY 4.0 and individual data licenses require attribution. Design your map layout to include this information professionally (typically in a footer or text block).

### What about screenshots or screen recordings?

If you create tutorials that show the course materials:
- Attribute the original materials in your video description or accompanying text
- Note that you're demonstrating the course content
- Link to the original repository

### Do I need to license my student assignments?

You own your work and can choose any license (or no license). However, if you build on course materials, you should attribute them regardless of what license you choose for your additions.

### What if I want to use stricter licensing?

While you can license your original contributions under stricter terms, you cannot add restrictions to the course materials themselves—the CC BY 4.0 license prohibits this. Your new work can be more restrictive, but the course materials must remain under their original licenses.

## Quick Reference

### Common Scenarios

| What you're doing | How to attribute |
|-------------------|------------------|
| Using code from a notebook | Include copyright notice and MIT License reference in comments or README |
| Adapting a course map design | Include "Map design adapted from Introduction to GIS course materials © 2025 Claire Boulange, CC BY 4.0" in map footer |
| Teaching with course slides | Add attribution slide citing original course, author, and license |
| Quoting lab instructions | Use quotation marks and cite "Introduction to GIS course materials © 2025 Claire Boulange, CC BY 4.0" |
| Building on course concepts | Brief acknowledgment in README or documentation |
| Using course datasets | Attribute the original data source (see [Data Inventory](data-inventory.md)), not the course |

### Attribution Templates

**Minimal code attribution:**
```python
# © 2025 Claire Boulange, MIT License
# https://github.com/[repository-url]
```

**Minimal content attribution:**
```
© 2025 Claire Boulange, CC BY 4.0
```

**Full attribution:**
```
Introduction to GIS course materials
© 2025 Claire Boulange
Code: MIT License | Content: CC BY 4.0
https://github.com/[repository-url]
```

## Resources and Further Reading

### License Texts
- **MIT License:** <https://opensource.org/license/mit/>
- **CC BY 4.0 Legal Code:** <https://creativecommons.org/licenses/by/4.0/legalcode>
- **CC BY 4.0 Summary:** <https://creativecommons.org/licenses/by/4.0/>

### Best Practices
- **Creative Commons Best Practices for Attribution:** <https://wiki.creativecommons.org/wiki/Best_practices_for_attribution>
- **Open Source Initiative:** <https://opensource.org/>
- **Choose an Open Source License:** <https://choosealicense.com/>

### Data Licensing
- **Open Data Commons:** <https://opendatacommons.org/>
- **Australian Government Intellectual Property Rules:** <https://www.ag.gov.au/rights-and-protections/intellectual-property>
- **Understanding Open Data Licenses:** <https://theodi.org/article/publishers-guide-to-open-data-licensing/>

## Contact and Contributions

If you have questions about licensing or attribution that aren't answered here, please open an issue in the course repository. We're happy to provide clarification and will update this guide based on common questions.

When contributing to this course, you agree to license your contributions under the same terms (MIT for code, CC BY 4.0 for content).
