CREATE OR REPLACE FUNCTION calculate_risk_score(p_severity INT, p_repeat_count INT)
RETURNS NUMERIC AS $$
BEGIN
    RETURN (p_severity * 2) + (p_repeat_count * 1.5);
END;
$$ LANGUAGE plpgsql;

SELECT calculate_risk_score(8, 3);  

CREATE OR REPLACE FUNCTION top_attackers(p_limit INT)
RETURNS TABLE(source_ip TEXT, total_events BIGINT) AS $$
BEGIN
    RETURN QUERY
    SELECT e.source_ip, COUNT(*)
    FROM security_events e
    GROUP BY e.source_ip
    ORDER BY COUNT(*) DESC
    LIMIT p_limit;
END;
$$ LANGUAGE plpgsql;
SELECT * FROM top_attackers(5);

CREATE OR REPLACE FUNCTION log_event_to_audit()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO audit_log(event_id, action, logged_at)
    VALUES (NEW.id, 'INSERT', NOW());
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_audit_security_events
AFTER INSERT ON security_events
FOR EACH ROW
EXECUTE FUNCTION log_event_to_audit();

CREATE OR REPLACE FUNCTION validate_agent_status()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.status NOT IN ('idle','busy','offline') THEN
        RAISE EXCEPTION 'Invalid agent status: %', NEW.status;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_validate_agent
BEFORE UPDATE ON agents
FOR EACH ROW
EXECUTE FUNCTION validate_agent_status();