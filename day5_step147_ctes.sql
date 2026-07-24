SELECT event_type, severity
FROM events
WHERE severity > (SELECT AVG(severity) FROM events);

WITH avg_sev AS (
    SELECT AVG(severity) AS avg_val FROM events
)
SELECT event_type, severity
FROM events, avg_sev
WHERE severity > avg_val;

WITH high_sev AS (
    SELECT event_type, severity
    FROM events
    WHERE severity >= 7
),
critical_only AS (
    SELECT event_type, severity
    FROM high_sev
    WHERE severity >= 9
)
SELECT * FROM critical_only;

WITH ranked AS (
    SELECT event_type, severity,
           RANK() OVER(ORDER BY severity DESC) AS severity_rank
    FROM events
)
SELECT * FROM ranked WHERE severity_rank <= 2;