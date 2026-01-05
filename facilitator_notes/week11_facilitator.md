# Week 11 Facilitator Notes: Design & Storytelling Studio

## Session Overview

**Session Title:** Design & Storytelling Studio
**Duration:** 3 hours (with 10-minute break)
**Session Type:** Workshop-intensive with minimal lecture
**Preparation Time Required:** 90 minutes

### Learning Objectives

By the end of this session, students will be able to:

1. Facilitate and participate in constructive design critique sessions using a structured rubric
2. Audit maps for accessibility compliance (WCAG color contrast, typography, screen reader compatibility)
3. Write effective map titles, annotations, and supporting narratives that clarify rather than clutter
4. Scope a realistic capstone project with clear objectives, data sources, and deliverables

### Materials Needed

**For Instructor:**
- [ ] 3-5 example maps for group critique (mix of strong and weak examples)
- [ ] Prepared critique demonstration (script yourself giving feedback on 1 map)
- [ ] Accessibility audit live demo setup (Color Oracle installed, WebAIM Contrast Checker bookmarked)
- [ ] Printed copies of Design Critique Rubric (1 per student)
- [ ] Printed copies of Accessibility Checklist (1 per student)
- [ ] Capstone proposal template (digital, shared via course platform)
- [ ] Projector/screen for sharing student work
- [ ] Timer for keeping critique sessions on track
- [ ] Whiteboard/markers for documenting common themes

**For Students (communicated 1 week in advance):**
- [ ] 2-3 maps from previous weeks exported as PDFs
- [ ] Laptop with QGIS installed
- [ ] Color Oracle or Coblis bookmarked
- [ ] Notebook for documenting feedback
- [ ] Initial capstone project ideas (brainstorming stage)

**Digital Resources to Share:**
- Design Critique Rubric: `/site_docs/reference/design-rubric.md`
- Accessibility Checklist: `/site_docs/reference/accessibility-checklist.md`
- Capstone Template: `/site_docs/reference/capstone-template.md`
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
- Color Oracle download: https://colororacle.org/

---

## Before Class Checklist

### 1 Week Before
- [ ] Send reminder email: students must bring 2-3 exported maps (PDF format)
- [ ] Share critique rubric and accessibility checklist for preview
- [ ] Request students start thinking about capstone topics
- [ ] Test all web tools (WebAIM, Coblis) to ensure they're still functional
- [ ] Prepare example maps for demonstration

### 3 Days Before
- [ ] Finalize critique groups (3-4 students each, balanced by skill level if possible)
- [ ] Prepare your demonstration critique (script 5 minutes of modeled feedback)
- [ ] Create slide deck with key concepts (15 slides max—this is a workshop, not lecture)
- [ ] Set up shared folder for students to upload maps (for projection during group critique)

### Day Before
- [ ] Print rubrics and checklists
- [ ] Test projection setup with sample student PDFs
- [ ] Prepare capstone scoping worksheet/template
- [ ] Review student work from previous weeks to anticipate common design issues

### Morning Of
- [ ] Arrive 15 minutes early to set up projection
- [ ] Arrange room for small group work (clusters of 3-4 desks)
- [ ] Test Color Oracle on projection system
- [ ] Write session timeline on board
- [ ] Have backup activities ready in case timing shifts

---

## Session Flow

### 0:00-0:15 | Introduction & Framing (15 min)

**Objectives:** Set expectations, explain critique culture, preview activities

**Script/Talking Points:**

"Welcome to Design Week. You've spent 10 weeks building technical skills—today we focus on communication. A perfect analysis is worthless if your audience doesn't understand your map. This session is about iteration: create, critique, revise. Professional cartographers do this constantly. You'll practice today."

**Key Messages:**
- Critique is generosity, not criticism—it helps others achieve their goals
- Accessibility is quality design, not a constraint
- Your capstone project starts today with scoping

**Activities:**
1. Show before/after example (same map, improved after critique)
2. Explain critique protocol: "What works / What could be stronger / Suggestion"
3. Set ground rules:
   - Feedback on work, not person
   - Specific, actionable comments only
   - Listen without defending (take notes instead)
   - Presenter speaks first to explain intent

**Transition:** "Let's see what this looks like in practice."

---

### 0:15-0:30 | Critique Demonstration (15 min)

**Objectives:** Model effective critique process, show rubric in action

**Setup:**
- Project one example map (ideally a student map from previous cohort, with permission)
- Walk through rubric dimensions aloud

**Demonstration Script:**

1. **Presenter explains (2 min):**
   - "This map shows [topic]. My audience is [group]. I want them to understand [message]."

2. **You give feedback using rubric (10 min):**

   **Clarity:**
   - "What works: The title immediately tells me this is about population density in Sydney."
   - "What could be stronger: The legend has 7 color classes—that's too many for quick comprehension."
   - "Suggestion: Simplify to 4-5 classes using natural breaks."

   **Hierarchy:**
   - "What works: The map frame is appropriately sized—it's clearly the focus."
   - "What could be stronger: The legend and scale bar are the same visual weight, competing for attention."
   - "Suggestion: Reduce scale bar size or move it to bottom corner."

   **Accuracy:**
   - "What works: Projection is appropriate for this region (GDA2020)."
   - "What could be stronger: North arrow is missing—orientation isn't obvious."
   - "Suggestion: Add small north arrow in top right."

   **Accessibility:**
   - "What works: Font is sans-serif and readable."
   - "What could be stronger: Color ramp uses red-green, problematic for colorblind viewers."
   - "Suggestion: Switch to blue-yellow or sequential single-hue ramp."

3. **Debrief (3 min):**
   - Ask students: "What made this feedback actionable?"
   - Expected answers: Specific, focused on goals, suggested solutions
   - "Now you'll practice in small groups."

---

### 0:30-1:15 | Design Critique Workshop (45 min)

**Objectives:** Students give/receive structured feedback on their own maps

**Setup:**
- Break into pre-assigned groups of 3-4
- Each group needs: rubrics, timer, projection space or printed maps
- Instructor circulates between groups

**Timing per Person (in groups of 4):**
- Presenter explains map/intent: 2 minutes
- Group examines map in silence: 1 minute
- Each peer gives feedback: 2 minutes each (6 min for 3 peers)
- Presenter asks clarifying questions: 1 minute
- **Total: ~10 minutes per person, 40 minutes per group**

**Facilitator Role:**
- Circulate and listen for quality of feedback
- Intervene if feedback becomes vague ("Make it better" → "Can you be more specific?")
- Note common issues across groups for later discussion
- Keep time—announce when to move to next presenter

**Common Issues to Watch For:**
1. **Vague feedback:** "I like it" or "Looks good"
   - **Intervention:** "What specifically works? Name one element."

2. **Personal taste, not goal-focused:** "I would have used blue"
   - **Intervention:** "Does the current color choice help the map achieve its purpose?"

3. **Defensive presenters:** Arguing with feedback
   - **Intervention:** "Just take notes for now—you'll decide what to apply during revision."

4. **Groups finishing too fast:** They're being superficial
   - **Intervention:** "Go deeper on accessibility—run this through Color Oracle."

**Wrap-up (5 min):**
- Reconvene whole class
- Ask: "What patterns did you notice? What issues came up repeatedly?"
- Document themes on whiteboard (likely: color contrast, title clarity, legend complexity)

---

### 1:15-1:25 | BREAK (10 min)

*Encourage students to stretch, grab water, chat informally about their maps*

---

### 1:25-1:50 | Accessibility Audit Workshop (25 min)

**Objectives:** Students systematically check maps against WCAG standards

**Introduction (5 min):**
- "Accessible design isn't extra work—it's good design. High contrast helps everyone, not just low-vision users. Colorblind-safe palettes are often more elegant than rainbow ramps. Let's audit."

**Live Demonstration (8 min):**
1. **Color Contrast Check:**
   - Project a map with text
   - Sample title color using eyedropper (QGIS or browser inspector)
   - Input into WebAIM Contrast Checker
   - Show pass/fail result
   - Demonstrate fix: darken text or add buffer

2. **Color Blindness Simulation:**
   - Open Color Oracle
   - Activate Deuteranopia filter
   - Point out where categories become indistinguishable
   - Show alternative color ramp that works

3. **Typography Check:**
   - Zoom into map to show label sizes
   - Identify overlapping labels or insufficient buffers
   - Demonstrate quick fix in QGIS Layout

**Student Activity (10 min):**
- Students audit one of their own maps using checklist
- Work individually or in pairs
- Test at least: color contrast, colorblind simulation, typography
- Document results in Accessibility Checklist

**Wrap-up (2 min):**
- "What surprised you? What failed that you thought was fine?"
- Common revelation: "I thought my colors were fine, but they fail for protanopia."
- "This is why we test. Revisions happen in Activity 4."

---

### 1:50-2:15 | Narrative Framing Mini-Lecture & Workshop (25 min)

**Objectives:** Students learn to write effective titles and annotations

**Mini-Lecture (10 min):**

**Slide 1: The Power of Words**
- Show same map with three different titles:
  1. "Population" (too vague)
  2. "Population Density in Sydney, 2021" (descriptive)
  3. "Rapid Population Growth Concentrated in Western Sydney Suburbs" (interpretive)
- Ask: "Which title helps you understand the point fastest?"

**Slide 2: Title Formula**
- [What] + [Where] + [When] + optional [Why/So What]
- Examples:
  - "Healthcare Access Gaps in Rural NSW, 2023"
  - "15-Minute Service Areas Reveal Equity Issues in Public Transit"

**Slide 3: Annotation Strategy**
- Show over-annotated map (cluttered)
- Show same map with 2 strategic callouts (clear)
- Rule: Highlight only the most critical 1-3 features

**Slide 4: Alt Text for Digital Maps**
- Format: "Map type + topic + key finding"
- Example: "Choropleth map of median income by suburb in Melbourne showing highest earners concentrated in eastern suburbs (>$120k/year), with western suburbs averaging 30% lower incomes."

**Workshop Activity (12 min):**
1. Students rewrite the title of one of their maps (3 min)
2. Pair-share: Read new title to partner—can they predict map content? (3 min)
3. Add 1-2 strategic annotations to map (sketch on printout or note in digital file) (4 min)
4. Volunteer shares before/after title with class (2 min)

**Key Teaching Point:**
- "Titles and annotations aren't decoration—they're guidance. Your job is to help readers understand quickly. Every word should earn its place."

---

### 2:15-2:45 | Capstone Planning Workshop (30 min)

**Objectives:** Students scope realistic projects, identify data, draft timelines

**Introduction (5 min):**
- "Your capstone is due Week 12. That's one week away. Today you'll scope something achievable, meaningful, and showcase-worthy."
- Show 2-3 examples from previous cohorts (if available)
- Emphasize: "Depth over breadth. One excellent analysis beats three rushed attempts."

**Scoping Framework (8 min):**

Present the **SMART Capstone Checklist** on slide:

- **Specific:** Clear spatial question, defined study area
- **Measurable:** Concrete deliverables (map + 500-word report? Web map?)
- **Achievable:** Uses data you can access now, skills you have now
- **Relevant:** Personally meaningful or professionally useful
- **Time-bound:** Completable in 1 week (assume 8-10 hours of work)

**Common Pitfalls:**
1. Study area too large (e.g., "all of Australia" → narrow to one city)
2. Data doesn't exist or requires payment (verify before committing)
3. Trying to learn a new tool mid-project (stick to QGIS)
4. Politically sensitive topics without ethical review (choose carefully)

**Workshop Activity (15 min):**

Students work individually to complete **Capstone Proposal Worksheet:**

1. **Spatial Question (1 sentence):**
   - Example: "Where are food deserts located in Greater Melbourne?"

2. **Why It Matters (2-3 sentences):**
   - Example: "Access to fresh food impacts public health. Low-income neighborhoods often have fewer grocery stores, forcing residents to rely on convenience stores with limited healthy options."

3. **Data Sources (list format):**
   - Supermarket locations (OSM, Overpass Turbo)
   - Census data on income (ABS 2021)
   - Suburb boundaries (ABS Digital Boundaries)

4. **Analysis Methods:**
   - Buffer analysis (500m walkable distance from supermarkets)
   - Spatial join (income data to buffers)
   - Choropleth map of underserved areas

5. **Expected Deliverable:**
   - A3 print map + 500-word report + 3-minute presentation

6. **Timeline:**
   - Day 1-2: Data download and cleaning
   - Day 3-4: Analysis and initial map draft
   - Day 5-6: Revision and final export
   - Day 7: Presentation prep

**Facilitator Role During Workshop:**
- Circulate and ask probing questions:
  - "Have you verified this data exists and is downloadable?"
  - "Can you complete this analysis in one week?"
  - "Is your study area small enough?"
- Help students narrow scope if too ambitious
- Suggest alternative data sources if primary is unavailable
- Flag projects that need ethical consideration

**Wrap-up (2 min):**
- "By end of class, I want to approve your topic. Grab me for 2-minute check-ins now or after class."
- "If data doesn't exist, you need a new plan today. Don't wait until Week 12."

---

### 2:45-3:00 | Wrap-up, Reflection Prompt & Preview (15 min)

**Review Key Takeaways (5 min):**

Ask students to share:
1. "What's one piece of feedback you received that you'll definitely apply?"
2. "What accessibility issue surprised you?"
3. "What's your capstone topic in one sentence?"

**Reflection Prompt (3 min):**

Assign written reflection (due before Week 12):
- What was the most valuable piece of feedback you received during critique? How will you apply it?
- Which accessibility issue surprised you most when you audited your maps?
- Compare a map before and after revision—what specific changes made the biggest impact?
- What's the spatial question driving your capstone project? Why does it matter to you?
- What's your biggest concern or uncertainty about completing the capstone in Week 12?
- How has your understanding of "good map design" evolved since Week 1?

**Preview Week 12 (3 min):**

"Next week is your showcase. You'll execute your capstone, create a polished deliverable, and present to the group. Expectations:
- Bring a finished map (PDF or web map)
- Prepare 3-minute presentation
- Support your peers during their presentations
- Celebrate your growth"

**Before You Leave (2 min):**
- "Complete your capstone proposal tonight—I'll review and approve via email within 24 hours."
- "Start downloading data this week. Don't wait until Week 12."
- "Office hours available [times] for troubleshooting."

**Final Note (2 min):**
- "Look at your Week 1 map. Compare it to what you made today. That difference is your learning. Be proud."

---

## Key Concepts to Emphasize

### 1. Critique Culture

**Core Principle:** Critique helps designers achieve their goals—it's generous, not adversarial.

**Teaching Approach:**
- Model vulnerability: Share a map you created and critique it yourself
- Normalize revision: "Professionals iterate constantly. First drafts are supposed to be rough."
- Separate designer from design: "We're evaluating the map's effectiveness, not your worth."

**Red Flags to Address:**
- Students saying "I like it" without specifics → "What specifically works?"
- Presenters getting defensive → "Just listen and take notes—you decide later what to apply."
- Feedback based on personal taste → "Does this choice help the map achieve its purpose?"

---

### 2. Accessibility as Quality Design

**Core Principle:** Accessible design improves the experience for all users, not just those with disabilities.

**Teaching Approach:**
- Frame positively: "High contrast is easier for everyone to read, especially on projectors or in sunlight."
- Show data: "8% of men have color vision deficiency—that's 1-2 people in this room."
- Demonstrate live: Use Color Oracle to make the problem visible

**Common Student Misconceptions:**
- "My color scheme looks fine to me" → Show them the colorblind simulation
- "Accessibility is just for compliance" → Emphasize professional standards and reach
- "Adding text buffers is extra work" → Show how it improves readability for everyone

**Practical Tips to Share:**
- ColorBrewer (colorbrewer2.org) has built-in colorblind-safe options
- QGIS symbology panel has "colorblind-safe" filter
- WebAIM Contrast Checker should be bookmarked permanently

---

### 3. Narrative Structure in Maps

**Core Principle:** Every map tells a story—your job is to make that story clear.

**Teaching Approach:**
- Compare journalism to cartography: "Headline = title, lede = annotations, article = supporting text"
- Show examples of interpretive vs. descriptive titles
- Practice exercise: Cover the title of a professional map, look at it, then reveal title—does it match your interpretation?

**Story Elements in Maps:**
1. **Title:** The headline—what's the main message?
2. **Annotations:** The lede—what should readers notice first?
3. **Legend/labels:** The context—how to decode the visual information
4. **Caption/supporting text:** The explanation—why it matters, what it means

**Red Flags:**
- Titles that are just variable names ("SEIFA_2021_Decile")
- Over-annotation (10+ callouts cluttering the map)
- Annotations that just repeat what's obvious ("This is Melbourne")
- Missing context (no explanation of why this map exists)

---

### 4. Audience Awareness

**Core Principle:** Design choices depend on who will use the map and for what purpose.

**Teaching Approach:**
- Ask: "Who is your audience? What do they already know? What do they need to learn?"
- Show same data visualized differently for different audiences:
  - Academic audience: Technical title, detailed legend, projection info
  - Public audience: Plain language title, simplified categories, big labels

**Audience Considerations:**
- **Technical knowledge:** Can they interpret a standard deviation map? Or do you need plain language categories?
- **Familiarity with place:** Do they need a locator map, or do they already know the region?
- **Purpose:** Is this for quick decision-making (simplify ruthlessly) or detailed analysis (include nuance)?

**Exercise:**
- Show a technical map and ask: "How would you adapt this for a community meeting? For a journal article? For social media?"

---

### 5. Visual Hierarchy

**Core Principle:** Design should guide the eye to the most important information first.

**Teaching Approach:**
- Squint test: "Blur your eyes and look at the map—what draws your attention first? Is that the right element?"
- Size, color, position all create hierarchy
- Demonstrate: Show map where title is tiny and legend is huge—it feels wrong

**Hierarchy Toolkit:**
- **Size:** Bigger = more important (title > subtitle > labels)
- **Color:** High contrast = emphasis (bright on dark, dark on light)
- **Position:** Top-left and center get noticed first (Western reading patterns)
- **Whitespace:** Isolation creates importance (don't crowd your main message)

**Common Mistakes:**
- All elements same size (nothing stands out)
- Legend bigger than title (confuses priority)
- Map frame too small (surrounded by clutter)
- No whitespace (everything competes)

---

## Critique Framework

### The Three-Part Feedback Structure

Teach students to structure every piece of feedback using this format:

1. **What works:** Specific positive element
2. **What could be stronger:** Specific issue or limitation
3. **Suggestion:** Actionable improvement

**Why This Format:**
- Starts positive (builds trust, acknowledges effort)
- Identifies problem clearly (without being vague)
- Offers solution (makes feedback actionable)

### Critique Rubric Dimensions

Provide students with a printed rubric covering four dimensions:

#### 1. Clarity
**Question:** Can a viewer understand the main message in 5 seconds?

**What to Look For:**
- Title clearly states topic, place, time
- Legend is interpretable without external help
- Visual complexity matches audience expertise

**Feedback Examples:**
- Strong: "The title immediately tells me this is about housing affordability in Auckland."
- Weak: "I can see there are different colors, but I'm not sure what they represent."

---

#### 2. Hierarchy
**Question:** Does the visual organization guide your eye appropriately?

**What to Look For:**
- Map frame is the dominant element
- Title is prominent but doesn't overpower
- Supporting elements (legend, scale, north arrow) are present but secondary
- Whitespace separates elements clearly

**Feedback Examples:**
- Strong: "My eye goes straight to the map, then the title, then the legend—perfect flow."
- Weak: "The legend is bigger than the map frame, which confuses what I should focus on."

---

#### 3. Accuracy
**Question:** Are labels correct, scale bar accurate, projections appropriate?

**What to Look For:**
- Spelling and grammar in labels/titles
- Scale bar matches actual distances
- Projection suitable for study area (e.g., not Web Mercator for area-based analysis)
- North arrow present (unless orientation is obvious)
- Data sources cited

**Feedback Examples:**
- Strong: "I checked your scale bar against Google Maps—it's accurate."
- Weak: "This label says 'Melbourn' (missing the 'e')—small typo to fix."

---

#### 4. Accessibility
**Question:** Can this be read by people with color vision deficiencies or low vision?

**What to Look For:**
- Text contrast meets WCAG AA (4.5:1) or AAA (7:1)
- Color palette works for deuteranopia, protanopia, tritanopia
- Font size at least 9pt (print) or 12pt (digital)
- Text buffers prevent labels from blending into background

**Feedback Examples:**
- Strong: "I ran this through Color Oracle—all categories remain distinct."
- Weak: "The red-green color scheme becomes muddy for colorblind viewers—try blue-yellow instead."

---

### Facilitating Critique Sessions

**Your Role as Facilitator:**

1. **Set the Tone:**
   - Emphasize learning, not judgment
   - Model giving feedback yourself first
   - Intervene if feedback becomes personal or vague

2. **Keep Time:**
   - Use a visible timer
   - Give 1-minute and 30-second warnings
   - Move groups along if they're stuck on one person too long

3. **Circulate and Listen:**
   - Visit each group at least twice
   - Listen for quality of feedback
   - Note common themes for whole-class debrief

4. **Intervene When Needed:**
   - If feedback is too vague: "Can you be more specific? Name one element that works well."
   - If presenter is defensive: "Just take notes for now—you'll decide what to apply later."
   - If feedback is based on personal taste: "Does this choice help the map achieve its purpose for the intended audience?"

5. **Celebrate Good Feedback:**
   - When you hear excellent critique, amplify it: "That's a great observation—specific and actionable."
   - Share standout feedback examples during whole-class debrief

---

### Handling Difficult Moments

**Scenario 1: Student gives vague feedback**
- Example: "It looks good" or "I like it"
- **Intervention:** "What specifically works? Name one design choice that's effective."

**Scenario 2: Student is overly critical**
- Example: "This is confusing, the colors are bad, I don't understand anything"
- **Intervention:** "Let's use the rubric structure: What's one thing that works? Then we'll identify one area to improve with a specific suggestion."

**Scenario 3: Presenter defends their choices**
- Example: "But I chose that color because I like blue"
- **Intervention:** "It's okay to defend your choices, but for now, just listen and take notes. You'll decide later what feedback to apply. The goal is to hear how others experience your map."

**Scenario 4: Group finishes too quickly**
- **Intervention:** "It looks like you've covered the basics. Now go deeper—run one map through Color Oracle and check for accessibility. Test the title: Can someone outside this group predict the map's content from the title alone?"

**Scenario 5: Silence/awkwardness**
- **Intervention:** "Let's start with Clarity. Can you understand the main message in 5 seconds? What helps or hinders that?"

---

## Discussion Prompts

Use these prompts to spark meaningful conversation during transitions or debrief moments:

### Opening Discussion (After Critique Demo)
**Prompt:** "What makes feedback helpful vs. unhelpful? Think of a time you received feedback on any project—what made it easy to act on?"

**Expected Answers:**
- Specific, not vague
- Focused on goals, not personal taste
- Actionable, with suggestions

**Teaching Point:** "That's what we're practicing today—feedback that helps people improve, not just evaluates."

---

### Mid-Session Discussion (After Critique Workshop)
**Prompt:** "What patterns did you notice? Did the same issues come up across multiple maps?"

**Expected Themes:**
- Color contrast problems
- Titles too technical or vague
- Legends with too many categories
- Missing data sources

**Teaching Point:** "These are common challenges, even for professionals. Recognizing them in others' work helps you catch them in your own."

---

### Accessibility Discussion (After Audit Workshop)
**Prompt:** "What surprised you most when you checked your map for accessibility?"

**Expected Responses:**
- "I thought my colors were fine, but they fail for colorblind viewers."
- "My text contrast was way lower than I realized."
- "I didn't know 8% of people can't see red-green differences."

**Teaching Point:** "This is why we test. Assumptions about readability don't match reality. Accessible design benefits everyone."

---

### Narrative Discussion (During Framing Workshop)
**Prompt:** "What makes a map tell a story vs. just show data? What's the difference?"

**Expected Answers:**
- Story maps have interpretive titles (not just "Population Map")
- Story maps highlight specific patterns with annotations
- Story maps have context (why this matters)

**Teaching Point:** "Data becomes a story when you add interpretation. Your job is to guide readers to the insight, not just present raw information."

---

### Capstone Discussion (During Planning Workshop)
**Prompt:** "What's your biggest concern about the capstone? What feels uncertain?"

**Expected Concerns:**
- "I don't know if my data exists"
- "I'm worried I'm choosing something too big"
- "I'm not sure what 'done' looks like"

**Teaching Point:** "These are all valid concerns, and we'll address them today. Scoping is the hardest part—once your plan is solid, execution is straightforward."

---

### Closing Discussion (Wrap-up)
**Prompt:** "How has your understanding of 'good map design' changed since Week 1?"

**Expected Responses:**
- "I used to think more colors = better. Now I know simplicity is stronger."
- "I didn't realize how much titles matter."
- "I thought accessibility was just a checkbox, but it's actually about reaching your audience."

**Teaching Point:** "You've developed a designer's eye. That's the real skill—not just making maps, but evaluating them critically and iterating toward excellence."

---

### Advanced Discussion (If Time Allows)
**Prompt:** "When is it okay to break design rules? When might you use 8 colors in a legend, or skip the north arrow, or use decorative fonts?"

**Expected Answers:**
- When audience is expert and expects complexity
- When the map is artistic/exploratory, not analytical
- When conventions (like north-up orientation) are so standard that north arrow is redundant

**Teaching Point:** "Rules are tools, not laws. But you have to understand the rules before you can break them intentionally. Breaking rules without understanding why they exist usually just creates confusion."

---

## Workshop Activities

### Activity 1: Design Critique Workshop (45 min)

**Format:** Small group peer review
**Group Size:** 3-4 students
**Materials:** Student maps, critique rubric, timer

**Setup:**
1. Pre-assign groups (balance skill levels if possible)
2. Each student brings 2 maps (minimum 1)
3. Provide printed rubrics (or digital on shared screen)

**Process:**

**Round 1: First map from each student**
- Presenter shows map and explains (2 min):
  - "This map shows [topic]"
  - "My audience is [who]"
  - "I want them to understand [message]"
- Group silently examines map (1 min)
- Each peer gives structured feedback (2 min each):
  - Use "What works / What could be stronger / Suggestion" format
  - Address at least 2 rubric dimensions (Clarity, Hierarchy, Accuracy, Accessibility)
- Presenter asks clarifying questions (1 min)
- **Rotate to next presenter (repeat cycle)**

**Facilitator Role:**
- Set timer and announce transitions
- Circulate between groups
- Listen for quality of feedback
- Intervene if feedback is vague or unproductive
- Note common themes for debrief

**Debrief (5 min):**
- Reconvene whole class
- Ask: "What issues came up repeatedly across maps?"
- Document themes on whiteboard
- Likely themes: color contrast, title clarity, legend complexity, missing data sources

**Variations:**
- **If class is large (>20 students):** Run two parallel sessions in different rooms
- **If class is small (<12 students):** Do whole-class critique with one volunteer map
- **If time is short:** Each student presents only 1 map instead of 2

---

### Activity 2: Accessibility Audit Workshop (25 min)

**Format:** Individual work with peer comparison
**Materials:** Student maps, Accessibility Checklist, Color Oracle, WebAIM Contrast Checker

**Setup:**
1. Students have laptops with Color Oracle installed
2. Share link to WebAIM Contrast Checker
3. Provide printed Accessibility Checklist

**Process:**

**Demo Phase (8 min):**
1. **Color Contrast:**
   - Project a student map
   - Use eyedropper to sample title color
   - Input hex codes into WebAIM Contrast Checker
   - Show pass/fail result
   - Demonstrate fix: darken text or add buffer

2. **Colorblind Simulation:**
   - Open Color Oracle
   - Cycle through filters (Deuteranopia, Protanopia, Tritanopia)
   - Point out where colors become indistinguishable
   - Show alternative palette that works

3. **Typography:**
   - Zoom into map labels
   - Identify issues: overlapping labels, insufficient buffers, too-small text
   - Show quick fix in QGIS

**Student Activity (12 min):**
1. Students choose one of their own maps
2. Work through Accessibility Checklist:
   - Test color contrast for title, labels, legend
   - Run map through Color Oracle (all 3 filters)
   - Check font sizes and readability
   - Draft alt text (1-2 sentences)
3. Document results: What passed? What failed? What needs revision?

**Pair Comparison (3 min):**
- Partner with neighbor
- Share one finding: "I was surprised by [X]"
- Trade tips: "I fixed [Y] by doing [Z]"

**Debrief (2 min):**
- Ask class: "What surprised you? What failed that you expected to pass?"
- Common revelations: Colors that look fine fail for colorblindness, text contrast lower than expected

---

### Activity 3: Title Rewriting Exercise (12 min)

**Format:** Individual work with pair-share
**Materials:** Student maps, title formula reference

**Setup:**
1. Write formula on board: **[What] + [Where] + [When] + optional [Why/So What]**
2. Show before/after examples on slide

**Process:**

**Individual Work (3 min):**
- Students identify one of their maps with a weak title
- Rewrite using the formula
- Aim for clarity and interpretation, not just description

**Before/After Examples to Share:**
- Before: "Population Map"
- After: "Population Density in Greater Sydney, 2021"
- Better: "Rapid Population Growth Concentrated in Western Sydney Suburbs, 2016-2021"

**Pair-Share (3 min):**
- Partner with neighbor
- Read new title aloud
- Partner tries to predict: "Based on this title, what do you expect to see on the map?"
- Discuss: Does the title accurately preview the content?

**Annotation Addition (4 min):**
- Students sketch 1-2 strategic annotations on their map
- Rule: Highlight only the most critical features (outliers, patterns, key locations)
- Use brief text (under 10 words per callout)

**Volunteer Share (2 min):**
- Ask for 1-2 volunteers to share before/after titles with whole class
- Class gives quick feedback: "Does this title tell me what to expect?"

---

### Activity 4: Capstone Scoping Workshop (15 min)

**Format:** Individual work with facilitator check-ins
**Materials:** Capstone Proposal Worksheet, data source reference list

**Setup:**
1. Share Capstone Proposal Template digitally
2. Write SMART criteria on board (Specific, Measurable, Achievable, Relevant, Time-bound)
3. Prepare list of common data sources for reference

**Process:**

**Guided Worksheet Completion (12 min):**

Students work individually through worksheet sections:

1. **Spatial Question (1 sentence):**
   - "Where are [phenomenon] located in [place]?"
   - "How has [variable] changed in [place] over [time]?"

2. **Why It Matters (2-3 sentences):**
   - Who cares about this question?
   - What decision or understanding does this inform?

3. **Data Sources (list format):**
   - Name each dataset
   - Verify it's downloadable (include URL)
   - Note format (shapefile, CSV, etc.)

4. **Analysis Methods:**
   - List 2-3 techniques from course (buffer, spatial join, choropleth, network analysis, etc.)
   - Keep it simple—stick to tools you know

5. **Expected Deliverable:**
   - Format: A3 print map? Web map? Map + report?
   - Length: 1 page? 500 words?
   - Presentation: 3 minutes? 5 slides?

6. **Timeline:**
   - Break Week 12 into daily tasks
   - Example:
     - Day 1-2: Data download and cleaning
     - Day 3-4: Analysis and initial map
     - Day 5-6: Revision and polish
     - Day 7: Presentation prep

**Facilitator Check-Ins (ongoing):**
- Circulate and ask probing questions:
  - "Have you confirmed this data exists and is downloadable?"
  - "Can you realistically complete this in one week?"
  - "Is your study area scoped narrowly enough?"
- Help students narrow if too ambitious
- Suggest alternatives if data unavailable

**Wrap-up (3 min):**
- "By end of class, I want to approve your topic. Grab me for a 2-minute check-in."
- "Submit completed proposal tonight—I'll review within 24 hours."

---

### Optional Activity: Before/After Comparison (If Time)

**Format:** Individual reflection
**Duration:** 10 min

**Process:**
1. Students retrieve their Week 1 map
2. Place it side-by-side with a recent map (Week 6, 8, or 10)
3. Document differences:
   - What improved? (technical skills, design choices, clarity)
   - What would you do differently now?
   - What does this reveal about your growth?

4. Share with partner:
   - "The biggest change I see is [X]"
   - "I'm proud of how I [Y]"

**Teaching Point:**
- "This difference is your learning. Don't underestimate how far you've come."

---

## Capstone Prep

### Helping Students Scope Projects

Capstone scoping is the most critical part of this week. A well-scoped project is 80% done before Week 12 even starts. Here's how to guide students:

---

### The SMART Capstone Framework

Use this as a checklist when reviewing proposals:

**S - Specific:**
- Is the spatial question clearly defined?
- Is the study area bounded and manageable?
- Are expected outcomes concrete?

**Red flags:**
- "I want to analyze climate change" (too broad)
- "I'll map the whole country" (too large)
- "I'll see what the data shows" (no hypothesis)

**Fix:** Narrow scope—"I'll map heat vulnerability in my city's urban core using tree cover and census data"

---

**M - Measurable:**
- Are deliverables defined? (map + report? web map? presentation?)
- Can you verify success? (e.g., "1 map, 500 words, 3-min presentation")

**Red flags:**
- "I'll make some maps" (vague)
- No clear endpoint

**Fix:** "I'll produce one A3 print map, a 500-word analysis, and a 3-minute presentation"

---

**A - Achievable:**
- Does the data exist and is it accessible?
- Can this be done with current QGIS skills?
- Is one week enough time?

**Red flags:**
- Data requires paid subscription or special access
- Student plans to learn Python or R mid-project
- Analysis requires techniques not covered in course

**Fix:** "I've downloaded all datasets and confirmed they're compatible. I'll use tools from Weeks 5-8 (buffers, spatial joins, choropleth mapping)"

---

**R - Relevant:**
- Is this meaningful to the student?
- Does it connect to their interests or professional goals?
- Will it make a good portfolio piece?

**Red flags:**
- "I just need something quick to submit"
- No connection to student's interests

**Fix:** Encourage students to choose topics they care about—motivation matters

---

**T - Time-bound:**
- Is there a realistic daily timeline?
- Are there built-in buffers for troubleshooting?

**Red flags:**
- "I'll do it all on the last day"
- No breakdown of tasks
- No contingency plan

**Fix:** Create day-by-day plan with specific milestones

---

### Common Capstone Pitfalls & Solutions

**Pitfall 1: Study area too large**
- **Example:** "I want to map public transit access across all of Australia"
- **Problem:** Massive data processing, overwhelming complexity
- **Solution:** "Narrow to one city: 'Public transit access in Greater Melbourne'"

**Pitfall 2: Data doesn't exist**
- **Example:** "I'll map illegal dumping sites"
- **Problem:** No public dataset available
- **Solution:** "Check data availability first. Alternative: use available datasets like waste collection zones or reported environmental violations"

**Pitfall 3: Trying to learn new tools mid-project**
- **Example:** "I'll create an interactive web map using Leaflet"
- **Problem:** Leaflet wasn't covered in course, requires JavaScript
- **Solution:** "Stick to QGIS. You can export a static map and embed it in a simple webpage, or use QGIS2Web plugin for basic interactivity"

**Pitfall 4: Politically sensitive topics without ethics review**
- **Example:** "I'll map crime rates by ethnicity"
- **Problem:** Risk of reinforcing stereotypes, ethical concerns
- **Solution:** "Reframe: 'I'll map crime rates by neighborhood socioeconomic status' or choose a less sensitive topic"

**Pitfall 5: Underestimating data cleaning time**
- **Example:** "I'll download the data on Day 6"
- **Problem:** Data cleaning often takes 30-50% of project time
- **Solution:** "Download and inspect data this week. Ensure it's clean and usable before Week 12 starts"

---

### Effective Check-In Questions

When students come to you with capstone ideas, ask:

1. **"Have you downloaded the data yet?"**
   - If no: "Do that today. You need to verify it's usable."
   - If yes: "Great—have you opened it in QGIS? Any issues?"

2. **"Can you complete this in 8-10 hours of work?"**
   - If unsure: "Let's list every task. How long for each?"
   - If no: "What can we cut to make this feasible?"

3. **"What's your backup plan if this data doesn't work?"**
   - Always have Plan B ready
   - Example: "If transit data is incomplete, I'll focus on just bus routes instead of all transit modes"

4. **"Why does this question matter to you?"**
   - If they shrug: "Think about what you care about—environmental justice? Urban planning? Public health? Choose something you're curious about."
   - If they light up: "Great—that passion will carry you through challenges"

5. **"What techniques from the course will you use?"**
   - Should name 2-3 specific methods (buffer analysis, spatial join, choropleth, etc.)
   - If vague: "Let's map this to specific weeks. Week 5 covered buffers, Week 7 covered spatial joins—which applies here?"

---

### Approving or Redirecting Proposals

**Green Light Projects (approve immediately):**
- Clear spatial question
- Data verified as accessible
- Realistic scope for one week
- Uses course techniques
- Student is enthusiastic

**Yellow Light Projects (needs refinement):**
- Good idea, but scope too broad → help narrow
- Data questionable → ask them to verify by tonight
- Timeline vague → work through day-by-day plan together

**Red Light Projects (redirect):**
- Data doesn't exist or requires payment → need new topic
- Requires skills not taught in course → simplify or choose different approach
- Ethically problematic → reframe or choose new topic
- Student clearly not invested → encourage them to find something meaningful

---

### Sample Approved Capstone Proposals

Share these as examples of well-scoped projects:

**Example 1: Food Access Analysis**
- **Question:** Where are food deserts located in Greater Melbourne?
- **Data:** Supermarket locations (OSM), census income data (ABS), suburb boundaries (ABS)
- **Methods:** Buffer analysis (500m walkable distance), spatial join, choropleth mapping
- **Deliverable:** A3 print map + 500-word report
- **Why it works:** Achievable, clear, uses Week 5-7 skills

**Example 2: Green Space Equity**
- **Question:** Do low-income neighborhoods have less access to parks?
- **Data:** Park boundaries (local council open data), census income (ABS), population density (ABS)
- **Methods:** Buffer analysis, spatial join, comparison statistics
- **Deliverable:** 2-page map layout with comparison charts
- **Why it works:** Manageable scope, combines mapping + basic analysis

**Example 3: Public Transit Gaps**
- **Question:** Which neighborhoods are underserved by public transit in Auckland?
- **Data:** Bus/train routes (GTFS from transit agency), census data, street network (OSM)
- **Methods:** Service area analysis (buffers), spatial join with demographic data
- **Deliverable:** Web map using QGIS2Web + 300-word summary
- **Why it works:** Data readily available, techniques covered in Week 8

---

### Timeline Template for Students

Provide this as a starting point for their proposals:

**Week 12 Capstone Timeline:**

**Day 1 (Monday):**
- Download all datasets
- Inspect data for completeness/quality
- Set up QGIS project with correct projection
- Create initial data cleaning plan

**Day 2 (Tuesday):**
- Clean and prepare data (join tables, fix geometries, standardize fields)
- Perform preliminary spatial joins or buffers
- Troubleshoot any data issues

**Day 3 (Wednesday):**
- Execute main analysis (buffer analysis, spatial statistics, classification)
- Create initial map draft
- Check: Does this answer my spatial question?

**Day 4 (Thursday):**
- Refine symbology (colors, labels, legend)
- Apply accessibility checks (color contrast, colorblind simulation)
- Write initial draft of supporting text

**Day 5 (Friday):**
- Peer review or self-critique using Week 11 rubric
- Make revisions based on feedback
- Finalize map layout

**Day 6 (Saturday):**
- Export final map (PDF/PNG)
- Complete written report or web page
- Create presentation slides (3-5 slides)

**Day 7 (Sunday):**
- Practice presentation (aim for 3 minutes)
- Prepare to answer questions
- Submit deliverables

**Buffer Day:**
- Build in extra time for troubleshooting—something will go wrong!

---

## Wrap-up & Preview

### Session Wrap-up (10 min)

**Review Learning Objectives:**

Ask students to self-assess:
- "Can you give constructive design feedback using a rubric?" (thumbs up/down)
- "Can you check a map for accessibility?" (thumbs up/down)
- "Can you write an effective map title?" (thumbs up/down)
- "Do you have a scoped capstone plan?" (thumbs up/down)

If many thumbs down, address gaps before dismissing class.

---

**Celebrate Progress:**

"Look at where you were in Week 1—many of you had never opened QGIS. Today you're critiquing maps like professionals, checking for accessibility compliance, and planning independent spatial analysis projects. That growth is real. Be proud."

---

**Reflection Assignment (Due before Week 12):**

Remind students to complete written reflection:
- Most valuable feedback received?
- Accessibility issue that surprised you?
- Before/after revision comparison?
- Capstone question and why it matters?
- Biggest concern about capstone?
- How has your definition of "good design" changed?

---

**Action Items Before Week 12:**

1. **Tonight:**
   - Finalize capstone proposal (instructor will review within 24 hours)
   - Download all capstone datasets and verify usability

2. **This Week:**
   - Revise at least one map based on critique feedback
   - Complete accessibility checklist
   - Start capstone data cleaning

3. **Before Week 12 Session:**
   - Have capstone analysis 50% complete
   - Draft map layout ready for refinement

---

### Preview of Week 12

**"Next week is your showcase week. Here's what to expect:"**

**Format:**
- First half: Dedicated work time with instructor support
- Second half: Capstone presentations (3 minutes each)

**Expectations:**
- Bring a polished final deliverable (map + report or web map)
- Prepare 3-minute presentation covering:
  - Your spatial question
  - Your methods
  - Your key findings
  - One challenge you overcame
- Be ready to answer 1-2 questions from peers

**Support Available:**
- Office hours: [insert times]
- Email troubleshooting: Response within 12 hours
- Slack/discussion forum for peer help

**Grading Criteria:**
- Technical execution (40%): Correct use of GIS techniques
- Design quality (30%): Clarity, accessibility, visual hierarchy
- Communication (20%): Title, annotations, supporting text
- Presentation (10%): Clear delivery, time management

**Portfolio Preparation:**
- This capstone will be a portfolio piece—choose something you're proud to share
- Consider adding your best Week 11 revised map too

---

**Final Encouragement:**

"This is your chance to synthesize everything you've learned. You've built the skills—Week 12 is about putting them together to answer a question you care about. Don't underestimate what you can do. I'm excited to see what you create."

---

**Questions?**

Open floor for:
- Capstone topic concerns
- Technical questions about revision tools
- Clarifications on Week 12 format

---

## Additional Facilitator Resources

### Pre-Session Preparation Checklist

**1 Week Before:**
- [ ] Email students: Bring 2-3 maps (PDF) for critique
- [ ] Share rubric, accessibility checklist, capstone template
- [ ] Test all web tools (WebAIM, Coblis, Color Oracle)

**3 Days Before:**
- [ ] Create critique groups (3-4 students, balanced skill levels)
- [ ] Prepare demonstration critique script
- [ ] Gather example maps (strong + weak) for teaching
- [ ] Set up shared folder for map uploads

**Day Before:**
- [ ] Print rubrics and checklists (1 per student)
- [ ] Test projection setup
- [ ] Review student work from previous weeks
- [ ] Prepare capstone scoping worksheet

**Morning Of:**
- [ ] Arrive 15 min early
- [ ] Arrange room for group work (clusters of 3-4)
- [ ] Test Color Oracle on projector
- [ ] Write timeline on board
- [ ] Prepare backup activities

---

### Example Maps for Demonstration

Prepare 3-5 example maps covering common issues:

1. **Weak Title Example:** Technical jargon, vague
2. **Color Accessibility Failure:** Red-green palette, poor contrast
3. **Visual Hierarchy Problem:** Legend bigger than map frame
4. **Over-Annotation Example:** 10+ callouts cluttering the view
5. **Strong Example:** Everything done well (for comparison)

**Sources for examples:**
- Previous student work (with permission)
- Your own maps (shows vulnerability)
- Maps from journals/reports (public domain)

---

### Troubleshooting Common Issues

**Issue: Students finish critique too quickly**
- **Solution:** "Go deeper—run this through Color Oracle. Check every rubric dimension, not just overall impression."

**Issue: Feedback is too vague**
- **Solution:** Model specificity: "Instead of 'looks good,' try 'The sequential color ramp clearly shows the progression from low to high values.'"

**Issue: Presenter gets defensive**
- **Solution:** Intervene gently: "It's natural to want to explain your choices, but for now, just listen and take notes. You'll decide what to apply later."

**Issue: Capstone proposals are too ambitious**
- **Solution:** Ask: "Can you complete this in 8 hours of work? Let's list every task and estimate time." Then help them cut scope.

**Issue: Students can't find data for capstone**
- **Solution:** Have backup data sources ready (ABS, OSM, local government open data portals). Redirect to topics with known available data.

---

### Time Management Tips

This session is workshop-heavy, so timing can slip. Here's how to stay on track:

**If Running Ahead:**
- Extend critique workshop (more maps per person)
- Add optional "before/after comparison" activity
- Deeper dive into one rubric dimension (e.g., spend 10 min just on accessibility)

**If Running Behind:**
- Reduce critique to 1 map per person (instead of 2)
- Shorten accessibility audit demo (show only color contrast, skip typography)
- Make capstone scoping homework instead of in-class activity

**Emergency Compression (if 30+ min behind):**
- Combine critique + accessibility workshops (do both simultaneously)
- Skip title rewriting exercise (assign as homework)
- Capstone scoping becomes office hours/async

---

### Assessment Guidance

**What to assess this week:**

1. **Revised map (before/after comparison):**
   - Does it show meaningful improvement?
   - Were accessibility issues addressed?
   - Is title clearer?

2. **Completed Accessibility Checklist:**
   - Did they test all criteria?
   - Are findings documented clearly?
   - Did they identify actionable issues?

3. **Capstone proposal:**
   - Is spatial question clear and specific?
   - Are data sources verified?
   - Is timeline realistic?
   - Does it demonstrate understanding of course techniques?

4. **Reflection:**
   - Evidence of engagement with critique process?
   - Awareness of own growth?
   - Thoughtful consideration of design principles?

**Grading Rubric (if needed):**
- Participation in critique: 25%
- Revised map quality: 30%
- Accessibility audit completeness: 20%
- Capstone proposal feasibility: 25%

---

### Support Resources for Students

**During Session:**
- Circulate actively—visit each group 2-3 times
- Offer troubleshooting: "Stuck? Let me help."
- Celebrate good work: "This is excellent—can you share with the class?"

**After Session:**
- Office hours for capstone scoping check-ins
- Email support for data sourcing questions
- Discussion forum for peer help

**Recommended External Resources:**
- ColorBrewer: https://colorbrewer2.org/
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
- Color Oracle: https://colororacle.org/
- Coblis: https://www.color-blindness.com/coblis-color-blindness-simulator/
- WCAG Guidelines: https://www.w3.org/WAI/WCAG21/quickref/

---

### Reflection Prompt for Facilitators

After the session, take 10 minutes to reflect:

**What worked well?**
- Which activities generated the most engagement?
- Where did students show breakthrough moments?

**What needs adjustment?**
- Did timing work? What ran long/short?
- Were instructions clear? Where did confusion arise?
- Did group composition work? Any dynamics to adjust?

**Student Needs:**
- Who needs extra capstone support?
- Are there common data sourcing challenges to address?
- Any accessibility concerns to follow up on?

**For Next Time:**
- Better examples to prepare?
- Different group configurations?
- Additional scaffolding needed?

---

## Key Takeaways for Facilitators

1. **This is a synthesis week:** Students are consolidating skills, not learning new tools. Focus on refinement and application.

2. **Critique culture matters:** Model generosity, specificity, and focus on goals. Set the tone early.

3. **Accessibility is non-negotiable:** Frame it as quality design, not compliance. Make the benefits visible.

4. **Capstone scoping is critical:** Invest time in helping students narrow scope. A well-scoped project is already half-done.

5. **Celebrate growth:** Remind students how far they've come since Week 1. Confidence matters for capstone success.

6. **Be flexible:** Workshops rarely go exactly as planned. Adjust timing as needed, but protect core activities (critique, accessibility audit, capstone scoping).

7. **Support is ongoing:** Week 12 capstone success depends on Week 11 preparation. Follow up with students who need extra help.

---

**Good luck! This is one of the most rewarding weeks—students grow rapidly when they practice critique and see their own improvement. Enjoy facilitating their growth.**
