SELECT threat_description
FROM security_events
WHERE to_tsvector('english', threat_description) @@ to_tsquery('english', 'ransomware & lateral_movement');

ALTER TABLE security_events ADD COLUMN search_vector tsvector;

UPDATE security_events
SET search_vector = to_tsvector('english', threat_description);

CREATE INDEX idx_events_search ON security_events USING GIN(search_vector);

SELECT threat_description
FROM security_events
WHERE search_vector @@ to_tsquery('english', 'ransomware | phishing');

SELECT threat_description, ts_rank(search_vector, to_tsquery('english', 'ransomware & lateral_movement')) AS relevance
FROM security_events
WHERE search_vector @@ to_tsquery('english', 'ransomware & lateral_movement')
ORDER BY relevance DESC;

CREATE TRIGGER trg_update_search_vector
BEFORE INSERT OR UPDATE ON security_events
FOR EACH ROW
EXECUTE FUNCTION tsvector_update_trigger(search_vector, 'pg_catalog.english', threat_description);