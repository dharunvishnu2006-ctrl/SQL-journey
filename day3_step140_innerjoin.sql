INSERT INTO agents (id, agent_name, status) VALUES
(1, 'Agent Ravi', 'active'),
(2, 'Agent Priya', 'offline'),
(3, 'Agent Karthik', 'active');

INSERT INTO tasks (id, task_name, assigned_agent) VALUES
(1, 'Investigate Alert 401', 1),
(2, 'Patch Server', 2),
(3, 'Review Logs', 1),
(4, 'Unassigned Cleanup', NULL);

SELECT t.task_name, ag.agent_name, ag.status
FROM tasks t
INNER JOIN agents ag ON t.assigned_agent = ag.id;

CREATE TABLE events (
    id INTEGER PRIMARY KEY,
    event_type TEXT,
    actor_id INTEGER,
    source_ip INTEGER,
    FOREIGN KEY (actor_id) REFERENCES threat_actors(id),
    FOREIGN KEY (source_ip) REFERENCES ip_addresses(id)
);

INSERT INTO ip_addresses (id, ip_value, actor_id) VALUES
(1, '103.21.45.10', 1),
(2, '45.9.12.200', 3),
(3, '198.51.100.7', 2);

INSERT INTO events (id, event_type, actor_id, source_ip) VALUES
(1, 'Ransomware', 1, 1),
(2, 'Phishing', 3, 2),
(3, 'DDoS', 2, 3);

SELECT e.event_type, a.actor_name, a.country, ip.ip_value
FROM events e
JOIN threat_actors a ON e.actor_id = a.id
JOIN ip_addresses ip ON e.source_ip = ip.id;