"""
Run me: python3 example.py
(Try it once with your venv NOT activated, and once with it activated —
compare the printed path.)

This doesn't install anything — it just proves to you, in code, whether
you're running inside a virtual environment and where packages would land.
"""

import sys
from pathlib import Path

print(f"Python executable: {sys.executable}")
print(f"sys.prefix:        {sys.prefix}")

in_venv = sys.prefix != sys.base_prefix
print(f"Running inside a venv: {in_venv}")

if in_venv:
    site_packages = Path(sys.prefix) / "lib"
    print(f"Packages installed via pip land under: {site_packages}")
else:
    print("Not in a venv — 'pip install' right now would affect your system Python.")
    print("Create one with: python3 -m venv .venv && source .venv/bin/activate")
