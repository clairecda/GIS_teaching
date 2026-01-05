# 1. Install QGIS

Install QGIS before Week 1. This takes about 15 minutes.

---

## Download QGIS

1. Go to [qgis.org/download](https://qgis.org/en/site/forusers/download.html)
2. Download the **Long Term Release (LTR)** for your system:
   - **Windows:** Click the green "Download QGIS" button, choose LTR
   - **Mac:** Click the Mac download, works for Intel and Apple Silicon
   - **Linux:** Follow your distribution's instructions

## Install

### Windows
1. Run the downloaded `.msi` file
2. Click through the installer, accept defaults
3. Wait for installation to complete

### Mac
1. Open the downloaded `.dmg` file
2. Drag QGIS to your Applications folder
3. **First launch is different:**
   - Go to Applications and find QGIS
   - **Right-click** (or Control-click) on QGIS
   - Click **Open** from the menu
   - A warning appears: "QGIS is from an unidentified developer"
   - Click **Open** again to confirm

!!! info "Why this extra step?"
    Mac's "Gatekeeper" security blocks apps from non-Apple sources. QGIS is safe—it's open-source software used by professionals worldwide. This right-click method tells Mac you trust it. You only need to do this once; future launches work normally.

### Linux
Follow the instructions for your distribution on the QGIS download page.

---

## Verify it works

1. Launch QGIS
2. You should see "QGIS 3.34" (or similar LTR version) in the title bar
3. Go to **View > Panels** and enable these essential panels:

| Panel | What it's for |
|-------|---------------|
| **Browser** | Navigate your computer's files and folders to find data |
| **Layers** | See and manage all the data layers on your map |
| **Processing Toolbox** | Access analysis tools (buffers, joins, etc.) |

!!! tip "Can't find a panel?"
    If a panel disappears, go to **View > Panels** and tick the checkbox next to its name. You can drag panels to rearrange them or dock them to different sides of the screen.

If QGIS opens without errors, you're ready for the next step.

---

## Troubleshooting

**Mac: "QGIS can't be opened"**
- Right-click the app > Open > Open anyway

**Windows: Installer blocked**
- Right-click installer > Properties > Unblock > Apply

**Slow or crashes**
- Go to Settings > Options > Rendering
- Enable "Simplify geometries"
- Reduce max threads if needed

---

**Next step:** [2. Set up your workspace](02-workspace-setup.md)
