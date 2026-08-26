import sqlite3

conn = sqlite3.connect('cloudshield_v2.db')
tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print(tables)
conn.close()