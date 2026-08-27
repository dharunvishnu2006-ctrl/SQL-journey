import sqlite3

conn = sqlite3.connect('cloudshield_v2.db')

conn.execute("""
CREATE TABLE IF NOT EXISTS dim_ip (
    ip_key INTEGER PRIMARY KEY,
    ip_address TEXT,
    country TEXT
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS dim_threat_type (
    threat_type_key INTEGER PRIMARY KEY,
    threat_name TEXT
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS fact_security_events (
    event_key INTEGER PRIMARY KEY,
    ip_key INTEGER,
    threat_type_key INTEGER,
    event_date TEXT,
    severity_score INTEGER,
    FOREIGN KEY (ip_key) REFERENCES dim_ip(ip_key),
    FOREIGN KEY (threat_type_key) REFERENCES dim_threat_type(threat_type_key)
)
""")

print("Star schema tables created.")

conn.execute("INSERT OR IGNORE INTO dim_ip (ip_key, ip_address, country) VALUES (1, '10.0.0.5', 'India')")
conn.execute("INSERT OR IGNORE INTO dim_ip (ip_key, ip_address, country) VALUES (2, '20.0.0.9', 'USA')")
conn.execute("INSERT OR IGNORE INTO dim_threat_type (threat_type_key, threat_name) VALUES (1, 'Malware')")
conn.execute("INSERT OR IGNORE INTO dim_threat_type (threat_type_key, threat_name) VALUES (2, 'Phishing')")

conn.execute("INSERT OR IGNORE INTO fact_security_events (event_key, ip_key, threat_type_key, event_date, severity_score) VALUES (1, 1, 1, '2026-01-15', 80)")
conn.execute("INSERT OR IGNORE INTO fact_security_events (event_key, ip_key, threat_type_key, event_date, severity_score) VALUES (2, 2, 2, '2026-01-16', 60)")
conn.commit()

print("\n--- Star Schema JOIN query ---")
result = conn.execute("""
    SELECT
        f.event_date,
        i.ip_address,
        i.country,
        t.threat_name,
        f.severity_score
    FROM fact_security_events f
    JOIN dim_ip i ON f.ip_key = i.ip_key
    JOIN dim_threat_type t ON f.threat_type_key = t.threat_type_key
""").fetchall()
for row in result:
    print(row)

from datetime import datetime

conn.execute("""
CREATE TABLE IF NOT EXISTS agent_status_history (
    id INTEGER PRIMARY KEY,
    agent_id TEXT,
    status TEXT,
    valid_from TEXT,
    valid_to TEXT
)
""")

def change_agent_status(agent_id, new_status):
    now = datetime.now().isoformat()
    conn.execute("""
        UPDATE agent_status_history
        SET valid_to = ?
        WHERE agent_id = ? AND valid_to IS NULL
    """, (now, agent_id))
    conn.execute("""
        INSERT INTO agent_status_history (agent_id, status, valid_from, valid_to)
        VALUES (?, ?, ?, NULL)
    """, (agent_id, new_status, now))
    conn.commit()

change_agent_status('A1', 'available')    

import time

change_agent_status('A1', 'busy')
time.sleep(1)
change_agent_status('A1', 'offline')

print("\n--- Full status history for A1 ---")
history = conn.execute("""
    SELECT agent_id, status, valid_from, valid_to
    FROM agent_status_history
    WHERE agent_id = 'A1'
    ORDER BY valid_from
""").fetchall()
for row in history:
    print(row)

print("\n--- Current status only (valid_to IS NULL) ---")
current = conn.execute("""
    SELECT agent_id, status, valid_from
    FROM agent_status_history
    WHERE agent_id = 'A1' AND valid_to IS NULL
""").fetchall()
for row in current:
    print(row)