# Week 11 · Design & Storytelling Studio

Your technical skills are strong, but a powerful analysis means nothing if no one understands your map. This week is dedicated to refining your cartographic communication through design critique, accessibility audits, and narrative framing. You'll gather feedback from peers, apply professional accessibility standards, and craft the supporting text that transforms data into insight. Think of this as your design intensive—a week to polish the maps you've created and prepare for your capstone presentation. Great design is iterative, and you'll practice the cycle of create-critique-revise that defines professional cartographic work.

## What you'll learn

By the end of this week, you'll be able to:

1. Facilitate and participate in constructive design critique sessions using a structured rubric.
2. Audit maps for accessibility compliance (WCAG color contrast, typography, screen reader compatibility).
3. Write effective map titles, annotations, and supporting narratives that clarify rather than clutter.
4. Scope a realistic capstone project with clear objectives, data sources, and deliverables.

## Before you start

- [ ] Gather 2-3 maps you've created in previous weeks (layouts from Weeks 2, 5, 6, or recent work)
- [ ] Export these maps as PDFs for peer review
- [ ] Review the lecture: [Week 11 · Narrative Map Design](../lectures/week11-storytelling.md)
- [ ] Install a color blindness simulator tool: [Color Oracle](https://colororacle.org/) (desktop) or bookmark [Coblis](https://www.color-blindness.com/coblis-color-blindness-simulator/)
- [ ] Download the [Design Critique Rubric](../reference/design-rubric.md) and [Accessibility Checklist](../reference/accessibility-checklist.md)
- [ ] Start brainstorming capstone project ideas—what spatial question do you want to answer?

## This week's activities

### Activity 1: Design critique workshop

Effective critique focuses on goals and outcomes, not personal taste. You'll practice giving and receiving structured feedback using a professional rubric.

**Steps:**

1. **Set up the critique** (small groups of 3-4 work best):
   - Each person shares 1-2 maps (printed or screen-shared)
   - Presenter briefly explains: What's the intended message? Who's the audience?
2. **Use the critique rubric** to evaluate each map across four dimensions:
   - **Clarity:** Can you understand the main message in 5 seconds?
   - **Hierarchy:** Does the visual organization guide your eye appropriately?
   - **Accuracy:** Are labels correct? Is the scale bar accurate? Are projections appropriate?
   - **Accessibility:** Can this be read by people with color vision deficiencies or low vision?
3. **Give feedback using this format:**
   - "What works: [specific positive element]"
   - "What could be stronger: [specific issue]"
   - "Suggestion: [actionable improvement]"
4. **Document feedback** you receive—take notes or screenshots of marked-up maps
5. Each person should receive feedback on at least 2 different maps

!!! tip "Critique is not criticism"
    Good critique helps the designer achieve their goals. Focus on whether the map communicates its intended message effectively, not whether you would have made different aesthetic choices.

**Example feedback:**

- "What works: The color palette is colorblind-safe and creates clear distinction between categories."
- "What could be stronger: The title is too technical—audience may not know what 'SEIFA decile quintiles' means."
- "Suggestion: Change title to 'Areas of Economic Disadvantage in Melbourne' and add a subtitle explaining the index."

### Activity 2: Accessibility audit

Accessible maps reach wider audiences and meet professional standards. You'll systematically check your maps against WCAG (Web Content Accessibility Guidelines) criteria.

**Steps:**

1. **Check color contrast** for all text elements:
   - Visit [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
   - Test each text-background combination (title on white, labels on map colors, etc.)
   - **Standard:** Text should meet WCAG AA (4.5:1 contrast) or ideally AAA (7:1 contrast)
   - If contrast fails, adjust text color, add text buffers/halos, or lighten/darken backgrounds
2. **Simulate color vision deficiencies:**
   - Open Color Oracle (or upload map to Coblis)
   - View your map through each filter: Deuteranopia, Protanopia, Tritanopia
   - Check: Can you still distinguish all categories? Does the hierarchy remain clear?
   - If categories become indistinguishable, adjust your color ramp or add patterns/textures
3. **Check typography:**
   - **Minimum sizes:** 9pt for print, 12pt for digital display
   - **Fonts:** Avoid decorative fonts for data labels; use sans-serif (Arial, Open Sans) for clarity
   - **Readability:** Ensure labels don't overlap; use text buffers to separate labels from background
4. **Write alt text** (for digital publication):
   - Draft a 1-2 sentence description capturing the map's key message
   - Format: "Map type + topic + key finding"
   - Example: "Choropleth map of healthcare accessibility in rural NSW showing 15-minute drive-time service areas, revealing significant gaps in western regions where 23% of high-need populations live beyond acceptable access thresholds."
5. Document your findings in the [Accessibility Checklist](../reference/accessibility-checklist.md)

!!! note "Accessibility is design quality"
    Accessible design isn't a constraint—it's good design. High contrast, readable fonts, and thoughtful color choices improve the experience for all users, not just those with disabilities.

### Activity 3: Narrative framing

The words on your map matter as much as the colors. You'll craft titles, annotations, and supporting text that guide interpretation.

**Steps:**

1. **Evaluate your current titles** using these questions:
   - Is it specific? (Avoid: "Population Map" → Prefer: "Population Density in Greater Sydney, 2021")
   - Does it indicate the message? (Consider adding interpretive elements: "Rapid Growth in Western Suburbs")
   - Is it jargon-free? (Replace technical terms with plain language)
2. **Write or revise map titles:**
   - **Formula:** [What] + [Where] + [When] + optional [Why/So What]
   - Test on a friend or classmate: Can they predict the map's content from the title alone?
3. **Add strategic annotations:**
   - Highlight 1-3 notable features (outliers, patterns, important locations)
   - Use arrows or callout lines sparingly
   - Keep annotation text brief (under 10 words per callout)
   - Example: "15% above regional average" with arrow to hotspot
4. **Draft supporting text** (if creating a report or web map):
   - **Context paragraph:** Why does this topic matter? What question are you answering?
   - **Method note:** What data did you use? What analysis techniques?
   - **Key findings:** 2-4 bullet points summarizing insights
   - **Limitations:** What caveats should readers know? What's uncertain?
5. **Test readability:**
   - Read your text aloud—does it sound natural?
   - Check reading level (aim for general audience, not academic specialists)
   - Remove unnecessary jargon or define it clearly

!!! warning "Over-annotation"
    Too many callouts create clutter. Prioritize ruthlessly—what absolutely needs to be highlighted? Everything else can go in a caption or supporting text.

### Activity 4: Layout refinement

Now apply the feedback you received. This is the iteration phase—where good maps become great.

**Steps:**

1. **Review critique notes** from Activity 1 and accessibility audit from Activity 2
2. **Prioritize revisions:**
   - Critical issues first (accessibility failures, inaccurate data, misleading classifications)
   - Then clarity improvements (better titles, adjusted colors, simplified legends)
   - Finally aesthetic polish (alignment, spacing, white space)
3. **Make revisions in QGIS:**
   - Update symbology if needed (new color ramps, pattern fills)
   - Edit labels (font changes, repositioning, buffer adjustments)
   - Adjust layout elements (title size, legend position, element alignment)
   - Add or refine annotations based on narrative choices from Activity 3
4. **Version control:**
   - Save revised layout with new name: `week11_revised_[mapname]`
   - Keep original for comparison
5. **Export updated versions** to `exports/week11/`
6. **Compare before/after:**
   - Place original and revised side-by-side
   - Document what changed and why in your reflection

!!! tip "Iteration is normal"
    Professional cartographers rarely get it right on the first try. This revision process is where learning happens—embrace it rather than seeing it as rework.

### Activity 5: Export best practices

Different outputs require different export settings. You'll learn when to use PNG vs PDF, how to set resolution, and how to handle licensing.

**Steps:**

1. **Understand export formats:**
   - **PNG/JPG:** For web, presentations, social media
     - Resolution: 300 DPI for high-quality, 150 DPI for web
     - PNG supports transparency; JPG creates smaller files
   - **PDF:** For print, reports, archival
     - Vector-based: stays crisp at any zoom level
     - Embeds fonts and preserves layout exactly
   - **SVG:** For web graphics that need to scale
     - Editable in design software (Illustrator, Inkscape)
     - Smaller file sizes than high-res PNG
2. **Export for different purposes:**
   - **Print:** PDF at actual size (A3, A4, etc.), 300 DPI for raster elements
   - **Web/presentation:** PNG 1920x1080px or 2560x1440px, 96-150 DPI
   - **Social media:** PNG 1200x630px (Twitter/Facebook card size)
3. **Configure export settings in QGIS:**
   - `Layout ▶ Export as Image...` or `Export as PDF...`
   - Check "Enable georeferencing" if you want to reimport map as georeferenced raster
   - For PDFs: Enable "Export RDF metadata" to embed licensing info
4. **Add licensing and attribution:**
   - Every export should include data sources
   - Add your name and year
   - Consider adding a license: "CC BY 4.0" allows reuse with attribution
   - Example footer: "Data: ABS 2021 Census, OSM | Map: [Your Name], 2024 | License: CC BY 4.0"
5. **Organize exports:**
   - Create subfolders: `exports/week11/print/`, `exports/week11/web/`
   - Use descriptive filenames: `accessibility_gaps_sydney_2024_web.png`
   - Keep a `README.txt` documenting what each file is for

!!! note "Archival formats"
    PDFs are best for long-term archival because they're self-contained (fonts embedded, exact layout preserved). PNGs can look different if fonts aren't installed on the viewing system.

### Activity 6: Capstone planning

Your capstone project will synthesize skills from across the course. This week you'll scope your project, identify data sources, and create a realistic timeline.

**Steps:**

1. **Choose a spatial question** you want to answer:
   - Should be personally meaningful or relevant to your community/field
   - Must be feasible with available data and your current skills
   - Examples:
     - "Where are the food access deserts in [my city]?"
     - "How has urban green space changed over the past decade?"
     - "Which neighborhoods have poor access to quality public transit?"
     - "What areas are most vulnerable to [climate hazard]?"
2. **Scope your project:**
   - **Study area:** Specific enough to be manageable (one city/region, not entire country)
   - **Time period:** Use recent, available data (avoid historical data that's hard to find)
   - **Methods:** Combine 2-3 techniques from the course (e.g., choropleth mapping + network analysis + hex binning)
3. **Identify data sources:**
   - Make a list of datasets you'll need (boundaries, points of interest, demographic data)
   - Verify they exist and are accessible (check download links)
   - Document: source, format, license, update frequency
   - Have a backup plan if primary data isn't available
4. **Draft a project outline:**
   - **Question/objective:** One clear sentence
   - **Background:** Why does this matter? (2-3 sentences)
   - **Data:** List of layers you'll use
   - **Methods:** What analysis will you perform?
   - **Expected output:** What will your final deliverable look like? (Map + report? Interactive web map? Presentation?)
   - **Timeline:** Week-by-week plan through Week 12
5. **Assess feasibility:**
   - Can you complete this in 2 weeks?
   - Do you have all required skills, or will you need to learn something new?
   - Is the scope too broad? (If yes, narrow your study area or simplify your question)
   - Is it too narrow? (If yes, add a comparison or expand the area)
6. **Get feedback:**
   - Share your outline with instructor or peers
   - Ask: Is this realistic? Is the question clear?
   - Revise based on feedback
7. **Document your plan:**
   - Save as `projects/capstone_proposal.txt` or `.md`
   - This becomes your roadmap for Week 12

!!! warning "Avoid scope creep"
    It's better to do one analysis really well than to attempt three analyses poorly. Choose depth over breadth. You can always note "future directions" for work beyond this course.

**Common capstone pitfalls to avoid:**

- Choosing a study area without available data
- Trying to learn a new tool (e.g., R, ArcGIS) during the capstone window
- Picking a politically sensitive topic without considering ethical implications
- Underestimating time required for data cleaning and troubleshooting

## Support materials

- Slides: [Week 11 lecture deck](../../assets/slides/week11.html)
- Lecture notes: [Narrative Map Design](../lectures/week11-storytelling.md)
- Rubric: [Design Critique Framework](../reference/design-rubric.md)
- Checklist: [Accessibility Standards](../reference/accessibility-checklist.md)
- Guide: [Writing Effective Map Titles](../reference/map-titles.md)
- Template: [Capstone Proposal Outline](../reference/capstone-template.md)
- Inspiration: [Example capstone projects from previous cohorts](../reference/capstone-examples.md)

## Reflect

Take 15-20 minutes to answer these questions in your [Week 11 reflection](../reference/reflections.md#week-11--design--storytelling):

- What was the most valuable piece of feedback you received during critique? How will you apply it?
- Which accessibility issue surprised you most when you audited your maps?
- Compare a map before and after revision—what specific changes made the biggest impact?
- What's the spatial question driving your capstone project? Why does it matter to you?
- What's your biggest concern or uncertainty about completing the capstone in Week 12?
- How has your understanding of "good map design" evolved since Week 1?

!!! tip "Capture your growth"
    Look back at your Week 1 map. What would you do differently now? Documenting your progress helps you recognize how much you've learned and builds confidence for the capstone ahead.

## What you'll submit

- [ ] At least one revised map showing improvements from peer critique (PDF or PNG with before/after comparison)
- [ ] Completed [Accessibility Checklist](../reference/accessibility-checklist.md) documenting audit results for 2+ maps
- [ ] Capstone proposal outline (1-2 pages) including question, data sources, methods, and timeline
- [ ] Your Week 11 reflection entry

## Coming up next week

Week 12 is your capstone showcase—the culmination of everything you've learned. You'll execute your project plan, create a polished final deliverable (map + supporting materials), and present your work to the group. This is your opportunity to demonstrate mastery, tell a compelling spatial story, and build a portfolio piece you're proud to share. Come prepared to troubleshoot, iterate quickly, and support your peers as they do the same. Make sure your capstone proposal is approved and your data is downloaded before Week 12 begins—you'll want to hit the ground running.
