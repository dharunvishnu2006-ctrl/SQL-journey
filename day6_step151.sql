INSERT INTO events (event_type, actor_id, severity, event_date)
VALUES ('  phishing  ', 3, 5, '2026-07-05');

SELECT event_type,
       UPPER(TRIM(event_type)) AS clean_event_type
FROM events
WHERE event_type = '  phishing  ';
SELECT event_type,
       actor_id,
       COALESCE(actor_id, -1) AS actor_id_display
FROM events;
SELECT event_type,
       SUBSTR(event_date, 1, 4) AS year_only,
       SUBSTR(event_date, 6, 2) AS month_only
FROM events;