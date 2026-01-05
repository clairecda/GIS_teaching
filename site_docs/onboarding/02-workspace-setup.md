# 2. Set Up Your Workspace

Create a folder structure to keep your course files organised. This takes 5 minutes.

---

## Create your course folder

1. Open Finder (Mac) or File Explorer (Windows)
2. Go to your Desktop (or Documents)
3. Create a new folder called `intro-gis`
4. Inside `intro-gis`, create these subfolders:

```
intro-gis/
├── data/
│   ├── raw/          ← Downloaded files go here
│   └── processed/    ← Cleaned/filtered data goes here
├── projects/         ← QGIS project files (.qgz)
├── exports/          ← Your map outputs (PNG, PDF)
└── notebooks/        ← Python notebooks (Week 7+)
```

---

## Connect the folder in QGIS

Adding your folder to Favorites lets you quickly access it without navigating through your whole computer each time.

1. Open QGIS
2. Find the **Browser** panel on the left side of the screen
3. Look for **Favorites** (usually near the top, with a star icon ⭐)
4. Right-click **Favorites** → **Add a Directory...**
5. Navigate to and select your `intro-gis/data` folder
6. Click **Select Folder** (Windows) or **Open** (Mac)

Your folder now appears under Favorites. Double-click to expand it and see your data files.

---

## Save your first project

1. In QGIS, go to **Project > Save As...**
2. Navigate to your `intro-gis/projects/` folder
3. Name it `week01.qgz`
4. Before saving, go to **Project > Properties > General**
5. Under "Save paths", select **Relative**
6. Click **OK**, then save your project

!!! info "What are relative paths?"
    When QGIS saves your project, it remembers where your data files are. There are two ways to store this:

    - **Absolute path:** `C:\Users\Claire\Desktop\intro-gis\data\countries.shp`
    - **Relative path:** `..\data\countries.shp` (means "go up one folder, then into data")

    **Why relative is better:** If you move your `intro-gis` folder to another location (or another computer), relative paths still work because they describe where files are *relative to the project*. Absolute paths break because the exact location changed.

    **Rule of thumb:** Always use relative paths if your data is inside your project folder.

---

## Tips

- **Keep raw data untouched** — work from copies in `processed/`
- **Use clear names** — `week03_seifa_join.gpkg` not `data_final_v2.gpkg`
- **One project per week** — easier to find things later

---

**Next step:** [3. Download datasets](03-download-data.md)
