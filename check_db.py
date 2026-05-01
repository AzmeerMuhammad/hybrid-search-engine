import sqlite3

conn = sqlite3.connect("data/index.db")
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM documents")
print("Documents:", cursor.fetchone()[0])
cursor.execute("SELECT COUNT(*) FROM postings")
print("Postings:", cursor.fetchone()[0])
cursor.execute("SELECT COUNT(*) FROM term_stats")
print("Term stats:", cursor.fetchone()[0])
conn.close()