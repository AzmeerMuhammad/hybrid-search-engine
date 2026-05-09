import argparse
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.index.bm25 import search
from src.pipeline import TextPipeline
from src.embeddings.semantic_search import semantic_search
process=TextPipeline()

parser = argparse.ArgumentParser()
parser.add_argument("--query", type=str, required=True)
parser.add_argument("--mode", type=str, default="bm25")
args = parser.parse_args()
if args.mode=="bm25":
    query=process.process(args.query)
    results=search(query,10)
elif args.mode=="semantic":
    results,elapsed=semantic_search(args.query,10)
    print(f"Time: {elapsed:.4f}s")
else:
    raise ValueError("Invalid mode")
for doc_id,score in results:
    print(f"Doc ID: {doc_id}, Score: {score}")



