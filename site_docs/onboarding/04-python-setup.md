# 4. Python Setup (Week 7+)

Starting Week 7, you'll use Python for GIS analysis. There are two ways to run the course notebooks:

| Option | Best for | Setup time |
|--------|----------|------------|
| **Google Colab** (Recommended) | Most students, quick start, Chromebooks | 5 minutes |
| **Local (Anaconda)** | Advanced users, large datasets, offline work | 30-45 minutes |

**When to do this:** Before Week 7. Skip for Weeks 1-6.

---

## Option A: Google Colab (Recommended)

### What is Google Colab?

Google Colab lets you run Python code in your browser—no installation needed. The code runs on Google's servers.

**Think of it like Google Docs for code.**

### The key concept: Where does the code run?

```
┌─────────────────────────────────────────────────────────────────┐
│                        YOUR COMPUTER                             │
│  ┌─────────────┐                                                │
│  │   Browser   │  ← You type code here                          │
│  └─────────────┘                                                │
│        │                                                        │
│        │  Your code is sent over the internet                   │
│        ▼                                                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     GOOGLE'S SERVERS                             │
│  ┌─────────────┐     ┌─────────────┐                            │
│  │   Colab     │ ←── │   Google    │                            │
│  │   Runtime   │     │   Drive     │                            │
│  └─────────────┘     └─────────────┘                            │
│   Code runs here      Your files go here                        │
└─────────────────────────────────────────────────────────────────┘
```

**The problem:** Colab can't see your laptop's files.

**The solution:** Store files in Google Drive, then connect ("mount") Drive to Colab.

---

### Step 1: Set up your Google Drive

Mirror your local folder structure in Google Drive:

```
My Drive/
└── intro-gis/
    ├── week07/
    │   ├── data/
    │   │   ├── raw/        ← Upload data here
    │   │   └── processed/  ← Outputs saved here
    │   └── exports/
    ├── week08/
    │   └── (same structure)
    └── ...
```

**To create:**
1. Go to [drive.google.com](https://drive.google.com)
2. Click **+ New** → **New folder** → name it `intro-gis`
3. Inside, create `week07`
4. Inside week07, create `data`, then inside data create `raw` and `processed`
5. Create `exports` folder inside week07

---

### Step 2: Upload your data

Upload files to the correct week's `raw/` folder:

- Week 8: `week08/data/raw/neighbourhoods.geojson`, `incidents.geojson`
- Week 9: `week09/data/raw/sentinel_before.tif`, etc.

---

### Step 3: Open a course notebook

1. Go to the weekly lab page (e.g., [Week 7](../weeks/week07.md))
2. Click **"Open in Colab"**
3. Sign in with your Google account

---

### Step 4: Run the setup cell

Every notebook starts with a setup cell. Click it and press **Shift + Enter**.

This installs GIS packages (~1 minute).

---

### Step 5: Mount your Google Drive

**What does "mount" mean?**

Like plugging in a USB drive—it connects your Drive so Colab can see your files.

Run this cell:
```python
from google.colab import drive
drive.mount('/content/drive')
```

Click **Connect to Google Drive** → Choose your account → **Allow**

Now your files are accessible at `/content/drive/MyDrive/intro-gis/week07/data/raw/...`

---

### Step 6: Work through the notebook

Run each cell with **Shift + Enter**. The notebooks:
- Detect Colab automatically
- Set correct file paths to your week folder
- Save outputs to `processed/`

---

### Step 7: Save your notebook

**Important!** Notebooks are NOT auto-saved.

- **Save to Drive:** `File → Save a copy in Drive`
- **Download:** `File → Download → Download .ipynb`

!!! warning "Sessions timeout after ~90 minutes"
    When you reconnect, re-run: setup cell → mount cell → data loading cells.

---

### Troubleshooting Colab

**"FileNotFoundError"**
- Drive not mounted, OR
- Wrong path — use folder icon in sidebar to find correct path

**"ModuleNotFoundError: No module named 'geopandas'"**
- Re-run the setup cell

---

## Option B: Local Setup (Anaconda)

Install Python on your computer for offline work and larger datasets.

### Step 0: Folder structure

Same structure as your QGIS weeks:

```
Desktop/
└── intro-gis/
    ├── week07/
    │   ├── data/
    │   │   ├── raw/
    │   │   └── processed/
    │   ├── week07.ipynb    ← Notebook lives here
    │   └── exports/
    ├── week08/
    └── ...
```

### Step 1: Download Anaconda

1. Go to [anaconda.com/download](https://www.anaconda.com/download)
2. Download for your OS (~600 MB)

### Step 2: Install Anaconda

=== "Windows"
    1. Double-click the `.exe` file
    2. Click **Next** through screens
    3. Check both boxes:
       - "Add Anaconda to my PATH"
       - "Register as default Python"
    4. Click **Install** (10-15 minutes)

=== "Mac"
    1. Double-click the `.pkg` file
    2. Click **Continue** → **Install**
    3. Enter your password
    4. Wait 10-15 minutes

=== "Linux"
    ```bash
    bash ~/Downloads/Anaconda3-*.sh
    # Press Enter, type yes, press Enter, type yes
    ```

### Step 3: Create your GIS environment

Open terminal:
- **Windows:** Search for "Anaconda Prompt"
- **Mac/Linux:** Open Terminal

Run these commands:

```bash
# Create environment
conda create -n intro-gis python=3.11 -y

# Activate it
conda activate intro-gis

# Install packages (5-15 minutes)
conda install -c conda-forge geopandas rasterio rioxarray osmnx networkx rasterstats contextily folium jupyter jupyterlab matplotlib seaborn -y
```

### Step 4: Test it

```bash
python -c "import geopandas; import rasterio; print('Success!')"
```

### Step 5: Launch Jupyter

```bash
conda activate intro-gis
cd ~/Desktop/intro-gis/week07
jupyter lab
```

Your browser opens. Open `week07.ipynb` and start working!

### Local workflow summary

```bash
# Every time:
conda activate intro-gis
cd ~/Desktop/intro-gis/week08    # Go to this week's folder
jupyter lab                       # Start Jupyter
# Ctrl+C to close when done
```

---

## Colab vs Local

| Scenario | Use Colab | Use Local |
|----------|-----------|-----------|
| First time with Python | ✓ | |
| Quick exploration | ✓ | |
| Chromebook | ✓ | |
| Slow internet | | ✓ |
| Large datasets (>100MB) | | ✓ |
| Capstone project | | ✓ |
| Offline work | | ✓ |

!!! note "You can switch anytime"
    Start with Colab. Install Anaconda later if needed.

---

**You're ready for Week 7!**
