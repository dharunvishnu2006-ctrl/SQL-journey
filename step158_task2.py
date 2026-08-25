from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///autopilot.db')

with engine.connect() as conn:
    conn.execute(
        text('''
            INSERT INTO ml_runs (model_name, accuracy)
            VALUES (:model_name, :accuracy)
        '''),
        {
            'model_name': 'RandomForest_v1',
            'accuracy': 0.92
        }
    )

    conn.commit()

with engine.connect() as conn:
    result = conn.execute(
        text('''
            SELECT * FROM ml_runs
            WHERE accuracy > :threshold
        '''),
        {'threshold': 0.90}
    )

    rows = result.fetchall()

    for row in rows:
        print(row.model_name, row.accuracy)