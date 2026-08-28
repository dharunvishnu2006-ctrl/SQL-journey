from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://cs_user:password@localhost/cloudshield_db",
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,
    pool_recycle=3600
)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM security_events WHERE id = :id"), {"id": 101})

[databases]
cloudshield_db = host=localhost port=5432 dbname=cloudshield_db

[pgbouncer]
pool_mode = transaction
max_client_conn = 200
default_pool_size = 10   