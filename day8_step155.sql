CREATE DATABASE sentinel_db;
CREATE USER sentinel_user WITH PASSWORD 'sentinel456';
GRANT ALL PRIVILEGES ON DATABASE sentinel_db TO sentinel_user;