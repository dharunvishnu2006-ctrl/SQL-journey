import sqlite3

conn = sqlite3.connect('cloudshield_v2.db')

conn.execute("""
CREATE TABLE IF NOT EXISTS threat_scores (
    id INTEGER PRIMARY KEY,
    ip TEXT,
    severity_score INTEGER
)
""")

existing = conn.execute("SELECT COUNT(*) FROM threat_scores").fetchone()[0]
if existing == 0:
    sample_data = [
        ('1.1.1.1', 20),
        ('2.2.2.2', 45),
        ('3.3.3.3', 60),
        ('4.4.4.4', 75),
        ('5.5.5.5', 95),
    ]
    conn.executemany(
        "INSERT INTO threat_scores (ip, severity_score) VALUES (?, ?)",
        sample_data
    )
    conn.commit()

print("Data ready.")

print("\n--- PERCENT_RANK and CUME_DIST ---")
result = conn.execute("""
    SELECT
        ip,
        severity_score,
        PERCENT_RANK() OVER (ORDER BY severity_score) AS pct_rank,
        CUME_DIST() OVER (ORDER BY severity_score) AS cume_dist
    FROM threat_scores
    ORDER BY severity_score
""").fetchall()
for row in result:
    print(row)

conn.execute("""
CREATE TABLE IF NOT EXISTS agent_tasks (
    id INTEGER PRIMARY KEY,
    agent_id TEXT,
    status TEXT,
    task_date TEXT
)
""")

existing2 = conn.execute("SELECT COUNT(*) FROM agent_tasks").fetchone()[0]
if existing2 == 0:
    sample_tasks = [
        ('A1', 'success', '2026-01'),
        ('A1', 'failed', '2026-01'),
        ('A1', 'success', '2026-02'),
        ('A2', 'success', '2026-01'),
        ('A2', 'success', '2026-02'),
    ]
    conn.executemany(
        "INSERT INTO agent_tasks (agent_id, status, task_date) VALUES (?, ?, ?)",
        sample_tasks
    )
    conn.commit()

print("\n--- FILTER clause: success count per agent ---")
result2 = conn.execute("""
    SELECT
        agent_id,
        task_date,
        SUM(CASE WHEN status = 'success' THEN 1 ELSE 0 END) AS success_count
    FROM agent_tasks
    GROUP BY agent_id, task_date
""").fetchall()
for row in result2:
    print(row)    

print("\n--- PIVOT: agents as rows, months as columns ---")
pivot_result = conn.execute("""
    SELECT
        agent_id,
        SUM(CASE WHEN task_date = '2026-01' THEN 1 ELSE 0 END) AS jan_tasks,
        SUM(CASE WHEN task_date = '2026-02' THEN 1 ELSE 0 END) AS feb_tasks
    FROM agent_tasks
    GROUP BY agent_id
""").fetchall()
for row in pivot_result:
    print(row)    