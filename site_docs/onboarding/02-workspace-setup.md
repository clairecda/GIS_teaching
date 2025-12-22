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

1. Open QGIS
2. In the **Browser** panel (left side), find **Favorites**
3. Right-click **Favorites** > **Add a Directory...**
4. Select your `intro-gis/data` folder
5. Now you can quickly access your data from QGIS

---

## Save your first project

1. In QGIS, go to **Project > Save As...**
2. Navigate to your `intro-gis/projects/` folder
3. Name it `week01.qgz`
4. Check **Save paths: relative** in project properties

This keeps your project portable between computers.

---

## Tips

- **Keep raw data untouched** — work from copies in `processed/`
- **Use clear names** — `week03_seifa_join.gpkg` not `data_final_v2.gpkg`
- **One project per week** — easier to find things later

---

**Next step:** [3. Download datasets](03-download-data.md)
