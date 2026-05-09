import json

top_docs = ["7344_8", "3387_2", "7344_6", "7344_0", "7371_0"]

with open("data/raw/collection.tsv", encoding="utf-8") as f:
    for line in f:
        doc_id, text = line.strip().split("\t", 1)
        if doc_id in top_docs:
            print(f"[{doc_id}] {text[:200]}")
            print()