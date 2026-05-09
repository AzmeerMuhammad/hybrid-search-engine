from sentence_transformers import SentenceTransformer
from tqdm import tqdm
import json
import numpy as np
import os

model =SentenceTransformer("all-MiniLM-L6-v2")

with open("data/raw/collection.tsv", "r", encoding="utf-8") as f:
    counter=0
    batch_texts=[]
    batch_ids=[]
    if os.path.exists("data/embeddings/checkpoint.npz"):
        data = np.load("data/embeddings/checkpoint.npz")
        embeddings_so_far = list(data["embeddings"])
        doc_ids_so_far = list(data["doc_ids"])
    else: 
        embeddings_so_far = []
        doc_ids_so_far = []
        os.makedirs("data/embeddings", exist_ok=True)
    for line in tqdm(f, desc="Embedding documents"):
        if counter==100000:
            break
        doc_id, text = line.strip().split("\t")
        batch_texts.append(text)
        batch_ids.append(doc_id)
        if len(batch_texts) == 64:
            embeddings = model.encode(batch_texts, batch_size=64, show_progress_bar=True)
            doc_ids_so_far.extend(batch_ids)
            embeddings_so_far.extend(embeddings)
            if len(embeddings_so_far) % 5000 < 64:
                np.savez("data/embeddings/checkpoint.npz",
                        embeddings=embeddings_so_far,
                        doc_ids=doc_ids_so_far)
            
            batch_texts=[]
            batch_ids=[]
        counter+=1
    if batch_texts:
        embeddings=model.encode(batch_texts,batch_size=64,show_progress_bar=True)
        embeddings_so_far.extend(embeddings)
        doc_ids_so_far.extend(batch_ids)
    np.save("data/embeddings/embeddings.npy", np.array(embeddings_so_far))
    np.save("data/embeddings/doc_ids.npy", np.array(doc_ids_so_far))
    print(f"Done. Saved {len(doc_ids_so_far)} embeddings.")
                

    
    
