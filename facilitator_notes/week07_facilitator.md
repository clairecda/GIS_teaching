# Week 7 Facilitator Notes: Bridge to Python / Reproducibility

## Session Overview

**Duration:** 90-120 minutes (recommend 120 for first-time Python students)

**Primary Learning Objectives:**
1. Students will successfully run a Python notebook using Google Colab or Jupyter
2. Students will understand the connection between QGIS workflows and Python equivalents
3. Students will articulate why reproducibility matters in spatial analysis
4. Students will recognize when to use GUI tools vs. code-based workflows

**Materials Needed:**
- [ ] Projector/screen sharing setup for live Colab demonstration
- [ ] Week 7 starter notebook link: [week07_hello_gis.ipynb](https://github.com/clairecda/GIS_teaching/blob/main/notebooks/week07_hello_gis.ipynb)
- [ ] Google Colab badge link ready: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/clairecda/GIS_teaching/blob/main/notebooks/week07_hello_gis.ipynb)
- [ ] Example QGIS project from Week 3 or 5 (for comparison demo)
- [ ] Backup: Downloaded notebook files in case internet fails
- [ ] Student login support: List of common Google account issues

**Mindset for this week:** This is a TRANSITION week, not a technical Python course. Focus on lowering anxiety, building confidence, and showing the "why" before diving into the "how." Many students will be intimidated by code—your primary goal is to make Python feel approachable.

---

## Before Class Checklist

### Technical Preparation (48 hours before class)
- [ ] **Test the Colab link yourself** - Open the Week 7 notebook in Colab and run all cells
- [ ] **Verify package installations work** - Make sure `!pip install geopandas...` completes without errors
- [ ] **Check notebook renders properly** - Confirm maps display, no broken cells
- [ ] **Test Google Drive mounting** (if demonstrating) - Practice mounting Drive in case students ask
- [ ] **Prepare offline backup** - Download the .ipynb file to your computer
- [ ] **Test local Jupyter** (optional) - If offering Anaconda support, verify your local setup works

### Content Preparation
- [ ] **Review QGIS-to-Python comparison table** - Be ready to explain each translation
- [ ] **Prepare 2-3 relatable automation examples** - E.g., "Imagine updating 50 health facility maps monthly"
- [ ] **Identify one simple past QGIS workflow to recreate** - E.g., Week 3 point-in-polygon or Week 5 buffer
- [ ] **Have reproducibility talking points ready** - Scientific publication requirements, audit trails, collaboration

### Student Support Materials
- [ ] **Colab troubleshooting cheat sheet** - Common errors and fixes (see section below)
- [ ] **Office hours schedule** - For students who need extra Python setup help
- [ ] **Optional resources list** - Additional Python/GeoPandas tutorials for curious students
- [ ] **Week 8 preview** - Brief outline so students know what's coming

### Internet Failure Backup Plan
If Colab/internet fails during class:
1. **Show pre-recorded demo** - Record yourself running the notebook beforehand
2. **Use screenshots** - Walk through the notebook with static images
3. **Local Jupyter demo** - Have Anaconda installed on your machine as backup
4. **Shift to discussion** - Spend more time on QGIS-to-Python comparison and reproducibility concepts

---

## Session Flow (Recommended Timing for 120-min session)

### 1. Opening & Context Setting (15 minutes)

**Welcome & Transition Framing (5 min)**
- "You've spent six weeks mastering QGIS—filtering, spatial joins, network analysis. Today we're adding a new tool to your toolkit: Python."
- **Key message:** Python doesn't replace QGIS. Professionals use both. This is about choosing the right tool for each task.

**Why Learn Python After QGIS? Discussion Prompt (10 min)**
Ask students to consider scenarios:
- "Imagine you need to create the same hotspot map for 20 different cities. Would you want to click through QGIS 20 times, or run a script once?"
- "What if a reviewer asks you to re-run your analysis with different parameters? Can you remember every setting you used in QGIS three months ago?"
- "How would you share your exact methodology with a colleague? Send them 15 screenshots of tool dialogs?"

**Write student responses on board/virtual whiteboard:**
- Automation & efficiency
- Reproducibility & documentation
- Collaboration & sharing
- Scalability (many datasets, repeated workflows)
- Transparency for publication/peer review

### 2. Transition Talk: GUI vs. Code (10 minutes)

**QGIS Strengths (validate what they've learned):**
- Visual exploration of unfamiliar data
- Quick map creation for presentations
- Intuitive for one-off analyses
- Excellent debugging tool (see what went wrong spatially)
- Great for communicating with non-technical stakeholders

**Python Strengths (where we're heading):**
- Automate repetitive tasks (process 100 files in minutes)
- Complete audit trail (every step documented in code)
- Version control friendly (track changes over time)
- Reproducible (run the same analysis next year, get same results)
- Integrates with data pipelines (connect to databases, APIs, web apps)

**Key Takeaway:** "Most spatial analysts use QGIS for exploration and prototyping, then Python for production workflows. You'll learn to recognize which tool fits each situation."

### 3. Reproducibility Deep Dive (15 minutes)

**What is Reproducibility?** (5 min)
- Definition: Someone else (or future you) can recreate your analysis and get the same results
- Components:
  - **Data:** Where did it come from? What version?
  - **Methods:** Exact steps, tools, parameters
  - **Environment:** Software versions, operating system
  - **Documentation:** Why you made each choice

**Why Does It Matter?** (5 min)
- **Science:** Peer review requires reproducible methods
- **Professional work:** Clients/managers may ask "how did you calculate this?"
- **Legal/policy:** Government analyses must be auditable
- **Collaboration:** Team members need to build on your work
- **Future you:** You'll forget your own methods in 6 months!

**QGIS vs. Python for Reproducibility** (5 min)
- QGIS: Requires manual documentation (screenshots, written notes, Processing History panel)
- Python: Code itself IS the documentation
- Jupyter notebooks: Combine code, results, explanations in one document

**Activity idea:** Show two approaches to documenting a buffer analysis:
1. QGIS: Screenshots of tool dialog → hard to re-create exact parameters
2. Python: `df.geometry.buffer(500)` → unambiguous, executable

### 4. Live Colab Walkthrough (25 minutes)

**CRITICAL: Slow down here. This is many students' first time running code.**

**Opening Colab (5 min)**
- Click the "Open in Colab" badge from the course website
- Wait for notebook to load (mention it may take 15-30 seconds)
- **Point out interface elements:**
  - Menu bar (File, Edit, Runtime...)
  - Code cells (gray background)
  - Text cells (white background, formatted markdown)
  - Table of contents button (left sidebar)
  - Files browser button (folder icon)

**Understanding Notebook Structure (3 min)**
- "Notebooks mix code and text. Text cells explain what we're doing, code cells do the work."
- "Think of it like a lab notebook with executable instructions."
- Show example: Text cell says "Load the data," code cell says `gdf = gpd.read_file(...)`

**Installing Packages (5 min)**
- Scroll to first code cell: `!pip install geopandas rasterio...`
- **Explain what this means:** "We're downloading tools other people built. GeoPandas is like QGIS's vector tools, but for Python."
- Run the cell (Shift + Enter OR click play button)
- **Manage expectations:** "This takes 1-2 minutes. You'll see installation progress. That's normal."
- While waiting, explain: "Colab resets when you close it, so you'll run this cell every session. It becomes muscle memory."

**Running Cells in Order (7 min)**
- Run second cell (imports): `import geopandas as gpd`
- **Explain:** "This loads the tools we installed. Like opening QGIS, but for each library."
- Run next cell (load data): `gdf = gpd.read_file(url)`
- **Connect to QGIS:** "This is like Layer → Add Vector Layer, but with code."
- Run cell that shows data: `gdf.head()`
- **Point out:** "Like the attribute table in QGIS! Same data, different view."

**Creating a Map (5 min)**
- Run the cell that plots: `gdf.plot()`
- **Celebrate:** "You just made a map with Python!"
- **Compare to QGIS:** "QGIS auto-styles layers. Python requires explicit styling commands. Trade-off: less automatic, more control."
- If notebook includes styled map, show before/after: default plot vs. styled version

**Common Issues to Address During Demo:**
- "If a cell shows an error, check if you ran previous cells in order."
- "Green checkmark = cell completed successfully."
- "Spinning icon = still running (wait)."
- "Red error text doesn't mean you broke it! Errors are normal. Read the message."

### 5. Student Hands-On Time (30 minutes)

**Setup Phase (10 min)**
- "Now it's your turn. Open the notebook link from the course site."
- Walk around / monitor screen shares
- Help with:
  - Google login issues
  - Colab not loading (refresh, try different browser)
  - Finding the "Open in Colab" button

**Guided Execution (15 min)**
- "Run the pip install cell. Raise your hand when it's done."
- Wait for most students to complete before moving on
- "Run the import cells. Does anyone see an error?"
- Troubleshoot collectively—common error: forgot to run pip install cell

**Independent Exploration (5 min)**
- "Continue running cells at your own pace. Try to understand what each one does."
- "Bonus: Try changing a number in a code cell (like buffer distance) and re-run it. See what happens!"
- Circulate to answer questions

**Milestone Check:** By end of this section, every student should have:
- Opened the Colab notebook
- Run at least 3-4 cells successfully
- Seen at least one map output

### 6. QGIS-to-Python Comparison (10 minutes)

**Pull up the comparison table from student materials:**

| QGIS Operation | QGIS Steps | Python Equivalent |
|----------------|-----------|-------------------|
| Load shapefile | Layer → Add Vector Layer | `gpd.read_file("data.shp")` |
| Filter features | Select by Expression → Export | `df[df['field'] > value]` |
| Buffer | Vector → Geoprocessing → Buffer | `df.geometry.buffer(distance)` |

**Interactive Activity:**
- Pick one operation students did recently (e.g., Week 5 buffer for health facilities)
- Show QGIS screenshots of the tool dialog
- Show Python equivalent: `facilities_gdf.geometry.buffer(500)`
- Ask: "Which is faster for one dataset? Which is faster for 50 datasets?"

**Pattern Recognition:**
- "Notice: Python operations are often shorter but less visual."
- "QGIS: Click, configure, run. Python: Write, execute, inspect."
- "Both do the same spatial analysis—just different interfaces."

### 7. Discussion: When to Use What? (10 minutes)

**Pose scenarios, ask students which tool they'd choose:**

1. **"Exploring a new dataset you've never seen before"**
   - Answer: QGIS (visual, fast exploration)
2. **"Creating a monthly report map with updated data"**
   - Answer: Python (automate the repeated workflow)
3. **"Making a one-time map for a presentation"**
   - Answer: QGIS (quick styling, no need for reproducibility)
4. **"Publishing a research paper with spatial methods"**
   - Answer: Python (reviewers can see exact code)
5. **"Troubleshooting why two polygons won't intersect"**
   - Answer: QGIS (visually inspect geometry issues)

**Synthesize student responses:**
- "You'll develop intuition over time."
- "When in doubt, prototype in QGIS, then productionize in Python."

### 8. Wrap-Up & Addressing Concerns (5 minutes)

**Normalize Python Anxiety:**
- "Raise your hand if you felt nervous about coding today."
- "That's completely normal. Learning a new language (Python) feels different than learning a new tool (QGIS)."
- "Remember: You're not becoming software engineers. You're learning to automate GIS workflows."

**Week 8 Preview:**
- "Next week: Hands-on Python spatial analysis. You'll load shapefiles, filter data, do spatial joins—everything you've done in QGIS, but in code."
- "Before next week: Make sure you can run today's notebook successfully. If not, come to office hours."

**Homework Reminder:**
- Screenshot of completed notebook
- 5-10 sentence reflection on running first Python notebook

---

## Key Concepts to Emphasize

### 1. Reproducibility is a Spectrum
- **Level 1:** Save your QGIS project file (basic)
- **Level 2:** Document steps in notes/screenshots (better)
- **Level 3:** Use Processing History to log tools (good)
- **Level 4:** Write Python scripts (excellent)
- **Level 5:** Use version control (Git) with Python (advanced)

Emphasize: "We're moving toward higher levels, but all have value."

### 2. Python Notebooks as Documentation
- Notebooks combine:
  - **Code** (what you did)
  - **Results** (maps, tables, statistics)
  - **Narrative** (why you made those choices)
- This is powerful for communication, publication, collaboration

### 3. When to Use Python vs. QGIS
**Use QGIS:**
- One-off analyses
- Visual exploration
- Quick maps for presentations
- Debugging spatial issues
- Working with non-technical collaborators

**Use Python:**
- Repetitive workflows (same analysis, many datasets)
- Automating reports
- Large-scale processing
- Scientific publication (transparency)
- Integration with data pipelines

**Use both:**
- Prototype in QGIS → finalize in Python
- Explore in QGIS → document in Python
- Create map in Python → style/finalize in QGIS (if needed)

### 4. Code is a Tool, Not the Goal
- **Reframe:** You're not learning to code. You're learning to use code as a tool for spatial analysis.
- Analogy: "You didn't learn QGIS to become QGIS experts—you learned it to answer spatial questions. Same with Python."

### 5. Iteration is Normal
- Professional spatial analysts:
  - Google syntax constantly
  - Get errors frequently
  - Copy/paste/modify code from Stack Overflow
  - Run cells multiple times to debug
- **Emphasize:** "If you get an error, you're doing it right. Errors teach you."

---

## Live Demo Script

### Pre-Demo Setup (before students arrive)
1. Open fresh browser window (or incognito) to simulate student experience
2. Have course website open with Week 7 page visible
3. Have example QGIS project ready (for comparison)

### Demo Sequence (annotate each action)

**Step 1: Opening Colab (2 min)**
- "I'm on the Week 7 course page. I'll click this 'Open in Colab' badge."
- *Click link*
- "Colab is loading. See the spinning icon? Takes about 15 seconds."
- *Wait for load*
- "Now I see the notebook. Notice the structure: text cells explaining, code cells doing work."

**Step 2: Installing Packages (3 min)**
- "First code cell installs our GIS tools. I'll click this play button."
- *Run pip install cell*
- "See the progress bars? This downloads GeoPandas and related libraries. Takes 1-2 minutes."
- *While waiting, explain packages:* "GeoPandas is like QGIS's vector tools. Rasterio handles raster data. These are tools other people built and shared."
- *When complete:* "Green checkmark means success. You'll do this once per session."

**Step 3: Importing Libraries (2 min)**
- "Next cell loads the tools we installed."
- *Run import cell*
- `import geopandas as gpd` → "Loading GeoPandas, nicknaming it 'gpd' to save typing."
- `import matplotlib.pyplot as plt` → "Loading our plotting tools."
- "This is like opening QGIS—we're preparing our workspace."

**Step 4: Loading Data (3 min)**
- "This cell loads spatial data."
- *Run read_file cell*
- `gdf = gpd.read_file(url)` → "In QGIS: Layer → Add Vector Layer. In Python: read_file. Same result."
- "`gdf` is our nickname for this dataset. Could call it anything (cities, boundaries, etc.)"

**Step 5: Inspecting Data (3 min)**
- *Run gdf.head() cell*
- "Like the attribute table in QGIS! See the columns? The 'geometry' column stores shapes."
- *Run gdf.crs cell*
- "Checking coordinate system. Like right-clicking a layer in QGIS → Properties → CRS."

**Step 6: Creating a Map (5 min)**
- *Run basic plot cell*
- "Our first Python map!"
- *Compare to QGIS map on screen*
- "QGIS automatically chose colors and styling. Python shows default: all features, one color."
- *If notebook has styled version, run that:*
- "`column='field_name', cmap='viridis'` → Color by attribute. Like categorized symbology in QGIS."

**Step 7: Demonstrating Reproducibility (5 min)**
- "Notice: Every step is documented in code. If I send you this notebook, you can click 'Run all' and get identical results."
- "In QGIS, you'd need to remember: which menu, which tool, which parameters. Here, it's all written."
- *Show cell that does buffer:* `gdf.geometry.buffer(500)`
- "Compare to QGIS: Vector → Geoprocessing → Buffer → Type 500 → OK. Same operation, different interface."

**Step 8: Saving Work (2 min)**
- "File → Save a copy in Drive. This saves to your Google Drive."
- "Or File → Download to save locally."
- "Important: Colab sessions reset after inactivity. Save often!"

---

## Discussion Prompts

### Opening Discussion: Why Automate?
**Prompt:** "Think about your Week 6 project. If I asked you to re-do the exact same analysis for a different city, how long would it take you? What if I asked for 10 cities?"

**Follow-up:** "What information would someone need to replicate your analysis? Where is that information stored?"

### Mid-Session: Reproducibility in Your Field
**Prompt:** "Imagine you're working for a health department. You create a map showing COVID-19 hotspots. A journalist asks: 'How did you define a hotspot? What distance did you use for clustering?' How do you answer?"

**Follow-up:** "With QGIS alone, you'd need written notes. With Python notebooks, the code shows every decision. Which is more transparent?"

### Closing: Tool Selection Strategy
**Prompt:** "You need to map flood risk for 200 coastal cities. The workflow: download DEM, calculate elevation statistics, classify risk zones, export map. Which tool do you use: QGIS or Python? Why?"

**Expected answer:** Python (repetitive workflow, 200 iterations)

**Follow-up:** "What if it's just one city, but you're presenting to the mayor tomorrow and need a polished map?"

**Expected answer:** QGIS (quick styling, one-time use)

### Reflection: Your Learning Journey
**Prompt:** "Six weeks ago, you opened QGIS for the first time. Today you ran Python code. How does this feel different? What strategies from learning QGIS can you apply to learning Python?"

**Goal:** Help students recognize they've successfully learned complex tools before; they can do it again.

---

## Common Student Issues & Solutions

### Technical Issues

#### Issue 1: "Colab won't load / stuck on loading screen"
**Symptoms:** Gray screen, spinning icon for >1 minute
**Solutions:**
1. Refresh the page (Ctrl+R / Cmd+R)
2. Try a different browser (Chrome works best)
3. Check internet connection
4. Try incognito/private mode (clears cache)
5. Sign out of Google account, sign back in

#### Issue 2: "ModuleNotFoundError: No module named 'geopandas'"
**Symptoms:** Error when running `import geopandas`
**Solutions:**
1. Check if pip install cell ran successfully (scroll up, look for green checkmark)
2. Re-run the pip install cell
3. Look for red error text in pip install output (indicates installation failed)
4. If installation failed: Internet issue or Colab outage. Wait 5 minutes and retry.

#### Issue 3: "Name 'gdf' is not defined"
**Symptoms:** Error when trying to use dataset
**Root cause:** Didn't run cells in order
**Solutions:**
1. "Click Runtime → Run all" to execute all cells from top
2. Or manually run cells in sequence from top to bottom
3. Explain: "Code cells depend on previous cells. Like building blocks—you need the foundation first."

#### Issue 4: "File not found" when loading data
**Symptoms:** `FileNotFoundError` or `urllib.error.URLError`
**Solutions:**
1. Check URL is correct (copy-paste error?)
2. Internet connection dropped (retry)
3. Data source website is down (use backup URL)
4. If using uploaded files: File wasn't uploaded or session reset (re-upload)

#### Issue 5: Session disconnected / "Reconnect" button appears
**Symptoms:** Colab shows warning about disconnection
**Cause:** Inactivity timeout (~90 min) or closed laptop
**Solutions:**
1. Click "Reconnect"
2. Re-run pip install cell (environment was reset)
3. Re-run all cells in order
4. If working on long analysis: Save frequently, click cells periodically to stay active

#### Issue 6: Can't log in to Google account
**Symptoms:** Login loop, "Account not eligible"
**Solutions:**
1. Use personal Gmail (some school accounts restrict Colab)
2. Check if school/organization blocks Colab (firewall issue)
3. Create free personal Google account
4. Fall back to local Jupyter (if Anaconda installed)

### Conceptual/Learning Issues

#### Issue 7: "I don't understand what this code does"
**Response approach:**
1. Validate: "That's normal! You're learning a new language."
2. Break it down: Walk through line by line, translate to QGIS equivalent
3. Encourage reading text cells: "The explanation is usually just above the code."
4. Use analogies: "Think of functions like tools in QGIS. `buffer()` is the Buffer tool."

#### Issue 8: "I got an error and don't know how to fix it"
**Teaching moment:**
1. "Errors are good! They tell you what went wrong."
2. Read the last line of error message (most specific)
3. Common patterns:
   - `NameError` → Variable doesn't exist (didn't run earlier cell)
   - `TypeError` → Wrong data type (used string instead of number)
   - `KeyError` → Column name doesn't exist (typo in field name)
   - `FileNotFoundError` → Data not found (path wrong)
4. Google search: "Python [error type] [brief description]"

#### Issue 9: "This is too overwhelming / I'll never learn Python"
**Anxiety management response:**
1. Normalize: "You're not alone. Most GIS professionals felt this way."
2. Reframe goal: "You're not learning all of Python. You're learning just enough to automate spatial workflows."
3. Point to past success: "Remember opening QGIS in Week 1? Felt overwhelming then too."
4. Break it down: "Next week, you'll do things you've done before (load data, filter, join)—just in Python instead of QGIS."
5. Resources: "Office hours, extra tutorials, peer support."

#### Issue 10: "Why can't we just use QGIS for everything?"
**Valid question—address directly:**
1. "You absolutely can! QGIS is powerful."
2. "Python adds specific capabilities:" [list automation, reproducibility examples]
3. Real-world example: "Imagine updating 50 maps monthly. QGIS: 50 hours. Python: 10 minutes."
4. Show both: "Let's compare the same task in QGIS vs Python" [live demo]
5. Freedom: "After this course, you choose which tool fits each job."

---

## Addressing Python Anxiety

### Recognize the Shift
- Moving from GUI → Code is a bigger mental shift than learning a new GUI tool
- Students who excelled at QGIS may struggle initially with Python
- Non-linear learning curve: Feels hard at first, then clicks suddenly

### Strategies for Reducing Anxiety

#### 1. Normalize Struggle
**Say things like:**
- "If you feel lost, you're in good company. Most spatial analysts feel this way at first."
- "I still Google basic Python syntax after 10 years. That's normal."
- "Errors don't mean you're bad at this. Errors mean you're learning."

#### 2. Connect to Prior Knowledge
**Bridge from QGIS:**
- "You already know how to do a buffer. Now you're learning a different way to click the 'buffer' button."
- "Same spatial concepts, different interface."
- Map every Python operation to QGIS equivalent (visual anchor)

#### 3. Set Realistic Expectations
**Week 7 goals (achievable):**
- Run a notebook successfully
- Understand what each cell does (generally)
- See the connection between QGIS and Python

**NOT Week 7 goals:**
- Write Python from scratch
- Memorize syntax
- Understand advanced programming concepts

#### 4. Celebrate Small Wins
- "You just imported a library! That's step 1."
- "Your first Python map! Screenshot this—you'll want to remember."
- "You debugged an error yourself! That's a crucial skill."

#### 5. Provide Multiple Support Pathways
- Office hours for one-on-one help
- Peer study groups
- Optional extra tutorials (for curious students)
- "Stuck? Ask!" culture in class

#### 6. Use Analogies and Plain Language
**Avoid:** "We'll instantiate a GeoDataFrame object and invoke methods on the geometry attribute."
**Instead:** "We'll load our shapefile into a variable called `gdf`, then use the buffer tool on it."

**Examples:**
- Variable = nickname for data
- Function = tool in QGIS toolbar
- Import = opening software
- Library/package = toolbox of functions
- Error = notification that something needs fixing

#### 7. Show Imperfect Process
- Make intentional mistakes during demo: "Oops, I forgot to run the import cell. See the error? Let me fix it."
- Google something during class: "I can't remember the syntax. Let me look it up."
- Show your messy notebooks: "Real work is never perfect. We iterate."

#### 8. Offer Alternative Paths
**For students truly struggling:**
- "You can complete this course using primarily QGIS. Python is a bonus skill, not a requirement."
- "Some students prefer QGIS for the capstone—that's fine!"
- "Learning Python can happen after this course. We're just planting the seed."

#### 9. Pair Programming / Peer Support
- Pair anxious students with confident ones (reverse roles next week)
- "Help your neighbor" culture reduces isolation
- Students often explain concepts better to each other than instructor can

#### 10. Growth Mindset Language
**Fixed mindset:** "I'm not a programmer. I can't do this."
**Growth mindset:** "I haven't learned this yet, but I will with practice."

**Encourage:**
- "This is hard right now. That means you're learning."
- "You couldn't use QGIS 6 weeks ago. Look at you now."

---

## Wrap-Up & Preview

### Session Closing (5 minutes)

**Recap Key Takeaways:**
1. ✅ Python doesn't replace QGIS—they complement each other
2. ✅ Reproducibility matters for science, collaboration, and your future self
3. ✅ You successfully ran Python code today (celebrate!)
4. ✅ Week 8: Hands-on spatial analysis (things you've done before, now in Python)

**Address Concerns:**
- "Who feels nervous about next week?" [hands up]
- "That's normal. Remember: You already know the spatial concepts. You're just learning new syntax."

**Preview Week 8:**
- "Next week: Load shapefiles, filter by attributes, spatial joins, calculate areas—everything you've done in QGIS."
- "The notebook will guide you step-by-step. You won't be writing code from scratch."
- "Goal: By end of Week 8, you'll have a complete spatial analysis in Python."

**Homework Reminder:**
- Screenshot of completed notebook
- 5-10 sentence reflection
- **Deadline:** [Specify]
- "If you can't get the notebook running, come to office hours this week. Don't wait until next class!"

**Encouragement:**
- "You've learned QGIS, PostGIS, spatial analysis concepts. Python is just another tool."
- "Six weeks from now, you'll look back at today and be amazed at your progress."

### Post-Session Follow-Up

**Send email within 24 hours:**
- Link to Week 7 notebook (again)
- Office hours schedule
- Common troubleshooting tips
- Optional resources:
  - [GeoPandas documentation](https://geopandas.org/)
  - [Python for GIS tutorial](https://automating-gis-processes.github.io/site/)
  - [Google Colab tutorial](https://colab.research.google.com/notebooks/intro.ipynb)

**Monitor for struggling students:**
- Check submission screenshots—identify students who didn't complete notebook
- Reach out personally: "Saw you didn't submit Week 7. Need help getting set up?"
- Offer extra support before Week 8

**Prepare for next week:**
- Week 8 builds directly on Week 7—students MUST have Colab/Jupyter working
- First 10 minutes of Week 8: Quick recap + final troubleshooting
- Have advanced material ready for students who are racing ahead

---

## Additional Resources for Facilitators

### Recommended Pre-Reading
- [Teaching Python to GIS Students](https://www.directionsmag.com/article/9831) (strategies)
- [GeoPandas documentation](https://geopandas.org/) (for your own reference)
- [Jupyter Notebook best practices](https://jupyter-notebook.readthedocs.io/en/stable/notebook.html)

### Advanced Topics (if students ask)
**"Can we use VS Code instead of Jupyter?"**
- Yes, but recommend Jupyter for this course (better for learning, shows output inline)
- VS Code + Jupyter extension works great for advanced users

**"What about QGIS Python console (PyQGIS)?"**
- Different from GeoPandas Python
- PyQGIS automates QGIS itself
- GeoPandas is standalone Python for GIS
- Both valuable—this course focuses on GeoPandas (more portable, better for reproducibility)

**"Should we learn R instead?"**
- Both Python and R are excellent for GIS
- Python: More general-purpose, better for web apps, automation
- R: Stronger statistics, great visualization (ggplot2)
- This course uses Python; principles transfer to R

**"What about ArcPy?"**
- ArcPy = Python library for ArcGIS (Esri)
- Requires ArcGIS license (expensive)
- GeoPandas is open-source, free, cross-platform
- Skills transfer between them

### Troubleshooting: Facilitator Technical Issues

**Problem: Your demo Colab won't connect**
- Switch to pre-recorded demo video
- Or use local Jupyter (why you tested beforehand!)
- Or show screenshots + explain verbally

**Problem: Package installation failing for everyone**
- Possible Colab outage (check status.cloud.google.com)
- Fall back to discussion-heavy session (QGIS vs Python comparison)
- Reschedule hands-on for next class

**Problem: Students have wildly different tech literacy**
- Pair students: tech-savvy with beginners
- Provide "fast track" bonus challenges for advanced students
- Offer basic support resources for struggling students

---

## Notes for Future Iterations

**Things to improve based on student feedback:**
- [ ] Time allocation (was 30 min hands-on enough?)
- [ ] Technical issues encountered (document for future prevention)
- [ ] Anxiety level (how can we reduce further?)
- [ ] Pacing (too fast? too slow?)

**Student quotes to collect:**
- Successes ("Aha!" moments)
- Struggles (where did confusion happen?)
- Suggestions (what would have helped?)

**Metrics to track:**
- % students who successfully ran notebook
- % who needed one-on-one help
- % who seemed overwhelmed vs. confident
- Common errors encountered

**Adjust for next year:**
- More pre-class setup instructions?
- Pre-recorded video walkthrough?
- Simplified starter notebook?
- More time on reproducibility discussion?

---

## Quick Reference: Facilitator Cheat Sheet

### Opening Lines
"Welcome to the bridge! You've mastered QGIS—today we're adding Python to your toolkit. Not replacing QGIS, adding to it."

### Key Analogies
- Variable = nickname for data
- Function = QGIS tool
- Library = toolbox
- Error = helpful notification (not failure!)
- Jupyter = lab notebook with executable instructions

### Calming Phrases (for anxious students)
- "This is completely normal."
- "You already know the spatial concepts—just learning new buttons."
- "I Google this syntax all the time."
- "Errors mean you're learning."

### Emergency Pivots
- Internet fails → Use screenshots + discussion
- Colab down → Local Jupyter demo
- Students lost → Pair programming rescue

### Time Checks
- 15 min: Intro/context done
- 30 min: Transition + reproducibility discussed
- 60 min: Live demo complete
- 90 min: Students have run notebook
- 105 min: Discussion complete
- 120 min: Wrap-up done

### Success Criteria
By end of session, students should:
- [ ] Have opened Colab
- [ ] Run at least one code cell
- [ ] Seen a Python-generated map
- [ ] Understand Python complements QGIS
- [ ] Feel cautiously optimistic (not terrified)

---

**Remember:** Your energy sets the tone. If you're enthusiastic and relaxed about Python, students will mirror that. If you're anxious about teaching code, they'll absorb that anxiety. Position Python as a helpful tool, not a scary hurdle.

**You've got this!** Week 7 is a pivot point—students will remember this as the week they became coders (even if they don't feel like it yet). Make it supportive, achievable, and even fun.
