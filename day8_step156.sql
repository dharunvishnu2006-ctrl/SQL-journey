INSERT INTO threat_events (source_ip, cve_metadata)
VALUES (
    '10.0.0.5',
    '{"cve_id": "CVE-2025-9999", "cvss_score": 7.5, "exploitable": false}'
)
RETURNING id;