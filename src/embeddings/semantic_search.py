import numpy
import time
from sentence_transformers import SentenceTransformer
embeddings=numpy.load("data/embeddings/embeddings.npy")
doc_ids=numpy.load("data/embeddings/doc_ids.npy")
query_model =SentenceTransformer("all-MiniLM-L6-v2")

norms = numpy.linalg.norm(embeddings, axis=1, keepdims=True)
embeddings = embeddings / norms

def semantic_search(query: str, top_k: int = 10) -> list[tuple]:
    start=time.time()
    embeds=query_model.encode([query])[0]
    scores=numpy.dot(embeddings, embeds)
    top_ids=numpy.argsort(-scores)[:top_k]
    results=[]
    for idx in top_ids:
        doc_id=doc_ids[idx]
        score=float(scores[idx])
        results.append((doc_id,score))
        
    return results, time.time()-start
