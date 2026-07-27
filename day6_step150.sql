SELECT event_type, event_date, severity
FROM events
WHERE event_date >= DATE('2026-07-04', '-7 days');

SELECT event_type,
       event_date,
       STRFTIME('%Y-%m', event_date) AS event_month
FROM events;
ALTER TABLE events ADD COLUMN resolved_date DATE;
UPDATE events SET resolved_date = '2026-07-03' WHERE id = 1;
UPDATE events SET resolved_date = '2026-07-02' WHERE id = 2;
UPDATE events SET resolved_date = '2026-07-06' WHERE id = 3;
UPDATE events SET resolved_date = '2026-07-05' WHERE id = 4;

SELECT event_type, event_date, resolved_date,
       JULIANDAY(resolved_date) - JULIANDAY(event_date) AS days_to_resolve
FROM events;
SELECT event_type, event_date,
       DATETIME(event_date, '+5 hours', '+30 minutes') AS event_date_ist
FROM events;