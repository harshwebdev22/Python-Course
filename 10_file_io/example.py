"""
Run me: python3 example.py
Creates and cleans up its own scratch files in this folder.
"""

import json
from pathlib import Path

# --- pathlib basics ---
data_path = Path(__file__).parent / "scratch.txt"
print(f"path: {data_path}")
print(f"name={data_path.name} suffix={data_path.suffix} parent={data_path.parent}")

# --- writing with `with` ---
with open(data_path, "w") as f:
    f.write("first line\n")
    f.writelines(["second line\n", "third line\n"])

# --- reading whole file ---
with open(data_path) as f:
    contents = f.read()
print("--- whole file ---")
print(contents)

# --- reading line by line (memory-efficient for big files) ---
print("--- line by line ---")
with open(data_path) as f:
    for line in f:
        print(f"> {line.strip()}")

# --- pathlib's one-shot shortcuts ---
data_path.write_text("overwritten via pathlib\n")
print("--- via pathlib read_text ---")
print(data_path.read_text())

# --- JSON ---
json_path = Path(__file__).parent / "scratch.json"
data = {"name": "Harsh", "age": 30, "known_languages": ["JS", "PHP"]}

with open(json_path, "w") as f:
    json.dump(data, f, indent=2)

with open(json_path) as f:
    loaded = json.load(f)
print("--- loaded json ---")
print(loaded)

json_string = json.dumps(data)
print(f"--- as a string --- \n{json_string}")

# --- cleanup ---
data_path.unlink()
json_path.unlink()
print("scratch files cleaned up")
