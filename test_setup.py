from sentence_transformers import SentenceTransformer
import time

model = SentenceTransformer('all-MiniLM-L6-v2')

test_sentences = ["This is a test sentence about banking and finance."] * 100

start = time.time()
embeddings = model.encode(test_sentences, batch_size=64)
elapsed = time.time() - start

print(f"100 sentences in {elapsed:.2f}s")
print(f"Estimated time for 676k docs: {(elapsed/100)*676193/3600:.1f} hours")
print(f"Embedding shape: {embeddings.shape}")