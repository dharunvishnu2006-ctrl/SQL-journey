SELECT event_type, severity,
       LAG(severity, 1, 0) OVER(ORDER BY id) AS prev_severity
FROM events;
SELECT event_type, severity,
       LAG(severity, 1, severity) OVER(ORDER BY id) AS prev_severity,
       ROUND((severity - LAG(severity, 1, severity) OVER(ORDER BY id)) * 100.0 
             / LAG(severity, 1, severity) OVER(ORDER BY id), 2) AS pct_change
FROM events;
SELECT event_type, severity,
       LAG(severity, 1, severity) OVER(ORDER BY id) AS prev_severity,
       CASE 
           WHEN severity > 2 * LAG(severity, 1, severity) OVER(ORDER BY id) 
           THEN 'ANOMALY SPIKE'
           ELSE 'normal'
       END AS anomaly_flag
FROM events;