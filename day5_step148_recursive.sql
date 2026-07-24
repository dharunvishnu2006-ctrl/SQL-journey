CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    manager_id INTEGER
);

INSERT INTO employees (id, name, manager_id) VALUES
(1, 'Karthik', NULL),
(2, 'Ravi', 1),
(3, 'Priya', 1),
(4, 'Arjun', 2),
(5, 'Divya', 2),
(6, 'Suresh', 4);

WITH RECURSIVE org_chart AS (
    SELECT id, name, manager_id, 1 AS depth
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT e.id, e.name, e.manager_id, oc.depth + 1
    FROM employees e
    JOIN org_chart oc ON e.manager_id = oc.id
)
SELECT * FROM org_chart ORDER BY depth, id;

WITH RECURSIVE descendants AS (
    SELECT id, name, manager_id
    FROM employees
    WHERE id = 2

    UNION ALL

    SELECT e.id, e.name, e.manager_id
    FROM employees e
    JOIN descendants d ON e.manager_id = d.id
)
SELECT * FROM descendants WHERE id != 2;