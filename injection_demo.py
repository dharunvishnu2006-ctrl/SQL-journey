import sqlite3
from sqlalchemy import create_engine, text

conn = sqlite3.connect('cloudshield_v2.db')

conn.execute("""
CREATE TABLE IF NOT EXISTS demo_users (
    id INTEGER PRIMARY KEY,
    username TEXT
)
""")
conn.execute("INSERT INTO demo_users (username) VALUES ('ramesh')")
conn.execute("INSERT INTO demo_users (username) VALUES ('priya')")
conn.commit()

def vulnerable_lookup(user_input):
    query = f"SELECT * FROM demo_users WHERE username = '{user_input}'"
    print("Executing query:", query)
    result = conn.execute(query).fetchall()
    return result

print(vulnerable_lookup("ramesh"))

malicious_input = "x' OR '1'='1"
print(vulnerable_lookup(malicious_input))

def safe_lookup(user_input):
    query = "SELECT * FROM demo_users WHERE username = ?"
    print("Executing query:", query, "with param:", user_input)
    result = conn.execute(query, (user_input,)).fetchall()
    return result

print(safe_lookup("x' OR '1'='1"))

engine = create_engine('sqlite:///cloudshield_v2.db')

malicious_input = "x' OR '1'='1"

with engine.connect() as conn2:
    result = conn2.execute(
        text("SELECT * FROM demo_users WHERE username = :name"),
        {"name": malicious_input}
    ).fetchall()
    print("ORM-safe result:", result)