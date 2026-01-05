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

Google Colab is a free service that lets you run Python code in your web browser. You don't install anything on your computer—the code runs on Google's computers (servers) in a data center somewhere.

**Think of it like Google Docs for code:** Just as Google Docs lets you write documents without installing Word, Colab lets you run Python without installing Python.

### The key concept: Where does the code run?

This is the most important thing to understand:

```
┌─────────────────────────────────────────────────────────────────┐
│                        YOUR COMPUTER                             │
│  ┌─────────────┐                                                │
│  │   Browser   │  ← You type code here                          │
│  │   (Chrome)  │                                                │
│  └─────────────┘                                                │
│        │                                                        │
│        │  Your code is sent over the internet                   │
│        ▼                                                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ Internet
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     GOOGLE'S SERVERS                             │
│  ┌─────────────┐                                                │
│  │   Colab     │  ← Your code actually runs here                │
│  │   Runtime   │                                                │
│  └─────────────┘                                                │
│        │                                                        │
│        │  But this computer can't see your laptop's files!      │
│        │  It CAN see your Google Drive (if you connect it)      │
│        ▼                                                        │
│  ┌─────────────┐                                                │
│  │   Google    │  ← Your data files go here                     │
│  │   Drive     │                                                │
│  └─────────────┘                                                │
└─────────────────────────────────────────────────────────────────┘
```

**The problem:** When your code says `read_file("my_data.geojson")`, it looks for that file on the Google server—not on your laptop. Your laptop's files are invisible to Colab.

**The solution:** Store your data files in Google Drive, then "mount" (connect) your Drive to Colab. Now your code can access your files.

---

### Step 1: Set up your Google Drive folder

Before opening any notebooks, organize your Google Drive to mirror your local folder:

1. Go to [drive.google.com](https://drive.google.com)
2. Click **+ New** → **New folder**
3. Name it exactly: `intro-gis`
4. Open the `intro-gis` folder
5. Create a subfolder called `data`
6. Inside `data`, create two folders: `raw` and `processed`

Your Drive should look like this:

```
My Drive/
└── intro-gis/
    └── data/
        ├── raw/          ← Upload downloaded files here
        └── processed/    ← Save modified data here
```

**Upload your data files** to `data/raw/`. For example, Week 8 needs `neighbourhoods.geojson` and `incidents.geojson` in `data/raw/`.

---

### Step 2: Open a course notebook

1. Go to the weekly guide (e.g., [Week 7](../weeks/week07.md))
2. Click the **"Open in Colab"** button
3. Sign in with your Google account if prompted

The notebook opens in a new tab. You'll see cells with code and explanations.

---

### Step 3: Run the setup cell

Every notebook starts with a setup cell that:

1. Detects that you're in Colab
2. Installs the GIS packages (takes ~1 minute)

Click on the first code cell and press **Shift + Enter** to run it. Wait for it to finish.

---

### Step 4: Mount your Google Drive

This is the crucial step that connects your Drive to Colab.

**What does "mount" mean?**

Think of Google Drive like a USB stick. When you plug a USB into your computer, it "mounts"—your computer can suddenly see and access the files on it.

"Mounting" Google Drive in Colab does the same thing: it connects your Drive to the Colab server so your code can read your files.

**Run the mount cell:**

The notebooks include a cell like this:

```python
from google.colab import drive
drive.mount('/content/drive')
```

When you run it:

1. A popup appears asking for permission
2. Click **Connect to Google Drive**
3. Choose your Google account
4. Click **Allow**
5. You'll see: `Mounted at /content/drive`

**Now your Drive is connected!** Your files are accessible at `/content/drive/MyDrive/intro-gis/data/...`

---

### Step 5: Work through the notebook

Run each cell in order using **Shift + Enter**. The notebooks are designed to:

- Automatically detect Colab and set the correct file paths
- Load your data from Google Drive
- Guide you through the analysis step by step

---

### Step 6: Save your work

Your changes to the notebook are NOT automatically saved. Save regularly:

- **To Google Drive:** `File → Save a copy in Drive` (recommended)
- **To your computer:** `File → Download → Download .ipynb`

!!! warning "Sessions timeout after ~90 minutes"
    If you're inactive for too long, Colab disconnects. When you reconnect, you need to:

    1. Re-run the setup cell (reinstall packages)
    2. Re-run the mount cell (reconnect Drive)
    3. Re-run any cells that load data

    Your Drive files are safe—they persist forever. Only the Colab "runtime" resets.

---

### Complete Colab workflow summary

Every time you work on a Python notebook:

```
1. Open notebook from course website → "Open in Colab"
2. Run setup cell → Installs packages (~1 min)
3. Run mount cell → Connects Google Drive
4. Run remaining cells → Do the analysis
5. Save your work → File > Save a copy in Drive
```

---

### Troubleshooting Colab

**"ModuleNotFoundError: No module named 'geopandas'"**

- You didn't run the setup cell, or it failed
- Scroll to the top and run the first code cell again

**"FileNotFoundError: [Errno 2] No such file or directory"**

- Your Google Drive isn't mounted, OR
- The file path is wrong, OR
- The file doesn't exist in Drive

**To debug file paths:**

1. Click the **folder icon** (📁) in Colab's left sidebar
2. Click **drive** → **MyDrive** → navigate to your file
3. Right-click the file → **Copy path**
4. Use that exact path in your code

**"Drive already mounted" message**

- This is fine! It just means Drive was already connected
- You don't need to mount it again

**Session disconnected**

- Normal after ~90 minutes of inactivity
- Click "Reconnect" and re-run cells from the top

---

## Option B: Local Setup (Anaconda)

Install Python and packages on your computer for faster performance and offline access.

### When to choose local setup

- You have slow or unreliable internet
- You're working with large datasets (>100MB)
- You want to work offline
- You're doing the capstone project

### Step 0: Create your workspace

Make sure you have the folder structure from the [Workspace Setup](02-workspace-setup.md):

```
Desktop/
└── intro-gis/
    ├── data/
    │   ├── raw/          ← Downloaded files
    │   └── processed/    ← Modified data
    ├── exports/
    └── notebooks/        ← Save notebooks here
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

An environment is like a separate workspace for Python. It keeps this course's packages isolated from other Python projects. If something breaks, you can delete the environment and start fresh.

**Open your terminal:**

- **Windows:** Click Start, search for "**Anaconda Prompt**" (not regular Command Prompt!)
- **Mac:** Open **Terminal** (Applications > Utilities > Terminal)
- **Linux:** Open your terminal application

**Run these commands one at a time:**

```bash
# Create a new environment
conda create -n intro-gis python=3.11 -y

# Activate the environment
conda activate intro-gis

# Install GIS packages (takes 5-15 minutes)
conda install -c conda-forge geopandas rasterio rioxarray osmnx networkx rasterstats contextily folium jupyter jupyterlab matplotlib seaborn -y
```

!!! tip "How to know you're in the right environment"
    Your terminal prompt shows `(intro-gis)` at the beginning:
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
cd ~/Desktop/intro-gis
jupyter lab
```

Your browser opens with Jupyter. Open a notebook from the `notebooks/` folder and start working!

### Local workflow summary

Every time you work on a Python notebook:

```bash
# 1. Open terminal (Anaconda Prompt on Windows)
# 2. Activate environment
conda activate intro-gis

# 3. Navigate to your project folder
cd ~/Desktop/intro-gis

# 4. Launch Jupyter
jupyter lab

# 5. Work on notebooks in your browser
# 6. Ctrl+C in terminal to close Jupyter when done
```

---

## Colab vs Local: Quick comparison

| Scenario | Use Colab | Use Local |
|----------|-----------|-----------|
| First time trying Python | ✓ | |
| Quick exploration | ✓ | |
| Working on Chromebook | ✓ | |
| Slow/unreliable internet | | ✓ |
| Large local datasets (>100MB) | | ✓ |
| Capstone project | | ✓ |
| Need to work offline | | ✓ |

!!! note "You can switch anytime"
    Start with Colab. If you need local setup later, install Anaconda then. The notebooks work in both environments.

---

## Troubleshooting Anaconda

**"conda: command not found"**

- Windows: Use "Anaconda Prompt" not Command Prompt
- Mac/Linux: Run: `echo 'export PATH="$HOME/anaconda3/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc`

**Package installation failed**

- Try installing one at a time: `conda install -c conda-forge geopandas -y`

**"ModuleNotFoundError" in Jupyter**

- You forgot to activate the environment
- Close Jupyter, run `conda activate intro-gis`, then `jupyter lab` again

**Start over completely**

```bash
conda deactivate
conda env remove -n intro-gis
```
Then redo Step 3.

---

**You're ready for Week 7!** Choose Colab to start quickly, or set up Anaconda if you prefer local development.
