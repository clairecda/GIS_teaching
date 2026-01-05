# Week 7 Lecture · Bridge to Python & Reproducibility

## This week
This week marks your transition from QGIS's graphical interface to Python-based spatial analysis. You'll set up Anaconda, create your first Python environment, and explore why reproducibility matters for collaboration, auditing, and publishing spatial research.

## By the end of the week you will
- Explain why reproducibility matters in spatial analysis and how Python supports it.
- Install Anaconda and create a working `intro-gis` environment with spatial packages.
- Understand project organization best practices (folder structure, relative paths, documentation).
- Run your first GeoPandas commands in a Jupyter notebook.

## Key vocabulary
Anaconda · Conda environment · GeoPandas · Jupyter Notebook · reproducibility · virtual environment · package management · relative paths · documentation · version control.

## Reproducibility as accountability

We often frame reproducibility as a technical practice—version control, environments, documentation. But reproducibility is fundamentally about **accountability**: Can someone else verify what you did and why?

**Why this matters beyond convenience:**

- A spatial analysis that justifies a highway route, rezoning decision, or resource allocation should be auditable
- "I ran it through GIS" is not an explanation. Which tools? Which parameters? Which version of the data?
- Reproducible workflows make assumptions visible—and visible assumptions can be questioned

**Who can reproduce?**

Reproducibility assumes access:

- Software licenses and computing resources aren't universally available
- Code-based workflows require programming skills—this shifts who can participate in verification
- Open data initiatives help, but many critical datasets remain proprietary or paywalled

**The limits of reproducibility:**

- A workflow can be perfectly reproducible and still encode bias in its design
- Reproducing flawed methods at scale doesn't make them correct—it makes them efficiently wrong
- The most important choices (which question to ask, which boundaries to use, which populations to include) often happen before the reproducible part begins

**Professional practice:**

Documenting your work isn't just about getting the same answer twice—it's about enabling others to ask whether it was the right answer in the first place.

## What happens in class
- Discuss why spatial analysts are shifting from GUI tools to code-based workflows.
- Walk through Anaconda installation and environment creation together.
- Demonstrate activating environments and launching Jupyter notebooks.
- Compare a QGIS workflow to its Python equivalent (loading data, styling, exporting).
- Troubleshoot installation issues and verify package imports work.

## Prepare beforehand
- Download Anaconda installer for your operating system (from [anaconda.com/download](https://www.anaconda.com/download)).
- Review the [Python Setup Guide](../onboarding/04-python-setup.md) and note any system-specific requirements.
- Think about one repetitive QGIS task you'd like to automate with Python.

## Connected lab
This week's lab guides you through creating the `intro-gis` environment, verifying package installations, and running your first spatial analysis in Jupyter—loading Natural Earth data, creating a simple map, and exporting it programmatically.

