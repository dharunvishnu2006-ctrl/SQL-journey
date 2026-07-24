SELECT event_type, severity,
       FIRST_VALUE(severity) OVER(ORDER BY id) AS first_severity
FROM events;
SELECT event_type, severity,
       LAST_VALUE(severity) OVER(ORDER BY id) AS last_severity_wrong
FROM events;
SELECT event_type, severity,
       LAST_VALUE(severity) OVER(
           ORDER BY id
           ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
       ) AS last_severity
FROM events;
SELECT event_type, severity,
       FIRST_VALUE(severity) OVER(ORDER BY id) AS baseline_severity,
       severity - FIRST_VALUE(severity) OVER(ORDER BY id) AS delta_from_baseline
FROM events;