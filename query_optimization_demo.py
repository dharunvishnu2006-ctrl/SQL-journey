import sqlite3
import random

conn = sqlite3.connect('cloudshield_v2.db')

conn.execute("""
CREATE TABLE IF NOT EXISTS big_events (
    id INTEGER PRIMARY KEY,
    source_ip TEXT,
    event_time TEXT,
    severity INTEGER
)
""")

existing = conn.execute("SELECT COUNT(*) FROM big_events").fetchone()[0]
if existing == 0:
    ips = [f"10.0.0.{i}" for i in range(1, 51)]
    rows = []
    for i in range(5000):
        rows.append((
            random.choice(ips),
            f"2026-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
            random.randint(1, 100)
        ))
    conn.executemany(
        "INSERT INTO big_events (source_ip, event_time, severity) VALUES (?, ?, ?)",
        rows
    )
    conn.commit()

print("Rows in big_events:", conn.execute("SELECT COUNT(*) FROM big_events").fetchone()[0])

print("\n--- EXPLAIN QUERY PLAN (before index) ---")
plan = conn.execute("""
    EXPLAIN QUERY PLAN
    SELECT * FROM big_events WHERE source_ip = '10.0.0.25'
""").fetchall()
for row in plan:
    print(row)

conn.execute("CREATE INDEX IF NOT EXISTS idx_big_events_ip ON big_events(source_ip)")
conn.commit()

print("\n--- EXPLAIN QUERY PLAN (after index) ---")
plan2 = conn.execute("""
    EXPLAIN QUERY PLAN
    SELECT * FROM big_events WHERE source_ip = '10.0.0.25'
""").fetchall()
for row in plan2:
    print(row)    

import time

conn.execute("DROP INDEX IF EXISTS idx_big_events_ip")

start = time.time()
for _ in range(50):
    conn.execute("SELECT * FROM big_events WHERE source_ip = '10.0.0.25'").fetchall()
no_index_time = time.time() - start
print(f"\nTime WITHOUT index (50 runs): {no_index_time:.4f} seconds")

conn.execute("CREATE INDEX idx_big_events_ip ON big_events(source_ip)")

start = time.time()
for _ in range(50):
    conn.execute("SELECT * FROM big_events WHERE source_ip = '10.0.0.25'").fetchall()
with_index_time = time.time() - start
print(f"Time WITH index (50 runs): {with_index_time:.4f} seconds")

print(f"\nSpeedup: {no_index_time / with_index_time:.2f}x faster with index")    