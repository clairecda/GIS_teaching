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
3. First launch: Right-click > Open (to bypass Gatekeeper)

### Linux
Follow the instructions for your distribution on the QGIS download page.

---

## Verify it works

1. Launch QGIS
2. You should see "QGIS 3.34" (or similar LTR version) in the title bar
3. Go to **View > Panels** and enable:
   - Browser
   - Layers
   - Processing Toolbox

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
