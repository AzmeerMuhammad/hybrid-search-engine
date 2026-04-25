# verify_data.py
import os

files = [
    "data/raw/collection.tsv",
    "data/raw/queries.tsv",
    "data/raw/qrels.tsv"
]

for filepath in files:
    if not os.path.exists(filepath):
        print(f"MISSING: {filepath}")
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    print(f"\n{filepath}")
    print(f"  Total lines: {len(lines):,}")
    print(f"  First line:  {lines[0][:100].strip()}")
    print(f"  Last line:   {lines[-1][:100].strip()}")