SELECT actor_name, threat_level
FROM threat_actors
ORDER BY threat_level DESC
LIMIT 2;

SELECT actor_name, threat_level
FROM threat_actors
ORDER BY threat_level DESC
LIMIT 2 OFFSET 2;

SELECT actor_name, country, threat_level
FROM threat_actors
ORDER BY country ASC, threat_level DESC;