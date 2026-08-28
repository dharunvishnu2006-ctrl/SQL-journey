CREATE ROLE replicator WITH REPLICATION LOGIN PASSWORD 'securepass';

pg_basebackup -h primary_host -D /var/lib/postgresql/standby_data -U replicator -P -R

CREATE PUBLICATION cve_pub FOR TABLE security_events;

CREATE SUBSCRIPTION cve_sub
CONNECTION 'host=primary_host dbname=cloudshield_db user=replicator password=securepass'
PUBLICATION cve_pub;

SELECT client_addr, state, sent_lsn, replay_lsn,
       (sent_lsn - replay_lsn) AS lag_bytes
FROM pg_stat_replication;