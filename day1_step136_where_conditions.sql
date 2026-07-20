
SELECT actor_name, country
FROM threat_actors
WHERE country = 'Russia' OR country = 'North Korea';

SELECT actor_name, country
FROM threat_actors
WHERE country IN ('Russia', 'North Korea');

ALTER TABLE threat_actors ADD COLUMN threat_level INTEGER;

UPDATE threat_actors SET threat_level = 9 WHERE actor_name = 'APT29';
UPDATE threat_actors SET threat_level = 5 WHERE actor_name = 'Lazarus';
UPDATE threat_actors SET threat_level = 7 WHERE actor_name = 'Fancy Bear';

SELECT actor_name, threat_level
FROM threat_actors
WHERE threat_level BETWEEN 6 AND 9;

SELECT actor_name, country
FROM threat_actors
WHERE actor_name LIKE 'Fancy%';

INSERT INTO threat_actors (actor_name, country) VALUES ('Unknown Actor', 'Unknown');

SELECT actor_name, threat_level
FROM threat_actors
WHERE threat_level IS NULL;