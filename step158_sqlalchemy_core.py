from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///autopilot.db')

with engine.connect() as conn:

    conn.execute(
        text('INSERT INTO ml_runs (model_name, accuracy) VALUES (:model_name, :accuracy)'),
        {'model_name': 'LogisticRegression_v1', 'accuracy': 0.87}
    )
    conn.commit()
with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM ml_runs'))
    rows = result.fetchall()

    for row in rows:
        print("By index:", row[0], row[1], row[2])
        print("By key:", row.model_name, row.accuracy)