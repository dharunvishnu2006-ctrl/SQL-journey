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
