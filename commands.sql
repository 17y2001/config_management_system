CREATE USER config_user WITH PASSWORD 'yash2001';
ALTER ROLE config_user SET client_encoding TO 'utf8';
ALTER ROLE config_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE config_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE config_db TO config_user;