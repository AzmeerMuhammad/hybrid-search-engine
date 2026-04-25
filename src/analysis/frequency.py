import json
import matplotlib.pyplot as plt
from collections import Counter
from tqdm import tqdm

top_terms = Counter()

# --- 1. Data Loading and Parsing ---
with open("data/processed/collection_processed.jsonl", "r", encoding="utf-8") as inf:
    for line in tqdm(inf, desc="Processing terms", unit="doc"):
        # Parse JSON line
        data = json.loads(line.strip())
        
        # Extract the list of tokens from the dict values
        for tokens in data.values():
            top_terms.update(tokens)

# --- 2. Data Preparation ---
# Get the top 20 most frequent terms
top_20 = top_terms.most_common(20)

# Unpack the list of tuples
terms = [t for t, c in top_20]
counts = [c for t, c in top_20]

# Reverse the lists so the highest frequency is at the top of the horizontal bar chart
terms = terms[::-1]
counts = counts[::-1]
# --- 3. Visualization ---
fig, ax = plt.subplots(figsize=(10, 8))
# Draw horizontal bars
ax.barh(terms, counts, color='skyblue', edgecolor='navy')
# Add labels and title
ax.set_xlabel('Frequency')
ax.set_ylabel('Terms')
ax.set_title('Top 20 Most Frequent Terms in Processed Collection')
# Add grid for readability
ax.xaxis.grid(True, linestyle='--', alpha=0.7)
# Adjust layout to prevent clipping of labels
plt.tight_layout()
# Save the figure
plt.savefig("data/processed/top_terms.png")
# Show it
plt.show()

print(f"Unique terms: {len(top_terms)}")