import sqlite3

conn = sqlite3.connect('cloudshield_v2.db')

conn.execute("""
CREATE TABLE IF NOT EXISTS threat_summary (
    id INTEGER PRIMARY KEY,
    threat_type TEXT,
    month TEXT,
    count_val INTEGER
)
""")

existing = conn.execute("SELECT COUNT(*) FROM threat_summary").fetchone()[0]
if existing == 0:
    sample_data = [
        ('malware', '2026-01', 50),
        ('malware', '2026-02', 30),
        ('phishing', '2026-01', 20),
        ('phishing', '2026-02', 40),
    ]
    conn.executemany(
        "INSERT INTO threat_summary (threat_type, month, count_val) VALUES (?, ?, ?)",
        sample_data
    )
    conn.commit()

print("Data ready.")

print("\n--- Level 1: Detail (threat_type + month) ---")
detail = conn.execute("""
    SELECT threat_type, month, SUM(count_val) as total
    FROM threat_summary
    GROUP BY threat_type, month
""").fetchall()
for row in detail:
    print(row)

print("\n--- Level 2: Subtotal (threat_type only, month = NULL) ---")
subtotal = conn.execute("""
    SELECT threat_type, NULL as month, SUM(count_val) as total
    FROM threat_summary
    GROUP BY threat_type
""").fetchall()
for row in subtotal:
    print(row)

print("\n--- Level 3: Grand Total (both = NULL) ---")
grand_total = conn.execute("""
    SELECT NULL as threat_type, NULL as month, SUM(count_val) as total
    FROM threat_summary
""").fetchall()
for row in grand_total:
    print(row)    

print("\n--- Full ROLLUP Simulation (UNION ALL) ---")
rollup_sim = conn.execute("""
    SELECT threat_type, month, SUM(count_val) as total
    FROM threat_summary
    GROUP BY threat_type, month

    UNION ALL

    SELECT threat_type, NULL as month, SUM(count_val) as total
    FROM threat_summary
    GROUP BY threat_type

    UNION ALL

    SELECT NULL as threat_type, NULL as month, SUM(count_val) as total
    FROM threat_summary

    ORDER BY threat_type, month
""").fetchall()
for row in rollup_sim:
    print(row)    