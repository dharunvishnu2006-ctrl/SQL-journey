ALTER TABLE events ADD COLUMN event_date DATE;
UPDATE events SET event_date = '2026-07-01' WHERE id = 1;
UPDATE events SET event_date = '2026-07-02' WHERE id = 2;
UPDATE events SET event_date = '2026-07-03' WHERE id = 3;
UPDATE events SET event_date = '2026-07-04' WHERE id = 4;

SELECT event_type, event_date, severity,
       SUM(severity) OVER(
           ORDER BY event_date
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_total
FROM events;

SELECT event_type, event_date, severity,
       SUM(severity) OVER(
           PARTITION BY STRFTIME('%Y', event_date)
           ORDER BY event_date
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS ytd_total
FROM events;