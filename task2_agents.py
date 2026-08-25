import sqlite3

with sqlite3.connect('agents.db') as conn:
    agents = [
        ('Agent-02', 'active'),
        ('Agent-03', 'idle'),
        ('Agent-04', 'busy'),
        ('Agent-05', 'active'),
        ('Agent-06', 'idle')
    ]
    conn.executemany(
        'INSERT INTO agents (name, status) VALUES (?, ?)',
        agents
    )

with sqlite3.connect('agents.db') as conn:
    cursor = conn.execute(
        'SELECT * FROM agents WHERE status = ?',
        ('active',)
    )
    rows = cursor.fetchall()
    print(rows)