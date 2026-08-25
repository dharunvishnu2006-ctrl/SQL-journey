import sqlite3

with sqlite3.connect('threats.db') as conn:
 
    conn.execute('''
        CREATE TABLE IF NOT EXISTS security_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_ip TEXT NOT NULL,
            severity TEXT NOT NULL,
            event_time TEXT NOT NULL
        )
    ''')

    conn.execute(
        'INSERT INTO security_events (source_ip, severity, event_time) VALUES (?, ?, ?)',
        ('192.168.1.5', 'HIGH', '2026-08-25 10:00:00')
    )

    bulk_events = [
        ('10.0.0.1', 'CRITICAL', '2026-08-25 10:01:00'),
        ('10.0.0.2', 'LOW', '2026-08-25 10:02:00'),
        ('10.0.0.3', 'HIGH', '2026-08-25 10:03:00'),
    ]
    conn.executemany(
        'INSERT INTO security_events (source_ip, severity, event_time) VALUES (?, ?, ?)',
        bulk_events
    )

with sqlite3.connect('threats.db') as conn:
    cursor = conn.execute('SELECT * FROM security_events WHERE severity = ?', ('HIGH',))
    
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor2 = conn.execute('SELECT * FROM security_events')
    first_row = cursor2.fetchone()
    print("First row only:", first_row)