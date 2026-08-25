from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///autopilot.db')

with engine.connect() as conn:

    conn.execute(
        text('''
            INSERT INTO ml_runs (model_name, accuracy)
            VALUES (:model_name, :accuracy)
        '''),
        {
            'model_name': 'RandomForest_v2',
            'accuracy': 0.93
        }
    )

    conn.execute(
        text('''
            INSERT INTO ml_runs (model_name, accuracy)
            VALUES (:model_name, :accuracy)
        '''),
        {
            'model_name': 'XGBoost_v2',
            'accuracy': 0.96
        }
    )

    conn.commit()

with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM ml_runs'))
    rows = result.fetchall()

    for row in rows:
        print(row)

engine = create_engine(
    'postgresql://cs_user:password@localhost/cloudshield_db',
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True
)        