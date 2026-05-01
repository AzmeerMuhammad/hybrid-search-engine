import sqlite3
import math
import argparse

# connect to your database
conn = sqlite3.connect("data/index.db")
cursor = conn.cursor()

def score(query_tokens: list[str], doc_id: str) -> float:
    k1=1.5
    b=0.75
    avg_dl=39.5
    N=676193
    score=0

    # fetch one row
    cursor.execute("SELECT doc_length FROM documents WHERE doc_id = ?", (doc_id,))
    row = cursor.fetchone()
    doc_length = row[0]  # first column of the result

    for term in query_tokens:
        

        # fetch multiple rows
        cursor.execute("SELECT term_freq FROM postings WHERE term = ? AND doc_id = ?", (term, doc_id))
        row = cursor.fetchone()
        term_freq = row[0] if row else 0  # if term not in doc, frequency is 0

        # fetch doc_freq from term_stats
        cursor.execute("SELECT doc_freq FROM term_stats WHERE term = ?", (term,))
        row = cursor.fetchone()
        doc_freq = row[0] if row else None  # None means term not in index at all

        if doc_freq is None: 
            continue

        idf=math.log(N/doc_freq)

        tf_norm=(term_freq * (k1 + 1))/ (term_freq + k1 * (1 - b + b * (doc_length/avg_dl)))

        score+=idf * tf_norm
    return score


def search(query_tokens: list[str], top_k: int = 10) -> list[tuple]:
    score_list=dict()
    candidate_docs=set()
    for tokens in query_tokens:
        cursor.execute("SELECT DISTINCT doc_id FROM postings WHERE term = ?",(tokens,))
        rows=cursor.fetchall()
        candidate_docs.update(row[0] for row in rows)
    for doc_id in candidate_docs:
        score_list[doc_id]=score(query_tokens,doc_id)
    return sorted(score_list.items(), key=lambda x:x[1], reverse=True)[:top_k]


parser = argparse.ArgumentParser()
parser.add_argument("--query", type=str, required=True)
parser.add_argument("--mode", type=str, default="bm25")
args = parser.parse_args()

print(args.query)
print(args.mode)
