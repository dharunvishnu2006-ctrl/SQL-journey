ALTER TABLE security_events ADD COLUMN cve_metadata JSONB;

INSERT INTO security_events (id, cve_metadata)
VALUES (101, '{"cvss_score": 9.8, "exploitable": true, "vendor": "Apache"}'::jsonb);

SELECT
    cve_metadata -> 'cvss_score'  AS as_json,
    cve_metadata ->> 'cvss_score' AS as_text
FROM security_events
WHERE id = 101;

SELECT *
FROM security_events
WHERE cve_metadata @> '{"exploitable": true}';


UPDATE security_events
SET cve_metadata = jsonb_set(cve_metadata, '{cvss_score}', '9.9')
WHERE id = 101;

CREATE INDEX idx_cve_metadata ON security_events USING GIN(cve_metadata);
SELECT cve_metadata -> 'details' ->> 'patch_available' AS patch_status
FROM security_events
WHERE id = 101;