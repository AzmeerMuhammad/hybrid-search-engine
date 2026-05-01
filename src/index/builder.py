import json
import sqlite3
from collections import Counter
from tqdm import tqdm
def create_index(db_path="data/index.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.executescript("""
        CREATE TABLE IF NOT EXISTS documents (
            doc_id TEXT PRIMARY KEY,
            doc_length INTEGER
        );

        CREATE TABLE IF NOT EXISTS postings (
            term TEXT,
            doc_id TEXT,
            term_freq INTEGER,
            FOREIGN KEY (doc_id) REFERENCES documents(doc_id)
        );

        CREATE TABLE IF NOT EXISTS term_stats (
            term TEXT PRIMARY KEY,
            doc_freq INTEGER
        );
                         
        CREATE INDEX IF NOT EXISTS idx_postings_term 
            ON postings(term);
    """)

    conn.commit()
    return conn, cursor

conn, cursor = create_index()
cursor.execute("PRAGMA journal_mode=WAL")
cursor.execute("PRAGMA synchronous=OFF")
top_terms=Counter()
with open("data/processed/collection_processed.jsonl","r", encoding="utf-8") as f:
    for line in tqdm(f, desc="Indexing documents"):
        data=json.loads(line.strip())
        for doc_id,tokens in data.items():
            term_freqs=Counter(tokens)
            top_terms.update(set(term_freqs))
            cursor.execute("INSERT INTO documents VALUES (?, ?)", (doc_id,len(tokens)))
            for term, freq in term_freqs.items():
                cursor.execute("INSERT INTO postings VALUES (?, ?, ?)", (term, doc_id, freq))
    for term, df in top_terms.items():
        cursor.execute("INSERT INTO term_stats VALUES (?, ?)", (term,df))


conn.commit()
conn.close()
