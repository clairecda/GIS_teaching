# 2. Set Up Your Workspace

Create a folder structure to keep your course files organised. This takes 5 minutes.

---

## Create your course folder

1. Open Finder (Mac) or File Explorer (Windows)
2. Go to your Desktop (or Documents)
3. Create a new folder called `intro-gis`

Now create the **subfolders** inside it. You need to create each folder one by one:

4. Open your `intro-gis` folder
5. Create a folder called `week01`
6. Open `week01` and create these folders inside it:
   - Create a folder called `data`
   - Create a folder called `exports`
7. Open the `data` folder you just created
8. Inside `data`, create two more folders:
   - Create a folder called `raw`
   - Create a folder called `processed`

When you're done, your folder structure should look like this:

```
intro-gis/
└── week01/
    ├── data/
    │   ├── raw/        ← Downloaded files go here
    │   └── processed/  ← Your modified data goes here
    ├── week01.qgz      ← Your QGIS project file (you'll create this later)
    └── exports/        ← Your map outputs (PNG, PDF)
```

!!! tip "How to create a folder"
    **Mac:** Right-click → New Folder (or Cmd + Shift + N)

    **Windows:** Right-click → New → Folder (or Ctrl + Shift + N)

Each week, create a new folder with the same structure:

```
intro-gis/
├── week01/
│   ├── data/raw/
│   ├── data/processed/
│   ├── week01.qgz
│   └── exports/
├── week02/
│   └── (same structure)
├── ...
└── week12/
```

!!! tip "Create folders as you go"
    Don't create all 12 weeks now. Create `week01/` today, then `week02/` next week.

---

## Connect the folder in QGIS

Add your course folder to Favorites for quick access:

1. Open QGIS
2. Find the **Browser** panel on the left
3. Right-click **Favorites** → **Add a Directory...**
4. Select your `intro-gis` folder
5. Click **Select Folder** (Windows) or **Open** (Mac)

Your folder now appears under Favorites. Expand it to see your week folders.

---

## Save your first project

1. In QGIS, go to **Project > Save As...**
2. Navigate to your `intro-gis/week01/` folder
3. Name it `week01.qgz`
4. Before saving, go to **Project > Properties > General**
5. Under "Save paths", select **Relative**
6. Click **OK**, then save

!!! info "What are relative paths?"
    - **Absolute path:** `C:\Users\Claire\Desktop\intro-gis\week01\data\raw\countries.shp`
    - **Relative path:** `data\raw\countries.shp`

    Relative paths still work if you move your folder. Always use them.

---

## The raw/processed rule

This is the most important habit you'll learn:

| Folder | What goes here | Can I edit files? |
|--------|----------------|-------------------|
| `raw/` | Downloaded files exactly as you got them | **No** — never edit |
| `processed/` | Data you've cleaned, filtered, or modified | Yes |

**Why?** If you make a mistake, you can always start fresh from `raw/`. Professional GIS work requires tracing data back to its source.

---

## Your capstone project

Your capstone gets its own folder at the end:

```
intro-gis/
├── week01/
├── week02/
├── ...
├── week12/
└── capstone/
    ├── data/
    │   ├── raw/
    │   └── processed/
    ├── capstone.qgz
    ├── notebooks/      ← Python analysis
    └── exports/
```

The capstone folder works exactly like a week folder, but it's your own project that you build throughout the course.

---

## Tips

- **Never edit files in `raw/`** — always save to `processed/`
- **Use clear names** — `suburbs_joined.gpkg` not `data_final_v2.gpkg`
- **Each week is self-contained** — easy to find your work later

---

**Next step:** [3. Download datasets](03-download-data.md)
