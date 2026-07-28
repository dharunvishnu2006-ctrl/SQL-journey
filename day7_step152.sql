SELECT event_type, severity,
       CASE
           WHEN severity > 8 THEN 'CRITICAL'
           WHEN severity > 5 THEN 'HIGH'
           ELSE 'LOW'
       END AS threat_label
FROM events;

SELECT
    SUM(CASE WHEN severity > 8 THEN 1 ELSE 0 END) AS critical_count,
    SUM(CASE WHEN severity > 5 AND severity <= 8 THEN 1 ELSE 0 END) AS high_count,
    SUM(CASE WHEN severity <= 5 THEN 1 ELSE 0 END) AS low_count
FROM events;

SELECT event_type, severity,
       CASE
           WHEN severity > 8 THEN 'CRITICAL'
           WHEN severity > 5 THEN 'HIGH'
           ELSE 'LOW'
       END AS threat_label
FROM events
ORDER BY
    CASE
        WHEN severity > 8 THEN 1
        WHEN severity > 5 THEN 2
        ELSE 3
    END;

SELECT
    STRFTIME('%Y-%m', event_date) AS month,
    SUM(CASE WHEN event_type = 'Ransomware' THEN 1 ELSE 0 END) AS ransomware_count,
    SUM(CASE WHEN event_type = 'Phishing' THEN 1 ELSE 0 END) AS phishing_count,
    SUM(CASE WHEN event_type = 'DDoS' THEN 1 ELSE 0 END) AS ddos_count,
    SUM(CASE WHEN event_type = 'Brute Force' THEN 1 ELSE 0 END) AS brute_force_count
FROM events
GROUP BY STRFTIME('%Y-%m', event_date);    