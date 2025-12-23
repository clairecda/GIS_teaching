# 4. Python Setup (Week 7+)

Starting Week 7, you'll use Python for GIS analysis. There are two ways to run the course notebooks:

| Option | Best for | Setup time |
|--------|----------|------------|
| **Google Colab** (Recommended) | Most students, quick start, Chromebooks | 2 minutes |
| **Local (Anaconda)** | Advanced users, large datasets, offline work | 30-45 minutes |

**When to do this:** Before Week 7. Skip for Weeks 1-6.

---

## Option A: Google Colab (Recommended)

Google Colab runs Python in your browser — no installation required.

### Step 1: Get a Google account

You need a Google account to use Colab. If you have Gmail, you're already set.

### Step 2: Open a course notebook

1. Go to the [Notebooks page](../reference/notebooks.md)
2. Click the **"Open in Colab"** button for Week 7
3. Sign in with your Google account if prompted

### Step 3: Install GIS packages

Colab doesn't have GIS packages pre-installed. Run this cell at the top of each notebook:

```python
# Run this first in Colab
!pip install geopandas rasterio rasterstats osmnx contextily folium -q
```

This takes about 1-2 minutes. You'll need to run it each time you open a notebook (Colab environments reset).

### Step 4: Save your work

- **To Google Drive:** `File → Save a copy in Drive`
- **To your computer:** `File → Download → Download .ipynb`

!!! tip "Save early, save often"
    Colab sessions timeout after ~90 minutes of inactivity. Save your work regularly!

### That's it!

You're ready for Week 7. No terminal commands, no environment setup.

---

## Option B: Local Setup (Anaconda)

Install Python and packages on your computer for faster performance and offline access.

### Step 1: Download Anaconda

1. Go to [anaconda.com/download](https://www.anaconda.com/download)
2. Download the installer for your operating system
3. The file is about 600 MB

### Step 2: Install Anaconda

=== "Windows"
    1. Double-click the downloaded `.exe` file
    2. Click **Next** through the welcome screens
    3. Accept the license agreement
    4. Choose "Just Me" for installation type
    5. Check both boxes:
       - "Add Anaconda to my PATH environment variable"
       - "Register Anaconda as my default Python"
    6. Click **Install** (takes 10-15 minutes)

=== "Mac"
    1. Double-click the downloaded `.pkg` file
    2. Click **Continue** through the screens
    3. Accept the license agreement
    4. Click **Install** and enter your password
    5. Wait 10-15 minutes

=== "Linux"
    1. Open Terminal
    2. Run: `bash ~/Downloads/Anaconda3-*.sh`
    3. Press Enter to read the license, type `yes` to accept
    4. Press Enter for default location
    5. Type `yes` to initialize conda
    6. Close and reopen Terminal

### Step 3: Create your GIS environment

Open your terminal:
- **Windows:** Search for "Anaconda Prompt" in Start menu
- **Mac/Linux:** Open Terminal

Run these commands:

```bash
conda create -n intro-gis python=3.11 -y
conda activate intro-gis
conda install -c conda-forge geopandas rasterio rioxarray osmnx networkx rasterstats contextily folium jupyter jupyterlab matplotlib seaborn -y
```

This downloads about 500 MB and takes 5-15 minutes.

### Step 4: Test your setup

```bash
python -c "import geopandas; import rasterio; import osmnx; print('All packages installed!')"
```

You should see: `All packages installed!`

### Step 5: Launch Jupyter

```bash
conda activate intro-gis
jupyter lab
```

Your browser opens with Jupyter. You're ready!

---

## Colab vs Local: When to use which

| Scenario | Use Colab | Use Local |
|----------|-----------|-----------|
| First time trying Python | ✓ | |
| Quick exploration | ✓ | |
| Working on Chromebook | ✓ | |
| Slow/unreliable internet | | ✓ |
| Large local datasets (>100MB) | | ✓ |
| Capstone project | | ✓ |
| Need specific package versions | | ✓ |

!!! note "You can switch anytime"
    Start with Colab. If you find you need local setup later (for the capstone or large datasets), you can install Anaconda then.

---

## Troubleshooting

### Colab issues

**"ModuleNotFoundError" for geopandas/rasterio**
- Run the `!pip install ...` cell at the top of the notebook
- Make sure it completed without errors

**Session disconnected / timed out**
- Colab sessions reset after inactivity
- Re-run cells from the top, including the pip install cell

**"You must enable billing" error**
- You're trying to use too much memory
- Reduce dataset size or switch to local setup

### Anaconda issues

**"conda: command not found"**
- Windows: Use "Anaconda Prompt" not Command Prompt
- Mac/Linux: Run: `echo 'export PATH="$HOME/anaconda3/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc`

**Package installation failed**
- Try one at a time: `conda install -c conda-forge geopandas -y`

**"ModuleNotFoundError" in Jupyter**
- Activate environment first: `conda activate intro-gis`
- Then launch: `jupyter lab`

**Start over completely**
```bash
conda deactivate
conda env remove -n intro-gis
```
Then redo Step 3.

---

## Quick reference

### Colab workflow
1. Open notebook from [Notebooks page](../reference/notebooks.md)
2. Run pip install cell
3. Work through notebook
4. Save to Drive or download

### Local workflow
```bash
conda activate intro-gis
cd ~/Desktop/intro-gis
jupyter lab
# Work on notebooks
# Ctrl+C to close
```

---

**You're ready for Week 7!** Choose Colab to start quickly, or set up Anaconda if you prefer local development.
