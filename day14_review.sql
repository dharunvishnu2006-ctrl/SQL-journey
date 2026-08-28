CREATE OR REPLACE FUNCTION log_status_change()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF OLD.status IS DISTINCT FROM NEW.status THEN
        INSERT INTO task_history (task_id, old_status, new_status)
        VALUES (NEW.id, OLD.status, NEW.status);
    END IF;
    RETURN NEW;
END;
$$;

CREATE TRIGGER task_status_change
AFTER UPDATE ON tasks
FOR EACH ROW
EXECUTE FUNCTION log_status_change();