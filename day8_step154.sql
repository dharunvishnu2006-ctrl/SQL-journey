BEGIN;
UPDATE agents
SET status = 'busy'
WHERE id = 3;
INSERT INTO tasks (assigned_agent, description)
VALUES (3, 'Patch server');
COMMIT;