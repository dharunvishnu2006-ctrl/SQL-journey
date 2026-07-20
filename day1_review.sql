CREATE TABLE malware_samples (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file_hash TEXT NOT NULL,
    actor_id INTEGER,
    FOREIGN KEY (actor_id) REFERENCES threat_actors(id)
);