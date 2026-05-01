import sqlite3
import math
import os
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(os.getcwd(), "data", "index.db")
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

def calculate_score_fast(query_tokens, term_freqs, doc_length, df_map):
    k1 = 1.5
    b = 0.75
    avg_dl = 39.5
    N = 676193
    score = 0
    for term in query_tokens:
        if term not in term_freqs or term not in df_map:
            continue
        doc_freq = df_map[term]
        term_freq = term_freqs[term]
        idf = math.log(N / doc_freq)
        tf_norm = (term_freq * (k1 + 1)) / (term_freq + k1 * (1 - b + b * (doc_length / avg_dl)))
        score += idf * tf_norm
    return score

def search(query_tokens: list[str], top_k: int = 10) -> list[tuple]:
    if not query_tokens:
        return []
    placeholders = ",".join("?" * len(query_tokens))
    cursor.execute(f"SELECT term, doc_freq FROM term_stats WHERE term IN ({placeholders})", query_tokens)
    df_map = {row[0]: row[1] for row in cursor.fetchall()}
    cursor.execute(f"""
        SELECT p.term, p.doc_id, p.term_freq, d.doc_length
        FROM postings p
        JOIN documents d ON p.doc_id = d.doc_id
        WHERE p.term IN ({placeholders})
        LIMIT 10000
    """, query_tokens)
    rows = cursor.fetchall()
    doc_data = defaultdict(lambda: {"length": 0, "terms": {}})
    for term, doc_id, tf, length in rows:
        doc_data[doc_id]["length"] = length
        doc_data[doc_id]["terms"][term] = tf
    score_list = []
    for doc_id, data in doc_data.items():
        current_score = calculate_score_fast(query_tokens, data["terms"], data["length"], df_map)
        score_list.append((doc_id, current_score))
    return sorted(score_list, key=lambda x: x[1], reverse=True)[:top_k]