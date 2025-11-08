#!/usr/bin/env python3
"""
Environment validation script for the Intro to GIS course.

This script checks that all required packages are installed correctly.
Run with: `python verify_setup.py`
"""

import importlib
import sys
from typing import Iterable


CORE_MODULES: Iterable[str] = (
    "geopandas",
    "shapely",
    "pyproj",
    "rasterio",
    "rioxarray",
    "osmnx",
    "contextily",
)


def main() -> None:
    print("🔍 Checking your GIS environment setup...\n")
    print(f"Python version: {sys.version.split()[0]}")
    print()

    failures = []
    for module_name in CORE_MODULES:
        try:
            module = importlib.import_module(module_name)
            version = getattr(module, "__version__", "unknown")
            print(f"✅ {module_name:15s} {version}")
        except ImportError:
            print(f"❌ {module_name:15s} NOT INSTALLED")
            failures.append(module_name)
        except Exception as exc:
            print(f"⚠️  {module_name:15s} ERROR: {exc}")
            failures.append(module_name)

    print()

    if failures:
        print("⚠️  Some packages are missing or failed to import.")
        print(f"Missing packages: {', '.join(failures)}\n")
        print("To fix this:")
        print("1. Make sure your conda environment is activated:")
        print("   conda activate intro-gis")
        print("2. Try reinstalling the missing packages:")
        print(f"   conda install -c conda-forge {' '.join(failures)}")
        print("3. If problems persist, try recreating the environment:")
        print("   conda env remove -n intro-gis")
        print("   conda env create -f environment.yml")
        print()
        raise SystemExit(1)

    print("🎉 Success! All packages are installed correctly.")
    print("You're ready to start the Python weeks!")
    print()


if __name__ == "__main__":
    main()
