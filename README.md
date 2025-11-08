# Introduction to GIS with Python

A 12-week, project-based introduction to geographic information systems that transitions learners from QGIS fundamentals to Python-based spatial analysis. This repository contains all course materials, including lecture content, weekly labs, Jupyter notebooks, and supporting resources.

## Course Overview

This course teaches GIS through practical application across crime analysis, public health, environmental science, and transport planning. Students begin with QGIS's graphical interface (weeks 1-6), transition to reproducible Python workflows (weeks 7-10), and conclude with map design and a capstone project (weeks 11-12).

**Target audience:** Beginners comfortable with command-line tools; Python experience helpful but not required.

**Learning outcomes:** Students will master QGIS operations, understand vector/raster data and coordinate systems, perform spatial analysis in Python (GeoPandas, Rasterio, OSMnx), and create publication-quality maps following cartographic principles.

## Course Structure

### Weeks 1-6: QGIS Fundamentals
- **Week 1:** QGIS installation, interface navigation, project setup, coordinate reference systems
- **Week 2:** Symbology, map layouts, print composer, typography and visual hierarchy
- **Week 3:** Vector analysis, attribute tables, field calculator, spatial joins
- **Week 4:** Raster data, terrain analysis, interpolation, contour generation
- **Week 5:** Crime hotspot mapping, kernel density, temporal filtering
- **Week 6:** Public health accessibility, network analysis, service area modeling

### Week 7: Python Transition
- Reproducible environment setup (conda, Docker, dev containers)
- Jupyter notebook orientation
- Moving from GUI to code-based workflows

### Weeks 8-10: Python Automation
- **Week 8:** Vector workflows with GeoPandas (cleaning, joins, exports)
- **Week 9:** Raster and remote sensing with Rasterio/xarray (zonal statistics, change detection)
- **Week 10:** Network analysis with OSMnx (routing, isochrones, GTFS)

### Weeks 11-12: Design & Capstone
- **Week 11:** Map design studio (accessibility, storytelling, portfolio development)
- **Week 12:** Student-defined capstone project and presentation

## Deployment & Student Access

### Publishing the Course Website

This course is designed to be deployed as a static website using MkDocs. Students access weekly instructions, lectures, and readings via the website, then clone the repository to get notebooks.

**Recommended workflow:**

1. **Deploy the MkDocs site** (GitHub Pages, Read the Docs, or similar)
2. **Make the repository public** (or provide access to students)
3. **Students use both:**
   - Website for instructions and readings
   - Repository for notebooks and environment files

### Deployment Options

**Option A: GitHub Pages (Recommended)**

```bash
# Build and deploy
mkdocs gh-deploy
```

This creates a `gh-pages` branch with the built site. Enable GitHub Pages in repository settings.

**Option B: Manual deployment**

```bash
# Build to site/ directory
mkdocs build

# Upload site/ to your web host
```

**Update the following after deployment:**
1. Add site URL to this README
2. Update `[INSERT REPO URL]` placeholders in `site_docs/onboarding/accessing-course-materials.md`
3. Add site link to `site_docs/index.md`

### Student Access Pattern

Students need access to **two things:**

1. **Course website** (deployed MkDocs site) - For weekly instructions. Latest deployment: https://clairecda.github.io/GIS_teaching/
2. **GitHub repository** (cloned or downloaded) - For notebooks and environment files

See `site_docs/onboarding/accessing-course-materials.md` for the student-facing guide that explains this.

## For Instructors

### Building the Course Site Locally

The course content is organized as a MkDocs site. To preview locally:

```bash
# Install dependencies
pip install mkdocs mkdocs-material

# Serve locally at http://127.0.0.1:8000
mkdocs serve

# Build static site to site/ directory
mkdocs build
```

The site configuration is in `mkdocs.yml`. Course content lives in `site_docs/`:
- `site_docs/weeks/` - Weekly lab instructions
- `site_docs/lectures/` - Lecture content for each week
- `site_docs/onboarding/` - Getting started guides (QGIS install, data downloads, environment setup)
- `site_docs/reference/` - Quick references, checklists, and templates
- `site_docs/dev/` - Instructor notes and draft materials

### Generating Slides

HTML slide decks for lectures are generated from Python:

```bash
# Run from repository root
python assets/slides/generate_slides.py
```

This creates `assets/slides/week01.html` through `week12.html`. Slides feature:
- Professional teal/blue theme matching the MkDocs site
- Keyboard navigation (arrows, spacebar, Home/End)
- Responsive design and print-friendly CSS
- Accessible markup with ARIA labels

Edit the `SLIDES` dictionary in `generate_slides.py` to modify content.

### Repository Layout

```
├── site_docs/              # MkDocs source (student-facing content)
│   ├── weeks/              # Weekly lab guides
│   ├── lectures/           # Lecture content
│   ├── onboarding/         # Setup instructions
│   ├── reference/          # Cheat sheets and templates
│   └── dev/                # Instructor development notes
├── resources/              # Supporting materials
│   ├── notebooks/          # Jupyter notebooks for weeks 8-10
│   ├── data/               # Spatial datasets (raw/, processed/, external/)
│   ├── docs/               # Archived legacy materials
│   └── environment/        # Conda environment files
├── assets/                 # Media and slides
│   └── slides/             # HTML slide decks + generation script
├── .devcontainer/          # VS Code dev container configuration
├── mkdocs.yml              # MkDocs site configuration
├── README.md               # This file
├── LICENSE                 # MIT License for code
└── CONTENT_LICENSE.md      # CC BY 4.0 for course materials
```

### Python Environment

Students can choose from three environment options:

1. **Dev container** (recommended): VS Code + Docker setup in `.devcontainer/`
2. **Local conda**: `conda env create -f resources/environment/environment.yml`
3. **Google Colab**: Lightweight cloud option for students without local setup

The environment includes: GeoPandas, Rasterio, xarray, OSMnx, matplotlib, and Jupyter.

Verification script: `resources/environment/verify_setup.py`

### Datasets

Course datasets cover crime, health, environmental, and transport domains. Data sources and licensing details are documented in `site_docs/reference/data-inventory.md`.

Data is organized in `resources/data/`:
- `raw/` - Original downloads (not version controlled - add to `.gitignore`)
- `processed/` - Cleaned datasets ready for labs
- `external/` - Third-party datasets with attribution

Students follow `site_docs/onboarding/data-downloads.md` to acquire weekly datasets.

!!! note "Data not included in repository"
    Datasets are not included in this repository due to size and licensing. Instructors and students must download data following the guides in `site_docs/onboarding/`.

### Notebooks

Python notebooks for weeks 8-10 are in `resources/notebooks/`:
- `week08_vector_workflows.ipynb` - GeoPandas operations
- `week09_raster_remote_sensing.ipynb` - Raster processing
- `week10_transport_networks.ipynb` - Network analysis

Each notebook includes:
- Learning objectives
- Step-by-step guided exercises
- Independent challenges
- Reflection prompts

## Contributing

Contributions are welcome. Please:
- Follow the existing structure in `site_docs/`
- Update `mkdocs.yml` navigation when adding new pages
- Regenerate slides after modifying `generate_slides.py`
- Test MkDocs builds locally before submitting changes
- Document data sources in the inventory

## Licensing

- **Code** (notebooks, scripts, dev containers): [MIT License](LICENSE)
- **Course content** (lectures, guides, slides): [Creative Commons Attribution 4.0 International](CONTENT_LICENSE.md)

When reusing materials, attribute as:
```
Introduction to GIS course materials © 2025 Claire Boulange, licensed under CC BY 4.0.
```

## Course Philosophy

This course emphasizes:
- **Progressive disclosure:** Start with visual interfaces before introducing code
- **Applied learning:** Every week addresses real-world problems in specific domains
- **Reproducibility:** Python workflows promote transparent, shareable analysis
- **Design thinking:** Maps are communication tools; cartography matters
- **Equity awareness:** Critical examination of how GIS intersects with social justice

Students emerge with both technical skills and critical thinking about when and how to apply spatial analysis ethically.

## Quick Start for Students

1. **Access the course website:** https://clairecda.github.io/GIS_teaching/
2. **Read the getting started guide:** [Accessing Course Materials](site_docs/onboarding/accessing-course-materials.md)
3. **Install QGIS:** Follow [QGIS Installation Guide](site_docs/onboarding/qgis-install.md)
4. **Download Week 1 data:** See [Data Downloads Guide](site_docs/onboarding/data-downloads.md)
5. **Clone repository (Week 7):** Follow [Accessing Course Materials](site_docs/onboarding/accessing-course-materials.md) to get notebooks

## Support & Issues

- **Questions about content:** Contact your instructor
- **Technical issues:** Check troubleshooting guides in `site_docs/onboarding/`
- **Repository issues:** Open an issue on GitHub

---

**Built with:** MkDocs, MkDocs Material theme, Python, QGIS, Jupyter
**Last updated:** 2025
