CREATE TABLE threat_actors (
    id SERIAL PRIMARY KEY,
    actor_name VARCHAR(100) NOT NULL,
    country VARCHAR(50)
);

CREATE TABLE ip_addresses (
    id SERIAL PRIMARY KEY,
    ip_value VARCHAR(45) NOT NULL,
    actor_id INT REFERENCES threat_actors(id)
);

INSERT INTO threat_actors (actor_name, country)
VALUES ('APT29', 'Russia');

INSERT INTO threat_actors (actor_name, country)
VALUES ('Lazarus', 'North Korea');

INSERT INTO ip_addresses (ip_value, actor_id)
VALUES ('45.33.12.1', 1);

INSERT INTO ip_addresses (ip_value, actor_id)
VALUES ('45.33.12.5', 1);

INSERT INTO ip_addresses (ip_value, actor_id)
VALUES ('103.85.24.9', 2);

SELECT t.actor_name, t.country, i.ip_value
FROM threat_actors t, ip_addresses i
WHERE t.id = i.actor_id;