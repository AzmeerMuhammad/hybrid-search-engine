import sqlite3
import json

conn = sqlite3.connect("data/index.db")
cursor = conn.cursor()

top_docs = ["17065_4", "6132_0", "68381_6"]

with open("data/raw/collection.tsv", encoding="utf-8") as f:
    for line in f:
        doc_id, text = line.strip().split("\t", 1)
        if doc_id in top_docs:
            print(f"[{doc_id}] {text[:200]}")
            print()