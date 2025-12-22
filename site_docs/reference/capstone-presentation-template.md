# Capstone Presentation Template

Use this structure for your 8-10 minute capstone presentation. Each section includes guidance on content and timing.

---

## Slide 1: Title Slide (15 seconds)

**Include:**

- Project title (clear and descriptive)
- Your name
- Date
- Course name (optional)

**Example:**

> **Transit Deserts: Mapping Public Transport Access Gaps in Western Sydney**
>
> Jane Smith | December 2024 | Introduction to GIS

---

## Slide 2: The Hook (30-45 seconds)

**Purpose:** Grab attention and establish why this matters.

**Include ONE of these approaches:**

- A compelling statistic ("1 in 5 residents in my study area can't reach a hospital within 30 minutes")
- A question ("What if the bus never came to your neighborhood?")
- A personal connection ("When I moved to [area], I noticed...")
- A real-world impact ("This analysis could help planners prioritize...")

**Avoid:**

- Starting with "My project is about..."
- Technical jargon
- Long background paragraphs

---

## Slide 3: Research Question (45-60 seconds)

**Include:**

- One clear, focused research question
- Study area with location map
- Why this question matters (1-2 sentences)

**Format:**

> **Research Question:**
> [Your question here]
>
> **Study Area:**
> [Map showing geographic scope]
>
> **Why it matters:**
> [Brief justification]

---

## Slide 4: Data Sources (60-90 seconds)

**Include:**

- List of key datasets (3-5 maximum)
- Source and date for each
- Brief note on data quality or limitations

**Format as table or bullet list:**

| Dataset | Source | Year |
|---------|--------|------|
| Census population | ABS | 2021 |
| Road network | OpenStreetMap | 2024 |
| Hospital locations | NSW Health | 2023 |

**Mention any data challenges:**

- "The hospital data didn't include opening hours, so I assumed 24/7 access"
- "OSM road data may be incomplete in rural areas"

---

## Slide 5: Methods Overview (90-120 seconds)

**Include:**

- Workflow diagram OR numbered steps
- Key techniques used (name them)
- Software/tools used

**Format option 1 - Workflow diagram:**

```
[Census Data] → [Spatial Join] → [Buffer Analysis] → [Population Count] → [Map Output]
```

**Format option 2 - Numbered steps:**

1. Downloaded and cleaned census data
2. Created 15-minute drive-time service areas around hospitals
3. Joined population data to identify underserved areas
4. Calculated statistics by demographic group

**Keep it high-level:** Don't explain every click in QGIS.

---

## Slides 6-8: Key Findings (3-4 minutes total)

**Structure:** One major finding per slide.

**Each slide should include:**

- A map or visualization
- A clear headline stating the finding
- 1-2 bullet points of supporting evidence

**Example slide:**

> **Finding 1: Western suburbs have poorest hospital access**
>
> [Map showing service areas and gap zones]
>
> - 23% of residents in highlighted areas beyond 30-minute threshold
> - Three LGAs particularly affected: [names]

**Tips:**

- Let the map do the talking; don't crowd with text
- Use annotations/arrows to highlight key patterns
- Ensure all maps have titles, legends, and scale bars

---

## Slide 9: Limitations & Next Steps (60-90 seconds)

**Include:**

**Limitations (be honest):**

- Data gaps or quality issues
- Assumptions you made
- What the analysis couldn't capture

**Next steps (if you had more time):**

- Additional analyses you'd run
- Data you'd collect
- How findings could be applied

**Example:**

> **Limitations:**
>
> - Used straight-line distance; road network would be more accurate
> - Data from 2021 may not reflect recent population changes
>
> **Next steps:**
>
> - Incorporate public transit travel times
> - Extend analysis to regional NSW
> - Share findings with local health planning committee

---

## Slide 10: Conclusion & Questions (30 seconds + Q&A)

**Include:**

- One-sentence summary of main finding
- Thank you
- Your contact info (optional: email, LinkedIn, GitHub)
- "Questions?" prompt

**Example:**

> **Key takeaway:** 23% of Western Sydney residents face significant barriers to hospital access, with low-income areas disproportionately affected.
>
> Thank you!
>
> Questions?
>
> jane.smith@email.com

---

## Presentation Checklist

### Content

- [ ] Hook grabs attention in first 30 seconds
- [ ] Research question is clear and specific
- [ ] All data sources are credited
- [ ] Methods are explained at appropriate level (not too technical)
- [ ] Findings are clearly stated with supporting evidence
- [ ] Limitations are honestly acknowledged
- [ ] Conclusion summarizes the key takeaway

### Visuals

- [ ] All maps have titles, legends, scale bars
- [ ] Text is readable from back of room (minimum 24pt)
- [ ] No more than 5-6 bullet points per slide
- [ ] Consistent color scheme and fonts throughout
- [ ] High-resolution map exports (no pixelation)

### Delivery

- [ ] Practiced timing (8-10 minutes)
- [ ] Prepared for likely questions
- [ ] Backup plan if technology fails (PDF copy)
- [ ] Tested screen sharing/projector

---

## Timing Guide

| Section | Time | Cumulative |
|---------|------|------------|
| Title + Hook | 0:45 | 0:45 |
| Research Question | 0:45 | 1:30 |
| Data Sources | 1:00 | 2:30 |
| Methods | 1:30 | 4:00 |
| Findings (3 slides) | 3:30 | 7:30 |
| Limitations + Next Steps | 1:00 | 8:30 |
| Conclusion | 0:30 | 9:00 |
| **Buffer for Q&A** | 1:00+ | 10:00+ |

---

## Common Presentation Mistakes

1. **Reading slides verbatim** - Use slides as prompts, not scripts
2. **Too much text** - If you can't read it in 3 seconds, it's too much
3. **Unexplained maps** - Walk the audience through what they're seeing
4. **Rushed endings** - Save time for limitations and conclusions
5. **No backup plan** - Always have a PDF copy on USB drive
6. **Ignoring time limits** - Practice with a timer; respect your peers' time

---

## Questions to Prepare For

Anticipate these common questions:

- "Why did you choose this study area?"
- "How did you handle [specific data challenge]?"
- "What would you do differently if you started over?"
- "How could this analysis be applied in practice?"
- "Did you find anything that surprised you?"
- "What additional data would improve the analysis?"

Good luck with your presentation!
