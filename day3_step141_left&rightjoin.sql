SELECT t.task_name, ag.agent_name, ag.status
FROM tasks t
LEFT JOIN agents ag ON t.assigned_agent = ag.id;

SELECT t.task_name
FROM tasks t
LEFT JOIN agents ag ON t.assigned_agent = ag.id
WHERE ag.id IS NULL;

INSERT INTO ip_addresses (id, ip_value, actor_id) VALUES
(4, '8.8.8.8', NULL);

SELECT ip.ip_value, ip.actor_id, e.event_type
FROM ip_addresses ip
LEFT JOIN events e ON ip.id = e.source_ip;

SELECT ip.ip_value
FROM ip_addresses ip
LEFT JOIN events e ON ip.id = e.source_ip
WHERE e.id IS NULL;