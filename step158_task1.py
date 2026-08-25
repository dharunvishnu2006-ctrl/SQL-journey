from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///autopilot.db')

with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM ml_runs'))
    rows = result.fetchall()

    for row in rows:
        print(row[0], row[1], row[2])