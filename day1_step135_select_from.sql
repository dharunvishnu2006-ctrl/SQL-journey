SELECT actor_name AS name, country AS origin_country
FROM threat_actors;

SELECT country FROM threat_actors;

SELECT DISTINCT country FROM threat_actors;

SELECT actor_name, LENGTH(country) AS country_name_length
FROM threat_actors;