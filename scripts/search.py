import argparse
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.index.bm25 import search
from src.pipeline import TextPipeline
process=TextPipeline()

parser = argparse.ArgumentParser()
parser.add_argument("--query", type=str, required=True)
parser.add_argument("--mode", type=str, default="bm25")
args = parser.parse_args()

query=process.process(args.query)
results=search(query,10)
for doc_id,score in results:
    print(f"Doc ID: {doc_id}, Score: {score}")



