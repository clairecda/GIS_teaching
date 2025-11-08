# Accessing Course Materials

This guide explains how to access course materials and download the notebooks you'll need for Weeks 8-10.

## What you need

**For Weeks 1-6 (QGIS):**
- QGIS installed on your computer
- Datasets downloaded following weekly guides

**For Weeks 7-10 (Python):**
- Everything above, PLUS:
- Anaconda installed (see [Anaconda Setup Guide](anaconda-setup.md))
- Jupyter notebooks downloaded (explained below)

## How to get notebooks (Weeks 8-10)

**Simple approach (recommended):**

Each week, download the notebook directly from the course website:

1. **Go to the weekly instructions** (e.g., Week 8)
2. **Click the notebook download link** at the top of the page (e.g., "Download week08_vector_workflows.ipynb")
3. **Save the notebook** to your `intro-gis/notebooks/` folder (the one you created in Week 7)

That's it! No Git required.

**Where to save notebooks:**
```
intro-gis/
├── notebooks/          ← Save downloaded notebooks here
│   ├── week08_vector_workflows.ipynb
│   ├── week09_raster_remote_sensing.ipynb
│   └── week10_transport_networks.ipynb
├── data/               ← Save datasets here
└── exports/            ← Your outputs go here
```

---

## Opening notebooks in Jupyter

After downloading the notebooks, here's how to use them:

1. **Activate your conda environment:**
   ```bash
   conda activate intro-gis
   ```

2. **Navigate to your notebooks folder:**
   ```bash
   cd ~/Desktop/intro-gis/notebooks    # Mac/Linux
   cd %USERPROFILE%\Desktop\intro-gis\notebooks    # Windows
   ```

3. **Launch Jupyter Lab:**
   ```bash
   jupyter lab
   ```

4. **Your browser opens** — click on the notebook to start working!

---

## Alternative: Clone the repository (optional, for advanced users)

If you're comfortable with Git and want all materials at once, you can clone the course repository.

**Benefits:**
- Get all notebooks at once
- Easy to update if instructor makes changes
- Access to environment configuration files

**How to clone (brief instructions):**

1. **Install Git** if you don't have it:
   - Windows: [git-scm.com](https://git-scm.com/)
   - Mac: Type `git --version` in Terminal (auto-installs)
   - Linux: `sudo apt install git`

2. **Get the repository URL** from your instructor

3. **Clone it:**
   ```bash
   cd ~/Desktop    # or wherever you want it
   git clone [REPOSITORY_URL]
   cd intro-to-gis
   ```

4. **Get updates later:**
   ```bash
   cd intro-to-gis
   git pull
   ```

---

## Common questions

### "Do I need to know Git/GitHub?"

**No!** For this course, just download notebooks from the weekly pages. Git is optional for advanced users.

### "How do I get updates if the instructor fixes a notebook?"

If you downloaded manually: Just re-download the fixed version from the website.

If you cloned: Run `git pull` in the repository folder.

### "Where do I put the datasets?"

Put data in: `intro-gis/data/` (follow each week's data download guide for specifics)

### "Can't open notebooks in Jupyter?"

Make sure you:
1. Completed Week 7 Anaconda setup
2. Activated your environment: `conda activate intro-gis`
3. Are in the right folder: `cd intro-gis/notebooks`
4. Launched Jupyter: `jupyter lab`

### "Can I work on Google Colab instead?"

Yes! You can upload notebooks to Colab, but you'll need to:
- Upload datasets to your Google Drive
- Modify file paths in the notebook
- Install packages at the start of each session

Anaconda on your computer is recommended for this course.

---

## Getting help

**Environment issues?**
- Check the [Anaconda Setup Guide](anaconda-setup.md)
- Review [Week 7](../weeks/week07.md) setup instructions

**Can't access the website?**
- Check the URL with your instructor
- Try a different browser

**Other issues?**
- Ask your instructor or classmates
- Check troubleshooting sections in weekly guides

---

**That's it!** You don't need to understand Git to take this course. Just download notebooks from the weekly pages when you need them.
