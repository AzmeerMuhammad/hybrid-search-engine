# Input:  raw string (any case, punctuation, URLs, unicode)
# Output: clean lowercase string, no punctuation, no URLs
# NOT tokenizing yet — that's the next module's job

import re
import unicodedata

def normalize(text: str) -> str:
    # your steps go here
    text=unicodedata.normalize("NFKD",text)
    text=text.encode("ascii","ignore").decode("ascii")
    text=text.lower()
    text=re.sub(r"https?://\S+"," ",text)
    text=re.sub(r"www\.\S+"," ",text)
    text=re.sub(r"[^a-z\s]"," ",text)
    text=re.sub(r"\s+"," ",text)
    text=text.strip()
    return text

with open("data/raw/collection.tsv", encoding="utf-8") as f:
    for i, line in enumerate(f):
        _, text = line.strip().split("\t", 1)
        print(f"BEFORE: {text[:100]}")
        print(f"AFTER:  {normalize(text)[:100]}")
        print()
        if i == 9:
            break