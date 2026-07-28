EXPLAIN QUERY PLAN
SELECT * FROM events WHERE actor_id = 2;

CREATE INDEX idx_events_actor ON events(actor_id);
EXPLAIN QUERY PLAN
SELECT * FROM events WHERE actor_id = 2;

EXPLAIN QUERY PLAN
SELECT * FROM events WHERE severity > 6;

CREATE INDEX idx_events_covering ON events(actor_id, event_date, severity);
EXPLAIN QUERY PLAN
SELECT actor_id, event_date, severity
FROM events
WHERE actor_id = 2;