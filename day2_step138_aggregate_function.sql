SELECT COUNT(*) AS total_rows, COUNT(threat_level) AS rows_with_level
FROM threat_actors;

SELECT SUM(threat_level) AS total_threat, AVG(threat_level) AS avg_threat
FROM threat_actors;

SELECT SUM(COALESCE(threat_level, 0)) AS total_threat, AVG(COALESCE(threat_level, 0)) AS avg_threat
FROM threat_actors;

SELECT MIN(threat_level) AS lowest_threat, MAX(threat_level) AS highest_threat
FROM threat_actors;