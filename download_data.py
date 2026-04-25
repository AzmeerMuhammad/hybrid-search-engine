from datasets import load_dataset
import csv
import os

os.makedirs("data/raw", exist_ok=True)

print("Loading dataset...")
dataset = load_dataset("microsoft/ms_marco", "v1.1", split="train[:100000]")

# --- collection.tsv ---
print("Saving passages...")
with open("data/raw/collection.tsv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    for i, item in enumerate(dataset):
        for j, passage in enumerate(item["passages"]["passage_text"]):
            writer.writerow([f"{i}_{j}", passage])

# --- queries.tsv ---
print("Saving queries...")
with open("data/raw/queries.tsv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    for i, item in enumerate(dataset):
        writer.writerow([i, item["query"]])

# --- qrels.tsv ---
print("Saving relevance labels...")
with open("data/raw/qrels.tsv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    for i, item in enumerate(dataset):
        passages = item["passages"]
        for j, is_selected in enumerate(passages["is_selected"]):
            writer.writerow([i, 0, f"{i}_{j}", is_selected])

print("Done. All three files saved.")