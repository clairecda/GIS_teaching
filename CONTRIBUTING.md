# Contributing & Instructor Guide

This document covers how to run, customize, and contribute to the Introduction to GIS course.

## Repository structure

```
├── site_docs/              # Course website content (MkDocs)
│   ├── weeks/              # Weekly student guides
│   ├── lectures/           # Lecture notes
│   ├── readings/           # Background readings
│   ├── onboarding/         # Setup guides
│   └── reference/          # Quick references
├── notebooks/              # Python notebooks (weeks 7-10)
├── facilitator_notes/      # Instructor guides (not published)
├── assets/slides/          # HTML lecture slides
├── mkdocs.yml              # Site configuration
└── README.md               # Public landing page
```

## Running the site locally

```bash
# Install dependencies
pip install mkdocs mkdocs-material pymdown-extensions

# Preview locally (auto-refreshes on changes)
mkdocs serve

# Build static site
mkdocs build

# Deploy to GitHub Pages
mkdocs gh-deploy
```

## For instructors

### Facilitator notes

Detailed teaching guides are in `facilitator_notes/` (not published to the website):

- Session flow with timing
- Live demo scripts
- Discussion prompts
- Common student issues and solutions

### Generating slides

```bash
python assets/slides/generate_slides.py
```

### Python notebooks

Notebooks are designed to run in **Google Colab** with data stored in Google Drive:

1. Students click "Open in Colab" links
2. Notebooks auto-detect Colab and install packages
3. Students mount their Google Drive to access data files
4. Outputs save back to Drive

The notebooks explain this workflow with clear instructions about what "mounting" means.

## Customizing the course

### Editing content

1. Edit markdown files in `site_docs/`
2. Preview with `mkdocs serve`
3. Update `mkdocs.yml` if adding/removing pages
4. Deploy with `mkdocs gh-deploy`

### Data sources

Students download data from various sources (Natural Earth, ABS, OpenStreetMap). Update the data guides in:
- `site_docs/onboarding/03-download-data.md`
- `site_docs/reference/data-download-checklist.md`

### Weekly topics

The 12-week structure can be adapted:
- **Weeks 1-6:** QGIS fundamentals (flexible order)
- **Week 7:** Bridge to Python (required before weeks 8-10)
- **Weeks 8-10:** Python workflows (can be reordered)
- **Weeks 11-12:** Design and capstone

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Test with `mkdocs serve`
4. Submit a pull request

### Style guidelines

- Use Australian English spelling
- Follow existing markdown structure
- Include QGIS-to-Python comparisons where relevant
- Document data sources and licensing

## License

- **Code** (notebooks, scripts): MIT License
- **Content** (lectures, guides): CC BY 4.0

Attribution:
```
Introduction to GIS course materials © 2025 Claire Boulange, licensed under CC BY 4.0.
```
