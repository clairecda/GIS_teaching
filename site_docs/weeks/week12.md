# Week 12 · Capstone Showcase

You made it. Over the past 11 weeks, you've moved from navigating QGIS for the first time to conducting spatial analyses that combine multiple datasets, methods, and tools. This final week is your chance to present what you've learned—sharing your capstone project, organizing your work, and reflecting on how far you've come. This isn't just an ending—it's a starting point for continued GIS learning.

## What you'll learn

By the end of this week, you'll be able to:

1. Present your capstone project clearly, explaining your question, methods, and findings to a non-technical audience.
2. Organize your project files (data, maps, notebooks) in a logical structure that you (and others) can understand.
3. Give and receive constructive peer feedback to improve spatial analysis work.
4. Reflect on what you've learned and identify realistic next steps for continued GIS practice.

## Before you start

- [ ] Finalize your capstone analysis—all code should run without errors, all maps should be export-ready
- [ ] Review the lecture: [Week 12 · Synthesis & Communication](../lectures/week12-capstone-theory.md)
- [ ] Test your presentation on a friend or family member—can they follow your story?
- [ ] Gather all project files (QGIS projects, Python notebooks, data sources, exports) into one organized location
- [ ] Read the [Capstone Evaluation Rubric](#capstone-evaluation-rubric) below to understand how your work will be assessed
- [ ] Prepare any questions about career paths, further study, or technical challenges for the closing discussion

## This week's activities

### Activity 1: Final troubleshooting clinic

Before presentations, you'll have dedicated time to resolve any lingering technical issues and polish your work.

**Steps:**

1. **Open lab time:** Work through final revisions with instructor and peer support available
2. **Common issues to check:**
   - Do all code cells run top-to-bottom without errors?
   - Are all data paths relative or documented clearly?
   - Do maps have proper titles, legends, scale bars, and data credits?
   - Are outputs organized logically (separate folders for maps, data, notebooks)?
   - Is your problem statement clear and focused?
3. **Quick wins:**
   - Add missing docstrings or comments to clarify complex code blocks
   - Export final maps at high resolution (300 DPI for printing)
   - Check color accessibility using Color Oracle or similar tools
   - Proofread any text annotations or captions for typos

!!! tip "Practice run-throughs"
    Do a complete dry run of your code before the showcase. Open a fresh kernel, run all cells sequentially, and time yourself. You'll catch dependencies and bugs you might otherwise miss.

### Activity 2: Presentation preparation

A great analysis deserves great storytelling. You'll structure your presentation to guide your audience from question to insight.

**Presentation structure (8-10 minutes):**

1. **Hook (30 seconds):** Start with the "why"—why does this problem matter? Who is affected?
2. **Problem framing (1-2 min):** What specific question are you answering? What's the geographic context?
3. **Data & methods (2-3 min):** What datasets did you use? What techniques did you apply (buffers, joins, hotspot analysis, network analysis, etc.)? Show a workflow diagram if helpful.
4. **Key findings (3-4 min):** What did you discover? Use 2-4 maps or visualizations to tell the story. Highlight the most important patterns.
5. **Limitations & next steps (1-2 min):** What are the caveats? What would you do with more time/data/resources?
6. **Q&A (2-3 min):** Field questions from peers and instructor

**Presentation tips:**

- **Visual hierarchy:** Use one slide per main idea. Don't crowd slides with text or multiple maps.
- **Map design:** Every map should be self-explanatory (title, legend, scale, source). Remove layers that don't serve your narrative.
- **Annotate findings:** Add arrows, callout boxes, or highlights to guide the viewer's eye to important patterns.
- **Practice timing:** Aim for 8 minutes so you have buffer time. Set a timer during practice runs.
- **Prepare for questions:** Anticipate what people might ask about your methods, data quality, or assumptions.

!!! note "Storytelling over exhaustiveness"
    You don't need to show every single map you created or every step of your analysis. Choose the 3-5 most compelling visuals that build toward your conclusion. Less is more.

**Slides checklist:**

- [ ] Title slide with your name and project title
- [ ] Problem statement slide (may include a location map)
- [ ] Data sources slide (list datasets and years)
- [ ] Methods overview (workflow diagram or bullet points)
- [ ] 2-4 results slides (maps, charts, or tables)
- [ ] Limitations & next steps slide
- [ ] Thank you / Questions slide with your contact info

**Optional:** Use the [Capstone Presentation Template](../reference/capstone-presentation-template.md) as a starting point.

### Activity 3: Showcase presentations

This is your moment to share what you've built. You'll present to your peers, instructor, and potentially invited guests (community partners, GIS professionals).

**Format:**

- Each student presents for 8-10 minutes
- 2-3 minutes of Q&A after each presentation
- Presentations can be in-person, hybrid, or fully online depending on class format
- Record presentations (with permission) for portfolio use

**As a presenter:**

- Arrive early to test screen sharing, audio, and video if virtual
- Have a backup plan (PDF of slides, offline copy) in case of technical issues
- Speak to the audience, not the screen—maintain eye contact
- Pause for questions rather than rushing through

**As an audience member:**

- Take notes using the [Peer Feedback Form](#peer-feedback-form) below
- Ask at least one question to support your peers
- Notice what works well in others' presentations—you can learn from their techniques

!!! tip "Celebrate each other"
    This is a milestone moment. Acknowledge the work your classmates have done. Genuine, specific compliments ("I loved how you framed the equity dimension of your analysis") build community and confidence.

### Activity 4: Peer feedback

Structured feedback helps everyone improve. You'll use a rubric to assess each other's work, focusing on both technical quality and communication effectiveness.

**Steps:**

1. During each presentation, complete the [Peer Feedback Form](#peer-feedback-form)
2. After all presentations, submit feedback forms to the instructor (or directly to presenters, depending on class norms)
3. Review feedback you receive with an open mind—look for patterns in what people noticed

**Feedback best practices:**

- **Be specific:** Instead of "nice maps," say "the graduated color scheme on your accessibility map made the gaps really clear."
- **Balance strengths and growth areas:** Start with what worked well, then offer constructive suggestions.
- **Focus on the work, not the person:** Say "the legend could be larger" rather than "you forgot to make the legend readable."
- **Ask questions:** "Have you thought about normalizing by population?" invites dialogue rather than dictating changes.

### Activity 5: Organize your project files

You've created valuable work over 12 weeks. Now make sure you (and others) can find and understand it.

**Create a simple project folder:**

1. Organize everything into one folder on your computer:
   ```
   my_capstone_project/
   ├── data/
   │   ├── raw/              (original downloads - never edit!)
   │   └── processed/        (cleaned data you created)
   ├── projects/             (QGIS .qgz files)
   ├── notebooks/            (Python notebooks, if you used them)
   ├── maps/                 (final maps - PDF and PNG)
   └── project_summary.txt   (plain text file - see below)
   ```

2. Write a **project_summary.txt** file explaining your work (plain text, 1 page maximum):

   ```
   PROJECT TITLE: [Give your project a clear name]

   YOUR NAME: [Your name]
   DATE COMPLETED: [e.g., May 2024]

   RESEARCH QUESTION:
   [What were you trying to find out? 1-2 sentences]

   DATA SOURCES:
   - Dataset 1 (where it came from, what year)
   - Dataset 2 (where it came from, what year)
   - etc.

   METHODS USED:
   [Brief description - e.g., "Used QGIS to create buffers and calculate areas,
   then used GeoPandas for spatial joins and density calculations"]

   KEY FINDINGS:
   - Finding 1
   - Finding 2
   - Finding 3

   LIMITATIONS:
   [What couldn't you do? What data was missing? What would make this better?]

   FILES IN THIS PROJECT:
   - maps/accessibility_map.pdf - Main map showing results
   - notebooks/analysis.ipynb - Python analysis (if applicable)
   - projects/capstone.qgz - QGIS project file
   ```

3. **Make a backup copy!**
   - Save to external drive, USB stick, or cloud storage (Google Drive, Dropbox, OneDrive)
   - Email yourself a copy
   - Don't rely on just one copy—computers fail!

!!! warning "Save your work properly"
    12 weeks of work deserves protection. Make at least 2 copies in different locations before you relax.

**Optional: Share your work (when you're ready)**

If you want to build a portfolio or share your project, you have options:

- **Easy:** Upload maps to LinkedIn with a project description
- **Medium:** Share an organized folder via Google Drive or Dropbox
- **Advanced:** Learn GitHub and create a repository (many tutorials exist online—you can learn this later!)

!!! tip "GitHub can wait"
    GitHub is incredibly useful for portfolio building, but it's a whole separate skill. Focus on organizing your files clearly now. You can always learn GitHub later when you have time to dedicate to it properly. Many free tutorials exist (GitHub Skills, YouTube, etc.).

### Activity 6: Reflection and next steps

Your final task is to reflect on your learning journey and plan how you'll continue building GIS skills.

**Reflection prompts (30-45 minutes of writing):**

1. **Growth:** Compare your Week 1 self to now. What skills surprised you most? What felt harder than expected?
2. **Challenges:** What was the most frustrating obstacle you overcame? How did you solve it?
3. **Applications:** How might you use GIS in your field (research, career, community work)?
4. **Unfinished business:** What topic or technique from the course do you want to explore more deeply?
5. **Next steps:** What's your plan for continuing GIS learning after this course ends?

**Future directions to consider:**

- Take advanced courses (spatial statistics, remote sensing, web mapping, GIS programming)
- Contribute to open-source GIS projects (QGIS, Leaflet, GeoPandas)
- Join local GIS user groups or online communities
- Apply GIS skills to a capstone thesis, work project, or volunteer initiative
- Pursue GIS certification (GISP, Esri Technical Certification)
- Attend GIS conferences (many offer student discounts or virtual options)

!!! note "GIS is a practice"
    You've built a strong foundation, but expertise comes from continued use. Set a goal to do one small GIS project per quarter—even if it's just mapping your favorite hiking trails or analyzing neighborhood walkability. Skills rust without practice.

## Support materials

- Slides: [Week 12 lecture deck](../slides/index.md)
- Lecture notes: [Synthesis & Communication](../lectures/week12-capstone-theory.md)
- Template: [Capstone Presentation Template](../reference/capstone-presentation-template.md)
- Resources: [Continuing Education Guide](../reference/continuing-education.md)

### Capstone evaluation rubric

Your capstone project will be assessed using the following criteria:

| Criterion | Exemplary (4) | Proficient (3) | Developing (2) | Beginning (1) |
|-----------|---------------|----------------|----------------|---------------|
| **Problem Framing** | Clear, focused research question with strong justification | Clear question with some justification | Vague or overly broad question; weak justification | No clear question |
| **Data & Methods** | Appropriate data sources; methods applied correctly; workflow is logical | Appropriate data; standard methods applied correctly | Data or methods have some issues | Major data or method problems |
| **Technical Execution** | Analysis works correctly; outputs are high quality | Analysis works with minor issues; outputs are adequate | Analysis has errors; outputs are incomplete | Analysis doesn't work; outputs missing |
| **Spatial Insight** | Findings clearly answer the question; patterns are interpreted thoughtfully | Findings address the question; patterns are identified | Findings are tangential; limited interpretation | No clear findings |
| **Communication** | Maps/visuals are polished; story is compelling; limitations acknowledged | Maps/visuals are clear; story is coherent; some limitations noted | Maps/visuals need work; story is unclear | Maps/visuals are poor; no story |
| **Organization** | Project files are well-organized; data sources documented; summary is clear | Files are organized; most sources documented | Files are somewhat disorganized; documentation is minimal | Files are chaotic; no documentation |

**Scoring:**
- 22-24 points: Exceptional work demonstrating strong GIS skills
- 18-21 points: Solid work showing good understanding with room to grow
- 14-17 points: Adequate work meeting core requirements with some gaps
- Below 14: Incomplete work requiring significant revision

### Peer feedback form

Use this form when reviewing classmates' presentations. Focus on being helpful and specific.

**Presenter name:** ___________________________

**Project title:** ___________________________

**What worked well? (Choose 2-3)**

- [ ] Problem was clearly framed and compelling
- [ ] Methods were appropriate and well-explained
- [ ] Maps/visuals were clear and well-designed
- [ ] Findings were interesting and well-supported
- [ ] Limitations and next steps were thoughtfully addressed
- [ ] Presentation was well-paced and engaging
- [ ] Questions were handled confidently

**Specific strengths (be specific—what exactly was good?):**

_______________________________________________________________

_______________________________________________________________

**Growth opportunities (frame as questions or suggestions, not criticisms):**

_______________________________________________________________

_______________________________________________________________

**One question I have about this work:**

_______________________________________________________________

**Overall impression (circle one):**

This project demonstrates:  **Beginning skills** / **Developing skills** / **Proficient skills** / **Exceptional skills**

## Reflect

This is your final reflection—make it count. Take 30-45 minutes to answer these questions in your [Week 12 reflection](../reference/reflections.md#week-12--capstone-showcase):

- What are you most proud of in your capstone project? What makes it meaningful to you?
- What technical skill grew the most over 12 weeks? (e.g., symbology, Python, problem framing, troubleshooting)
- What was your biggest "aha!" moment in the course—when did something click?
- How has your understanding of what GIS can (and can't) do evolved since Week 1?
- What ethical considerations will you carry forward into future spatial work?
- What's your plan for practicing GIS after this course ends? Be specific—set a concrete goal.
- If you could send advice back in time to your Week 1 self, what would you say?

!!! tip "Save this reflection"
    This isn't just a course requirement—it's a record of your learning journey. Put it somewhere you'll find it in six months or a year when you need a reminder of how far you've come.

## What you'll submit

- [ ] **Organized project folder** containing:
  - QGIS project file (.qgz) and/or Jupyter notebooks (.ipynb)
  - Final maps (PDF or PNG)
  - `project_summary.txt` file
- [ ] **Presentation slides** (PDF or PowerPoint)
- [ ] **Peer feedback forms** (completed for at least 2-3 classmates)
- [ ] **Final reflection entry** (see reflection prompts above)

**Submission format:** Follow your instructor's guidelines (upload to LMS, shared folder, etc.)

**Submission deadline:** [Per course schedule]

## What's next: Continuing your GIS journey

This course gave you foundations. Here's how to build on them.

### Learning pathways

**For Python-focused spatial analysis:**
- [Automating GIS Processes](https://autogis-site.readthedocs.io/) — University of Helsinki's free course
- [Geographic Data Science with Python](https://geographicdata.science/book/) — Comprehensive online textbook
- [GeoPandas documentation](https://geopandas.org/) — Essential library for spatial Python

**For advanced QGIS skills:**
- [QGIS Training Manual](https://docs.qgis.org/latest/en/docs/training_manual/) — Official tutorials on advanced topics
- [Spatial Thoughts courses](https://courses.spatialthoughts.com/) — Free courses on QGIS, Python, Earth Engine

**For specialized domains:**
- Remote sensing: [NASA ARSET](https://appliedsciences.nasa.gov/what-we-do/capacity-building/arset) — Free remote sensing training
- Web mapping: [Leaflet](https://leafletjs.com/), [Mapbox](https://www.mapbox.com/), [Kepler.gl](https://kepler.gl/)
- Spatial statistics: [Spatial Data Science Textbook](https://rspatial.org/index.html)
- Transport modeling: [A/B Street](https://abstreet.org/), [MATSim](https://www.matsim.org/)

### Communities to join

- **QGIS User Groups:** [Find your local chapter](https://qgis.org/en/site/forusers/usergroups.html)
- **GeoForAll:** Global network of open-source GIS labs ([osgeo.org/initiatives/geo-for-all/](https://www.osgeo.org/initiatives/geo-for-all/))
- **r/gis on Reddit:** Active community for questions and discussion
- **GIS Stack Exchange:** Q&A site for technical GIS problems ([gis.stackexchange.com](https://gis.stackexchange.com/))
- **Twitter/Mastodon #GIS and #QGIS hashtags:** Follow practitioners, see cool projects

### Conferences and events

- **FOSS4G** — Free and Open Source Software for Geospatial (annual global conference, regional events)
- **AAG Annual Meeting** — American Association of Geographers (large academic conference)
- **Esri User Conference** — Industry-focused (expensive but lots of free online content)
- **State GIS conferences** — Many states/regions have annual GIS days or conferences
- **Maptime** — Informal meetups for mappers ([maptime.io](http://maptime.io/))

### Career paths using GIS

GIS skills open doors across many fields:

- **Urban planning:** Transportation modeling, land use analysis, zoning
- **Public health:** Disease mapping, accessibility analysis, health equity research
- **Environmental science:** Habitat modeling, conservation planning, climate analysis
- **Emergency management:** Disaster response, evacuation planning, risk assessment
- **Business intelligence:** Site selection, market analysis, logistics optimization
- **Social science research:** Demographic analysis, neighborhood effects, spatial inequality
- **Nonprofit/advocacy:** Community mapping, environmental justice, participatory GIS
- **Journalism:** Data journalism, investigative mapping, visual storytelling
- **Tech industry:** Location-based services, autonomous vehicles, delivery routing

**Job titles to search:**
- GIS Analyst, GIS Specialist, Spatial Data Scientist
- Geospatial Developer, Cartographer, Location Analyst
- Urban Data Analyst, Transportation Planner, Environmental Scientist

**Building your professional network:**
- Update LinkedIn with GIS skills and link to your portfolio
- Join professional organizations (URISA, ASPRS, AAG)
- Volunteer your GIS skills for nonprofits or community groups
- Contribute to OpenStreetMap or open-source GIS projects

### Closing thoughts

You've learned to see the world through a spatial lens—to ask not just "what?" and "why?" but "where?" and "how does location shape the answer?" You've built technical skills, but more importantly, you've developed spatial thinking: the ability to recognize patterns, identify relationships, and understand how geography influences human and environmental systems.

The projects you'll create next won't be perfect, and that's okay. You'll encounter data issues, software bugs, and analyses that don't work out as planned. That's part of the process. The difference now is that you have the tools, vocabulary, and troubleshooting skills to work through those challenges.

Keep mapping. Keep questioning. Keep sharing what you learn.

Congratulations on completing this course. You're now part of a global community of spatial thinkers who use geography to understand and improve the world. We can't wait to see what you map next.
