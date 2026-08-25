import sqlite3

with sqlite3.connect('autopilot.db') as conn:
    conn.execute('''
        CREATE TABLE IF NOT EXISTS ml_runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            model_name TEXT NOT NULL,
            accuracy REAL NOT NULL
        )
    ''')

try:
    with sqlite3.connect('autopilot.db') as conn:
        conn.execute(
            'INSERT INTO ml_runs (model_name, accuracy) VALUES (?, ?)',
            ('RandomForest_v1', 0.91)
        )
        conn.execute(
            'INSERT INTO ml_runs (model_name, accuracy) VALUES (?, ?)',
            ('XGBoost_v1', 0.94)
        )
        conn.execute(
            'INSERT INTO ml_runs (model_name, accuracy) VALUES (?, ?)',
            (None, 0.89)
        )
except sqlite3.IntegrityError as e:
    print("Insert failed, transaction rolled back:", e)

with sqlite3.connect('autopilot.db') as conn:
    cursor = conn.execute('SELECT * FROM ml_runs')
    rows = cursor.fetchall()
    print("Final table contents:", rows)