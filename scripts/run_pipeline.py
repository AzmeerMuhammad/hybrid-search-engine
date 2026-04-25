from tqdm import tqdm
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.pipeline import TextPipeline
import json
process=TextPipeline()
total_docs=0
total_tokens=0
start=time.time()
with open("data/raw/collection.tsv",encoding="utf-8") as inf:
    with open("data/processed/collection_processed.jsonl","a",encoding="utf-8") as outf:
        for line in tqdm(inf, desc="Processing", unit="doc"):
            line=line.strip()
            doc_id,text=line.split("\t",1)
            processed_text=process.process(text)

            json.dump({doc_id:processed_text},outf)
            outf.write("\n")
            total_docs+=1
            total_tokens+=len(processed_text)
end=time.time()
print(f"\nProcessed {total_docs} docs: {total_tokens} tokens\n")
print(f"\nAverage token length: {total_tokens/total_docs}")
print(f"Time: {end-start}")