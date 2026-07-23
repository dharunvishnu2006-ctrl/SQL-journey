SELECT event_type, severity,
       ROW_NUMBER() OVER(ORDER BY severity DESC) AS rank_num
FROM events;
INSERT INTO events (id, event_type, actor_id, source_ip, severity) VALUES
(4, 'Brute Force', 2, 3, 7);
SELECT event_type, severity,
       ROW_NUMBER() OVER(ORDER BY severity DESC) AS rank_num
FROM events;

SELECT event_type, severity,
       NTILE(2) OVER(ORDER BY severity DESC) AS bucket
FROM events;