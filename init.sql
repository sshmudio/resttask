CREATE USER postgres;
CREATE DATABASE postgres;
GRANT ALL PRIVILEGES ON DATABASE postgres TO postgres;
CREATE DATABASE test_psqldb;
GRANT ALL PRIVILEGES ON DATABASE test_psqldb TO postgres;
