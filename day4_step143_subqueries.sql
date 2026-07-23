ALTER TABLE events ADD COLUMN severity INTEGER;
UPDATE events SET severity = 9 WHERE id = 1;
UPDATE events SET severity = 4 WHERE id = 2;
UPDATE events SET severity = 7 WHERE id = 3;
SELECT event_type, severity
FROM events
WHERE severity > (SELECT AVG(severity) FROM events);
SELECT event_type, actor_id
FROM events
WHERE actor_id IN (SELECT id FROM threat_actors WHERE country = 'Russia');

SELECT event_type, actor_id
FROM events e
WHERE EXISTS (
    SELECT 1 FROM threat_actors a
    WHERE a.id = e.actor_id AND a.country = 'Russia'
);