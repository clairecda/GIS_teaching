# Setting Up Python with Anaconda

This guide walks you through installing Anaconda and the Python packages you need for Weeks 7-10.

**Time required:** 30-45 minutes (including download time)

---

## Step 1: Download Anaconda

1. Go to [anaconda.com/download](https://www.anaconda.com/download)
2. Download the installer for your operating system:
   - **Windows:** Click the Windows download button
   - **Mac:** Click the Mac download button (works for both Intel and M1/M2/M3)
   - **Linux:** Click the Linux download button
3. The file is about 600 MB—wait for the download to complete

---

## Step 2: Install Anaconda

### Windows

1. Double-click the downloaded `.exe` file
2. Click **Next** through the welcome screens
3. Accept the license agreement
4. Choose "Just Me" for installation type
5. **Important:** Check both boxes:
   - ✅ "Add Anaconda to my PATH environment variable"
   - ✅ "Register Anaconda as my default Python"
6. Click **Install** (takes 10-15 minutes)
7. Click **Finish**

### Mac

1. Double-click the downloaded `.pkg` file
2. Click **Continue** through the screens
3. Accept the license agreement
4. Click **Install** and enter your password
5. Wait 10-15 minutes
6. Click **Close**

### Linux

1. Open Terminal
2. Run: `bash ~/Downloads/Anaconda3-*.sh`
3. Press Enter to read the license, then type `yes` to accept
4. Press Enter to use the default location
5. Type `yes` when asked to initialize conda
6. Close and reopen Terminal

---

## Step 3: Create Your GIS Environment

Now you'll install the spatial analysis packages (GeoPandas, Rasterio, OSMnx).

### Open your terminal

- **Windows:** Search for "Anaconda Prompt" in the Start menu
- **Mac/Linux:** Open Terminal

### Run these commands

Copy and paste each line, pressing Enter after each:

```bash
conda create -n intro-gis python=3.11 -y
```

Wait for it to complete, then:

```bash
conda activate intro-gis
```

Your prompt should now show `(intro-gis)` at the beginning.

Now install the packages:

```bash
conda install -c conda-forge geopandas rasterio rioxarray osmnx networkx rasterstats contextily folium jupyter jupyterlab matplotlib seaborn -y
```

This downloads about 500 MB and takes 5-15 minutes. Go grab a coffee!

---

## Step 4: Test Your Setup

With your environment still activated, run:

```bash
python -c "import geopandas; import rasterio; import osmnx; print('✅ All packages installed!')"
```

You should see: `✅ All packages installed!`

If you see an error, try reinstalling (see Troubleshooting below).

---

## Step 5: Launch Jupyter

1. Make sure your environment is activated:
   ```bash
   conda activate intro-gis
   ```

2. Launch Jupyter Lab:
   ```bash
   jupyter lab
   ```

3. Your browser will open with the Jupyter interface

4. Create a new notebook and run:
   ```python
   import geopandas as gpd
   print("Hello GIS!")
   ```

5. To close Jupyter: press `Ctrl+C` twice in the terminal

---

## Daily Workflow

Every time you work on Python labs:

1. Open Anaconda Prompt (Windows) or Terminal (Mac/Linux)
2. Activate your environment: `conda activate intro-gis`
3. Navigate to your folder: `cd ~/Desktop/intro-gis`
4. Launch Jupyter: `jupyter lab`
5. Work on your notebook
6. Save and close: `Ctrl+C` in terminal

---

## Troubleshooting

### "conda: command not found"

**Windows:** Use "Anaconda Prompt" from the Start menu instead of Command Prompt.

**Mac/Linux:** Run this command:
```bash
echo 'export PATH="$HOME/anaconda3/bin:$PATH"' >> ~/.zshrc && source ~/.zshrc
```

### Package installation failed

Try installing packages one at a time:
```bash
conda activate intro-gis
conda install -c conda-forge geopandas -y
conda install -c conda-forge rasterio -y
conda install -c conda-forge osmnx -y
conda install -c conda-forge jupyter -y
```

### "ModuleNotFoundError" in Jupyter

Make sure your environment is activated before launching Jupyter:
```bash
conda activate intro-gis
jupyter lab
```

In Jupyter, go to **Kernel → Change Kernel → Python (intro-gis)** if available.

### Start over completely

If nothing works, remove everything and try again:
```bash
conda deactivate
conda env remove -n intro-gis
```
Then go back to Step 3.

---

## Quick Reference

| Command | What it does |
|---------|-------------|
| `conda activate intro-gis` | Activate the environment (do this first!) |
| `conda deactivate` | Deactivate the environment |
| `jupyter lab` | Launch Jupyter |
| `conda env list` | Show all environments |

---

**You're ready for Week 7!** If you can run `import geopandas` in a Jupyter notebook, everything is working.

*Last updated: December 2025*
