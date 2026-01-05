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

Colab comes with basic Python, but not with GIS tools. You need to install them.

**What is `pip install`?**

`pip` is Python's package manager—it downloads and installs code libraries that other people wrote. When you run `pip install geopandas`, you're downloading the GeoPandas library (for working with maps) from the internet.

Run this cell at the top of each notebook:

```python
# Run this first in Colab
!pip install geopandas rasterio rasterstats osmnx contextily folium -q
```

| Package | What it does |
|---------|--------------|
| `geopandas` | Read/write/analyze spatial data (like shapefiles) |
| `rasterio` | Work with raster images (satellite data, DEMs) |
| `osmnx` | Download street networks from OpenStreetMap |
| `contextily` | Add basemaps to your plots |
| `folium` | Create interactive web maps |

This takes about 1-2 minutes. The `-q` means "quiet" (less output text).

!!! warning "You must run this every session"
    Colab environments reset when you close the tab or after ~90 minutes of inactivity. Each time you reconnect, run the pip install cell again.

### Step 4: Access your data

Colab runs in the cloud, so you need to get your data files into the Colab environment. Choose the method that works best for you:

=== "Option 1: Upload files (simplest)"

    1. Click the **folder icon** in the left sidebar to open the file browser
    2. Click the **upload icon** (paper with arrow)
    3. Select your data files (`.geojson`, `.shp`, `.tif`, etc.)
    4. Wait for upload to complete
    5. Access files with: `gpd.read_file("filename.geojson")`

    !!! warning "Uploads are temporary"
        Uploaded files are deleted when your session ends. Re-upload each time you reconnect.

=== "Option 2: Google Drive (persistent)"

    Connect your Google Drive so files stay saved between sessions.

    **Step 1: First, organize your Drive**

    1. Open [Google Drive](https://drive.google.com) in a new tab
    2. Click **+ New** → **New folder**
    3. Name it `intro-gis`
    4. Upload your data files into this folder

    **Step 2: Mount Drive in Colab**

    1. In your Colab notebook, create a new code cell
    2. Type this code:
    ```python
    from google.colab import drive
    drive.mount('/content/drive')
    ```
    3. Run the cell (Shift + Enter)
    4. A popup appears asking permission — click **Connect to Google Drive**
    5. Choose your Google account
    6. Click **Allow** to give Colab access
    7. When successful, you'll see: `Mounted at /content/drive`

    **Step 3: Access your files**

    Your Drive files are now at `/content/drive/MyDrive/`. To load a file:
    ```python
    # If your file is in Drive > intro-gis > data
    gdf = gpd.read_file("/content/drive/MyDrive/intro-gis/data/boundaries.geojson")
    ```

    **How to find the correct path:**

    1. Click the **folder icon** (📁) in Colab's left sidebar
    2. Click **drive** → **MyDrive** → navigate to your file
    3. Right-click the file → **Copy path**
    4. Paste the path in your code

    !!! tip "Best for larger projects"
        Files in Drive persist forever. You won't need to re-upload each session.

=== "Option 3: Load from URL (no upload needed)"

    If data is hosted online, load it directly:

    ```python
    # Load from a URL
    url = "https://example.com/data/boundaries.geojson"
    gdf = gpd.read_file(url)
    ```

    The course notebooks include sample data URLs where possible.

### Step 5: Save your work

- **To Google Drive:** `File → Save a copy in Drive`
- **To your computer:** `File → Download → Download .ipynb`

!!! tip "Save early, save often"
    Colab sessions timeout after ~90 minutes of inactivity. Save your work regularly!

### That's it!

You're ready for Week 7. No terminal commands, no environment setup.

---

## Option B: Local Setup (Anaconda)

Install Python and packages on your computer for faster performance and offline access.

### Step 0: Create your workspace (if you haven't already)

Make sure you have the folder structure from the [Data Download Guide](03-download-data.md):

```
Desktop/
└── intro-gis/
    ├── data/
    │   ├── raw/
    │   └── processed/
    ├── outputs/
    ├── projects/
    └── notebooks/    ← Save notebooks here
```

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

**What is an environment?**

An environment is like a separate workspace for Python. It keeps this course's packages isolated from other Python projects. If something breaks, you can delete the environment and start fresh without affecting anything else.

**Open your terminal:**

- **Windows:** Click Start, search for "**Anaconda Prompt**" (not regular Command Prompt!)
- **Mac:** Open **Terminal** (Applications > Utilities > Terminal)
- **Linux:** Open your terminal application

**Run these commands one at a time:**

```bash
# Step 1: Create a new environment called "intro-gis" with Python 3.11
conda create -n intro-gis python=3.11 -y

# Step 2: Activate (switch to) this environment
conda activate intro-gis

# Step 3: Install GIS packages into this environment
conda install -c conda-forge geopandas rasterio rioxarray osmnx networkx rasterstats contextily folium jupyter jupyterlab matplotlib seaborn -y
```

| Command | What it does |
|---------|--------------|
| `conda create -n intro-gis` | Creates a new environment named "intro-gis" |
| `conda activate intro-gis` | Switches to using that environment |
| `conda install -c conda-forge ...` | Downloads packages from conda-forge (a package repository) |
| `-y` | Auto-confirms prompts (so you don't have to type "yes") |

This downloads about 500 MB and takes 5-15 minutes. You'll see progress bars as packages download.

!!! tip "How to know you're in the right environment"
    When the environment is active, your terminal prompt shows `(intro-gis)` at the beginning:
    ```
    (intro-gis) C:\Users\Claire>
    ```
    If you see `(base)` instead, run `conda activate intro-gis` again.

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

**"FileNotFoundError" when loading data**
- File wasn't uploaded or path is wrong
- Check the file browser (folder icon) to see uploaded files
- Use the exact filename: `gpd.read_file("myfile.geojson")` not `gpd.read_file("data/myfile.geojson")`

**Uploaded files disappeared**
- Colab sessions reset after ~90 minutes of inactivity
- Re-upload your files, or use Google Drive for persistent storage

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
3. Upload data files OR mount Google Drive
4. Work through notebook
5. Save to Drive or download

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
