SELECT country, COUNT(*) AS actor_count
FROM threat_actors
GROUP BY country;

SELECT country, COUNT(*) AS actor_count
FROM threat_actors
GROUP BY country
HAVING COUNT(*) > 1;

SELECT country, COUNT(*) AS actor_count
FROM threat_actors
WHERE threat_level > 5
GROUP BY country
HAVING COUNT(*) >= 1;