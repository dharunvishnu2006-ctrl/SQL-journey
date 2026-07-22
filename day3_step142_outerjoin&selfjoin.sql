ALTER TABLE agents ADD COLUMN manager_id INTEGER;
UPDATE agents SET manager_id = 3 WHERE id = 1;
UPDATE agents SET manager_id = 3 WHERE id = 2;
SELECT e.agent_name AS employee, m.agent_name AS manager
FROM agents e
LEFT JOIN agents m ON e.manager_id = m.id;

SELECT a.actor_name, ip.ip_value
FROM threat_actors a
LEFT JOIN ip_addresses ip ON a.id = ip.actor_id

UNION

SELECT a.actor_name, ip.ip_value
FROM ip_addresses ip
LEFT JOIN threat_actors a ON ip.actor_id = a.id;
SELECT a.actor_name, ip.ip_value
FROM threat_actors a
LEFT JOIN ip_addresses ip ON a.id = ip.actor_id
WHERE ip.id IS NULL

UNION

SELECT a.actor_name, ip.ip_value
FROM ip_addresses ip
LEFT JOIN threat_actors a ON ip.actor_id = a.id
WHERE a.id IS NULL;