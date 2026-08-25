import sqlite3

with sqlite3.connect('agents.db') as conn:
    conn.execute('''
        CREATE TABLE IF NOT EXISTS agents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            status TEXT
        )
    ''')
    conn.execute(
        'INSERT INTO agents (name, status) VALUES (?, ?)',
        ('Agent-01', 'active')
    )

with sqlite3.connect('agents.db') as conn:
    cursor = conn.execute('SELECT * FROM agents')
    rows = cursor.fetchall()
    print(rows)