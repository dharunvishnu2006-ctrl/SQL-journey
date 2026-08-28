CREATE TABLE security_events (
    id BIGSERIAL,
    event_time TIMESTAMP NOT NULL,
    source_ip INET,
    severity INT,
    threat_description TEXT
) PARTITION BY RANGE (event_time);

CREATE TABLE security_events_2025_12 PARTITION OF security_events
    FOR VALUES FROM ('2025-12-01') TO ('2026-01-01');

CREATE TABLE security_events_2026_01 PARTITION OF security_events
    FOR VALUES FROM ('2026-01-01') TO ('2026-02-01');

EXPLAIN ANALYZE
SELECT * FROM security_events
WHERE event_time BETWEEN '2026-01-01' AND '2026-01-31';    

CREATE TABLE task_logs (
    id BIGSERIAL,
    region TEXT NOT NULL,
    task_details TEXT
) PARTITION BY LIST (region);

CREATE TABLE task_logs_south PARTITION OF task_logs
    FOR VALUES IN ('South', 'Kerala', 'TamilNadu');

CREATE TABLE task_logs_north PARTITION OF task_logs
    FOR VALUES IN ('North', 'Delhi', 'Punjab');

CREATE TABLE ml_runs (
    id BIGSERIAL,
    experiment_id INT NOT NULL,
    accuracy NUMERIC
) PARTITION BY HASH (experiment_id);

CREATE TABLE ml_runs_p0 PARTITION OF ml_runs
    FOR VALUES WITH (MODULUS 8, REMAINDER 0);

CREATE TABLE ml_runs_p1 PARTITION OF ml_runs
    FOR VALUES WITH (MODULUS 8, REMAINDER 1);    

CREATE TABLE security_events_default PARTITION OF security_events DEFAULT;    